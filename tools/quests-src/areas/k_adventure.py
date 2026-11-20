from engine import *

# Úrovně: milníky (hexagon) mají v podnázvu „Začátečník“, „Pokročilý“ nebo „Expert“.
M = dict(shape="hexagon", size=1.5)

# ---------------------------------------------------------------- ALEX'S CAVES
ALEXSCAVES = dict(
    key="alexs_caves", group="explore", title="Alex's Caves",
    subtitle="Šest vzácných jeskyní hluboko pod zemí", icon="alexscaves:cave_tablet",
    quests=[
        # ---------- Začátečník: jak jeskyně najít
        Q("intro", "Alex's Caves", tasks=[auto()], icon="alexscaves:cave_book", xp=10, s="Začátečník", **M, d=[
            "&bAlex's Caves&r přidává šest vzácných jeskynních biomů hluboko pod zemí.",
            "Každý biom má vlastní tvory, suroviny, výbavu a bosse. Některé jsou velmi nebezpečné.",
            "Tady se naučíš jeskyně najít, přežít v nich a nakonec porazit jejich bosse.",
            "&aTip: Začni hledáním podzemní chatky. Jsou v ní kamenné tabulky, které tě k jeskyním dovedou.&r"]),
        Q("cabin", "Podzemní chatka", dep=["intro"], tasks=[structure("alexscaves:underground_cabin")], icon="minecraft:spruce_door", xp=20, d=[
            "Podzemní chatky jsou malé dřevěné domky v obyčejných jeskyních.",
            "Najdeš je při průzkumu jeskyní. Mapu k chatce ti někdy prodá kartograf (vesničan) nebo ji najdeš v truhle v opuštěném dole.",
            "&aV truhlách chatky bývají kamenné tabulky a někdy i kniha jeskyní.&r"]),
        Q("tablet", "Kamenná tabulka", dep=["cabin"], items=[("alexscaves:cave_tablet", 1)], xp=30, d=[
            "Kamenná tabulka (&eCave Tablet&r) je zápis o jednom jeskynním biomu.",
            "Najdeš ji v truhlách podzemních chatek a v ruinách uvnitř jeskynních biomů.",
            "Sama ti cestu neukáže. Musíš ji přeložit na stole (&eSpelunkery Table&r)."]),
        Q("spelunkery", "Stůl na překlady", dep=["cabin"], items=[("alexscaves:spelunkery_table", 1)], xp=20, d=[
            "Stůl na překlady (&eSpelunkery Table&r) nejde vyrobit. Najdeš ho jen v podzemní chatce.",
            "Vytěž ho a odnes si ho domů."]),
        Q("codex", "Přelož tabulku", dep=["tablet", "spelunkery"], tasks=[adv("alexscaves:alexscaves/cave_codex")], icon="alexscaves:cave_codex", xp=30, d=[
            "Na stůl polož tabulku a papír. Na tabulce se ukážou runy.",
            "Kliknutím runu odhalíš. Když přes slovo přejedeš lupou, uvidíš jeho překlad.",
            "&cMáš jen 5 pokusů, pak se tabulka zničí.&r",
            "Když hledané slovo uhodneš třikrát, vznikne kodex (&eCave Codex&r)."]),
        Q("map", "Mapa jeskyně", dep=["codex"], tasks=[adv("alexscaves:alexscaves/cave_map")], icon="alexscaves:cave_map", xp=40, s="Pokročilý", **M, d=[
            "Kodex dej doprostřed pracovního stolu a kolem něj 8 papírů. Vznikne mapa jeskyně (&eCave Biome Map&r).",
            "Mapa ukazuje cestu k nejbližšímu biomu, o kterém je kodex. Chvíli trvá, než ho najde.",
            "Teď už nehledáš naslepo. Vyber si biom a vydej se tam! Každý biom je samostatná větev této kapitoly."]),
        Q("book", "Kniha jeskyní", dep=["tablet"], items=[("alexscaves:cave_book", 1)], xp=20, d=[
            "Kniha jeskyní (&eCave Compendium&r) je průvodce všemi šesti biomy přímo ve hře.",
            "Vyrobíš ji z knihy, kamenné tabulky a zlatého nugetu.",
            "&aKaždý kodex ti v ní odemkne víc informací o svém biomu.&r"]),

        # ---------- Magnetické jeskyně
        Q("magnetic_enter", "Magnetické jeskyně", dep=["map"], tasks=[biome("alexscaves:magnetic_caves")], icon="alexscaves:galena", xp=40, d=[
            "Magnetické jeskyně jsou z šedého kamene galenitu (&eGalena&r) a rostou v nich obří krystaly.",
            "Rudé neodymové krystaly přitahují kovové věci, modré je odpuzují.",
            "&cŽelezná a netheritová výbava tě tu bude přitahovat i odstrkovat. Lepší je nekovová výbava.&r",
            "&cTeslovy baňky (&eTesla Bulb&r) dávají rány bleskem a při rozbití vybuchují.&r"]),
        Q("magnetic", "Neodym", dep=["magnetic_enter"], items=[("alexscaves:raw_scarlet_neodymium", 1), ("alexscaves:raw_azure_neodymium", 1)], xp=40, d=[
            "Surový neodym získáš rozbíjením krystalů (sloupů a uzlů) v magnetických jeskyních.",
            "Padá i z Teletora, létajícího nepřítele se železnou zbraní nad hlavou.",
            "&aTip: Galenit obsahuje železo. Z 9 galenitu je lisovaný galenit (&ePacked Galena&r), který se v peci přetaví na železný nuget.&r"]),
        Q("neodymium_ingot", "Neodymové ingoty", dep=["magnetic"], items=[("alexscaves:scarlet_neodymium_ingot", 1), ("alexscaves:azure_neodymium_ingot", 1)], xp=30, d=[
            "Do pracovního stolu dej 3 kusy surového neodymu a 3 železné ingoty. Vznikne 1 neodymový ingot (&eScarlet Neodymium Ingot&r nebo &eAzure Neodymium Ingot&r).",
            "Ingoty jsou základ všech magnetických věcí."]),
        Q("magnets", "Magnety", dep=["neodymium_ingot"], items=[("alexscaves:scarlet_magnet", 1), ("alexscaves:azure_magnet", 1)], xp=40, d=[
            "Rudý magnet (&eScarlet Magnet&r) přitahuje kovové bloky, modrý (&eAzure Magnet&r) je odpuzuje.",
            "Pohne až 27 bloky najednou. Musí být kovové, nebo k nim přilepené slizovým blokem.",
            "&aDosah magnetu zvětšíš ingotem stejné barvy, ingotem opačné barvy ho zmenšíš.&r"]),
        Q("maglev", "Levitační kolej", dep=["neodymium_ingot"], items=[("alexscaves:magnetic_levitation_rail", 6)], xp=25, optional=True, d=[
            "Levitační kolej (&eMagnetic Levitation Rail&r) zvedne vozík do vzduchu. Vozík na ní jede rychleji než na obyčejné koleji.",
            "Ze 2 modrých neodymových ingotů, 6 železných ingotů a tyčky vyrobíš 6 kolejí."]),
        Q("teletor", "Telecore", dep=["magnetic_enter"], items=[("alexscaves:telecore", 1)], xp=30, d=[
            "Teletor je nepřítel, který se vznáší a ovládá železnou zbraň nad hlavou. Útočí s ní i z dálky.",
            "Po zabití z něj padá &eTelecore&r a někdy i surový neodym."]),
        Q("gauntlet", "Galenitová rukavice", dep=["teletor", "neodymium_ingot"], items=[("alexscaves:galena_gauntlet", 1)], xp=50, d=[
            "Galenitová rukavice (&eGalena Gauntlet&r) se drží v druhé ruce. V hlavní ruce měj železný nebo netheritový nástroj.",
            "Rukavice ho vystřelí asi 20 bloků daleko. Nástroj zraní moby nebo sám těží bloky, na které je určený.",
            "Vyrobíš ji z lisovaného galenitu, &eTelecore&r, rudého neodymového ingotu a slizu &eFerrouslimeball&r (padá z Ferrouslime)."]),
        Q("magnetron", "Magnetron", dep=["magnetic"], tasks=[kill("alexscaves:magnetron")], icon="alexscaves:heart_of_iron", xp=100, s="Expert", **M, d=[
            "Teď už nejde o průzkum, ale o boj s bossem. Magnetron je vzácný a silný strážce magnetických jeskyní.",
            "Zpočátku se jen nenápadně kutálí.",
            "Když tě uvidí, postaví si z okolních bloků obří tělo. &cKovadliny a pily v okolí použije jako zbraně.&r",
            "Po smrti se rozpadne a zůstane po něm srdce ze železa (&eHeart of Iron&r)."]),
        Q("resistor_shield", "Odporový štít", dep=["magnetron", "neodymium_ingot"], items=[("alexscaves:resistor_shield", 1)], xp=60, d=[
            "Odporový štít (&eResistor Shield&r) chrání jako běžný štít. Když se jím bráníš, vysílá magnetický puls, který zraňuje okolní nepřátele.",
            "Když se kryješ a držíš Shift, přepneš, jestli puls nepřátele odhazuje (modrá), nebo přitahuje (rudá)."]),
        Q("quarry", "Magnetický lom", dep=["magnetron", "neodymium_ingot"], items=[("alexscaves:quarry", 1), ("alexscaves:quarry_smasher", 1)], xp=80, d=[
            "Magnetický lom (&eMagnetic Quarry&r) sám vytěží celou oblast až dolů.",
            "Za blok lomu dej do obdélníku 4 magnetická světla (&eMagnetic Light&r). Až mezi nimi přeskakují blesky, polož dovnitř drtič (&eMagnetic Quarry Smasher&r).",
            "Světla vyrobíš z &eNotor Gizmo&r (padá z Notora) a železa. Drtič potřebuje &eHeavyweight&r z Boundroida.",
            "Vytěžené věci vylétají horem z bloku lomu."]),

        # ---------- Pravěké jeskyně
        Q("primordial_enter", "Pravěké jeskyně", dep=["map"], tasks=[biome("alexscaves:primordial_caves")], icon="alexscaves:limestone", xp=40, d=[
            "Pravěké jeskyně jsou obří jeskyně z vápence (&eLimestone&r). Jantar na stropě je osvětluje jako ve dne, proto se tu nespawnují příšery.",
            "Žijí tu dinosauři! Býložravci jsou klidní, dokud na ně nezaútočíš.",
            "&cDravci jako Vallumraptor (loví ve smečkách) nebo obří Tremorsaurus útočí i na tebe.&r"]),
        Q("primordial", "Jantar a maso", dep=["primordial_enter"], items=[("alexscaves:amber", 1), ("alexscaves:dinosaur_chop", 1)], xp=40, d=[
            "Jantar (&eAmber&r) visí ze stropu jeskyně. Vytěžíš ho jen krumpáčem s očarováním Hedvábný dotek, jinak z něj nic nepadne. Dinosauří maso (&eDinosaur Chop&r) padá z velkých dinosaurů.",
            "Maso si opeč. &aZ opečeného masa vyrobíš 12 dinosauřích nugetek (&eDinosaur Nugget&r).&r"]),
        Q("tree_star", "Stromová hvězda", dep=["primordial_enter"], items=[("alexscaves:tree_star", 1)], xp=20, d=[
            "Stromová hvězda (&eTree Star&r) roste na pradávných stromech.",
            "Je to oblíbené jídlo mnoha dinosaurů. Grottoceratopse s ní rozmnožíš."]),
        Q("salad", "Uklidňující salát", dep=["tree_star"], items=[("alexscaves:serene_salad", 1)], xp=30, d=[
            "Uklidňující salát (&eSerene Salad&r) ruší omráčení a pomáhá ochočit některé dinosaury.",
            "Recept: kapradinový výhonek (&eFiddlehead&r), stromová hvězda, piniové oříšky (&ePine Nuts&r) a miska.",
            "Výhonky získáš jen od Grottoceratopse, když sní kudrnatou kapradinu (&eCurly Fern&r).",
            "&aVallumraptora ochočíš takto: dej do truhly nugetky. Když si je ukradne a sní, může se uklidnit. Pak mu dej salát.&r"]),
        Q("subterranodon", "Létající ještěr", dep=["primordial_enter"], tasks=[adv("alexscaves:alexscaves/tame_subterranodon")], icon="alexscaves:subterranodon_egg", xp=40, optional=True, d=[
            "Subterranodona ochočíš několika syrovými ocasy trilokarise (&eRaw Trilocaris Tail&r).",
            "Pravým tlačítkem na něj nasedneš a nese tě. Nahoru letí jen chvíli, pak musí přistát.",
            "Shift + pravé tlačítko přepíná: následuj / zůstaň / volně se pohybuj."]),
        Q("club", "Pravěký kyj", dep=["primordial"], items=[("alexscaves:primitive_club", 1)], xp=30, d=[
            "Pravěký kyj (&ePrimitive Club&r) je pomalá zbraň, která může cíl omráčit až na 15 sekund.",
            "Vyrobíš ho z těžké kosti (&eHeavy Bone&r) a dvou cykasů (&eCycad&r). Těžké kosti padají z velkých dinosaurů.",
            "&aTremorsaura ochočíš tak, že ho kyjem omráčíš a hned mu dáš salát. Musíš to zkusit několikrát.&r"]),
        Q("primordial_armor", "Pravěká zbroj", dep=["club"], items=[("alexscaves:primordial_helmet", 1), ("alexscaves:primordial_tunic", 1), ("alexscaves:primordial_pants", 1)], xp=40, d=[
            "Pravěkou zbroj vyrobíš z tvrdé kůže (&eTough Hide&r), kostních bloků a těžkých kostí. Tvrdá kůže padá z Grottoceratopse.",
            "Každý kus zvýší, kolik zdraví a nasycení ti dá syrové maso."]),
        Q("catalyst", "Zlověstný katalyzátor", dep=["club"], items=[("alexscaves:ominous_catalyst", 1)], xp=50, d=[
            "Zlověstný katalyzátor (&eOminous Catalyst&r) vyrobíš z 8 těžkých kostí a jantarové zvláštnosti (&eAmber Curiosity&r).",
            "Jantarová zvláštnost vzácně vypadne při těžbě jantaru (i bez Hedvábného doteku).",
            "&cKatalyzátor hozený do kráteru sopky v pravěké jeskyni probudí bosse. Připrav se dobře!&r"]),
        Q("luxtructosaurus", "Luxtructosaurus", dep=["catalyst"], tasks=[kill("alexscaves:luxtructosaurus")], icon="alexscaves:tectonic_shard", xp=100, s="Expert", **M, d=[
            "Luxtructosaurus je nemrtvý dinosaurus zavřený v sopce. Má 600 bodů zdraví a oheň mu neublíží.",
            "&cDupe, kope a máchá ocasem, který ti vyřadí štít. Když zuří, chrlí oheň. Během boje sopky kolem vybuchují.&r",
            "Po smrti z něj zbudou tektonické úlomky (&eTectonic Shard&r)."]),
        Q("extinction_spear", "Kopí vyhynutí", dep=["luxtructosaurus"], items=[("alexscaves:extinction_spear", 1)], xp=80, d=[
            "Kopí vyhynutí (&eExtinction Spear&r) je nejsilnější zbraň pravěkých jeskyní.",
            "Vyrobíš ho z tektonických úlomků, vápencového kopí (&eLimestone Spear&r), jantarové zvláštnosti a těžké kosti.",
            "Při zásahu zaútočí duch dinosaura. Hozené kopí vybuchne a vrátí se ti do ruky."]),

        # ---------- Toxické jeskyně
        Q("toxic_enter", "Toxické jeskyně", dep=["map"], tasks=[biome("alexscaves:toxic_caves")], icon="alexscaves:radrock", xp=40, d=[
            "Toxické jeskyně jsou radioaktivní pustina z kamene &eRadrock&r.",
            "&cJezírka kyseliny ničí brnění a pak i tebe. Radioaktivní věci ti dají efekt ozáření (&eIrradiated&c): zastaví léčení a silnější ozáření tě zraňuje.&r",
            "&aJídlo ze sirného prachu (&eSulfur Dust&r) tě léčí i při ozáření.&r"]),
        Q("toxic", "Uran", dep=["toxic_enter"], items=[("alexscaves:uranium", 1)], xp=40, d=[
            "Uran (&eUranium&r) získáš z uranové rudy (&eRadrock Uranium Ore&r), která je v radrocku.",
            "Uran je palivo a surovina pro všechny jaderné věci tohoto biomu."]),
        Q("polymer", "Polymerová deska", dep=["toxic"], items=[("alexscaves:polymer_plate", 4)], xp=40, d=[
            "Polymerová deska (&ePolymer Plate&r) je velmi odolný materiál.",
            "Recept: toxická pasta (&eToxic Paste&r, padá z Gammaroache), láhev radonu (&eBottle of Radon&r), sirný prach a železný ingot. Vzniknou 4 desky.",
            "Radon nabereš prázdnou lahví z geotermálního průduchu, ze kterého stoupá zelený plyn. Sirný prach vytěžíš ze sirných krystalů."]),
        Q("hazmat", "Ochranný oblek", dep=["polymer"], items=[("alexscaves:hazmat_mask", 1), ("alexscaves:hazmat_chestplate", 1), ("alexscaves:hazmat_leggings", 1), ("alexscaves:hazmat_boots", 1)], xp=80, d=[
            "Ochranný oblek (&eHazmat Mask&r, &eHazmat Chestplate&r, &eHazmat Leggings&r, &eHazmat Boots&r) snižuje poškození a účinky ozáření i kyseliny.",
            "Celý oblek potřebuje 24 polymerových desek.",
            "&aKusy obleku občas najdeš i v truhlách toxických ruin.&r"]),
        Q("nucleeper", "Nucleeper", dep=["toxic_enter"], items=[("alexscaves:fissile_core", 1)], xp=50, d=[
            "Nucleeper je jaderný creeper. Před výbuchem se mu zavírá jádro, houká siréna a bliká.",
            "&cMusíš ho zabít dřív, než se jádro zavře. Jeho výbuch je atomový!&r",
            "Někdy z něj padne štěpné jádro (&eFissile Core&r)."]),
        Q("uranium_rod", "Uranová tyč", dep=["toxic"], items=[("alexscaves:uranium_rod", 1)], xp=30, d=[
            "Uranová tyč (&eUranium Rod&r) svítí a slouží jako jaderné palivo.",
            "Vyrobíš ji z 6 uranu, 2 železných ingotů a ohnivé tyče."]),
        Q("raygun", "Paprsková pistole", dep=["polymer", "nucleeper", "uranium_rod"], items=[("alexscaves:raygun", 1)], xp=80, d=[
            "Paprsková pistole (&eRaygun&r) střílí radioaktivní paprsek. Jeden zásah ubere jen 1 bod zdraví, ale útočí 4× rychleji než běžná zbraň.",
            "Cíl dostane ozáření. Jako střelivo spotřebovává uranové tyče."]),
        Q("nuclear_furnace", "Jaderná pec", dep=["uranium_rod"], items=[("alexscaves:nuclear_furnace_component", 8), ("alexscaves:metal_barrel", 1)], xp=60, d=[
            "Jaderná pec taví všechno, co vysoká pec, ale 5× rychleji.",
            "Postav ji z 8 dílů (&eNuclear Furnace Component&r) do kostky 2×2×2. Díly jsou z uranu, vysoké pece a zuhelnatělých zbytků (&eCharred Remnant&r, padají z Brainiaca).",
            "Palivem jsou uranové tyče. Jedna utaví celý stack, ale vzniká odpad.",
            "&cDo pece vkládej kovové sudy (&eMetal Barrel&r). Odpad se do nich uloží. Jinak pec vybuchne!&r",
            "Kovový sud vyrobíš z obyčejného sudu a 8 železných ingotů."]),
        Q("nuclear_bomb", "Jaderná bomba", dep=["nucleeper", "uranium_rod"], items=[("alexscaves:nuclear_bomb", 1)], xp=60, optional=True, d=[
            "Jaderná bomba (&eNuclear Bomb&r) zničí obrovské okolí a všechny kolem ozáří.",
            "&cNikdy ji neodpaluj blízko své nebo cizí základny!&r",
            "&aZapálenou bombu ještě zneškodníš: klikni na ni pravým tlačítkem s nůžkami.&r"]),
        Q("tremorzilla_egg", "Vejce Tremorzilly", dep=["luxtructosaurus", "hullbreaker", "nuclear_bomb"], items=[("alexscaves:tremorzilla_egg", 1)], xp=100, d=[
            "Vejce Tremorzilly (&eTremorzilla Egg&r) složíš z tektonických úlomků, nesmrtelného embrya (&eImmortal Embryo&r) a vejce Tremorsaura.",
            "Vejce Tremorsaura získáš, když dvěma ochočeným Tremorsaurům dáš dinosauří maso.",
            "Vejce se samo nikdy nevylíhne. Vylíhne se jen díky jadernému výbuchu poblíž."]),
        Q("tremorzilla", "Král příšer", dep=["tremorzilla_egg", "nuclear_furnace"], tasks=[adv("alexscaves:alexscaves/tame_tremorzilla")], icon="alexscaves:waste_drum", xp=100, s="Expert", **M, d=[
            "Tremorzilla je obří radioaktivní dinosaurus s ničivým paprskem.",
            "Ochočíš ji krmením sudů s odpadem (&eWaste Drum&r). Ty vznikají v jaderné peci.",
            "Ochočenou Tremorzillu můžeš osedlat a ovládat její paprsek."]),

        # ---------- Propastná rokle
        Q("abyssal_enter", "Propastná rokle", dep=["map"], tasks=[biome("alexscaves:abyssal_chasm")], icon="alexscaves:abyssmarine", xp=40, d=[
            "Propastná rokle je obří příkop pod oceánem. Nad tebou jsou stovky bloků vody a skoro úplná tma.",
            "&cPotřebuješ dýchat pod vodou: lektvar dýchání pod vodou, potápěčskou helmu nebo ponorku.&r",
            "Dno pokrývá kal (&eMuck&r), který tě zpomaluje."]),
        Q("abyssal", "Mořské sklo", dep=["abyssal_enter"], items=[("alexscaves:sea_glass_shards", 1)], xp=40, d=[
            "Úlomky mořského skla (&eSea Glass Shards&r) občas vypadnou při těžbě kalu.",
            "Spojíš je zpátky ve sklo, nebo z nich vyrobíš hlubinné sklo."]),
        Q("depth_glass", "Hlubinné sklo", dep=["abyssal"], items=[("alexscaves:depth_glass", 6)], xp=30, d=[
            "Přes hlubinné sklo (&eDepth Glass&r) je ve vodě lépe vidět.",
            "Z 5 úlomků mořského skla a 4 železných ingotů vznikne 8 skel.",
            "Šest kusů budeš potřebovat na stavbu ponorky."]),
        Q("diving", "Potápěčský oblek", dep=["abyssal_enter"], items=[("alexscaves:diving_helmet", 1), ("alexscaves:diving_chestplate", 1), ("alexscaves:diving_leggings", 1), ("alexscaves:diving_boots", 1)], xp=80, d=[
            "Potápěčský oblek (&eDiving Helmet&r, &eDiving Chestplate&r, &eDiving Leggings&r, &eDiving Boots&r) nejde vyrobit.",
            "Nosí ho utopenci v rokli a najdeš ho v truhlách podvodních ruin.",
            "Helma prodlužuje dýchání pod vodou, kalhoty zrychlují plavání a boty chůzi po kalu."]),
        Q("biolum", "Podvodní pochodně", dep=["abyssal_enter"], items=[("alexscaves:bioluminescent_torch", 4)], xp=25, d=[
            "Svítící červ (Gossamer Worm) upustí bioluminiscenci (&eBioluminesscence&r).",
            "Z ní a tyčky vyrobíš 4 pochodně (&eBioluminescent Torch&r), které svítí i pod vodou.",
            "&aZ bioluminiscence a mořských hub (&ePing-Pong Sponge&r) je i plovák (&eFloater&r), který tě rychle vynese k hladině.&r"]),
        Q("altar", "Propastný oltář", dep=["abyssal"], items=[("alexscaves:abyssal_altar", 1)], xp=30, d=[
            "Perla (&ePearl&r) občas vypadne z mušle (&eMussel&r). Mušle rostou na pevných blocích na dně.",
            "Oltář (&eAbyssal Altar&r) vyrobíš z perly a 4 bloků &eAbyssmarine&r."]),
        Q("deep_ones", "Hlubinní", dep=["altar"], tasks=[adv("alexscaves:alexscaves/trade_with_deep_one")], icon="alexscaves:pearl", xp=50, d=[
            "Hlubinní (Deep One) jsou tajemní obyvatelé rokle. Zpočátku tě sledují a utíkají před tebou.",
            "Když jsou blízko, polož na oltář perlu. Přinesou ti za ni něco na výměnu.",
            "Čím víc obchoduješ, tím víc tě mají rádi. Nakonec ti i pomáhají v boji.",
            "&cKdyž některého zraníš, všichni tě budou mít rádi míň a nakonec zaútočí.&r"]),
        Q("deep_gear", "Zbraně z hlubin", dep=["deep_ones"], items=[("alexscaves:ortholance", 1)], xp=40, optional=True, d=[
            "Rytíři hlubin nabízejí ve výměně kopí (&eOrtholance&r) a kouzelnou lasturu (&eMagic Conch&r). Mágové nabízejí hůl (&eSea Staff&r).",
            "Kopí podržením nabiješ a vyrazíš vpřed s vlnou, která zraňuje. Lastura přivolá hlubinné na pomoc."]),
        Q("submarine", "Ponorka", dep=["depth_glass"], tasks=[adv("alexscaves:alexscaves/ride_submarine")], icon="alexscaves:enigmatic_engine", xp=60, d=[
            "Ponorka (&eSubmarine&r) je kabina, ve které se dá dýchat. Má i světlomety. Quest splníš, když do ní nasedneš (pravé tlačítko).",
            "Rozbitou ponorku najdeš v podvodních ruinách. Oprav ji měděnými ingoty, zelenou měď očisti sekerou.",
            "Novou postavíš: obal záhadný motor (&eEnigmatic Engine&r) kostkou z bloků mědi a na přední stranu dej 6 hlubinných skel.",
            "&cKdyž se blíží Hullbreaker, hned vypni světla!&r"]),
        Q("hullbreaker", "Hullbreaker", dep=["submarine"], tasks=[kill("alexscaves:hullbreaker")], icon="alexscaves:immortal_embryo", xp=100, s="Expert", **M, d=[
            "Hullbreaker je obří ryba, delší než 15 bloků, se 400 body zdraví.",
            "Loví podle světla. Láká ho všechno, co svítí, i efekt Záře. Než zaútočí, krouží kolem a bliká.",
            "Po smrti vyplivne, co snědl: záhadný motor (&eEnigmatic Engine&r) i nesmrtelné embryo (&eImmortal Embryo&r)."]),

        # ---------- Opuštěné dutiny
        Q("forlorn_enter", "Opuštěné dutiny", dep=["map"], tasks=[biome("alexscaves:forlorn_hollows")], icon="alexscaves:guanostone", xp=40, d=[
            "Opuštěné dutiny zahaluje nepřirozená tma. Země je z guanového kamene (&eGuanostone&r) a koprolitu (&eCoprolith&r).",
            "&cSvětlo přiláká můry (Gloomoth) a za nimi dravce. Kultisté (Underzealot) rozbíjejí pochodně.&r",
            "&aV guanovém kameni je redstonová ruda, v koprolitu uhlí.&r"]),
        Q("moth_ball", "Můří kulička", dep=["forlorn_enter"], items=[("alexscaves:moth_ball", 1)], xp=25, d=[
            "Můří kulička (&eMoth Ball&r) drží můry dál od světel.",
            "Recept: můří prach (&eMoth Dust&r, padá z můr), guáno (&eGuano&r) a 2 provázky.",
            "&aZe 2 guán a kostní moučky je hnojivo (&eFertilizer&r), které funguje líp než kostní moučka.&r"]),
        Q("occult_gem", "Okultní drahokam", dep=["forlorn_enter"], items=[("alexscaves:occult_gem", 1)], xp=40, d=[
            "Okultní drahokam (&eOccult Gem&r) padá z Watchera, nebo ho najdeš v truhlách ruin.",
            "Watcher vznikne, když kultisté obětují můru. &cUmí tě posednout: na chvíli vidíš jeho očima a nemůžeš se hýbat.&r",
            "&aZ drahokamu je i totem (&eTotem of Possession&r), kterým na chvíli ovládneš moba.&r"]),
        Q("forsaken", "Forsaken", dep=["forlorn_enter"], tasks=[kill("alexscaves:forsaken")], icon="alexscaves:forsaken_idol", xp=100, s="Expert", **M, d=[
            "Forsaken je nejsilnější tvor dutin (250 bodů zdraví). Vznikne, když kultisté obětují netopýra Vespera.",
            "&cÚtočí zvukovými vlnami i na dálku. Když je slabý, zčerná a ve tmě se rychle léčí. Bojuj na světle!&r"]),
        Q("forlorn", "Čistá temnota", dep=["forsaken"], items=[("alexscaves:guanostone", 1), ("alexscaves:pure_darkness", 1)], xp=60, d=[
            "Čistá temnota (&ePure Darkness&r) padá jen z Forsakena.",
            "Z ní, temných cárů (&eDark Tatters&r) a můřího prachu vyrobíš stínové hedvábí (&eShadow Silk&r).",
            "Hedvábí je surovina na nejlepší výbavu dutin."]),
        Q("dreadbow", "Luk hrůzy", dep=["forlorn"], items=[("alexscaves:dreadbow", 1)], xp=60, d=[
            "Luk hrůzy (&eDreadbow&r) se nabíjí pomaleji, ale na cíl z výšky spadne celá sprška šípů.",
            "Vyrobíš ho z čisté temnoty, stínového hedvábí a křídel Vespera (&eVesper Wing&r)."]),
        Q("darkness_armor", "Plášť temnoty", dep=["forlorn", "occult_gem"], items=[("alexscaves:hood_of_darkness", 1), ("alexscaves:cloak_of_darkness", 1)], xp=60, d=[
            "Kápě (&eHood of Darkness&r) a plášť (&eCloak of Darkness&r) se vyrábějí ze stínového hedvábí a okultního drahokamu.",
            "Když nosíš obojí a stojíš ve tmě, plní se ti ukazatel temnoty.",
            "Plný ukazatel ti dovolí 10 sekund velmi rychle létat, ale jen ve tmě."]),

        # ---------- Cukrová dutina
        Q("candy_enter", "Cukrová dutina", dep=["map"], tasks=[biome("alexscaves:candy_cavity")], icon="alexscaves:candy_cane_block", xp=40, d=[
            "Cukrová dutina je jeskyně ze sladkostí: čokolády, dortu, zmrzliny a lízátek.",
            "Tečou tu řeky fialové limonády a světlo dávají gumová sluníčka (&eSundrop&r).",
            "&cNe všechno je přátelské. Sladcí tvorové a čarodějnice (Licowitch) tě napadnou.&r"]),
        Q("candy", "Sladkosti", dep=["candy_enter"], items=[("alexscaves:candy_cane", 1), ("alexscaves:block_of_chocolate", 1)], xp=40, d=[
            "Cukrová hůl (&eCandy Cane&r) je běžná surovina dutiny, padá z Caniaců. Blok čokolády (&eBlock of Chocolate&r) vytěžíš ze stěn a země dutiny.",
            "&aSladké jídlo ti občas dá efekt &eSugar Rush&a – na chvíli se pohybuješ a útočíš rychleji.&r"]),
        Q("candy_hook", "Hák z cukrové hole", dep=["candy"], items=[("alexscaves:candy_cane_hook", 1)], xp=40, d=[
            "Hák (&eCandy Cane Hook&r) vystřelíš a přitáhne tě k místu, kam se zasekne. Můžeš držet dva najednou.",
            "Vyrobíš ho z nabroušené cukrové hole (&eSharpened Candy Cane&r, padá z Caniaca), lékořicových šlahounů (&eLicoroot Vine&r) a tyče z cukrových holí (&eCandy Cane Pole&r)."]),
        Q("shot_gum", "Žvýkačková brokovnice", dep=["candy"], items=[("alexscaves:shot_gum", 1)], xp=40, d=[
            "Brokovnice (&eShot Gum&r) střílí dvě žvýkačky naráz. Odrážejí se od stěn.",
            "Střelivo jsou hromádky žvýkaček (&eGumball Pile&r) z Gumbeepera. Jedna hromádka = 5 výstřelů.",
            "Na výrobu potřebuješ i cukrové sklo (&eSugar Glass&r) z cukru a mátového prášku (&ePeppermint Powder&r)."]),
        Q("licowitch", "Zářivá esence", dep=["candy_enter"], items=[("alexscaves:radiant_essence", 1)], xp=50, d=[
            "Čarodějnice Licowitch žijí ve věžích na velkých lékořicových stromech. Hází lektvary a vyvolávají sladké tvory.",
            "Po zabití můžou upustit zářivou esenci (&eRadiant Essence&r). Najdeš ji i v truhlách jejich věží.",
            "&aZ esence, želatiny a karamelu jsou gumová sluníčka (&eSundrop&r) a z nich duhové boty (&eRainbounce Boots&r), které ruší pád.&r"]),
        Q("gum_worm", "Gumový červ", dep=["shot_gum", "candy_hook"], tasks=[kill("alexscaves:gum_worm")], icon="alexscaves:gobthumper", xp=100, s="Expert", **M, d=[
            "Gumový červ je obr dlouhý desítky bloků. Je neutrální, dokud ho nenaštveš.",
            "Přivoláš ho blokem &eGobthumper&r (želatina, hromádky žvýkaček a nabroušená cukrová hůl).",
            "&aDvěma háky se do něj můžeš zaseknout a jezdit na něm.&r",
            "Po smrti z něj může padnout sladký zub (&eSweet Tooth&r)."]),
        Q("sack_of_sating", "Vak sytosti", dep=["gum_worm"], items=[("alexscaves:sack_of_sating", 1)], xp=60, d=[
            "Vak sytosti (&eSack of Sating&r) sní jídlo, které na něj přetáhneš, a uloží si ho.",
            "Když máš hlad, sám tě nakrmí. Unese skoro nekonečně jídla.",
            "Vyrobíš ho ze sladkého zubu, želatiny a lékořicových šlahounů."]),
    ],
)

