"""Rozvržení questů v kapitole (vrstvy + barycentrum + PAV, oprava kolizí, žíhání)."""
def _pav(desired, gaps):
    """Minimalizuje sum (y_i - desired_i)^2 při y_{i+1} - y_i >= gaps[i] (pořadí zachováno)."""
    off = [0.0]
    for g in gaps:
        off.append(off[-1] + g)
    z = [d - o for d, o in zip(desired, off)]
    blocks = []  # [sum, count]
    for v in z:
        blocks.append([v, 1])
        while len(blocks) > 1 and blocks[-2][0] / blocks[-2][1] > blocks[-1][0] / blocks[-1][1]:
            s, c = blocks.pop()
            blocks[-1][0] += s
            blocks[-1][1] += c
    out = []
    for s, c in blocks:
        out += [s / c] * c
    return [v + o for v, o in zip(out, off)]


def layout2(quests, step=1.5, dstep=0.9, sweeps=12, gap=None, straight=False):
    if all(q.x is not None and q.y is not None for q in quests):
        return quests
    by = {q.k: q for q in quests}
    depth = {}

    def d(k, seen=()):
        if k in depth:
            return depth[k]
        q = by[k]
        ds = [d(x, seen + (k,)) for x in q.dep if x in by and x not in seen]
        depth[k] = (max(ds) + 1) if ds else 0
        return depth[k]

    for q in quests:
        d(q.k)
    n = max(depth.values()) + 1
    # uzly: skutečné questy + dummy uzly pro dlouhé hrany
    preds = {q.k: [] for q in quests}
    succs = {q.k: [] for q in quests}
    layer = dict(depth)
    real = set(by)
    chain = {}
    for q in quests:
        for p in q.dep:
            if p not in by:
                continue
            prev = p
            for L in range(depth[p] + 1, depth[q.k]):
                dk = f"~{p}>{q.k}@{L}"
                layer[dk] = L
                chain[dk] = (p, q.k)
                preds[dk] = [prev]
                succs[dk] = []
                succs[prev].append(dk)
                prev = dk
            preds[q.k].append(prev)
            succs[prev].append(q.k)
    cols = [[] for _ in range(n)]
    for k in layer:
        cols[layer[k]].append(k)
    index = {q.k: i for i, q in enumerate(quests)}

    def key0(k):
        return index.get(k, index.get(k.split(">")[-1].split("@")[0], 0))

    for c in cols:
        c.sort(key=key0)
    pos = {}

    def renum():
        for c in cols:
            for i, k in enumerate(c):
                pos[k] = i

    renum()
    for it in range(sweeps):
        rng = range(1, n) if it % 2 == 0 else range(n - 2, -1, -1)
        for L in rng:
            nb = preds if it % 2 == 0 else succs

            def bc(k):
                ns = nb[k]
                return sum(pos[x] for x in ns) / len(ns) if ns else pos[k]

            cols[L].sort(key=lambda k: (bc(k), pos[k]))
            for i, k in enumerate(cols[L]):
                pos[k] = i
    # y: iterativně - průměr sousedů, pak PAV s rozestupy
    y = {}
    for c in cols:
        acc = 0.0
        for i, k in enumerate(c):
            if i:
                acc += step if (k in real and c[i - 1] in real) else (dstep if (k not in real and c[i - 1] not in real) else (step + dstep) / 2)
            y[k] = acc

    def place(L, nbs):
        c = cols[L]
        des = []
        for k in c:
            if k in chain and straight:
                a, b = chain[k]
                La, Lb = layer[a], layer[b]
                des.append(y[a] + (y[b] - y[a]) * (L - La) / (Lb - La))
                continue
            ns = [x for x in nbs[k]]
            if k in real and straight:
                # skutečný quest: průměr přímých sousedů i konců dlouhých hran
                ns2 = [(chain[x][0] if nbs is preds else chain[x][1]) if x in chain else x for x in nbs[k]]
                ns = ns2
            des.append(sum(y[x] for x in ns) / len(ns) if ns else y[k])
        gaps = []
        for i in range(1, len(c)):
            a, b = c[i - 1] in real, c[i] in real
            gaps.append(step if a and b else (dstep if not a and not b else (step + dstep) / 2))
        for k, v in zip(c, _pav(des, gaps)):
            y[k] = v

    for it in range(20):
        if it % 2 == 0:
            for L in range(1, n):
                place(L, preds)
        else:
            for L in range(n - 2, -1, -1):
                place(L, succs)
    for L in range(1, n):
        place(L, preds)
    xs = [0.0]
    if gap:
        xs = [L * gap for L in range(n)]
    for L in (range(1, n) if not gap else []):
        maxdy = 0
        for k in cols[L]:
            for p in preds[k]:
                maxdy = max(maxdy, abs(y[k] - y[p]))
        xs.append(xs[-1] + max(1.75, min(0.35 * maxdy + 0.6, 4.0)))
    for q in quests:
        q.x, q.y = xs[depth[q.k]], y[q.k]
    m = min(q.y for q in quests)
    for q in quests:
        q.y = round(q.y - m, 3)
        q.x = round(q.x, 3)
    return quests


