#!/usr/bin/env bash
# Obnoví referenční data z jarů modů (pro psaní a kontrolu questů, analýzu receptů).
#   tools/refdata/rebuild.sh [cílová_složka]   (výchozí: /tmp/bombovo-refdata)
# Výsledek: <cíl>/jars (všechny serverové jary + vanilla 1.21.1), <cíl>/db (recepty, tagy, lang, průvodci,
# loot tables, advancementy, worldgen) a <cíl>/db/index (items.tsv, recipes.tsv, advancement_titles.tsv…).
# Aktualizuje i tools/registry/obtainable.txt (předměty s funkčním receptem nebo lootem).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
OUT="${1:-/tmp/bombovo-refdata}"
mkdir -p "$OUT/jars"
python3 -I "$ROOT/tools/refdata/dl.py" "$ROOT/mods" "$OUT/jars"
cp "$ROOT"/mods/*.jar "$OUT/jars/" 2>/dev/null || true   # vlastní jary přímo v repu (Fossils)
if [ ! -f "$OUT/jars/zz_minecraft-1.21.1-client.jar" ]; then
  M=$(curl -s https://piston-meta.mojang.com/mc/game/version_manifest_v2.json | python3 -c "import json,sys;print([v['url'] for v in json.load(sys.stdin)['versions'] if v['id']=='1.21.1'][0])")
  U=$(curl -s "$M" | python3 -c "import json,sys;print(json.load(sys.stdin)['downloads']['client']['url'])")
  curl -sfL -o "$OUT/jars/zz_minecraft-1.21.1-client.jar" "$U"
fi
rm -rf "$OUT/db"
python3 -I "$ROOT/tools/refdata/extract.py" "$OUT/jars" "$OUT/db"
python3 -I "$ROOT/tools/refdata/index.py" "$OUT/db" "$ROOT/tools/registry/items.txt"
python3 -I "$ROOT/tools/refdata/obtainable2.py" "$OUT/jars" "$ROOT/tools/registry/items.txt" "$ROOT/tools/registry/obtainable.txt"
python3 -I "$ROOT/tools/refdata/names_en.py" "$OUT/db" "$ROOT/tools/registry"
cp "$OUT/db/index/items.tsv" "$ROOT/tools/registry/item_names.tsv"
echo "Hotovo: $OUT"
