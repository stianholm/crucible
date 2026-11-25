# The sandbox runner image. Built from a pinned base, kept minimal — a
# Python interpreter and nothing else. Every tool present in this image is
# a tool a candidate can invoke. See docs/security.md's supply chain section.
#
# Pin by digest (see .sandbox-runner-digest, written by build.sh) and
# rebuild deliberately, not on every base-image update.
FROM python@sha256:2f17fc044b579bab302c2e8054d3a686e2cb9a83de48e70534b94cd8ebbe06a9

# No pip installs, no shell utilities beyond what the base already has.
# Candidates run as an unprivileged, nologin user — never root inside the
# container, on top of --cap-drop ALL and --security-opt no-new-privileges
# at the docker-run level.
RUN useradd --no-create-home --shell /usr/sbin/nologin sandboxrunner
USER sandboxrunner

COPY --chown=sandboxrunner:sandboxrunner run_candidate.py /run_candidate.py

ENTRYPOINT ["python", "/run_candidate.py"]
