import zipfile, io, os, sys, re, json
jars, out = sys.argv[1], sys.argv[2]
KEEP = re.compile(r'^(data/[^/]+/(recipe|recipes|advancement|advancements|tags|worldgen/structure|worldgen/biome|dimension|dimension_type|loot_table|loot_tables|curios|ponder|minecolonies)/.*\.json'
                  r'|assets/[^/]+/lang/(en_us|cs_cz)\.json'
                  r'|assets/[^/]+/(patchouli_books|modonomicon|ae2guide|guideme|guide|ponder|manual|lexicon)/.*\.(json|md)'
                  r'|data/[^/]+/(patchouli_books|modonomicon)/.*\.json)$')
def walk(z, src, depth=0):
    for n in z.namelist():
        if n.endswith('.jar') and depth < 2:
            try:
                walk(zipfile.ZipFile(io.BytesIO(z.read(n))), src + '!' + os.path.basename(n), depth + 1)
            except Exception as e: print('nested fail', n, e)
            continue
        if KEEP.match(n):
            if '/lang/' in n and not n.endswith('.json'): continue
            p = os.path.join(out, n)
            os.makedirs(os.path.dirname(p), exist_ok=True)
            data = z.read(n)
            if os.path.exists(p) and '/lang/' in n:
                # merge lang
                try:
                    a = json.load(open(p)); a.update(json.loads(data)); data = json.dumps(a, ensure_ascii=False, indent=1).encode()
                except Exception: pass
            open(p, 'wb').write(data)
    # mod id -> jar mapping
    for n in z.namelist():
        if n == 'META-INF/neoforge.mods.toml' or n == 'META-INF/mods.toml':
            t = z.read(n).decode('utf8', 'replace')
            for m in re.finditer(r'modId\s*=\s*"([^"]+)"', t):
                MODS.append((m.group(1), src))
MODS = []
for f in sorted(os.listdir(jars)):
    if f.endswith('.jar'):
        try: walk(zipfile.ZipFile(os.path.join(jars, f)), f)
        except Exception as e: print('fail', f, e)
with open(os.path.join(out, 'MODIDS.tsv'), 'w') as o:
    for m, s in MODS: o.write(f'{m}\t{s}\n')
