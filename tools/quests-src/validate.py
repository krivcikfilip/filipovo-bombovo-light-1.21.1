"""Validace questů proti registrům ze serveru (tools/registry) a proti původním questům (baseline.json)."""
import os, re, json
from collections import defaultdict
from engine import GROUPS

HERE = os.path.dirname(os.path.abspath(__file__))
REG = os.path.join(HERE, "..", "registry")


def _set(name):
    return set(open(os.path.join(REG, name)).read().split())


ITEMS = _set("items.txt")
OBTAINABLE = _set("obtainable.txt")
ENTITIES = _set("entities.txt")
BIOMES = _set("biomes.txt")
STRUCTURES = _set("structures.txt")
DIMENSIONS = _set("dimensions.txt")
ADVANCEMENTS = _set("advancements.txt")
AU_HIDDEN = _set("almostunified_hidden.txt")  # Almost Unified je skryje a recepty dávají preferovaný předmět
BASELINE = json.load(open(os.path.join(HERE, "baseline.json")))

CZ = re.compile(r"[áčďéěíňóřšťúůýž]", re.I)
EN_WORDS = re.compile(r"\b(the|and|you|your|with|this|that|will|can|from|into|when|which|makes|first|need|it's|don't)\b", re.I)
HILITE = re.compile(r"&[0-9a-fk-o].*?(&r|$)")
PAREN = re.compile(r"\([^)]*\)")
# Původní questy s chybným úkolem, které se smí opravit (klíč -> důvod). Stejný počet úkolů zachovat.
TASK_FIXES = {
    "ad_astra/steel": "ad_astra:steel_ingot skrývá Almost Unified -> mekanism:ingot_steel",
    "aeronautics/levitite": "levitit nejde sebrat (noLootTable) -> advancement unidentified_floating_object",
    "aeronautics/islands": "aerolit padá jen jako větvička -> aeroscapes:quickslate z 9 větviček",
    "luminous/gilded": "gilded_piglin_trophy nejde získat (mob se nespawnuje) -> jiný získatelný předmět Luminous Nether",
}
ALLOWED_TASKS = {"item", "kill", "dimension", "biome", "structure", "advancement", "stat"}

# ---- Vlastní jména se nepřekládají (mody, dimenze, biomy, stavby, bossové a mobové, jednotky).
# Hra běží anglicky, hráč musí v textu poznat jméno, které vidí ve hře (F3, mapa, JEI, Jade).
# names_en.tsv: druh, id, anglický název z lang souborů modů (biome/entity/dimension).
NAMES_EN = defaultdict(dict)
_ne = os.path.join(REG, "names_en.tsv")
if os.path.exists(_ne):
    for _l in open(_ne, encoding="utf-8"):
        _p = _l.rstrip("\n").split("\t")
        if len(_p) == 3:
            NAMES_EN[_p[0]][_p[1]] = _p[2]
# Bossové z vanilly (ostatní vanilla mobové smí zůstat česky: kráva, zombie, kostlivec…)
VANILLA_BOSSES = {"minecraft:ender_dragon", "minecraft:wither", "minecraft:warden", "minecraft:elder_guardian"}
# České překlady vlastních jmen, které se nesmí objevit (regex, bez ohledu na velikost písmen -> anglický název).
# Další přidávej sem nebo do PROPER_NAMES_CZ ve své oblasti.
PROPER_NAMES_CZ = {
    r"soumra[čc]n\w* les": "Twilight Forest",
    r"pravěk\w* jeskyn": "Primordial Caves",
    r"toxick\w* jeskyn": "Toxic Caves",
    r"magnetick\w* jeskyn": "Magnetic Caves",
    r"cukrov\w* dutin": "Candy Cavity",
    r"opuštěn\w* dutin": "Forlorn Hollows",
    r"propastn\w* rokl": "Abyssal Chasm",
    r"zkušební\w* komnat": "Trial Chambers",
    r"starověk\w* měst": "Ancient City",
    r"ender\w* drak|drak\w* z endu": "Ender Dragon",
    # očarování (anglicky, jak je hra ukazuje: Silk Touch, Fortune, Looting, Protection…)
    r"hedvábn\w* dot|něžn\w* dot|jemn\w* doty": "Silk Touch",
    r"drancování": "Looting",
    r"štěstí\w* moř": "Luck of the Sea",
    r"očarování\w* (štěstí|ochran|ostrost|nezlomnost|účinnost|oprav|síl)": "anglický název očarování",
    r"ochran\w* (před|proti) (ohněm|výbuch|pádem|projektil)": "Fire/Blast/Projectile Protection, Feather Falling",
    r"\bostrost\w*|\bnezlomnost\w*|pírkov\w* pád|afinit\w* k vod|mraziv\w* chodec|hloubkov\w* chodec": "anglický název očarování",
}


