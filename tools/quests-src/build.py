import sys, importlib, glob, os
import descs
from engine import build

ITEMS = set(open(os.path.join(os.path.dirname(__file__), "items.txt")).read().split())

MODULES = ["ch_start", "ch_tech", "ch_tech2", "ch_food", "ch_build", "ch_explore"]
ORDER = [
    ("ch_start", "WELCOME"), ("ch_more", "QUARK"),
    ("ch_tech", "CREATE"), ("ch_tech", "CREATE_ADDONS"), ("ch_tech", "AERO"), ("ch_more", "TRAINS"), ("ch_tech", "VEHICLES"),
    ("ch_tech2", "MEKANISM"), ("ch_tech2", "STORAGE"),
    ("ch_food", "FARMERS"), ("ch_food", "DELIGHTS"), ("ch_food", "LETSDO"), ("ch_food", "CREATEFOOD"), ("ch_food", "PAMS"), ("ch_food", "FISHING"),
    ("ch_build", "COLONIES"), ("ch_build", "BUILDING"),
    ("ch_explore", "EXPLORE"), ("ch_explore", "CREATURES"), ("ch_explore", "NETHER_END"), ("ch_explore", "AETHER"),
    ("ch_explore", "TWILIGHT"), ("ch_explore", "ALEXSCAVES"), ("ch_explore", "ADASTRA"), ("ch_explore", "FOSSILS"), ("ch_more", "LUMINOUS"), ("ch_more", "GEAR"),
]

chapters = []
for mod, name in ORDER:
    try:
        m = importlib.import_module(mod)
    except ModuleNotFoundError:
        continue
    if hasattr(m, name):
        ch = getattr(m, name)
        for q in ch["quests"]:
            if not q.d and (name, q.k) in descs.D:
                q.d = [descs.D[(name, q.k)]]
        chapters.append(ch)

out = sys.argv[1] if len(sys.argv) > 1 else "/home/claude/quests/out"
used = build(chapters, out, "Filipovo Bombovo 2")
bad = [(c, q, i) for c, q, i in used if i not in ITEMS]
nq = sum(len(c["quests"]) for c in chapters)
print(f"chapters={len(chapters)} quests={nq} items={len(used)} missing={len(bad)}")
for c, q, i in bad:
    print("  MISSING", c, q, i)
