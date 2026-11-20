import os, re, sys, glob, subprocess, concurrent.futures as cf
mods, out = sys.argv[1], sys.argv[2]
jobs = []
for f in sorted(glob.glob(os.path.join(mods, "*.pw.toml"))):
    t = open(f).read()
    if re.search(r'^side = "client"', t, re.M): continue
    fn = re.search(r'^filename = "(.*)"', t, re.M).group(1)
    m = re.search(r'^url = "(.*)"', t, re.M)
    if m: url = m.group(1)
    else:
        fid = int(re.search(r'file-id = (\d+)', t).group(1))
        url = f"https://mediafilez.forgecdn.net/files/{fid//1000}/{fid%1000}/{fn}"
    jobs.append((fn, url))
def get(j):
    fn, url = j
    p = os.path.join(out, fn)
    if os.path.exists(p) and os.path.getsize(p) > 1000: return fn, "ok"
    r = subprocess.run(["curl", "-sfL", "--retry", "3", "-o", p, url])
    return fn, "ok" if r.returncode == 0 else f"FAIL {url}"
with cf.ThreadPoolExecutor(12) as ex:
    for fn, st in ex.map(get, jobs):
        if st != "ok": print(fn, st)
print("jobs", len(jobs))
