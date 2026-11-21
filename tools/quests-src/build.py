"""Sestaví FTB Quests ze zdrojů v areas/*.py.

  python3 build.py --check                 # jen validace všech oblastí
  python3 build.py --check --area b_create # validace, vypíše jen problémy dané oblasti
  python3 build.py --install               # validace + zápis do config/ftbquests/quests a tools/quests

Build skončí chybou, pokud validace najde chybu (E...). Varování (W...) je nutné projít ručně.
"""
import sys, importlib, os, shutil, tempfile, argparse
from engine import build
import validate

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))

# Pořadí oblastí = pořadí kapitol v knize (uvnitř oblasti podle CHAPTERS)
AREAS = [
    "a_start", "b_create", "c_create_addons", "d_transport", "e_tech",
    "f_food", "g_food2", "h_build", "i_dims", "j_explore", "k_adventure",
]


def load(only_area=None):
    """Načte oblasti. Když jiná (cizí) oblast nejde načíst (někdo ji právě edituje),
    použije se její poslední funkční kopie z areas/.cache."""
    import importlib.util
    adir = os.path.join(HERE, "areas")
    cdir = os.path.join(adir, ".cache")
    os.makedirs(cdir, exist_ok=True)
    sys.path.insert(0, adir)
    chapters, owner, no_recipe, proper_cz = [], {}, {}, {}
    for a in AREAS:
        path = os.path.join(adir, a + ".py")
        try:
            spec = importlib.util.spec_from_file_location(a, path)
            m = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(m)
            shutil.copyfile(path, os.path.join(cdir, a + ".py"))
        except Exception as e:
            if only_area is None or a == only_area:
                raise
            print(f"! oblast {a} nejde načíst ({type(e).__name__}: {e}) - používám poslední funkční kopii")
            spec = importlib.util.spec_from_file_location(a, os.path.join(cdir, a + ".py"))
            m = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(m)
        for ch in m.CHAPTERS:
            chapters.append(ch)
            owner[ch["key"]] = a
        no_recipe.update(getattr(m, "NO_RECIPE", {}))
        proper_cz.update(getattr(m, "PROPER_NAMES_CZ", {}))
    return chapters, owner, no_recipe, proper_cz


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--install", action="store_true")
    ap.add_argument("--area")
    args = ap.parse_args()
    chapters, owner, no_recipe, proper_cz = load(args.area)
    errors, warnings = validate.run(chapters, owner, no_recipe, only_area=args.area, proper_cz=proper_cz)
    for w in warnings:
        print("W", w)
    for e in errors:
        print("E", e)
    nq = sum(len(c["quests"]) for c in chapters)
    mine = [c for c in chapters if not args.area or owner[c["key"]] == args.area]
    print(f"chapters={len(chapters)} quests={nq} | area: chapters={len(mine)} quests={sum(len(c['quests']) for c in mine)} | errors={len(errors)} warnings={len(warnings)}")
    tmp = tempfile.mkdtemp()
    try:
        try:
            build(chapters, tmp, "Filipovo Bombovo 2")  # i při --check: ověří závislosti a rozložení
        except AssertionError as e:
            # chyby závislostí hlásí validátor; při --area nechceme padat kvůli cizí oblasti
            if args.install or not args.area:
                raise
            print("! build selhal (pravděpodobně cizí oblast):", e)
        if errors:
            sys.exit(1)
        if args.install:
            src = os.path.join(tmp, "config", "ftbquests", "quests")
            for dst in (os.path.join(ROOT, "config", "ftbquests", "quests"), os.path.join(ROOT, "tools", "quests")):
                shutil.rmtree(dst, ignore_errors=True)
                shutil.copytree(src, dst)
            print("installed ->", "config/ftbquests/quests + tools/quests")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    main()
