from engine import *

# Oblast c_create_addons: rozcestník „Create: doplňky“ (původní kapitola create_addons)
# + tematické kapitoly skupiny create. Milníky: hexagon 1.5, úroveň v podnázvu.

M = dict(shape="hexagon", size=1.5)


# ======================================================================
# Kapitola ELEKTŘINA
# ======================================================================
# Kapitola Elektřina: Create Crafts & Additions (createaddition) + Create: New Age (create_new_age)
# Úrovně: Začátečník -> Pokročilý -> Expert (milníky hexagon, úroveň v podnázvu)
CADD_POWER = dict(
    key="cadd_power", group="create", title="Elektřina",
    subtitle="Proud z otáčení, motory, energizér a jaderný reaktor",
    icon="createaddition:alternator",
    quests=[
        Q("intro", "Elektřina v Create", icon="createaddition:copper_spool", tasks=[auto()], dep=["create_addons:start"], xp=10, d=[
            "Elektřina (⚡, v jiných modech FE) je energie, která běží po drátech. Dostane se daleko a pohání i stroje z jiných modů, třeba Mekanism nebo AE2.",
            "",
            "Create jinak pracuje s otáčením. Rychlost otáčení je RPM. Síla otáčení je SU – každý stroj nějaké SU spotřebuje a zdroj jich má jen omezeně.",
            "{@pagebreak}",
            "Elektřinu přidávají dva mody: &bCreate Crafts & Additions&r (alternátor, elektromotor, teslova cívka, akumulátor) a &bCreate: New Age&r (generátor s magnety, energizér, teplo a jaderný reaktor).",
            "",
            "Každá linka má tři úrovně: &eZačátečník&r, &ePokročilý&r a &eExpert&r. Milníky (šestiúhelníky) ukazují, kdy přecházíš na další úroveň.",
            "",
            "&aKaždý mod má své vlastní dráty a konektory. Kolik energie stroj má, ti ukážou inženýrské brýle.&r",
        ]),

        # ---------- Create Crafts & Additions: energie ----------
        Q("rods", "Kovové tyče", dep=["intro", "create_addons:wire"], items=[("createaddition:iron_rod", 4)], xp=15, d=[
            "Tyče potřebuješ do skoro všech elektrických strojů.",
            "",
            "Hoď ingot na vrch válcovací stolice (&eRolling Mill&r) a stolice z něj udělá 2 tyče. Z plátu udělá 2 dráty. Hotové věci vytáhneš pravým tlačítkem.",
            "",
            "&aStolici můžeš zautomatizovat: pás a dva trychtýře (&eFunnel&r) – jedním věci dovnitř, druhým ven.&r",
        ]),
        Q("spool", "Měděná cívka", dep=["rods"], items=[("createaddition:copper_spool", 4)], xp=20, d=[
            "Na cívce je navinutý drát. Cívkou spojuješ konektory a potřebuješ ji i do receptů.",
            "",
            "Ze 2 železných plátů a 1 železné tyče vyrobíš 24 prázdných cívek (&eEmpty Spool&r). Prázdnou cívku obklop 4 měděnými dráty a máš měděnou cívku (&eCopper Spool&r).",
            "",
            "&aAlternátor potřebuje 4 měděné cívky, elektromotor 3.&r",
        ]),
        Q("capacitor", "Kondenzátor", dep=["rods", "create:zinc"], items=[("createaddition:capacitor", 2)], xp=20, d=[
            "Kondenzátor (&eCapacitor&r) je elektrická součástka. Tady ho potřebuješ jako díl do elektromotoru, teslovy cívky, akumulátoru a elektrické pumpy.",
            "",
            "Vyrobíš ho z měděného plátu, zinkového plátu (&eZinc Sheet&r) a redstonové pochodně. Zinkový plát vylisuješ mechanickým lisem ze zinkového ingotu.",
        ]),
        Q("connectors", "Konektory a vedení", s="Začátečník", dep=["spool", "capacitor", "create_addons:alternator"], items=[("createaddition:connector", 4)], xp=35, shape="hexagon", size=1.5, d=[
            "Tvůj první elektrický obvod: alternátor vyrobí elektřinu, dráty ji odvedou a elektromotor z ní udělá otáčení třeba na druhém konci základny.",
            "",
            "Konektor (&eSmall Connector&r) vyrobíš z měděné tyče, andezitové slitiny a slizové koule (3 kusy). Polož ho přímo na stroj. Měděnou cívkou klikni pravým tlačítkem na první a pak na druhý konektor. Spojení spotřebuje jednu cívku a vrátí ti prázdnou.",
            "{@pagebreak}",
            "Drát může být dlouhý až 16 bloků, konektor unese 4 dráty. Montážním klíčem přepínáš režim konektoru:",
            "&ePull&r bere energii ze stroje (dej ho na alternátor). &ePush&r energii do stroje posílá (dej ho na motor). &eNone&r jen předává energii dál – hodí se jako sloup vedení.",
            "",
            "&aDrát odstraníš tak, že prázdnou cívkou klikneš na oba konce. Drát se ti vrátí jako plná cívka.&r",
        ]),
        Q("electrum", "Elektrum nabíjením", s="Pokročilý", dep=["connectors", "create_addons:tesla"], items=[("createaddition:electrum_ingot", 4)], xp=45, shape="hexagon", size=1.5, d=[
            "Teď už elektřinu jen nepřenášíš – začínáš s ní vyrábět. Teslova cívka nabíjí suroviny a mění je na nové.",
            "",
            "Pod teslovu cívku dej odkládací desku (&eDepot&r) a polož na ni zlatý ingot. Cívka ho nabije a vznikne elektrum (&eElectrum Ingot&r). Stejně se nabíjí zlatá tyč, drát, plát nebo blok.",
            "{@pagebreak}",
            "Elektrum potřebuješ na elektrový drát do akumulátoru a na silné vedení.",
            "",
            "&aNabíjecí recepty najdeš v JEI pod „Charging“. Z obyčejné knihy cívka udělá i očarovanou knihu (&eChanneling&r) – stojí to ale 1 000 000 ⚡.&r",
        ]),
        Q("pump", "Elektrická pumpa", dep=["connectors", "create:fluids"], items=[("createaddition:electric_pump", 1)], xp=30, d=[
            "Elektrická pumpa (&eElectric Pump&r) žene kapaliny potrubím jako mechanické čerpadlo. Nepotřebuje ale otáčení – stačí jí elektřina z konektoru.",
            "",
            "Vyrobíš ji v mechanickém výrobníku z mechanického čerpadla, kondenzátoru, měděných cívek a sušené chaluhy.",
            "",
            "&aŠipka ukazuje, kterým směrem teče kapalina. Montážním klíčem směr otočíš.&r",
        ]),
        Q("pei", "Energie pro stroje v pohybu", dep=["electrum", "create_addons:accumulator"], items=[("createaddition:portable_energy_interface", 2)], xp=30, optional=True, d=[
            "Přenosné energetické rozhraní (&ePortable Energy Interface&r) dobíjí akumulátory na pohyblivé konstrukci (kontrapci), třeba na vlaku.",
            "",
            "Jedno rozhraní dej na konstrukci, druhé na pevné místo. Mezi nimi musí být mezera 1 nebo 2 bloky. Když konstrukce projede kolem, rozhraní se spojí a energie přeteče podle nastavení konektoru.",
            "",
            "&aRedstonový signál na pevném rozhraní spojení zakáže.&r",
        ]),
        Q("base_power", "Napájení celé základny", s="Expert", dep=["electrum", "create_addons:accumulator"], items=[("createaddition:large_connector", 4), ("createaddition:electrum_spool", 2)], xp=60, shape="hexagon", size=1.5, d=[
            "Teď už malé konektory nestačí. Přenesou jen 1 000 ⚡ za tick. Velký konektor (&eLarge Connector&r) přenese 5 000 ⚡, drát k němu smí být dlouhý 32 bloků a unese 6 drátů.",
            "",
            "Velký konektor vyrobíš ze zlaté nebo elektrové tyče, 2 andezitových slitin a slizové koule (2 kusy). Spojuješ je elektrovou (&eElectrum Spool&r) nebo zlatou cívkou – měděná na ně nestačí.",
            "{@pagebreak}",
            "Efektivní napájení základny: víc alternátorů na rychlém a silném zdroji otáčení (třeba velký parní stroj) → velké konektory → velký akumulátor jako zásobník → silné vedení ke strojům.",
            "",
            "&aAkumulátor může mít až 3 × 3 bloky na šířku a 5 bloků na výšku. Každý blok pojme 2 000 000 ⚡. Elektřinu tak máš i ve chvíli, kdy zdroj stojí.&r",
        ]),

        # ---------- Create Crafts & Additions: paliva ----------
        Q("straw", "Ohňohořák na kapaliny", s="Začátečník", dep=["intro", "create_addons:wire", "create:burner"], items=[("createaddition:straw", 1)], xp=20, shape="hexagon", size=1.5, d=[
            "Se slámkou (&eStraw&r) pije ohňohořák (&eBlaze Burner&r) tekutá paliva. Nemusíš ho pak pořád krmit uhlím.",
            "",
            "Slámku vyválcuješ ve válcovací stolici z bambusu nebo papíru. Klikni s ní pravým tlačítkem na ohňohořák. Palivo pak naleješ kbelíkem nebo přivedeš potrubím.",
            "",
            "&aHoří třeba láva, rostlinný olej, nafta nebo biopalivo. Seznam paliv je v JEI pod „Liquid Burning“.&r",
        ]),
        Q("biomass", "Biomasa", dep=["straw", "create:mixer"], items=[("createaddition:biomass", 4)], xp=25, d=[
            "Tekuté palivo si můžeš vypěstovat. Začíná se biomasou (&eBiomass&r).",
            "",
            "Nejdřív lisuj semínka: mechanický lis nad tyglíkem (&eBasin&r) z jednoho semínka vymačká 100 mB oleje. Vznikne rostlinný olej (&ePlant Oil&r).",
            "",
            "Pak v zahřáté míchačce smíchej 100 mB oleje s plodinami, listím, sazenicemi nebo květinami.",
            "",
            "&aZ biomasy uděláš lisem nad tyglíkem i pelety (&eBiomass Pellet&r). Jedna peleta hoří v peci jako 4 uhlí.&r",
        ]),
        Q("biofuel", "Biopalivo", s="Pokročilý", dep=["biomass", "create:millstone"], items=[("createaddition:bioethanol_bucket", 1)], xp=45, shape="hexagon", size=1.5, d=[
            "Biopalivo (&eBiofuel&r) je jediné tekuté palivo, které ohňohořák se slámkou rozpálí doběla – stejně jako ohňodort (&eBlaze Cake&r). Jeden kbelík vydrží 20 minut.",
            "",
            "V míchačce smíchej 2 biomasy, cukr a uškvařenou mouku (&eCinder Flour&r). Vznikne 125 mB biopaliva. Do kbelíku ho naplníš dávkovačem (&eSpout&r).",
            "",
            "&aFarma, lis, míchačky a potrubí k ohňohořákům = palivo, o které se nemusíš starat.&r",
        ]),

        # ---------- Create: New Age: elektřina ----------
        Q("magnetite", "Magnetit", dep=["intro"], items=[("create_new_age:magnetite_block", 8)], xp=20, d=[
            "Magnety jsou srdce generátoru z &bCreate: New Age&r. Nejslabší magnet je magnetitový blok (&eMagnetite Block&r).",
            "",
            "Najdeš ho v podzemí v &eOverworldu&r, ve výšce zhruba od -20 do 60. Když ho vytěžíš, padne ti celý blok.",
            "",
            "&aMagnetit potřebuješ i do základního motoru.&r",
        ]),
        Q("generator", "Postav generátor", s="Začátečník", dep=["magnetite", "create_addons:newage"], items=[("create_new_age:copper_wire", 8), ("create_new_age:electrical_connector", 4)], xp=40, shape="hexagon", size=1.5, d=[
            "Generátor mění otáčení na elektřinu. Generátorové cívky (&eGenerator Coil&r) dej do řady jako hřídel a roztoč je. Kolem cívek postav magnety a na konec řady dej uhlíkové kartáče (&eCarbon Brushes&r).",
            "",
            "&aPřesné rozestavění magnetů ukazuje ponder: podrž klávesu W nad cívkou.&r",
            "{@pagebreak}",
            "Kartáče sbírají elektřinu z cívek a posílají ji do sousedních bloků. Na kartáče dej elektrický konektor (&eElectrical Connector&r) a druhý konektor dej na stroj.",
            "",
            "Měděný drát z New Age (&eCopper Wire&r) nařežeš mechanickou pilou z měděného plátu. Klikni drátem na oba konektory. Každé spojení spotřebuje 1 drát a smí být dlouhé až 16 bloků.",
            "",
            "&cCívky nic dalšího neroztočí, jen spotřebovávají SU. Dej jim silný zdroj otáčení.&r",
        ]),
        Q("basic_motor", "Základní motor", dep=["generator"], items=[("create_new_age:basic_motor", 1)], xp=25, d=[
            "Základní motor (&eBasic Motor&r) mění elektřinu zpět na otáčení.",
            "",
            "Rychlost nastavíš montážním klíčem. Síla (SU) zůstává stejná. Redstonovým signálem motor vypneš. Kliknutím pravým tlačítkem tohle chování obrátíš.",
            "",
            "&aElektřinu přivedeš konektorem položeným přímo na motor.&r",
        ]),
        Q("overcharged", "Nabité kovy", s="Pokročilý", dep=["generator", "create_addons:energiser"], items=[("create_new_age:overcharged_iron", 4), ("create_new_age:overcharged_gold", 2), ("create_new_age:overcharged_diamond", 1)], xp=45, shape="hexagon", size=1.5, d=[
            "Teď už jen nevyrábíš proud – energizér z něj dělá nové suroviny. Nabité kovy potřebuješ na všechny lepší stroje z New Age.",
            "",
            "Energizér nabíjí předměty na odkládací desce nebo na pásu pod sebou. Potřebuje elektřinu a otáčení zároveň.",
            "{@pagebreak}",
            "Železný ingot spotřebuje 1 000 ⚡, zlatý 2 000 ⚡ a diamant 10 000 ⚡. Recepty najdeš v JEI pod „Energizing“.",
            "",
            "&aČím rychleji se energizér točí, tím rychleji nabíjí. Dej ho nad pás a nabíjení poběží samo.&r",
        ]),
        Q("adv_energiser", "Pokročilý energizér", dep=["overcharged"], items=[("create_new_age:advanced_energiser", 1)], xp=30, d=[
            "Základní energizér je na velkou výrobu pomalý. Pokročilý energizér (&eAdvanced Energiser&r) nabíjí 4× rychleji.",
            "",
            "Vyrobíš ho ze základního energizéru, 2 nabitých zlatých ingotů (&eOvercharged Gold&r) a 2 hromosvodů.",
            "",
            "&aZesílený energizér (&eReinforced Energiser&r) s nabitými diamanty je zase 4× rychlejší než pokročilý.&r",
        ]),
        Q("magnets", "Silnější magnety", dep=["overcharged"], items=[("create_new_age:redstone_magnet", 4), ("create_new_age:layered_magnet", 4)], xp=35, d=[
            "Magnetit má sílu jen 1, takže generátor mění na elektřinu malou část otáčení. Silnější magnety zvýší účinnost. Cívka pak ale bere víc SU.",
            "",
            "Síla magnetů: magnetit 1, redstonový magnet (&eRedstone Magnet&r) 2, vrstvený magnet (&eLayered Magnet&r) 4.",
            "",
            "&aRedstonový magnet je z redstonového bloku a železných nugetů. Vrstvený je z nabitého železa a nabitého zlata.&r",
        ]),
        Q("circuits", "Obvody", dep=["overcharged"], items=[("create_new_age:copper_circuit", 2)], xp=30, d=[
            "Měděný obvod (&eCopper Circuit&r) potřebuješ na rozšíření motorů.",
            "",
            "Nejdřív vylisuj prázdné obvody (&eBlank Circuit&r): mechanický lis nad tyglíkem slisuje kámen, redstone, železný ingot a křemen na 4 obvody. Ohňohořák pod tyglíkem musí být rozpálený doběla.",
            "",
            "Pak pokladačem (&eDeployer&r) přidej na prázdný obvod měděný drát z New Age.",
        ]),
        Q("adv_motor", "Pokročilý motor", dep=["basic_motor", "overcharged"], items=[("create_new_age:advanced_motor", 1)], xp=35, d=[
            "Základní motor má na velké stroje málo síly. Pokročilý motor (&eAdvanced Motor&r) dá 4× víc síly (SU) a může se točit 2× rychleji.",
            "",
            "Vyrobíš ho z mosazného pouzdra, nabitého železa, hřídele a zlatých nugetů.",
            "",
            "&aNejsilnější je zesílený motor (&eReinforced Motor&r) z nabitých diamantů.&r",
        ]),
        Q("motor_ext", "Rozšíření motoru", dep=["adv_motor", "circuits"], items=[("create_new_age:basic_motor_extension", 1)], xp=30, optional=True, d=[
            "Rozšíření (&eBasic Motor Extension&r) dej za motor. Zvýší jeho sílu (SU) až na dvojnásobek.",
            "",
            "Násobek nastavíš na rozšíření. &cMotor pak spotřebuje úměrně víc elektřiny.&r",
        ]),
        Q("big_generator", "Velký generátor", s="Expert", dep=["magnets", "adv_energiser"], items=[("create_new_age:fluxuated_magnetite", 8), ("create_new_age:overcharged_golden_wire", 8)], xp=80, shape="hexagon", size=1.5, d=[
            "Teď už jedna cívka a slabé magnety nestačí. Velký generátor má dlouhou řadu cívek – jedny kartáče sbírají elektřinu až z 8 cívek.",
            "",
            "Kolem cívek dej nejsilnější magnety: &eFluxuated Magnetite&r má sílu 8, &eNetherite Magnet&r dokonce 24. Fluxovaný magnetit vyrobíš z magnetitu, nabitého zlata a nabitého diamantu.",
            "{@pagebreak}",
            "Silné magnety berou hodně SU. Generátor proto pohání velký zdroj otáčení, třeba velký parní stroj.",
            "",
            "Měděný drát velký proud neunese. Každý lepší drát přenese 2× víc: měděný, nabitý železný, nabitý zlatý (&eOvercharged Golden Wire&r) a nejlepší nabitý diamantový.",
            "",
            "&aZlatý drát nařežeš pilou z nabitého zlatého plátu.&r",
        ]),

        # ---------- Create: New Age: teplo ----------
        Q("heat_pipes", "Tepelné trubky", dep=["intro", "create_addons:newage"], items=[("create_new_age:heat_pipe", 8)], xp=20, d=[
            "New Age umí pracovat i s teplem. Tepelné trubky (&eHeat Pipe&r) rozvádějí teplo od zdroje ke strojům.",
            "",
            "Vyrobíš je z terakoty, měděného plátu a zinkových nugetů. Kolik tepla trubka má, ukážou inženýrské brýle.",
            "",
            "&cKdyž se blok přehřeje, změní se na lávu. Teplo musí mít kam odtékat.&r",
        ]),
        Q("solar", "Teplo ze slunce", dep=["heat_pipes"], items=[("create_new_age:basic_solar_heating_plate", 2), ("create_new_age:stirling_engine", 1)], xp=30, d=[
            "Solární ohřívací deska (&eBasic Solar Heating Plate&r) přes den vyrábí teplo zadarmo.",
            "",
            "Stirlingův motor (&eStirling Engine&r) dej nad zdroj tepla, třeba nad trubku. Začne se pomalu točit. Čím víc tepla dostane, tím rychleji se točí.",
        ]),
        Q("heater", "Ohřívač kotle", s="Pokročilý", dep=["solar", "overcharged", "create:steam"], items=[("create_new_age:heater", 1)], xp=40, shape="hexagon", size=1.5, d=[
            "Stirlingův motor je slabý. Víc z tepla dostaneš, když jím ohřeješ parní kotel. Ohřívač (&eHeater&r) funguje jako ohňohořák pod kotlem, jen místo paliva bere teplo z trubek.",
            "",
            "Čím víc tepla do něj přivedeš, tím víc tepla dává kotli. Vyrobíš ho z prázdného ohňohořáku, nabitého železa, tepelných trubek a železných nugetů.",
            "",
            "&aTeplo z jaderného reaktoru využiješ právě takhle: tepelné trubky dovedou teplo k ohřívačům pod parními kotli.&r",
        ]),

        # ---------- Create: New Age: jaderný reaktor ----------
        Q("thorium", "Thorium", dep=["intro", "create_addons:newage"], items=[("create_new_age:thorium", 8)], xp=25, d=[
            "Thorium (&eThorium&r) je surovina na jaderné palivo.",
            "",
            "Thoriová ruda je v &eOverworldu&r ve výšce zhruba od 20 do 120. Padá z ní thorium.",
            "",
            "&aThorium umíš rozmnožit: v míchačce smíchej thorium, kámen, blok jílu a 1 000 mB vody. Vzniknou 2 kusy thoria.&r",
        ]),
        Q("rad_thorium", "Radioaktivní thorium", dep=["thorium", "create:crushing"], items=[("create_new_age:radioactive_thorium", 2)], xp=30, d=[
            "Radioaktivní thorium (&eRadioactive Thorium&r) získáš drcením thoria v drtících kolech.",
            "",
            "Vypadne jen v 10 % případů. Navíc často dostaneš železné nugety a zkušenosti. Připrav si víc thoria.",
        ]),
        Q("fuel", "Jaderné palivo", dep=["rad_thorium", "create:precision"], items=[("create_new_age:nuclear_fuel", 2)], xp=40, d=[
            "Jaderné palivo (&eNuclear Fuel&r) se vyrábí sekvenční montáží z radioaktivního thoria.",
            "",
            "Kroky: lis, pokladač přidá železný plát, lis. Postup najdeš v JEI.",
            "",
            "&aNa 2 reaktorové tyče potřebuješ 2 jaderná paliva, 4 reaktorová skla (&eReactor Glass&r), 4 reaktorové pláště a 6 zlatých plátů. Sestavíš je v mechanickém výrobníku.&r",
        ]),
        Q("hazmat", "Ochrana před zářením", dep=["rad_thorium"], items=[("minecraft:leather_helmet", 1), ("minecraft:leather_chestplate", 1), ("minecraft:leather_leggings", 1), ("minecraft:leather_boots", 1)], xp=20, d=[
            "&cBěžící reaktor vyzařuje smrtelné záření.&r Chrání tě celá kožená zbroj – všechny 4 díly najednou. Místo kožené čepice můžeš mít inženýrské brýle.",
            "",
            "Záření neprojde reaktorovými bloky (plášť, sklo, tyče, vstup paliva, výdech tepla).",
            "",
            "&aNejbezpečnější je reaktor celý obestavět reaktorovým pláštěm nebo sklem.&r",
        ]),
        Q("reactor_build", "Spusť reaktor", s="Expert", dep=["fuel", "heater", "hazmat", "create_addons:reactor"], items=[("create_new_age:reactor_fuel_acceptor", 1), ("create_new_age:reactor_heat_vent", 1)], xp=100, shape="hexagon", size=1.5, d=[
            "Teď už slunce ani palivo v ohňohořáku nestačí. Reaktor vyrábí obrovské množství tepla pro parní kotle.",
            "",
            "Reaktorové tyče postav do řady. Na jeden konec řady dej vstup paliva (&eReactor Fuel Acceptor&r), na druhý výdech tepla (&eReactor Heat Vent&r).",
            "{@pagebreak}",
            "Do vstupu paliva vkládej jaderné palivo, třeba trychtýřem. Z výdechu veď tepelné trubky k ohřívačům pod parními kotli.",
            "",
            "&cTeplo musí mít vždy kam odtékat. Jinak se reaktor přehřeje, tyče vybuchnou a reaktor se roztaví.&r",
            "",
            "&cNerozbíjej tyč, ve které je palivo – vybuchne.&r",
            "",
            "&aPonder reaktoru (klávesa W nad tyčí) ukazuje celou stavbu.&r",
        ]),
    ],
)

