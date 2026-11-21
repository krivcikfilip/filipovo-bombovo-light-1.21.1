from engine import *

# Oblast j_explore: průzkum overworldu (biomy, struktury, Lootr), tvorové, mazlíčci, oceán, Luminous.
# Úrovně: milník (hexagon) s podnázvem Začátečník / Pokročilý / Expert označuje přechod mezi úrovněmi.

B = "Začátečník"
A = "Pokročilý"
X = "Expert"

# =====================================================================
# PRŮZKUM SVĚTA – dungeony, chrámy, Lootr, líhně (původní kapitola)
# =====================================================================
EXPLORE = dict(
    key="exploration", group="explore", title="Průzkum světa",
    subtitle="Dungeony, chrámy a poklady", icon="minecraft:compass",
    quests=[
        Q("start", "Velký svět", icon="minecraft:filled_map", tasks=[auto()], xp=10, shape="hexagon", size=1.5, s=B, d=[
            "Svět v tomto packu je větší a divočejší než obyčejný Minecraft.",
            "&bTectonic&r dělá vysoké hory a hluboké oceány. &bTerralith&r přidává spoustu nových biomů. Mody &bYUNG's&r vylepšují dungeony, doly a chrámy.",
            "",
            "&aTip:&r Na výpravu si vezmi jídlo, pochodně, postel a náhradní nástroje. Biom, ve kterém stojíš, uvidíš po stisku F3.",
            "Pokračuj kapitolami &eBiomy a krajina&r a &eStavby a města&r."]),
        Q("lootr_cart", "Vozík s pokladem", dep=["mineshaft"], tasks=[adv("lootr:1cart")], icon="minecraft:chest_minecart", xp=20, d=[
            "Truhly ve stavbách jsou z modu &bLootr&r. Každý hráč v nich najde svůj vlastní poklad.",
            "Otevři vozík s truhlou (nákladní vozík) v dole &eMineshaft&r.",
            "",
            "&cTruhly z Lootru nerozbíjej!&r Jdou rozbít jen se Shiftem a ostatní hráči by pak o svůj poklad přišli."]),
        Q("small_dungeon", "Monster Room", dep=["start"], tasks=[structure("betterdungeons:small_dungeon")], icon="minecraft:mossy_cobblestone", xp=20, d=[
            "Malý podzemní dungeon &eMonster Room&r. &bYUNG's Better Dungeons&r ho přestavěl, takže vypadá líp než v obyčejném Minecraftu.",
            "Uprostřed je líheň, která pořád vyrábí příšery. Kolem jsou truhly.",
            "",
            "&aTip:&r Hledej v jeskyních. Takové dungeony jsou pod zemí skoro všude."]),
        Q("mineshaft", "Mineshaft", dep=["start"], tasks=[structure("#minecraft:mineshaft")], icon="minecraft:rail", xp=20, d=[
            "&eMineshaft&r je starý důl s kolejemi a dřevěnými trámy. Najdeš ho pod zemí.",
            "&bYUNG's Better Mineshafts&r mění jeho vzhled podle biomu – v poušti, v džungli, v ledu nebo v houbách vypadá pokaždé jinak.",
            "",
            "&aTip:&r Na kolejích stojí vozíky s truhlami. Kolejnice si můžeš sebrat."]),
        Q("dungeon", "Fortress of the Undead", dep=["small_dungeon"], tasks=[structure("betterdungeons:skeleton_dungeon")], icon="minecraft:bone", xp=50, shape="hexagon", size=1.5, s=A, d=[
            "&eFortress of the Undead&r je velký podzemní dungeon plný kostlivců a líhní. Je tmavý a má hodně chodeb.",
            "Teď už nestačí jen proběhnout – potřebuješ železnou zbroj, štít a hodně pochodní.",
            "",
            "&aTip:&r Každou líheň hned zakryj pochodněmi nebo ji vykopej. Pak se vrať pro truhly."]),
        Q("zombie_dungeon", "Catacomb", dep=["small_dungeon"], tasks=[structure("betterdungeons:zombie_dungeon")], icon="minecraft:rotten_flesh", xp=40, d=[
            "&eCatacomb&r je podzemní hřbitov s hroby a zombie. Uvnitř je několik truhel, některé u náhrobků.",
            "Jsou tu líhně zombie. Nejdřív je zakryj pochodněmi nebo vykopej, pak prohledej hroby."]),
        Q("spider_dungeon", "Spider Cave", dep=["small_dungeon"], tasks=[structure("betterdungeons:spider_dungeon")], icon="minecraft:cobweb", xp=40, d=[
            "&eSpider Cave&r je jeskyně plná pavučin a pavouků.",
            "&aTip:&r Pavučiny rychle přeseká meč nebo nůžky. Bez nich v pavučině uvízneš."]),
        Q("spawner", "Líheň domů", dep=["dungeon"], items=[("minecraft:spawner", 1)], xp=60, d=[
            "Díky modu &bApothic Spawners&r můžeš líheň vykopat a odnést domů.",
            "Potřebuješ krumpáč s očarováním &eSilk Touch&r. Líheň pak polož, kam chceš – třeba nad farmu na příšery.",
            "&cKrumpáč přitom ztratí 100 bodů výdrže.&r",
            "",
            "&aTip:&r Líheň můžeš vylepšit různými předměty (další quest). Co který předmět dělá, ukáže JEI."]),
        Q("spawner_light", "Líheň za světla", dep=["spawner"], tasks=[adv("apothic_spawners:light")], icon="minecraft:soul_lantern", xp=40, d=[
            "Líheň vylepšíš tak, že na ni klikneš pravým tlačítkem s předmětem v ruce.",
            "&eLucerna duší&r zařídí, že líheň funguje i za světla. Kolem farmy si tak můžeš svítit.",
            "",
            "Další vylepšení: &ecukr&r zkrátí čekání, &ezkvašené pavoučí oko&r přidá víc příšer naráz."]),
        Q("spawner_players", "Líheň bez hráče", dep=["spawner_light"], tasks=[adv("apothic_spawners:players")], icon="minecraft:nether_star", xp=100, optional=True, d=[
            "Normálně líheň pracuje jen tehdy, když je hráč blízko.",
            "&eNetherová hvězda&r (z Withera) to změní. Líheň pak běží, i když jsi daleko – třeba pro automatickou farmu."]),
        Q("lootr_25", "Lovec pokladů", dep=["lootr_cart", "dungeon"], tasks=[adv("lootr:25loot")], icon="minecraft:chest", xp=40, d=[
            "Otevři 25 truhel, sudů nebo vozíků z &bLootru&r.",
            "Truhly ve stavbách se nevyplatí přeskakovat. Můžou v nich být očarované knihy, diamanty i vzácné kovářské šablony."]),
        Q("lootr_100", "Sto pokladů", dep=["lootr_25"], tasks=[adv("lootr:100loot")], icon="minecraft:gold_block", xp=100, optional=True, d=[
            "Otevři 100 truhel z Lootru. To se povede jen opravdovému průzkumníkovi.",
            "&aTip:&r Nejvíc truhel mají velké stavby: hrady, pevnosti a chrámy."]),
        Q("desert", "Desert Temple", dep=["dungeon"], tasks=[structure("betterdeserttemples:desert_temple")], icon="minecraft:sand", xp=30, d=[
            "&bYUNG's Better Desert Temples&r udělal z pyramidy v poušti velký chrám &eDesert Temple&r s chodbami, pastmi a hrobkami.",
            "Hledej ho v poušti. Uvnitř máš &eÚnavu z těžby&r – nejde tedy prostě prokopat zdi.",
            "",
            "&cPozor na pasti a na truhly s nástrahou.&r"]),
        Q("pharaoh", "Kletba faraona", dep=["desert"], tasks=[adv("betterdeserttemples:temple_clear")], icon="minecraft:golden_sword", xp=80, d=[
            "Hluboko v chrámu odpočívá faraon (&ePharaoh&r). Je to pouštní zombie se zvláštní hlavou.",
            "Když ho porazíš, kletba zmizí a &eÚnava z těžby&r v chrámu přestane."]),
        Q("jungle", "Jungle Temple", dep=["dungeon"], tasks=[structure("betterjungletemples:jungle_temple")], icon="minecraft:mossy_cobblestone", xp=30, d=[
            "&eJungle Temple&r je velký kamenný chrám zarostlý džunglí od &bYUNG's Better Jungle Temples&r.",
            "Uvnitř jsou pasti a truhly. V &ezvláštním štěrku&r najdeš &eštětečkem&r smaragdy.",
            "",
            "&cPozor:&r některé truhly jsou s nástrahou."]),
        Q("trial", "Trial Chambers", dep=["dungeon"], tasks=[structure("minecraft:trial_chambers")], icon="minecraft:trial_key", xp=50, d=[
            "&eTrial Chambers&r je podzemní komplex z mědi a tufu. Najdeš ho hluboko pod zemí.",
            "&aKde hledat:&r nejbližší je kolem X 240, Z -2690. V nejstarší části světa kolem vašich základen (asi do 1 500 bloků od spawnu) nejsou.",
            "Líheň klání (&eTrial Spawner&r) posílá vlny příšer. Když je porazíš, dostaneš klíč klání (&eTrial Key&r). Tím odemkneš trezor (&eVault&r) s odměnou.",
            "",
            "&cPozor na fičáky (&eBreeze&c) – střílí větrné náboje, které tě odhodí.&r"]),
        Q("vault", "Pokladnice", dep=["trial"], tasks=[adv("minecraft:adventure/under_lock_and_key")], icon="minecraft:vault", xp=40, d=[
            "Odemkni &ePokladnici&r ve stavbě &eTrial Chambers&r &eKlíčem klání&r.",
            "Každý hráč může každou pokladnici otevřít jen jednou."]),
        Q("breeze", "Fičákova hůl", dep=["trial"], items=[("minecraft:breeze_rod", 1)], xp=40, d=[
            "Padá z fičáka, větrné příšery ze stavby &eTrial Chambers&r.",
            "Vyrobíš z ní &eVětrné náboje&r. Hodíš je pod sebe a vyskočíš vysoko. Hůl je také potřeba na &ePalcát&r."]),
        Q("ominous", "Zlověstná pokladnice", dep=["vault", "breeze"], tasks=[adv("minecraft:adventure/revaulting")], icon="minecraft:ominous_trial_key", xp=120, shape="hexagon", size=1.5, s=X, d=[
            "Teď přichází nejtěžší výzva &eTrial Chambers&r. Když vstoupíš se &eZlověstným znamením&r, líhně klání zesílí.",
            "&eZlověstné znamení&r dostaneš vypitím &eZlověstné lahvičky&r. Ta padá z kapitána nájezdníků (nese prapor).",
            "Silné líhně dávají &eZlověstný klíč klání&r. Ten otevře zlověstnou pokladnici – jen v ní je &eTěžké jádro&r na Palcát."]),
        Q("monument", "Ocean Monument", dep=["dungeon"], tasks=[structure("betteroceanmonuments:ocean_monument")], icon="minecraft:prismarine", xp=60, d=[
            "&eOcean Monument&r je obrovský chrám na dně hlubokého oceánu. &bYUNG's Better Ocean Monuments&r ho přestavěl.",
            "Hlídají ho strážci, kteří střílí laserem.",
            "",
            "&aTip:&r Vezmi si lektvary dýchání pod vodou a vidění ve tmě."]),
        Q("elder", "Elder Guardian", dep=["monument"], tasks=[kill("minecraft:elder_guardian")], icon="minecraft:wet_sponge", xp=120, d=[
            "V monumentu žijí bossové &eElder Guardian&r (velcí strážci). Dávají ti &eÚnavu z těžby&r, takže zdi neprokopeš.",
            "Poraz je. Únava pak zmizí a můžeš v klidu kopat a hledat poklady.",
            "",
            "&aTip:&r Mléko únavu na chvíli smaže."]),
        Q("stronghold", "Stronghold", dep=["dungeon"], tasks=[structure("betterstrongholds:stronghold")], icon="minecraft:ender_eye", xp=60, shape="hexagon", size=1.5, s=X, d=[
            "&eStronghold&r je pevnost hluboko pod zemí. Je v ní portál do Endu.",
            "Najdeš ji pomocí &eEndových očí&r: hoď oko do vzduchu a jdi směrem, kam letí.",
            "",
            "&bYUNG's Better Strongholds&r z ní udělal velké bludiště. Značkuj si cestu pochodněmi."]),
        Q("ancient", "Ancient City", dep=["stronghold"], tasks=[structure("minecraft:ancient_city")], icon="minecraft:sculk_catalyst", xp=100, d=[
            "&eAncient City&r je obrovské město hluboko dole v biomu &eDeep Dark&r.",
            "&cBuď potichu.&r Sculková čidla slyší tvoje kroky. Sculkový kvílák pak přivolá &eWardena&r. Choď se Shiftem.",
            "",
            "&aTip:&r Vlna na podlaze tlumí zvuk tvých kroků."]),
        Q("warden", "Warden", dep=["ancient"], tasks=[kill("minecraft:warden")], icon="minecraft:sculk_shrieker", xp=250, d=[
            "&eWarden&r je nejsilnější příšera v Overworldu. Je slepý, ale slyší každý krok a cítí tě nablízku.",
            "Většina hráčů se mu radši vyhne. Porazit ho je opravdový úspěch – vezmi si tu nejlepší výbavu."]),
        Q("all_dungeons", "Mistr dungeonů", dep=["dungeon", "zombie_dungeon", "spider_dungeon"], tasks=[adv("betterdungeons:all_dungeons")], icon="minecraft:skeleton_skull", xp=100, optional=True, d=[
            "Navštiv všechny čtyři dungeony z &bYUNG's Better Dungeons&r: &eMonster Room&r, &eFortress of the Undead&r, &eCatacomb&r a &eSpider Cave&r.",
            "Quest se splní sám, až vstoupíš do posledního z nich."]),
    ],
)

