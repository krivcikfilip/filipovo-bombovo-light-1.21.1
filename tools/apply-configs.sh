#!/usr/bin/env bash
# Přidá shaderpack, přepočítá index a označí "preserve" soubory,
# které si hráč může upravit (packwiz je pak při updatu nepřepíše).
set -euo pipefail
cd "$(dirname "$0")/.."
PW="${PACKWIZ:-$(command -v packwiz || echo "$HOME/go/bin/packwiz")}"

# 1) Complementary Unbound (stejný shader jako ve starém modpacku)
if ! ls shaderpacks/*.pw.toml >/dev/null 2>&1; then
  "$PW" -y mr add complementary-unbound
fi

# Pokud packwiz stáhl jinou verzi než r5.9.3, přejmenuj nastavení shaderu
SP=$(grep -h '^filename' shaderpacks/*.pw.toml | head -1 | sed 's/.*= *"\(.*\)"/\1/')
if [ -n "$SP" ] && [ "$SP" != "ComplementaryUnbound_r5.9.3.zip" ]; then
  mv shaderpacks/ComplementaryUnbound_r5.9.3.zip.txt "shaderpacks/$SP.txt"
  sed -i '' "s/^shaderPack=.*/shaderPack=$SP/" config/iris.properties
fi
echo "Shaderpack: $SP"

# 2) Index
"$PW" refresh

# 3) preserve = true pro hráčská nastavení
PRESERVE="options.txt servers.dat config/iris.properties config/xaerohud.txt \
config/xaero/minimap/client.cfg config/xaero/minimap/profiles/default.cfg \
config/xaero/minimap/profiles/info_display_config/default.cfg.txt \
config/xaero/world-map/client.cfg config/xaero/world-map/profiles/default.cfg \
shaderpacks/$SP.txt"
awk -v list="$PRESERVE" '
  BEGIN { n = split(list, a, " "); for (i = 1; i <= n; i++) p["file = \"" a[i] "\""] = 1 }
  /^\[\[files\]\]/ { inb = 0 }
  /^preserve *=/ { if (inb) next }
  { print }
  ($0 in p) { print "preserve = true"; inb = 1 }
' index.toml > index.toml.tmp && mv index.toml.tmp index.toml
"$PW" refresh

echo "--- preserve:"; grep -B1 '^preserve' index.toml | grep '^file'