# Přepsané původní questy kapitoly create_addons (úkoly beze změny)
ORIG_POWER = {
    "wire": Q("wire", "Měděný drát", dep=["start", "create:sheets"], items=[("createaddition:copper_wire", 8), ("createaddition:rolling_mill", 1)], xp=25, d=[
        "&bCreate Crafts & Additions&r přidává elektřinu. Začíná se válcovací stolicí (&eRolling Mill&r).",
        "",
        "Stolici roztoč a hoď na ni měděný plát. Udělá z něj 2 měděné dráty (&eCopper Wire&r). Z ingotů dělá tyče.",
        "",
        "&aVíc najdeš v kapitole Elektřina.&r",
    ]),
    "alternator": Q("alternator", "Z otáčení elektřina", s="Začátečník", dep=["wire", "create:crafter", "cadd_power:spool"], items=[("createaddition:alternator", 1)], xp=40, shape="hexagon", size=1.5, d=[
        "Alternátor (&eAlternator&r) mění otáčení na elektřinu (⚡). Potřebuje aspoň 32 RPM. Čím rychleji se točí, tím víc elektřiny vyrobí.",
        "",
        "Vyrobíš ho v mechanickém výrobníku ze 4 měděných cívek, železných plátů, železné tyče a andezitové slitiny.",
        "",
        "&aVíc najdeš v kapitole Elektřina.&r",
    ]),
    "motor": Q("motor", "Z elektřiny otáčení", dep=["wire", "create:crafter", "cadd_power:spool", "cadd_power:capacitor"], items=[("createaddition:electric_motor", 1)], xp=40, d=[
        "Elektromotor (&eElectric Motor&r) dělá opak alternátoru: z elektřiny vyrábí otáčení.",
        "",
        "Rychlost nastavíš kolečkem myši na zadní straně. Čím rychleji se točí, tím víc elektřiny spotřebuje. Vyrobíš ho v mechanickém výrobníku ze 3 měděných cívek, kondenzátoru, mosazných plátů, železné tyče a andezitové slitiny.",
        "",
        "&aVíc najdeš v kapitole Elektřina.&r",
    ]),
    "accumulator": Q("accumulator", "Ulož si energii", dep=["tesla", "cadd_power:electrum"], items=[("createaddition:modular_accumulator", 2)], xp=40, d=[
        "Akumulátor (&eAccumulator&r) je velká baterie. Bloky polož k sobě a spojí se do jednoho, až 3 × 3 bloky na šířku a 5 bloků na výšku. Každý blok pojme 2 000 000 ⚡.",
        "",
        "Na akumulátor dej dva konektory. Jeden nastav na vstup, druhý na výstup. Bloky nad a pod akumulátorem dostávají energii samy.",
        "",
        "&aVyrobíš ho z mosazného pouzdra, 2 kondenzátorů, měděné tyče a elektrového drátu (&eElectrum Wire&r). Víc najdeš v kapitole Elektřina.&r",
    ]),
    "tesla": Q("tesla", "Teslova cívka", dep=["alternator", "cadd_power:capacitor"], items=[("createaddition:tesla_coil", 1)], xp=40, d=[
        "Teslova cívka (&eTesla Coil&r) nabíjí předměty pod sebou: baterie, nástroje s energií i suroviny podle receptů (třeba zlato na elektrum).",
        "",
        "Vyrobíš ji v mechanickém výrobníku z měděných cívek, kondenzátorů, mosazného pouzdra, mosazných plátů, elektronky a andezitové slitiny. Energii jí přiveď konektorem.",
        "",
        "&cRedstonový signál ji přepne do útoku – pak dává elektrické rány hráčům i příšerám kolem.&r",
        "",
        "&aVíc najdeš v kapitole Elektřina.&r",
    ]),
    "newage": Q("newage", "Create: New Age", dep=["start", "create:alloy"], items=[("create_new_age:generator_coil", 1), ("create_new_age:carbon_brushes", 1)], xp=40, d=[
        "&bCreate: New Age&r je druhý mod na elektřinu. Má generátory s magnety, motory, energizér, teplo a jaderný reaktor.",
        "",
        "Generátorovou cívku (&eGenerator Coil&r) vyrobíš z 8 měděných ingotů a bloku andezitové slitiny. Uhlíkové kartáče (&eCarbon Brushes&r) z andezitové slitiny, uhlí a hřídele.",
        "",
        "&aVíc najdeš v kapitole Elektřina.&r",
    ]),
    "energiser": Q("energiser", "Energizér", dep=["newage", "create:casing"], items=[("create_new_age:basic_energiser", 1)], xp=40, d=[
        "Energizér (&eBasic Energiser&r) nabíjí kovy a diamanty elektřinou. Vyrobíš ho z andezitového pouzdra a hromosvodu.",
        "",
        "Potřebuje elektřinu i otáčení. Předmět mu polož pod něj na odkládací desku nebo na pás.",
        "",
        "&aVíc najdeš v kapitole Elektřina.&r",
    ]),
    "reactor": Q("reactor", "Jádro!", s="Expert", dep=["energiser", "create:crafter", "cadd_power:fuel"], items=[("create_new_age:reactor_casing", 8), ("create_new_age:reactor_rod", 1)], xp=80, shape="hexagon", size=1.5, d=[
        "Jaderný reaktor z New Age dává obrovské množství tepla pro parní kotle.",
        "",
        "Reaktorový plášť (&eReactor Casing&r) se vyrábí sekvenční montáží z cihel: energizér, pokladač přidá železný plát, lis. Reaktorovou tyč (&eReactor Rod&r) sestavíš v mechanickém výrobníku z pláště, skla, zlatých plátů a jaderného paliva.",
        "",
        "&cReaktor je nebezpečný. Než ho spustíš, projdi kapitolu Elektřina.&r",
    ]),
}

NO_RECIPE_POWER = {
    "createaddition:bioethanol_bucket": "Prázdný kbelík naplní biopalivem dávkovač (Spout) z Create, kapalinu vyrobí míchačka (create:mixing bioethanol).",
}


# ======================================================================
# Kapitola ROPA A PALIVO
# ======================================================================
# Kapitola: Ropa a palivo (Create: Diesel Generators)
CADD_OIL = dict(
    key="cadd_oil", group="create", title="Ropa a palivo",
    subtitle="Motory, ropná pumpa a destilace", icon="createdieselgenerators:pumpjack_head",
    quests=[
        Q("intro", "Ropa a palivo", s="Create: Diesel Generators", icon="createdieselgenerators:diesel_engine",
          tasks=[auto()], dep=["create_addons:start"], xp=10, d=[
            "&bCreate: Diesel Generators&r přidává motory na kapalné palivo, těžbu ropy a její zpracování.",
            "",
            "Pár pojmů: &eMotor&r mění palivo na rotaci. &ePalivo&r je hořlavá kapalina, kterou motor pomalu spaluje.",
            "",
            "&emB&r je jednotka kapaliny: 1 kbelík = 1 000 mB. &eSU&r je síla otáčení, kterou motor dává a stroje Create spotřebovávají. Inženýrské brýle ti ukážou, kolik jí zbývá.",
            "{@pagebreak}",
            "Cesta kapitolou:",
            "&aZačátečník&r – ruční nástroje, první motor a palivo ze semínek.",
            "&aPokročilý&r – linka, která palivo vyrábí sama, a těžba ropy.",
            "&aExpert&r – destilační věž, obří motor a celá naftová elektrárna.",
            "",
            "&aTip: K hlavním strojům má mod animovaný návod (ponder). Najeď myší na předmět a podrž W.&r"]),
        Q("pistons", "Píst motoru", dep=["intro"],
          items=[("createdieselgenerators:engine_piston", 2)], xp=15, d=[
            "Píst motoru (&eEngine Piston&r) je hlavní díl naftového motoru. Na jeden motor potřebuješ dva.",
            "",
            "Vyrobíš ho z andezitové slitiny, hřídele a zinkového nugetu. Jeden recept dá 2 písty.",
            "",
            "K motoru (&eDiesel Engine&r) dál potřebuješ blok mosazi, nádrž, křesadlo a dvě desky z leštěného černokamene. Motor vyrobíš v questu Naftový motor v kapitole Create: doplňky."]),

        # --- ruční nástroje
        Q("tools", "Kladivo a štípačky", dep=["intro"],
          items=[("createdieselgenerators:hammer", 1), ("createdieselgenerators:wire_cutters", 1)], xp=20, d=[
            "Dva ruční nástroje pro začátek, než postavíš stroje.",
            "",
            "Kladivo (&eHammer&r): vezmi ingot do druhé ruky a použij kladivo (pravé tlačítko). Ze železného, měděného, zlatého nebo mosazného ingotu tak vyklepeš plát.",
            "",
            "Štípačky (&eWire Cutters&r) se používají stejně. Z prken nastříhají 4 klacky. S modem &bCreate Crafts & Additions&r stříhají z plátů i dráty.",
            "",
            "&aTip: Všechny recepty ukáže JEI v záložkách Hammering a Wire Cutting.&r"]),

        # --- palivo z rostlin
        Q("plant_oil", "Rostlinný olej", s="Začátečník", dep=["intro", "create:mixer"], shape="hexagon", size=1.5,
          items=[("createdieselgenerators:plant_oil_bucket", 1)], xp=30, d=[
            "Rostlinný olej (&ePlant Oil&r) je nejjednodušší palivo. Vyrobíš ho z obyčejných semínek.",
            "",
            "Polož tyglík (&eBasin&r) pod mechanický lis (&eMechanical Press&r) a vhoď do něj semínka. Lis z každého semínka vymačká 100 mB oleje.",
            "",
            "Olej odčerpej z tyglíku čerpadlem do nádrže a z ní potrubím do motoru. Kbelíkem motor nenaplníš.",
            "",
            "Kbelík na úkol naplníš tak, že klikneš prázdným kbelíkem na tyglík nebo nádrž. Musí v nich být aspoň 1 000 mB oleje.",
            "",
            "&aTip: Olej je slabé palivo, ale na první motor stačí. Až budeš chtít víc síly, pokračuj k etanolu a bionaftě.&r"]),
        Q("basin_lid", "Víko na tyglík", dep=["plant_oil"],
          items=[("createdieselgenerators:basin_lid", 1)], xp=20, d=[
            "Olej sám je slabý. Na silnější bionaftu potřebuješ ještě etanol, a ten vzniká kvašením.",
            "",
            "Víko na tyglík (&eBasin Lid&r) udělá z tyglíku kvasnou nádobu. Vyrobíš ho ze 3 andezitových slitin a hodin. Polož ho na tyglík. Do tyglíku pak vhoď suroviny a víko je samo zpracuje, bez lisu i míchačky.",
            "",
            "&aTip: Recepty ukáže JEI v záložce Basin Processing. Takhle uděláš i těsto z mouky a vody.&r"]),
        Q("ethanol", "Etanol", dep=["basin_lid"],
          items=[("createdieselgenerators:ethanol_bucket", 1)], xp=30, d=[
            "Etanol (&eEthanol&r) je palivo, které vzniká kvašením.",
            "",
            "Do tyglíku s víkem vhoď cukr, jablko, bramboru nebo cukrovou třtinu a k tomu kostní moučku. Z jedné suroviny a jedné kostní moučky vznikne 200 mB etanolu.",
            "",
            "&aTip: Etanol spálí motor, hořák i zapalovač.&r"]),
        Q("bulk_fermenter", "Velký kvasný sud", dep=["ethanol"], optional=True,
          items=[("createdieselgenerators:bulk_fermenter", 1)], xp=25, d=[
            "Kvasný sud (&eBulk Fermenter&r) je větší kvasná nádoba. Vyrobíš ho ze sudu a 2 andezitových slitin. Sudy položené k sobě se spojí do jednoho velkého, podobně jako nádrže.",
            "",
            "Ze stejné suroviny a kostní moučky dá 400 mB etanolu. To je dvakrát víc než tyglík s víkem.",
            "",
            "Předměty do něj dostaneš trychtýřem nebo násypkou, kapaliny potrubím.",
            "",
            "&aTip: S ohřevem zespodu umí z dlažebního kamene udělat lávu.&r"]),
        Q("biodiesel", "Automatická bionafta", s="Pokročilý", dep=["plant_oil", "ethanol"], shape="hexagon", size=1.5,
          items=[("createdieselgenerators:biodiesel_bucket", 1)], xp=50, d=[
            "Bionafta (&eBiodiesel&r) je nejlepší palivo bez ropy. V motoru je asi dvakrát silnější než olej nebo etanol.",
            "",
            "Teď už ruční plnění nestačí – motor palivo spaluje pořád. Postav linku, která bionaftu vyrábí sama:",
            "1. Pás doveze semínka (třeba z farmy s mechanickým sklízečem) do tyglíku pod lisem.",
            "2. Do tyglíku s víkem sype trychtýř cukrovou třtinu a kostní moučku.",
            "{@pagebreak}",
            "3. Olej a etanol přiveď čerpadly do tyglíku pod mechanickou míchačkou (&eMechanical Mixer&r). Ze 100 mB oleje a 100 mB etanolu vznikne 200 mB bionafty. Ohřev není potřeba.",
            "4. Bionaftu odčerpej do nádrže a z ní potrubím do motoru.",
            "",
            "&aTip: Když motor stojí, zkontroluj brýlemi, jestli v nádrži není prázdno.&r"]),
        Q("canister", "Kanystr", dep=["plant_oil"], optional=True,
          items=[("createdieselgenerators:canister", 1)], xp=15, d=[
            "Kanystr (&eCanister&r) je přenosná nádrž na 4 000 mB kapaliny. Když ho vykopeš, kapalina v něm zůstane.",
            "",
            "Vyrobíš ho ze sudu, 2 andezitových slitin a 3 železných plátů.",
            "",
            "Naplníš ho potrubím nebo dávkovačem.",
            "",
            "&aTip: Hodí se na převoz paliva k motoru, který stojí daleko od základny.&r"]),
        Q("burner", "Hořák na palivo", dep=["ethanol", "create:brass"],
          items=[("createdieselgenerators:burner", 1)], xp=40, d=[
            "Ohňohořák musíš krmit předměty. Hořák (&eBurner&r) také hřeje, ale pálí kapalné palivo z potrubí. Nemusíš do něj chytat ohniváka.",
            "",
            "Vyrobíš ho z prázdného ohňohořáku (&eEmpty Blaze Burner&r), mosazného ingotu, hřídele, 2 andezitových slitin a 2 křesadel.",
            "",
            "Palivo do něj přiveď potrubím. Jak silně hoří, nastavíš rukojetí k ventilu (např. &eCopper Valve Handle&r) přiloženou k hořáku.",
            "",
            "Hřeje tyglík i destilační věž.",
            "",
            "&aTip: Každé palivo hřeje jinak. Podrž Alt nad kbelíkem paliva a uvidíš jeho sílu v motoru i v hořáku.&r"]),

        # --- motory
        Q("upgrades", "Vylepšení motoru", dep=["create_addons:diesel"], optional=True,
          items=[("createdieselgenerators:engine_turbocharger", 1), ("createdieselgenerators:engine_silencer", 1)], xp=30, d=[
            "Naftový motor jde vylepšit. Vylepšení nasadíš tak, že s ním klikneš pravým tlačítkem na motor.",
            "",
            "Turbodmychadlo (&eEngine Turbocharger&r) motor zrychlí. Ve výchozím nastavení se točí dvakrát rychleji.",
            "",
            "Tlumič (&eEngine Silencer&r) motor ztiší. Hodí se, když motor stojí u domu."]),

        # --- ropa
        Q("hole", "Postav ropnou pumpu", dep=["create_addons:pumpjack"],
          items=[("createdieselgenerators:pumpjack_hole", 1)], xp=50, d=[
            "Teď už palivo z rostlin na velké stroje nestačí. Nejsilnější palivo je z ropy. Díly pumpy máš z questu Ropná pumpa v kapitole Create: doplňky.",
            "",
            "Ropná pumpa je pohyblivá konstrukce. Postav ji nad chunkem, kde skener našel ropu.",
            "",
            "1. Postav sloup a na jeho vršek dej hlavní ložisko (&ePumpjack Bearing&r).",
            "2. Postav rameno – rovnou vodorovnou řadu bloků (např. kovové nosníky). Musí vést napříč těsně před přední stranou ložiska.",
            "3. Na jeden konec ramene dej hlavu pumpy (&ePumpjack Head&r).",
            "4. Na druhý konec dej druhé ložisko a klikni na něj montážním klíčem. Změní se na kloub pro kliku.",
            "{@pagebreak}",
            "5. Pod kloub postav kliku (&ePumpjack Crank&r) a přiveď do ní rotaci.",
            "6. Celé rameno slep vteřinovým lepidlem (&eSuper Glue&r).",
            "7. Klikni prázdnou rukou na hlavní ložisko. Pumpa se sestaví. Když se klika točí, pumpa se kývá.",
            "",
            "Když pumpa napíše chybu, uprav délku ramene nebo velikost kliky (nastavuje se na klice).",
            "{@pagebreak}",
            "Teď vrt (&ePumpjack Hole&r):",
            "1. Pod hlavou pumpy vykopej díru až k podloží.",
            "2. Do díry dej rovnou svislou řadu potrubí (&eFluid Pipe&r) až k podloží.",
            "3. Navrch potrubí polož vrt.",
            "4. Ropu z vrtu odsávej z boku mechanickým čerpadlem (&eMechanical Pump&r)."]),
        Q("crude", "Surová ropa", dep=["hole"],
          items=[("createdieselgenerators:crude_oil_bucket", 1)], xp=40, d=[
            "Surová ropa (&eCrude Oil&r) teče z vrtu ropné pumpy. Sama v motoru nehoří, musíš ji nejdřív vydestilovat.",
            "",
            "Pumpa těží, jen když se točí klika. Ropu odváděj čerpadlem do velké nádrže.",
            "",
            "&aTip: Podívej se na vrt inženýrskými brýlemi (&eEngineer's Goggles&a). Uvidíš, kolik ropy v chunku zbývá. Obyčejné naleziště se časem vyčerpá, naleziště &eBottomless Supply&a je nekonečné.&r"]),
        Q("asphalt", "Asfaltová silnice", dep=["crude"], optional=True,
          items=[("createdieselgenerators:asphalt_block", 16)], xp=20, d=[
            "Asfalt (&eAsphalt Block&r) je blok na silnice. Chodí se po něm o čtvrtinu rychleji.",
            "",
            "V tyglíku pod míchačkou s ohřevem smíchej 2 štěrky, 2 písky a 100 mB ropy. Vzniknou 4 bloky asfaltu.",
            "",
            "Jde to i ručně: 4 písky, 4 štěrky a kbelík ropy dají na pracovním stole 8 bloků.",
            "",
            "&aTip: Na řezačce kamene z asfaltu uděláš schody a desky.&r"]),
        Q("fuels", "Nafta a benzín", s="Expert", dep=["create_addons:distill", "crude"], shape="hexagon", size=1.5,
          items=[("createdieselgenerators:diesel_bucket", 1), ("createdieselgenerators:gasoline_bucket", 1)], xp=80, d=[
            "Teď už surová ropa nestačí – v motoru nehoří. Destilační věž ji rozdělí na naftu (&eDiesel&r) a benzín (&eGasoline&r).",
            "",
            "1. Postav nádrž (&eFluid Tank&r) vysokou aspoň 3 bloky.",
            "2. Klikni na ni destilační jednotkou (&eDistillation Controller&r). Potřebuješ jednu na každý blok nádrže. Na věž 1×1×3 tedy tři.",
            "3. Pod věž dej ohňohořáky (&eBlaze Burner&r) a krm je. Ponder ukazuje jeden ohňohořák pod každým blokem spodku. Čím víc rozpálených ohňohořáků, tím rychleji věž pracuje.",
            "{@pagebreak}",
            "4. Ropu napumpuj do spodního patra věže.",
            "5. Nafta se objeví ve 2. patře, benzín ve 3. patře. Odčerpej je potrubím z boku těchto pater.",
            "",
            "&cKdyž se patro s výstupem zaplní, věž se zastaví. Výstupy průběžně odčerpávej.&r",
            "",
            "&aTip: Ohňodort (&eBlaze Cake&r) ohňohořák rozžhaví víc. Pak ze 100 mB ropy vznikne 75 mB nafty a 75 mB benzínu místo 50 a 50 a jde to rychleji.&r"]),

        # --- nástroje na kapaliny
        Q("lighter", "Zapalovač", dep=["plant_oil", "create:brass", "create:spout"], optional=True,
          items=[("createdieselgenerators:lighter", 1)], xp=15, d=[
            "Zapalovač (&eLighter&r) je křesadlo na palivo. Naplň ho dávkovačem jakýmkoli palivem z této kapitoly.",
            "",
            "Pravým tlačítkem ho otevřeš nebo zavřeš a zkusíš zapálit oheň. Shift + pravé tlačítko ho jen otevře nebo zavře.",
            "",
            "&aTip: Přejmenuj ho na kovadlině. Některá jména mu změní vzhled.&r"]),
        Q("sprayer", "Chemický rozprašovač", dep=["plant_oil", "create:precision", "create:crafter", "create:spout"],
          items=[("createdieselgenerators:chemical_sprayer", 1)], xp=30, d=[
            "Chemický rozprašovač (&eChemical Sprayer&r) stříká kapalinu ze své nádržky.",
            "",
            "Vyrobíš ho v mechanickém výrobníku (&eMechanical Crafter&r) z precizního strojku, měděného bloku, potrubí, sušené chaluhy a 2 chaluhových rukojetí (&eKelp Handle&r).",
            "",
            "Naplníš ho dávkovačem jakoukoli kapalinou. Nádržka pojme 200 mB.",
            "",
            "Podrž pravé tlačítko a rozprašovač začne stříkat."]),
        Q("flamethrower", "Plamenomet", dep=["sprayer", "lighter"],
          items=[("createdieselgenerators:chemical_sprayer_lighter", 1)], xp=30, d=[
            "Rozprašovač se zapalovačem (&eChemical Sprayer With Lighter&r) se pokusí stříkanou kapalinu zapálit. Je to plamenomet.",
            "",
            "Vyrobíš ho pokladačem (&eDeployer&r): polož rozprašovač pod pokladač a dej mu do ruky zapalovač.",
            "",
            "Naplň ho hořlavým palivem, třeba benzínem.",
            "",
            "&cPozor, oheň zapálí i dřevěné stavby kolem tebe!&r"]),
        Q("turret", "Chemická věž", dep=["sprayer"],
          items=[("createdieselgenerators:chemical_turret", 1), ("createdieselgenerators:entity_filter", 1)], xp=50, d=[
            "Chemická věž (&eChemical Turret&r) je rozprašovač na podstavci. Potřebuje rotaci z ozubeného kolečka a kapalinu v nádržce.",
            "",
            "Když dostane redstonový signál, začne stříkat. Pravým kliknutím ji ovládáš sám, se Shiftem ovládání ukončíš.",
            "",
            "Věž může ovládat i tvor. Posaď ho na sedačku z Create (&eSeat&r) hned vedle věže. Do slotu filtru na věži dej filtr tvorů (&eEntity Filter&r). Tvor pak bude stříkat na ty, kteří filtru odpovídají.",
            "",
            "&aTip: Věž jde vylepšit zapalovačem, pak stříká oheň.&r"]),

        # --- velké motory
        Q("huge", "Obří naftový motor", dep=["create_addons:big_diesel", "create:steam", "fuels"],
          items=[("createdieselgenerators:huge_diesel_engine", 1)], xp=80, d=[
            "Obří naftový motor (&eHuge Diesel Engine&r) dá ze všech motorů nejvíc síly z jednoho bloku a točí se nejrychleji. Vyrábí se z parního motoru.",
            "",
            "Klikni hřídelí (&eShaft&r) na motor a hřídel se sama položí na správné místo, dva bloky před motor. Palivo přiveď potrubím.",
            "",
            "Jakmile motor dostane palivo, hřídel se začne točit. Redstonový signál ho zastaví.",
            "",
            "&aTip: Nejsilnější palivo je nafta. Podrž Alt nad kbelíkem paliva a uvidíš, kolik dá který motor.&r"]),
        Q("plant", "Naftová elektrárna", s="Expert", dep=["huge"], shape="hexagon", size=1.5,
          items=[("createdieselgenerators:oil_barrel", 4)], xp=100, d=[
            "Teď to spoj dohromady: stanice, která sama těží ropu, destiluje ji a pohání motory.",
            "",
            "1. Ropné pumpy (nejlépe na nalezišti &eBottomless Supply&r) → čerpadlo → nádrž s ropou.",
            "2. Destilační věž s ohňodorty. Ohňohořáky může krmit pokladač (&eDeployer&r) nebo mechanická paže. Ze 100 mB ropy tak dostaneš 75 + 75 mB místo 50 + 50.",
            "{@pagebreak}",
            "3. Naftu ukládej do sudů na ropu (&eOil Barrel&r). Sudy položené k sobě se spojí do většího (nejvýš 3 bloky široko). Můžeš je dát nastojato i naležato.",
            "4. Ze sudů veď naftu potrubím do obřích nebo modulárních motorů.",
            "5. Benzín pal v hořácích, které hřejí tyglíky nebo věž, nebo v dalších motorech.",
            "{@pagebreak}",
            "Inženýrskými brýlemi zkontroluj, kolik síly (SU) stanice dává a kolik jí stroje berou.",
            "",
            "&aTip: Alternátor z modu &bCreate Crafts & Additions&r změní rotaci na elektřinu (FE).&r",
            "",
            "&cHořlavé kapaliny drž dál od ohně a lávy.&r"]),

        # --- formy
        Q("molds", "Formy", dep=["intro", "create:drill", "create:sheets"], optional=True,
          items=[("createdieselgenerators:mold", 1)], xp=20, d=[
            "Forma (&eMold&r) se vkládá do tyglíku. Mechanický lis pak do formy lisuje a dávkovač do ní odlévá kapalinu.",
            "",
            "Formu nařeže mechanická pila (&eMechanical Saw&r) ze železného plátu. Tvarů je víc (řetěz, vlnky, miska, tyčka). Vybereš ho filtrem na pile.",
            "",
            "&aTip: Recepty ukáže JEI v záložkách Compression Molding a Casting. Třeba lis s řetězovou formou udělá z 6 železných nugetů řetěz.&r"]),
    ],
)