# =====================================================================
# BIOMY A KRAJINA – Terralith a Tectonic (nová kapitola)
# =====================================================================
BIOMES = dict(
    key="biomes", group="explore", title="Biomy a krajina",
    subtitle="Zajímavá místa z Terralithu a Tectonicu", icon="minecraft:grass_block",
    quests=[
        Q("b_intro", "Nové biomy", icon="minecraft:grass_block", tasks=[auto()], xp=10, shape="hexagon", size=1.5, s=B, d=[
            "Biom je druh krajiny: les, poušť, hory, oceán… Každý biom má jiné stromy, zvířata a stavby.",
            "&bTerralith&r přidává přes 90 nových biomů, i podzemních. &bTectonic&r dělá krajinu vyšší a dramatičtější.",
            "",
            "Název biomu uvidíš po stisku F3 (vlevo, řádek &eBiome&r). Biomy z Terralithu mají jméno jako &eterralith:yellowstone&r.",
            "V questech píšeme anglické názvy biomů, stejně jako je uvidíš ve hře."]),
        Q("sakura", "Sakura Grove", dep=["b_intro"], tasks=[biome("terralith:sakura_grove")], icon="minecraft:cherry_sapling", xp=15, d=[
            "&eSakura Grove&r je háj plný sakur (třešní) s růžovým listím. Roste tu i bambus, břízy a cukrová třtina.",
            "&aTip:&r Třešňové dřevo má krásnou růžovou barvu. Hodí se na stavby."]),
        Q("moonlight", "Moonlight Grove", dep=["b_intro"], tasks=[biome("terralith:moonlight_grove")], icon="minecraft:amethyst_shard", xp=15, d=[
            "&eMoonlight Grove&r je kouzelný les. Na zemi tu rostou malé ametystové krystaly.",
            "&aTip:&r V těchto tajemných biomech se staví stavby &eMage Tower&r (kapitola Stavby a města)."]),
        Q("oasis", "Desert Oasis", dep=["b_intro"], tasks=[biome("terralith:desert_oasis")], icon="minecraft:lily_pad", xp=15, d=[
            "&eDesert Oasis&r je zelené místo uprostřed pouště. Jsou tu jezírka, palmy, mech a lekníny.",
            "&aTip:&r Desert Oasis je dobré místo na první základnu v poušti – je tu voda i dřevo."]),
        Q("yellowstone", "Yellowstone", dep=["sakura", "moonlight", "oasis"], tasks=[biome("terralith:yellowstone")], icon="minecraft:magma_block", xp=30, shape="hexagon", size=1.5, s=A, d=[
            "Teď už vyraz dál od domova. Tyhle biomy jsou vzácnější a nebezpečnější.",
            "&eYellowstone&r má barevnou zem, jezírka a místa, ze kterých stoupá kouř.",
            "",
            "&cPozor na bloky magmatu&r – pálí, když na nich stojíš. Choď se Shiftem nebo se jim vyhni."]),
        Q("emerald", "Emerald Peaks", dep=["yellowstone"], tasks=[biome("terralith:emerald_peaks")], icon="minecraft:emerald", xp=30, d=[
            "&eEmerald Peaks&r jsou vysoké hory. Ve skále jsou dutiny z kalcitu a hladkého čediče. V nich je &eHlubinné smaragdové ložisko&r.",
            "&aTip:&r Na smaragdy použij krumpáč s očarováním &eFortune&r. Smaragdy se hodí na obchod s vesničany."]),
        Q("volcano", "Volcanic Peaks", dep=["yellowstone"], tasks=[biome("#terralith:volcanic")], icon="minecraft:lava_bucket", xp=40, d=[
            "Sopečný biom: &eVolcanic Peaks&r (vrchol sopky) nebo &eVolcanic Crater&r (kráter). Ze svahů tu teče láva.",
            "&cNechoď sem bez ohnivzdorných lektvarů.&r Do lávy se snadno spadne."]),
        Q("glacial", "Glacial Chasm", dep=["yellowstone"], tasks=[biome("terralith:glacial_chasm")], icon="minecraft:blue_ice", xp=30, d=[
            "&eGlacial Chasm&r je hluboká rokle v ledu se zasněženými stěnami a modrým ledem.",
            "Žijí tu králíci a vzácně lední medvědi. V noci sem chodí tuláci – kostlivci, jejichž šípy tě zpomalí.",
            "&aTip:&r Modrý led je nejkluzčí blok ve hře – hodí se na rychlé ledové cesty."]),
        Q("underground_jungle", "Underground Jungle", dep=["yellowstone"], tasks=[biome("terralith:cave/underground_jungle")], icon="minecraft:moss_block", xp=40, shape="hexagon", size=1.5, s=X, d=[
            "Poslední úroveň: biomy pod zemí. Musíš kopat nebo hledat hluboké jeskyně.",
            "&eUnderground Jungle&r je jeskyně plná mechu, bahna a vody. Žijí tu axolotlové, želvy a žáby."]),
        Q("frostfire", "Frostfire Caves", dep=["underground_jungle"], tasks=[biome("terralith:cave/frostfire_caves")], icon="minecraft:soul_lantern", xp=60, d=[
            "&eFrostfire Caves&r je mrazivá jeskyně pod zemí. Na stropě a na zemi je &eModrý led&r a na zemi hoří modrý &eOheň duší&r.",
            "Z příšer tu žijí jen kostlivci a tuláci. Ukrývá se tu ledový dungeon z Terralithu.",
            "&cPozor:&r do ohně duší nešlapej."]),
        Q("mantle", "Mantle Caves", dep=["underground_jungle"], tasks=[biome("terralith:cave/mantle_caves")], icon="minecraft:basalt", xp=60, d=[
            "&eMantle Caves&r jsou nejhlubší jeskyně, skoro u dna světa. Z mnoha míst tu kape láva a jsou tu pruhy čediče a magmatu.",
            "&cVezmi si ohnivzdorné lektvary a kbelík vody.&r"]),
        Q("skylands", "Skylands", dep=["underground_jungle"], tasks=[biome("#terralith:skylands")], icon="minecraft:feather", xp=100, d=[
            "Velmi vzácný biom &eSkylands&r: ostrovy, které se vznášejí ve vzduchu. Padají z nich vodopády.",
            "Skylands mají čtyři druhy: jarní, letní, podzimní a zimní.",
            "&aTip:&r Hledej je z výšky. Pomůžou ti Krovky nebo velká mapa."]),
    ],
)

