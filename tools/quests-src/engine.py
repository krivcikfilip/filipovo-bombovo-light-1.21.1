import re
"""Generator FTB Quests (1.21.1 / ftbquests 2101.x) ze specifikace v Pythonu.

Specifikace kapitoly:
  dict(key, title, subtitle, icon, group, quests=[Q(...), ...])
Quest:
  Q(k, t, d=[...], items=[(id, n)], tasks=[...], dep=[...], xp=..., s=subtitle,
    icon=..., rewards=[(id, n)], one_of=False, x=None, y=None)
"""
import hashlib, os, json

GROUPS = [
    ("start", "Getting Started"),
    ("tech", "Technology"),
    ("food", "Food & Farming"),
    ("build", "Colonies & Building"),
    ("explore", "Exploration & Dimensions"),
]


def hid(*parts):
    n = int(hashlib.sha1("/".join(parts).encode()).hexdigest()[:16], 16)
    # FTB parsuje ID jako signed long: první hex číslice musí být 0-7
    n &= 0x7FFFFFFFFFFFFFFF
    h = f"{n:016X}"
    # FTB nesnese ID složené jen z číslic (bralo by se jako long) – pojistka
    if h.isdigit():
        h = "1A" + h[2:]
    return h


class Q:
    def __init__(self, k, t, d=None, items=None, tasks=None, dep=None, xp=None,
                 s=None, icon=None, rewards=None, one_of=False, x=None, y=None,
                 optional=False):
        self.k, self.t, self.d, self.s = k, t, d or [], s
        self.items = items or []
        self.tasks = tasks or []
        self.dep = dep or []
        self.xp = xp
        self.icon = icon
        self.rewards = rewards or []
        self.one_of = one_of
        self.x, self.y = x, y
        self.optional = optional


# ---------- task helpers ----------
def check():
    return {"type": "checkmark"}

def auto():
    """Splní se sám hned po odemčení (odehraný čas >= 1 tick)."""
    return {"type": "stat", "stat": "minecraft:play_time", "value": 1}


def dim(d):
    return {"type": "dimension", "dimension": d}

def kill(e, n=1):
    return {"type": "kill", "entity": e, "value": n}

def biome(b):
    return {"type": "biome", "biome": b}

def structure(s):
    return {"type": "structure", "structure": s}

def adv(a):
    return {"type": "advancement", "advancement": a, "criterion": ""}


# ---------- SNBT writer ----------
def esc_amp(v):
    # '&' je ve FTB formátovací kód; holé '&' (ne &a, &r...) musí být '\\&'
    if isinstance(v, str):
        return re.sub(r"&(?![0-9a-fk-or])", r"\\&", v)
    if isinstance(v, list):
        return [esc_amp(i) for i in v]
    if isinstance(v, dict):
        return {k: esc_amp(x) for k, x in v.items()}
    return v


def snbt(v, ind=0):
    t = "\t"
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, Raw):
        return v.s
    if isinstance(v, int):
        return str(v)
    if isinstance(v, float):
        return f"{v}d"
    if isinstance(v, str):
        return json.dumps(v, ensure_ascii=False)
    if isinstance(v, list):
        if not v:
            return "[ ]"
        if all(isinstance(i, str) for i in v):
            if len(v) == 1:
                return "[" + snbt(v[0]) + "]"
            return "[\n" + "".join(t * (ind + 1) + snbt(i) + "\n" for i in v) + t * ind + "]"
        return "[\n" + "".join(t * (ind + 1) + snbt(i, ind + 1) + "\n" for i in v) + t * ind + "]"
    if isinstance(v, dict):
        out = "{\n"
        for k in sorted(v):
            out += t * (ind + 1) + k + ": " + snbt(v[k], ind + 1) + "\n"
        return out + t * ind + "}"
    raise TypeError(v)


class Raw:
    def __init__(self, s):
        self.s = s


def L(n):
    return Raw(f"{n}L")


def item_obj(i):
    return {"count": 1, "id": i}


