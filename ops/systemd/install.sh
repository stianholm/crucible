#!/usr/bin/env bash
# Install crucible's systemd user units and enable their timers. The service
# files say @REPO@ where the repository path goes; this writes copies with the
# real path filled in, so re-run it after editing a unit. Needs lingering
# (loginctl enable-linger), or timers stop at logout and miss reboots.
set -euo pipefail
cd "$(dirname "$0")"
REPO=$(cd ../.. && pwd)
mkdir -p ~/.config/systemd/user
for u in crucible-*.service crucible-*.timer; do
  # Older installs linked these files; remove the link so sed never writes through it.
  rm -f ~/.config/systemd/user/"$u"
  sed "s|@REPO@|$REPO|g" "$u" > ~/.config/systemd/user/"$u"
done
systemctl --user daemon-reload
for t in crucible-*.timer; do systemctl --user enable --now "$t"; done
systemctl --user list-timers 'crucible-*'