# =====================================================================
# STAVBY A MĚSTA – T&T, Explorify, IDAS, RS, MVS, Create stavby (nová)
# =====================================================================
STRUCTURES = dict(
    key="structures", group="explore", title="Stavby a města",
    subtitle="Vesnice, hrady a ztracená místa", icon="minecraft:bell",
    quests=[
        Q("s_intro", "Stavby ve světě", icon="minecraft:bell", tasks=[auto()], xp=10, shape="hexagon", size=1.5, s=B, d=[
            "Ve světě je spousta staveb. Přidávají je mody &bTowns and Towers&r, &bExplorify&r, &bIntegrated Dungeons and Structures&r, &bRepurposed Structures&r, &bMoog's Voyager Structures&r a stavby pro &bCreate&r.",
            "Každý biom má jiné stavby. Čím vzácnější stavba, tím lepší poklad a silnější nepřátelé.",
            "",
            "&aTip:&r Stavby hledej z výšky – z hory nebo z vrcholu stromu je vidíš z dálky."]),
        Q("village", "Vesnice", dep=["s_intro"], tasks=[structure("#minecraft:village")], icon="minecraft:bell", xp=15, d=[
            "Vesnice s vesničany. &bTowns and Towers&r a &bRepurposed Structures&r jim dávají jiný vzhled v každém biomu.",
            "S vesničany můžeš obchodovat za smaragdy. Knihovník prodává očarované knihy.",
            "",
            "&aTip:&r Postav si u vesnice postel. Při útoku nájezdníků vesnici braň."]),
        Q("outpost", "Pillager Outpost", dep=["village"], tasks=[structure("#minecraft:pillager_outpost")], icon="minecraft:crossbow", xp=25, d=[
            "&ePillager Outpost&r je dřevěná věž, kde žijí nájezdníci s kušemi. &bTowns and Towers&r jim dává různý vzhled podle biomu.",
            "&cPozor:&r kapitán s praporem upustí &eZlověstnou lahvičku&r. Když ji vypiješ, při příchodu do vesnice spustíš nájezd."]),
        Q("tavern", "Tavern", dep=["s_intro"], tasks=[structure("explorify:tavern")], icon="minecraft:barrel", xp=15, d=[
            "&eTavern&r je velký hostinec od &bExplorify&r. Stojí v lese, v květinovém lese nebo na nížině.",
            "Uvnitř je hodně truhel s jídlem a věcmi z vesnice."]),
        Q("windmill", "Oak Windmill", dep=["s_intro"], tasks=[structure("create_structures_overhaul:oakwindmill")], icon="create:white_sail", xp=20, d=[
            "&eOak Windmill&r je dubový větrný mlýn z modu &bCreate: Structures Overhaul&r. Najdeš ho v lese, v květinovém lese nebo na nížině.",
            "Je postavený z dílů &bCreate&r. V sudech můžeš najít i díly Create, třeba ozubená kola nebo ložisko větrného mlýna (&eWindmill Bearing&r)."]),
        Q("fortified", "Fortified Village", dep=["village"], tasks=[structure("#terralith:fortified_villages")], icon="minecraft:stone_bricks", xp=30, d=[
            "&eFortified Village&r je vesnice s kamennými hradbami od &bTerralithu&r. Stojí na nížinách, horských loukách a vysočinách, další verze v poušti.",
            "Má hostinec, kováře a další dílny s truhlami."]),
        Q("castle_ruins", "Castle Ruins", dep=["s_intro"], tasks=[structure("mvs:castle_ruins")], icon="minecraft:cracked_stone_bricks", xp=20, d=[
            "&eCastle Ruins&r je rozpadlý hrad od &bMoog's Voyager Structures&r. Může stát skoro kdekoli na pevnině.",
            "V sutinách jsou truhly a sudy."]),
        Q("idas_castle", "Castle", dep=["fortified", "castle_ruins"], tasks=[structure("idas:castle")], icon="minecraft:iron_bars", xp=50, shape="hexagon", size=1.5, s=A, d=[
            "Teď vyraz za velkými stavbami. Jsou dál a některé hlídají nepřátelé.",
            "Hrad &eCastle&r z modu &bIntegrated Dungeons and Structures&r stojí v biomech &eForest&r, &eBirch Forest&r, &ePlains&r nebo &eMeadow&r. Žijí v něm vesničané.",
            "Je v něm knihovna, ložnice, sklady i trůnní sál – a desítky truhel."]),
        Q("hunters", "Hunter's Cabin", dep=["idas_castle"], tasks=[structure("idas:hunters_cabin")], icon="minecraft:crossbow", xp=40, d=[
            "&eHunter's Cabin&r je chata v lese nebo v tajze. Obsadili ji nájezdníci a jsou tu i jejich líhně.",
            "&cNájezdníci střílí z kuší.&r Vezmi si štít."]),
        Q("haunted", "Haunted Manor", dep=["idas_castle"], tasks=[structure("idas:haunted_manor")], icon="minecraft:skeleton_skull", xp=50, d=[
            "&eHaunted Manor&r je velký temný dům v biomu &eDark Forest&r. Je plný kostlivců a líhní.",
            "Za odvahu tě čekají truhly s poklady a nářadím."]),
        Q("mage", "Mage Tower", dep=["idas_castle"], tasks=[structure("#terralith:mage_towers")], icon="minecraft:enchanted_book", xp=50, d=[
            "Stavby &eMage Tower&r a &eMage Complex&r jsou věže a sídla mágů od &bTerralithu&r. Stojí jen v kouzelných biomech, třeba &eMoonlight Grove&r, &eLavender Valley&r, &eAmethyst Rainforest&r nebo &eMirage Isles&r.",
            "&cHlídají je nájezdníci, mstitelé, čarodějnice i mágové.&r V truhlách je cenný poklad."]),
        Q("train_station", "Lost Train Station", dep=["windmill", "idas_castle"], tasks=[structure("create_structures_arise:createlosttrainstation")], icon="create:railway_casing", xp=40, d=[
            "&eLost Train Station&r je opuštěné nádraží z &bCreate: Structures Arise&r. Je v něm míchačka, lis, drtící kola i mechanická paže.",
            "&aTip:&r Stroje můžeš rozebrat a odnést si je. Ušetříš tak hodně surovin."]),
        Q("pillager_fortress", "Pillager Fortress", dep=["hunters", "haunted", "mage"], tasks=[structure("idas:pillager_fortress")], icon="minecraft:ominous_bottle", xp=120, shape="hexagon", size=1.5, s=X, d=[
            "Nejtěžší stavby ve světě. Jdi jen v dobré zbroji, s jídlem a lektvary.",
            "&ePillager Fortress&r stojí na nížinách, v tajze, v džungli, v květinovém lese a v dalších biomech. Žijí v ní mstitelé, mágové i ničitelé a jsou tu líhně.",
            "Ve vězení najdeš zajaté vesničany."]),
        Q("airship", "Pillager Steampunk Airship", dep=["pillager_fortress"], tasks=[structure("create_structures_arise:pillagersteampunkairship")], icon="create:propeller", xp=150, d=[
            "&ePillager Steampunk Airship&r je obří létající loď nájezdníků z &bCreate: Structures Arise&r. Vznáší se vysoko na nebi (asi ve výšce 160–190 bloků).",
            "Na palubě jsou nájezdníci, jejich líhně a líhně přízraků. Truhel je tu přes 40.",
            "&aTip:&r Nahoru se dostaneš na Krovkách nebo po vysokém sloupu."]),
        Q("ochrum_tower", "Tower of Ochrum", dep=["pillager_fortress"], tasks=[structure("create_structures_arise:towerofochrum")], icon="create:ochrum", xp=150, d=[
            "&eTower of Ochrum&r je velmi vysoká věž (asi 176 bloků) z &bCreate: Structures Arise&r.",
            "Uvnitř jsou líhně tuláků, přízraků a jedna líheň mágů. V truhlách najdeš poklad."]),
    ],
)