# Přepsané původní questy kapitoly create_addons (úkoly beze změny)
ORIG_OIL = {
    "diesel": Q("diesel", "Naftový motor", s="Create: Diesel Generators", dep=["start", "create:brass", "create:fluids", "cadd_oil:pistons"],
                items=[("createdieselgenerators:diesel_engine", 1)], xp=40, d=[
        "Naftový motor (&eDiesel Engine&r) z modu &bCreate: Diesel Generators&r pálí kapalné palivo a dává silnou rotaci z jednoho bloku.",
        "",
        "Palivo do něj přiveď potrubím, kbelíkem ho nenaplníš. Rotace jde ven hřídelí. Redstonový signál motor zastaví.",
        "",
        "Na začátek stačí rostlinný olej nebo etanol. Víc najdeš v kapitole Ropa a palivo."]),
    "oil": Q("oil", "Najdi ropu", dep=["diesel"],
             items=[("createdieselgenerators:oil_scanner", 1)], xp=30, d=[
        "Ropný skener (&eOil Scanner&r) zjistí, kolik ropy je v chunku, kde stojíš. Klikni pravým tlačítkem a chvíli počkej.",
        "",
        "Víc ropy bývá v savanách, pouštích, pustinách (&eBadlands&r), pláních a oceánech. Nejlepší je naleziště &eBottomless Supply&r – nikdy nedojde.",
        "",
        "Víc najdeš v kapitole Ropa a palivo."]),
    "pumpjack": Q("pumpjack", "Ropná pumpa", dep=["oil", "create:bearing", "create:crafter"],
                  items=[("createdieselgenerators:pumpjack_crank", 1), ("createdieselgenerators:pumpjack_head", 1), ("createdieselgenerators:pumpjack_bearing", 1)], xp=50, d=[
        "Ropná pumpa tahá ropu z podloží. Hlavní díly jsou ložisko (&ePumpjack Bearing&r), hlava (&ePumpjack Head&r) a klika (&ePumpjack Crank&r).",
        "",
        "Ložisko vyrobíš z mechanického ložiska, zinkových ingotů a andezitových slitin. Klika se skládá v mechanickém výrobníku.",
        "",
        "Ložiska budeš potřebovat dvě. Návod na stavbu krok za krokem najdeš v kapitole Ropa a palivo."]),
    "distill": Q("distill", "Destilace", dep=["pumpjack"],
                 items=[("createdieselgenerators:distillation_controller", 1)], xp=60, d=[
        "Destilační jednotka (&eDistillation Controller&r) promění obyčejnou nádrž v destilační věž. Ta rozdělí ropu na naftu a benzín.",
        "",
        "Jeden recept dá 4 kusy. Na každý blok věže potřebuješ jeden.",
        "",
        "Návod na stavbu věže najdeš v kapitole Ropa a palivo."]),
    "big_diesel": Q("big_diesel", "Modulární motor", dep=["distill"],
                    items=[("createdieselgenerators:large_diesel_engine", 1)], xp=60, d=[
        "Modulární naftový motor (&eModular Diesel Engine&r) se dá skládat za sebe do řady.",
        "",
        "Čím víc motorů spojíš, tím víc síly dají.",
        "",
        "Víc najdeš v kapitole Ropa a palivo."]),
}

NO_RECIPE_OIL = {
    "createdieselgenerators:plant_oil_bucket": "kbelík naplní dávkovač (Spout) rostlinným olejem z lisu",
    "createdieselgenerators:ethanol_bucket": "kbelík naplní dávkovač (Spout) etanolem z kvašení",
    "createdieselgenerators:biodiesel_bucket": "kbelík naplní dávkovač (Spout) bionaftou z míchačky",
    "createdieselgenerators:crude_oil_bucket": "kbelík naplní dávkovač (Spout) ropou z ropné pumpy",
    "createdieselgenerators:diesel_bucket": "kbelík naplní dávkovač (Spout) naftou z destilační věže",
    "createdieselgenerators:gasoline_bucket": "kbelík naplní dávkovač (Spout) benzínem z destilační věže",
}


# ======================================================================
# Kapitola PRŮMYSL
# ======================================================================
# Kapitola Průmysl: Create: Enchantment Industry, Create Ore Excavation, Create: Power Loader,
# Create: Connected, Create: Dragons Plus, Create: More Features.
# Vstupní questy modů jsou původní questy v kapitole create_addons („Create: doplňky“, viz ORIG).
# Milníky (hexagon) označují přechod na úroveň Začátečník / Pokročilý / Expert.


