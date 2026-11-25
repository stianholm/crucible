"""PHASE-5.md task 5.3: train one LoRA adapter on a harvested training set.

Runs inside the training image (train/Dockerfile), with the proposer stopped:

    python -m train.distil --data data/train/<stamp>.jsonl --out adapters/<stamp> \\
                           --deadline 2026-10-17T06:00

Always from the stock base, never from a previous adapter (task 5.3). One
epoch, rank 16, attention projections only.

Three choices the phase document leaves open, made here:
- **Loss on the response only.** The prompt/response boundary is found by
  rendering the same conversation with and without the assistant turn, so it
  does not depend on knowing gpt-oss's special-token markers.
- **Per-example weights** (task 5.1's magnitude weighting) scale each
  example's loss. TRL's SFT trainer has no per-example weight; at a batch size
  of 1 a small Trainer subclass does it exactly.
- **The analysis channel is trained on by default** (`thinking` in the
  harvest). gpt-oss always reasons before it answers, and training on the
  final text alone would teach a turn shape the model never produces.
  `--no-thinking` drops it.

The deadline is a hard stop (task 5.2: an overrun costs a day of
generations). A run stopped by it still saves, but `train_meta.json` records
`complete: false`, and the nightly job must not load such an adapter.
"""

from __future__ import annotations

import argparse
import json
import math
import time
from datetime import datetime
from pathlib import Path

# Unsloth patches transformers on import, so it comes first.
from unsloth import FastLanguageModel  # noqa: I001

import torch
from transformers import Trainer, TrainerCallback, TrainingArguments

BASE = "openai/gpt-oss-120b"
MAX_SEQ = 8192
TARGETS = ["q_proj", "k_proj", "v_proj", "o_proj"]


def load_rows(path: Path, thinking: bool) -> list[dict]:
    rows = []
    for line in path.read_text().splitlines():
        r = json.loads(line)
        if not thinking:
            r["messages"][-1].pop("thinking", None)
        rows.append(r)
    return rows


def encode(tok, row: dict) -> dict | None:
    """input_ids and labels with the prompt masked out, or None if too long."""
    msgs = row["messages"]
    prompt = tok.apply_chat_template(msgs[:-1], tokenize=False, add_generation_prompt=True)
    full = tok.apply_chat_template(msgs, tokenize=False)
    if not full.startswith(prompt):
        # The template rendered the shared prefix differently with and without
        # the final turn, so the boundary cannot be trusted. Fail loudly rather
        # than train on the wrong tokens.
        raise ValueError("chat template prefix mismatch; response-only masking would be wrong")
    p_ids = tok(prompt, add_special_tokens=False)["input_ids"]
    ids = tok(full, add_special_tokens=False)["input_ids"]
    if len(ids) > MAX_SEQ:
        return None
    labels = [-100] * len(p_ids) + ids[len(p_ids):]
    return {"input_ids": ids, "labels": labels, "weight": float(row.get("weight", 1.0))}


class WeightedTrainer(Trainer):
    """Scales each example's loss by its harvest weight. Batch size 1 only.

    num_items_in_batch has to reach the model. With it, the model returns its
    summed token loss over the response tokens of the whole accumulated batch,
    and the Trainer skips its own division by gradient_accumulation_steps.
    Dropping it, as the first version did, gave per-example means that the
    Trainer still did not divide, so loss and gradients were 16 times too
    large (smoke test 2026-10-16: logged loss ~120, grad norm ~125)."""

    def compute_loss(self, model, inputs, return_outputs=False, num_items_in_batch=None):
        weight = inputs.pop("weight")
        out = model(**inputs, num_items_in_batch=num_items_in_batch)
        loss = out.loss * weight.to(out.loss.dtype).mean()
        return (loss, out) if return_outputs else loss


def collate(batch: list[dict]) -> dict:
    assert len(batch) == 1, "WeightedTrainer assumes per_device_train_batch_size=1"
    b = batch[0]
    return {"input_ids": torch.tensor([b["input_ids"]]), "attention_mask": torch.ones(1, len(b["input_ids"]), dtype=torch.long),
            "labels": torch.tensor([b["labels"]]), "weight": torch.tensor([b["weight"]])}


class Deadline(TrainerCallback):
    def __init__(self, deadline: datetime | None):
        self.deadline = deadline
        self.hit = False

    def on_step_end(self, args, state, control, **kw):
        if self.deadline and datetime.now() >= self.deadline:
            self.hit = True
            control.should_training_stop = True


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="python -m train.distil")
    ap.add_argument("--data", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--base", default=BASE)
    ap.add_argument("--deadline", type=datetime.fromisoformat, default=None)
    ap.add_argument("--no-thinking", dest="thinking", action="store_false")
    ap.add_argument("--max-steps", type=int, default=-1, help="smoke tests only")
    args = ap.parse_args(argv)

    t0 = time.time()
    model, tok = FastLanguageModel.from_pretrained(args.base, max_seq_length=MAX_SEQ, load_in_4bit=True, dtype=None)
    model = FastLanguageModel.get_peft_model(
        model, r=16, lora_alpha=16, lora_dropout=0.05, target_modules=TARGETS,
        use_gradient_checkpointing="unsloth", random_state=0,
    )
    load_s = time.time() - t0

    rows = load_rows(args.data, args.thinking)
    encoded = [e for e in (encode(tok, r) for r in rows) if e is not None]
    dropped = len(rows) - len(encoded)

    deadline = Deadline(args.deadline)
    targs = TrainingArguments(
        output_dir=str(args.out / "checkpoints"),
        per_device_train_batch_size=1,
        gradient_accumulation_steps=16,
        num_train_epochs=1,  # one pass: more epochs is how you overfit and forget
        max_steps=args.max_steps,
        learning_rate=1e-4,
        lr_scheduler_type="cosine",
        warmup_steps=0.03,  # transformers 5 removed warmup_ratio; a float below 1 is a ratio
        optim="adamw_8bit",
        logging_steps=1,
        save_strategy="no",
        report_to=[],
        seed=0,
        bf16=True,
        remove_unused_columns=False,
    )
    trainer = WeightedTrainer(model=model, args=targs, train_dataset=encoded, data_collator=collate, callbacks=[deadline])
    result = trainer.train()

    args.out.mkdir(parents=True, exist_ok=True)
    model.save_pretrained(str(args.out))
    tok.save_pretrained(str(args.out))
    losses = [h["loss"] for h in trainer.state.log_history if "loss" in h]
    meta = {
        "base": args.base,
        "data": str(args.data),
        "data_manifest": json.loads(args.data.with_suffix(".manifest.json").read_text())
        if args.data.with_suffix(".manifest.json").exists() else None,
        "examples": len(encoded),
        "dropped_over_max_seq": dropped,
        "thinking": args.thinking,
        "lora": {"r": 16, "alpha": 16, "dropout": 0.05, "targets": TARGETS},
        "steps": trainer.state.global_step,
        "planned_steps": math.ceil(len(encoded) / 16) if args.max_steps < 0 else args.max_steps,
        "losses": losses,
        "complete": not deadline.hit,
        "load_s": round(load_s, 1),
        "train_s": round(result.metrics.get("train_runtime", 0.0), 1),
        "peak_mem_gb": round(torch.cuda.max_memory_allocated() / 2**30, 1),
    }
    (args.out / "train_meta.json").write_text(json.dumps(meta, indent=1))
    print(json.dumps({k: v for k, v in meta.items() if k not in ("losses", "data_manifest")}, indent=1))
    return 0 if meta["complete"] else 3


if __name__ == "__main__":
    raise SystemExit(main())