# =====================================================================
# TVOROVÉ – Alex's Mobs, Naturalist a další (původní kapitola)
# =====================================================================
CREATURES = dict(
    key="creatures", group="explore", title="Divoká zvířata",
    subtitle="Alex's Mobs, Naturalist a další", icon="alexsmobs:animal_dictionary",
    quests=[
        Q("c_intro", "Divočina", icon="alexsmobs:animal_dictionary", tasks=[auto()], xp=10, shape="hexagon", size=1.5, s=B, d=[
            "Ve světě žije hodně nových zvířat a příšer. Přidávají je mody &bAlex's Mobs&r, &bNaturalist&r, &bCritters and Companions&r, &bAdorable Hamster Pets&r a &bBen's Sharks&r.",
            "Některá zvířata jsou hodná, jiná útočí. Ze spousty z nich padají věci na užitečnou výbavu.",
            "",
            "&aTip:&r Když se podíváš na zvíře, nahoře na obrazovce uvidíš jeho jméno."]),
        Q("dict", "Zvířecí slovník", dep=["c_intro"], items=[("alexsmobs:animal_dictionary", 1)], xp=20, d=[
            "Kniha od &bAlex's Mobs&r (&eAnimal Dictionary&r). Popisuje každé zvíře: kde žije, co z něj padá a jak ho ochočit.",
            "Při prvním připojení ji dostaneš zdarma. Když ji ztratíš, vyrob ji z knihy, zeleného barviva a jedné věci ze zvířete (například &eCrocodile Scute&r)."]),
        Q("banana", "Banány!", dep=["dict"], items=[("alexsmobs:banana", 1)], xp=15, d=[
            "Banán (&eBanana&r) občas padá z &eTropického listí&r. Je to vzácné – asi jednou z 200 listů.",
            "Nelámej listí nůžkami ani s očarováním &eSilk Touch&r, pak banán nepadá. Očarování &eFortune&r šanci zvýší.",
            "&aTip:&r Banány milují gorily a kapucínské opičky."]),
        Q("capuchin", "Opičí kamarád", dep=["banana"], tasks=[adv("alexsmobs:alexsmobs/tame_capuchin")], icon="alexsmobs:banana", xp=25, d=[
            "Opička &eCapuchin Monkey&r žije v džungli a v mangrovech.",
            "Ochočíš ji banány. Ochočená opička tě následuje a bojuje za tebe – může ti sedět na rameni a házet kameny."]),
        Q("roadrunner", "Pírko kukačky", dep=["dict"], items=[("alexsmobs:roadrunner_feather", 1)], xp=20, d=[
            "Pírko kukačky (&eRoadrunner Feather&r) padá z ptáka &eRoadrunner&r. Ten běhá v poušti a v pustině.",
            "Je rychlý, takže ho musíš dohnat nebo zaskočit."]),
        Q("rr_boots", "Běžecké boty", dep=["roadrunner"], items=[("alexsmobs:roadrunner_boots", 1)], xp=30, d=[
            "Boty kukačky (&eRoadrunner Boots&r) tě zrychlí, když jdeš po písku.",
            "Vyrob je ze 4 pírek kukačky, &eKožených bot&r a 2 bloků &eOpracovaného pískovce&r."]),
        Q("bear", "Medvědí srst", dep=["dict"], items=[("alexsmobs:bear_fur", 1)], xp=25, d=[
            "Srst (&eHair of Bear&r) padá z medvěda &eGrizzly Bear&r. Ten žije v lesích a v tajze.",
            "&cMedvěd je klidný jen z dálky.&r Když se přiblížíš, zaútočí. Mívá u sebe mláďata."]),
        Q("grizzly_tame", "Ochočený grizzly", dep=["bear"], tasks=[adv("alexsmobs:alexsmobs/tame_grizzly_bear")], icon="minecraft:salmon", xp=50, d=[
            "Medvěda nejdřív nakrm medem (&ePlástev medu&r nebo lahev medu). Pak je chvíli klidný.",
            "V tu chvíli mu dej &eSyrového lososa&r. Na ochočeném medvědovi můžeš jezdit do boje."]),
        Q("raccoon", "Mývalí ocas", dep=["dict"], items=[("alexsmobs:raccoon_tail", 1)], xp=20, d=[
            "Ocas (&eRaccoon Tail&r) padá z mývala &eRaccoon&r. Mýval žije v lesích, na nížinách a v tajze.",
            "&aTip:&r Mývala ochočíš vajíčkem, když je blízko vody. Nejdřív si ho opere."]),
        Q("frontier_cap", "Čepice zálesáka", dep=["bear", "raccoon"], items=[("alexsmobs:frontier_cap", 1)], xp=30, d=[
            "Čepice zálesáka (&eFrontiersman's Cap&r) tě zrychlí, když se plížíš.",
            "Vyrob ji z 5 kusů medvědí srsti, &eKožené čapky&r a mývalího ocasu."]),
        Q("croc", "Krokodýlí šupina", dep=["dict"], items=[("alexsmobs:crocodile_scute", 1)], xp=30, d=[
            "Šupina (&eCrocodile Scute&r) padá z krokodýla &eCrocodile&r. Krokodýl žije v bažinách, v mangrovech a v řekách.",
            "&cKrokodýl je nebezpečný.&r Umí tě chytit a táhnout pod vodu. Bojuj s ním na souši."]),
        Q("croc_chest", "Krokodýlí brnění", dep=["croc"], items=[("alexsmobs:crocodile_chestplate", 1)], xp=40, d=[
            "Krokodýlí hrudní plát (&eCrocodile Chestplate&r) je pevná zbroj.",
            "Vyrob ho z 8 krokodýlích šupin."]),
        Q("blossom", "Akáciový květ", dep=["dict"], items=[("alexsmobs:acacia_blossom", 1)], xp=25, d=[
            "Akáciový květ (&eAcacia Blossom&r) občas padá z &eAkáciového listí&r. Je vzácný (asi jednou ze 130 listů).",
            "Stejně jako u banánů nepoužívej nůžky ani očarování &eSilk Touch&r."]),
        Q("elephant", "Sloní jízda", dep=["blossom"], tasks=[adv("alexsmobs:alexsmobs/tame_elephant")], icon="alexsmobs:acacia_blossom", xp=40, d=[
            "Slon &eElephant&r žije ve stádech na savaně. Ochočíš ho akáciovým květem.",
            "Ochočit jde jen sloní mládě nebo slon bez klů. Na slonovi můžeš jezdit a s truhlou ti nese věci."]),
        Q("centipede", "Cave Centipede", dep=["dict"], tasks=[kill("alexsmobs:centipede_head")], icon="alexsmobs:centipede_leg", xp=40, shape="hexagon", size=1.5, s=A, d=[
            "Teď už lov těžších a vzácnějších tvorů. Na mnoho z nich potřebuješ dobrou zbroj.",
            "Stonožka &eCave Centipede&r je vzácná a žije hluboko v jeskyních. &cJe pomalá, ale silná a její kousnutí otráví.&r"]),
        Q("centipede_legs", "Lezecké kalhoty", dep=["centipede"], items=[("alexsmobs:centipede_leggings", 1)], xp=50, d=[
            "Kalhoty ze stonožky (&eCave Centipede Leggings&r) ti dovolí lézt po stěnách.",
            "Vyrob je ze 7 nožiček stonožky (&eCave Centipede Leg&r)."]),
        Q("outback", "Kalhoty z buše", dep=["centipede"], items=[("alexsmobs:emu_leggings", 1)], xp=50, d=[
            "Kalhoty z buše (&eOutback Leggings&r) ti dávají šanci, že se tě nedotkne šíp ani jiná střela.",
            "Vyrob je ze 4 pírek emu (&eEmu Feather&r) a 3 klokaních kůží (&eKangaroo Hide&r).",
            "&eEmu&r i klokan &eKangaroo&r žijí na savaně a v pustině. &cEmu se brání ve skupině.&r"]),
        Q("antlers", "Losí parohy", dep=["centipede"], items=[("alexsmobs:moose_headgear", 1)], xp=40, d=[
            "Čelenka s parohy (&eAntler Headdress&r) zvýší, jak daleko odhodíš nepřítele úderem.",
            "Vyrob ji ze 2 losích parohů (&eMoose Antler&r), železného ingotu a 2 vláken.",
            "Los &eMoose&r žije v zasněžené tajze. Parohy sám shazuje jednou za několik dní."]),
        Q("rocky", "Kamenný pancíř", dep=["centipede"], items=[("alexsmobs:rocky_chestplate", 1)], xp=50, d=[
            "Kamenný pancíř (&eRock Shell Chestplate&r): když sprintuješ, kutálíš se jako koule.",
            "Vyrob ho z 8 kamenných ulit (&eRocky Shell&r). Padají z tvora &eRocky Roller&r v biomu &eDripstone Caves&r. &cTen útočí.&r"]),
        Q("froststalker", "Mrazivá helma", dep=["centipede"], items=[("alexsmobs:froststalker_helmet", 1)], xp=50, d=[
            "Helma z rohu (&eFroststalker Helmet&r). Šelmy &eFroststalker&r si pak myslí, že jsi jedna z nich. &cKdyž některou napadneš, obrátí se proti tobě.&r",
            "Vyrob ji z rohu (&eFroststalker Horn&r) a 5 bloků &eHutného ledu&r. Froststalkeři žijí v biomech &eIce Spikes&r a &eFrozen Peaks&r."]),
        Q("fish_oil", "Rybí olej", dep=["centipede"], items=[("alexsmobs:fish_oil", 1)], xp=30, d=[
            "Rybí olej (&eFish Oil&r) vyrobíš z lahvičky a 4 ryb &eBlobfish&r. Ty žijí hluboko v oceánu.",
            "Olejem ochočíš orla."]),
        Q("eagle", "Sokolník", dep=["fish_oil"], tasks=[adv("alexsmobs:alexsmobs/tame_bald_eagle")], icon="alexsmobs:falconry_glove", xp=50, d=[
            "Orel &eBald Eagle&r žije v horských lesích. Ochočíš ho rybím olejem.",
            "Se sokolnickou rukavicí (&eFalconry Glove&r, ze 4 kůží a medvědí srsti) ho můžeš nosit na ruce a posílat na nepřátele."]),
        Q("rainbow", "Duhové sklo", dep=["centipede"], items=[("alexsmobs:rainbow_glass", 1)], xp=30, d=[
            "Duhové sklo (&eRainbow Glass&r) je barevné a svítí.",
            "Vyrob 8 kusů z 8 skel a duhového želé (&eRainbow Jelly&r). To padá z žebernatek &eComb Jelly&r v ledových oceánech."]),
        Q("th_wing", "Křídlo jestřábníka", dep=["outback", "rocky"], items=[("alexsmobs:tarantula_hawk_wing", 1)], xp=80, shape="hexagon", size=1.5, s=X, d=[
            "Nejtěžší výbava z Alex's Mobs. Na to potřebuješ zkušenosti i dobrou zbroj.",
            "Křídlo (&eTarantula Hawk Wing&r) složíš z 9 roztrhaných kousků (&eTattered Tarantula Hawk Wing&r). Padají z obří vosy &eTarantula Hawk&r v poušti."]),
        Q("th_elytra", "Vosí krovky", dep=["th_wing"], items=[("alexsmobs:tarantula_hawk_elytra", 1)], xp=120, d=[
            "Vosí krovky (&eTarantula Hawk Elytra&r) fungují jako Krovky, ale dávají navíc 3 body brnění.",
            "Vyrob je ze 2 křídel a obyčejných &eKrovek&r z Endu."]),
        Q("capsid", "Raketa z Endu", dep=["th_wing"], items=[("alexsmobs:enderiophage_rocket", 1)], xp=80, d=[
            "Na ostrovech Endu žije &eEnderiophage&r, podivný stroj, který loví endermany. Padá z něj &eCapsid&r.",
            "Z capsidu, 2 železných nugetů a 2 bloků &eEnderitu&r vyrobíš 3 rakety (&eEnderiophage Rocket&r). Fungují jako rachejtle pro let s Krovkami."]),
        Q("mimicream", "Mimikrém", dep=["th_wing"], items=[("alexsmobs:mimicream", 1)], xp=80, d=[
            "Mimikrém (&eMimicream&r) padá z &eMimicube&r. Ten žije na vnějších ostrovech Endu u staveb &eEnd City&r.",
            "Z 8 mimikrémů a nástroje vyrobíš jeho kopii. &cKopie má ale nulovou výdrž&r – musíš ji opravit."]),
        Q("net", "Síť na zvířátka", dep=["c_intro"], items=[("naturalist:capture_net", 1)], xp=15, d=[
            "&bNaturalist&r přidává jeleny, medvědy, šneky, motýly, lvy a další zvířata.",
            "Síť (&eCapture Net&r) vyrobíš z bambusu a vláken. Klikni s ní pravým tlačítkem na malé zvíře a chytíš ho jako předmět.",
            "Chytíš motýla, housenku, mravence, kraba, šneka, krysu, ježka nebo štíra."]),
        Q("butterfly", "Motýl", dep=["net"], items=[("naturalist:butterfly", 1)], xp=20, d=[
            "Chyť motýla (&eButterfly&r) sítí. Motýli létají v lesích, na nížinách a v bažinách.",
            "Chycený motýl je v inventáři jako předmět."]),
        Q("venison", "Zvěřina", dep=["c_intro"], items=[("naturalist:venison", 1)], xp=15, d=[
            "Zvěřina (&eVenison&r) padá z jelena &eDeer&r z modu Naturalist. Jeleni žijí v lesích, třeba v biomech &eCherry Grove&r a &eSakura Grove&r.",
            "Jsou plaší a rychle utíkají, takže se k nim musíš připlížit. Zvěřinu si upeč."]),
        Q("bear_honey", "Med pro medvěda", dep=["venison"], tasks=[adv("naturalist:husbandry/feed_bear_honeycomb")], icon="minecraft:honeycomb", xp=25, d=[
            "Medvědi z Naturalistu žijí v lesích a v tajze.",
            "Hoď medvědovi &ePlástev medu&r na zem. Medvěd si ho vezme a sní."]),
        Q("critters", "Vážčí křídlo", dep=["c_intro"], items=[("crittersandcompanions:dragonfly_wing", 1)], xp=20, d=[
            "&bCritters and Companions&r přidává vydry, fretky, pandy červené, kapry koi, vážky a další.",
            "Vážčí křídlo (&eDragonfly Wing&r) padá z vážky. Vážky létají hlavně u vody.",
            "&aTip:&r Křídlem ochočíš pavouka &eJumping Spider&r. Víc v kapitole &eMazlíčci a chov&r."]),
        Q("hamster", "Křeččí směs", dep=["c_intro"], items=[("adorablehamsterpets:hamster_food_mix", 1)], xp=20, d=[
            "Krmná směs pro křečky (&eHamster Food Mix&r) z modu &bAdorable Hamster Pets&r.",
            "Vyrob ji ze 3 slunečnicových semínek, 2 dýňových semínek, mrkve a 3 semínek pšenice (dá 4 kusy).",
            "Směs křečka vyléčí a odemkne mu lícní torbu. &cKřečka s ní ale neochočíš&r – na to je okurka (kapitola &eMazlíčci a chov&r)."]),
        Q("shark", "Žraločí zub", dep=["ocean:fish_bucket"], items=[("benssharks:shark_tooth", 1)], xp=30, d=[
            "Žraločí zub (&eShark Tooth&r) z &bBen's Sharks&r nepadá ze zabitého žraloka.",
            "Vezmi do hlavní ruky rybí kbelík (&eFish Bucket&r) a klikni pravým tlačítkem na žraloka &eTiger Shark&r. Žralok ho sní a upustí zub.",
            "Žraloci Tiger Shark žijí v biomech &eWarm Ocean&r a &eLukewarm Ocean&r a u pláží."]),
    ],
)

