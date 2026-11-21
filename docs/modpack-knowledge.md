# Filipovo Bombovo 2 – ověřená fakta o packu

Stav k 2026-11-21. Všechno tady bylo ověřeno v datech jarů (recepty, tagy, lang, kód přes `javap`),
v registrech ze serveru nebo přímo na serveru (`/locate`, logy). Kde něco ověřené není, je to napsané.

## Zdroje pravdy a nástroje

| Co | Kde |
|---|---|
| Registry ze serveru (předměty, entity, biomy, struktury, dimenze, advancementy) | `tools/registry/*.txt` (dump přes KubeJS, 2026-11-20) |
| Názvy předmětů (EN + CZ, pokud mod má češtinu) | `tools/registry/item_names.tsv` |
| Předměty s funkčním receptem nebo lootem (podmínky `neoforge:conditions` vyhodnocené) | `tools/registry/obtainable.txt` |
| Almost Unified – config a skryté předměty | `tools/registry/almostunified/`, `tools/registry/almostunified_hidden.txt` |
| Výsledky `/locate` (kde ve světě co je) | `tools/registry/locate_results.txt` |
| Configy ze serveru, které nejsou v packu | `tools/registry/configs/` |
| Rozbalená data všech jarů (recepty, lang, průvodci…) | `tools/refdata/rebuild.sh` → `/tmp/bombovo-refdata/db` |
| Kolize receptů (analýza) | `tools/refdata/recipe_conflicts_impact.txt`, `tools/refdata/crafting_conflicts.tsv` |

Na serveru nejsou žádné KubeJS skripty ani datapacky kromě těch v repu (`kubejs/`). Server běží v Dockeru
(`server/`), pack si stahuje přes packwiz při každém restartu.
Zálohy (neřešit, spravuje uživatel): 4:20 `scripts/backup.sh` (tar světa), 4:50 rclone na Google Disk, k tomu Simple Backups
(každých 120 min). **Noční restart (od 22.11.):** cron hosta 4:55 → `scripts/nightly-restart.sh` (varování hráčům, restart
v 5:00, ~1,5 min, při něm se stáhne aktuální pack). Compose na hostu: `/srv/gameservers/minecraft-modpack-03/`
(kontejner `minecraft_server_03`, `stop_grace_period: 3m`). Proti pádům kvůli chybě
entity/bloku je v packu **Neruina** (přidána 21.11.; chybnou věc pozastaví a ohlásí místo pádu serveru). Při lagu
`/spark profiler` (Spark je v packu).

## Svět serveru

- Spawn: **X 1701, Z -620**.
- Overworld předgenerovaný Chunky: čtverec kolem spawnu, poloměr 5000 (hotovo 16.11.).
- **Přegenerování (schváleno 21.11.):** ponechávají se jen regiony `r.0..6 × r.-5..1` (bloky X 0..3583, Z -2560..1023),
  kde mají hráči všechny základny (hlavní oblast X 672..3023, Z -1040..879). Zbytek overworldu (region, entities, poi)
  se po záloze smaže a znovu předgeneruje do 6000. **Overworld hotový 21.11. 10:02** (564 001 chunků, 9 h 25 min,
  ~16,6 cps, TPS 20; stav v `tools/registry/pregen_status.txt`). Nether 2500 kolem 213/-78, Twilight 3000, Aether 3000
  a End 3000 čekají na večer. Záloha před regenerací: `backups/world-pre-regen-2026-11-21_0034` na serveru.
  Nether se nepřegenerovává (hráči v něm mají věci do ~560 bloků, portál u základny: OW [2288,-776] ↔ N [288,-96]).
- **Světová hranice nastavena 21.11.:** střed 1701.5/-619.5, šířka 12000 (ověřeno `/worldborder get` ve všech dimenzích). Hranice má ve všech dimenzích
  **stejnou velikost**, posouvá se jen střed podle `coordinate_scale` dimenze (Nether střed /8, Twilight ×8).
- **Twilight Forest má `coordinate_scale` 0.125** → souřadnice v Twilightu = overworld × 8. Obsah, kam vede portál
  od spawnu, je kolem X 13600, Z -5000. Portály postavené daleko od spawnu skončí na okraji Twilight hranice.
- Hráči jsou 4, server je pomalý na generování nových chunků → questy smí cílit jen na místa uvnitř předgenerované oblasti.