CADD_INDUSTRY = dict(
    key="cadd_industry", group="create", title="Průmysl",
    subtitle="Zkušenosti, těžba žil, chunk loadery a chytré převody",
    icon="createoreexcavation:drilling_machine",
    quests=[
        Q("start", "Průmysl", s="Doplňky pro velkou továrnu", icon="createoreexcavation:drilling_machine",
          tasks=[auto()], dep=["create_addons:start"], xp=10, d=[
            "Tato kapitola ukazuje doplňky &bCreate&r pro velkou továrnu.",
            "Najdeš tu očarování s tekutými zkušenostmi, nekonečnou těžbu rud, načítání chunků, nové převodovky, práci s kapalinami a pár užitečných drobností.",
            "Každý mod začíná questem v kapitole &eCreate: doplňky&r. Pak pokračuješ tady od začátečníka až po experta.",
            "Šestiúhelníky jsou milníky. Jejich podnázev říká, na jakou úroveň se jimi dostaneš."]),

        # ---------- Create: Enchantment Industry ----------
        Q("xp_store", "Ulož si zkušenosti", s="Začátečník", icon="create_enchantment_industry:experience_hatch",
          tasks=[adv("create_enchantment_industry:spirit_taking")], dep=["create_addons:cei"], xp=20, **M, d=[
            "Zkušenosti (zelené kuličky) teď nemusíš nosit v sobě. Poklop zkušeností (&eExperience Hatch&r) je převede na tekuté zkušenosti (&eLiquid Experience&r) a uloží do nádrže.",
            "Polož ho na nádrž (&eFluid Tank&r). Pravým tlačítkem do něj zkušenosti uložíš. Shift + pravé tlačítko je zase vybereš.",
            "Tekuté zkušenosti se měří v mB jako jiné kapaliny. Můžeš je čerpat trubkami a plnit jimi stroje.",
            "&aTip:&r Na panelu poklopu nastavíš, kolik zkušeností se přesune jedním kliknutím."]),
        Q("lantern", "Lucerna zkušeností", dep=["xp_store"], items=[("create_enchantment_industry:experience_lantern", 1)], xp=25, d=[
            "Teď už nemusíš kuličky sbírat sám. Lucerna zkušeností (&eExperience Lantern&r) je nasává z okolí, i z hráčů. Čím víc jich má, tím víc svítí.",
            "Vyrobíš ji z bloku zkušeností (&eBlock of Experience&r), houby a měděného pouzdra (&eCopper Casing&r).",
            "&aTip:&r Hodí se k farmě na moby. Funguje i na pohyblivé konstrukci (kontrapci)."]),
        Q("template", "Šablona očarování", dep=["xp_store"], items=[("create_enchantment_industry:enchanting_template", 1)], xp=25, d=[
            "Šablona očarování (&eEnchanting Template&r) nese očarování, která později přeneseš na předmět.",
            "Vyrobíš ji, když blok zkušeností rozmáčkneš mechanickým lisem (&eMechanical Press&r).",
            "Zatím je prázdná. Naplníš ji v plamenném očarovávači a na předmět ji naneseš plamenným kovářem."]),
        Q("smith_tpl", "Kovářská šablona plamene", dep=["xp_store"],
          items=[("create_dragons_plus:blaze_upgrade_smithing_template", 2)], xp=40, d=[
            "Tuto kovářskou šablonu (&eSmithing Template&r) potřebuješ, když chceš z ohňohořáku (&eBlaze Burner&r) udělat plamenný stroj.",
            "První kus najdeš v &eNetheru&r, v truhlách staveb &eNether Fortress&r a &eBastion Remnant&r.",
            "Další si vyrobíš: šablona, 7 ohnivých tyčí a netherrack dají 2 šablony. &cVždy si nech aspoň jednu šablonu na další kopírování.&r"]),
        Q("first_enchant", "Očarování bez stolu", s="Pokročilý", icon="create_enchantment_industry:blaze_enchanter",
          tasks=[adv("create_enchantment_industry:blazing_enchantment")], dep=["create_addons:enchanter"], xp=40, **M, d=[
            "Teď už nemusíš klikat u očarovacího stolu a platit vlastními úrovněmi. Plamenný očarovávač bere tekuté zkušenosti z trubky.",
            "Nastav na panelu úroveň, vlož neočarovaný předmět a počkej. Očarovaný předmět vybereš pravým tlačítkem s prázdnou rukou.",
            "&aPrvní automatizace:&r Mechanická paže (&eMechanical Arm&r) umí očarovávači předměty vkládat i je vybírat. Stačí k němu přivést zkušenosti trubkou."]),
        Q("sigil", "Naplň šablonu", icon="create_enchantment_industry:enchanting_template",
          tasks=[adv("create_enchantment_industry:sigil_forging")], dep=["first_enchant", "template"], xp=40, d=[
            "Náhodné očarování ti nestačí? Očaruj místo předmětu prázdnou šablonu.",
            "Do panelu na očarovávači vlož vzorový předmět, třeba diamantový meč. Pak do očarovávače vlož prázdnou šablonu.",
            "Šablona dostane očarování, která se hodí pro vzorový předmět. Různé materiály a druhy předmětů dávají různá očarování."]),
        Q("forger", "Plamenný kovář", dep=["smith_tpl", "create:burner"], items=[("create_enchantment_industry:blaze_forger", 1)], xp=50, d=[
            "Plamenný kovář (&eBlaze Forger&r) spojuje očarování jako kovadlina, ale cena za opravu se nezvyšuje.",
            "Vyrobíš ho na kovářském stole: ohňohořák + kovadlina + kovářská šablona plamene. Pohánějí ho tekuté zkušenosti.",
            "Na bočním panelu přepínáš režim: spojení dvou předmětů, nanesení šablony na předmět, nebo vytažení očarování do prázdné šablony."]),
        Q("apply", "Nanes šablonu", icon="create_enchantment_industry:blaze_forger",
          tasks=[adv("create_enchantment_industry:sigil_casting")], dep=["sigil", "forger"], xp=40, d=[
            "Přepni plamenného kováře do režimu nanášení (&eApply&r).",
            "Vlož do něj předmět a naplněnou šablonu. Kovář přenese očarování ze šablony na předmět.",
            "&aTip:&r I kováře umí mechanická paže plnit a vybírat."]),
        Q("cake", "Dort očarování", dep=["first_enchant", "create:spout"], items=[("create_enchantment_industry:experience_cake", 1)], xp=40, d=[
            "Dort očarování (&eCake o' Enchanting&r) přepne plamenné stroje do super režimu.",
            "Mechanickým lisem v tyglíku (&eBasin&r) slisuj vejce, cukr a lapis. Vznikne základ dortu. Dávkovačem (&eSpout&r) ho polij 1 000 mB tekutých zkušeností.",
            "Nakrm dortem očarovávač nebo kováře a stroj začne vřít. Dort jde do druhého zásobníku stroje – ten trubkou nenaplníš."]),
        Q("super", "Super očarování", s="Expert", icon="create_enchantment_industry:super_enchanting_template",
          dep=["cake", "apply"], items=[("create_enchantment_industry:super_enchanting_template", 1)], xp=80, **M, d=[
            "Teď už nejsi omezený běžnými limity. V super režimu jdou úrovně očarování nad maximum, kovář spojí i očarování, která se navzájem vylučují, a očarovávač umí pokladová očarování.",
            "V super režimu ale stroje přijímají jen super šablony (&eSuper Enchanting Template&r).",
            "{@pagebreak}",
            "Polož hromosvod přímo na blok zkušeností. Když do hromosvodu udeří blesk, blok se může změnit na blok super zkušeností (&eBlock of Super Experience&r). Blesk ze super režimu ho promění vždy.",
            "Blok super zkušeností rozmáčkni lisem a máš super šablonu.",
            "&cSuper režim přivolává blesky. Dej poblíž stroje hromosvod. Když stroj zakryješ blokem, blesk do něj neudeří, ale výsledek může být horší (třeba s kletbou).&r"]),
        Q("classic", "Očarovací linka", dep=["apply"], items=[("create_enchantment_industry:classic_blaze_enchanter", 1)], xp=60, d=[
            "Teď už nemusíš šablonu pokaždé vyrábět znovu. Klasický plamenný očarovávač (&eClassic Blaze Enchanter&r) očaruje každý předmět podle šablony ve filtru a šablona se nespotřebuje.",
            "Vyrobíš ho na kovářském stole z ohňohořáku, kovářské šablony plamene a příručky (&eBlaze's Enchanting Handbook&r). Příručku vyrobíš z kovářské šablony plamene, 2 robustních plátů, 2 lahviček zkušeností a magmového bloku.",
            "Předměty mu posílej po pásu, zkušenosti trubkou. Když šablona nese víc očarování, dá na předmět náhodně jedno. V super režimu (se super šablonou) zvedne o jednu úroveň očarování, které už předmět má ve stejné úrovni."]),

        # ---------- Create Ore Excavation ----------
        Q("drill", "Železný vrták", s="Začátečník", dep=["create_addons:excavation"], items=[("createoreexcavation:drill", 1)], xp=30, **M, d=[
            "Žíla je obrovské ložisko rudy hluboko pod zemí. Nevidíš ji a krumpáčem ji nevytěžíš – patří vždy k jednomu chunku.",
            "Vrtná souprava (&eDrilling Machine&r) z ní těží bez kopání, ale bez vrtáku nefunguje. Nejjednodušší je železný vrták (&eIron Drill&r) z 5 železných ingotů a 2 železných bloků.",
            "Vlož vrták do soupravy a roztoč ji. Souprava musí stát na pevné zemi v chunku se žílou. Brýle ti ukážou, co se těží a kolik žíly zbývá."]),
        Q("atlas", "Průzkum žíly", dep=["drill"],
          items=[("createoreexcavation:sample_drill", 1), ("createoreexcavation:vein_atlas", 1)], xp=40, d=[
            "Teď už nemusíš hledat naslepo. Hledač žil řekne jen druh rudy, přesné údaje zjistíš vzorkovacím vrtákem (&eSample Drill&r).",
            "Polož ho na žílu a navrch dej měděnou tlakovou láhev (&eCopper Backtank&r) se vzduchem. Klikni na vrták a počkej. Pak na něj klikni atlasem žil (&eOre Vein Atlas&r).",
            "Atlas si žílu zapamatuje a ukáže její polohu a velikost. Nekonečná žíla má značku ∞. Podle atlasu můžeš nastavit, co bude hledač hledat."]),
        Q("auto_mine", "Těžba bez dozoru", s="Pokročilý", dep=["atlas", "create_addons:chunkload"],
          items=[("createoreexcavation:raw_diamond", 1)], xp=50, **M, d=[
            "Teď už nemusíš soupravu vybírat ručně. Vytěžené suroviny z ní odebírej trychtýřem nebo mechanickou paží a pošli je pásem do trezoru.",
            "Chunk loader (&eAndesite Chunk Loader&r) vedle soupravy udrží chunk načtený, takže těží, i když jsi daleko.",
            "Vyplatí se diamantová žíla. Souprava z ní těží surový diamant (&eRaw Diamond&r), který mechanickou pilou rozřežeš na diamant. Smaragdová žíla funguje stejně."]),
        Q("netherite_drill", "Netheritový vrták", s="Expert", dep=["auto_mine"], items=[("createoreexcavation:netherite_drill", 1)], xp=80, **M, d=[
            "Teď už železný vrták nestačí. Nejtěžší žíly vyžadují netheritový vrták (&eNetherite Drill&r).",
            "Nejdřív vyrob diamantový vrták (&eDiamond Drill&r) ze železného vrtáku, diamantů a diamantového bloku. Pak ho na kovářském stole vylepši netheritovým ingotem a netheritovou šablonou.",
            "S ním těžíš žílu tvrzených diamantů v &eOverworldu&r a žílu prastarých trosek v &eNetheru&r. Obě potřebují při vrtání lávu – přiveď ji do soupravy trubkou."]),

        # ---------- Create: Power Loader ----------
        Q("brass_loader", "Mosazný chunk loader", s="Pokročilý", dep=["create_addons:chunkload", "create:precision", "create:crafter"],
          items=[("create_power_loader:brass_chunk_loader", 1)], xp=60, **M, d=[
            "Teď už jeden chunk nestačí. Mosazný chunk loader (&eBrass Chunk Loader&r) udrží načtených víc chunků najednou.",
            "Prázdný mosazný loader vyrobíš v mechanickém výrobníku (&eMechanical Crafter&r). Pak s ním klikni pravým tlačítkem na ghasta, aby ho chytil.",
            "Na panelu nastavíš oblast 1×1, 3×3 nebo 5×5 chunků. Větší oblast potřebuje vyšší rychlost otáčení.",
            "&aTip:&r Na pohyblivé konstrukci (kontrapci) načítá 3×3 chunky kolem sebe i bez otáčení. Vedle vlakové stanice načte okolí, jen když u ní stojí vlak."]),

        # ---------- Create: Connected ----------
        Q("cc_gearbox", "Nové převodovky", s="Začátečník", dep=["start", "create:casing"],
          items=[("create_connected:six_way_gearbox", 1), ("create_connected:parallel_gearbox", 1)], xp=25, **M, d=[
            "&bCreate: Connected&r přidává chytré díly pro rozvod otáčení. Síť je všechno, co je spojené hřídelemi a ozubenými koly.",
            "Převodovka na 6 stran (&e6-way Gearbox&r) má hřídel na všech stranách. Horní a spodní hřídel se točí poloviční rychlostí.",
            "Paralelní převodovka (&eParallel Gearbox&r) obrátí směr otáčení, když ho vede rovně. Za roh ho pošle stejným směrem."]),
        Q("cc_clutch", "Pojistky proti přetížení", dep=["cc_gearbox", "create:tube"],
          items=[("create_connected:overstress_clutch", 1), ("create_connected:shear_pin", 1)], xp=30, d=[
            "Když stroje chtějí víc síly, než zdroje dávají, síť se přetíží a zastaví celá. Tyto díly ji ochrání.",
            "Přetěžovací spojka (&eOverstress Clutch&r) se při přetížení po chvíli rozpojí. Zpátky ji spojíš montážním klíčem (&eWrench&r).",
            "Střižný kolík (&eShear Pin&r) se při přetížení zlomí a musíš ho vyměnit. Vyrobíš ho, když mechanickou pilou rozřežeš hřídel."]),
        Q("cc_brake", "Brzda", dep=["cc_gearbox"], items=[("create_connected:brake", 1)], xp=20, optional=True, d=[
            "Brzda (&eBrake&r) zastaví stroje, aniž bys rozpojoval hřídele.",
            "Když dostane redstonový signál, vytvoří obrovské zatížení. Síť se přetíží a zastaví.",
            "Vyrobíš ji z andezitového pouzdra, hřídele, redstonu a obsidiánu."]),
        Q("cc_catalyst", "Katalyzátor větráku", dep=["cc_gearbox", "create:spout", "create:brass"],
          items=[("create_connected:fan_blasting_catalyst", 1)], xp=35, d=[
            "Katalyzátor nahradí blok před větrákem (&eEncased Fan&r) při hromadném zpracování.",
            "Prázdný katalyzátor (&eEmpty Fan Catalyst&r) vyrobíš z mosazi a železných mříží. Dávkovačem ho naplň lávou a vznikne tavný katalyzátor (&eFan Blasting Catalyst&r).",
            "Polož ho před větrák místo lávy. Láva v katalyzátoru nic nezapálí a nikam neteče. S vodou vyrobíš prací katalyzátor, kliknutím netherrackem uzený katalyzátor."]),
        Q("cc_ports", "Přístup k inventářům", dep=["cc_gearbox", "create:tube", "create:brass"],
          items=[("create_connected:inventory_access_port", 1), ("create_connected:inventory_bridge", 1)], xp=30, d=[
            "Přístupový bod k inventáři (&eInventory Access Port&r) inventář „prodlouží“. Stroje připojené k bodu pracují s inventářem za ním.",
            "Inventářový most (&eInventory Bridge&r) spojí dva inventáře najednou. Na jeho filtrech nastavíš, co jde do kterého.",
            "Body ani most nemají vlastní místo na věci. Nedají se napojit za sebe. Redstonovým signálem je vypneš."]),
        Q("cc_bridge", "Kinetický most", s="Pokročilý", dep=["cc_clutch", "create:brass"],
          items=[("create_connected:kinetic_bridge", 1)], xp=40, **M, d=[
            "Teď už nemusí být celá továrna jedna síť. Kinetický most (&eKinetic Bridge&r) posílá nastavené množství síly z jedné sítě do druhé a sítě zůstanou oddělené.",
            "Když přetížíš druhou síť, první běží dál. Kolik síly most posílá, nastavíš na panelu.",
            "&aTip:&r Když se přetíží zdrojová síť, dej před most přetěžovací spojku. Uvolní sílu, kterou by most zbytečně bral."]),
        Q("cc_spg", "Sekvenční generátor", dep=["cc_bridge", "create:precision"],
          items=[("create_connected:sequenced_pulse_generator", 1)], xp=45, d=[
            "Sekvenční generátor signálu (&eSequenced Pulse Generator&r) vysílá redstonový signál podle seznamu kroků s časováním.",
            "Potřebuje řídicí čip (&eControl Chip&r). Vyrobíš ho sekvenční montáží ze zlatého plátu: pokladač přidá elektronku, pak redstone a nakonec lis. Celé se to opakuje třikrát.",
            "Pravým tlačítkem otevřeš nastavení. Signál zezadu spustí sekvenci, signál z boku ji zastaví a vynuluje."]),
        Q("cc_battery", "Bateriová banka", s="Expert", icon="create_connected:kinetic_battery",
          tasks=[adv("create_connected:kinetic_battery")], dep=["cc_bridge", "create_addons:connected"], xp=70, **M, d=[
            "Teď už jedna baterie nestačí. Postav banku, která podrží továrnu v chodu, i když zdroje nejedou. Úkol splníš, když baterii nabiješ doplna.",
            "Baterie má zadní výstup. Po nabití nebo vybití se spojí s předním vstupem, takže baterie za sebou se nabíjejí a vybíjejí postupně. Řetěz tak běží déle.",
            "Víc síly najednou dostaneš, když baterie zapojíš vedle sebe (paralelně). Signál do jedné baterie v řetězu zapne všechny.",
            "{@pagebreak}",
            "Baterie si náboj drží i jako předmět. Nabitou baterií klikni na vybíjející se baterii a dobiješ ji. Pokladač nebo mechanická paže to zvládne sám.",
            "Stav nabití přečte komparátor, přesněji prahový spínač (&eThreshold Switch&r). Displejový vysílač (&eDisplay Link&r) ho ukáže na tabuli."]),

        # ---------- Create: Dragons Plus ----------
        Q("dp_dye", "Tekuté barvivo", s="Pokročilý", dep=["create_addons:dragons", "create:mixer"],
          items=[("create_dragons_plus:red_dye_bucket", 1)], xp=30, **M, d=[
            "Teď už neobarvuješ předměty po jednom v ruce. &bCreate: Dragons Plus&r přidává tekutá barviva.",
            "V mechanické míchačce (&eMechanical Mixer&r) smíchej barvivo s vodou. Vznikne tekuté barvivo. Z 1 barviva a 250 mB vody je 250 mB tekutého barviva, na kbelík tedy potřebuješ 4 barviva.",
            "Kbelík naplníš dávkovačem nebo přes kapalinový poklop (Shift + pravé tlačítko).",
            "Vylij barvivo před větrák. Proud vzduchu přes něj hromadně obarví předměty.",
            "&aTip:&r Když tekuté barvivo steče do lávy, vznikne beton stejné barvy."]),
        Q("dp_freeze", "Hromadné mrazení", dep=["dp_dye", "create:fan"],
          items=[("minecraft:powder_snow_bucket", 1)], xp=30, d=[
            "Stejně jako barvivo funguje i prachový sníh: větrák, který přes něj fouká, předměty mrazí.",
            "Led změní na zhuštěný led a ten na modrý led. Magmový krém změní na sliz a ohnivou tyč (&eBlaze Rod&r) na větrnou tyč (&eBreeze Rod&r).",
            "Prachový sníh nabereš kbelíkem v biomech &eSnowy Slopes&r a &eGrove&r. Před větrák ho vylij z kbelíku."]),
        Q("dp_ending", "Hromadné endování", s="Expert", dep=["dp_freeze"], items=[("minecraft:dragon_head", 1)], xp=60, **M, d=[
            "Teď už nemusíš do &eEndu&r pro každý endový kámen. Větrák, který fouká přes dračí hlavu nebo dračí dech, předměty „endí“.",
            "Z dlažebního kamene udělá endový kámen, z jablka chorusové ovoce a z kůže blánu fantoma.",
            "Dračí hlavu najdeš na lodi u stavby &eEnd City&r."]),

        # ---------- Create: More Features ----------
        Q("mf_powder", "Domácí střelný prach", dep=["start", "create:millstone", "create:crushing"],
          items=[("create_mf:saltpeter", 2), ("create_mf:sulfur", 1), ("create_mf:coal_pin", 1)], xp=30, d=[
            "&bCreate: More Features&r umí vyrobit střelný prach bez creeperů.",
            "Ledek (&eSaltpeter&r) a síru (&eSulfur&r) získáš, když mlýnským kamenem (&eMillstone&r) meleš netherrack. Ledek dává i vápenec (&eLimestone&r), ale ten musíš rozdrtit drtícími koly (&eCrushing Wheel&r) – mlýnský kámen z vápence dělá něco jiného.",
            "Uhelný kolík (&eCoal Pin&r) vznikne, když drtícími koly drtíš uhlí. Ze 2 ledků, 1 síry a 1 kolíku vyrobíš 2 střelné prachy."]),
        Q("mf_box", "Andezitová bedna", dep=["start", "create:vault"], items=[("create_mf:andesite_box", 1)], xp=25, d=[
            "Andezitová bedna (&eAndesite Box&r) je velké úložiště. Pojme 1000 předmětů.",
            "Vyrobíš ji ze 6 andezitových pouzder, 2 trezorů (&eItem Vault&r) a truhly. Recept dá 2 bedny.",
            "&aTip:&r Mosazná bedna (&eBrass Box&r) pojme 3000 předmětů a spolupracuje s násypkami. Měděná bedna (&eCopper Box&r) je nádrž na 1500 mB kapaliny."]),
        Q("mf_workshop", "Řemeslníci z Create", s="Pokročilý", dep=["mf_box", "create:deployer"], items=[("create_mf:workshop", 1)], xp=50, **M, d=[
            "Teď už nemusíš všechno vyrábět sám. More Features přidává vesničanům nová povolání a každé má svůj pracovní blok.",
            "Dílna (&eWorkshop&r) udělá z vesničana bez práce konstruktéra (&eConstructor&r). Potřebuješ na ni sadu základních strojů (&eSet Of Basic Mechanisms&r).",
            "Sada se skládá z lisu, větráku, míchačky, vrtáku, pokladače, pily, sklízeče, pluhu a mlýnského kamene.",
            "Další pracovní bloky jsou třeba &ePlumber Table&r, &eLineman Table&r nebo &ePostman worktable&r. Noví řemeslníci prodávají za smaragdy věci z Create."]),
    ],
)

# Přepsané původní questy kapitoly create_addons (klíče a úkoly beze změny)
ORIG_INDUSTRY = {
    "dragons": Q("dragons", "Kapalinový poklop", dep=["start", "create:fluids"], items=[("create_dragons_plus:fluid_hatch", 1)], xp=30, d=[
        "&bCreate: Dragons Plus&r přidává hlavně věci pro práci s kapalinami. Potřebují ho i další doplňky.",
        "Kapalinový poklop (&eFluid Hatch&r) vyrobíš z měděného ingotu a cedníku (&eItem Drain&r). Polož ho na nádrž.",
        "Pravým tlačítkem s kbelíkem vyliješ kapalinu do nádrže. Shift + pravé tlačítko kbelík z nádrže naplní.",
        "Víc najdeš v kapitole Průmysl."]),
    "cei": Q("cei", "Tekuté zkušenosti", dep=["dragons", "create:crushing"],
             items=[("create_enchantment_industry:mechanical_grindstone", 1), ("create_enchantment_industry:experience_hatch", 1)], xp=40, d=[
        "&bCreate: Enchantment Industry&r mění zkušenosti na kapalinu. Tu můžeš čerpat, skladovat a očarovávat s ní.",
        "Nejdřív potřebuješ blok zkušeností (&eBlock of Experience&r) z 9 nugetů zkušeností. Nugety občas padají, když drtícími koly drtíš rudy.",
        "Klikni blokem zkušeností na položený kapalinový poklop a vznikne poklop zkušeností (&eExperience Hatch&r). Mechanickou brusku (&eMechanical Grindstone&r) vyrobíš z andezitové slitiny a hřídele.",
        "{@pagebreak}",
        "Klikni bruskou na cedník (&eItem Drain&r) a vznikne brusný odtok. Na něj polož druhou brusku a roztoč ji.",
        "Bruska rozemele nugety zkušeností na tekuté zkušenosti. Umí taky sundat očarování z předmětu.",
        "Víc najdeš v kapitole Průmysl."]),
    "enchanter": Q("enchanter", "Plamenný očarovávač", dep=["cei", "create:burner"],
                   items=[("create_enchantment_industry:blaze_enchanter", 1)], xp=60, shape="hexagon", size=1.5, d=[
        "Plamenný očarovávač (&eBlaze Enchanter&r) očarovává jako očarovací stůl. Místo tvých úrovní ale bere tekuté zkušenosti.",
        "Vyrobíš ho na kovářském stole: ohňohořák (&eBlaze Burner&r) + očarovací stůl + kovářská šablona plamene. Šablonu najdeš v truhlách staveb &eNether Fortress&r a &eBastion Remnant&r v &eNetheru&r.",
        "Na panelu nastav úroveň očarování (u očarovacího stolu je nejvýš 30) a vlož předmět. &aVyšší úroveň není vždy lepší – některá očarování se pak neobjeví.&r",
        "Víc najdeš v kapitole Průmysl."]),
    "printer": Q("printer", "Tiskárna", dep=["cei", "create:spout"], items=[("create_enchantment_industry:printer", 1)], xp=40, d=[
        "Tiskárna (&ePrinter&r) kopíruje knihy a další věci.",
        "Vyrobíš ji z mosazného plátu, dávkovače (&eSpout&r) a železného bloku.",
        "Do filtru vlož předlohu a přiveď správnou kapalinu. Umí kopírovat popsané i očarované knihy, pojmenovat předměty nebo změnit adresu balíčku. Co přesně potřebuje, ukáže JEI.",
        "Víc najdeš v kapitole Průmysl."]),
    "excavation": Q("excavation", "Nekonečná ruda", dep=["start", "create:crafter", "create:precision", "create:spout"],
                    items=[("createoreexcavation:vein_finder", 1), ("createoreexcavation:drilling_machine", 1)], xp=60, d=[
        "&bCreate Ore Excavation&r: hluboko pod zemí jsou velké žíly rud. Vrtná souprava je těží pořád dokola.",
        "Hledač žil (&eOre Vein Finder&r) vyrobíš z endového oka, ametystu, redstonové rudy a 2 klacků. &cRedstonovou rudu musíš vytěžit krumpáčem s Hedvábným dotekem.&r",
        "Klikni hledačem pravým tlačítkem. Řekne ti, jestli je žíla přímo v tomto chunku, poblíž, nebo jestli jsou dál jen její stopy.",
        "Vrtnou soupravu (&eDrilling Machine&r) složíš v mechanickém výrobníku. Polož ji v chunku se žílou. Víc najdeš v kapitole Průmysl."]),
    "chunkload": Q("chunkload", "Načítání chunků", dep=["start", "create:casing"],
                   items=[("create_power_loader:andesite_chunk_loader", 1)], xp=40, d=[
        "&bCreate: Power Loader&r udrží chunk načtený, i když jsi daleko. Stroje v něm pak běží dál.",
        "Prázdný andezitový loader (&eEmpty Andesite Chunk Loader&r) vyrobíš ze skla, kotvy oživení (&eRespawn Anchor&r), hřídele a andezitových pouzder. Pak s ním klikni pravým tlačítkem na ghasta v &eNetheru&r.",
        "Chycený ghast loader oživí. Loader pak drží svůj chunk, dokud se točí dost rychle. Víc najdeš v kapitole Průmysl."]),
    "connected": Q("connected", "Baterie a silo", dep=["start", "create:precision"],
                   items=[("create_connected:kinetic_battery", 1), ("create_connected:item_silo", 1)], xp=40, d=[
        "&bCreate: Connected&r přidává spoustu chytrých dílů. Tyhle dva patří k nejužitečnějším.",
        "Kinetická baterie (&eKinetic Battery&r) ukládá sílu. Bez signálu se nabíjí ze sítě. S redstonovým signálem se vybíjí a sama pohání stroje.",
        "Itemové silo (&eItem Silo&r) je trezor postavený na výšku. Vyrobíš ho ze sudu a železných plátů. Baterie vyrobíš z mosazného pouzdra, precizního strojku, 2 železných plátů a redstonu – recept dá rovnou 8 kusů.",
        "Víc najdeš v kapitole Průmysl."]),
}

NO_RECIPE_INDUSTRY = {
    "create_dragons_plus:red_dye_bucket": "Míchačka: červené barvivo + voda = tekuté červené barvivo (recept mixing/red_dye_from_item); kbelík se naplní dávkovačem nebo přes Fluid Hatch.",
}


# ======================================================================
# Kapitola VELKÁ DĚLA
# ======================================================================
# Kapitola Velká děla (Create Big Cannons 5.11.7). Fakta ověřena v jaru:
# recepty data/createbigcannons/recipe, block_recipes (odlévání/vrtání/stavba vrstev),
# ponder texty a scény (assets/createbigcannons/ponder), CBCBigCannonMaterials / CBCAutocannonMaterials,
# big_cannon_breech_strength, CBCCfgFailure (výchozí šance selhání), CannonCastMouldBlock, CannonCastShape.