# =====================================================================
# MAZLÍČCI A CHOV – ochočování, JEB, křečci, C&C, Fowl Play, Autumnity (nová)
# =====================================================================
PETS = dict(
    key="pets", group="explore", title="Mazlíčci a chov",
    subtitle="Ochočování a péče o zvířata", icon="minecraft:lead",
    quests=[
        Q("p_intro", "Ochoč si zvíře", icon="minecraft:lead", tasks=[auto()], xp=10, shape="hexagon", size=1.5, s=B, d=[
            "Ochočené zvíře je tvoje: chodí za tebou, brání tě nebo ti pomáhá. Většinu zvířat ochočíš tak, že jim dáš správné jídlo.",
            "Jaké jídlo které zvíře chce, ukáže &bJust Enough Breeding&r v JEI. Najeď na jídlo a stiskni U – uvidíš záložky &eBreeding&r (rozmnožování) a &eTaming&r (ochočení).",
            "&cPozor:&r zvířata z Fowl Play a křečky JEI neukazuje. Pro ně čti questy v této kapitole."]),
        Q("tame_any", "První mazlíček", dep=["p_intro"], tasks=[adv("minecraft:husbandry/tame_an_animal")], icon="minecraft:bone", xp=15, d=[
            "Ochoč jakékoli zvíře. Nejsnadnější je vlk (kost) nebo kočka (syrová ryba).",
            "Když se kolem zvířete objeví srdíčka, je tvoje. Pravým tlačítkem ho posadíš nebo zase zvedneš."]),
        Q("h_seeds", "Okurková semínka", dep=["p_intro"], items=[("adorablehamsterpets:cucumber_seeds", 1)], xp=10, d=[
            "Křečky přidává &bAdorable Hamster Pets&r. Křečci žijí v mnoha biomech a v každém mají jinou barvu srsti.",
            "V teplejších biomech (nížiny, savany, okraje džungle) rostou divoké okurkové keře. Klikni na ně pravým tlačítkem a dostaneš okurková semínka (&eCucumber Seeds&r). Zasaď je na pole."]),
        Q("h_slice", "Plátky okurky", dep=["h_seeds"], items=[("adorablehamsterpets:sliced_cucumber", 1)], xp=15, d=[
            "Z jedné okurky (&eCucumber&r) vyrobíš 3 plátky (&eSliced Cucumber&r).",
            "Plátky okurky jsou návnada na křečky."]),
        Q("h_tame", "Ochoč křečka", dep=["h_slice"], tasks=[adv("adorablehamsterpets:husbandry/tame_hamster")], icon="adorablehamsterpets:sliced_cucumber", xp=25, d=[
            "Drž plátek okurky a plíž se (Shift) ke křečkovi. Klikni na něj pravým tlačítkem a zkoušej to, dokud se neochočí.",
            "Ochočený křeček tě následuje. Barva srsti záleží na tom, kde žil."]),
        Q("h_book", "Kniha o křečcích", dep=["h_slice"], items=[("adorablehamsterpets:hamster_guide_book", 1)], xp=15, d=[
            "Kniha &eHamster Tips&r (průvodce o křečcích) vysvětluje všechno o křečcích. Je v angličtině.",
            "Vyrob ji z knihy a plátku okurky."]),
        Q("h_pouch", "Lícní torba", dep=["h_tame", "creatures:hamster"], tasks=[adv("adorablehamsterpets:husbandry/cheeky_storage")], icon="adorablehamsterpets:hamster_food_mix", xp=25, d=[
            "Nakrm ochočeného křečka krmnou směsí (&eHamster Food Mix&r). Odemkneš mu tím lícní torbu.",
            "Shift + pravé tlačítko na křečka otevře torbu se 6 místy. Křeček ti v ní nosí věci."]),
        Q("h_shoulder", "Křeček na rameni", dep=["h_tame"], tasks=[adv("adorablehamsterpets:husbandry/shoulder_hamster")], icon="adorablehamsterpets:cheese", xp=25, shape="hexagon", size=1.5, s=A, d=[
            "Teď z křečka uděláš pomocníka. Z kbelíku mléka vyrobíš 3 kusy sýra (&eCheese&r).",
            "Drž sýr u ochočeného křečka. Křeček ti vyskočí na rameno."]),
        Q("h_diamond", "Nos na poklady", dep=["h_shoulder"], tasks=[adv("adorablehamsterpets:husbandry/nose_for_treasure")], icon="minecraft:diamond", xp=50, d=[
            "Křeček na rameni čenichá. Když jsi blízko diamantů (asi do 10 bloků), dá ti vědět.",
            "&aTip:&r Choď s křečkem na rameni po jeskyních. Zlato ho mate, nenech se splést. Taky zapiští, když na tebe míří creeper."]),
        Q("silk", "Hedvábí", dep=["p_intro"], items=[("crittersandcompanions:silk", 1)], xp=15, d=[
            "Hedvábí (&eSilk&r) z &bCritters and Companions&r najdeš v hedvábných kokonech na stromech v lesích a džunglích a v biomu &eLush Caves&r. Padá i ze skákavého pavouka (&eJumping Spider&r).",
            "Z hedvábí vyrobíš vodítko, hák nebo obyčejné vlákno."]),
        Q("grapple", "Hák s lanem", dep=["silk"], items=[("crittersandcompanions:grappling_hook", 1)], xp=30, d=[
            "Hák (&eGrappling Hook&r) vystřelíš do bloku. Zachytí se a přitáhne tě k sobě. Hodí se na skály a hory.",
            "Vyrob ho ze 4 hedvábí a železného ingotu."]),
        Q("pearl", "Perlový náhrdelník", dep=["grapple"], items=[("crittersandcompanions:pearl_necklace_1", 1)], xp=80, shape="hexagon", size=1.5, s=X, d=[
            "Perly jsou vzácné. Dá ti je jen vydra &eOtter&r, která žije v řekách.",
            "Dej vydře škeble (&eClam&r). Chytíš je rybařením nebo padají z utopenců. Vydra škebli otevře a občas v ní najde perlu.",
            "Náhrdelník (&ePearl Necklace 1&r) ze 4 perel nos na krku: zrychlí plavání a utopenci a strážci tě hůř uvidí."]),
        Q("scarecrow", "Strašák", dep=["p_intro"], items=[("fowlplay:scarecrow", 1)], xp=15, d=[
            "&bFowl Play&r přidává ptáky: holuby, vrabce, kardinály, racky, tučňáky, jestřáby a další.",
            "Strašák (&eScarecrow&r) ze 2 balíků slámy a 3 tyček ptáky odežene od tvého pole.",
            "&aTip:&r Ptáci se bojí hráčů a jestřábů. Holuba můžeš ochočit."]),
        Q("hawkeye", "Sokolí oko", dep=["scarecrow"], tasks=[adv("fowlplay:adventure/damage_flying_bird")], icon="minecraft:arrow", xp=30, optional=True, d=[
            "Zasáhni šípem letícího ptáka. Je to těžké – ptáci létají rychle a mění směr."]),
        Q("syrup", "Javorový sirup", dep=["p_intro"], items=[("autumnity:syrup_bottle", 1)], xp=25, d=[
            "&bAutumnity&r přidává podzimní javory. Rostou i v obyčejných lesích.",
            "Oloupej javorový kmen sekerou. Někdy se objeví mízový kmen. Klikni na něj prázdnou lahvičkou a dostaneš mízu (&eSap Bottle&r).",
            "Mízu upeč v peci – vznikne sirup (&eSyrup Bottle&r)."]),
        Q("pancake", "Palačinka", dep=["syrup"], items=[("autumnity:pancake", 1)], xp=25, d=[
            "Palačinka (&ePancake&r) se vyrábí ze sirupu, mléka, vajíčka a 2 pšenic.",
            "Je to dobré jídlo na cesty."]),
    ],
)

