"""Anglické názvy biomů, entit a dimenzí (z lang souborů modů) -> tools/registry/names_en.tsv.
Používá validátor questů: vlastní jména se v questech nepřekládají.
  python3 -I tools/refdata/names_en.py <db> <registry_dir>"""
import json, os, sys, glob

db, reg = sys.argv[1], sys.argv[2]
lang = {}
for f in sorted(glob.glob(os.path.join(db, "assets", "*", "lang", "en_us.json"))):
    try:
        lang.update(json.load(open(f, encoding="utf-8")))
    except Exception:
        pass
for f in sorted(glob.glob(os.path.join(db, "assets", "minecraft", "lang", "en_us.json"))):
    lang.update(json.load(open(f, encoding="utf-8")))
# Dimenze bez lang klíče: jak je hráči znají (název modu / běžný název)
DIMS = {"minecraft:overworld": "Overworld", "minecraft:the_nether": "Nether", "minecraft:the_end": "End",
        "twilightforest:twilight_forest": "Twilight Forest", "aether:the_aether": "Aether"}
rows = []
for kind, fn in (("biome", "biomes.txt"), ("entity", "entities.txt"), ("dimension", "dimensions.txt")):
    for rid in open(os.path.join(reg, fn)).read().split():
        ns, path = rid.split(":", 1)
        name = DIMS.get(rid) if kind == "dimension" else None
        name = name or lang.get(f"{kind}.{ns}.{path}")
        if kind == "dimension" and not name:
            name = lang.get(f"dimension.{ns}.{path}")
        if name:
            rows.append(f"{kind}\t{rid}\t{name}")
open(os.path.join(reg, "names_en.tsv"), "w", encoding="utf-8").write("\n".join(rows) + "\n")
print("names_en.tsv:", len(rows))
