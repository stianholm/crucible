# Run report — capability_case / e91960cc-51a9-4e2b-8d5d-49c4b0f4e395

## Parameters

- Budget: {'max_iterations': 50, 'max_tokens': 2000000, 'max_wall_s': 14400, 'patience': 12, 'actual_iterations': 6, 'actual_tokens': 14625, 'actual_wall_s': 15524.2, 'stop_reason': 'max_wall_s (14400)'}
- Baseline scalar: 0.3902

## Health signals

| Signal | Value | Status |
|---|---|---|
| Accept rate | 33.3% | OK |
| Parse failures | 0.0% | OK |
| Inadmissible | 0.0% | OK |
| Tokens per iteration | flat | OK |
| Total iterations | 6 | OK |
| Accepted candidates | 2 | OK |

## Score trajectory

```
n=  0  scalar=0.0000  accepted=False  incumbent_best=0.3902
n=  1  scalar=0.6681  accepted=True  incumbent_best=0.6681
n=  2  scalar=0.7836  accepted=True  incumbent_best=0.7836
n=  3  scalar=0.0000  accepted=False  incumbent_best=0.7836
n=  4  scalar=0.0000  accepted=False  incumbent_best=0.7836
n=  5  scalar=0.0000  accepted=False  incumbent_best=0.7836
```

## Accepted candidates, in full

### n=1 (scalar 0.6681, parent d1e0d5e9c75c5ddf)

detail: `{'failed_checks': "absent-failure_mode_analysis-01 [floor_correct]: floor requires reject (evidence dimension 'failure_mode_analysis' is entirely absent, not just thin (p.25)); got 'needs_more_evidence'\nabsent-failure_mode_analysis-02 [floor_correct]: floor requires reject (evidence dimension 'failure_mode_analysis' is entirely absent, not just thin (p.25)); got 'needs_more_evidence'\nmixed-02 [floor_correct]: floor passes (no disqualifier); got 'reject' — 'reject' would be wrong here\nmixed-02 [judge]: BAND: 0"}`

### n=2 (scalar 0.7836, parent 04b13bb44817eef5)

detail: `{'failed_checks': "antipattern-governlater-03 [floor_correct]: floor requires reject (anti-pattern 'we_will_govern_it_later': governance for the relaxation was not defined upfront (p.29)); got 'sound'"}`

