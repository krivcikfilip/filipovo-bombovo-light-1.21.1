#!/usr/bin/env bash
# Nainstaluje questy z tools/quests do packu (config/ftbquests/quests), přepočítá index a pushne.
set -euo pipefail
cd "$(dirname "$0")/.."
PW="${PACKWIZ:-$(command -v packwiz || echo "$HOME/go/bin/packwiz")}"
git pull --ff-only
rm -rf config/ftbquests/quests
mkdir -p config/ftbquests
cp -R tools/quests config/ftbquests/quests
"$PW" refresh
git add -A
git commit -m "FTB Quests: 27 tutoriálových kapitol, 447 questů"
git push
echo "HOTOVO - restartuj server, questy se načtou při startu."