# ---------------------------------------------------------------- AD ASTRA
ADASTRA = dict(
    key="ad_astra", group="explore", title="Ad Astra",
    subtitle="Rakety a cesta na jiné planety", icon="ad_astra:tier_1_rocket",
    quests=[
        # ---------- Začátečník: příprava na Zemi
        Q("intro", "Ad Astra", tasks=[auto()], icon="ad_astra:tier_1_rocket", xp=10, s="Začátečník", **M, d=[
            "&bAd Astra&r tě vezme do vesmíru: na Měsíc, Mars, Venuši, Merkur a planetu Glacio v jiné sluneční soustavě.",
            "Cesta: energie → ocel → díly rakety → palivo a kyslík → start. Na každé planetě najdeš rudu na další, silnější raketu.",
            "&aPrůvodce Astrodux vyrobíš z knihy, 4 modrých barviv a 4 železných ingotů.&r"]),
        Q("coal_gen", "Uhelný generátor", dep=["intro"], items=[("ad_astra:coal_generator", 1)], xp=20, d=[
            "Všechny stroje Ad Astra potřebují energii. Uhelný generátor (&eCoal Generator&r) ji vyrábí z uhlí nebo dřeva.",
            "Stroj polož přímo vedle generátoru. Energie do něj poteče sama.",
            "&aNa delší vzdálenost později použiješ kabely (&eSteel Cable&r).&r"]),
        Q("furnace", "Etrionická pec", dep=["coal_gen"], items=[("ad_astra:etrionic_blast_furnace", 1)], xp=20, d=[
            "Etrionická vysoká pec (&eEtrionic Blast Furnace&r) má dva režimy: tavení (4 věci naráz) a slévání, ve kterém vyrábí ocel.",
            "Recept potřebuje železné pláty. Udělej si kompresor (&eCompressor&r) ze železa a pístů a vylisuj v něm pláty ze železných ingotů.",
            "Pláty se ve hře ukážou jako &eIron Sheet&r z Create. Je to totéž. &aVyrobí je i mechanický lis z Create.&r"]),
        Q("steel", "Ocel", dep=["furnace"], items=[("mekanism:ingot_steel", 8)], xp=20, d=[
            "Ocel (&eSteel Ingot&r) je hlavní materiál první rakety, skafandru i strojů.",
            "V etrionické peci přepni režim na slévání a vlož železný ingot a uhlí. Dostaneš 1 ocel.",
            "&aJiné cesty: míchačka z Create nad ohňohořákem (2 železa a uhlí dají 2 oceli) nebo metalurgický infuzér z Mekanismu.&r",
            "Všechna ocel v packu je stejný předmět, takže je jedno, kde ji vyrobíš."]),
        Q("compressor", "Ocelové pláty", dep=["steel"], items=[("ad_astra:compressor", 1), ("ad_astra:steel_plate", 8)], xp=25, d=[
            "Kompresor (&eCompressor&r) lisuje ingoty na pláty. Teď v něm z oceli vylisuj ocelové pláty (&eSteel Plate&r).",
            "Skoro všechno dál je z ocelových plátů. &aUmí je i mechanický lis z Create.&r"]),
        Q("parts", "Díly rakety", dep=["compressor"], items=[("ad_astra:rocket_nose_cone", 1), ("ad_astra:rocket_fin", 4), ("ad_astra:steel_tank", 2), ("ad_astra:steel_engine", 1)], xp=40, d=[
            "Raketa se skládá ze špice (&eRocket Nose Cone&r), 4 ploutví (&eRocket Fin&r), 2 nádrží (&eSteel Tank&r) a motoru (&eSteel Engine&r).",
            "Motor potřebuje rám (&eEngine Frame&r) a větrák (&eFan&r). Oba jsou z ocelových plátů a ocelových tyčí (&eSteel Rod&r).",
            "Nádrž potřebuje plynovou nádrž (&eGas Tank&r)."]),
        Q("workbench", "Pracovní stůl NASA", dep=["compressor"], items=[("ad_astra:nasa_workbench", 1)], xp=40, d=[
            "Rakety se skládají jen v pracovním stole NASA (&eNasa Workbench&r).",
            "Raketa 1. stupně potřebuje: špici, 6 bloků oceli, 4 ploutve, 2 ocelové nádrže a ocelový motor."]),
        Q("oil", "Ropa", dep=["intro"], tasks=[adv("ad_astra:ocean_cleanup")], icon="ad_astra:oil_bucket", xp=30, d=[
            "Ropa tryská z ropných pramenů nad hladinou oceánu. Naber ji kbelíkem (&eOil Bucket&r).",
            "&cRopa se neobnovuje. Nasbírej jí víc, na jeden let tam a zpět potřebuješ asi 6 kbelíků.&r",
            "&aDo rafinerie jde i ropa z modu Create Diesel Generators (&eCrude Oil Bucket&r).&r"]),
        Q("fuel", "Raketové palivo", dep=["compressor", "oil"], items=[("ad_astra:fuel_refinery", 1), ("ad_astra:fuel_bucket", 1)], xp=40, d=[
            "Rafinerie (&eFuel Refinery&r) mění ropu na raketové palivo (&eFuel Bucket&r). Potřebuje energii.",
            "Ropu dej do levého slotu. Palivo pak nabereš do kbelíku.",
            "Na start potřebuješ 3 kbelíky paliva. &aRaketa spálí i naftu a bionaftu z Create Diesel Generators (&eDiesel Bucket&r, &eBiodiesel Bucket&r).&r"]),
        Q("suit", "Skafandr", dep=["compressor"], items=[("ad_astra:space_helmet", 1), ("ad_astra:space_suit", 1), ("ad_astra:space_pants", 1), ("ad_astra:space_boots", 1)], xp=60, d=[
            "Ve vesmíru a na většině planet není vzduch. Skafandr (&eSpace Helmet&r, &eSpace Suit&r, &eSpace Pants&r, &eSpace Boots&r) drží kyslík, který dýcháš.",
            "Kyslík do něj nabereš v plniči kyslíku.",
            "&cNa Venuši a Merkuru obyčejný skafandr nestačí. Spálíš se.&r"]),
        Q("oxygen", "Plnič kyslíku", dep=["suit"], items=[("ad_astra:oxygen_loader", 1)], xp=30, d=[
            "Plnič kyslíku (&eOxygen Loader&r) mění vodu na kyslík. Potřebuje energii.",
            "Vodu dej do levé nádrže. Kyslík pak nabereš do skafandru, kbelíku nebo plynové nádrže (&eGas Tank&r).",
            "&aNáhradní plynovou nádrž s kyslíkem si vezmi s sebou. Když ji držíš a podržíš pravé tlačítko, doplní kyslík do skafandru.&r"]),
        Q("ti_69", "Kapesní měřák", dep=["compressor"], items=[("ad_astra:ti_69", 1)], xp=15, optional=True, d=[
            "&eTI-69&r ukáže kyslík, teplotu a gravitaci tam, kde stojíš.",
            "Hodí se, když nevíš, jestli je někde bezpečno."]),

        # ---------- Pokročilý: Měsíc a Mars
        Q("rocket1", "Raketa 1. stupně", dep=["workbench", "parts", "fuel"], items=[("ad_astra:tier_1_rocket", 1), ("ad_astra:launch_pad", 1)], xp=100, s="Pokročilý", **M, d=[
            "Doteď jsi stavěl na Zemi. Teď konečně poletíš! Raketa 1. stupně (&eTier 1 Rocket&r) doletí na Měsíc a na oběžnou dráhu Země.",
            "Postav odpalovací rampu (&eLaunch Pad&r) a raketu polož doprostřed.",
            "Shift + pravé tlačítko na raketu otevře její inventář. Nalij do ní 3 kbelíky paliva.",
            "Nastup (pravé tlačítko) a stiskni mezerník. Nahoře si vybereš, kam poletíš."]),
        Q("moon", "Měsíc", dep=["rocket1", "oxygen"], tasks=[dim("ad_astra:moon")], icon="ad_astra:moon_sand", xp=100, d=[
            "&cNež odletíš: do inventáře rakety dej odpalovací rampu a 3 kbelíky paliva na cestu zpět. Jinak na Měsíci uvízneš!&r",
            "Na Měsíci je −173 °C a není vzduch. Voda zamrzne a pochodně se rozbijí. Vezmi si náhradní kyslík, jídlo a jako světlo pochodně duší nebo světlit.",
            "Po přistání dej Shift + pravé tlačítko na přistávací modul (&eLander&r) a vezmi si z něj raketu, palivo a rampu. Modul pak rozbij.",
            "Na Měsíci najdeš rudu desh."]),
        Q("earth_orbit", "Oběžná dráha", dep=["rocket1", "oxygen"], tasks=[dim("ad_astra:earth_orbit")], icon="ad_astra:gas_tank", xp=40, d=[
            "Na obrazovce výběru cíle můžeš místo přistání zvolit oběžnou dráhu. Je tam nulová gravitace a vznášíš se.",
            "Na oběžné dráze si za suroviny postavíš vesmírnou stanici. U Země stojí 64 železných plátů, 32 ocelí, 32 deshových ingotů a 32 deshových plátů.",
            "&aSolární panely na oběžné dráze Země vyrábějí víc energie než na povrchu Země.&r"]),
        Q("desh", "Desh", dep=["moon"], items=[("ad_astra:desh_ingot", 8)], xp=40, d=[
            "Desh je ruda z Měsíce. Těž ji pod povrchem a přetav na ingoty (&eDesh Ingot&r).",
            "Z deshe jsou lepší stroje, rychlejší kabely a raketa 2. stupně."]),
        Q("cheese", "Měsíční sýr", dep=["moon"], items=[("ad_astra:cheese", 1)], xp=15, optional=True, d=[
            "Na Měsíci je i sýrová ruda (&eMoon Cheese Ore&r). Padá z ní sýr (&eCheese&r), který se dá jíst."]),
        Q("lunarians", "Lunariáni", dep=["moon"], tasks=[structure("ad_astra:lunarian_village")], icon="minecraft:emerald", xp=30, optional=True, d=[
            "Pod povrchem Měsíce jsou vesnice Lunariánů. Nepotřebují kyslík a obchodují s věcmi pro vesmír, třeba se skafandry.",
            "&aNa všech planetách chodí i potulný obchodník (&eLunarian Wandering Trader&r). Za smaragdy prodává palivo, kyslík, rampy i vodu.&r"]),
        Q("base", "Měsíční základna", dep=["desh"], items=[("ad_astra:oxygen_distributor", 1), ("ad_astra:solar_panel", 2)], xp=60, d=[
            "Rozdělovač kyslíku (&eOxygen Distributor&r) naplní uzavřenou místnost vzduchem, až 6 000 bloků. Potřebuje vodu a energii.",
            "V jeho okně je tlačítko, které ukáže, kam se kyslík šíří. Když je zvýrazněná celá místnost, je těsná a můžeš sundat helmu.",
            "&cKdyž do místnosti prorazíš díru, vzduch uteče a vysaje všechno ven!&r",
            "Solární panel (&eSolar Panel&r) vyrábí energii ze slunce. &aNekonečnou vodu dá vodní čerpadlo (&eWater Pump&r) postavené nad zdrojem vody.&r"]),
        Q("gravity", "Umělá gravitace", dep=["base"], items=[("ad_astra:gravity_normalizer", 1)], xp=40, optional=True, d=[
            "Gravitační normalizátor (&eGravity Normalizer&r) nastaví v uzavřené místnosti gravitaci od 0 do 2 G.",
            "Spotřebuje hodně energie. Stav ho jen tam, kde ho opravdu potřebuješ."]),
        Q("rover", "Vozítko", dep=["desh"], items=[("ad_astra:tier_1_rover", 1)], xp=60, d=[
            "Vozítko (&eTier 1 Rover&r) jezdí rychle po nerovném terénu. Má 2 sedadla, 16 slotů a rádio.",
            "Tankuje se palivem jako raketa: Shift + pravé tlačítko a palivo do levého slotu."]),
        Q("rocket2", "Raketa 2. stupně", dep=["desh"], items=[("ad_astra:tier_2_rocket", 1)], xp=100, d=[
            "Raketa 2. stupně (&eTier 2 Rocket&r) se staví stejně jako první, ale z deshe: 6 bloků deshe, deshové nádrže (&eDesh Tank&r) a deshový motor (&eDesh Engine&r).",
            "Doletí na Mars."]),
        Q("mars", "Mars", dep=["rocket2"], tasks=[dim("ad_astra:mars")], icon="ad_astra:mars_sand", xp=100, d=[
            "Mars je studený, nemá vzduch a gravitace je slabší než na Zemi. Skafandr nutný!",
            "Těž tu ostrum a ledové střepy (&eIce Shard&r)."]),
        Q("ostrum", "Ostrum", dep=["mars"], items=[("ad_astra:ostrum_ingot", 8)], xp=50, d=[
            "Ostrum je ruda z Marsu. Přetav ji na ingoty (&eOstrum Ingot&r).",
            "Z ostra je netheritový skafandr, kryomrazák, energizér a raketa 3. stupně."]),
        Q("cryo", "Kryopalivo", dep=["ostrum"], items=[("ad_astra:cryo_freezer", 1), ("ad_astra:ice_shard", 4)], xp=50, d=[
            "Kryopalivo je mnohem lepší palivo: na start stačí 1 kbelík místo 3.",
            "Vyrábí ho kryomrazák (&eCryo Freezer&r) z ledu. Nejvíc ho dá ledový střep (&eIce Shard&r). Jeho ruda je na Měsíci, Marsu a Glaciu.",
            "Jde i obyčejný, zhutněný a modrý led, ale dají méně."]),
        Q("energizer", "Energizér", dep=["ostrum"], items=[("ad_astra:energizer", 1)], xp=40, d=[
            "Energizér (&eEnergizer&r) uloží 2 miliony energie a při rozbití si ji nechá.",
            "Předmět nabiješ tak, že s ním klikneš na nabitý energizér. Tak nabiješ i jet suit."]),

        # ---------- Expert: horké planety a jiná soustava
        Q("netherite_suit", "Netheritový skafandr", dep=["ostrum", "nether_end:netherite"], items=[("ad_astra:netherite_space_helmet", 1), ("ad_astra:netherite_space_suit", 1), ("ad_astra:netherite_space_pants", 1), ("ad_astra:netherite_space_boots", 1)], xp=80, d=[
            "Na Venuši je 464 °C a na Merkuru 167 °C. Obyčejný skafandr tě neochrání.",
            "Netheritový skafandr má trvalou odolnost proti ohni a lepší ochranu.",
            "Vyrobíš ho z netheritové zbroje, ostrových a deshových plátů."]),
        Q("rocket3", "Raketa 3. stupně", dep=["ostrum"], items=[("ad_astra:tier_3_rocket", 1)], xp=100, s="Expert", **M, d=[
            "Dosud jsi létal na studené planety. Teď míříš do žáru a pak až do jiné sluneční soustavy.",
            "Raketa 3. stupně (&eTier 3 Rocket&r) je z ostra: 6 bloků ostra, ostrové nádrže a ostrový motor.",
            "Doletí na Venuši a Merkur."]),
        Q("venus", "Venuše", dep=["rocket3", "netherite_suit"], tasks=[dim("ad_astra:venus")], icon="ad_astra:venus_sand", xp=100, d=[
            "&cBez netheritového skafandru na Venuši rychle uhoříš!&r",
            "Venuše je rozpálená a nemá vzduch. Těž tu kalorit."]),
        Q("mercury", "Merkur", dep=["rocket3", "netherite_suit"], tasks=[dim("ad_astra:mercury")], icon="ad_astra:mercury_stone", xp=60, d=[
            "Merkur je planeta nejblíž Slunci. &cBez netheritového skafandru uhoříš.&r",
            "&aSolární panely tu vyrábějí nejvíc energie ze všech planet.&r"]),
        Q("calorite", "Kalorit", dep=["venus"], items=[("ad_astra:calorite_ingot", 8)], xp=60, d=[
            "Kalorit je ruda z Venuše. Přetav ji na ingoty (&eCalorite Ingot&r).",
            "Z kaloritu je raketa 4. stupně a jet suit."]),
        Q("rocket4", "Raketa 4. stupně", dep=["calorite"], items=[("ad_astra:tier_4_rocket", 1)], xp=100, d=[
            "Raketa 4. stupně (&eTier 4 Rocket&r) je z kaloritu a doletí do jiné sluneční soustavy, k hvězdě Proxima Centauri."]),
        Q("glacio", "Glacio", dep=["rocket4"], tasks=[dim("ad_astra:glacio")], icon="ad_astra:jet_suit", xp=100, d=[
            "Glacio je zamrzlá planeta u Proximy Centauri. Má dýchatelný vzduch, takže tu přežiješ i bez skafandru.",
            "&cJe tu ale velká zima.&r Najdeš tu i ledové střepy pro kryopalivo."]),
        Q("jet_suit", "Jet suit", dep=["calorite", "energizer", "netherite_suit"], items=[("ad_astra:jet_suit_helmet", 1), ("ad_astra:jet_suit", 1), ("ad_astra:jet_suit_pants", 1), ("ad_astra:jet_suit_boots", 1)], xp=100, d=[
            "Jet suit je nejlepší skafandr: víc ochrany, víc kyslíku a umí létat.",
            "Mezerník = stoupání, mezerník + sprint = rychlý let. Let funguje na energii, nabij ho v energizéru.",
            "Vyrobíš ho z netheritového skafandru, kaloritu, kaloritových nádrží a motoru."]),
        Q("zip_gun", "Tryskací pistole", dep=["earth_orbit"], items=[("ad_astra:zip_gun", 1)], xp=30, optional=True, d=[
            "Tryskací pistole (&eZip Gun&r) spaluje kyslík a tlačí tě dopředu. V nulové gravitaci je to nejlepší způsob pohybu.",
            "&cVe vesmíru tě nic nezastaví. Neleť moc rychle, nebo se ztratíš.&r"]),
    ],
)