CADD_CANNONS = dict(
    key="cadd_cannons", group="create", title="Velká děla",
    subtitle="Od železného děla po ocelové a autokanón", icon="createbigcannons:he_shell",
    quests=[
        Q("intro", "Velká děla", s="Jak funguje dělo", icon="createbigcannons:cannon_mount", tasks=[auto()], dep=["create_addons:start"], xp=10, d=[
            "&bCreate Big Cannons&r přidává obří děla, která se staví z bloků. Dělo je řada bloků položená na lafetě.",
            "Odzadu dopředu: uzávěr (&eCannon End&r) nebo závěr (&eBreech&r), pak komory (&eCannon Chamber&r) na nálože a nakonec hlaveň (&eCannon Barrel&r).",
            "Pojmy: nálož (&ePowder Charge&r) je pytel prachu, který střelu vystřelí. Komora je díl, kam patří nálože. Hlaveň je přední díl, kterým letí střela. Závěr je zadní díl, který jde otevřít.",
            "Postup: nejdřív jednoduché dělo z kovaného železa. Pak litinové dělo, které se odlévá do forem. Nakonec bronz a ocel, které vydrží víc náloží.",
            "&cŠpatně nabité dělo může prasknout a vybuchnout. Čti questy pozorně.&r",
        ]),
        Q("wrought", "Železné dělo", dep=["intro", "create_addons:cannon"], xp=30,
          items=[("createbigcannons:wrought_iron_cannon_end", 1), ("createbigcannons:wrought_iron_cannon_chamber", 2)], d=[
            "Nejjednodušší dělo je z kovaného železa. Uzávěr (&eWrought Iron Cannon End&r) a komoru (&eWrought Iron Cannon Chamber&r) vyrobíš na pracovním stole ze železných plátů a střelného prachu. Uzávěr potřebuje navíc železný ingot.",
            "Tyhle bloky se po položení samy spojí. Postav je vodorovně na lafetu: vzadu uzávěr, před ním dvě komory. Přesné místo ukáže ponder lafety (podrž &eW&r).",
            "&cŽelezné dělo vydrží jen 1 nálož.&r Dřevěné dělo (&eLog Cannon Chamber&r) je ještě slabší – může prasknout už při jedné náloži.",
        ]),
        Q("loading", "Nabij a vystřel", s="Začátečník", dep=["wrought", "create_addons:shot"], xp=40, shape="hexagon", size=1.5,
          items=[("createbigcannons:ram_rod", 1)], d=[
            "Nabíjecí tyč (&eRam Rod&r) zatlačí náboje do děla. Vyrobíš ji z beranidla (&eRam Head&r) a dvou klacků.",
            "Polož nálož (&ePowder Charge&r) jako blok před ústí děla a klikni na ni tyčí. Nálož se zasune dovnitř. Stejně potom zatlač i střelu.",
            "Nálože jsou vždy vzadu, střela před nimi. Tyč ti při práci bere hlad.",
            "{@pagebreak}",
            "Na lafetě je ploška s kladívkem. Když do ní pustíš redstonový signál (třeba pákou), dělo se sestaví.",
            "Pak dej signál do plošky s hořícím dělem. Dělo vystřelí.",
            "Když signál z kladívka vypneš, dělo se rozloží a vrátí se do polohy, ve které bylo sestavené.",
        ]),
        Q("aim", "Míření", dep=["loading"], xp=25, items=[("createbigcannons:cannon_mount_extension", 1)], d=[
            "Lafeta míří pomocí rotace. Rotace zespodu otáčí dělem do stran. Rotace z boku ho zvedá a sklápí.",
            "S brýlemi (&eEngineer's Goggles&r) uvidíš na lafetě úhly děla i jeho sílu.",
            "Rozšíření lafety (&eCannon Mount Extension&r) přidá další místa pro připojení. Šipka na jeho boku ukazuje, ke které lafetě patří.",
            "&aTip:&r Pevná lafeta (&eFixed Cannon Mount&r) nepotřebuje rotaci. Úhel se jí nastaví na bocích a míří pořád na stejné místo.",
        ]),
        Q("worm", "Bezpečné nabíjení", dep=["loading"], xp=30, items=[("createbigcannons:worm", 1)], d=[
            "Když je nálož moc slabá, střela uvízne v hlavni. Vytáhneš ji vytahovákem (&eWorm&r) z hlavice (&eWorm Head&r) a dvou klacků.",
            "Každý kov potřebuje určitou sílu nálože na každý kus hlavně. Litina potřebuje 1 nálož na každý kus. Počítá se i kus, ve kterém leží střela.",
            "&cDělo může prasknout, když: dáš víc náloží, než vydrží; nálož leží v hlavni místo v komoře; střela v hlavni do něčeho narazí.&r",
            "&cMezi náložemi nenechávej mezery. Jinak nemusí shořet všechny.&r",
            "{@pagebreak}",
            "&aTip:&r Náboje zatopené vodou nevybuchnou od ohně ani od výbuchu. Mokrá nálož je ale slabší a jako první nálož v děle nevzplane.",
            "Mokrá nálož časem sama vyschne. V &eNetheru&r je hned po položení suchá.",
        ]),
        Q("loader", "Nabíjecí stroj", dep=["loading"], xp=30,
          items=[("createbigcannons:cannon_loader", 1), ("createbigcannons:ram_head", 1)], d=[
            "Teď už nemusíš nabíjet ručně – zvládne to stroj.",
            "Nabíječ (&eCannon Loader&r) funguje jako mechanický píst. Prodlužuje se prodlužovacími ojnicemi (&ePiston Extension Pole&r) a na konec potřebuje beranidlo (&eRam Head&r).",
            "Nabíječ, náboje a dělo musí ležet v jedné řadě. Před nabíjením musí být dělo rozložené.",
            "&aTip:&r S hlavicí vytahováku (&eWorm Head&r) nabíječ vytáhne uvízlou střelu. Nabíjet umí i mechanický píst, portálový jeřáb (&eGantry Carriage&r) nebo lanová kladka (&eRope Pulley&r).",
        ]),
        Q("carriage", "Pojízdná lafeta", dep=["wrought"], xp=25, optional=True,
          items=[("createbigcannons:cannon_carriage", 1)], d=[
            "Pojízdná lafeta (&eCannon Carriage&r) je dělo na kolech. Dá se s ní jezdit, ale nedá se automatizovat.",
            "Vyrobíš ji z prken, hřídele a dvou párů kol (&ePair of Cannon Wheels&r).",
            "Klikni na ni montážním klíčem a sestaví se nebo rozloží. Střílí se klávesou &eFire Controlled Cannon&r (najdeš ji v ovládání).",
        ]),
        Q("cast_iron", "Litina", dep=["worm", "create:burner"], xp=30,
          items=[("createbigcannons:cast_iron_ingot", 16)], d=[
            "Teď už železné dělo nestačí – vydrží jen 1 nálož. Litinové vydrží 2, takže dostřelí dál.",
            "Litina (&eCast Iron Ingot&r) se ale nedá skládat na stole. Díly se z ní odlévají do forem.",
            "Vyrobíš ji mechanickým lisem nad tyglíkem (&eBasin&r). Pod tyglíkem musí hořet ohňohořák (&eBlaze Burner&r). Do tyglíku dej železný ingot a uhlí.",
            "&aTip:&r Železný blok a uhelný blok dají rovnou litinový blok.",
        ]),
        Q("foundry", "Tavení kovu", dep=["cast_iron", "create:fluids"], xp=30, items=[("createbigcannons:basin_foundry_lid", 1)], d=[
            "Víko slévárny (&eBasin Foundry Lid&r) změní tyglík na tavicí pec. Vyrobíš ho ze 4 andezitových slitin.",
            "Polož víko na tyglík a pod tyglík ohňohořák. Musí hořet, jinak se nic neroztaví.",
            "Hoď do tyglíku litinu. Z každého ingotu je 90 mB tekuté litiny. Čerpadlem (&eMechanical Pump&r) ji odvedeš trubkami.",
        ]),
        Q("moulds", "Formy a licí písek", dep=["foundry", "create:drill"], xp=40,
          items=[("createbigcannons:casting_sand", 16), ("createbigcannons:very_small_cast_mould", 1),
                 ("createbigcannons:medium_cast_mould", 1), ("createbigcannons:cannon_end_cast_mould", 1)], d=[
            "Dřevěné formy vyřežeš z kmenů na mechanické pile (&eMechanical Saw&r). Filtrem na pile vybereš, kterou formu chceš.",
            "&eVery Small Cast Mould&r je na hlaveň, &eMedium Cast Mould&r na komoru a &eCannon End Cast Mould&r na uzávěr.",
            "Licí písek (&eCasting Sand&r) uděláš na stole ze 2 písků, hlíny a jílu.",
            "{@pagebreak}",
            "Polož formu a kolem ní 8 bloků licího písku (čtverec 3 × 3). Klikni na formu licím pískem a pak prázdnou rukou. Vznikne vrstva odlitku.",
            "Další vrstvy stav na sebe. Celé dělo tak odliješ najednou a bude spojené v jeden kus.",
            "Tekutý kov nalij shora trubkou. Hlaveň potřebuje 7 ingotů, komora 12 a uzávěr 9.",
            "{@pagebreak}",
            "Plný odlitek chvíli tuhne. Komparátor u něj ukáže, jak je plný. Hotový odlitek otevřeš kliknutím nebo rozbitím.",
            "&cOdlitý díl děla se po rozbití bez krumpáče s Hedvábným dotekem rozpadne na nugety. Dělo přesouvej stroji z Create (ložisko, píst), aby zůstalo vcelku.&r",
        ]),
        Q("drill", "Vyvrtej dělo", s="Pokročilý", dep=["moulds", "create:bearing"], xp=60, shape="hexagon", size=1.5,
          items=[("createbigcannons:cannon_drill", 1)], d=[
            "Odlitá hlaveň a komora jsou uvnitř plné. Vyvrtáš je vrtačkou (&eCannon Drill&r).",
            "Dělo připevni na mechanické ložisko (&eMechanical Bearing&r). To je soustruh, který dělem točí. Proti ústí postav vrtačku a prodluž ji prodlužovacími ojnicemi (&ePiston Extension Pole&r).",
            "Vrtačka potřebuje rotaci a vodu. Musí se točit stejně rychle nebo rychleji než soustruh. Při vrtání padají nugety. Uzávěr se nevrtá.",
            "{@pagebreak}",
            "Hotové litinové dělo: uzávěr, 2 komory a 2 kusy hlavně. Do komor dej 2 nálože, střelu před ně.",
            "&aTip:&r S brýlemi uvidíš v popisku bloku děla, kolik náloží vydrží.",
        ]),
        Q("welder", "Svářečka", dep=["drill", "create:brass"], xp=30, items=[("createbigcannons:cannon_welder", 1)], d=[
            "Díly děla položené rukou se nespojí. Svářečka (&eCannon Welder&r) spojí dva sousední díly.",
            "Klikni svářečkou pravým tlačítkem na dva sousední díly. Díly musí být ze stejného kovu a stejného typu děla.",
            "&cSvařené litinové dělo vydrží o 1 nálož méně.&r Lepší je dělo odlít celé. Bronz svařováním nezeslábne.",
        ]),
        Q("breech", "Posuvný závěr", dep=["drill"], xp=40,
          items=[("createbigcannons:cast_iron_sliding_breechblock", 1), ("createbigcannons:sliding_breech_cast_mould", 1)], d=[
            "Teď už nemusíš nabíjet přes ústí. Posuvný závěr (&eCast Iron Sliding Breech&r) se dává místo uzávěru a dělo nabíjíš zezadu.",
            "Odlij ho ve formě &eSliding Breech Cast Mould&r a vyvrtej. Pak do něj klikni klínem (&eCast Iron Sliding Breechblock&r). Teprve pak je hotový.",
            "Závěr otevřeš a zavřeš rotací. Do otevřeného závěru vlož náboje.",
            "&cPosuvný závěr vydrží jen omezený počet náloží: litinový 2, bronzový a ocelový 4. Ocelové dělo samo vydrží 8, s posuvným závěrem jen 4.&r",
        ]),
        Q("quickfire", "Rychlopalný závěr", dep=["breech"], xp=40, items=[("createbigcannons:quickfiring_mechanism", 1)], d=[
            "Teď už nemusíš závěr otvírat rotací – rychlopalný se otevře kliknutím.",
            "Mechanismus (&eQuick-Firing Mechanism&r) změní posuvný závěr na rychlopalný. Klikni s ním na závěr.",
            "Rychlopalný závěr otevřeš a zavřeš kliknutím na jeho bok. Nejdřív vlož střelu, pak nálož a závěr zavři.",
            "Prázdné nábojnice po výstřelu vyhodí sám. &cVydrží ale jen 2 nálože, ať je z jakéhokoli kovu.&r",
            "&aTip:&r Nabíjet ho umí mechanická paže (&eMechanical Arm&r). Montážním klíčem ho vrátíš na posuvný závěr.",
        ]),
        Q("big_cartridge", "Velká nábojnice", dep=["quickfire", "create:brass", "create:millstone"], xp=50,
          items=[("createbigcannons:big_cartridge", 1), ("createbigcannons:nitropowder", 4)], d=[
            "Teď už nemusíš do děla cpát několik pytlů prachu.",
            "Velká nábojnice (&eBig Cartridge&r) je rychlá nálož pro rychlopalný závěr. Do jednoho výstřelu se dává jen jedna.",
            "Ze 4 mosazných plátů uděláš na pracovním stole 4 plechy (&eBig Cartridge Sheet&r). Plech pak na pásu pod lisem 5× slisuješ (sekvenční montáž).",
            "Nábojnici na stole naplň nitroprachem (&eNitropowder&r). Víc prachu dá silnější výstřel, nejvýš 4 dávky.",
            "{@pagebreak}",
            "Nitroprach: v míchačce smíchej ohnivý prach (&eBlaze Powder&r), magmový krém (&eMagma Cream&r) a 2 střelné prachy. Vzniknou 2 kusy &eCongealed Nitro&r.",
            "Ten upeč v peci a výsledek umel mlýnským kamenem (&eMillstone&r). Z jednoho kusu jsou 2 nitroprachy.",
        ]),
        Q("guncotton", "Střelná bavlna", dep=["loading", "create:mixer"], xp=30,
          items=[("createbigcannons:packed_guncotton", 2)], d=[
            "Střelná bavlna (&eGuncotton&r) je silná výbušnina do granátů.",
            "V míchačce smíchej papír, střelný prach, redstone a 200 mB vody. Ohřev není potřeba.",
            "Lis nad tyglíkem slisuje 3 kusy na lisovanou střelnou bavlnu (&ePacked Guncotton&r).",
        ]),
        Q("he", "Výbušný granát", dep=["guncotton", "create:crafter"], xp=40, items=[("createbigcannons:he_shell", 1)], d=[
            "Výbušný granát (&eHigh Explosive (HE) Shell&r) vybuchne o něco silněji než TNT.",
            "Složí ho mechanický výrobník (&eMechanical Crafter&r) z 5 železných ingotů, 2 &ePacked Guncotton&r a dřevěné desky.",
            "Aby vybuchl, potřebuje zapalovač. Ten je v dalším questu.",
        ]),
        Q("fuze", "Zapalovače", dep=["he"], xp=30,
          items=[("createbigcannons:impact_fuze", 4), ("createbigcannons:timed_fuze", 4)], d=[
            "Zapalovač (&eFuze&r) určí, kdy granát vybuchne. Dej granát a zapalovač spolu do pracovního stolu.",
            "Nárazový zapalovač (&eImpact Fuze&r) vybuchne při nárazu, ale ne vždy. Je z kamenného tlačítka a redstonu. Časový (&eTimed Fuze&r) vybuchne po nastaveném čase. Čas nastavíš pravým tlačítkem. Je ze železného ingotu, hodin a redstonu. Oba recepty dají 4 kusy.",
            "&eInertia Fuze&r je spolehlivější nárazový. &eProximity Fuze&r vybuchne blízko bloku. &eWired Fuze&r odpálíš redstonem, za letu nevybuchne.",
            "&aTip:&r Zapalovač z položeného granátu sundáš pravým tlačítkem prázdnou rukou.",
        ]),
        Q("more_shells", "Další střely", dep=["fuze", "cast_iron"], xp=40,
          items=[("createbigcannons:ap_shot", 1), ("createbigcannons:shrapnel_shell", 1), ("createbigcannons:bag_of_grapeshot", 1)], d=[
            "Teď už jen plná střela nestačí – každý cíl chce jinou střelu.",
            "Průbojná střela (&eArmor Piercing (AP) Shot&r) prorazí víc bloků. Je z litiny, železa a desky.",
            "Šrapnel (&eShrapnel Shell&r) po výbuchu rozhází kuličky do šířky. Potřebuje zapalovač.",
            "Kartáč (&eBag of Grapeshot&r) se hned po výstřelu rozsype na kuličky. Ničí měkké bloky, třeba dřevo.",
            "Kuličky (&eShot Balls&r) uděláš z 8 železných nugetů a 1 železného ingotu, dostaneš 2. &aTip:&r JEI ukáže i kouřový granát a granát s tekutinou.",
        ]),
        Q("bronze", "Bronzové dělo", dep=["breech"], xp=40, optional=True,
          items=[("createbigcannons:bronze_sliding_breechblock", 1)], d=[
            "Bronzové dělo vydrží 4 nálože a svařováním nezeslábne.",
            "Bronz (&eBronze Ingot&r) uděláš v míchačce s ohřevem z mědi, zinku a uškvařené mouky (&eCinder Flour&r). Jde to i ze 2 mosazí a uškvařené mouky. Vzniknou vždy 2 ingoty.",
            "Roztav ho, odlij a vyvrtej stejně jako litinu. Bronz potřebuje 2 nálože na každé 3 kusy hlavně.",
            "Posuvný závěr z bronzu dokončíš klínem &eBronze Sliding Breechblock&r.",
        ]),
        Q("screw", "Šroubový závěr", dep=["breech"], xp=50,
          items=[("createbigcannons:steel_screw_lock", 1), ("createbigcannons:screw_breech_cast_mould", 1)], d=[
            "Teď už posuvný závěr nestačí – dělo s ním vydrží nejvýš 4 nálože. Šroubový závěr dělo neoslabí.",
            "Ocel (&eSteel Ingot&r) je nejlepší běžný kov na děla. V míchačce s ohřevem vzniknou ze 2 železných ingotů a uhlí 2 ocelové ingoty. Je to stejná ocel jako z Mekanismu.",
            "Šroubový závěr (&eSteel Screw Breech&r) odlij z oceli ve formě &eScrew Breech Cast Mould&r a vyvrtej. Pak do něj klikni zámkem (&eSteel Screw Lock&r).",
            "Odemkneš ho rotací. Pak ho odsuň Create strojem, dělo nabij a závěr zase zavři.",
        ]),
        Q("builder", "Ocelové dělo", s="Expert", dep=["screw", "create:fan"], xp=80, shape="hexagon", size=1.5,
          items=[("createbigcannons:cannon_builder", 1), ("createbigcannons:small_cast_mould", 1)], d=[
            "Teď už odlití nestačí – ocelová hlaveň a komora se skládají z vrstev. Každou vrstvu odlij z oceli a vyvrtej.",
            "Ocelová hlaveň je 1 vrstva (velmi malá). Ocelová komora má 3 vrstvy: velmi malou, malou a střední.",
            "Stavěč (&eCannon Builder&r) zasouvá vrstvy do sebe. Funguje jako píst s prodlužovacími ojnicemi. Redstonovým pulzem přepneš, jestli vrstvu drží.",
            "{@pagebreak}",
            "Složené vrstvy zahřej: větrák (&eEncased Fan&r) fouká přes lávu na vrstvy. Za chvíli se změní v hotový díl děla.",
            "Ocel potřebuje jen 1 nálož na 2 kusy hlavně. Se šroubovým závěrem vydrží 8 náloží.",
            "JEI v kategorii &eCannon Building&r ukáže vrstvy i pro silnější díly.",
        ]),
        Q("nethersteel", "Nethersteelové dělo", dep=["builder"], xp=100,
          items=[("createbigcannons:nethersteel_ingot", 8), ("createbigcannons:nethersteel_screw_lock", 1)], d=[
            "Teď už ani ocel nestačí – vydrží 8 náloží. Nethersteel (&eNethersteel Ingot&r) vydrží 10 a potřebuje jen 1 nálož na 3 kusy hlavně. Do děla z něj dáš nejvíc náloží.",
            "V míchačce smíchej netheritový šrot (&eNetherite Scrap&r) a 8 litinových ingotů (nebo 4 ocelové). Ohňohořák musí být přehřátý – nakrm ho ohňodortem (&eBlaze Cake&r). Vznikne 8 ingotů.",
            "Díly se dělají stejně jako ocelové: roztavit, odlít vrstvy, vyvrtat, složit stavěčem a zahřát.",
            "Šroubový závěr z nethersteelu dokončíš zámkem &eNethersteel Screw Lock&r. &cNethersteel nejde svařovat, dělo musí vzniknout vcelku.&r",
        ]),
        Q("ap_shell", "Průbojný granát", dep=["more_shells", "create:drill"], xp=60,
          items=[("createbigcannons:ap_shell", 1), ("createbigcannons:inertia_fuze", 2)], d=[
            "Teď už nemusíš volit mezi průrazem a výbuchem. Průbojný granát (&eArmor Piercing (AP) Shell&r) prorazí bloky a vybuchne až uvnitř opevnění.",
            "Složí ho mechanický výrobník z litiny, železa, &ePacked Guncotton&r a desky.",
            "Zapalovač se mu dává zespodu. Proto použij setrvačný zapalovač (&eInertia Fuze&r), který funguje i zespodu. Nárazový zapalovač tam nefunguje.",
            "Setrvačný zapalovač je z kamenného tlačítka, vratné pružiny (&eRecoil Spring&r) a redstonu. Pružinu uděláš z pružinového drátu (&eSpring Wire&r): pila ho nařeže ze železného plátu a lis ho 3× slisuje (sekvenční montáž).",
        ]),
        Q("autocannon", "Autokanón", dep=["drill"], xp=50,
          items=[("createbigcannons:autocannon_barrel_cast_mould", 1), ("createbigcannons:autocannon_breech_cast_mould", 1),
                 ("createbigcannons:cast_iron_autocannon_breech_extractor", 1)], d=[
            "Teď už nemusíš po každém výstřelu nabíjet. Autokanón střílí rychle malými náboji. Formy na jeho díly vyřežeš z kmenů na pile.",
            "Do malých forem stačí kliknout licím pískem, čtverec písku kolem není potřeba. Odlitou hlaveň a závěr vyvrtej.",
            "Do závěru pak klikni vyhazovačem (&eCast Iron Autocannon Breech Extractor&r). Ten vznikne na pile z litinového ingotu (sekvenční montáž).",
            "{@pagebreak}",
            "Autokanón postav na lafetu. Může být dlouhý nejvýš 3 bloky včetně závěru (bronzový 5, ocelový 7).",
            "Střílí, dokud má signál v plošce s hořícím dělem. Silnější signál = rychlejší střelba.",
        ]),
        Q("ac_ammo", "Náboje do autokanónu", dep=["autocannon", "create:brass"], xp=40,
          items=[("createbigcannons:machine_gun_round", 16), ("createbigcannons:autocannon_ammo_container", 1)], d=[
            "Nejlevnější náboj je kulometný (&eMachine Gun Round&r). Hodí se hlavně na tvory.",
            "Pila rozřeže plát (železný, měděný nebo mosazný) na &eAutocannon Cartridge Sheet&r. Další řez dá 4 prázdné náboje. Na stole k nim přidej střelný prach a měděný nugget.",
            "Zásobník (&eAutocannon Ammo Container&r) vyrobíš z mosazného ingotu a železných plátů. Naplníš ho v jeho menu. Klikni s ním pravým tlačítkem na závěr a vložíš ho do autokanónu.",
            "&aTip:&r Silnější náboj: na stole spoj plnou nábojnici (&eFilled Autocannon Cartridge&r) s &eFlak Autocannon Round&r nebo &eArmor Piercing (AP) Autocannon Round&r. Nábojnici uděláš z plechu: lis ho 6× slisuje a pokladač do něj přidá střelný prach.",
        ]),
    ],
)

# Přepsané původní questy kapitoly create_addons (úkoly beze změny).
ORIG_CANNONS = {
    "cannon": Q("cannon", "Lafeta děla", s="Create Big Cannons", dep=["start", "create:sheets"], xp=40,
                items=[("createbigcannons:cannon_mount", 1)], d=[
        "&bCreate Big Cannons&r přidává obří děla, která se staví z bloků.",
        "Lafeta (&eCannon Mount&r) drží dělo, míří s ním a odpaluje ho. Vyrobíš ji ze železných plátů, hřídelí, andezitového pouzdra a střelného prachu.",
        "&aVíc najdeš v kapitole Velká děla.&r",
    ]),
    "shot": Q("shot", "Střely a nálože", dep=["cannon", "create:mixer"], xp=40,
              items=[("createbigcannons:solid_shot", 4), ("createbigcannons:powder_charge", 4)], d=[
        "Dělo potřebuje střelu a za ní prachové nálože. Víc náloží = delší dostřel, ale dělo jich vydrží jen omezeně.",
        "Plná střela (&eSolid Shot&r) je ze železných ingotů, nugetů a dřevěné desky.",
        "Nálož (&ePowder Charge&r) vznikne z prázdného pytlíku (&eEmpty Powder Charge&r) a lisovaného prachu (&ePacked Gunpowder&r). Pytlík je z vlny a dvou provázků. Lis nad tyglíkem slisuje 3 střelné prachy na lisovaný prach.",
        "&aVíc najdeš v kapitole Velká děla.&r",
    ]),
}


