# Příručka pro psaní questů (FTB Quests, Filipovo Bombovo 2)

Modpack: Minecraft 1.21.1, NeoForge, ~280 modů. Hrají to Češi, i děti a úplní nováčci.
Kniha questů je **průvodce packem**: hráč díky ní pochopí každý mod a jeho postup (progres)
tak, aby nemusel hledat tutoriály na YouTube.

## 1. Jazyk a styl (nejdůležitější)

- **Vše česky**, gramaticky správně (i/y, čárky, shoda). Tykej hráči: „Vyrob si…“, „Postav…“, „Polož…“.
- **Krátké a jasné věty.** Jedna věta = jedna informace. Žádné slohy, příběhy, vtipy ani vata
  („Vítej, odvážný dobrodruhu…“ je špatně). Popis musí pochopit desetileté dítě.
- Popis questu má obvykle 2–4 krátké odstavce (každý řetězec v `d=[...]` je odstavec, `""` je prázdný řádek):
  1. **Co to je a k čemu to je** (1 věta).
  2. **Jak to získat / vyrobit / postavit** – konkrétně: jaký stroj, jaké suroviny, kam to položit, kde to najít.
  3. **Tip** – jak to použít chytře/efektivně, na co si dát pozor, co bude dál.
- Odstavec max. ~250 znaků. Pokud je potřeba víc (návody na stavbu), rozděl na více odstavců
  nebo stránek – samostatný řetězec `"{@pagebreak}"` v `d=[...]` založí novou stránku popisu.
- **Názvy předmětů**: ve hře je většina modů anglicky. Proto: české slovo a hned za ním přesný anglický
  název z JEI zvýrazněný žlutě, např. `mechanický lis (&eMechanical Press&r)`. Přesný anglický název
  ber ze sloupce `en_name` v `tools/registry/item_names.tsv` (ne z hlavy). Dále v textu už stačí česky.
  Vanilla předměty mají ve hře češtinu – u nich stačí český název (ten je ve sloupci `cs_name`, pokud je).
- **Vlastní jména se NEPŘEKLÁDAJÍ** (rozhodnutí uživatele 2026-11-21). Hra běží anglicky a hráč musí poznat jméno,
  které vidí ve hře (F3, mapa, JEI, Jade, chat). Anglicky, přesně podle `en_us` lang, zůstávají:
  názvy modů, **dimenzí** (Overworld, Nether, End, Aether, Twilight Forest, Moon, Mars…), **biomů** (Primordial Caves,
  Cherry Grove…), **staveb** (Trial Chambers, Ancient City, Woodland Mansion…), **bossů** (Ender Dragon, Wither, Warden,
  Naga, Lich…) a **mobů z modů** (Vallumraptor, Deep One…), jednotky a zkratky (SU, RPM, FE, mB, AE, ME).
  Běžní vanilla mobové smí zůstat česky (kráva, zombie, kostlivec, pavouk, vesničan).
  Předměty zůstávají ve tvaru `český název (&eEnglish Name&r)` (viz níže).
  Skloňuj jen jednoslovná jména, kde je to v češtině běžné (v Netheru, do Endu, v Aetheru, poraz Wardena).
  Víceslovná jména neskloňuj, pomoz si českým slovem: „v dimenzi Twilight Forest“, „v biomu Primordial Caves“,
  „poraz bosse Ender Dragon“, „najdi stavbu Trial Chambers“. Očarování taky anglicky (Silk Touch, Fortune, Looting, Protection). Krátké české vysvětlení smíš přidat
  („Twilight Forest je les věčného soumraku“), ale nikdy jako náhradu jména.
  Validátor hlídá: úkol biome/dimension/kill (mobové z modů a vanilla bossové) musí mít v textu anglické jméno
  (`tools/registry/names_en.tsv`) a známé české překlady jmen jsou chyba (`PROPER_NAMES_CZ` ve `validate.py`
  a v oblasti).
- Formátovací kódy: `&e` předmět/pojem, `&b` název modu (při prvním výskytu), `&c` varování
  (nebezpečí, ztráta věcí), `&a` tip. **Každé zvýraznění ukonči `&r`.** Holé `&` (např. „Slice & Dice“) je OK.
- Názvy questů: česky, krátké (ideálně do 25 znaků), podstatné jméno nebo výzva: „Mechanický lis“, „Postav větrný mlýn“.
- Klávesy piš jako ve hře: „Shift + pravé tlačítko“.

## 2. Fakta – žádné chyby

- **Každé tvrzení musí být ověřené** v datech modu (recepty, lang soubory, průvodci v jaru, ponder texty).
  Když si nejsi jistý, informaci vynech nebo ji napiš obecněji. Raději méně, ale správně.