# =====================================================================
# MOŘE A ŘEKY – Upgrade Aquatic, Ben's Sharks (nová)
# =====================================================================
OCEAN = dict(
    key="ocean", group="explore", title="Moře a řeky",
    subtitle="Upgrade Aquatic a Ben's Sharks", icon="minecraft:heart_of_the_sea",
    quests=[
        Q("o_intro", "Pod hladinou", icon="minecraft:heart_of_the_sea", tasks=[auto()], xp=10, shape="hexagon", size=1.5, s=B, d=[
            "Voda je v tomto packu živější. &bUpgrade Aquatic&r přidává ryby, rostliny a mořské příšery. &bBen's Sharks&r přidává hodně druhů žraloků.",
            "Pod vodou ti dochází vzduch. Vezmi si lektvar dýchání pod vodou.",
            "&aTip:&r &eHelma z želvoviny&r ti díky Upgrade Aquatic dává dýchání pod vodou celou dobu, dokud ji nosíš. Jen se přitom opotřebovává."]),
        Q("pike", "Štika v kbelíku", dep=["o_intro"], items=[("upgrade_aquatic:pike_bucket", 1)], xp=15, d=[
            "Štika &ePike&r žije v řekách a bažinách.",
            "Klikni na ni &eKbelíkem vody&r a chytíš ji živou (&eBucket of Pike&r). Štiky mají spoustu různých barev."]),
        Q("lionfish", "Perutýn", dep=["o_intro"], items=[("upgrade_aquatic:cooked_lionfish", 1)], xp=15, d=[
            "Perutýn &eLionfish&r žije v teplých oceánech. Chytíš ho i na prut.",
            "&cPozor, umí otrávit.&r Upeč si ho (&eCooked Lionfish&r)."]),
        Q("pickerelweed", "Vzduch z rostliny", dep=["o_intro"], tasks=[adv("upgrade_aquatic:husbandry/eat_pickerelweed")], icon="upgrade_aquatic:boiled_pickerelweed", xp=20, d=[
            "Rostlina &ePickerelweed&r roste u řek, v bažinách a v džungli.",
            "Upeč ji v peci nebo udírně a sněz &eBoiled Pickerelweed&r. Pod vodou ti vrátí bublinky vzduchu."]),
        Q("bedroll", "Spaní pod vodou", dep=["o_intro"], tasks=[adv("upgrade_aquatic:adventure/sleep_underwater")], icon="upgrade_aquatic:bedroll", xp=20, d=[
            "Spací vak (&eBedroll&r) vyrobíš z 5 kůží a 1 bílé vlny.",
            "Na rozdíl od postele v něm můžeš spát i pod vodou. Vyspi se v něm pod hladinou."]),
        Q("fish_bucket", "Rybí kbelík", dep=["o_intro"], items=[("benssharks:fish_bucket", 1)], xp=15, d=[
            "Rybí kbelík (&eFish Bucket&r) je krmení pro žraloky. Vyrob ho z kbelíku, kostní moučky a 2 různých ryb (třeba treska a losos).",
            "&cNěkteří žraloci jsou nebezpeční.&r Než skočíš do moře, podívej se, co v něm plave."]),
        Q("feed_shark", "Krmení žraloka", dep=["fish_bucket"], tasks=[adv("benssharks:pleasure")], icon="benssharks:fish_bucket", xp=30, d=[
            "Drž rybí kbelík v hlavní ruce a klikni pravým tlačítkem na žraloka &eTiger Shark&r.",
            "Žralok se nají a za odměnu ti dá žraločí zub. Prázdný kbelík dostaneš zpět."]),
        Q("shark_club", "Žraločí kyj", dep=["creatures:shark"], items=[("benssharks:shark_tooth_club", 1)], xp=30, d=[
            "Kyj se žraločími zuby (&eShark Tooth Club&r). Vyrob ho ze 4 žraločích zubů, 2 prken a tyčky."]),
        Q("ammonite", "Zkamenělá loděnka", dep=["o_intro"], items=[("upgrade_aquatic:embedded_ammonite", 1)], xp=20, shape="hexagon", size=1.5, s=A, d=[
            "Teď se pustíš do hlubin a za mořskými příšerami.",
            "Zkamenělina (&eEmbedded Ammonite&r) je blok v kameni pod plážemi a oceány. Když ji upečeš v peci, dostaneš &eUlitu loděnky&r."]),
        Q("coralstone", "Korálový kámen", dep=["ammonite"], items=[("upgrade_aquatic:coralstone", 1)], xp=25, d=[
            "Korálový kámen (&eCoralstone&r) vyrobíš z 8 &eKamenných cihel&r a &eUlity loděnky&r (dá 8 kusů).",
            "Když leží vedle bloku korálu, časem se změní na korálový kámen té barvy."]),
        Q("luminous_prismarine", "Svítící prismarín", dep=["ammonite", "exploration:monument"], items=[("upgrade_aquatic:luminous_prismarine", 1)], xp=30, d=[
            "Svítící prismarín (&eLuminous Prismarine&r) vyrobíš z 8 prismarínových střepů a &eVáčku světélkujícího inkoustu&r.",
            "Svítí, takže se hodí na osvětlení staveb pod vodou."]),
        Q("thrasher", "Zub mlátičky", dep=["ammonite"], items=[("upgrade_aquatic:thrasher_tooth", 1)], xp=40, d=[
            "&eThrasher&r je mořská příšera v chladných a ledových oceánech.",
            "&cUmí tě chytit do tlamy a vidí tě přes zvukové vlny.&r Padá z ní zub (&eThrasher Tooth&r)."]),
        Q("tooth_lantern", "Zubová lucerna", dep=["thrasher"], items=[("upgrade_aquatic:tooth_lantern", 1)], xp=25, d=[
            "Lucerna (&eTooth Lantern&r) ze 2 zubů mlátičky a prismarínového krystalu.", "Z 9 zubů vyrobíš i blok zubů na stavbu."]),
        Q("elder_eye", "Oko prastrážce", dep=["exploration:elder"], items=[("upgrade_aquatic:elder_eye", 1)], xp=40, d=[
            "Z každého bosse &eElder Guardian&r padne oko (&eElder Eye&r).",
            "Je to senzor: když před ním stojí živý tvor, vydá redstone signál. Hodí se na pasti a automatické dveře."]),
        Q("great_thrasher", "Great Thrasher", dep=["thrasher"], tasks=[kill("upgrade_aquatic:great_thrasher")], icon="upgrade_aquatic:disc_fragment_atlantis", xp=120, shape="hexagon", size=1.5, s=X, d=[
            "&eGreat Thrasher&r je největší mořská příšera Upgrade Aquatic. Objevuje se jen v hlubokém ledovém oceánu místo obyčejného Thrashera.",
            "Padají z ní zuby a někdy &eÚlomek desky&r (&eDisc Fragment&r). Z 9 úlomků složíš gramofonovou desku."]),
        Q("trident", "Trojzubec", dep=["shark_club", "thrasher"], items=[("minecraft:trident", 1)], xp=80, d=[
            "&eTrojzubec&r obvykle padá jen z utopenců. Tady si ho můžeš vyrobit.",
            "&bBen's Sharks&r: 3 zuby v prismarínu (&eDent&r, žraločí zub nad prismarínovým střepem) a 2 prismarínové střepy.",
            "&bUpgrade Aquatic&r: 3 zuby mlátičky a 2 prismarínové tyčky (&ePrismarine Rod&r)."]),
    ],
)