# ======================================================================
# Kapitola POHYB A VÝBAVA
# ======================================================================
# Kapitola: Pohyb a výbava (Hypertubes, Teleporters, Stuff 'N Additions, Mechanical Companion,
# Escalated, Aquatic Ambitions). Vstupní původní questy jsou v kapitole create_addons (ORIG níže).
# Každá linka: Začátečník -> Pokročilý -> Expert (milníky hexagon s podnázvem úrovně).

LVL1, LVL2, LVL3 = "Začátečník", "Pokročilý", "Expert"

CADD_GEAR = dict(
    key="cadd_gear", group="create", title="Pohyb a výbava",
    subtitle="Hypertrubky, teleporty, jetpacky a mechanický vlk", icon="create_sa:brass_jetpack_chestplate",
    quests=[
        Q("start", "Pohyb a výbava", s="Cestování a vybavení s Create", icon="create_sa:brass_jetpack_chestplate",
          tasks=[auto()], dep=["create_addons:start"], xp=10, d=[
            "Tahle kapitola ukazuje doplňky Create pro rychlé cestování a pro tvou výbavu.",
            "&bCreate: Hypertubes&r – trubky, které tě přenesou po základně. &bCreate: Teleporters&r – teleporty pro hráče, předměty, bloky a velké portály.",
            "&bCreate Stuff 'N Additions&r – jetpacky, exoskelety, drony a plamenomet. &bCreate: Mechanical Companion&r – mechanický vlk, který tě chrání.",
            "&bCreate: Escalated&r – pohyblivé chodníky a eskalátory. &bCreate: Aquatic Ambitions&r – klec pro konduit a nový druh zpracování větrákem.",
            "Každá linka vede od začátečníka přes pokročilého až po experta. Úrovně poznáš podle šestiúhelníků. &aPrvní quest hypertrubek, teleportů, jetpacku, dronu a vlka je v kapitole Create: doplňky.&r",
            "{@pagebreak}",
            "&ePojmy, které tu potkáš:&r",
            "&eRPM&r = otáčky za minutu, tedy jak rychle se hřídel točí. &emB&r = tisícina kbelíku kapaliny (1000 mB = 1 kbelík).",
            "&eSekvenční montáž&r = výroba po krocích. Předmět jede po pásu pod stroji a každý stroj přidá jeden krok. Přesné kroky ukáže JEI.",
            "Pokladač (&eDeployer&r) přikládá předměty, dávkovač (&eSpout&r) plní kapalinou. Mechanický výrobník (&eMechanical Crafter&r) skládá velké recepty, které se na pracovní stůl nevejdou.",
        ]),

        # ---------------- HYPERTUBES (začátek: původní quest hypertube)
        Q("ht_accel", "Urychlovač", icon="create_hypertube:hypertube_accelerator",
          dep=["start", "create_addons:hypertube", "create:precision"], items=[("create_hypertube:hypertube_accelerator", 1)], xp=30, d=[
            "Urychlovač (&eHypertube Accelerator Block&r) zrychlí každého, kdo jím projíždí. Hodí se hlavně na dlouhé trasy.",
            "Vyrobíš ho z precizního strojku, dvou trychtýřů (&eHypertube Funnel&r) a dvou ozubených koleček. Zapoj ho do trasy a roztoč ho jako ozubené kolečko.",
            "&aKlíčem ho přepneš do režimu brzdy (&eBrake Mode&r). Pak cestující naopak zpomalí, třeba před cílem.&r",
        ]),
        Q("ht_split", "Rozbočovač", s=LVL2, icon="create_hypertube:hypertube_junction", **M,
          dep=["ht_accel", "create:crafter"], items=[("create_hypertube:hypertube_junction", 1)], xp=40, d=[
            "Teď už jedna rovná trasa nestačí – postavíš síť. Rozbočovač (&eHypertube Splitter&r) spojí až tři trubky, takže se trasa větví.",
            "Vyrobíš ho v mechanickém výrobníku ze dvou mosazných plátů, vysílače, trubky a tří trychtýřů.",
            "Když jím projíždíš, směr vybereš klávesami pro chůzi. Klíčem přepneš režimy, ve kterých posílá cestující vždy stejnou cestou.",
            "&aTrubkami cestují i vesničané, krávy, prasata, ovce, slepice, některé ryby a balíčky z Create.&r",
        ]),
        Q("ht_scanner", "Chytrá síť", s=LVL3, icon="create_hypertube:tube_scanner_attachment", **M,
          dep=["ht_split", "create:deployer"], items=[("create_hypertube:tube_scanner_attachment", 1), ("create_hypertube:redstone_detector_tube_attachment", 1)], xp=60, d=[
            "Teď už síť nebudeš přepínat ručně – řídí ji redstone. Senzory se vkládají do vstupů, urychlovačů a rozbočovačů, klidně na víc stran najednou.",
            "Redstonový detektor (&eRedstone Detector Tube Attachment&r) přepíná redstonovým signálem režim urychlovače nebo vstupu. U rozbočovače přepíná mezi oběma pevnými směry.",
            "Skener (&eTube Scanner Attachment&r) vyrobíš sekvenční montáží z detektoru: mosazný plát, elektronka a znovu mosazný plát. Když trubkou někdo jede, vyšle signál 8 (mládě) nebo 15 (dospělý).",
            "&aSignál ze skeneru můžeš vést do detektoru u rozbočovače nebo urychlovače. Tak síť sama rozhodne, kam koho pošle.&r",
        ]),

        # ---------------- TELEPORTERS
        Q("tp_pearl", "Redstonová perla", s=LVL1, icon="createteleporters:redstone_pearl", **M,
          dep=["start", "create:burner"], items=[("createteleporters:redstone_pearl", 2)], xp=25, d=[
            "&bCreate: Teleporters&r přidává teleporty pro hráče, předměty i bloky. Všechny potřebují redstonovou perlu (&eRedstone Pearl&r).",
            "Perlu vyrobíš v mechanické míchačce nad zapáleným ohňohořákem (&eBlaze Burner&r): enderová perla a růženín (&eRose Quartz&r).",
            "&aPerel budeš potřebovat hodně – do teleportérů, odkazů i portálů.&r",
        ]),
        Q("tp_mech", "Kvantový mechanismus", icon="createteleporters:quantum_mechanism",
          dep=["tp_pearl", "create:spout"], items=[("createteleporters:quantum_mechanism", 1)], xp=50, d=[
            "Perla sama teleport neudělá. Srdce každého teleportéru je kvantový mechanismus (&eQuantum Mechanism&r) a ten potřebuje teleportační šťávu (&eQuantum Fluid&r, v popiscích &eTelejuice&r).",
            "Šťáva: v míchačce nad zapáleným ohňohořákem smíchej plod chorusu (&eChorus Fruit&r) a 250 mB vody. Chorus roste v &eEndu&r.",
            "Pokročilý díl (&eAdvanced Component&r): sekvenční montáží nasaď na diamant robustní plát (&eSturdy Sheet&r), pak redstonovou perlu a nakonec ho slisuj.",
            "Mechanismus: robustní plát naplň 250 mB šťávy, nasaď na něj pokročilý díl a slisuj. &aPak si vyrob teleportér z kapitoly Create: doplňky.&r",
        ]),
        Q("tp_link", "Odkaz a první skok", icon="createteleporters:tp_link",
          dep=["tp_mech", "create_addons:teleporter"], items=[("createteleporters:tp_link", 1)], xp=40, d=[
            "Teleportér bez cíle nikam nevede. Cíl si pamatuje odkaz (&eTp Link&r). Vyrobíš ho z vysílače, redstonové perly, mosazného plátu a pokročilého dílu.",
            "Jdi na cílové místo a klikni odkazem pravým tlačítkem na blok. Nad ním nech volné místo. Pak odkaz vlož do teleportéru.",
            "Do teleportéru napumpuj šťávu, každý skok spotřebuje 250 mB. Stoupni si na něj a počkej, až se nabije.",
            "&cCíl musí být ve stejné dimenzi a v dosahu (výchozí je 450 bloků). Vzdálenost uvidíš v okně teleportéru.&r",
        ]),
        Q("tp_item", "Teleport předmětů", s=LVL2, icon="createteleporters:item_tp", **M,
          dep=["tp_link"], items=[("createteleporters:item_tp", 1)], xp=40, d=[
            "Teď už neteleportuješ jen sebe, ale i náklad. Teleport předmětů (&eItem Teleporter&r) pošle celý stoh předmětů na uložené místo a přijímač nepotřebuje.",
            "Vyrobíš ho z mosazných pouzder, šachet, sudů a kvantového mechanismu. Vlož do něj odkaz a předměty a pošli do něj redstonový pulz.",
            "Předměty vypadnou nad uloženým blokem, tak tam dej násypku a truhlu. Stoh 64 kusů stojí 100 mB šťávy. Výchozí dosah je 500 bloků ve stejné dimenzi.",
        ]),
        Q("tp_advlink", "Rozšířený odkaz", icon="createteleporters:adv_tplink",
          dep=["tp_item"], items=[("createteleporters:adv_tplink", 1), ("createteleporters:quantum_casing", 8)], xp=50, d=[
            "Obyčejný odkaz už nestačí na portály ani na přesun bloků. Rozšířený odkaz (&eAdvanced Tp Link&r) vyrobíš ze dvou vysílačů, redstonové perly, kvantového pouzdra a kvantového mechanismu.",
            "Kvantové pouzdro (&eQuantum Casing&r) vznikne, když vlakové pouzdro (&eTrain Casing&r) naplníš dávkovačem 1000 mB šťávy. Z pouzder se staví rám portálu.",
            "&aZ teleportu předmětů, kvantových pouzder, kvantového mechanismu, pokladačů a pokročilého dílu vyrobíš teleport bloků (&eBlock Teleporter&r). Na redstonový signál přenese blok před sebou na místo uložené rozšířeným odkazem. Spotřebuje 1000 mB šťávy.&r",
        ]),
        Q("tp_portal", "Kvantový portál", s=LVL3, icon="createteleporters:custom_portal_base", **M,
          dep=["tp_advlink", "create:crafter"], items=[("createteleporters:custom_portal_base", 2)], xp=100, d=[
            "Teď už tě nebrzdí dosah ani dimenze. Ovladač portálu (&eCustom Portal Controller&r) postaví portál bez omezení dosahu, i do jiné dimenze. Recept v mechanickém výrobníku dá rovnou dva.",
            "Postav obdélníkový rám z kvantových pouzder. Vnitřek musí mít na šířku i na výšku 3 až 21 bloků a musí být prázdný. Ovladač dej do spodní řady rámu.",
            "Po obou stranách ovladače nech jeden volný blok, doplní se sám. Rám musí být celý, i s rohy.",
            "{@pagebreak}",
            "Oba ovladače přepni do režimu &ePortal to portal&r a klikni na oba stejným rozšířeným odkazem. Potom ten odkaz vlož do jednoho z nich.",
            "Do každého ovladače napumpuj aspoň 256 mB šťávy. Při cestě se šťáva bere z portálu, kterým odcházíš.",
            "&aPortálem projede i vlak. Oba konce ale musí být v režimu Portal to portal.&r",
        ]),

        # ---------------- STUFF 'N ADDITIONS
        Q("sa_heat", "Tepelný motor", s=LVL1, icon="create_sa:heat_engine", **M,
          dep=["start", "create:deployer"], items=[("create_sa:heat_engine", 1)], xp=30, d=[
            "&bCreate Stuff 'N Additions&r přidává jetpacky, exoskelety, drony a další výbavu. Základem jsou malé motory a začíná se tím nejjednodušším.",
            "Tepelný motor (&eHeat Engine&r) vyrobíš sekvenční montáží. Na andezitovou slitinu pokladač nasadí ozubené kolečko, velké ozubené kolečko, zinkový a měděný nuget. Celé se to opakuje třikrát.",
            "&aTepelný motor pohání výbavu na palivo: andezitový jetpack, andezitový exoskelet a plamenomet (&eFlamethrower&r), který střílí oheň a slouží i jako přenosná pec.&r",
        ]),
        Q("sa_andesite_jet", "Andezitový jetpack", icon="create_sa:andesite_jetpack_chestplate",
          dep=["sa_heat", "create:crafter"],
          items=[("create_sa:andesite_jetpack_chestplate", 1), ("create_sa:small_fueling_tank", 1)], xp=50, d=[
            "Andezitový jetpack (&eAndesite Jetpack&r) je první jetpack tohoto modu. Skládá se v mechanickém výrobníku a létá na palivo.",
            "Ve vzduchu drž mezerník a letíš. Shift + mezerník zapne vznášení. Mezerník ve vodě zapne rychlé plavání.",
            "Palivová nádrž (&eSmall Fueling Tank&r) se plní pravým kliknutím na lávu. Když ji máš v inventáři, sama dobíjí výbavu na palivo.",
            "&aNouzově: vezmi jetpack do druhé ruky a vyhoď na zem uhlí. Větší nádrž vyrobíš, když menší obložíš 4 robustními pláty (&eSturdy Sheet&r).&r",
        ]),
        Q("sa_hydraulic", "Hydraulický motor", icon="create_sa:hydraulic_engine",
          dep=["sa_andesite_jet", "create:spout"], items=[("create_sa:hydraulic_engine", 1)], xp=30, d=[
            "Palivo už umíš. Druhým pohonem je voda pod tlakem. Využívá ji hydraulický motor (&eHydraulic Engine&r).",
            "Vyrobíš ho sekvenční montáží: měděný plát naplň dávkovačem 250 mB vody a dvakrát ho slisuj. Celé se to opakuje třikrát.",
            "&aZ hydraulického motoru vyrobíš měděný jetpack, měděný exoskelet a chytač bloků (&eBlock Picker&r).&r",
        ]),
        Q("sa_copper_jet", "Měděný jetpack", icon="create_sa:copper_jetpack_chestplate",
          dep=["sa_hydraulic"],
          items=[("create_sa:copper_jetpack_chestplate", 1), ("create_sa:small_filling_tank", 1)], xp=40, d=[
            "Měděný jetpack (&eCopper Jetpack&r) místo paliva potřebuje vodu. Vyrobíš ho na obyčejném pracovním stole.",
            "Plnicí nádrž (&eSmall Filling Tank&r) vyrobíš z nádrže z Create. Plní se pravým kliknutím na vodu a v inventáři sama doplňuje výbavu na vodu.",
            "&aOvládá se stejně jako andezitový jetpack. Nouzově ho doplníš kbelíkem vody: jetpack do druhé ruky a kbelík vyhoď.&r",
        ]),
        Q("sa_steam", "Parní motorek", s=LVL2, icon="create_sa:steam_engine", **M,
          dep=["sa_copper_jet"], items=[("create_sa:steam_engine", 1)], xp=40, d=[
            "Teď už jeden pohon nestačí – mosazná výbava spojí vodu i palivo a dělá z nich páru. Potřebuje parní motorek z tohoto modu (&eSteam Engine&r).",
            "&cNepleť si ho s velkým parním strojem z Create – tohle je jen součástka.&r",
            "Vyrobíš ho sekvenční montáží. Na mosazný plát pokladač nasadí ozubené kolečko, velké ozubené kolečko, vrtuli a andezitovou slitinu. Celé se to opakuje třikrát.",
            "&aZ parního motorku vyrobíš mosazný jetpack (quest v kapitole Create: doplňky), mosazný exoskelet a přenosný vrták (&ePortable Drill&r).&r",
        ]),
        Q("sa_netherite_jet", "Netheritový jetpack", s=LVL3, icon="create_sa:netherite_jetpack_chestplate", **M,
          dep=["sa_steam", "create_addons:sa_jetpack"], items=[("create_sa:netherite_jetpack_chestplate", 1)], xp=80, d=[
            "Nejlepší jetpack modu. Netheritový jetpack (&eNetherite Jetpack&r) je vylepšený mosazný jetpack a jako předmět neshoří v ohni ani v lávě.",
            "Vyrobíš ho na kovářském stole: mosazný jetpack a netheritový ingot. Místo šablony tam dej nádrž (&eFluid Tank&r) z Create.",
            "&aStejně jako mosazný potřebuje vodu i palivo. Nos u sebe plnicí i palivovou nádrž a o doplňování se nestaráš.&r",
        ]),
        Q("sa_drone_mod", "Moduly dronu", icon="create_sa:vault_component",
          dep=["sa_steam", "create_addons:sa_drone"], items=[("create_sa:vault_component", 1)], xp=40, d=[
            "Holý dron tě jen sleduje. Užitečný bude, až mu nasadíš modul: klikni na dron pravým tlačítkem s dílem v ruce.",
            "Trezorový díl (&eVault Component&r) vyrobíš z trezoru z Create a dá dronu úložiště. Mosazná vrtací hlava (&eBrass Drill Head&r) z něj udělá těžaře.",
            "Dál můžeš nasadit měděný magnet (&eCopper Magnet&r) nebo díl s vrtulí (&eFan Component&r). Ovladačem dronu moduly zapínáš a vypínáš.",
        ]),
        Q("sa_exo", "Exoskelet", icon="create_sa:andesite_exoskeleton_chestplate", optional=True,
          dep=["sa_heat", "create:crafter"], items=[("create_sa:andesite_exoskeleton_chestplate", 1)], xp=40, d=[
            "Exoskelet nosíš místo hrudního plátu a dává ti efekty navíc. Spotřebovává přitom palivo nebo vodu.",
            "Andezitový (&eAndesite Exoskeleton&r) běží na palivo: rychleji těžíš (Spěch II), ale slaběji útočíš (Slabost). Měděný (&eCopper Exoskeleton&r) běží na vodu: silněji útočíš (Síla II), ale pomaleji těžíš.",
            "Mosazný (&eBrass Exoskeleton&r) dává Spěch i Sílu a potřebuje palivo i vodu. Na kovářském stole ho stejně jako jetpack vylepšíš na netheritový.",
        ]),

        # ---------------- MECHANICAL COMPANION (začátek: původní quest wolf)
        Q("wolf_proc", "Procesor vlka", icon="createmechanicalcompanion:mechanical_wolf_processor",
          dep=["start", "create_addons:wolf"], items=[("createmechanicalcompanion:mechanical_wolf_processor", 1)], xp=40, d=[
            "Základní deska je jen tělo. Mozek vlka je procesor (&eMechanical Wolf Processor&r). Vznikne, když pokladač nasadí na základní desku optický senzor (&eOptical Sensor&r).",
            "Růženínovou čočku (&eRose Quartz Lens&r) vybrousíš šmirglpapírem z elektronky. Senzor pak vyrobíš sekvenční montáží: andezitové pouzdro dvakrát slisuj a nasaď na něj čočku.",
            "&aZákladní desku, senzor i čočku najdeš také v truhlách stavby &eIllager Workshop&a.&r",
        ]),
        Q("wolf_link", "Přivolej vlka", icon="createmechanicalcompanion:mechanical_wolf_link",
          dep=["wolf_proc", "create:crafter"], items=[("createmechanicalcompanion:mechanical_wolf_link", 1)], xp=60, d=[
            "Odkaz (&eMechanical Wolf Link&r) přivolá vlka. Vyrobíš ho v mechanickém výrobníku z mosazných plátů, andezitové slitiny, precizního strojku, procesoru a redstonového vysílače.",
            "Nasaď si ho do slotu doplňků na hlavu (&eCurios&r). Objeví se vlk a bude tě chránit. Pravým kliknutím na vlka otevřeš jeho moduly.",
            "Zraněného vlka opravíš montážním klíčem. Když vlk zemře, po chvíli se znovu objeví i se svými moduly.",
        ]),
        Q("wolf_mod", "První moduly", s=LVL2, icon="createmechanicalcompanion:reinforced_plates", **M,
          dep=["wolf_link"],
          items=[("createmechanicalcompanion:reinforced_plates", 1), ("createmechanicalcompanion:mounted_crossbow", 1)], xp=50, d=[
            "Teď už vlk jen nekouše – dostane výbavu. Vlk má 1 slot na obranu, 3 na útok, 2 na pohyb a 3 na užitečné věci.",
            "Obrana: zesílené pláty (&eReinforced Plates&r) z mosazi a štítu. Útok: namontovaná kuše (&eMounted Crossbow&r) z precizního strojku, obyčejné kuše a mosazi. Střílí jen na cíl vlka.",
            "&aDalší útočné moduly: teslův ocas (&eTesla Tail&r) zraní, kdo vlka napadne. Ohnivé tesáky (&eSmelting Fangs&r) zapalují a chrání vlka před ohněm.&r",
        ]),
        Q("wolf_full", "Plně vybavený vlk", s=LVL3, icon="createmechanicalcompanion:quantum_drive", **M,
          dep=["wolf_mod"],
          items=[("createmechanicalcompanion:netherite_plates", 1), ("createmechanicalcompanion:quantum_drive", 1),
                 ("createmechanicalcompanion:regenerative_casing", 1)], xp=100, d=[
            "Teď už zesílené pláty nestačí. Netheritové pláty (&eNetherite Plates&r) vzniknou, když pokladač nasadí netheritový ingot na zesílené pláty. Přidají zbroj, zdraví, odolnost proti odhození a ohni.",
            "Kvantový pohon (&eQuantum Drive&r) vlka teleportuje k cíli. Léčivé pouzdro (&eRegenerative Casing&r) vzniká nasazením precizního strojku na zesílené pláty a vlk se s ním sám léčí.",
            "&aObsaď všech 9 slotů: přidej raketu (&eBooster Rocket&r), světlo (&eMounted Light&r) a radar (&eMob Radar&r), který ukáže nepřátele i přes zdi.&r",
        ]),
        Q("wolf_workshop", "Najdi Illager Workshop", icon="createmechanicalcompanion:blueprint_painting", optional=True,
          dep=["wolf_proc"], tasks=[structure("createmechanicalcompanion:illager_workshop")], xp=50, d=[
            "Stavba &eIllager Workshop&r je plná strojů z Create. V jejích truhlách najdeš díly pro vlka.",
            "Objevuje se ve stejných biomech jako stavba &ePillager Outpost&r. Mapu k ní ti prodá kartograf (za 10 smaragdů a kompas) nebo potulný obchodník.",
            "&cHlídají ji &eIllager Engineer&c a &eIllager Supervisor&c s bramborovým dělem. Vezmi si dobrou zbroj.&r",
        ]),

        # ---------------- ESCALATED
        Q("esc_walkway", "Pohyblivý chodník", s=LVL1, icon="escalated:metal_walkway_steps", **M,
          dep=["start", "create:shaft", "create:sheets"], items=[("escalated:metal_walkway_steps", 4)], xp=30, d=[
            "&bCreate: Escalated&r přidává pohyblivé chodníky a eskalátory. Pohání je rotace z hřídelí, stejně jako stroje z Create.",
            "Kovové schody (&eMetal Walkway Steps&r) vyrobíš z řetězů a železných plátů. Dřevěné (&eWooden Walkway Steps&r) z řetězů a dřevěných desek.",
            "Polož dvě hřídele a klikni na obě pravým tlačítkem se schody v ruce. Mezi nimi vznikne chodník. Špatný výběr zrušíš Shiftem + pravým tlačítkem.",
            "&aChodník rozšíříš, když ho propojíš s hřídelí hned vedle. Kliknutím hřídelí na prostřední díl přidáš další pohon.&r",
        ]),
        Q("esc_escalator", "Eskalátor se zábradlím", s=LVL2, icon="create:belt_connector", **M,
          dep=["esc_walkway"], tasks=[adv("escalated:handrail")], xp=30, d=[
            "Teď už nejedeš jen po rovině, ale i nahoru. Eskalátor postavíš stejně jako chodník, jen hřídele jsou v různé výšce.",
            "Vodorovná vzdálenost hřídelí musí být o 3 bloky větší než výšková. Příklad: 4 bloky nahoru znamená 7 bloků dopředu.",
            "Zábradlí přidáš pravým kliknutím mechanickým pásem (&eMechanical Belt&r) na chodník nebo eskalátor. Nad ním musí být volné místo. Quest se splní, až zábradlí přidáš.",
            "&aSchody i zábradlí obarvíš barvivem a vodou barvu smyješ. Kliknutím blokem skla uděláš skleněné zábradlí.&r",
        ]),
        Q("esc_heaven", "Schody do nebe", s=LVL3, icon="escalated:wooden_walkway_steps", **M,
          dep=["esc_escalator"], tasks=[adv("escalated:escalator_100")], xp=60, d=[
            "Jeden eskalátor už máš. Teď postav celou věž: vystoupej o 100 bloků výš jen po jedoucích eskalátorech.",
            "Navazuj eskalátory na sebe. Každý potřebuje pohon na svých koncích. Doprostřed eskalátoru hřídel přidat nejde.",
            "&aInženýrské brýle (&eEngineer's Goggles&a) ukážou, jestli máš dost síly pro všechny eskalátory.&r",
        ]),

        # ---------------- AQUATIC AMBITIONS
        Q("aq_alloy", "Prismarinová slitina", icon="create_aquatic_ambitions:prismarine_alloy",
          dep=["start", "create:mixer"], items=[("create_aquatic_ambitions:prismarine_alloy", 4)], xp=25, d=[
            "&bCreate: Aquatic Ambitions&r přidává mechanickou klec pro konduit (&eConduit&r) a nový druh zpracování větrákem.",
            "Prismarinovou slitinu (&ePrismarine Alloy&r) vyrobíš v míchačce z prismarinu a měděného nugetu. Jde to i na pracovním stole: 2 prismariny a 2 měděné nugety dají 1 slitinu.",
            "&aDvě slitiny nad sebou na pracovním stole dají tyč (&ePrismarine Alloy Rod&r).&r",
        ]),
        Q("aq_cage", "Klec konduitu", s=LVL2, icon="create_aquatic_ambitions:mechanical_conduit", **M,
          dep=["aq_alloy"], items=[("create_aquatic_ambitions:mechanical_conduit", 1)], xp=60, d=[
            "Teď už nepotřebuješ velký prismarinový prstenec kolem konduitu. Klec konduitu (&eConduit Cage&r) ho nahradí jedním blokem.",
            "Vyrobíš ji z konduitu, 5 prismarinových tyčí, 2 slitin a potrubí. Konduit vyrobíš ze srdce moře a 8 ulit loděnky (&eNautilus Shell&r).",
            "Klec probudíš, když do ní zespodu napumpuješ kapalinu. S vodou dává efekt konduitu (&eConduit Power&r), jiné kapaliny dávají jiné efekty.",
            "&aVe slotu režimu vybereš, koho efekt zasáhne, třeba jen hráče nebo jen příšery.&r",
        ]),
        Q("aq_rock", "Podezřelý kámen", icon="create_aquatic_ambitions:suspicious_rock",
          dep=["aq_cage", "create:millstone"], items=[("create_aquatic_ambitions:suspicious_rock", 1)], xp=25, d=[
            "Klec umí i zpracovávat předměty. Nejcennější surovinou pro ni je podezřelý kámen (&eSuspicious Rock&r).",
            "Když v mlýnském kameni meleš vápenec (&eLimestone&r), dostaneš vápníkový prášek (&eCalcium Rich Powder&r) a s šancí 5 % i podezřelý kámen. Vápenec vznikne, když se láva potká s tekoucím medem.",
            "&aVápníkový prášek, štěrk a 100 mB lávy slisuj v tyglíku pod mechanickým lisem a dostaneš kalcit.&r",
        ]),
        Q("aq_shell", "Ostnatá lastura", s=LVL3, icon="create_aquatic_ambitions:spiky_shell", **M,
          dep=["aq_rock"], items=[("create_aquatic_ambitions:spiky_shell", 1)], xp=60, d=[
            "Teď už klec nejen dává efekty, ale i vyrábí. Větrák, který fouká skrz probuzenou klec, zpracovává předměty novým způsobem (&eConduit Channeling&r).",
            "Z podezřelého kamene tak dostaneš s šancí 50 % ulitu loděnky a s šancí 10 % ostnatou lasturu (&eSpiky Shell&r).",
            "Stejně vyrobíš srdce moře z oka Endu, prismarinové střepy z pazourku nebo oživíš mrtvé korály.",
            "&aZe 3 ostnatých lastur a 2 prismarinových tyčí vyrobíš trojzubec!&r",
        ]),
    ],
)