- Čísla (stres SU, rychlosti, počty) piš jen když jsi je ověřil (v datech, v kódu jaru přes `javap -c`, nebo
  na oficiální wiki/GitHubu modu PRO TUTO VERZI). Jinak napiš, jak to hráč zjistí sám (např. „brýle ukážou…“).
- Pozor na verzi: Minecraft **1.21.1**, Create **6.0.x** (má balíčkovou logistiku: Packager, Stock Keeper,
  Frogport…), Mekanism 10.7+. Návody ze starších verzí často neplatí.
- **Almost Unified** sjednocuje kovy: priorita `minecraft > create > mekanism`. Skryté předměty jsou
  v `tools/registry/almostunified_hidden.txt` – ty nikdy nedávej jako úkol (validátor to hlídá).
  Např. ocel je `mekanism:ingot_steel`, ne ocel z Ad Astra nebo Big Cannons.
- Recepty platí z jarů, KROMĚ úprav v `kubejs/` (server_scripts: kolize receptů, duplicitní bedny; data: žíla platiny,
  zkušební komnaty). Validátor KubeJS nevidí – před psaním o receptu zkontroluj, jestli ho `kubejs/` nemění.
- Configy v repu, které mění hru: `config/quark-common.toml` (vypnuté funkce Quarku), `config/simulated-server.toml`.

## 3. Návrh questů

- **Úkoly se plní samy** – nikdy `check()` (zaškrtávátko). Povolené úkoly:
  `items=[(id, počet)]` (stačí mít v inventáři, nic se nebere), `kill(entita, n)`, `dim(dimenze)`,
  `biome(biom)`, `structure(struktura)`, `adv(advancement)` a `auto()` jen pro úvodní quest kapitoly
  (splní se hned – slouží jako „úvod“ s vysvětlením modu).
- **Návaznost odpovídá skutečnému postupu**: když k výrobě věci B potřebuješ věc A, quest B závisí na A.
  Kapitola má jasnou páteř (hlavní cestu) a z ní odbočky. Nováček jde shora dolů a ví, co dělat dál.
- Závislost na questu z jiné kapitoly: `dep=["create:brass"]` (formát `klíč_kapitoly:klíč_questu`).
  Smíš ji dát jen na **původní questy** (seznam v `baseline.json`, tvar `kapitola/quest`) nebo na questy
  ve svých vlastních kapitolách. Používej to střídmě, jen když je to opravdu potřeba (např. addony Create → mosaz).
- Milníky (velké kroky, např. první parní stroj) označ `shape="hexagon", size=1.5`. Nepovinné vedlejší
  questy `optional=True`.
- Počty v úkolech rozumné (ne 64 diamantů). XP odměna podle náročnosti 10–100. Žádné nové předmětové
  odměny (existující nech).
- Nedávej stejný předmět jako úkol do dvou questů (validátor upozorní `[dup]`), pokud to nemá jasný důvod.
- Kapitola ideálně do ~60 questů. Když je obsahu víc, založ další kapitolu ve své oblasti (nový unikátní
  `key`, česky `title` a `subtitle`, `group` z: start, create, tech, food, build, explore) a přidej ji do `CHAPTERS`.
- Úvodní quest každé kapitoly (`auto()`): co mod dělá, co se v kapitole naučíš, kde začít.

### Původní questy (musí zůstat!)
- Původní questy (`baseline.json`) **nesmíš smazat, přesunout do jiné kapitoly ani přejmenovat jejich klíč**
  a **nesmíš měnit jejich úkoly** (items/tasks) – hráči v nich mají postup. Nepřidávej jim ani nové úkoly.
- Smíš: přeložit/přepsat název, popis a podnázev do češtiny, opravit věcné chyby v popisu, změnit/přidat
  závislosti, ikonu, XP, tvar.
- Když je původní quest nesplnitelný nebo chybný, nech ho a napiš to do závěrečné zprávy
  (výjimky už povolené v `validate.py` → `TASK_FIXES` smíš opravit).

## 4. Technika

- Zdroj: `tools/quests-src/areas/<tvoje_oblast>.py` – **edituj jen svůj soubor**. Engine (`engine.py`),
  build, validátor ani cizí oblasti neměň. Pomocné funkce: `from engine import *` (Q, auto, dim, kill, biome,
  structure, adv).
- `Q(klíč, název, d=[...], items=[...], tasks=[...], dep=[...], xp=.., s=podnázev, icon=.., optional=.., shape=.., size=..)`
- Klíče questů: krátké, anglické, `snake_case`, unikátní v kapitole. Klíč kapitoly unikátní v celé knize.
- Předměty, které nemají recept ani loot table (validátor hlásí chybu), ale opravdu se dají získat
  (drop z moba, rybaření, výměna, generuje se ve světě…): přidej do slovníku `NO_RECIPE = {"mod:id": "jak se získá"}`
  na konci svého souboru – **jen pokud jsi to ověřil**. Jinak předmět nepoužívej.