# ---------- build ----------
def _seg_dist(px, py, ax, ay, bx, by):
    dx, dy = bx - ax, by - ay
    L = dx * dx + dy * dy
    t = 0 if L == 0 else max(0, min(1, ((px - ax) * dx + (py - ay) * dy) / L))
    cx, cy = ax + t * dx, ay + t * dy
    return ((px - cx) ** 2 + (py - cy) ** 2) ** 0.5


def collisions(quests, r=0.62):
    by = {q.k: q for q in quests}
    bad = []
    for q in quests:
        for d in q.dep:
            p = by[d]
            for o in quests:
                if o is q or o is p:
                    continue
                if _seg_dist(o.x, o.y, p.x, p.y, q.x, q.y) < r:
                    bad.append((p.k, q.k, o.k))
    return bad


def layout(quests, step=1.5):
    """Vrstvené rozložení: sloupec = hloubka závislostí, děti u rodičů,
    mezery mezi sloupci podle strmosti čar a posun questů, přes které by vedla čára."""
    if all(q.x is not None and q.y is not None for q in quests):
        return quests
    by = {q.k: q for q in quests}
    depth = {}

    def d(q, seen=()):
        if q.k in depth:
            return depth[q.k]
        ds = [d(by[x], seen + (q.k,)) for x in q.dep if x in by and x not in seen]
        depth[q.k] = (max(ds) + 1) if ds else 0
        return depth[q.k]

    for q in quests:
        d(q)
    ncol = max(depth.values()) + 1
    cols = [[q for q in quests if depth[q.k] == c] for c in range(ncol)]
    y = {}
    for i, q in enumerate(cols[0]):
        y[q.k] = i * step
    for c in range(1, ncol):
        col = cols[c]
        want = {q.k: (sum(y[p] for p in q.dep) / len(q.dep)) for q in col}
        col.sort(key=lambda q: (want[q.k], quests.index(q)))
        # skupiny se stejným rodičovským y vycentrovat kolem něj
        placed = []
        i = 0
        while i < len(col):
            j = i
            while j + 1 < len(col) and abs(want[col[j + 1].k] - want[col[i].k]) < 1e-9:
                j += 1
            n = j - i + 1
            base = want[col[i].k] - (n - 1) * step / 2
            for k in range(n):
                placed.append([col[i + k], base + k * step])
            i = j + 1
        # odstranit překryvy (zachovat pořadí)
        for k in range(1, len(placed)):
            if placed[k][1] < placed[k - 1][1] + step:
                placed[k][1] = placed[k - 1][1] + step
        for q, yy in placed:
            y[q.k] = yy
        cols[c] = [p[0] for p in placed]

    def assign_x():
        xs = [0.0]
        for c in range(1, ncol):
            maxdy = 0
            for q in cols[c]:
                for p in q.dep:
                    if depth[p] == c - 1:
                        maxdy = max(maxdy, abs(y[q.k] - y[p]))
            gap = max(1.75, 0.5 * maxdy + 0.5)
            xs.append(xs[-1] + gap)
        for c in range(ncol):
            for q in cols[c]:
                q.x, q.y = xs[c], y[q.k]

    for _ in range(200):
        assign_x()
        bad = collisions(quests)
        if not bad:
            break
        # posunout blokující quest (a vše pod ním ve sloupci) dolů
        blocker = by[bad[0][2]]
        c = depth[blocker.k]
        hit = False
        for q in cols[c]:
            if q is blocker:
                hit = True
            if hit:
                y[q.k] += step
    # normalizace: nejmenší y = 0
    m = min(q.y for q in quests)
    for q in quests:
        q.y = round(q.y - m, 3)
        q.x = round(q.x, 3)
    return quests