### Generování – známé problémy
- **Aero Islands (aeroscapes)** přepisuje `minecraft:dimension/overworld`, ale vyhrává Terralith → biomy Aero Islands
  (`deep_voidsea` se negeneruje vůbec, `hallowed_isles` jen daleko) a jeho létající ostrovy prakticky nejsou.
  Aero Islands navíc přesunul **zkušební komnaty** do `deep_voidsea` → v původně vygenerované oblasti nejsou žádné.
  Oprava: `kubejs/data/minecraft/worldgen/structure*/trial_chambers.json` (vanilla) – platí jen pro nové chunky.
- **Alex's Caves s Tectonic/Terralith**: Toxic Caves, Primordial Caves a Candy Cavity potřebují extrémní kontinentálnost,
  která se skoro negeneruje. Config v packu (`config/alexscaves_biome_generation/*.json`) podmínky uvolňuje → objevují se
  v chuncích generovaných po změně (b4ff20b). V chuncích vygenerovaných dřív jsou jen Magnetic Caves a Forlorn Hollows;
  `/locate` a mapy jeskyní (Cave Map) tam hlásí i biomy, které tam ve skutečnosti nejsou („duchové“). Po regeneraci
  se v kole 5 (locate z 9 bodů) žádný duch v ponechané oblasti neobjevil. Ověřené výskyty (offline v .mca) jsou
  v `tools/registry/locate_results.txt` (kolo 5) a v popisech questů Alex's Caves.
- Kolo 5: všechny cíle questů v overworldu jsou do 6000 od spawnu (nejdál Desert Oasis 5728, Haunted Manor 5364).
- **Abyssal Chasm v našem světě není.** Port Alex's Caves 2.0.10 má v `MultiNoiseBiomeSourceMixin` natvrdo podmínku
  continentalness ≤ -0.5 (jen pod hlubokým oceánem), config ji neobejde. V oblasti ~20000×20000 je jediný výskyt
  kolem [-2300, -8300], mimo hranici. Questy větve Abyssal a Tremorzilla (vejce potřebuje Immortal Embryo, padá jen
  z Hullbreakera) byly odebrány (nikdo je neměl splněné). Změna Tectonic `ocean_offset` by změnila povrch → nezkoušeno.
- **Medieval Buildings** (overworld) má biome tagy odkazující na neexistující biomy (BOP, BWG, Regions Unexplored) →
  stavby se nejspíš negenerují. End Edition (`medievalend:*`) funguje.
- Deep dark a starověká města: `deep_dark` je 492 bloků od spawnu. `/locate structure minecraft:ancient_city` je extrémně
  pomalý (přes 17 min) – nepouštět.
- Daleko od spawnu (mimo hranici 6000): čarodějnická chýše (YUNG), labyrint a Ancient Mines (IDAS), džunglová pevnost
  (Repurposed Structures), hrad `create_ltab:thecastle`.

## Recepty a předměty

- **Almost Unified**: priorita `minecraft > kubejs > create > mekanism`, sjednocuje ingoty, nugety, prachy, pláty, rudy…
  Ocel = `mekanism:ingot_steel` (ocel z Ad Astra a Big Cannons je skrytá). `loot_unification` je vypnuté.
- **Create Waystones Recipes** přepisuje recepty Waystones → waystone, warp stone, svitky a warp plate se dělají
  v mechanickém crafteru Create.
- **Create Food** přepisuje velkou část receptů Farmer's Delight (hamburger, mleté maso, těsto, jablečný koláč…);
  ExtraDelight vypíná FD rybí guláš v hrnci. Pořadí přepisů: createfood > rusticdelight > extradelight > FD (odvozeno).
- **Abnormals Delight**: fungují jen recepty s Autumnity a Upgrade Aquatic (ostatní Abnormals mody v packu nejsou).
- **Kolize receptů**: `kubejs/server_scripts/recipe_conflicts.js` opravuje ~95 kolizí mimo pracovní stůl (pec, udírna,
  táborák, prkénko, hrnec, odšťavňovač, stroje Create). Pracovní stůl řeší Polymorph (306 kolizí, výběr šipkami).
  **FastFurnace** si v peci pamatuje první recept a výběr Polymorphu ignoruje → kolize v peci musí řešit skript.
  Duplicitní úložné bedny/pytle (auto-compacting Create): `kubejs/server_scripts/storage_duplicates.js` – zůstává bedna
  z Farmer's Delight / Fruits Delight / Ender's Delight / Mekanism, ostatním odebrán jen recept na výrobu (rozbalení zůstává);
  kukuřice, chilli a káva berou jen surovinu svého modu. Ostatní kolize v mechanickém crafteru (hlavně dekorace) neřešené,
  seznam v `tools/refdata/crafting_conflicts.tsv`.