def repair(quests, collisions, step=1.5, max_iter=400):
    """Odsune questy, přes které vede cizí čára: střídavě nahoru/dolů o malý krok,
    ostatní ve sloupci posune, aby zůstal rozestup."""
    by = {q.k: q for q in quests}
    tried = {}
    for _ in range(max_iter):
        bad = collisions(quests)
        if not bad:
            break
        p, qk, ok = bad[0]
        o = by[ok]
        n = tried.get(ok, 0) + 1
        tried[ok] = n
        delta = 0.5 * ((n + 1) // 2) * (1 if n % 2 else -1)
        col = sorted([q for q in quests if abs(q.x - o.x) < 1e-6], key=lambda q: q.y)
        o.y += delta
        # zachovat rozestupy ve sloupci
        col.sort(key=lambda q: q.y)
        i = col.index(o)
        for j in range(i + 1, len(col)):
            if col[j].y < col[j - 1].y + step:
                col[j].y = col[j - 1].y + step
        for j in range(i - 1, -1, -1):
            if col[j].y > col[j + 1].y - step:
                col[j].y = col[j + 1].y - step
    m = min(q.y for q in quests)
    for q in quests:
        q.y = round(q.y - m, 3)
    return quests


def repair_down(quests, collisions, step=1.5, max_iter=600):
    by = {q.k: q for q in quests}
    for _ in range(max_iter):
        bad = collisions(quests)
        if not bad:
            break
        o = by[bad[0][2]]
        col = sorted([q for q in quests if abs(q.x - o.x) < 1e-6], key=lambda q: q.y)
        hit = False
        for q in col:
            if q is o:
                hit = True
            if hit:
                q.y += step / 2
    m = min(q.y for q in quests)
    for q in quests:
        q.y = round(q.y - m, 3)
    return quests


def spread_x(quests, factor):
    for q in quests:
        q.x = round(q.x * factor, 3)
    return quests


def anneal(quests, seg_dist, r=0.62, step=1.5, iters=60000, seed=1):
    """Posouvá questy ve sloupcích (x pevné) tak, aby žádná čára nevedla přes cizí quest
    a kapitola byla co nejnižší. Deterministické (seed)."""
    import random, math
    rnd = random.Random(seed)
    by = {q.k: q for q in quests}
    ks = [q.k for q in quests]
    X = {q.k: q.x for q in quests}
    Y = {q.k: q.y for q in quests}
    edges = [(d, q.k) for q in quests for d in q.dep if d in by]
    inc = {k: [] for k in ks}
    for i, (a, b) in enumerate(edges):
        inc[a].append(i)
        inc[b].append(i)
    cols = {}
    for k in ks:
        cols.setdefault(round(X[k], 3), []).append(k)

    def hit(i, o):
        a, b = edges[i]
        if o == a or o == b:
            return 0
        return 1 if seg_dist(X[o], Y[o], X[a], Y[a], X[b], Y[b]) < r else 0

    def local(*keys):
        # kolize, kterých se dané questy účastní (jako bod nebo jako konec hrany), bez duplicit
        pairs = set()
        for k in keys:
            for i in range(len(edges)):
                if hit(i, k):
                    pairs.add((i, k))
            for i in inc[k]:
                for o in ks:
                    if hit(i, o):
                        pairs.add((i, o))
        return len(pairs)

    def total():
        return sum(hit(i, o) for i in range(len(edges)) for o in ks)

    def height():
        return max(Y.values()) - min(Y.values())

    def elen(k):
        return sum(abs(Y[edges[i][0]] - Y[edges[i][1]]) for i in inc[k])

    coll = total()
    W = 40.0
    cost = W * coll + height() + 0.05 * sum(abs(Y[a] - Y[b]) for a, b in edges)
    best = (coll, height(), dict(Y))
    T0 = 3.0
    for it in range(iters):
        T = T0 * (1 - it / iters) + 0.01
        k = rnd.choice(ks)
        col = cols[round(X[k], 3)]
        old = Y[k]
        if rnd.random() < 0.3 and len(col) > 1:
            other = rnd.choice([o for o in col if o != k])
            new_k, new_o = Y[other], Y[k]
            before = local(k, other)
            hb = height(); lb = elen(k) + elen(other)
            Y[k], Y[other] = new_k, new_o
            after = local(k, other)
            ha = height(); la = elen(k) + elen(other)
            d = W * (after - before) + (ha - hb) + 0.05 * (la - lb)
            if d <= 0 or rnd.random() < math.exp(-d / T):
                coll += after - before
            else:
                Y[k], Y[other] = new_o, new_k
        else:
            new = round(old + rnd.choice([-1, 1]) * rnd.choice([0.5, 0.75, 1.5, 3.0]), 3)
            if any(abs(new - Y[o]) < step - 1e-6 for o in col if o != k):
                continue
            before = local(k); hb = height(); lb = elen(k)
            Y[k] = new
            after = local(k); ha = height(); la = elen(k)
            d = W * (after - before) + (ha - hb) + 0.05 * (la - lb)
            if d <= 0 or rnd.random() < math.exp(-d / T):
                coll += after - before
            else:
                Y[k] = old
        if coll < best[0] or (coll == best[0] and height() < best[1]):
            best = (coll, height(), dict(Y))
    Yb = best[2]
    m = min(Yb.values())
    for q in quests:
        q.y = round(Yb[q.k] - m, 3)
    return best[0]