# Přepsané původní questy kapitoly create_addons (úkoly beze změny).
ORIG_GEAR = {
    "hypertube": Q("hypertube", "Hypertrubky", s="Rychlá doprava po základně", icon="create_hypertube:hypertube_entrance",
        dep=["start", "create:brass"],
        items=[("create_hypertube:hypertube", 16), ("create_hypertube:hypertube_entrance", 1)], xp=40, d=[
            "&bCreate: Hypertubes&r přidává trubky, které tě vysají a rychle přenesou jinam.",
            "Trubky (&eHypertube Block&r) vyrobíš z mosazných plátů a skleněných tabulí, 16 kusů najednou. Vstup (&eHypertube Entrance Block&r) složíš z trychtýře (&eHypertube Funnel&r), ozubeného kolečka a chytré šachty.",
            "Trychtýř je z mosazného plátu, trubky a sušené chaluhy.",
            "Stavba: polož trubku, klikni na ni pravým tlačítkem s další trubkou v ruce a druhou trubku polož jinde. Mezi nimi vznikne oblouk z trubek z tvého inventáře.",
            "Do vstupu vlezeš, když se u něj skrčíš (Shift). Vstup se musí točit aspoň 16 RPM (otáček za minutu). Čím rychleji se točí, tím rychleji cestuješ. Z trubky vyskočíš levým Shiftem.",
            "&aVíc najdeš v kapitole Pohyb a výbava.&r",
        ]),
    "teleporter": Q("teleporter", "Teleportér", s="Teleport pro hráče a moby", icon="createteleporters:teleporter",
        dep=["start", "create:deployer", "cadd_gear:tp_mech"],
        items=[("createteleporters:teleporter", 1)], xp=60, d=[
            "Teleportér (&eEntity Teleporter&r) z &bCreate: Teleporters&r přenese hráče a moby na uložené místo. Cílový teleportér nepotřebuješ.",
            "Vyrobíš ho z mosazných pouzder, redstonových perel, elektronek a kvantového mechanismu. Na kameníku z něj uděláš i nižší verzi.",
            "&aJak vyrobit mechanismus a jak teleportér nastavit, najdeš v kapitole Pohyb a výbava.&r",
        ]),
    "sa_jetpack": Q("sa_jetpack", "Mosazný jetpack", s="Létej na páru", icon="create_sa:brass_jetpack_chestplate",
        dep=["start", "create:crafter", "cadd_gear:sa_steam"],
        items=[("create_sa:brass_jetpack_chestplate", 1)], xp=60, d=[
            "Mosazný jetpack (&eBrass Jetpack&r) z &bCreate Stuff 'N Additions&r létá ve vzduchu i rychle plave pod vodou.",
            "Skládá se v mechanickém výrobníku z parního motorku, větráků, ozubených koleček, mosazi a andezitové slitiny. Potřebuje vodu i palivo, z nich dělá páru.",
            "&aVíc najdeš v kapitole Pohyb a výbava.&r",
        ]),
    "sa_drone": Q("sa_drone", "Mosazný dron", s="Létající pomocník", icon="create_sa:brass_drone_item",
        dep=["start", "create:crafter"],
        items=[("create_sa:brass_drone_item", 1), ("create_sa:drone_controller", 1)], xp=60, d=[
            "Mosazný dron (&eBrass Drone&r) z &bCreate Stuff 'N Additions&r je létající pomocník. Sleduje tě, když máš u sebe ovladač (&eDrone Controller&r).",
            "Dron se skládá v mechanickém výrobníku z vrtulí, redstonového vysílače, andezitové slitiny a precizního strojku. Ovladač vyrobíš z propojeného ovladače a mosazi.",
            "&aOvladačem zapínáš moduly dronu a měníš jeho vzdálenost. Víc najdeš v kapitole Pohyb a výbava.&r",
        ]),
    "wolf": Q("wolf", "Mechanický vlk", s="Robotický parťák", icon="createmechanicalcompanion:mechanical_wolf_link",
        dep=["start", "create:deployer"],
        items=[("createmechanicalcompanion:mechanical_wolf_motherboard", 1)], xp=60, d=[
            "&bCreate: Mechanical Companion&r přidává mechanického vlka. Chrání tě a dá se vylepšovat moduly.",
            "Základní deska (&eMechanical Wolf Motherboard&r) vzniká sekvenční montáží na měděném plátu: zelené barvivo, lis, komparátor a elektronka.",
            "&aVíc najdeš v kapitole Pohyb a výbava.&r",
        ]),
}

NO_RECIPE_GEAR = {
    "create_sa:heat_engine": "sekvenční montáž (data/create_sa/recipe/heat_engine_recipe.json; index ji nepozná kvůli formátu výsledku)",
    "create_sa:hydraulic_engine": "sekvenční montáž (data/create_sa/recipe/hydraulic_engine_recipe.json)",
    "create_sa:steam_engine": "sekvenční montáž (data/create_sa/recipe/steam_engine_recipe.json)",
}


# ======================================================================
# Kapitola DEKORACE
# ======================================================================
# Kapitola: Dekorace (Copycats+, Bits 'n' Bobs, Create Deco, Create: Interiors, Rechiseled: Create)
CADD_DECO = dict(
    key="cadd_deco", group="create", title="Dekorace",
    subtitle="Imitace, světla, lávky, židle a tesání", icon="copycats:copycat_slope",
    quests=[
        Q("start", "Krásná továrna", s="Začátečník", icon="createdeco:yellow_andesite_lamp",
          tasks=[auto()], dep=["create_addons:start"], xp=10, shape="hexagon", size=1.5, d=[
            "Tahle kapitola ti ukáže, jak udělat z továrny hezké místo. Je tu pět modů.",
            "",
            "&bCreate: Copycats+&r – imitace: bloky, které převezmou vzhled jiného bloku.",
            "&bCreate: Bits 'n' Bobs&r – žárovky, nixie displeje, řetězové pohony a barevné potrubí.",
            "&bCreate Deco&r – kovové lávky, lampy, dveře, kontejnery a barevné cihly.",
            "{@pagebreak}",
            "&bCreate: Interiors&r – židle, křesla a polštáře.",
            "&bRechiseled: Create&r – dláto, které z kamenů a oken Create udělá nové vzory.",
            "",
            "Cesta kapitolou: &aZačátečník&r (první dekorace z jednoduchých surovin), &aPokročilý&r (víc materiálů v jednom bloku, řetězy, kontejnery) a &aExpert&r (skryté stroje a živé nápisy).",
            "",
            "&aTip: Ke strojům Create i k věcem z těchto modů je často animovaný návod. Najeď myší na předmět a podrž W.&r"]),

        # ---------------- Copycats+
        Q("cc_shapes", "Imitace všech tvarů", dep=["start", "create_addons:copycats"],
          items=[("copycats:copycat_block", 1), ("copycats:copycat_slope", 2)], xp=20, d=[
            "Imitační panel už znáš. &bCopycats+&r přidává desítky dalších tvarů: celý blok, svah, schody, plot, zídku, žebřík a další.",
            "",
            "Skoro všechny se dělají v kameníkovi ze zinkového ingotu. Z jednoho ingotu je imitační blok (&eCopycat Block&r), dva svahy (&eCopycat Slope&r) a u menších tvarů i víc kusů.",
            "",
            "Pravým tlačítkem s blokem v ruce imitaci „obarvíš“. Montážním klíčem materiál zase odebereš.",
            "{@pagebreak}",
            "Některé tvary jdou ve výrobní mřížce přepnout na příbuzný tvar. Například svah na svislý svah a zpátky.",
            "",
            "&aTip: Shift + pravé tlačítko prázdnou rukou zapne nebo vypne propojené textury. Pak se sousední imitace spojí do jedné plochy.&r"]),
        Q("cc_func", "Tajný vchod", dep=["cc_shapes"],
          items=[("copycats:copycat_ghost_block", 1), ("copycats:copycat_door", 1)], xp=25, d=[
            "Některé imitace nejsou jen ozdoba. Imitační dveře (&eCopycat Door&r) se otvírají jako normální dveře, ale vypadají jako blok, který do nich dáš.",
            "",
            "Imitační falešný blok (&eCopycat Ghost Block&r) vypadá jako pevný blok, ale projdeš jím. Hráči ani zvířata do něj nenarazí.",
            "",
            "Obojí se vyrábí v kameníkovi ze zinkového ingotu.",
            "",
            "&aTip: Dej do dveří i falešného bloku stejný materiál jako do zdi okolo. Vchod do tajné místnosti pak nikdo nenajde.&r"]),
        Q("cc_multi", "Víc materiálů v jednom", s="Pokročilý", dep=["cc_shapes"],
          items=[("copycats:copycat_byte", 8)], xp=35, shape="hexagon", size=1.5, d=[
            "Doteď měla jedna imitace jeden materiál. Teď se naučíš skládat do jednoho bloku víc materiálů.",
            "",
            "Imitační miniblok (&eCopycat Byte&r) je osmina bloku. Z jednoho zinkového ingotu jich kameník udělá 8.",
            "",
            "Do jednoho bloku položíš až 8 minibloků a každý může mít jiný materiál. Tak postavíš třeba šachovnici nebo malé sochy.",
            "{@pagebreak}",
            "Stejně fungují i imitační půlblok (&eCopycat Slab&r), deska (&eCopycat Board&r) a polovrstva (&eCopycat Half Layer&r).",
            "",
            "Když budeš při plnění držet &eLevý Alt&r, materiál se dá do všech částí bloku najednou.",
            "",
            "&aTip: U vrstev a řezů klikni stejnou imitací znovu na položený blok. Imitace se tím zvětší.&r"]),
        Q("cc_kinetic", "Skryté stroje", s="Expert", dep=["cc_multi"],
          items=[("copycats:copycat_cogwheel", 4)], xp=50, shape="hexagon", size=1.5, d=[
            "Nejvyšší úroveň imitací: díly strojů, které vypadají jako obyčejné bloky. Ozubená kola a hřídele pak schováš přímo do zdi.",
            "",
            "Imitační ozubené kolečko (&eCopycat Cogwheel&r) vyrobíš ze 4 ozubených koleček a zinkového ingotu. Dostaneš 4 kusy.",
            "",
            "Točí se a přenáší rotaci úplně stejně jako normální ozubené kolečko. Jen má vzhled bloku, který do něj dáš.",
            "{@pagebreak}",
            "Stejně funguje velké kolečko (&eCopycat Large Cogwheel&r), hřídel (&eCopycat Shaft&r) a potrubí (&eCopycat Fluid Pipe&r).",
            "",
            "&aTip: Když postavíš celý pohon z imitací, bude továrna vypadat jako obyčejný dům. Brýlemi i tak uvidíš jejich rychlost a napětí.&r"]),

        # ---------------- Bits 'n' Bobs
        Q("bnb_lights", "Žárovky a světlomety", dep=["start"],
          items=[("bits_n_bobs:lightbulb", 3), ("bits_n_bobs:headlamp", 2)], xp=20, d=[
            "&bBits 'n' Bobs&r přidává světla, která můžeš ovládat redstonem.",
            "",
            "Žárovka (&eLightbulb&r) se vyrobí z redstonu, světlitého prachu a skla. Jeden recept dá 3 žárovky.",
            "",
            "Žárovka svítí, když dostane redstonový signál. Pravým tlačítkem prázdnou rukou ji přepneš, aby svítila pořád. Montážním klíčem jí přidáš nebo sundáš klec.",
            "{@pagebreak}",
            "Z jedné žárovky vyrobíš dva světlomety (&eHeadlamp&r). Dají se obarvit barvivem a do jednoho bloku jich položíš víc.",
            "",
            "&aTip: Světlomety se hodí na vlaky a na ozdobné cedule.&r"]),
        Q("bnb_pipes", "Barevné potrubí", dep=["start", "create:fluids"],
          tasks=[adv("bits_n_bobs:dye_fluid_component")], xp=25, d=[
            "Dvě potrubí, která vedou těsně vedle sebe, se normálně samy spojí. Barvivo tomu zabrání.",
            "",
            "Klikni barvivem na nádrž (&eFluid Tank&r). Obarví se celá. Se Shiftem obarvíš jen jeden blok nádrže.",
            "",
            "Potrubí obarvíš tak, že při pokládání držíš barvivo ve druhé ruce.",
            "{@pagebreak}",
            "Obarvené potrubí se samo spojí jen s potrubím stejné barvy. Neobarvené potrubí se spojí se vším.",
            "",
            "Quest se splní, až poprvé obarvíš nádrž nebo potrubí.",
            "",
            "&aTip: Každá kapalina může mít svou barvu potrubí. Hned uvidíš, kde teče voda a kde láva.&r"]),
        Q("bnb_chain", "Řetězový pohon", s="Pokročilý", dep=["start", "create:shaft"],
          items=[("bits_n_bobs:small_flanged_cogwheel", 2), ("bits_n_bobs:large_flanged_cogwheel", 1)], xp=35, shape="hexagon", size=1.5, d=[
            "Doteď musela ozubená kola stát těsně u sebe. Řetěz přenese rotaci i mezi koly, která jsou od sebe daleko.",
            "",
            "Ozubené kolo s přírubou (&eFlanged Cogwheel&r) vyrobíš z ozubeného kolečka a železného nugetu. Velké (&eLarge Flanged Cogwheel&r) z velkého ozubeného kolečka a nugetu.",
            "{@pagebreak}",
            "Vezmi do ruky řetězy a klikej postupně na kola, která chceš spojit. Řetěz jde i přes obyčejná ozubená kola. Musí vytvořit uzavřenou smyčku a kola se nesmí dotýkat.",
            "",
            "Pohon spotřebuje řetězy podle délky. Převod zůstane stejný jako u kol, která se dotýkají: malé kolo se točí 2× rychleji než velké.",
            "{@pagebreak}",
            "Místo řetězu můžeš použít i mechanický pás (&eMechanical Belt&r) nebo lano. Ty jdou natáhnout jen přes kola s přírubou.",
            "",
            "&aTip: Mezi dvěma velkými koly může řetěz změnit směr. Kola musí mít společnou tečnu, po které řetěz povede. Podívej se do ponderu.&r"]),
        Q("bnb_struts", "Šikmé vzpěry", dep=["start", "create:sheets"], optional=True,
          items=[("bits_n_bobs:girder_strut", 6)], xp=20, d=[
            "Vzpěra (&eGirder Strut&r) je kovový nosník, který se natáhne mezi dva bloky. Může vést i šikmo.",
            "",
            "Vyrobíš ji ze 3 kovových nosníků (&eMetal Girder&r) a 2 andezitových slitin. Dostaneš 6 kusů. Lanová verze (&eCable Girder Strut&r) má místo nosníků železné nugety.",
            "",
            "Vzpěra vede rovně a nedá se ohnout. Jak ji položit, ukáže ponder.",
            "",
            "&aTip: Kovový nosník, kovový držák i vzpěru zrezivíš praním: pošli je větrákem přes vodu.&r"]),
        Q("bnb_pulley", "Řetězová kladka", dep=["start", "create:bearing"], optional=True,
          items=[("bits_n_bobs:chain_pulley", 1)], xp=20, d=[
            "Řetězová kladka (&eChain Pulley&r) funguje jako lanová kladka (&eRope Pulley&r) z Create. Zvedá a spouští bloky, jen místo lana visí řetěz.",
            "",
            "Polož lanovou kladku a klikni na ni řetězem. Kladka se změní na řetězovou a řetěz ti zůstane v ruce.",
            "",
            "&aTip: Hodí se do dolů a na výtahy, kde lano nevypadá dobře.&r"]),
        Q("bnb_nixie", "Živé nápisy", s="Expert", dep=["create_addons:bnb"],
          items=[("bits_n_bobs:nixie_board", 8)], xp=50, shape="hexagon", size=1.5, d=[
            "Nixie deska (&eNixie Board&r) je plochý svítící displej na text. Umí delší nápisy i víc řádků.",
            "",
            "Vyrobíš ji ze 6 leštěných růženínů a železného plátu. Dostaneš 8 kusů.",
            "",
            "Desky vedle sebe se spojí do delšího displeje. Desky nad sebou nebo pod sebou vytvoří vyšší displej.",
            "{@pagebreak}",
            "Text nastavíš jmenovkou nebo psací podložkou (&eClipboard&r). Montážním klíčem přepínáš režimy zobrazení – některé ukážou víc znaků a víc řádků. Barvivem přebarvíš celý displej najednou.",
            "{@pagebreak}",
            "Expertní trik: displejový vysílač (&eDisplay Link&r). Polož ho na zdroj informací, třeba na kukačkové hodiny nebo na sklad, a propoj ho s nixie deskou. Displej pak sám ukazuje aktuální stav. Jak se propojuje, ukáže ponder vysílače.",
            "",
            "&aTip: Takhle uděláš ceduli, která ukazuje, co se děje ve tvé továrně.&r"]),

        # ---------------- Create Deco
        Q("deco_catwalk", "Kovové lávky", dep=["start", "create:alloy"],
          items=[("createdeco:andesite_catwalk", 4), ("createdeco:andesite_catwalk_railing", 4)], xp=20, d=[
            "&bCreate Deco&r přidává kovové stavební díly v barvách kovů z Create: andezitu, železa, mědi, zinku, mosazi a dalších.",
            "",
            "Většinu dílů vyrobíš v kameníkovi přímo z ingotu nebo slitiny. Z jedné andezitové slitiny jsou 4 lávky (&eAndesite Catwalk&r) nebo 8 zábradlí (&eAndesite Catwalk Railing&r).",
            "",
            "Lávka je mřížka, po které se chodí. Zábradlí dáš na její okraj.",
            "{@pagebreak}",
            "Stejně se dělají mřížky, pletivo, schody k lávkám a podpěry. Vlož slitinu do kameníku a prohlédni si všechny tvary.",
            "",
            "&aTip: Lávky z andezitu jsou nejlevnější. Pozdější kovy jako mosaz mají stejné tvary, jen jinou barvu.&r"]),
        Q("deco_lamps", "Klecové lampy", dep=["deco_catwalk", "create:press"],
          items=[("createdeco:yellow_andesite_lamp", 2)], xp=20, d=[
            "Klecová lampa (&eYellow Andesite Cage Lamp&r) je světlo v kovové kleci. Hodí se do továren a na lávky.",
            "",
            "Nejdřív lisem (&eMechanical Press&r) vylisuj z andezitové slitiny plát (&eAndesite Alloy Sheet&r). Do mřížky dej shora dolů: andezitovou slitinu, pochodeň a plát.",
            "",
            "Barvu lampy určí to, co dáš doprostřed: pochodeň = žlutá, redstonová pochodeň = červená, pochodeň duší = modrá, svítivé bobule = zelená.",
            "",
            "&aTip: Lampy z ostatních kovů se dělají stejně, jen z nugetu a plátu daného kovu.&r"]),
        Q("deco_bricks", "Barevné cihly", dep=["start"],
          items=[("createdeco:blue_bricks", 4)], xp=20, d=[
            "Create Deco umí cihly v sedmi barvách. Barvu jim dá kámen z Create.",
            "",
            "Dej do mřížky 8 cihel a doprostřed kámen &eAsurine&r. Vzniknou 4 modré cihly (&eBlue Bricks&r). Asurine najdeš v podzemí ve vrstvách mezi jinými kameny.",
            "",
            "Jiné kameny z Create, například &eCrimsite&r nebo &eOchrum&r, dají jiné barvy. Všechny recepty ukáže JEI.",
            "",
            "&aTip: V kameníkovi z cihel uděláš krátké, dlouhé, rohové a dlaždicové varianty.&r"]),
        Q("deco_container", "Lodní kontejnery", s="Pokročilý", dep=["deco_catwalk", "create:sheets"],
          items=[("createdeco:blue_shipping_container", 2)], xp=35, shape="hexagon", size=1.5, d=[
            "Teď z dekorace uděláš užitečný sklad. Lodní kontejner (&eBlue Shipping Container&r) funguje stejně jako trezor (&eItem Vault&r) z Create, jen vypadá jako barevný kontejner.",
            "",
            "Vyrobíš ho z barviva, 2 železných plátů a sudu. Nebo obarvíš hotový trezor barvivem ve výrobní mřížce.",
            "{@pagebreak}",
            "Kontejnery položené k sobě se spojí do jednoho velkého skladu, stejně jako trezory.",
            "",
            "Plní se a vybírají trychtýřem, mechanickou paží nebo jiným strojem, ne rukou.",
            "",
            "&aTip: Každá barva může znamenat jiný druh zboží. Ve skladu se pak hned vyznáš.&r"]),
        Q("deco_industrial", "Průmyslové železo", dep=["deco_catwalk", "building:createdeco"], optional=True,
          items=[("createdeco:industrial_iron_catwalk", 4)], xp=25, d=[
            "Průmyslové železo je tmavý kov pro velké tovární haly.",
            "",
            "V kameníkovi udělej ze železného ingotu 2 bloky průmyslového železa (&eBlock of Industrial Iron&r). Z bloku ve výrobní mřížce dostaneš 9 ingotů průmyslového železa.",
            "",
            "Z ingotu pak v kameníkovi vyrobíš lávky (&eIndustrial Iron Catwalk&r), mřížky, žebříky a další díly.",
            "",
            "&aTip: Z jednoho železného ingotu je tak 18 ingotů průmyslového železa. Je to levný materiál na velké stavby.&r"]),

        # ---------------- Create: Interiors
        Q("int_chair", "Pohodlné křeslo", dep=["start"],
          items=[("interiors:white_chair", 1)], xp=20, d=[
            "&bCreate: Interiors&r přidává židle, křesla, polštáře a stolky.",
            "",
            "Bílé křeslo (&eWhite Chair&r) vyrobíš z dřevěného půlbloku, prken a bílé vlny. Jinou barvu dostaneš z jiné vlny nebo obarvením hotového křesla.",
            "",
            "Pravým tlačítkem si sedneš. Levým Shiftem vstaneš.",
            "{@pagebreak}",
            "Montážním klíčem přidáš nebo sundáš opěrky. Shift + montážní klíč změní výšku opěradla.",
            "",
            "Křeslo funguje i na pohyblivé stavbě Create jako sedačka. Hráč na něm zůstane sedět, i když se stavba hýbe.",
            "",
            "&aTip: Židle z modu Bits 'n' Bobs jsou z vlny a dřevěných schodů.&r"]),
        Q("int_extra", "Polštáře a nízké křeslo", dep=["int_chair"], optional=True,
          items=[("interiors:white_floor_chair", 1), ("interiors:white_cushion", 2)], xp=15, d=[
            "Do pokoje patří i nízké křeslo a polštáře.",
            "",
            "Nízké křeslo (&eWhite Floor Chair&r) vyrobíš ze 2 dřevěných půlbloků a bílé vlny. Sedí se na něm stejně jako na křesle.",
            "",
            "Polštář (&eWhite Cushion&r) je z prken a vlny. Recept dá 2 kusy. Polštář je měkký a dá se na něm skákat.",
            "",
            "&aTip: Když k nízkému křeslu přidáš v mřížce dřevěný půlblok, vznikne z něj normální křeslo.&r"]),

        # ---------------- Rechiseled: Create
        Q("rc_windows", "Tesání bloků Create", dep=["start", "building:rechiseled"],
          items=[("rechiseledcreate:oak_window_bars", 2)], xp=20, d=[
            "Dláto (&eChisel&r) z modu &bRechiseled&r mění bloky na jiné vzory: cihličky, dlaždice, sloupy a další. Díky &bRechiseled: Create&r umí i kameny, okna a růženínové dlaždice z Create.",
            "",
            "Vezmi dláto do ruky a stiskni pravé tlačítko. Do okna vlož bloky a klikni na vzor, který chceš. Tlačítko &eChisel all&r přetesá celý stoh najednou.",
            "{@pagebreak}",
            "Úkol: vyrob si dubové okno (&eOak Window&r) z Create – je z prken a skla. Pak ho dlátem přetesej na okno s mřížkou (&eOak Window Bars&r).",
            "",
            "Stejně přetesáš kameny z Create, třeba &eAsurine&r nebo &eCrimsite&r, a dlaždice z růženínu.",
            "",
            "&aTip: Všechny vzory ukáže JEI v záložce Chiseling. Tesat se dá i automaticky mechanickým dlátem (&eMechanical Chisel&r).&r"]),
    ],
)