def _name_in(name, text):
    """Anglický název je v textu (dovolí české koncovky: Aether -> Aetheru, Naga -> Nagu)."""
    t = text.lower()
    n = name.lower()
    if n in t:
        return True
    return len(n) >= 4 and n[:-1] in t  # Naga -> Nagu, Lich -> Licha


def run(chapters, owner, no_recipe, only_area=None, proper_cz=None):
    errors, warnings = [], []
    cz_rx = [(re.compile(k, re.I), v) for k, v in {**PROPER_NAMES_CZ, **(proper_cz or {})}.items()]
    group_keys = {g for g, _ in GROUPS}
    keys = {(c["key"], q.k) for c in chapters for q in c["quests"]}
    item_quests = defaultdict(list)

    def mine(chkey):
        return only_area is None or owner.get(chkey) == only_area

    def E(ch, q, msg):
        if mine(ch):
            errors.append(f"[{ch}/{q}] {msg}")

    def W(ch, q, msg):
        if mine(ch):
            warnings.append(f"[{ch}/{q}] {msg}")

    def chk_item(ch, q, iid, what):
        if iid not in ITEMS:
            E(ch, q, f"{what}: neexistující předmět {iid}")
        elif iid in AU_HIDDEN and not what.startswith("ikona"):
            E(ch, q, f"{what}: {iid} skrývá Almost Unified (recepty dávají jiný mod) - použij preferovaný předmět (priorita minecraft > create > mekanism)")
        elif what.startswith("ikona"):
            pass  # ikona jen musí existovat (může to být i spawn egg)
        elif iid not in OBTAINABLE and iid not in no_recipe:
            if iid.startswith("minecraft:"):
                W(ch, q, f"{what}: {iid} nemá recept ani loot (vanilla - ověř, že jde získat)")
            else:
                E(ch, q, f"{what}: {iid} nemá recept ani loot table -> ověř zdroj a přidej do NO_RECIPE s vysvětlením")

    seen_ch = set()
    for c in chapters:
        ck = c["key"]
        if ck in seen_ch:
            E(ck, "-", "duplicitní klíč kapitoly")
        seen_ch.add(ck)
        if c["group"] not in group_keys:
            E(ck, "-", f"neznámá skupina {c['group']}")
        chk_item(ck, "-", c["icon"], "ikona kapitoly")
        if not CZ.search(c["title"] + " " + c.get("subtitle", "")):
            W(ck, "-", f"název/podnázev kapitoly asi není česky: {c['title']!r}")
        for rx, en in cz_rx:
            m = rx.search(c["title"] + " | " + c.get("subtitle", ""))
            if m:
                E(ck, "-", f"přeložené vlastní jméno {m.group(0)!r} -> piš {en!r}")
        seen_q = set()
        for q in c["quests"]:
            if q.k in seen_q:
                E(ck, q.k, "duplicitní klíč questu")
            seen_q.add(q.k)
            if not q.t:
                E(ck, q.k, "chybí název")
            if len(q.t) > 40:
                W(ck, q.k, f"dlouhý název ({len(q.t)} znaků)")
            if not q.d or not any(s.strip() for s in q.d):
                E(ck, q.k, "chybí popis")
            text = " ".join(q.d) + " " + q.t + " " + (q.s or "")
            if not CZ.search(text):
                W(ck, q.k, "popis asi není česky (žádná diakritika)")
            for s in q.d + [q.t, q.s or ""]:
                plain = PAREN.sub("", HILITE.sub("", s))
                hits = EN_WORDS.findall(plain)
                if len(hits) >= 2:
                    W(ck, q.k, f"anglická slova v textu {hits[:4]}: {s[:70]!r}")
                if len(s) > 320:
                    W(ck, q.k, f"příliš dlouhý odstavec ({len(s)} znaků) - rozděl ho")
                if re.search(r"&[0-9a-fk-o]", s) and not re.search(r"&r", s):
                    W(ck, q.k, "barevný kód bez &r na konci zvýraznění")
            for rx, en in cz_rx:
                m = rx.search(text)
                if m:
                    E(ck, q.k, f"přeložené vlastní jméno {m.group(0)!r} -> piš {en!r}")
            for t in q.tasks:
                ty = t.get("type")
                need = None
                if ty == "biome" and not t["biome"].startswith("#"):
                    need = NAMES_EN["biome"].get(t["biome"])
                elif ty == "dimension":
                    need = NAMES_EN["dimension"].get(t["dimension"])
                elif ty == "kill" and (not t["entity"].startswith("minecraft:") or t["entity"] in VANILLA_BOSSES):
                    need = NAMES_EN["entity"].get(t["entity"])
                if need and not _name_in(need, text):
                    E(ck, q.k, f"v názvu ani popisu chybí anglické jméno {need!r} ({ty}) - vlastní jména se nepřekládají")
            if not q.items and not q.tasks:
                E(ck, q.k, "quest nemá žádný úkol")
            for iid, n in q.items:
                chk_item(ck, q.k, iid, "úkol")
                if n < 1:
                    E(ck, q.k, f"počet {n} u {iid}")
                item_quests[iid].append(f"{ck}/{q.k}")
            for iid, n in q.rewards:
                chk_item(ck, q.k, iid, "odměna")
            if q.icon:
                chk_item(ck, q.k, q.icon, "ikona")
            for t in q.tasks:
                ty = t.get("type")
                if ty not in ALLOWED_TASKS:
                    E(ck, q.k, f"nepovolený typ úkolu {ty} (žádné checkmarky - quest se musí splnit sám)")
                elif ty == "kill" and t["entity"] not in ENTITIES:
                    E(ck, q.k, f"neexistující entita {t['entity']}")
                elif ty == "dimension" and t["dimension"] not in DIMENSIONS:
                    E(ck, q.k, f"neexistující dimenze {t['dimension']}")
                elif ty == "biome":
                    b = t["biome"]
                    if b.startswith("#"):
                        W(ck, q.k, f"biome tag {b} - ověř, že existuje")
                    elif b not in BIOMES:
                        E(ck, q.k, f"neexistující biom {b}")
                elif ty == "structure":
                    s = t["structure"]
                    if s.startswith("#"):
                        W(ck, q.k, f"structure tag {s} - ověř, že existuje")
                    elif s not in STRUCTURES:
                        E(ck, q.k, f"neexistující struktura {s}")
                elif ty == "advancement" and t["advancement"] not in ADVANCEMENTS:
                    E(ck, q.k, f"neexistující advancement {t['advancement']}")
                elif ty == "stat" and not (t.get("stat") == "minecraft:play_time" and t.get("value") == 1):
                    E(ck, q.k, "stat úkol je povolen jen jako auto()")
            for d in q.dep:
                if ":" in d:
                    oc, oq = d.split(":", 1)
                    if (oc, oq) not in keys:
                        E(ck, q.k, f"závislost na neexistujícím questu {d}")
                elif (ck, d) not in keys:
                    E(ck, q.k, f"závislost na neexistujícím questu {d}")
        # cykly v rámci knihy
    graph = {(c["key"], q.k): [tuple(d.split(":", 1)) if ":" in d else (c["key"], d) for d in q.dep]
             for c in chapters for q in c["quests"]}
    state = {}

    def dfs(n, stack):
        state[n] = 1
        for m in graph.get(n, []):
            if state.get(m) == 1:
                E(n[0], n[1], f"cyklická závislost přes {m[0]}/{m[1]}")
            elif m in graph and not state.get(m):
                dfs(m, stack)
        state[n] = 2

    for n in graph:
        if not state.get(n):
            dfs(n, [])

    # původní questy musí zůstat (stejná kapitola, klíč a úkoly; nové úkoly jen přidat na konec)
    byk = {(c["key"], q.k): q for c in chapters for q in c["quests"]}
    for full, b in BASELINE.items():
        ck, qk = full.split("/", 1)
        q = byk.get((ck, qk))
        if q is None:
            E(ck, qk, "PŮVODNÍ QUEST CHYBÍ - nesmí se odebrat ani přesunout do jiné kapitoly")
            continue
        bi = [tuple(x) for x in b["items"]]
        if full in TASK_FIXES:
            pass
        elif [tuple(x) for x in q.items[:len(bi)]] != bi:
            E(ck, qk, f"původní item úkoly změněny: bylo {bi}")
        if q.tasks[:len(b["tasks"])] != b["tasks"]:
            E(ck, qk, f"původní ostatní úkoly změněny: bylo {b['tasks']}")

    for iid, qs in item_quests.items():
        if len(qs) > 1 and any(mine(x.split("/")[0]) for x in qs):
            warnings.append(f"[dup] {iid} je úkolem ve více questech: {', '.join(qs)}")
    return errors, warnings
