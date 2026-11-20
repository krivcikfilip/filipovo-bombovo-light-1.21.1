import zipfile, io, os, re, sys, json
from collections import defaultdict
jars, items_txt, out = sys.argv[1], sys.argv[2], sys.argv[3]
ITEMS = set(open(items_txt).read().split())
modids = set(); variants = defaultdict(list); loot_ids = set()
RE = re.compile(r'^data/([^/]+)/recipes?/(.+)\.json$')
LT = re.compile(r'^data/[^/]+/loot_tables?/.+\.json$')
pat = re.compile(r'"(?:name|id|item)"\s*:\s*"([a-z0-9_.\-]+:[a-z0-9_./\-]+)"')
def walk(z, src, depth=0):
    for n in z.namelist():
        if n.endswith('.jar') and depth < 2:
            try: walk(zipfile.ZipFile(io.BytesIO(z.read(n))), src + '!' + os.path.basename(n), depth + 1)
            except Exception: pass
        elif n == 'META-INF/neoforge.mods.toml':
            t = z.read(n).decode('utf8', 'replace')
            for sec in re.split(r'(?m)^\s*\[\[', t):
                if sec.startswith('mods]]'):
                    m = re.search(r'modId\s*=\s*"([^"]+)"', sec)
                    if m: modids.add(m.group(1))
        elif RE.match(n):
            try: variants[RE.match(n).group(1) + ':' + RE.match(n).group(2)].append((src, json.loads(z.read(n))))
            except Exception: pass
        elif LT.match(n):
            loot_ids.update(pat.findall(z.read(n).decode('utf8', 'ignore')))
for f in sorted(os.listdir(jars)):
    if f.endswith('.jar'):
        try: walk(zipfile.ZipFile(os.path.join(jars, f)), f)
        except Exception as e: print('fail', f, e)
modids |= {'minecraft', 'neoforge'}
def cond(c):
    """True / False / None (neznámé -> nevíme, bereme jako zapnuté)"""
    t = c.get('type', '')
    if t == 'neoforge:mod_loaded': return c.get('modid') in modids
    if t == 'neoforge:not':
        v = cond(c.get('value', {}))
        return None if v is None else (not v)
    if t in ('neoforge:and', 'neoforge:or'):
        vs = [cond(x) for x in c.get('values', [])]
        if t == 'neoforge:and':
            return False if False in vs else (None if None in vs else True)
        return True if True in vs else (None if None in vs else False)
    if t == 'neoforge:false': return False
    if t == 'neoforge:true': return True
    if t == 'neoforge:item_exists': return c.get('item') in ITEMS
    return None
def enabled(r):
    if not isinstance(r, dict): return False
    return all(cond(c) is not False for c in r.get('neoforge:conditions', []) if isinstance(c, dict))
def outs(r):
    res = []
    def take(x):
        if isinstance(x, str): res.append(x)
        elif isinstance(x, dict):
            for k in ('id', 'item'):
                if isinstance(x.get(k), str): res.append(x[k]); break
            else:
                for v in x.values():
                    if isinstance(v, (dict, list)): take(v)
        elif isinstance(x, list):
            for y in x: take(y)
    for k in ('result', 'results', 'output', 'outputs', 'mainOutput', 'secondaryOutput', 'item_output', 'gas_output', 'chemical_output'):
        if k in r: take(r[k])
    return res
ok = set(); disabled_paths = 0
for path, vs in variants.items():
    if not all(enabled(r) for _, r in vs):
        disabled_paths += 1
        # pokud je některá varianta vypnutá, bereme jen zapnuté varianty z jiných jarů, které nejsou původní
        vs = [(s, r) for s, r in vs if enabled(r)]
        if len(vs) == 0: continue
    for s, r in vs: ok.update(outs(r))
ok |= loot_ids
ok &= ITEMS
open(out, 'w').write('\n'.join(sorted(ok)) + '\n')
print('modids', len(modids), 'recipe paths', len(variants), 'paths with disabled variant', disabled_paths, 'obtainable', len(ok))
