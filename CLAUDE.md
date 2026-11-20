# Filipovo Bombovo 2 (modpack)

Minecraft 1.21.1 + NeoForge 21.1.266, ~300 modů, spravováno přes packwiz. Hrají 4 Češi na vlastním serveru
(Docker, `server/`). Komunikuj česky.

## Než začneš
- Ověřená fakta o packu, světě serveru a známých problémech: **`docs/modpack-knowledge.md`** – přečti před každou
  změnou questů, receptů nebo generování.
- Data z jarů modů (recepty, tagy, lang, průvodci) si obnov přes `tools/refdata/rebuild.sh` (→ `/tmp/bombovo-refdata`).
  Nic o modech netvrď z paměti, ověř to v datech nebo v kódu jaru (`javap`).
- Server má vlastní Claude session („Komunikace s agentem na PC“) – umí spouštět příkazy přes RCON (`/locate`,
  dumpy registrů, logy). Na serveru nic neměň bez souhlasu uživatele.

## Struktura
- `mods/*.pw.toml` – mody (packwiz); `mods/fossil-…jar` je náš vlastní port Fossils & Archeology.
- `config/` – configy distribuované hráčům i serveru; `kubejs/` – serverové skripty a datapack.
- `config/ftbquests/quests/` – **generovaný výstup**, needituj ručně. Zdroj je `tools/quests-src/`.
- `tools/` a `docs/` nejsou součástí packu (`.packwizignore`).

## Questy (FTB Quests)
- Zdroj: `tools/quests-src/areas/*.py`, pravidla psaní: `tools/quests-src/GUIDE.md`.
- Validace: `python3 tools/quests-src/build.py --check [--area <oblast>]` – musí mít 0 chyb.
- Instalace: `tools/install-quests.sh` (build + packwiz refresh), pak commit a push.
- Původní questy z `tools/quests-src/baseline.json` nikdy nemaž ani neměň jejich úkoly (postup hráčů).

## Po každé změně souborů packu
`packwiz refresh` (binárka `~/go/bin/packwiz`), commit, push. Server si pack stáhne při restartu.