ORIG_DECO = {
    "copycats": Q("copycats", "Imitace", dep=["start", "create:zinc"],
        items=[("create:copycat_panel", 4)], xp=15, s="Create: Copycats+", d=[
            "Imitace (copycat) je blok, který převezme vzhled jiného bloku.",
            "",
            "Imitační panel (&eCopycat Panel&r) vyrobíš v kameníkovi ze zinkového ingotu. Z jednoho ingotu jsou 4 panely.",
            "",
            "Polož panel a klikni na něj pravým tlačítkem s plným blokem v ruce. Panel dostane vzhled toho bloku. Montážním klíčem materiál zase odebereš.",
            "",
            "Mod &bCopycats+&r přidává mnoho dalších tvarů. Víc najdeš v kapitole Dekorace."]),
    "bnb": Q("bnb", "Bits 'n' Bobs", dep=["start", "create:brass"],
        items=[("bits_n_bobs:large_nixie_tube", 1), ("bits_n_bobs:flywheel_bearing", 1)], xp=30, s="Create: Bits 'n' Bobs", d=[
            "&bBits 'n' Bobs&r přidává světla, displeje, řetězové pohony a dekorace pro továrny.",
            "",
            "Velká nixie trubice (&eLarge Nixie Tube&r) je svítící displej na znaky. Vyrobíš ji ze 4 leštěných růženínů a 2 železných plátů, dostaneš 4 kusy. Text nastavíš jmenovkou nebo psací podložkou (&eClipboard&r).",
            "{@pagebreak}",
            "Ložisko setrvačníku (&eFlywheel Bearing&r) je z mosazného pouzdra, andezitové slitiny, velkého ozubeného kolečka a dřevěného půlbloku. Když se točí, roztočí bloky přilepené před ním jako velký setrvačník.",
            "",
            "Pravým tlačítkem prázdnou rukou setrvačník z přilepených bloků sestavíš, dalším kliknutím ho zase rozebereš.",
            "",
            "Víc najdeš v kapitole Dekorace."]),
}

# ======================================================================
# Kapitola „Create: doplňky“ – rozcestník addonů (původní kapitola create_addons)
# Původní questy zůstávají zde (úkoly beze změny), jejich české texty jsou v ORIG_* výše.
# Tematické kapitoly na ně navazují přes dep="create_addons:<klíč>".
# ======================================================================
ORIG_HUB = {
    "start": Q("start", "Addony pro Create", s="Rozcestník", icon="create:brass_ingot", tasks=[auto()], xp=10, d=[
        "Addon je mod, který rozšiřuje Create o nové stroje a věci. Tahle kapitola je rozcestník: každý addon tu má jeden vstupní quest.",
        "",
        "Vstupní quest ti řekne, co addon dělá a k čemu je dobrý. Pak pokračuj v jeho tematické kapitole.",
        "{@pagebreak}",
        "Tematické kapitoly: &eElektřina&r, &eRopa a palivo&r, &ePrůmysl&r, &eVelká děla&r, &ePohyb a výbava&r a &eDekorace&r.",
        "",
        "Addony staví na základním Create. Některé questy se proto odemknou až po questech z kapitoly &eCreate&r (třeba po mosazi).",
        "",
        "&aMilníky (šestiúhelníky) s podnázvem Začátečník, Pokročilý a Expert ukazují, jak daleko v addonu jsi.&r",
    ]),
    "slicer": Q("slicer", "Kráječ", s="Slice & Dice", dep=["start", "create:casing"], items=[("sliceanddice:slicer", 1)], xp=30, d=[
        "Kráječ (&eSlicer&r) z modu &bSlice & Dice&r krájí jídlo místo tebe podle receptů krájecího prkénka.",
        "",
        "Vyrobíš ho z ozubeného kolečka, andezitového pouzdra a točny (&eTurntable&r). Postav ho nad pás, odkládací desku (&eDepot&r) nebo tyglík (&eBasin&r) a pravým tlačítkem do něj vlož nůž.",
        "",
        "&aVíc o jídle ze strojů najdeš v kapitole Create: kuchyně.&r",
    ]),
    "wrapped": Q("wrapped", "Balení dárků", s="Create: Wrapped", dep=["start"], items=[("create_wrapped:wrapping_station", 1)], xp=20, d=[
        "&bCreate: Wrapped&r přidává balení dárků a pár vánočních sladkostí.",
        "",
        "Balicí stůl (&eWrapping Station&r) vyrobíš z prken, papíru a železného ingotu.",
        "",
        "&aZ těsta, cukru a lahvičky medu vyrobíš na pracovním stole perník (&eGingerbread&r).&r",
    ]),
    "trading": Q("trading", "Obchodní stolek", s="Create: Trading Floor", dep=["start", "create:tube"], items=[("trading_floor:trading_depot", 1)], xp=40, d=[
        "&bCreate: Trading Floor&r umí obchodovat s vesničany automaticky. Už nemusíš klikat na každý obchod.",
        "",
        "Obchodní stolek (&eTrading Depot&r) vyrobíš z odkládací desky (&eDepot&r) a 2 elektronek (&eElectron Tube&r).",
        "",
        "Polož ho hned vedle pracovního bloku vesničana. Když vesničan příště pracuje u svého bloku, obchoduje se stolkem.",
    ]),
}

HUB_NEW = [
    # ---------- Create: Wrapped ----------
    Q("wr_present", "Zabal dárek", dep=["wrapped"], items=[("create_wrapped:red_present", 1)], xp=15, optional=True, d=[
        "Teď z balicího stolu uděláš první dárek.",
        "",
        "Balicí papír (&eRed Wrapping Paper&r) vyrobíš z 8 papírů a červeného barviva. Do balicího stolu vlož věc, kterou chceš darovat, a balicí papír. Za chvíli vznikne zabalený dárek (&eRed Present&r).",
        "",
        "&aKdo dárek drží v ruce a klikne pravým tlačítkem, rozbalí ho a dostane věc uvnitř.&r",
    ]),

    # ---------- Create: Trading Floor + Create: Dynamic Village ----------
    Q("tf_auto", "Automatický obchod", s="Začátečník", dep=["trading"], tasks=[adv("trading_floor:money_money_money")], icon="minecraft:emerald", xp=25, shape="hexagon", size=1.5, d=[
        "Teď poprvé obchoduješ bez klikání.",
        "",
        "Na obchodní stolek polož to, co vesničan za obchod chce (třeba smaragdy). Filtrem na stolku vyber, jaké zboží chceš dostat. Zboží se objeví na stolku.",
        "",
        "&aVesničan obchoduje jen v pracovní době, tedy přes den. V noci stolek čeká.&r",
    ]),
    Q("tf_drop", "Obchodní linka", s="Pokročilý", dep=["tf_auto"], tasks=[adv("trading_floor:drop_shipper")], icon="create:belt_connector", xp=40, shape="hexagon", size=1.5, d=[
        "Teď už stolek nebudeš plnit ručně. Cíl: získej 64 smaragdů z jednoho obchodního stolku. Smaragdy dostaneš, když vesničanovi něco prodáváš, třeba farmáři pšenici.",
        "",
        "Zboží přivez na stolek pásem. Hotové věci odebírej trychtýřem (&eFunnel&r) nebo mechanickou paží a pošli je do truhly.",
        "{@pagebreak}",
        "Obchod, který chce dvě různé věci, zvládnou 2 stolky vedle sebe. Na prvním nastav filtr, aby nedělal jiné obchody. Stolky sdílejí obsah, jen když mají stejný filtr nebo je druhý prázdný.",
        "",
        "&aDíky &bCreate: Dynamic Village&a jsou ve vesnicích i řemeslníci z Create. Vesničan dostane povolání podle bloku.&r",
        "",
        "&aSchématický stůl = mechanický inženýr, cedník (&eItem Drain&a) = hydraulický inženýr, mechanický vrták = horník, vlaková stanice = mechanik vlaků. Prodávají díly Create za smaragdy.&r",
    ]),
    Q("tf_jeff", "Obchodní impérium", s="Expert", dep=["tf_drop"], tasks=[adv("trading_floor:happy_jeff")], icon="minecraft:emerald_block", xp=80, shape="hexagon", size=1.5, d=[
        "Teď stavíš celou obchodní halu. Cíl: získej 1000 smaragdů z jednoho obchodního stolku.",
        "",
        "Víc vesničanů vedle sebe, každý se svým stolkem. Jeden pás je zásobuje a druhý odváží zboží do skladu.",
        "",
        "&aDisplejový vysílač (&eDisplay Link&a) na stolku ukáže na ceduli počet hotových obchodů.&r",
    ]),

    # ---------- Create: Let The Adventure Begin ----------
    Q("ltab_kings", "Najdi Kings Castle", s="Let The Adventure Begin", dep=["start"], tasks=[structure("create_ltab:kings_castle")], icon="minecraft:totem_of_undying", xp=50, optional=True, d=[
        "&bCreate: Let The Adventure Begin&r přidává do světa stavby z bloků Create: domy, větrné mlýny, lomy, jeskyně a hrady. V jejich truhlách najdeš kořist.",
        "Stavba &eKings Castle&r je vzácná. Hledej ji v biomech &ePlains&r a &eBirch Forest&r, spíš dál od spawnu. Stačí, když do ní vejdeš.",
        "",
        "&cUvnitř je truhla, která přivolá bosse. Než ji otevřeš, připrav se na boj.&r",
    ]),
    Q("ltab_king", "Poraz bosse Evoker King", s="Expert", dep=["ltab_kings"], tasks=[adv("create_ltab:evoker_king")], icon="minecraft:goat_horn", xp=100, optional=True, shape="hexagon", size=1.5, d=[
        "Když v &eKings Castle&r otevřeš truhlu, objeví se boss &eEvoker King&r.",
        "",
        "&cMá mnohem víc životů než obyčejný vyvolávač a drží totem nesmrtelnosti, takže ho porazíš až napodruhé. Šípy blízko něj zmizí a místo čelistí na tebe posílá drtící kola.&r",
        "",
        "&aZ bosse padá Roh nenávisti (&eHorn of Hatred&a), který ti dá efekt Zlé znamení (&eBad Omen&a). Někdy upustí i brýle s Ochranou V.&r",
    ]),
]


_ORIG = {}
for _o in (ORIG_HUB, ORIG_POWER, ORIG_OIL, ORIG_INDUSTRY, ORIG_CANNONS, ORIG_GEAR, ORIG_DECO):
    for _k, _q in _o.items():
        assert _k not in _ORIG, _k
        _ORIG[_k] = _q

# Pořadí původních questů (klíče a úkoly se nesmí měnit)
_ORIG_KEYS = ["start", "wire", "alternator", "motor", "accumulator", "tesla", "diesel", "oil", "pumpjack",
              "distill", "big_diesel", "newage", "energiser", "reactor", "cei", "enchanter", "printer", "cannon",
              "shot", "slicer", "excavation", "chunkload", "hypertube", "teleporter", "copycats", "sa_jetpack",
              "sa_drone", "bnb", "connected", "dragons", "wolf", "wrapped", "trading"]
assert set(_ORIG_KEYS) == set(_ORIG), set(_ORIG_KEYS) ^ set(_ORIG)

CREATE_ADDONS = dict(
    key="create_addons", group="create", title="Create: doplňky",
    subtitle="Rozcestník addonů: co který dělá a kde začít", icon="createaddition:electric_motor",
    quests=[_ORIG[k] for k in _ORIG_KEYS] + HUB_NEW,
)

NO_RECIPE = {}
for _n in (NO_RECIPE_POWER, NO_RECIPE_OIL, NO_RECIPE_INDUSTRY, NO_RECIPE_GEAR):
    NO_RECIPE.update(_n)

# Přeložená vlastní jména (validátor je hlásí jako chybu, piš anglický název ze hry)
PROPER_NAMES_CZ = {
    r"normáln\w* svět": "Overworld",
    r"netherov\w* pevnost|pevnost\w* v netheru": "Nether Fortress",
    r"\bbašt\w*": "Bastion Remnant",
    r"endov\w* měst": "End City",
    r"zasněžen\w* hor": "Snowy Slopes / Grove",
    r"březov\w* les": "Birch Forest",
    r"základn\w* pillager\w*": "Pillager Outpost",
    r"díln\w* illager\w*": "Illager Workshop",
    r"illagersk\w* inženýr": "Illager Engineer",
    r"dozorc\w* s bramborov\w*": "Illager Supervisor",
    r"královsk\w* hrad": "Kings Castle",
    r"král\w* vyvolávač\w*": "Evoker King",
}


def _spaced(d):
    """Mezi odstavce bez prázdného řádku vloží prázdný řádek (jednotný vzhled popisů)."""
    if "" in d:
        return d
    out = []
    for p in d:
        if out and p != "{@pagebreak}" and out[-1] != "{@pagebreak}":
            out.append("")
        out.append(p)
    return out


# Pořadí kapitol této oblasti v knize questů
CHAPTERS = [CREATE_ADDONS, CADD_POWER, CADD_OIL, CADD_INDUSTRY, CADD_CANNONS, CADD_GEAR, CADD_DECO]
for _c in CHAPTERS:
    for _q in _c["quests"]:
        _q.d = _spaced(_q.d)
