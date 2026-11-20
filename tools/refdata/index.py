import os, json, sys, re, glob
db = sys.argv[1]; items_txt = sys.argv[2]; out = os.path.join(db, 'index'); os.makedirs(out, exist_ok=True)
ITEMS = [l.strip() for l in open(items_txt) if l.strip()]
en, cs = {}, {}
for p in glob.glob(f'{db}/assets/*/lang/en_us.json'):
    try: en.update(json.load(open(p)))
    except Exception as e: print('lang fail', p, e)
for p in glob.glob(f'{db}/assets/*/lang/cs_cz.json'):
    try: cs.update(json.load(open(p)))
    except Exception: pass
def nm(d, i):
    ns, path = i.split(':', 1)
    for k in (f'item.{ns}.{path}', f'block.{ns}.{path}'):
        if k in d: return d[k]
    return ''
with open(f'{out}/items.tsv', 'w') as o:
    o.write('id\ten_name\tcs_name\n')
    for i in ITEMS: o.write(f'{i}\t{nm(en,i)}\t{nm(cs,i)}\n')
# recipes
def outs(r):
    res = []
    def take(x):
        if isinstance(x, str): res.append(x)
        elif isinstance(x, dict):
            for k in ('id', 'item', 'fluid'):
                if isinstance(x.get(k), str): res.append(x[k]); break
        elif isinstance(x, list):
            for y in x: take(y)
    for k in ('result', 'results', 'output', 'outputs', 'mainOutput', 'secondaryOutput'):
        if k in r: take(r[k])
    return res
n = 0
with open(f'{out}/recipes.tsv', 'w') as o:
    o.write('output\trecipe_type\tfile\n')
    for p in glob.glob(f'{db}/data/*/recipe/**/*.json', recursive=True) + glob.glob(f'{db}/data/*/recipes/**/*.json', recursive=True):
        try: r = json.load(open(p))
        except Exception: continue
        if not isinstance(r, dict): continue
        t = r.get('type', '?')
        for x in outs(r) or ['?']:
            o.write(f'{x}\t{t}\t{os.path.relpath(p, db)}\n'); n += 1
print('recipes rows', n)
ents = sorted({k[len('entity.'):].replace('.', ':', 1) for k in en if re.match(r'^entity\.[a-z0-9_]+\.[a-z0-9_/]+$', k)})
open(f'{out}/entities_from_lang.txt', 'w').write('\n'.join(ents) + '\n')
def ids(sub):
    s = set()
    for p in glob.glob(f'{db}/data/*/{sub}/**/*.json', recursive=True):
        ns = p[len(db)+6:].split('/')[0]
        s.add(ns + ':' + os.path.splitext(p.split(f'/{sub}/', 1)[1])[0])
    return sorted(s)
for name, sub in [('biomes', 'worldgen/biome'), ('structures', 'worldgen/structure'), ('dimensions', 'dimension')]:
    open(f'{out}/{name}.txt', 'w').write('\n'.join(ids(sub)) + '\n')
adv = ids('advancement') + ids('advancements')
open(f'{out}/advancements.txt', 'w').write('\n'.join(sorted(set(adv))) + '\n')
# advancement titles
with open(f'{out}/advancement_titles.tsv', 'w') as o:
    for p in glob.glob(f'{db}/data/*/advancement*/**/*.json', recursive=True):
        try: a = json.load(open(p))
        except Exception: continue
        d = a.get('display') if isinstance(a, dict) else None
        if not d: continue
        t = d.get('title'); t = t.get('translate', '') if isinstance(t, dict) else t
        de = d.get('description'); de = de.get('translate', '') if isinstance(de, dict) else de
        ns = p[len(db)+6:].split('/')[0]; aid = ns + ':' + os.path.splitext(re.split(r'/advancements?/', p, 1)[1])[0]
        o.write(f'{aid}\t{en.get(t, t)}\t{en.get(de, de)}\n')
json.dump(en, open(f'{out}/en_us_all.json', 'w'), ensure_ascii=False, indent=0)