# =====================================================================
# LUMINOUS – Beasts, Overworld, Nether, Butterflies, Tag (původní kapitola)
# =====================================================================
LUMINOUS = dict(
    key="luminous", group="explore", title="Luminous",
    subtitle="Bestie, motýli a strašidla", icon="luminous_beasts:ultimate_bestiary",
    quests=[
        Q("l_intro", "Svět Luminous", icon="luminous_beasts:ultimate_bestiary", tasks=[auto()], xp=10, shape="hexagon", size=1.5, s=B, d=[
            "Mody &bLuminous&r přidávají motýly, světlušky, nové příšery, dekorace a hlavně &ebestie&r – velké a silné tvory.",
            "Bestie v Overworldu se objevují jen v noci, pod širým nebem a ve tmě. Každá žije v jiném biomu. Některé se líhnou z vajec nebo z kokonů.",
            "",
            "Začni motýly. Až budeš mít diamanty a dobrou zbroj, vyrob si &eBestiář&r a jdi na bestie."]),
        Q("lw_net", "Síťka na motýly", dep=["l_intro"], items=[("luminousworld:butterfly_net", 1)], xp=15, d=[
            "Síťka (&eButterfly Net&r) z &bLuminous Overworld&r. Vyrob ji ze 2 zlatých ingotů, vlákna a 2 tyček.",
            "Recept je stejný jako u síťky z &bLuminous Butterflies&r. Kterou síťku dostaneš, vybereš tlačítkem u výsledku receptu.",
            "&cMotýly chytíš jen touto síťkou z Luminous Overworld.&r"]),
        Q("net", "Druhá síťka", dep=["lw_net"], items=[("luminous_butterflies:butterfly_net", 1)], xp=10, d=[
            "Síťka z modu &bLuminous Butterflies&r má stejný recept. U výsledku receptu přepni na druhou verzi.",
            "Motýli z Luminous Butterflies se ale v tomto packu neobjevují. Tahle síťka je jen do sbírky."]),
        Q("encyclopedia", "Encyklopedie motýlů", dep=["net"], items=[("luminous_butterflies:butterfly_encyclopedia", 1)], xp=20, optional=True, d=[
            "Encyklopedii motýlů nejde vyrobit. Koupíš ji od obchodníka.",
            "Potulný obchodník ji někdy prodává za 15 smaragdů a knihu. Knihovník na třetí úrovni za 8 diamantů a knihu."]),
        Q("jar", "Sklenice", dep=["lw_net"], items=[("luminousworld:jar", 1)], xp=10, d=[
            "Sklenice (&eGlass Jar&r) se vyrábí z dřevěné desky a skla.",
            "Polož ji na zem. Pak na ni klikni síťkou, ve které máš chyceného motýla – motýl se přesune do sklenice."]),
        Q("monarch", "Monarcha ve sklenici", dep=["jar"], items=[("luminousworld:monarch_jar", 1)], xp=20, d=[
            "&eMonarch Butterfly&r je oranžový motýl. Létá v lesích a květinových lesích.",
            "Chyť ho síťkou a dej do sklenice. Plnou sklenici vezmeš do inventáře takto: Shift + pravé tlačítko prázdnou rukou (&eMonarch Jar&r).",
            "&aTip:&r Druhů motýlů je přes 20 a každý žije jinde – některé i v Netheru a v Endu."]),
        Q("tag", "Ozdobná visačka", dep=["l_intro"], items=[("luminoustag:decorative_tag", 1)], xp=10, d=[
            "Visačka (&eDecorative Tag&r) z &bLuminous Tag&r. Vyrobíš ji ze železného ingotu, papíru a 3 červených barviv.",
            "Je to přísada do dekorací z Luminous (lucerny, ohniště, svícny…). Při výrobě se nespotřebuje, jen se opotřebuje. Vydrží 3 výroby."]),
        Q("bestiary", "Bestiář", dep=["l_intro"], items=[("luminous_beasts:ultimate_bestiary", 1)], xp=30, shape="hexagon", size=1.5, s=A, d=[
            "Teď začíná lov bestií. Potřebuješ železnou nebo lepší zbroj, štít, jídlo a lektvary.",
            "Bestiář (&eUltimate Bestiary&r) vyrobíš z knihy a 4 diamantů. Ke každé bestii píše, kolik má životů, kde žije, co umí a co z ní padá.",
            "Z bestie padá buď trofej, nebo gramofonová deska. Někdy i její vzácný předmět.",
            "&aTip:&r Když místo trofeje padne deska, musíš bestii porazit znovu."]),
        Q("beast_pit", "Jáma bestií", dep=["bestiary"], items=[("luminous_beasts:beast_pit_off", 1)], xp=40, d=[
            "Jáma bestií (&eBeast Pit&r) přivolá bestii. Vyrobíš ji ze 4 &eBřidlic&r, &eStřelného prachu&r a &eTáboráku s ohněm duší&r.",
            "Polož ji do biomu, kde bestie žije, a zapal ji &eKřesadlem&r. Jáma pak láká bestii toho biomu.",
            "&cPotřebuješ kolem volné místo.&r Nejlíp funguje na otevřeném prostranství."]),
        Q("ent", "Tree Ent", dep=["bestiary"], items=[("luminous_beasts:tree_ent_trophy", 1)], xp=80, d=[
            "&eTree Ent&r je živý strom. Objevuje se v noci v lesích.",
            "Prolézá listím. Může z něj padnout &eTree Ent Root&r. Když ho držíš v druhé ruce, občas zpomalí nepřítele, kterého zasáhneš."]),
        Q("hermit", "Hermit King", dep=["beast_pit"], items=[("luminous_beasts:hermit_king_trophy", 1)], xp=80, d=[
            "&eHermit King&r je obří krab s ulitou. Sám se v tomto packu neobjevuje, musíš ho přivolat.",
            "Postav &eJámu bestií&r v biomu &eBeach&r (obyčejná pláž) a zapal ji. Když má krab málo životů, schová se do ulity a léčí se.",
            "Může z něj padnout &eShellmet&r – helma, která tě zrychlí na písku."]),
        Q("mummy", "Mummy", dep=["bestiary"], items=[("luminous_beasts:mummy_trophy", 1)], xp=80, d=[
            "&eMummy&r se objevuje v noci v poušti a v pustině.",
            "&cMá kouzelný amulet, kterým mění druh útoků.&r Může z ní padnout &eMummy Wraps&r. S nimi na hlavě tě nic neotráví a nemáš hlad."]),
        Q("yeti", "Yeti", dep=["bestiary"], items=[("luminous_beasts:yeti_trophy", 1)], xp=80, d=[
            "&eYeti&r se objevuje v noci v zasněžených biomech.",
            "&cDýchá mráz.&r Může z něj padnout &eYeti Horn&r. S ním se v chladných biomech rychleji léčíš."]),
        Q("gator", "Vile Gator", dep=["bestiary"], items=[("luminous_beasts:vile_gator_trophy", 1)], xp=80, d=[
            "Obří aligátor &eVile Gator&r žije v bažinách a v mangrovech. Objevuje se v noci.",
            "&cKouše jedem a vyhazuje tě do vzduchu.&r Jeho trofej se jmenuje &eToxic Gator Trophy&r."]),
        Q("stalker", "Bone Stalker", dep=["bestiary"], items=[("luminous_beasts:bone_stalker_trophy", 1)], xp=80, d=[
            "&eBone Stalker&r žije v biomu &eDark Forest&r.",
            "&cUmí se zneviditelnit a oslepit tě.&r Může z něj padnout &eBone Rattle&r: když zemřeš, přivolá ti spojence."]),
        Q("witchdoctor", "Witch Doctor", dep=["bestiary"], items=[("luminous_beasts:witch_doctor_trophy", 1)], xp=80, d=[
            "&eWitch Doctor&r se objevuje v noci v džungli.",
            "&cDvakrát se zneviditelní a nechá za sebou příšery.&r Může z něj padnout &eJungle Pendant&r."]),
        Q("viper", "Sea Viper", dep=["bestiary"], items=[("luminous_beasts:sea_viper_trophy", 1)], xp=100, d=[
            "&eSea Viper&r se líhne z vajíčka na dně chladných a ledových oceánů.",
            "Když vajíčko rozbiješ (bez &eSilk Touch&r), had se vylíhne. &cPod vodou tebou hází.&r Vezmi si lektvar dýchání pod vodou."]),
        Q("scarecrow", "The Scarecrow", dep=["bestiary"], items=[("luminous_beasts:scarecrow_trophy", 1)], xp=80, d=[
            "&eThe Scarecrow&r vypadá jako obyčejný strašák, dokud se nepohne. Objevuje se v noci na nížinách, jen za úplňku.",
            "Přivolává si pomocníky. Snazší je přivolat ho &eJámou bestií&r na nížině. Trofej z něj padá vždy."]),
        Q("headsman", "Horseless Headsman", dep=["bestiary"], items=[("luminous_beasts:horseless_headsman_trophy", 1)], xp=120, d=[
            "&eHorseless Headsman&r je strašidelný rytíř bez hlavy. Objevuje se v noci v tajze, jen za úplňku.",
            "Přivolává dýňové pomocníky. Může z něj padnout &ePumpkin Helmet&r – za úplňku ti dává sílu."]),
        Q("moth", "Luminous Moth", dep=["bestiary"], items=[("luminous_beasts:luminous_moth_trophy", 1)], xp=80, d=[
            "Obří můra &eLuminous Moth&r se líhne z velkého kokonu. Kokony visí na smrkovém jehličí v tajze.",
            "Rozbij kokon (bez &eSilk Touch&r) a můra se vylíhne.",
            "&aTip:&r Kokon v biomu &eDark Forest&r skrývá vzácnou bílou můru &eAlbino Moth&r."]),
        Q("phoenix", "Phoenix", dep=["bestiary"], items=[("luminous_beasts:phoenix_trophy", 1)], xp=120, shape="hexagon", size=1.5, s=X, d=[
            "Nejtěžší bestie Overworldu. Jdi na ni s nejlepší výbavou a ohnivzdornými lektvary.",
            "Hnízdo &ePhoenixe&r s vajíčkem je v pustině. Rozbij vajíčko bez &eSilk Touch&r a Phoenix se vylíhne.",
            "&cKdyž ho porazíš, znovu se narodí jako mládě (&eBaby Phoenix&r).&r Teprve z mláděte padá trofej (nebo deska) a někdy &ePhoenix Feather&r. S pírkem si po smrti necháš věci."]),
        Q("lnether", "Luminous Nether", dep=["bestiary"], tasks=[dim("minecraft:the_nether")], icon="luminous_nether:ghost_lantern", xp=20, d=[
            "&bLuminous Nether&r přidává do Netheru biomy &eAsh Forest&r s duchy a &eFungal Plains&r s kultem piglinů a nové bestie.",
            "Další questy v této větvi se plní v Netheru. Vždy si tam vezmi ohnivzdorné lektvary."]),
        Q("ash_forest", "Ash Forest", dep=["lnether"], tasks=[adv("luminous_nether:ash_forest_advancement")], icon="luminous_nether:ghostly_essence", xp=30, d=[
            "Navštiv biom &eAsh Forest&r v Netheru. Žijí tu duchové.",
            "Z duchů padá &eGhostly Essence&r. Je potřeba na lucerny duchů a další věci z Luminous Nether."]),
        Q("fungal", "Fungal Plains", dep=["lnether"], tasks=[adv("luminous_nether:fungal_plains_advancement")], icon="minecraft:crimson_fungus", xp=30, d=[
            "Navštiv biom &eFungal Plains&r. Žije tu kult piglinů a houbové bytosti.",
            "Z vůdce kultu (&ePiglin Cultist Leader&r) může padnout jejich prapor (&eCultist Flag&r)."]),
        Q("executioner", "Piglin Executioner", dep=["lnether"], items=[("luminous_beasts:executioner_trophy", 1)], xp=120, d=[
            "&ePiglin Executioner&r žije v biomu &eNether Wastes&r.",
            "&cKdyž prohrává, volá si na pomoc pigliny.&r Může z něj padnout &eExecutioner Cowl&r."]),
        Q("furnace", "The Furnace", dep=["lnether"], items=[("luminous_beasts:furnace_trophy", 1)], xp=120, d=[
            "&eThe Furnace&r je chodící pec plná ohně. Žije v biomu &eNether Wastes&r a přivolává ohnivé pomocníky &eEmber&r.",
            "&cBez ohnivzdorného lektvaru nechoď.&r Může z ní padnout &eMolten Coal&r."]),
        Q("soulfurnace", "The Soul Furnace", dep=["furnace"], items=[("luminous_beasts:soul_furnace_trophy", 1)], xp=150, d=[
            "&eThe Soul Furnace&r je silnější verze The Furnace, hoří ohněm duší. Žije v biomu &eSoul Sand Valley&r.",
            "Je vzácná, ale trofej z ní padá vždy."]),
        Q("mushlin", "Crimson Mushlin King", dep=["lnether"], items=[("luminous_beasts:crimson_mushlin_king_trophy", 1)], xp=120, d=[
            "&eCrimson Mushlin King&r je obří houba, v Bestiáři zvaná &eCrimson Spitter&r. Někdy se objeví v biomu &eCrimson Forest&r spolu s piglinem.",
            "&cPlive jedovaté oblaky.&r Jeho trofej se jmenuje &eCrimson Spitter Trophy&r."]),
        Q("gilded", "Kost duší", dep=["lnether"], items=[("luminous_nether:soul_bone", 1)], xp=60, d=[
            "&eRevenant&r je kostlivec z &bLuminous Nether&r. Žije v biomu &eSoul Sand Valley&r.",
            "Když ho porazíš, může z něj padnout kost duší (&eSoul Bone&r). Očarování &eKořist&r přidá víc kostí.",
            "",
            "&aTip:&r Z jedné kosti duší vyrobíš 6 kostních mouček. Ze 4 kostí složíš blok (&eSoul Bone Block&r)."]),
        Q("scrap", "Legendární šrot", dep=["ent", "hermit", "mummy", "yeti"], items=[("luminous_beasts:legendary_scrap", 1)], xp=80, d=[
            "Šrot (&eLegendary Scrap&r) dostaneš rozebráním trofeje nebo desky (2 kusy) nebo vzácného předmětu bestie (4 kusy) ve výrobní mřížce.",
            "Zatím k ničemu není – autor modu ho chystá na budoucí vylepšení. &cTrofej si před rozebráním nech na splnění questu.&r"]),
    ],
)

