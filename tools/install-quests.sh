#!/usr/bin/env bash
# Sestaví questy ze zdrojů (tools/quests-src/areas/*.py), zvaliduje je a nainstaluje do packu
# (config/ftbquests/quests + kopie v tools/quests) a přepočítá packwiz index.
# Commit a push dělej ručně až po kontrole.
set -euo pipefail
cd "$(dirname "$0")/.."
PW="${PACKWIZ:-$(command -v packwiz || echo "$HOME/go/bin/packwiz")}"
python3 tools/quests-src/build.py --install
"$PW" refresh
echo "HOTOVO - zkontroluj git diff, commitni a pushni; po restartu serveru se questy načtou."