def build(chapters, outdir, file_title):
    qdir = os.path.join(outdir, "config", "ftbquests", "quests")
    os.makedirs(os.path.join(qdir, "chapters"), exist_ok=True)
    os.makedirs(os.path.join(qdir, "lang"), exist_ok=True)
    lang = {"file.0000000000000001.title": file_title}
    used_items = []

    gids = {g: hid("group", g) for g, _ in GROUPS}
    for g, title in GROUPS:
        lang[f"chapter_group.{gids[g]}.title"] = title
    with open(os.path.join(qdir, "chapter_groups.snbt"), "w") as f:
        f.write(snbt({"chapter_groups": [{"id": gids[g]} for g, _ in GROUPS]}) + "\n")

    data = {
        "default_autoclaim_rewards": "disabled",
        "default_consume_items": False,
        "default_quest_disable_jei": False,
        "default_quest_shape": "circle",
        "default_reward_team": False,
        "detection_delay": 20,
        "disable_gui": False,
        "drop_book_on_death": False,
        "drop_loot_crates": False,
        "emergency_items_cooldown": 300,
        "fallback_locale": "",
        "grid_scale": 0.5,
        "hide_excluded_quests": False,
        "lock_message": "",
        "loot_crate_no_drop": {"boss": 0, "monster": 600, "passive": 4000},
        "pause_game": False,
        "progression_mode": "flexible",
        "show_lock_icons": False,
        "verify_on_load": False,
        "version": 13,
    }
    with open(os.path.join(qdir, "data.snbt"), "w") as f:
        f.write(snbt(data) + "\n")

    seen_keys = set()
    for order, ch in enumerate(chapters):
        cid = hid("chapter", ch["key"])
        lang[f"chapter.{cid}.title"] = ch["title"]
        if ch.get("subtitle"):
            lang[f"chapter.{cid}.chapter_subtitle"] = [ch["subtitle"]]
        qs = layout(ch["quests"])
        keys = {q.k for q in qs}
        out = []
        for q in qs:
            assert (ch["key"], q.k) not in seen_keys, (ch["key"], q.k)
            seen_keys.add((ch["key"], q.k))
            qid = hid("quest", ch["key"], q.k)
            tasks = []
            for n, (iid, cnt) in enumerate(q.items):
                t = {"id": hid("task", ch["key"], q.k, str(n)), "item": Raw('{ count: 1, id: "%s" }' % iid), "type": "item"}
                if cnt > 1:
                    t["count"] = L(cnt)
                tasks.append(t)
                used_items.append((ch["key"], q.k, iid))
            for n, td in enumerate(q.tasks):
                t = dict(td)
                t["id"] = hid("task", ch["key"], q.k, "x" + str(n))
                if t["type"] == "kill":
                    t["value"] = L(t["value"])
                tasks.append(t)
            rewards = []
            if q.xp:
                rewards.append({"id": hid("reward", ch["key"], q.k, "xp"), "type": "xp", "xp": q.xp})
            for n, (iid, cnt) in enumerate(q.rewards):
                r = {"id": hid("reward", ch["key"], q.k, str(n)), "item": item_obj(iid), "type": "item"}
                if cnt > 1:
                    r["count"] = cnt
                rewards.append(r)
                used_items.append((ch["key"], q.k + ":reward", iid))
            qd = {"id": qid, "tasks": tasks, "x": float(q.x), "y": float(q.y)}
            deps = [hid("quest", ch["key"], x) for x in q.dep if x in keys]
            missing = [x for x in q.dep if x not in keys]
            assert not missing, (ch["key"], q.k, missing)
            if deps:
                qd["dependencies"] = deps
            if rewards:
                qd["rewards"] = rewards
            if q.icon:
                qd["icon"] = {"id": q.icon}
                used_items.append((ch["key"], q.k + ":icon", q.icon))
            if q.optional:
                qd["optional"] = True
            out.append(qd)
            lang[f"quest.{qid}.title"] = q.t
            if q.s:
                lang[f"quest.{qid}.quest_subtitle"] = q.s
            if q.d:
                lang[f"quest.{qid}.quest_desc"] = q.d
        chd = {
            "default_hide_dependency_lines": False,
            "default_quest_shape": "",
            "filename": ch["key"],
            "group": gids[ch["group"]],
            "icon": {"id": ch["icon"]},
            "id": cid,
            "order_index": order,
            "quest_links": [],
            "quests": out,
        }
        used_items.append((ch["key"], ":chapter-icon", ch["icon"]))
        with open(os.path.join(qdir, "chapters", ch["key"] + ".snbt"), "w") as f:
            f.write(snbt(chd) + "\n")

    with open(os.path.join(qdir, "lang", "en_us.snbt"), "w") as f:
        f.write(snbt(esc_amp(lang)) + "\n")
    return used_items