- Validace (spouštěj často, na konci musí být **0 chyb** a projitá všechna varování):
  `cd tools/quests-src && python3 build.py --check --area <tvoje_oblast>`
- Varování „anglická slova“ může být falešné (anglický název mimo `&e…&r`) – pak dej název do `&e…&r`.

## 5. Kde najít pravdu (data)

`DB=/tmp/bombovo-refdata/db` – vytvoř ho příkazem `tools/refdata/rebuild.sh` (stáhne jary všech modů a rozbalí z nich data; trvá pár minut).

- `tools/registry/item_names.tsv` – všechna ID předmětů ze serveru + anglický a český název.
- `tools/registry/{entities,biomes,structures,dimensions,advancements}.txt` – registry ze serveru.
- `$DB/index/recipes.tsv` – výstup receptu → typ receptu → soubor. Recept pak čti v `$DB/<soubor>`.
- `$DB/data/<mod>/recipe/…` – recepty (crafting, create:mixing/pressing/sequenced_assembly, mekanism:…).
- `$DB/data/<mod>/loot_table/…` – dropy z bloků/mobů/truhel. `$DB/data/<mod>/worldgen/…` – struktury, biomy.
- `$DB/data/<mod>/advancement/…` a `$DB/index/advancement_titles.tsv` – advancementy (dobré na úkoly a nápady).
- `$DB/assets/<mod>/lang/en_us.json` – názvy, tooltipy a **ponder texty Create** (`create.ponder.*`), popisy mechanik.
- Průvodci uvnitř modů: `$DB/assets/*/patchouli_books`, `$DB/data/*/patchouli_books`, `$DB/assets/ae2/ae2guide`,
  `$DB/*/*/modonomicon` – výborný zdroj vysvětlení mechanik.
- Celé jary: `$DB/../jars/*.jar` (`unzip -l`, `unzip -p`, pro konstanty v kódu `javap -c -p`). Seznam modů: `mods/*.pw.toml`.
- Do jarů nic nezapisuj; pokud něco rozbalíš, tak do vlastní nové složky ve `$DB/../work/<oblast>/`.

## 6. Závěrečná zpráva (co vrátit)
Kapitoly (klíč, název, počet questů, z toho nových), které mody kapitoly pokrývají, mody z tvého přidělení,
které jsi vynechal a proč, všechny nejistoty a problémy původních questů. Výsledek validace (počet chyb/varování).

## 7. Kontrolní kolo (pro recenzenty)
Recenzent nepsal questy – čte je poprvé a opravuje přímo v souboru oblasti. Postup pro každý quest:
1. **Čeština:** pravopis (i/y, s/z, mě/mně, čárky před že/který/když/aby…, shoda podmětu s přísudkem), přirozená věta,
   žádné kalky z angličtiny, žádné anglické zbytky mimo `&e…&r`. Jednotná terminologie v celé oblasti
   (stejná věc = stejné české slovo). Text srozumitelný pro 10leté dítě – složité věty rozděl.
2. **Fakta:** u každého konkrétního tvrzení (suroviny, stroj, počty, kde se co najde, co blok dělá) si ověř v datech
   (recepty v `$DB`, lang, ponder, průvodci, `javap`). Špatné oprav, neověřitelné zobecni nebo smaž.
   Ověř i anglické názvy v `&e…&r` proti `en_name` v `tools/registry/item_names.tsv`.
3. **Návaznost:** pro item úkoly hlavní cesty zkontroluj, že suroviny z receptu (nebo stroj, který ho vyrábí) zavádí
   některý dřívější quest (přímá nebo nepřímá závislost), a že strom jde od začátečníka k expertovi. Chybějící
   závislosti doplň (jen v rámci pravidel bodu 3). Zkontroluj, že popis nesliboval, co quest neověřuje.
4. Původní questy (baseline.json): klíče, kapitoly a úkoly NEMĚNIT.
Na konci validace oblasti musí mít 0 chyb. Vrať seznam provedených oprav (stručně, po kategoriích) a co jsi nemohl ověřit.

## 8. Svět serveru – co je dosažitelné
Overworld je předgenerovaný (Chunky) a hráči nemají chodit za hranici světa. Úkoly `biome`/`structure` proto
smí mířit jen na cíle, které leží uvnitř – ověř to na serveru přes `/locate` (výsledky: `tools/registry/locate_results.txt`).
Detaily (velikost oblasti, hranice, známé problémy generování) jsou v `docs/modpack-knowledge.md`.