- Stůl z Handcrafted a Another Furniture mají stejný tvar (`###|/ /`) – řeší Polymorph.
- **Just In Nether**: kruorit a devourit nemají v packu využití jako surovina; ve vysoké peci (z Kindarx / Pigar) dávají
  20 XP za kus. Modulární zbraně z nich dělá Just In Blacksmith – **záměrně nepřidán** (2026-11-21): zbraně výrazně silnější
  než vanilla (železná sekera +14, diamantová +22 poškození) a v jaru je testovací materiál se 99 poškozením.
- **Luminous**: Luminous Overworld vypíná spawn motýlů z Luminous Butterflies; netherové bestie Luminous Nether se
  nespawnují, když je nainstalovaný Luminous Beasts (jsou jen jejich verze); Gilded Piglin trofej nejde získat.
- Nesbíratelné předměty: levitit (Create Aeronautics, zmizí při rozbití), ponorka z Alex's Caves (jen creative),
  aerolit (padá jako větvičky), `interiors:wall_mounted_table` (recept ve staré cestě `recipes/`, nenačte se).

## Configy packu (rozhodnutí)
- Quark: Totem of Holding vypnutý (po smrti jen tělo z Corpse). Automatic Tool Restock a Variant Selector vypnuté.
  Matrix Enchanting zapnutý (nahrazuje očarovávací stůl), Stonelingové zapnutí (Heart of Diamond).
- Mekanism: výbuch jaderného reaktoru zapnutý (výchozí), hlasový server vysílaček vypnutý (výchozí).
- MineColonies: advancementy dostává jen majitel a důstojníci kolonie (21 questů je používá).

## Ověřená čísla (výchozí configy)
**Create 6.0.10** (javap):
- Kapacita zdrojů (SU na 1 RPM): ruční klika 8 (32 RPM → 256 SU), mlýnské kolo 32 (8 RPM → 256 SU),
  velké mlýnské kolo 128 (4 RPM → 512 SU), větrný mlýn 512 (RPM = plachty/8, min. 8 plachet, max. 16 RPM),
  parní motor 1024 (plný výkon 64 RPM = 16 384 SU).
- Dopad strojů (SU/RPM): lis a drtící kolo 8; míchačka, mlýnský kámen, vrták, pila, pokladač, čerpadlo 4;
  větrák, mechanická paže, mechanický crafter 2. Max. rychlost 256 RPM.
- Kotel: úroveň = minimum z (teplo: 1 za hořák s palivem, 2 za přehřátý; velikost: 1 za 4 bloky nádrže;
  voda: 10 mB/tick na úroveň), max. 18. Pasivní ohřev = 1/8 výkonu. Čerpadlo dá |RPM|/2 mB/tick (256 RPM ≈ 12 úrovní).
- Praní štěrku: 25 % pazourek, 12,5 % železný nuget. Precizní mechanismus: 5 průchodů, 80 % úspěšnost.
**Mekanism**: zpracování rud – blok rudy 2/3/4/5×, vytěžená ruda 3 → 4/8/10. Fission reactor poškození nad 1200 K.
Teleportér: rám 3×4 s otvorem 1×2 (9 bloků rámu + teleportér dole uprostřed). Turbína: lichá délka strany půdorysu.
**AE2**: kanály 8 / 32 (dense), 63 typů na buňku, 2 FE = 1 AE.

## Klávesy (z `options.txt`)
JEI: R recept, U použití, A záložka; Jade: num 0; Xaero: M mapa, N waypoint, U/Y; Corpse: J historie smrtí;
Sophisticated Backpacks: B; Supplementaries toulec: V; Ping Wheel: boční tlačítko myši 5; jetpack Mekanism: G.
Hra je výchozí v angličtině (`lang:en_us`) – questy jsou česky a uvádějí i anglické názvy předmětů.

## FTB Quests – jak je udržovat
Viz `tools/quests-src/GUIDE.md`. Shrnutí: zdroj je `tools/quests-src/areas/*.py`, build
`python3 tools/quests-src/build.py --check` (validace) a `tools/install-quests.sh` (instalace + packwiz refresh).
Původní questy (`baseline.json`) se nesmí mazat ani měnit jejich úkoly – hráči v nich mají postup (ID se počítá
z klíče kapitoly a questu). Progression mode je „flexible“.
**Vlastní jména se nepřekládají** (mody, dimenze, biomy, stavby, bossové, mobové z modů, jednotky) – hra běží anglicky.
Validátor to hlídá přes `tools/registry/names_en.tsv` (generuje `tools/refdata/names_en.py`) a `PROPER_NAMES_CZ`.
Terralith, Incendium a některé stavby nemají lang – jejich anglické názvy jsou odvozené z ID.
