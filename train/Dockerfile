# PHASE-5.md task 5.3's training image.
#
# NVIDIA's PyTorch build, not PyPI's: like vLLM (AGENTS.md), sm_121 support
# arrives through NVIDIA's containers, and 26.08 matches the vLLM image's
# release so both share one CUDA and driver expectation. Pinned by digest per
# docs/security.md's supply chain section; the digest is recorded in
# train/.container-digest.
FROM nvcr.io/nvidia/pytorch:26.08-py3@sha256:3becd068f49bd2ad38f90db5f9a4803019a76933a24e63d821376c44e7a9200a

# requirements.lock is every package pip added or changed when resolving
# requirements.txt (the top-level names) inside this image, frozen and
# committed.
#
# The image's pip constraint file (/etc/pip/constraint.txt) is empty in 26.08,
# so nothing stops a dependency from replacing NVIDIA's torch with a PyPI wheel
# that has no sm_121 kernels. It did not happen when the lock was resolved, and
# the check below fails the build if it ever does.
COPY requirements.lock /tmp/requirements.lock
RUN pip install --no-cache-dir -r /tmp/requirements.lock \
 && python -c "import torch; assert 'nv26' in torch.__version__, torch.__version__"

WORKDIR /work