# ---------------------------------------------------------------- FOSSILS & ARCHEOLOGY
FOSSILS = dict(
    key="fossils", group="explore", title="Fossils & Archeology",
    subtitle="Oživ dinosaury z fosilií", icon="fossil:analyzer",
    quests=[
        # ---------- Začátečník: fosilie a analýza
        Q("intro", "Fossils & Archeology", tasks=[auto()], icon="fossil:dinopedia", xp=10, s="Začátečník", **M, d=[
            "&bFossils and Archeology Revival&r ti dovolí oživit dinosaury a pravěká zvířata. Na verzi 1.21.1 jsme ho převedli jen pro tento pack.",
            "Cesta: fosilie → analyzátor → DNA → kultivátor → vejce → dinosaurus.",
            "K tomu archeologie: relikvie, starodávné zbraně, Nether a boss Anu."]),
        Q("fossil", "Vykopej fosilii", dep=["intro"], items=[("fossil:fossil_bio", 1)], xp=20, d=[
            "Bloky fosilií (&eStone Fossil Block&r, &eDeepslate Fossil Block&r a další) jsou pod zemí. Vypadají jako kámen s otiskem kostí.",
            "Z kamenných bloků padá biofosilie (&eBio Fossil&r), střepy relikvie, rostlinná fosilie, kosti a vzácně i něco cenného. Z bloků v hlubinné břidlici padá místo biofosilie břidlicová fosilie.",
            "&aBlok fosilie vytěžený s Hedvábným dotekem rozdrtí i drtící kola z Create.&r"]),
        Q("relic", "Střepy relikvie", dep=["fossil"], items=[("fossil:relic_scrap", 1)], xp=15, d=[
            "Střepy relikvie (&eRelic Scrap&r) padají z bloků fosilií.",
            "V analyzátoru z nich dostaneš kamennou desku, figurky, rozbité zbraně nebo úlomky keramiky.",
            "Slouží i jako palivo do archeologova stolu."]),
        Q("dinopedia", "Dinopedie", dep=["fossil"], items=[("fossil:dinopedia", 1)], xp=15, d=[
            "Dinopedii (&eDinopedia&r) vyrobíš z knihy a libovolné fosilie.",
            "Klikni s ní pravým tlačítkem na tvora. Uvidíš jeho věk, hlad, náladu a co jí.",
            "&aNa vejci ukáže, jestli je mu teplo, nebo zima.&r"]),
        Q("sifter", "Síto", dep=["fossil"], items=[("fossil:sifter", 1)], xp=25, d=[
            "Do síta (&eSifter&r) vlož písek, hlínu nebo štěrk.",
            "Většinou z nich vypadnou obyčejné věci, ale občas i fosilie, úlomek keramiky (&ePottery Shard&r) nebo vzácně jantar.",
            "&aJe to pomalejší, ale bezpečná cesta k fosiliím bez kopání.&r"]),
        Q("analyzer", "Analyzátor", dep=["fossil", "relic"], items=[("fossil:analyzer", 1)], xp=40, d=[
            "Analyzátor (&eAnalyzer&r) rozebere fosilie, relikvie, zmrzlé maso a další věci.",
            "Vyrobíš ho ze železných ingotů, střepů relikvie a fosilie.",
            "&aNepotřebuje palivo ani energii. Stačí vložit věci a počkat.&r"]),
        Q("dna", "DNA", dep=["analyzer"], tasks=[adv("fossil:fossil/dna")], icon="fossil:tyrannosaurus_dna", xp=30, d=[
            "Z biofosilie dostaneš většinou kostní moučku nebo písek. DNA jen asi jednou ze sedmi pokusů.",
            "Druh je náhodný. Z biofosilií jsou hlavně dinosauři, z břidlicových fosilií prvohorní tvorové, ze zmrzlého masa hlavně savci a ptáci doby ledové.",
            "&aAnalyzuj hodně fosilií, ať máš z čeho vybírat.&r"]),
        Q("goo", "Biohmota", dep=["analyzer"], items=[("fossil:bio_goo", 2)], xp=20, d=[
            "Biohmota (&eBio Goo&r) je palivo kultivátoru.",
            "Vyrobíš ji z vejce, pšenice, shnilého masa a kbelíku mléka."]),

        # ---------- Pokročilý: oživení a chov
        Q("vat", "Kultivátor", dep=["goo", "dna"], items=[("fossil:culture_vat", 1)], xp=40, s="Pokročilý", **M, d=[
            "Zatím jsi jen sbíral a analyzoval. Teď z DNA poprvé vytvoříš život!",
            "Kultivátor (&eCulture Vat&r) vypěstuje vejce, injekci s embryem savce nebo živé semínko.",
            "Vlož DNA a jako palivo biohmotu. Vyrobíš ho ze skla, slizu, kbelíku vody a železa.",
            "&cNěkdy se pokus nepovede: kultivátor se rozbije a vyleze z něj zmetek Failuresaurus. Neměj ho v domě.&r"]),
        Q("eggs", "První vejce", dep=["vat"], tasks=[adv("fossil:fossil/dino_eggs")], icon="fossil:egg_item_triceratops", xp=40, d=[
            "Vejce polož na zem pravým tlačítkem.",
            "Vejce potřebuje teplo, a to znamená světlo. V teplém biomu stačí méně světla, ve studeném víc. &cVe tmě nebo ve vodě se líhnutí vrací zpět.&r",
            "Za pár minut se vylíhne mládě. Když jsi do 16 bloků, mnoho druhů tě rovnou přijme za pána."]),
        Q("feeder", "Krmítko", dep=["eggs"], items=[("fossil:feeder", 1)], xp=30, d=[
            "Do krmítka (&eFeeder&r) dej maso i rostliny. Dinosauři si z něj sami berou to, co jedí.",
            "&cHladový dravec může zaútočit i na tebe.&r Dinopedie ti ukáže, jak má tvor hlad."]),
        Q("whip", "Bič", dep=["eggs"], items=[("fossil:whip", 1)], xp=30, d=[
            "S bičem (&eWhip&r) v ruce klikni na svého dospělého dinosaura a nasedneš na něj. Jde to jen u druhů, na kterých se dá jezdit.",
            "&aNěkteré neochočené druhy jde bičem i ochočit.&r"]),
        Q("embryos", "Pravěcí savci", dep=["vat"], tasks=[adv("fossil:fossil/embryos")], icon="minecraft:wheat", xp=40, d=[
            "Z DNA savců (třeba mamuta) kultivátor vyrobí injekci s embryem.",
            "Injekcí klikni na dospělého savce: krávu, prase, ovci, koně a další. Zvíře za čas porodí pravěké mládě."]),
        Q("frozen_meat", "Zmrzlé maso", dep=["fossil"], items=[("fossil:frozen_meat", 1)], xp=25, d=[
            "Zmrzlé maso (&eFrozen Meat&r) padá z permafrostu (&ePermafrost Block&r). Ten je v hlíně studených biomů.",
            "V analyzátoru z něj získáš DNA mamuta, šavlozubého tygra, dronte a dalších zvířat doby ledové."]),
        Q("shale", "Břidlicová fosilie", dep=["fossil"], items=[("fossil:fossil_shale", 1)], xp=25, d=[
            "Břidlicová fosilie (&eShale Fossil&r) padá z bloků fosilií hluboko v hlubinné břidlici.",
            "Má v sobě DNA nejstarších tvorů, třeba dimetrodona nebo obří vážky."]),
        Q("tar", "Asfaltová jezírka", dep=["analyzer"], tasks=[adv("fossil:fossil/fossil_tar")], icon="fossil:tar_drop", xp=30, d=[
            "Asfaltová jezírka najdeš na pláních a v savanách, některá i v zasněžené krajině.",
            "Kbelíkem naber asfalt. V pracovním stole z kbelíku asfaltu vzniknou 4 kapky (&eTar Drop&r).",
            "Kapky analyzuj. Dostaneš asfaltovou fosilii (&eTar Fossil&r) s DNA zvířat doby ledové."]),
        Q("plant_fossil", "Rostlinná fosilie", dep=["analyzer"], items=[("fossil:fossil_plant", 1)], xp=20, d=[
            "Rostlinná fosilie (&ePlant Fossil&r) padá z bloků fosilií a ze síta.",
            "V analyzátoru z ní dostaneš zkamenělá semínka a pravěké sazenice."]),
        Q("seeds", "Pravěké rostliny", dep=["plant_fossil", "vat"], tasks=[adv("fossil:fossil/restored_seeds")], icon="fossil:fern_seed", xp=30, d=[
            "Zkamenělé semínko (třeba &eFossilized Fern Spores&r) dej do kultivátoru. Vznikne živé semínko.",
            "Zasaď ho a vyroste pravěká rostlina. &aBýložraví dinosauři je rádi jedí.&r"]),
        Q("amber", "Komár v jantaru", dep=["fossil"], items=[("fossil:amber_chunk_mosquito", 1)], xp=40, d=[
            "Jantarová ruda (&eAmber Ore&r) je pod zemí. Padá z ní kousek jantaru.",
            "Kousek s komárem (&eMosquito Amber Chunk&r) padne jen asi v 1 z 20 případů. Je to vzácná sběratelská ozdoba."]),
        Q("scarab_gem", "Skarabeový drahokam", dep=["fossil"], items=[("fossil:scarab_gem", 1)], xp=50, d=[
            "Skarabeový drahokam (&eScarab Gem&r) je velmi vzácný drop z bloků fosilií.",
            "Otevře sarkofág boha Anu a ochočí velké dravce.",
            "&aNa kovářském stole z diamantového nástroje, drahokamu a šablony netheritového vylepšení vznikne skarabeový nástroj.&r"]),
        Q("scarab_tame", "Král zvířat", dep=["scarab_gem", "eggs"], tasks=[adv("fossil:fossil/scarab_tame")], icon="fossil:scarab_sword", xp=60, optional=True, d=[
            "Velkého dravce (třeba tyranosaura) ochočíš skarabeovým drahokamem.",
            "Vodní dravce ochočíš vodním drahokamem (&eAquatic Scarab Gem&r) ze skarabeového drahokamu a dominikánského jantaru."]),

        # ---------- Archeologie
        Q("worktable", "Archeologův stůl", dep=["relic"], items=[("fossil:worktable", 1)], xp=25, d=[
            "Archeologův stůl (&eArcheology Workbench&r) vyrobíš z kůže a pracovního stolu.",
            "Opravuje starodávné zbraně, figurky a vázy. Palivem jsou střepy relikvie, u keramiky úlomky keramiky."]),
        Q("sword", "Starodávný meč", dep=["worktable"], items=[("fossil:ancient_sword", 1)], xp=60, d=[
            "Rozbitý starodávný meč (&eBroken Ancient Sword&r) vzácně padá z bloků fosilií a z analýzy relikvií.",
            "Na archeologově stole ho oprav na starodávný meč (&eAncient Sword&r).",
            "&aStejně opravíš i rozbitou starodávnou helmu.&r"]),
        Q("figurines", "Figurky", dep=["analyzer", "worktable"], tasks=[adv("fossil:fossil/figurines")], icon="fossil:figurine_anu_restored", xp=40, d=[
            "Zničené figurky dostaneš z analýzy střepů relikvie. Na archeologově stole je s úlomkem keramiky opravíš.",
            "Na otevření portálu k Anu budeš potřebovat 4 figurky (jakékoli)."]),

        # ---------- Expert: Anu
        Q("hell_boat", "Pekelná loď", dep=["figurines"], tasks=[structure("fossil:hell_boat")], icon="fossil:figurine_anu_pristine", xp=60, s="Expert", **M, d=[
            "Dosud jsi kopal a pěstoval. Teď tě čeká boj s bohem Anu.",
            "Začíná to v Netheru: na lávovém moři pluje pekelná loď se sochou Anu (&eAnu Statue&r).",
            "&cKdyž sochu rozbiješ, nic z ní nepadne. Rituál proto udělej přímo na lodi.&r",
            "Do 4 rohů kolem sochy (šikmo) dej figurky. Na 4 strany (rovně vedle sochy) dej redstonový prach.",
            "Socha vybuchne a objeví se totem, který otevře portál."]),
        Q("anu_lair", "Doupě Anu", dep=["hell_boat"], tasks=[dim("fossil:anu_lair")], icon="fossil:ancient_stone_bricks", xp=60, d=[
            "Projdi portálem do doupěte Anu. Stojí v něm Anuův hrad.",
            "&cHrad hlídají anubité (Anubite). Vezmi si dobrou zbroj a jídlo.&r"]),
        Q("sarcophagus", "Sarkofág", dep=["anu_lair", "scarab_gem"], tasks=[adv("fossil:fossil/sarcophagus")], icon="fossil:scarab_gem", xp=40, d=[
            "Uvnitř hradu je sarkofág. Klikni na něj skarabeovým drahokamem.",
            "&cTím probudíš Anu! Měj plné zdraví a dobrou výbavu.&r"]),
        Q("kill_anu", "Porazit Anu", dep=["sarcophagus"], tasks=[kill("fossil:anu_boss")], icon="fossil:figurine_anu_pristine", xp=100, s="Expert", **M, d=[
            "Anu je hlavní boss modu. Bojuje starodávným mečem a na dálku střílí ohnivé koule.",
            "Po smrti upustí starodávný klíč (&eAncient Key&r) a zůstane po něm mrtvé tělo."]),
        Q("key", "Starodávný klíč", dep=["kill_anu"], items=[("fossil:ancient_key", 1)], xp=60, d=[
            "Starodávný klíč (&eAncient Key&r) padá jen z poraženého Anu.",
            "Otevře starodávnou truhlu (&eAncient Chest&r) v klenotnici."]),
        Q("treasure_room", "Klenotnice", dep=["kill_anu"], tasks=[dim("fossil:treasure_room")], icon="fossil:ancient_chest", xp=60, d=[
            "Klikni na mrtvé tělo Anu. Přeneseš se do klenotnice.",
            "V klenotnici je i portál, kterým se vrátíš domů."]),
        Q("ancient_clock", "Starodávné hodiny", dep=["key", "treasure_room"], tasks=[adv("fossil:fossil/ancient_clock")], icon="fossil:ancient_clock", xp=100, d=[
            "V klenotnici otevři starodávnou truhlu klíčem.",
            "Uvnitř jsou starodávné hodiny (&eAncient Clock&r), poslední poklad modu. Gratulujeme!"]),
    ],
)

# Pořadí kapitol této oblasti v knize questů
CHAPTERS = [ALEXSCAVES, ADASTRA, FOSSILS]

# Předměty bez receptu/loot table, ověřené v kódu modu
NO_RECIPE = {
    "fossil:ancient_key": "drop z bosse Anu (AnuBoss.dropCustomDeathLoot -> ModItems.ANCIENT_KEY)",
}