# Pořadí kapitol této oblasti v knize questů
CHAPTERS = [EXPLORE, BIOMES, STRUCTURES, CREATURES, PETS, OCEAN, LUMINOUS]

# Předměty bez receptu a loot table, které ale prokazatelně jdou získat
NO_RECIPE = {
    "naturalist:butterfly": "Naturalist: chycení motýla sítí Capture Net (Catchable.catchAnimal)",
    "benssharks:shark_tooth": "Ben's Sharks: tygří žralok ho upustí po nakrmení Fish Bucketem (TigerSharkRightClickedOnEntityProcedure)",
    "upgrade_aquatic:pike_bucket": "Upgrade Aquatic: kbelík vody na živou štiku (Blueprint BucketableWaterAnimal)",
    "luminous_butterflies:butterfly_encyclopedia": "Obchod: potulný obchodník 15 smaragdů + kniha, knihovník úroveň 3 za 8 diamantů + kniha (LuminousButterfliesModTrades)",
}

# Přeložená vlastní jména (biomy, stavby, bossové, mobové z modů) -> správný anglický název
PROPER_NAMES_CZ = {
    r"opuštěn\w* d[ůo]l": "Mineshaft",
    r"sklep\w* s líhn": "Monster Room",
    r"pevnost\w* nemrtv": "Fortress of the Undead",
    r"pavouč\w* jeskyn": "Spider Cave",
    r"pouštní\w* chrám": "Desert Temple",
    r"chrám\w* v džungl": "Jungle Temple",
    r"komnat\w* klání": "Trial Chambers",
    r"podmořsk\w* monument": "Ocean Monument",
    r"(?<!oko )prastráž\w*": "Elder Guardian",
    r"prastar\w* měst": "Ancient City",
    r"temn\w* hlubin": "Deep Dark",
    r"vartýř\w*": "Warden",
    r"sakurov\w* háj": "Sakura Grove",
    r"měsíčn\w* háj": "Moonlight Grove",
    r"smaragdov\w* vrchol": "Emerald Peaks",
    r"ledov\w* propast": "Glacial Chasm",
    r"podzemn\w* džungl": "Underground Jungle",
    r"mraziv\w* oh(eň|n)": "Frostfire Caves",
    r"plášťov\w* jeskyn": "Mantle Caves",
    r"ledov\w* hrot": "Ice Spikes",
    r"zamrzl\w* vrchol": "Frozen Peaks",
    r"temn\w* hvozd": "Dark Forest",
    r"popelov\w* les": "Ash Forest",
    r"houbov\w* plán": "Fungal Plains",
    r"hlídk\w* nájezdník": "Pillager Outpost",
    r"opevněn\w* vesnic": "Fortified Village",
    r"loveck\w* chat": "Hunter's Cabin",
    r"strašideln\w* sídl": "Haunted Manor",
    r"věž\w* mágů": "Mage Tower",
    r"ztracen\w* nádraž": "Lost Train Station",
    r"pevnost\w* nájezdník": "Pillager Fortress",
    r"vzducholo\w* nájezdník": "Pillager Steampunk Airship",
    r"věž\w* z ochrum": "Tower of Ochrum",
    r"endov\w* měst": "End City",
    r"jeskynní\w* stonožk": "Cave Centipede",
    r"mraziv\w* šelm": "Froststalker",
    r"velk\w* mlátičk": "Great Thrasher",
    r"(?<!zub )(?<!zuby )(?<!zubů )mlátičk\w*": "Thrasher",
    r"stromov\w* ent": "Tree Ent",
    r"krabí\w* král": "Hermit King",
    r"\byetti\b": "Yeti",
    r"\bzl(ý|ého|ým|ému)\w* aligátor": "Vile Gator",
    r"kostěn\w* lov(ec|c)": "Bone Stalker",
    r"bezhlav\w* jezd": "Horseless Headsman",
    r"zářící\w* můr": "Luminous Moth",
    r"\bživ\w* pec": "The Furnace",
    r"pec\w* duší": "The Soul Furnace",
    r"karmínov\w* plivač": "Crimson Spitter",
    r"houbov\w* král": "Mushlin King",
}
