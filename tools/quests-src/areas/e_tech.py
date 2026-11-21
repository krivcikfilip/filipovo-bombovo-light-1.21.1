from engine import *

# Oblast e_tech: Mekanism (+Generators, Tools, Additions), úložiště (Iron Chests, Sophisticated Storage,
# Storage Drawers, Ender Storage, Building Gadgets, Extended Crafting), Applied Energistics 2, Refined Storage.
# Fakta ověřena v receptech, lang souborech, průvodci AE2 a v kódu jarů (Mekanism 10.7.19, AE2 19.2.19, RS 2.0.9).

MS = dict(shape="hexagon", size=1.5)  # milník

# =====================================================================================
# MEKANISM – základy, stroje, zpracování rud, chemie
# =====================================================================================
MEKANISM = dict(
    key="mekanism", group="tech", title="Mekanism",
    subtitle="Stroje, zpracování rud a chemie", icon="mekanism:metallurgic_infuser",
    quests=[
        Q("intro", "Co je Mekanism", tasks=[auto()], xp=10, s="Začátečník", icon="mekanism:metallurgic_infuser", **MS, d=[
            "&bMekanism&r je technický mod. Stavíš v něm elektrické stroje, které zpracují rudy až na pětinásobek, vyrábějí plyny a chemikálie a nakonec i jaderné palivo.",
            "Postup: osmium → metalurgický infuzér → ocel a obvody → ocelové krytí → první stroje. Každý další quest navazuje na předchozí.",
            "&aTip:&r Recept každé věci ukáže JEI: najeď na předmět a stiskni R. Stroje Mekanismu potřebují energii – první zdroj postavíš hned na začátku."]),
        Q("osmium", "Osmium", dep=["intro"], items=[("mekanism:raw_osmium", 8)], xp=20, d=[
            "&eOsmium&r je hlavní kov Mekanismu. Jeho ruda (&eOsmium Ore&r) se vyskytuje v kameni skoro v jakékoli výšce.",
            "Vytěžené osmium (&eRaw Osmium&r) přetav v peci na osmiový ingot (&eOsmium Ingot&r).",
            "&aTip:&r Mekanism přidává i rudy cínu, olova, uranu a fluoritu. Zatím je jen schovávej, budou se hodit."]),
        Q("heatgen", "Tepelný generátor", dep=["osmium"], items=[("mekanismgenerators:heat_generator", 1)], xp=30, d=[
            "Tepelný generátor (&eHeat Generator&r) je tvůj první zdroj energie pro Mekanism.",
            "Spaluje hořlavé věci (uhlí, dřevo) vložené do slotu. Energii dává i z lávy, která leží hned vedle něj.",
            "&aTip:&r Energii z generátoru odveď kabelem do strojů. Místo něj můžeš použít i alternátor (&eAlternator&r) z &bCreate Crafts & Additions&r."]),
        Q("infuser", "Metalurgický infuzér", dep=["osmium"], items=[("mekanism:metallurgic_infuser", 1)], xp=40, d=[
            "Metalurgický infuzér (&eMetallurgic Infuser&r) napustí kov jinou látkou, třeba uhlíkem nebo redstonem. Je to první a nejdůležitější stroj Mekanismu.",
            "Do levého slotu dej zdroj infuze (uhlí, redstone…), do prostředního předmět, který chceš upravit. Stroj musí mít energii.",
            "&aTip:&r Vyrobíš ho ze železa, dvou pecí, redstonu a osmiového ingotu."]),
        Q("steel", "Ocel", dep=["infuser"], items=[("mekanism:ingot_steel", 8)], xp=30, d=[
            "Ocel (&eSteel Ingot&r) potřebuješ skoro na všechno. Vyrábí se v infuzéru ve dvou krocích. Zdrojem infuze je uhlí nebo dřevěné uhlí.",
            "1) Železný ingot + uhlík = obohacené železo (&eEnriched Iron&r). 2) Obohacené železo + uhlík = ocelový prach (&eSteel Dust&r). Prach přetav v peci na ingot.",
            "&aTip:&r V packu se používá jen tahle ocel. Ocel z jiných modů sjednocuje mod &bAlmost Unified&r."]),
        Q("circuit", "Základní obvod", dep=["infuser"], items=[("mekanism:basic_control_circuit", 4)], xp=30, d=[
            "Základní řídicí obvod (&eBasic Control Circuit&r) je skoro v každém stroji Mekanismu.",
            "Vyrobíš ho v infuzéru: osmiový ingot doprostřed, redstone do levého slotu jako zdroj infuze.",
            "&aTip:&r Lepší obvody vzniknou z horšího obvodu a slitin. Pokročilý obvod přijde za pár kroků."]),
        Q("alloy", "Infuzní slitina", dep=["infuser"], items=[("mekanism:alloy_infused", 4)], xp=25, d=[
            "Infuzní slitina (&eInfused Alloy&r) je měděný ingot napuštěný redstonem v infuzéru.",
            "Potřebuješ ji na solární panely, vylepšení strojů a separátor. Pokročilý obvod (&eAdvanced Control Circuit&r) = základní obvod + 2 slitiny.",
            "&aTip:&r Slitinou klikni pravým tlačítkem na kabel nebo trubku Mekanismu a vylepšíš je na vyšší úroveň přímo na místě."]),
        Q("tablet", "Energetická tableta", dep=["alloy"], items=[("mekanism:energy_tablet", 2)], xp=20, d=[
            "Energetická tableta (&eEnergy Tablet&r) je malá baterie. Je součástí generátorů, energetických kostek a nástrojů.",
            "Vyrobíš ji z redstonu, zlatých ingotů a infuzní slitiny.",
            "&aTip:&r Na solární generátor potřebuješ jednu tabletu, na větrný dvě."]),
        Q("casing", "Ocelové krytí", dep=["steel"], items=[("mekanism:steel_casing", 2)], xp=30, d=[
            "Ocelové krytí (&eSteel Casing&r) je základ skoro všech strojů Mekanismu.",
            "Recept: 4 ocelové ingoty, 4 sklo a 1 osmiový ingot uprostřed.",
            "&aTip:&r Vyrob si jich rovnou víc – každý stroj potřebuje jedno."]),
        Q("cable", "Kabely", dep=["heatgen", "steel"], items=[("mekanism:basic_universal_cable", 16)], xp=15, d=[
            "Univerzální kabel (&eBasic Universal Cable&r) vede energii mezi generátory a stroji. Vyrobíš ho z oceli a redstonu.",
            "Kabel se sám napojí na sousední stroje. Stačí ho vést od generátoru ke strojům.",
            "&aTip:&r Infuzní slitinou (pravé tlačítko) vylepšíš kabel na rychlejší. Další úrovně vylepšíš lepšími slitinami."]),
        Q("solar", "Solární energie", dep=["heatgen", "tablet"], items=[("mekanismgenerators:solar_generator", 2)], xp=30, d=[
            "Solární generátor (&eSolar Generator&r) vyrábí energii zadarmo, ale jen přes den a když nad ním je volná obloha.",
            "Vyrobíš ho ze solárních panelů (&eSolar Panel&r), infuzní slitiny, železa, osmia a energetické tablety.",
            "&aTip:&r V noci nevyrábí nic. Přebytek ze dne ukládej do energetické kostky."]),
        Q("wind", "Větrná energie", dep=["heatgen", "tablet", "circuit"], items=[("mekanismgenerators:wind_generator", 1)], xp=40, d=[
            "Větrný generátor (&eWind Generator&r) se točí i v noci. Čím výš ho postavíš, tím víc energie dává.",
            "Zabírá na výšku víc bloků, takže nad ním nech volné místo.",
            "&aTip:&r Postav ho na vysokém kopci nebo na sloupu."]),
        Q("cube", "Energetická kostka", dep=["tablet", "casing"], items=[("mekanism:basic_energy_cube", 1)], xp=30, d=[
            "Energetická kostka (&eBasic Energy Cube&r) je baterie. Uloží přebytek z generátorů na později.",
            "V okně kostky vidíš, kolik energie je uloženo. Jsou tam i sloty na nabíjení předmětů, třeba nástrojů.",
            "&aTip:&r Která strana energii přijímá a která vydává, nastavíš v okně kostky (nastavení stran) nebo konfigurátorem."]),
        Q("enrich", "2× rudy: obohacovací komora", dep=["casing", "circuit"], items=[("mekanism:enrichment_chamber", 1)], xp=40, d=[
            "Obohacovací komora (&eEnrichment Chamber&r) je první stupeň zpracování rud. Z bloku rudy udělá 2 prachy, ze 3 kusů vytěžené rudy 4 prachy.",
            "Prach přetav v peci na ingot. Získáš tak víc kovu než přímým tavením.",
            "&aTip:&r Krumpáč se Štěstím dá víc kusů vytěžené rudy, krumpáč s Něžným dotekem celé bloky rudy. Stroje zpracují obojí."]),
        Q("infuse", "Obohacené materiály", dep=["enrich"], items=[("mekanism:enriched_carbon", 8)], xp=25, d=[
            "Obohacovací komora udělá z uhlí obohacený uhlík (&eEnriched Carbon&r) a z redstonu obohacený redstone (&eEnriched Redstone&r).",
            "V infuzéru dá 1 uhlí jen 10 jednotek uhlíku, ale 1 obohacený uhlík 80. U redstonu je to stejné. Ušetříš tak hodně surovin.",
            "&aTip:&r Diamant infuzér bere jen jako obohacený (&eEnriched Diamond&r) nebo jako prach. Obohať si pár diamantů na zesílenou slitinu."]),
        Q("smelter", "Energetická tavicí pec", dep=["enrich"], items=[("mekanism:energized_smelter", 1)], xp=30, d=[
            "Energetická tavicí pec (&eEnergized Smelter&r) taví jako obyčejná pec, ale na energii a bez paliva.",
            "Hodí se na tavení prachu z obohacovací komory. Zrychlíš ji vylepšením rychlosti.",
            "&aTip:&r Z tavicí pece jde udělat továrna (&eBasic Smelting Factory&r), která taví víc věcí najednou."]),
        Q("crusher", "Drtič", dep=["enrich"], items=[("mekanism:crusher", 1)], xp=20, d=[
            "Drtič (&eCrusher&r) rozdrtí ingoty na prach. Umí i dlažební kámen na štěrk, štěrk na písek a rostliny na bio palivo.",
            "Prach potřebuješ do receptů (elektrolytické jádro, vylepšení) a drtič je i součástí linky na 3× zpracování rud.",
            "&aTip:&r Co všechno drtič umí, zjistíš v JEI: najeď na drtič a stiskni U."]),
        Q("tin", "Cín", dep=["osmium"], items=[("mekanism:raw_tin", 6)], xp=15, d=[
            "Cínovou rudu (&eTin Ore&r) těžíš podobně jako osmium. Vytěžený cín (&eRaw Tin&r) přetav na ingot.",
            "Cín potřebuješ na jetpack a na bronz. Cínový prach je i zdroj infuze v infuzéru.",
            "&aTip:&r Cínový prach (&eTin Dust&r) dostaneš z obohacovací komory nebo z drtiče."]),
        Q("bronze", "Bronz", dep=["tin", "enrich"], items=[("mekanism:ingot_bronze", 4)], xp=20, d=[
            "Bronz (&eBronze Ingot&r) vzniká v infuzéru: zdrojem infuze je cínový prach, doprostřed dej 3 měděné ingoty. Vyjdou 4 bronzové ingoty.",
            "Bronz potřebuješ na solární neutronový aktivátor a na moduly MekaSuitu. Z bronzu jsou i nástroje a brnění z &bMekanism Tools&r.",
            "&aTip:&r Bronz z jiných modů je v packu sjednocený na tenhle."]),
        Q("upgrades", "Vylepšení strojů", dep=["enrich", "alloy"], items=[("mekanism:upgrade_speed", 1), ("mekanism:upgrade_energy", 1)], xp=40, d=[
            "Vylepšení se vkládají do stroje: v okně stroje otevři kartu vylepšení a vlož je dovnitř.",
            "Rychlost (&eSpeed Upgrade&r) zrychlí práci, ale stroj bere víc energie. Energie (&eEnergy Upgrade&r) sníží spotřebu a zvětší zásobník energie.",
            "&aTip:&r Kolik kusů jde do stroje vložit, ukáže tooltip vylepšení."]),
        Q("configurator", "Konfigurátor", dep=["steel"], items=[("mekanism:configurator", 1)], xp=20, d=[
            "Konfigurátor (&eConfigurator&r) nastavuje strany strojů: která strana je vstup a která výstup.",
            "Režimy přepínáš Shift + kolečkem myši. V režimu &eConfigurate&r pravým tlačítkem zjistíš, co strana dělá, a Shift + pravým ji změníš. V režimu &eWrench&r stroj Shift + pravým sebereš.",
            "&aTip:&r Stejné nastavení je i v okně stroje. Tam zapneš i automatický výstup (&eAuto-eject&r), který hotové věci sám vysune ven."]),
        Q("config_card", "Konfigurační karta", dep=["configurator", "circuit"], tasks=[adv("mekanism:configuration_copying")], xp=15, optional=True, icon="mekanism:configuration_card", d=[
            "Konfigurační karta (&eConfiguration Card&r) přenese nastavení stran z jednoho stroje na druhý.",
            "Shift + pravým tlačítkem na stroj nastavení zkopíruješ, pravým tlačítkem na jiný stroj ho vložíš.",
            "&aTip:&r Hodí se, když stavíš řadu stejných strojů."]),
        Q("transporter", "Logistický transportér", dep=["configurator", "circuit"], items=[("mekanism:basic_logistical_transporter", 16)], xp=30, d=[
            "Logistický transportér (&eBasic Logistical Transporter&r) je trubka na předměty. Vyrobíš ho z oceli a základního obvodu.",
            "Normálně sám z truhel nic nebere. Předměty do něj posílá stroj se zapnutým automatickým výstupem (&eAuto-eject&r) nebo logistický třídič.",
            "Konfigurátorem ale můžeš napojení transportéru na truhlu přepnout na sání (&ePull&r). Pak si věci z truhly bere sám.",
            "&aTip:&r Omezující transportér (&eRestrictive Transporter&r) se použije, jen když jiná cesta není. Odbočovací (&eDiversion Transporter&r) jde zapínat redstonem."]),
        Q("sorter", "Logistický třídič", dep=["transporter"], items=[("mekanism:logistical_sorter", 1)], xp=30, d=[
            "Logistický třídič (&eLogistical Sorter&r) vytahuje předměty z inventáře za sebou a posílá je dál do transportéru nebo truhly.",
            "Ve filtrech nastavíš, které předměty má posílat a kam. Nefiltrované věci může posílat také (volba &eEject unfiltered&r).",
            "&aTip:&r Třídič + transportéry = automatické třídění surovin do správných strojů a truhel."]),
        Q("installer", "Sada na továrnu", dep=["circuit"], items=[("mekanism:basic_tier_installer", 1)], xp=20, d=[
            "Sada na vylepšení (&eBasic Tier Installer&r) promění jednoduchý stroj na továrnu přímo na místě – nemusíš ho bourat.",
            "Klikni s ní pravým tlačítkem na stroj, třeba na energetickou tavicí pec. Továrnu pak sadami vyšší úrovně (&eAdvanced Tier Installer&r a další) vylepšíš ještě víc.",
            "&aTip:&r Továrnu jde vyrobit i rovnou v pracovním stole – recept ukáže JEI."]),
        Q("factory", "Továrny", dep=["smelter", "installer"], items=[("mekanism:basic_smelting_factory", 1)], xp=40, d=[
            "Továrna (&eBasic Smelting Factory&r) zpracovává víc věcí naráz: základní 3, pokročilá 5, elitní 7 a ultimátní 9.",
            "Továrnu jde udělat z většiny jednoduchých strojů: tavicí pece, obohacovací komory, drtiče, infuzéru, čisticí a vstřikovací komory a dalších.",
            "&aTip:&r Jedna továrna ušetří místo za několik samostatných strojů."]),
        Q("separator", "Elektrolytický separátor", dep=["enrich", "alloy"], items=[("mekanism:electrolytic_separator", 1)], xp=40, d=[
            "Elektrolytický separátor (&eElectrolytic Separator&r) rozloží kapalinu na dva plyny. Z vody udělá vodík (&eHydrogen&r) a kyslík (&eOxygen&r).",
            "Uvnitř je elektrolytické jádro (&eElectrolytic Core&r) z infuzní slitiny a prachu železa, zlata a osmia. Prach získáš v obohacovací komoře nebo drtiči.",
            "Vodu dodáš kbelíkem do slotu v okně nebo potrubím. Každý plyn vystupuje z jiné strany stroje.",
            "&aTip:&r Kyslík použiješ na 3× zpracování rud, vodík jako palivo pro jetpack nebo generátor."]),
        Q("gas", "Plyny a nádrže", dep=["separator"], items=[("mekanism:basic_pressurized_tube", 8), ("mekanism:basic_chemical_tank", 1)], xp=25, d=[
            "Plyny se nedají nabrat do kbelíku. Vedou se tlakovou trubkou (&eBasic Pressurized Tube&r) z oceli a skla.",
            "Chemická nádrž (&eBasic Chemical Tank&r) plyn uloží. Když ji vykopeš, plyn v ní zůstane, takže ho můžeš přenést.",
            "&aTip:&r Jedna síť trubek vede vždy jen jeden plyn. Pro každý plyn postav vlastní trasu."]),
        Q("pipe", "Kapaliny a pumpa", dep=["casing", "alloy"], items=[("mekanism:basic_mechanical_pipe", 8), ("mekanism:electric_pump", 1)], xp=25, d=[
            "Mechanické potrubí (&eBasic Mechanical Pipe&r) vede kapaliny, třeba vodu do separátoru. Vyrobíš ho z oceli a kbelíku.",
            "Elektrická pumpa (&eElectric Pump&r) nasává kapalinu pod sebou. Polož ji nad vodu nebo lávu a dej jí energii.",
            "&aTip:&r Pumpa s filtračním vylepšením (&eFilter Upgrade&r) čerpá z vody těžkou vodu. Tu budeš potřebovat až u fúzního reaktoru."]),
        Q("jetpack", "Jetpack", dep=["gas", "tin"], items=[("mekanism:jetpack", 1)], xp=60, d=[
            "Jetpack (&eJetpack&r) ti dovolí létat. Nosí se na hrudi místo brnění a pohání ho vodík.",
            "Naplníš ho v elektrolytickém separátoru – vlož ho do slotu u výstupu vodíku. Nebo ho naplň z chemické nádrže.",
            "&aTip:&r Režim (normální, vznášení, vypnuto) přepneš klávesou &eChest Mode Switch&r, výchozí je G. Změnit ji můžeš v Nastavení → Ovládání."]),
        Q("purif", "3× rudy: čisticí komora", dep=["enrich", "separator", "crusher"], items=[("mekanism:purification_chamber", 1), ("mekanism:advanced_control_circuit", 2)], xp=60, s="Pokročilý", **MS, d=[
            "Teď už nestačí jen obohacovat. Čisticí komora (&ePurification Chamber&r) je druhý stupeň: z bloku rudy udělá 3 hrudky (např. &eIron Clump&r), z 1 vytěžené rudy 2. Potřebuje kyslík.",
            "Linka: hrudka → drtič → špinavý prach (např. &eDirty Iron Dust&r) → obohacovací komora → prach → pec. Každý vyšší stupeň přidá na začátek nový stroj, zbytek linky už máš.",
            "Kyslík přiveď trubkou ze separátoru. Nouzově stačí vložit pazourek do slotu na plyn v okně komory.",
            "&aTip:&r Pokročilý obvod (&eAdvanced Control Circuit&r) vyrobíš ze základního obvodu a 2 infuzních slitin."]),
        Q("reinforced", "Zesílená slitina", dep=["infuse", "alloy"], items=[("mekanism:alloy_reinforced", 4)], xp=30, d=[
            "Zesílená slitina (&eReinforced Alloy&r) je infuzní slitina napuštěná diamantem v infuzéru.",
            "Zdrojem infuze je obohacený diamant nebo diamantový prach (&eDiamond Dust&r) z drtiče. Celý diamant infuzér nevezme.",
            "&aTip:&r Elitní obvod (&eElite Control Circuit&r) = pokročilý obvod + 2 zesílené slitiny."]),
        Q("dyntank", "Dynamická nádrž", dep=["steel", "circuit"], items=[("mekanism:dynamic_tank", 4), ("mekanism:dynamic_valve", 1)], xp=20, d=[
            "Z bloků dynamické nádrže (&eDynamic Tank&r) se staví velká dutá nádrž na kapaliny i plyny. Plní a vypouští se přes ventil (&eDynamic Valve&r).",
            "Samotný blok nádrže je i součástí receptů – potřebuješ ho na tlakovou reakční komoru a chemický oxidátor.",
            "&aTip:&r Místo některých bloků nádrže můžeš dát konstrukční sklo (&eStructural Glass&r) a vidět dovnitř."]),
        Q("personal", "Osobní truhla", dep=["steel", "circuit"], items=[("mekanism:personal_chest", 1)], xp=15, d=[
            "Osobní truhla (&ePersonal Chest&r) má 54 slotů a otevřeš ji i přímo z inventáře, když ji neseš u sebe.",
            "Věci v ní zůstanou, i když ji vykopeš a přeneseš.",
            "&aTip:&r Osobní truhla je v receptu na chemický oxidátor, robita a QIO."]),
        Q("evaporation", "Odpařovací věž", dep=["purif", "steel"], items=[("mekanism:thermal_evaporation_controller", 1), ("mekanism:thermal_evaporation_valve", 1)], xp=50, d=[
            "Termální odpařovací věž (&eThermal Evaporation Plant&r) odpařuje vodu a vyrábí solanku (&eBrine&r). Je to stavba z více bloků.",
            "Postav věž 4×4 bloky, vysokou 3 až 18 bloků: plné dno a stěny z bloků &eThermal Evaporation Block&r, nahoře otevřená, uvnitř vzduch.",
            "Do stěny dej jeden ovladač (&eThermal Evaporation Controller&r) a aspoň jeden ventil (&eThermal Evaporation Valve&r). Ventilem přiváděj vodu a odváděj solanku.",
            "&aTip:&r Čím je věž teplejší, tím rychleji pracuje. Teplo dodá topení (&eResistive Heater&r) položené vedle ventilu."]),
        Q("chem_infuser", "Chemický infuzér", dep=["gas"], items=[("mekanism:chemical_infuser", 1)], xp=40, d=[
            "Chemický infuzér (&eChemical Infuser&r) spojí dva plyny v nový.",
            "Nejdůležitější recept: vodík + chlor = chlorovodík (&eHydrogen Chloride&r). Ten potřebuješ na 4× zpracování rud.",
            "&aTip:&r Chlor vyrobí elektrolytický separátor ze solanky z odpařovací věže."]),
        Q("injection", "4× rudy: vstřikovací komora", dep=["purif", "reinforced", "chem_infuser", "evaporation"], items=[("mekanism:chemical_injection_chamber", 1), ("mekanism:elite_control_circuit", 2)], xp=80, d=[
            "Chemická vstřikovací komora (&eChemical Injection Chamber&r) je třetí stupeň: z bloku rudy udělá 4 střepy (např. &eIron Shard&r), ze 3 vytěžených rud 8. Potřebuje chlorovodík.",
            "Střepy dej do čisticí komory – udělá z nich hrudky – a dál pokračuj linkou jako u 3× zpracování.",
            "Chlorovodík přiveď trubkou z chemického infuzéru. Nouzově jde vložit sůl do slotu na plyn.",
            "&aTip:&r Vstřikovací komora udělá ze střelného prachu sirný prach (&eSulfur Dust&r). Bude se hodit na kyselinu sírovou."]),
        Q("compressor", "Osmiový kompresor", dep=["purif", "casing"], items=[("mekanism:osmium_compressor", 1)], xp=30, d=[
            "Osmiový kompresor (&eOsmium Compressor&r) lisuje prach a osmium do pevných ingotů.",
            "Osmium do něj dodáš tak, že vložíš osmiový ingot do slotu na plyn. Z rafinovaného obsidiánového prachu pak vyrobí rafinovaný obsidián. Ze světlitového prachu vyrobí rafinovaný světlit.",
            "&aTip:&r Oba ingoty potřebuješ na teleportér a nejlepší nástroje."]),
        Q("refined_obsidian", "Rafinovaný obsidián", dep=["compressor", "reinforced", "crusher"], items=[("mekanism:ingot_refined_obsidian", 4)], xp=40, d=[
            "Rafinovaný obsidián (&eRefined Obsidian Ingot&r) je velmi pevný kov.",
            "Postup: obsidián rozdrť v drtiči na prach. V infuzéru ho napusť diamantem – vznikne rafinovaný obsidiánový prach (&eRefined Obsidian Dust&r). Ten stlač v osmiovém kompresoru na ingot.",
            "&aTip:&r Z rafinovaného obsidiánu jsou nejsilnější nástroje a brnění z &bMekanism Tools&r."]),
        Q("refined_glowstone", "Rafinovaný světlit", dep=["compressor"], items=[("mekanism:ingot_refined_glowstone", 4)], xp=25, d=[
            "Rafinovaný světlit (&eRefined Glowstone Ingot&r) vyrobíš v osmiovém kompresoru ze světlitového prachu.",
            "Potřebuješ ho na rámy teleportéru (&eTeleporter Frame&r).",
            "&aTip:&r Z rafinovaného světlitu jsou i svítící nástroje a brnění z &bMekanism Tools&r."]),
        Q("atomic", "Atomová slitina", dep=["reinforced", "refined_obsidian"], items=[("mekanism:alloy_atomic", 4)], xp=50, d=[
            "Atomová slitina (&eAtomic Alloy&r) je nejlepší slitina. Vznikne v infuzéru ze zesílené slitiny a rafinovaného obsidiánu.",
            "Zdrojem infuze je rafinovaný obsidiánový prach nebo obohacený obsidián (&eEnriched Obsidian&r) z obohacovací komory.",
            "&aTip:&r Atomová slitina je v teleportéru, robitovi, digitálním horníkovi a nejlepších obvodech."]),
        Q("ultimate", "Ultimátní obvod", dep=["atomic", "injection"], items=[("mekanism:ultimate_control_circuit", 2)], xp=50, d=[
            "Ultimátní obvod (&eUltimate Control Circuit&r) = elitní obvod + 2 atomové slitiny.",
            "Potřebuješ ho na stroje pro 5× zpracování rud, na QIO a na MekaSuit.",
            "&aTip:&r Obvody jdou vyrábět i v infuzéru (obvod + zdroj infuze). V JEI porovnej, co je pro tebe levnější."]),
        Q("acid", "Kyselina sírová", dep=["chem_infuser", "dyntank", "personal"], items=[("mekanism:chemical_oxidizer", 1), ("mekanism:rotary_condensentrator", 1)], xp=50, d=[
            "Na 5× zpracování rud potřebuješ kyselinu sírovou (&eSulfuric Acid&r). Výroba má tři kroky.",
            "1) Chemický oxidátor (&eChemical Oxidizer&r) udělá ze sirného prachu oxid siřičitý. 2) Chemický infuzér: oxid siřičitý + kyslík = oxid sírový. 3) Chemický infuzér: oxid sírový + vodní pára = kyselina sírová.",
            "Vodní páru vyrobí z vody rotační kondenzátor (&eRotary Condensentrator&r). Ten převádí kapaliny na plyny a zpět.",
            "&aTip:&r Sirný prach dostaneš ze střelného prachu ve vstřikovací komoře, nebo z uhlí v tlakové reakční komoře."]),
        Q("dissolution", "5× rudy: celá linka", dep=["injection", "ultimate", "acid", "mekanism_power:fluorite"], items=[("mekanism:chemical_dissolution_chamber", 1), ("mekanism:chemical_washer", 1), ("mekanism:chemical_crystallizer", 1)], xp=100, s="Expert", **MS, d=[
            "Nejvyšší stupeň: 5× zpracování rud. Z bloku rudy dostaneš 5 ingotů, ze 3 vytěžených rud 10 krystalů.",
            "1) Rozpouštěcí komora (&eChemical Dissolution Chamber&r): ruda + kyselina sírová = špinavá kaše. 2) Pračka (&eChemical Washer&r): kaše + voda = čistá kaše. 3) Krystalizátor (&eChemical Crystallizer&r): kaše → krystaly (např. &eIron Crystal&r).",
            "Krystaly dej do vstřikovací komory a pokračuj linkou: střepy → hrudky → špinavý prach → prach → ingot.",
            "&aTip:&r Na krystalizátor potřebuješ fluorit (&eFluorite&r). Jeho rudu zpracuj v obohacovací komoře – z bloku rudy dá 6 kusů."]),
        Q("biofuel", "Bio palivo", dep=["crusher"], items=[("mekanism:bio_fuel", 16)], xp=15, d=[
            "Bio palivo (&eBio Fuel&r) vyrobíš v drtiči z rostlin – semínek, jablek, listí, trávy a dalších.",
            "Pálí ho bio-generátor a potřebuješ ho na substrát v tlakové reakční komoře.",
            "&aTip:&r Co všechno jde na bio palivo, ukáže JEI u drtiče."]),
        Q("prc", "Tlaková reakční komora", dep=["biofuel", "dyntank", "gas"], items=[("mekanism:pressurized_reaction_chamber", 1), ("mekanism:substrate", 4)], xp=50, d=[
            "Tlaková reakční komora (&ePressurized Reaction Chamber&r) zpracuje naráz pevnou látku, kapalinu a plyn.",
            "2 bio paliva + voda + vodík = substrát (&eSubstrate&r) a k tomu plyn etylen (&eEthene&r). Etylen je skvělé palivo do plynového generátoru.",
            "&aTip:&r Komora umí i uhlí + voda + kyslík = sirný prach a vodík."]),
        Q("hdpe", "HDPE plast", dep=["prc", "acid"], items=[("mekanism:hdpe_sheet", 4)], xp=40, d=[
            "HDPE je odolný plast. Substrát + kapalný etylen + kyslík v reakční komoře = HDPE peleta (&eHDPE Pellet&r).",
            "Komora dává etylen jako plyn. Na kapalinu ho převede rotační kondenzátor (&eRotary Condensentrator&r).",
            "3 pelety v obohacovací komoře = HDPE deska (&eHDPE Sheet&r).",
            "&aTip:&r HDPE desky potřebuješ na MekaSuit, solární neutronový aktivátor a plastové bloky."]),
        Q("robit", "Robit", dep=["atomic", "personal", "tablet"], items=[("mekanism:robit", 1)], xp=40, d=[
            "Robit (&eRobit&r) je malý robotický pomocník. Chodí za tebou, sbírá předměty ze země a má v sobě pec i pracovní stůl.",
            "Nabíjí se na nabíjecí podložce (&eChargepad&r). Je i součástí receptu na digitálního horníka.",
            "&aTip:&r Robitovi můžeš změnit vzhled – je na to advancement „A New Coat of Paint“."]),
        Q("teleporter", "Teleportér", dep=["atomic", "refined_glowstone"], items=[("mekanism:teleporter", 1)], xp=80, d=[
            "Teleportér (&eTeleporter&r) tě přenese k jinému teleportéru, i do jiné dimenze. Spotřebuje energii podle vzdálenosti.",
            "Postav svislý rám 3 bloky široký a 4 vysoký s prázdným otvorem 1×2 uprostřed. Samotný teleportér patří doprostřed spodní řady. Zbytek rámu je z 9 bloků &eTeleporter Frame&r.",
            "&aTip:&r Srdcem teleportéru je teleportační jádro (&eTeleportation Core&r) z atomové slitiny, diamantu, zlata a endových perel."]),
        Q("teleport_go", "Projdi teleportérem", dep=["teleporter"], tasks=[adv("mekanism:teleporter")], xp=40, icon="mekanism:teleporter_frame", d=[
            "Postav druhý teleportér a v okně obou nastav stejnou frekvenci.",
            "Oba teleportéry potřebují energii. Vejdi do rámu a přeneseš se k tomu druhému.",
            "&aTip:&r Frekvence může být soukromá, nebo veřejná pro všechny hráče."]),
        Q("miner", "Digitální horník", dep=["sorter", "robit", "teleporter"], items=[("mekanism:digital_miner", 1)], xp=100, d=[
            "Digitální horník (&eDigital Miner&r) těží bloky v okolí bez kopání tunelů – až do vzdálenosti 32 bloků.",
            "V okně nastav filtry (co má těžit, třeba jen rudy), poloměr a výšku. Volba &eSilk touch&r těží celé bloky.",
            "Vytěžené věci ukládá do sebe. Automatický výstup (&eAuto-eject&r) je pošle do truhly nebo transportéru.",
            "&aTip:&r Horník bere hodně energie. Vylepšení rychlosti ho zrychlí."]),
        Q("disassembler", "Atomový rozkladač", dep=["atomic", "tablet"], items=[("mekanism:atomic_disassembler", 1)], xp=50, d=[
            "Atomový rozkladač (&eAtomic Disassembler&r) je krumpáč, sekera i lopata v jednom. Běží na energii.",
            "Rychlost a režim těžby (třeba těžba celé žíly) přepneš Shift + kolečkem myši.",
            "&aTip:&r Nabiješ ho ve slotu energetické kostky nebo na nabíjecí podložce (&eChargepad&r)."]),
        Q("tools", "Mekanism Tools", dep=["steel"], items=[("mekanismtools:steel_paxel", 1)], xp=30, d=[
            "&bMekanism Tools&r přidává nástroje, štíty a brnění z osmia, bronzu, oceli, lazuritu, rafinovaného světlitu a rafinovaného obsidiánu.",
            "Paxel (&eSteel Paxel&r) je krumpáč, sekera a lopata v jednom. Vyrobíš ho z ocelového krumpáče, sekery, lopaty a dvou železných ingotů.",
            "&aTip:&r Ocel je dobrý začátek. Později přejdi na rafinovaný obsidián."]),
        Q("ro_armor", "Obsidiánové brnění", dep=["tools", "refined_obsidian"], items=[("mekanismtools:refined_obsidian_chestplate", 1)], xp=40, optional=True, d=[
            "Brnění z rafinovaného obsidiánu (&eRefined Obsidian Chestplate&r) je nejsilnější brnění z &bMekanism Tools&r.",
            "Vyrobíš ho stejně jako železné brnění, jen z ingotů rafinovaného obsidiánu.",
            "&aTip:&r Celou sadu doplní helma, kalhoty a boty ze stejného materiálu."]),
        Q("walkie", "Vysílačka", dep=["circuit", "steel"], items=[("mekanismadditions:walkie_talkie", 1)], xp=20, d=[
            "&bMekanism Additions&r přidává drobnosti: vysílačky, balony, plastové bloky a obsidiánový TNT.",
            "Vysílačka (&eWalkie-Talkie&r) slouží k hlasové komunikaci na zvoleném kanálu.",
            "&cPozor:&r Hlas funguje jen tehdy, když je na serveru zapnutý hlasový server Mekanismu. Ve výchozím nastavení je vypnutý."]),
        Q("otnt", "Obsidiánový TNT", dep=["walkie"], items=[("mekanismadditions:obsidian_tnt", 1)], xp=30, d=[
            "Obsidiánový TNT (&eObsidian TNT&r) vybuchne s poloměrem 12 bloků – obyčejný TNT má 4.",
            "Vyrobíš ho ze 3 TNT a 6 obsidiánu.",
            "&cPozor:&r Používej ho daleko od základny a zvířat."]),
        Q("plastic", "Plastové bloky", dep=["hdpe", "walkie"], items=[("mekanismadditions:white_plastic", 8)], xp=20, optional=True, d=[
            "Plastové bloky (&eWhite Plastic Block&r) vyrobíš ze 4 HDPE desek a barviva. Vyjdou 4 kusy v barvě barviva.",
            "Z nich jdou další varianty: kluzký plast, svítící plast, plastová cesta nebo zesílený plast.",
            "&aTip:&r Svítící panely (&eWhite Glow Panel&r) jsou pěkné osvětlení do základny."]),
        Q("meka", "MekaSuit", dep=["hdpe", "ultimate", "mekanism_power:polonium", "mekanism_power:induction"], items=[("mekanism:mekasuit_bodyarmor", 1)], xp=100, d=[
            "MekaSuit je nejlepší brnění v Mekanismu. Co umí, záleží na modulech, které do něj vložíš.",
            "Každý díl vyrobíš z netheritového dílu brnění, HDPE desek, ultimátního obvodu, indukčního článku (&eBasic Induction Cell&r) a polonia.",
            "&aTip:&r Moduly instaluješ v modifikační stanici (&eModification Station&r) – návod je v kapitole &bMekanism: pokročilé&r."]),
    ],
)

# =====================================================================================
# MEKANISM – pokročilé: generátory, jádro, QIO, MekaSuit
# =====================================================================================
MEK_POWER = dict(
    key="mekanism_power", group="tech", title="Mekanism: pokročilé",
    subtitle="Energie, jaderný reaktor, QIO a MekaSuit", icon="mekanismgenerators:fission_reactor_casing",
    quests=[
        Q("p_intro", "Velká energie", dep=["mekanism:heatgen"], tasks=[auto()], xp=10, s="Začátečník", icon="mekanismgenerators:heat_generator", **MS, d=[
            "Tahle kapitola navazuje na kapitolu &bMekanism&r. Naučíš se tu vyrábět hodně energie, skladovat ji a nakonec postavit jaderný a fúzní reaktor.",
            "Mekanism počítá energii v joulech (J), jiné mody ve FE. Převádí se samo – kabely Mekanismu napojíš i na stroje z jiných modů.",
            "&aTip:&r Začni jednoduchými generátory. Reaktory jsou na konci a jsou &cnebezpečné&r – čti pozorně každý quest."]),
        Q("bio_gen", "Bio-generátor", dep=["p_intro", "mekanism:biofuel", "mekanism:alloy"], items=[("mekanismgenerators:bio_generator", 1)], xp=25, d=[
            "Bio-generátor (&eBio-Generator&r) pálí bio palivo z drtiče. Je to jednoduchý zdroj energie, který jde snadno automatizovat.",
            "Bio palivo vlož do slotu. Generátor z něj udělá tekuté palivo a spaluje ho.",
            "&aTip:&r Napoj farmu na drtič a drtič na generátor – energie poteče sama."]),
        Q("adv_solar", "Pokročilý solár", dep=["p_intro", "mekanism:solar"], items=[("mekanismgenerators:advanced_solar_generator", 1)], xp=30, d=[
            "Pokročilý solární generátor (&eAdvanced Solar Generator&r) vyrábí víc energie než obyčejný.",
            "Vyrobíš ho ze 4 obyčejných solárních generátorů, infuzní slitiny a železa.",
            "&aTip:&r Stejně jako obyčejný funguje jen přes den pod volnou oblohou."]),
        Q("gas_gen", "Plynový generátor", dep=["p_intro", "mekanism:separator"], items=[("mekanismgenerators:gas_burning_generator", 1)], xp=40, d=[
            "Plynový generátor (&eGas-Burning Generator&r) spaluje plyny: vodík nebo etylen.",
            "Etylen z tlakové reakční komory je mnohem lepší – 1 mB etylenu dá mnohonásobně víc energie než 1 mB vodíku.",
            "&aTip:&r Etylen se vyrábí z bio paliva. Farma rostlin + drtič + reakční komora = stálý zdroj paliva."]),
        Q("lead", "Olovo", dep=["p_intro"], items=[("mekanism:raw_lead", 8)], xp=15, d=[
            "Olovo (&eLead Ore&r) těžíš jako ostatní rudy Mekanismu. Dobře chrání před radiací.",
            "Z olova je ochranný oblek, plášť jaderného reaktoru i části systému QIO.",
            "&aTip:&r Zpracuj ho ve strojích na zpracování rud – dostaneš víc ingotů."]),
        Q("uranium", "Uran", dep=["p_intro"], items=[("mekanism:raw_uranium", 8)], xp=20, d=[
            "Uran (&eUranium Ore&r) je surovina pro jaderné palivo. Uran v rudě není tolik radioaktivní, aby ti ublížil.",
            "Vytěžený uran (&eRaw Uranium&r) zpracuj na ingoty jako ostatní kovy.",
            "&cPozor:&r Radioaktivní je jaderný odpad z reaktoru a látky z něj (polonium, plutonium). Nikdy je nevypouštěj ven."]),
        Q("fluorite", "Fluorit", dep=["p_intro"], items=[("mekanism:fluorite_gem", 8)], xp=15, d=[
            "Fluorit (&eFluorite&r) najdeš hluboko pod zemí, níž než Y = 23. Rudu zpracuj v obohacovací komoře – z bloku rudy dá 6 kusů.",
            "Z fluoritu se vyrábí kyselina fluorovodíková na jaderné palivo. Jeho prach je potřeba na pelety z polonia a plutonia.",
            "&aTip:&r Fluoritový prach (&eFluorite Dust&r) dostaneš v drtiči."]),
        Q("hazmat", "Ochranný oblek", dep=["lead"], items=[("mekanism:hazmat_mask", 1), ("mekanism:hazmat_gown", 1), ("mekanism:hazmat_pants", 1), ("mekanism:hazmat_boots", 1)], xp=40, d=[
            "Ochranný oblek proti radiaci má 4 díly: masku (&eHazmat Mask&r), plášť (&eHazmat Gown&r), kalhoty (&eHazmat Pants&r) a boty (&eHazmat Boots&r).",
            "Vyrobíš je z olověných ingotů a oranžového barviva.",
            "&aTip:&r Nos ho vždy, když pracuješ s jaderným palivem nebo odpadem."]),
        Q("geiger", "Měření radiace", dep=["lead", "mekanism:circuit"], items=[("mekanism:geiger_counter", 1), ("mekanism:dosimeter", 1)], xp=20, d=[
            "Geigerův počítač (&eGeiger Counter&r) měří radiaci v okolí. Dozimetr (&eDosimeter&r) ukáže, kolik radiace jsi už dostal ty.",
            "Když počítač ukazuje zvýšenou radiaci, odejdi a vezmi si ochranný oblek.",
            "&aTip:&r Radiace v okolí časem sama klesá."]),
        Q("yellowcake", "Žlutý koláč", dep=["uranium", "mekanism:enrich"], items=[("mekanism:yellow_cake_uranium", 8)], xp=25, d=[
            "Žlutý koláč (&eYellow Cake Uranium&r) je první krok k jadernému palivu. Z 1 uranového ingotu udělá obohacovací komora 2 kusy.",
            "V chemickém oxidátoru z něj vznikne plyn oxid uraničitý.",
            "&aTip:&r Oxid uraničitý budeš potřebovat v dalším questu na jaderné palivo."]),
        Q("fissile", "Jaderné palivo", dep=["yellowcake", "fluorite", "mekanism:acid", "mekanism:dissolution"], items=[("mekanism:isotopic_centrifuge", 1)], xp=60, d=[
            "Jaderné palivo (&eFissile Fuel&r) se vyrábí ve třech krocích.",
            "1) Rozpouštěcí komora: fluorit + kyselina sírová = kyselina fluorovodíková. 2) Chemický infuzér: kyselina fluorovodíková + oxid uraničitý = fluorid uranový. 3) Izotopová odstředivka (&eIsotopic Centrifuge&r) z něj udělá palivo.",
            "&aTip:&r Palivo ukládej do chemických nádrží. Samo radioaktivní není, ale v reaktoru z něj vzniká radioaktivní odpad."]),
        Q("turbine", "Průmyslová turbína", dep=["p_intro", "mekanism:ultimate"], items=[("mekanismgenerators:rotational_complex", 1), ("mekanismgenerators:turbine_blade", 2), ("mekanismgenerators:electromagnetic_coil", 1), ("mekanismgenerators:turbine_vent", 1), ("mekanism:pressure_disperser", 1)], xp=80, d=[
            "Průmyslová turbína (&eIndustrial Turbine&r) mění páru na energii. Je to velká dutá stavba z pláště (&eTurbine Casing&r).",
            "Půdorys musí být čtverec s lichou délkou strany, třeba 5×5 nebo 7×7.",
            "Uprostřed je sloup rotorů (&eTurbine Rotor&r) s lopatkami (&eTurbine Blade&r). Na nejvyšší rotor patří rotační jednotka (&eRotational Complex&r) a kolem ní celá vrstva tlakových rozdělovačů (&ePressure Disperser&r) bez mezer.",
            "Nad ni polož cívky (&eElectromagnetic Coil&r) – musí se dotýkat sebe navzájem i rotační jednotky. Výpusti (&eTurbine Vent&r) dej do stěn na úroveň rotační jednotky nebo výš.",
            "{@pagebreak}",
            "Páru přiveď a energii odveď přes ventil (&eTurbine Valve&r).",
            "&aTip:&r Kondenzátory (&eSaturating Condenser&r) nad rotační jednotkou vrátí páru zpět jako vodu – ta se hodí pro reaktor."]),
        Q("fission", "Jaderný reaktor", dep=["fissile", "hazmat", "turbine"], items=[("mekanismgenerators:fission_reactor_casing", 16), ("mekanismgenerators:fission_reactor_port", 2), ("mekanismgenerators:fission_fuel_assembly", 1), ("mekanismgenerators:control_rod_assembly", 1)], xp=100, s="Expert", **MS, d=[
            "Jaderný reaktor (&eFission Reactor&r) spaluje jaderné palivo a vyrábí obrovské teplo. Tím ohřívá vodu na páru, ze které turbína udělá energii.",
            "Stavba: dutý kvádr z pláště (&eFission Reactor Casing&r), ve stěnách smí být sklo (&eReactor Glass&r). Uvnitř postav sloupy palivových článků (&eFission Fuel Assembly&r) a na vrch každého sloupu řídicí tyč (&eControl Rod Assembly&r).",
            "Do stěn dej porty (&eFission Reactor Port&r). Konfigurátorem jim nastavíš režim: vstup, výstup chladiva (pára) nebo výstup odpadu.",
            "{@pagebreak}",
            "&cBezpečnost:&r Nad 1200 K se reaktor začne poškozovat. Když poškození dosáhne 100 %, může vybuchnout a zamořit okolí radiací.",
            "Proto vždy měj dost vody na chlazení a odváděj páru. Začni s nízkým výkonem (&eRate Limit&r třeba 0,1 mB/t) a v okně sleduj teplotu. Tlačítkem &eSCRAM&r reaktor okamžitě vypneš.",
            "&aTip:&r Nejdřív postav turbínu a odvod páry, teprve potom reaktor zapni."]),
        Q("fission_safety", "Pojistka reaktoru", dep=["fission"], items=[("mekanismgenerators:fission_reactor_logic_adapter", 2)], xp=50, d=[
            "Logický adaptér (&eFission Reactor Logic Adapter&r) hlídá reaktor redstonem. Postav ho do stěny reaktoru.",
            "Jednoduchá pojistka: první adaptér nastav na &eHigh Temperature&r. Jeho signál přiveď do redstonové pochodně a pochodeň napoj na druhý adaptér v režimu &eActivation&r.",
            "Když se reaktor přehřeje, první adaptér vyšle signál, pochodeň zhasne a druhý adaptér reaktor vypne.",
            "&aTip:&r Stejně můžeš hlídat i poškození (&eDamage Critical&r) nebo plnou nádrž odpadu (&eCritical Waste Level&r)."]),
        Q("waste", "Jaderný odpad", dep=["fission"], items=[("mekanism:radioactive_waste_barrel", 1)], xp=40, d=[
            "Reaktor při spalování vyrábí jaderný odpad (&eNuclear Waste&r). Musíš ho odvádět portem v režimu výstupu odpadu.",
            "Ulož ho do sudu na radioaktivní odpad (&eRadioactive Waste Barrel&r), nebo ho rovnou zpracuj na polonium a plutonium.",
            "&cPozor:&r Odpad je radioaktivní. Když se sud, nádrž nebo trubka s odpadem zničí (třeba výbuchem), radiace unikne do okolí."]),
        Q("lithium", "Lithium", dep=["p_intro", "mekanism:evaporation", "mekanism:dissolution"], items=[("mekanism:dust_lithium", 8)], xp=40, d=[
            "Lithium potřebuješ na indukční matici a na fúzní palivo.",
            "Do odpařovací věže místo vody přiváděj solanku – vyrobí tekuté lithium. Rotační kondenzátor z něj udělá plyn a krystalizátor lithiový prach (&eLithium Dust&r).",
            "&aTip:&r Plynné lithium využije i solární neutronový aktivátor – vyrobí z něj tritium pro fúzi."]),
        Q("induction", "Indukční matice", dep=["lithium", "mekanism:cube"], items=[("mekanism:induction_casing", 8), ("mekanism:induction_port", 2), ("mekanism:basic_induction_cell", 1), ("mekanism:basic_induction_provider", 1)], xp=70, s="Pokročilý", **MS, d=[
            "Teď potřebuješ skladovat opravdu hodně energie. Indukční matice (&eInduction Matrix&r) je obří baterie z více bloků.",
            "Postav dutý kvádr z pláště (&eInduction Casing&r), stěny mohou být i ze skla (&eStructural Glass&r). Dovnitř dej články (&eBasic Induction Cell&r) – určují kapacitu – a poskytovatele (&eBasic Induction Provider&r) – určují rychlost.",
            "Do stěny dej dva porty (&eInduction Port&r) a konfigurátorem přepni jeden na výstup. Jeden port pak energii přijímá, druhý vydává.",
            "&aTip:&r Čím víc článků uvnitř, tím víc energie matice uloží."]),
        Q("sna", "Neutronový aktivátor", dep=["p_intro", "mekanism:hdpe", "mekanism:bronze", "mekanism:injection"], items=[("mekanism:solar_neutron_activator", 1)], xp=50, d=[
            "Solární neutronový aktivátor (&eSolar Neutron Activator&r) využívá sluneční záření. Musí vidět oblohu a nejlépe pracuje za jasného dne.",
            "Z jaderného odpadu vyrábí polonium, z plynného lithia tritium.",
            "&aTip:&r Déšť jeho práci zpomalí."]),
        Q("polonium", "Polonium", dep=["sna", "waste", "fluorite", "mekanism:prc"], items=[("mekanism:pellet_polonium", 1)], xp=70, d=[
            "Polonium vzniká v solárním neutronovém aktivátoru z jaderného odpadu (10 mB odpadu = 1 mB polonia).",
            "Peletu (&ePolonium Pellet&r) vyrobíš v tlakové reakční komoře: polonium + voda + fluoritový prach. Na 1 peletu je potřeba 1000 mB polonia.",
            "&aTip:&r Polonium je v MekaSuitu, modifikační stanici, přenosném QIO panelu a fúzním reaktoru."]),
        Q("plutonium", "Plutonium", dep=["waste", "fissile", "fluorite", "mekanism:prc"], items=[("mekanism:pellet_plutonium", 1)], xp=60, d=[
            "Plutonium vyrobí izotopová odstředivka z jaderného odpadu (10 mB odpadu = 1 mB plutonia).",
            "Peletu (&ePlutonium Pellet&r) vyrobíš stejně jako u polonia: v tlakové reakční komoře s vodou a fluoritovým prachem.",
            "&aTip:&r Plutoniové pelety jsou potřeba na plášť SPS."]),
        Q("laser", "Laser", dep=["p_intro", "mekanism:reinforced", "mekanism:cube"], items=[("mekanism:laser", 1), ("mekanism:laser_amplifier", 1)], xp=40, d=[
            "Laser (&eLaser&r) vystřelí paprsek energie. Ničí bloky, na které míří, a &czraní i tebe&r!",
            "Zesilovač (&eLaser Amplifier&r) sbírá energii z laserů a vystřelí ji podle nastavení, třeba na redstonový signál.",
            "&aTip:&r Laser a zesilovač budeš potřebovat k zapálení fúzního reaktoru a na nabitou cívku pro SPS."]),
        Q("sps", "SPS: antihmota", dep=["polonium", "plutonium", "laser", "induction"], items=[("mekanism:sps_casing", 4), ("mekanism:sps_port", 2), ("mekanism:supercharged_coil", 1)], xp=100, d=[
            "Superkritický fázový posunovač (SPS) mění polonium na antihmotu. Spotřebuje na to obrovské množství energie.",
            "Je to velká stavba z pláště (&eSPS Casing&r) a portů (&eSPS Port&r). Energii dodáš přes nabitou cívku (&eSupercharged Coil&r) položenou na port.",
            "&aTip:&r Je to konec Mekanismu – připrav si indukční matici plnou energie."]),
        Q("antimatter", "Antihmota", dep=["sps"], items=[("mekanism:pellet_antimatter", 1)], xp=100, d=[
            "Antihmota vzniká v SPS jako plyn. Krystalizátor z 1000 mB udělá peletu antihmoty (&eAntimatter Pellet&r).",
            "Pelety potřebuješ na antiprotonový nukleosyntetizátor.",
            "&aTip:&r Antihmotu ukládej do chemických nádrží, ať o ni nepřijdeš."]),
        Q("nucleo", "Přeměna hmoty", dep=["antimatter"], items=[("mekanism:antiprotonic_nucleosynthesizer", 1)], xp=100, d=[
            "Antiprotonový nukleosyntetizátor (&eAntiprotonic Nucleosynthesizer&r) přeměňuje předměty pomocí antihmoty a hodně energie.",
            "Například: uhlí → diamant, diamant → smaragd, cínový ingot → železný ingot, obsidián → plačící obsidián.",
            "&aTip:&r Všechny přeměny ukáže JEI."]),
        Q("deuterium", "Deuterium", dep=["p_intro", "mekanism:pipe", "mekanism:separator", "mekanism:tin"], items=[("mekanism:upgrade_filter", 1)], xp=30, d=[
            "Deuterium je první složka fúzního paliva. Vzniká z těžké vody (&eHeavy Water&r).",
            "Elektrickou pumpu vylepši filtrem (&eFilter Upgrade&r) – místo vody bude čerpat těžkou vodu. Elektrolytický separátor ji rozloží na deuterium a kyslík.",
            "&aTip:&r Pumpa potřebuje hodně vody. Polož ji nad velký zdroj, třeba moře."]),
        Q("dt_fuel", "Fúzní palivo", dep=["deuterium", "sna", "lithium"], items=[("mekanismgenerators:hohlraum", 1)], xp=50, d=[
            "Fúzní palivo D-T vznikne v chemickém infuzéru z deuteria a tritia. Tritium vyrobí solární neutronový aktivátor z plynného lithia.",
            "Hohlraum (&eHohlraum&r) vyrobíš v infuzéru ze 4 zlatých prachů a uhlíku. Naplň ho palivem D-T – vlož ho do slotu chemické nádrže s palivem.",
            "&aTip:&r Hohlraum se při zapálení reaktoru spotřebuje."]),
        Q("fusion", "Fúzní reaktor", dep=["dt_fuel", "laser", "polonium"], items=[("mekanismgenerators:fusion_reactor_controller", 1), ("mekanismgenerators:fusion_reactor_frame", 16), ("mekanismgenerators:fusion_reactor_port", 2), ("mekanismgenerators:laser_focus_matrix", 1)], xp=100, d=[
            "Fúzní reaktor (&eFusion Reactor&r) je nejsilnější zdroj energie v Mekanismu. Spaluje deuterium a tritium.",
            "Stavba má pevný tvar v prostoru 5×5×5 bloků: každá stěna vypadá jako kosočtverec – uprostřed 3×3 bloky a k tomu po jednom bloku uprostřed každé strany.",
            "Ovladač (&eFusion Reactor Controller&r) musí být uprostřed horní stěny. Ostatní bloky stěn jsou rámy (&eFusion Reactor Frame&r).",
            "Porty (&eFusion Reactor Port&r), sklo a laserovou matici (&eLaser Focus Matrix&r) smíš dát jen do středního kříže stěny: prostřední blok a 4 bloky kolem něj.",
            "{@pagebreak}",
            "Zapálení: do ovladače vlož naplněný hohlraum. Zesilovač laseru nabij energií a vystřel ho do laserové matice. Když je plazma dost horká, reaktor se zapálí.",
            "Pak do portů posílej deuterium a tritium a energii odváděj z portu.",
            "&aTip:&r V okně reaktoru nastavíš rychlost vstřikování paliva (&eInjection Rate&r)."]),
        Q("qio", "QIO úložiště", dep=["p_intro", "lead", "mekanism:ultimate", "mekanism:teleporter", "mekanism:personal"], items=[("mekanism:qio_drive_array", 1), ("mekanism:qio_drive_base", 1), ("mekanism:qio_dashboard", 1)], xp=80, d=[
            "QIO (&eQuantum Item Orchestration&r) je digitální úložiště Mekanismu bez kabelů. Všechno spojuje frekvence.",
            "Do pole disků (&eQIO Drive Array&r) vlož disky (&eQIO Drive&r). Panel (&eQIO Dashboard&r) ukazuje obsah a má v sobě pracovní stůl. V okně každého bloku nastav stejnou frekvenci.",
            "&aTip:&r Bloky QIO mohou stát daleko od sebe. Stačí jim stejná frekvence."]),
        Q("qio_io", "QIO dovoz a vývoz", dep=["qio"], items=[("mekanism:qio_importer", 1), ("mekanism:qio_exporter", 1)], xp=40, d=[
            "Dovozník (&eQIO Importer&r) a vývozník (&eQIO Exporter&r) se pokládají na blok, třeba na truhlu nebo stroj.",
            "Dovozník bere věci z bloku do QIO, vývozník je z QIO do bloku dává. Ve filtrech nastavíš, které věci.",
            "&aTip:&r Tak napojíš QIO na stroje – třeba vývozník na pec a dovozník na její výstup."]),
        Q("modstation", "Modifikační stanice", dep=["mekanism:meka"], items=[("mekanism:modification_station", 1), ("mekanism:module_base", 2)], xp=50, d=[
            "Modifikační stanice (&eModification Station&r) instaluje moduly do MekaSuitu a Meka-Toolu.",
            "Vlož do stanice díl brnění nebo nástroj a pak do něj přidej modul. Základem každého modulu je &eModule Base&r z HDPE, cínu a bronzu.",
            "&aTip:&r Každý modul má v okně vlastní nastavení – třeba ho vypnout nebo změnit jeho sílu."]),
        Q("meka_tool", "Meka-Tool", dep=["mekanism:meka", "mekanism:disassembler"], items=[("mekanism:meka_tool", 1)], xp=60, d=[
            "Meka-Tool (&eMeka-Tool&r) je vylepšený atomový rozkladač. Těží, kope i seká a dávají se do něj moduly.",
            "Užitečné moduly: rychlejší těžba (&eExcavation Escalation Unit&r), těžba celé žíly (&eVein Mining Unit&r), Něžný dotek nebo Štěstí.",
            "&aTip:&r Meka-Tool spotřebuje hodně energie – dej mu modul energie."]),
        Q("mod_energy", "Modul energie", dep=["modstation"], items=[("mekanism:module_energy_unit", 1)], xp=40, d=[
            "Modul energie (&eEnergy Unit&r) zvětší zásobník energie obleku nebo nástroje.",
            "Vyrobíš ho ze základu modulu, indukčního článku, infuzní slitiny a HDPE desek.",
            "&aTip:&r Do jednoho dílu jde vložit víc stejných modulů – kolik, ukáže modifikační stanice."]),
        Q("mekasuit_full", "Celý MekaSuit", dep=["meka_tool", "mod_energy"], tasks=[adv("mekanism:mekasuit")], xp=100, icon="mekanism:mekasuit_helmet", d=[
            "Obleč celý MekaSuit – helmu, hrudní díl, kalhoty a boty – a měj u sebe Meka-Tool.",
            "Teď můžeš do obleku přidávat další moduly: jetpack, dýchání pod vodou, noční vidění, magnet a mnoho dalších.",
            "&aTip:&r Na plné vybavení všemi moduly je advancement „True Dedication“."]),
    ],
)

# =====================================================================================
# ÚLOŽIŠTĚ – truhly, šuplíky, Sophisticated Storage, Building Gadgets, Extended Crafting
# (+ první kroky AE2 a RS z původní kapitoly; podrobně v kapitolách ae2 a refined_storage)
# =====================================================================================
STORAGE = dict(
    key="storage", group="tech", title="Úložiště",
    subtitle="Truhly, šuplíky, stavební nástroje a velké stoly", icon="storagedrawers:controller",
    quests=[
        Q("st_intro", "Kam s věcmi?", tasks=[auto()], xp=10, s="Začátečník", icon="ironchest:iron_chest", **MS, d=[
            "V téhle kapitole najdeš všechno o ukládání věcí: větší truhly, šuplíky na velké množství jednoho předmětu a propojené úložiště.",
            "Digitální úložiště má vlastní kapitoly: &bApplied Energistics 2&r a &bRefined Storage&r. Tady jsou jen jejich první kroky.",
            "&aTip:&r Na konci kapitoly jsou stavební nástroje (&bBuilding Gadgets&r) a velké pracovní stoly (&bExtended Crafting&r)."]),
        Q("chest", "Lepší truhla", dep=["st_intro"], items=[("ironchest:iron_chest", 1)], xp=15, d=[
            "&bIron Chests&r přidává větší truhly: měděnou, železnou, zlatou, diamantovou, krystalovou a obsidiánovou.",
            "Železnou truhlu (&eIron Chest&r) vyrobíš z obyčejné truhly a 8 železných ingotů.",
            "&aTip:&r Každá další úroveň má víc slotů."]),
        Q("chest_up", "Vylepšení truhly", dep=["chest"], items=[("ironchest:iron_to_gold_chest_upgrade", 1)], xp=15, d=[
            "Vylepšení truhly promění truhlu na vyšší úroveň i s obsahem – nemusíš nic přendávat. Vylepšení &eIron to Gold Chest Upgrade&r udělá ze železné truhly zlatou.",
            "Drž ho v ruce a klikni na truhlu Shift + pravým tlačítkem.",
            "&aTip:&r Obyčejnou truhlu z Minecraftu vylepšíš na železnou pomocí &eWood to Iron Chest Upgrade&r."]),
        Q("ender", "Ender Storage", dep=["st_intro"], items=[("enderstorage:ender_chest", 1), ("enderstorage:ender_pouch", 1)], xp=40, d=[
            "&bEnder Storage&r: truhly propojené kódem ze 3 barev. Stejné barvy = stejný obsah, i přes dimenze.",
            "Barvu změníš tak, že klikneš barvivem na jeden z barevných proužků na víku truhly.",
            "Endová kapsa (&eEnder Pouch&r) otevře truhlu se stejným kódem odkudkoli. Kód můžeš sdílet s kamarády."]),
        Q("drawers", "Šuplíky", dep=["st_intro"], items=[("storagedrawers:oak_full_drawers_1", 1)], xp=15, d=[
            "&bStorage Drawers&r jsou šuplíky na velké množství jednoho předmětu. Co je uvnitř, vidíš přímo zepředu.",
            "Šuplík (&eOak Drawers 1x1&r) vyrobíš z dubových prken a truhly. Jsou i verze se 2 a 4 přihrádkami.",
            "Pravým tlačítkem vložíš předmět z ruky. Rychlým dvojklikem pravým tlačítkem vložíš všechny stejné předměty z inventáře. Levým tlačítkem věci bereš."]),
        Q("compact", "Zhušťovací šuplík", dep=["drawers"], items=[("storagedrawers:compacting_drawers_3", 1)], xp=25, d=[
            "Zhušťovací šuplík (&eCompacting Drawers (3-Tier)&r) sám převádí mezi úrovněmi: nugety ↔ ingoty ↔ bloky.",
            "Vlož do něj třeba železné ingoty a hned si můžeš vzít i bloky nebo nugety.",
            "&aTip:&r Skvělý na kovy, redstone, uhlí nebo lazurit."]),
        Q("d_upgrade", "Větší šuplíky", dep=["drawers"], items=[("storagedrawers:obsidian_storage_upgrade", 1)], xp=20, d=[
            "Vylepšení kapacity (&eStorage Upgrade (I)&r a vyšší) zvětší, kolik se do šuplíku vejde. Vyrábí se ze šablony (&eUpgrade Template&r) a materiálu: obsidiánu, mědi, železa, zlata, smaragdu, diamantu nebo netheritu.",
            "Vylepšení vložíš tak, že s ním v ruce klikneš pravým tlačítkem na šuplík.",
            "&aTip:&r Vylepšení prázdnoty (&eVoid Upgrade&r) maže, co se už nevejde – hodí se k farmám."]),
        Q("dcontroller", "Ovladač šuplíků", dep=["compact"], items=[("storagedrawers:controller", 1)], xp=40, d=[
            "Ovladač šuplíků (&eDrawer Controller&r) spojí šuplíky, které se ho dotýkají – i přes další šuplíky.",
            "Když do ovladače vložíš předmět, sám ho pošle do správného šuplíku. Násypkou nebo trubkou do něj můžeš posílat celé dodávky.",
            "&aTip:&r Vzdálený šuplík připojíš vylepšením &eRemote Upgrade&r."]),
        Q("sophchest", "Sophisticated Storage", dep=["st_intro"], items=[("sophisticatedstorage:chest", 1)], xp=20, d=[
            "&bSophisticated Storage&r: truhly a sudy, do kterých jdou vkládat vylepšení – stejně jako do batohu.",
            "Sofistikovanou truhlu vyrobíš z obyčejné truhly a páky.",
            "&aTip:&r Truhly a sudy jdou vylepšovat na měděné, železné, zlaté, diamantové a netheritové. Vyšší úroveň = víc slotů i víc míst na vylepšení."]),
        Q("ss_tier", "Vylepšení úrovně", dep=["sophchest"], items=[("sophisticatedstorage:basic_to_iron_tier_upgrade", 1)], xp=20, d=[
            "Vylepšení úrovně (&eBasic to Iron Tier Upgrade&r) zvětší sofistikovanou truhlu nebo sud přímo na místě – obsah zůstane uvnitř.",
            "Drž ho v ruce a klikni pravým tlačítkem na postavenou truhlu.",
            "&aTip:&r Vylepšení &eBasic Tier Upgrade&r promění obyčejnou truhlu nebo sud z Minecraftu na sofistikovanou verzi."]),
        Q("ss_base", "Vylepšení truhel", dep=["sophchest"], items=[("sophisticatedstorage:upgrade_base", 1), ("sophisticatedstorage:hopper_upgrade", 1)], xp=25, d=[
            "Vylepšení se vkládají do slotů pro vylepšení na boku okna truhly. Většina se vyrábí ze základu (&eUpgrade Base&r) z prken a železa.",
            "Násypkové vylepšení (&eHopper Upgrade&r) samo bere věci z bloku nad truhlou a posílá je do bloku pod ní.",
            "&aTip:&r Další užitečná: sběrné (&ePickup Upgrade&r), filtr (&eFilter Upgrade&r) nebo tavení (&eSmelting Upgrade&r)."]),
        Q("ss_compact", "Zhušťování a mazání", dep=["ss_base", "welcome:backpack"], items=[("sophisticatedstorage:compacting_upgrade", 1)], xp=30, d=[
            "Zhušťovací vylepšení (&eCompacting Upgrade&r) samo zhušťuje věci. Základní verze zvládá jen recepty 2×2, pokročilá i 3×3.",
            "Vyrobíš ho ze základu vylepšení, pístů, železa a redstonu. Jde i ze zhušťovacího vylepšení pro batoh (&bSophisticated Backpacks&r) a prken.",
            "&aTip:&r Vylepšení &eVoid Upgrade&r maže nechtěné věci – třeba hlínu z kopání."]),
        Q("ss_stack", "Víc kusů do slotu", dep=["ss_base"], items=[("sophisticatedstorage:stack_upgrade_tier_1", 1)], xp=30, d=[
            "Vylepšení stohování (&eStack Upgrade Tier 1&r) zvětší, kolik kusů se vejde do jednoho slotu.",
            "Vyšší úrovně dávají ještě víc. Do jedné truhly se tak vejde obrovské množství věcí.",
            "&aTip:&r První úroveň vyrobíš z kmenů a základu vylepšení."]),
        Q("sophcontroller", "Ovladač úložiště", dep=["ss_tier"], items=[("sophisticatedstorage:controller", 1)], xp=40, s="Pokročilý", **MS, d=[
            "Teď z jednotlivých truhel uděláš jeden sklad. Ovladač úložiště (&eStorage Controller&r) spojí sofistikované truhly a sudy, které se ho dotýkají – i přes další truhly.",
            "Věci vložené do ovladače se samy uloží tam, kde je pro ně místo. Násypkou nebo trubkou do něj můžeš posílat celé dodávky.",
            "&aTip:&r Truhly dál od ovladače připojíš spojkou (&eStorage Link&r)."]),
        Q("ss_link", "Spojka a nástroj", dep=["sophcontroller"], items=[("sophisticatedstorage:storage_link", 1), ("sophisticatedstorage:storage_tool", 1)], xp=30, d=[
            "Spojka (&eStorage Link&r) připojí k ovladači skupinu truhel, která se ho nedotýká.",
            "Propoj je nástrojem (&eStorage Tool&r) – použij ho na ovladač a na spojku.",
            "&aTip:&r Nástroj umí i zamknout sloty nebo skrýt čísla na sudech. Režim přepneš Shift + kolečkem myši."]),
        Q("ss_tape", "Stěhování truhly", dep=["sophchest"], items=[("sophisticatedstorage:packing_tape", 1)], xp=20, d=[
            "Balicí páska (&ePacking Tape&r) ti dovolí přenést plnou truhlu i s obsahem.",
            "Klikni páskou pravým tlačítkem na truhlu nebo sud a pak ho vykopej. Obsah zůstane uvnitř. Páska vydrží jen několik použití.",
            "&aTip:&r Díky doplňku pro Create fungují sofistikované truhly a sudy i na pohyblivých strojích z Create (vlaky, vozíky) jako jejich úložiště."]),
        Q("gadget", "Building Gadgets", dep=["st_intro"], items=[("buildinggadgets2:gadget_building", 1)], xp=40, d=[
            "&bBuilding Gadgets&r: nástroje, které staví mnoho bloků najednou. Běží na energii (FE) – nabiješ je třeba v energetické kostce Mekanismu.",
            "Stavební nástroj (&eBuilding Gadget&r): blok vyber Shift + pravým tlačítkem a pak stav celé řady nebo plochy. Menu s režimy a velikostí otevřeš klávesou G.",
            "&aTip:&r Chyba? Klávesa U vrátí poslední stavbu zpět."]),
        Q("bg_exchange", "Výměna bloků", dep=["gadget"], items=[("buildinggadgets2:gadget_exchanging", 1)], xp=30, d=[
            "Výměnný nástroj (&eExchanging Gadget&r) nahradí bloky, které už stojí, jiným blokem.",
            "Nový blok vyber Shift + pravým tlačítkem a klikni na stěnu – vymění se celá plocha podle nastavené velikosti.",
            "&aTip:&r Skvělé na přestavbu domu z hlíny na kámen."]),
        Q("copypaste", "Kopírování staveb", dep=["gadget"], items=[("buildinggadgets2:gadget_copy_paste", 1)], xp=60, d=[
            "Kopírovací nástroj (&eCopy Paste Gadget&r) zkopíruje celou stavbu a postaví ji jinde.",
            "V režimu kopírování označ dva rohy oblasti, pak přepni na vkládání a stavbu polož. Bloky se berou z tvého inventáře.",
            "&aTip:&r Hodí se na opakující se stavby – domy, farmy nebo stroje z Create."]),
        Q("bg_cut", "Přesun staveb", dep=["copypaste"], items=[("buildinggadgets2:gadget_cut_paste", 1)], xp=40, optional=True, d=[
            "Vystřihovací nástroj (&eCut Paste Gadget&r) stavbu nekopíruje, ale přesune: na původním místě zmizí a objeví se jinde.",
            "Spotřebuje hodně energie, tak ho před použitím nabij.",
            "&aTip:&r Ideální, když chceš celou základnu posunout o kus dál."]),
        Q("bg_template", "Šablony staveb", dep=["copypaste"], items=[("buildinggadgets2:template_manager", 1)], xp=30, optional=True, d=[
            "Správce šablon (&eTemplate Manager&r) uloží zkopírovanou stavbu do šablony (&eTemplate&r).",
            "Šablonu si můžeš schovat nebo dát kamarádovi a stavbu pak postavit znovu.",
            "&aTip:&r Hodí se na výměnu návrhů staveb mezi hráči na serveru."]),
        Q("ec_iron", "Extended Crafting", dep=["st_intro"], items=[("extendedcrafting:black_iron_ingot", 4)], xp=20, d=[
            "&bExtended Crafting&r přidává větší pracovní stoly (3×3 až 9×9) a zvláštní způsoby výroby.",
            "Začni černým železem (&eBlack Iron Ingot&r): železný ingot + černé barvivo.",
            "&aTip:&r V tomhle packu se na velkých stolech vyrábějí jen materiály z &bExtended Crafting&r. Je to výzva navíc."]),
        Q("ec_table", "Velký pracovní stůl", dep=["ec_iron"], items=[("extendedcrafting:basic_table", 1)], xp=30, d=[
            "Základní stůl (&eBasic Crafting Table&r) je 3×3 stůl, který si pamatuje obsah, i když ho zavřeš.",
            "Potřebuješ na něj součástky (&eBasic Component&r) a katalyzátor (&eBasic Catalyst&r) z černého železa a luminescence (&eLuminessence&r).",
            "&aTip:&r Další stoly: pokročilý 5×5, elitní 7×7 a ultimátní 9×9. Každý se vyrábí z předchozího."]),
        Q("ec_ender", "Endový výrobník", dep=["ec_iron"], items=[("extendedcrafting:ender_crafter", 1), ("extendedcrafting:ender_alternator", 2)], xp=40, optional=True, d=[
            "Endový výrobník (&eEnder Crafter&r) vyrábí pomalu a bez energie. Kolem něj do 3 bloků postav endové alternátory (&eEnder Alternator&r) – čím víc, tím rychleji.",
            "Vyrábí se v něm třeba endová hvězda (&eEnder Star&r) z netherové hvězdy a endových očí.",
            "&aTip:&r Endový ingot (&eEnder Ingot&r) = železný ingot + endová perla."]),
        Q("ec_flux", "Fluxový výrobník", dep=["ec_iron"], items=[("extendedcrafting:flux_crafter", 1), ("extendedcrafting:flux_alternator", 2)], xp=40, optional=True, d=[
            "Fluxový výrobník (&eFlux Crafter&r) funguje jako endový, ale potřebuje energii (FE). Dodávají mu ji fluxové alternátory (&eFlux Alternator&r) do 3 bloků kolem.",
            "Alternátory napoj kabely na zdroj energie, třeba na generátor Mekanismu nebo alternátor z &bCreate Crafts & Additions&r.",
            "&aTip:&r Vyrábí se v něm fluxová hvězda (&eFlux Star&r) a vylepšený redstonový ingot (&eEnhanced Redstone Ingot&r)."]),
        Q("ec_crystaltine", "Krystaltin", dep=["ec_table"], items=[("extendedcrafting:elite_table", 1), ("extendedcrafting:crystaltine_ingot", 4)], xp=80, s="Expert", **MS, d=[
            "Krystaltin (&eCrystaltine Ingot&r) je vzácný materiál z elitního stolu (&eElite Crafting Table&r) 7×7.",
            "Recept: diamanty, lazurit, železo, zlato a dvě netherové hvězdy. Vyjdou 4 ingoty.",
            "&aTip:&r Na elitní stůl potřebuješ nejdřív pokročilý stůl (&eAdvanced Crafting Table&r)."]),
        # --- původní questy AE2 a RS (podrobně v kapitolách ae2 a refined_storage) ---
        Q("ae_meteor", "AE2: certusový křemen", dep=["st_intro"], items=[("ae2:certus_quartz_crystal", 8)], xp=30, d=[
            "&bApplied Energistics 2&r (AE2) je digitální úložiště a automatická výroba. Začíná se certusovým křemenem (&eCertus Quartz Crystal&r) z meteoritu.",
            "Podrobný návod krok za krokem najdeš v kapitole &bApplied Energistics 2&r."]),
        Q("ae_charger", "AE2: nabíječka a fluix", dep=["ae_meteor", "ae2:ae_charged"], items=[("ae2:charger", 1), ("ae2:fluix_crystal", 8)], xp=40, d=[
            "Nabíječka (&eCharger&r) nabíjí certusový křemen. Vyrobíš ji ze železa a mědi.",
            "Fluixový krystal (&eFluix Crystal&r): hoď do vody nabitý certus, redstone a netherový křemen. Vzniknou 2 fluixové krystaly."]),
        Q("ae_inscriber", "AE2: razítkovač", dep=["ae_charger", "ae2:ae_presses"], items=[("ae2:inscriber", 1)], xp=40, d=[
            "Razítkovač (&eInscriber&r) lisuje pomocí lisů z meteoritu plošné spoje a procesory.",
            "Vyrobíš ho ze železa, pístu a mědi."]),
        Q("ae_proc", "AE2: procesory", dep=["ae_inscriber", "ae2:ae_circuits"], items=[("ae2:logic_processor", 4), ("ae2:calculation_processor", 4), ("ae2:engineering_processor", 4)], xp=60, d=[
            "Tři druhy procesorů: logický (&eLogic Processor&r), výpočetní (&eCalculation Processor&r) a inženýrský (&eEngineering Processor&r).",
            "V razítkovači: vytištěný obvod nahoru, redstone doprostřed, vytištěný křemík dolů."]),
        Q("ae_drive", "AE2: první síť", dep=["ae_proc", "ae2:ae_energy"], items=[("ae2:controller", 1), ("ae2:drive", 1), ("ae2:terminal", 1), ("ae2:item_storage_cell_1k", 1)], xp=80, d=[
            "Disková jednotka (&eME Drive&r) s paměťovými buňkami + terminál (&eME Terminal&r) = všechny věci na jedné obrazovce s vyhledáváním.",
            "Zařízení spoj kabely a dodej energii. Ovladač (&eME Controller&r) potřebuješ, až bude mít síť víc než 8 zařízení – vysvětlení najdeš v kapitole &bApplied Energistics 2&r."]),
        Q("ae_craft", "AE2: automatická výroba", dep=["ae_drive", "ae2:ae_pattern_term"], items=[("ae2:pattern_provider", 1), ("ae2:molecular_assembler", 1), ("ae2:crafting_unit", 1)], xp=100, d=[
            "Poskytovatel vzorů (&eME Pattern Provider&r) posílá suroviny podle vzorů do sousedních bloků. Molekulární sestavovač (&eMolecular Assembler&r) vedle něj vyrábí recepty z pracovního stolu.",
            "Výrobní jednotka (&eCrafting Unit&r) je základ výrobního procesoru (CPU), který zakázky řídí.",
            "Vyrobitelnou věc pak v terminálu vyber a zadej počet. Pokud ji už máš, klikni na ni prostředním tlačítkem myši."]),
        Q("ae_wireless", "AE2: bezdrátový terminál", dep=["ae_drive"], items=[("ae2:wireless_terminal", 1), ("ae2:wireless_access_point", 1)], xp=60, d=[
            "Bezdrátový přístupový bod (&eME Wireless Access Point&r) zpřístupní síť na dálku. Potřebuje kanál.",
            "Bezdrátový terminál (&eWireless Terminal&r) propojíš se sítí tak, že ho vložíš do slotu v přístupovém bodu. Pak ho nabij."]),
        Q("rs_start", "RS: ovladač", dep=["st_intro", "refined_storage:rs_processors", "refined_storage:rs_casing"], items=[("refinedstorage:controller", 1)], xp=40, d=[
            "Ovladač (&eController&r) je srdce sítě &bRefined Storage&r. Dodává síti energii – napoj na něj zdroj FE, třeba generátor Mekanismu.",
            "Podrobný postup najdeš v kapitole &bRefined Storage&r. Vyber si pro základnu jeden systém: AE2, nebo Refined Storage."]),
        Q("rs_disk", "RS: disky a mřížka", dep=["rs_start", "refined_storage:rs_cores"], items=[("refinedstorage:disk_drive", 1), ("refinedstorage:1k_storage_disk", 1), ("refinedstorage:grid", 1)], xp=60, d=[
            "Do diskové jednotky (&eDisk Drive&r) vlož disk (&e1k Storage Disk&r) – pojme 1 000 předmětů.",
            "V mřížce (&eGrid&r) vidíš všechno, co je v síti, a můžeš to vkládat i brát."]),
        Q("rs_craft", "RS: automatická výroba", dep=["rs_disk", "refined_storage:rs_pattern_grid"], items=[("refinedstorage:autocrafter", 1), ("refinedstorage:pattern", 4)], xp=80, d=[
            "Do automatického výrobníku (&eAutocrafter&r) vlož zapsané vzory (&ePattern&r). Recepty z pracovního stolu vyrobí sám.",
            "Zpracovací vzory (třeba pro pec) posílá do bloku, na který je natočený. Výsledek se musí vrátit do sítě."]),
    ],
)

# =====================================================================================
# APPLIED ENERGISTICS 2
# =====================================================================================
AE2 = dict(
    key="ae2", group="tech", title="Applied Energistics 2",
    subtitle="Digitální úložiště a automatická výroba", icon="ae2:controller",
    quests=[
        Q("ae_intro", "Co je AE2", tasks=[auto()], xp=10, s="Začátečník", icon="ae2:certus_quartz_crystal", **MS, d=[
            "&bApplied Energistics 2&r (AE2) ukládá věci jako data do paměťových buněk. Všechno pak najdeš na jedné obrazovce a stroje ti mohou věci samy vyrábět.",
            "Postup: meteorit → certus a fluix → lisy a procesory → první síť → kanály → automatická výroba. Některé kroky jsou v kapitole &bÚložiště&r (mají v názvu „AE2:“).",
            "&aTip:&r AE2 má v sobě výborného průvodce: v inventáři najeď na předmět z AE2 a podrž klávesu G."]),
        Q("ae_compass", "Meteoritový kompas", dep=["ae_intro"], items=[("ae2:meteorite_compass", 1)], xp=20, d=[
            "Meteority jsou začátek AE2. Najdeš je podle velkého kráteru v krajině, nebo pomocí meteoritového kompasu (&eMeteorite Compass&r).",
            "Kompas vyrobíš v nabíječce (&eCharger&r). Nabíječku vyrobíš ze železa a mědi. Polož ji, vlož do ní obyčejný kompas a dodej energii.",
            "Bez jiného zdroje energie použij kliku (&eWooden Crank&r): polož ji na nabíječku shora nebo zespodu a klikej na ni pravým tlačítkem."]),
        Q("ae_find", "Najdi meteorit", dep=["ae_compass"], tasks=[structure("ae2:meteorite")], xp=30, icon="ae2:sky_stone_block", d=[
            "Dojdi k meteoritu (stavba &eMeteorite&r). Je to kráter s koulí z nebeského kamene (&eSky Stone&r).",
            "Prokopej se do středu. Najdeš certusový křemen, rostoucí krystaly, pučící certus a uprostřed tajemnou kostku (&eMysterious Cube&r).",
            "Vykopej tajemnou kostku obyčejným krumpáčem, ne Něžným dotekem. Vypadnou z ní všechny lisy pro razítkovač (&eInscriber&r)."]),
        Q("ae_presses", "Lisy", dep=["ae_find"], tasks=[adv("ae2:main/presses")], xp=30, icon="ae2:logic_processor_press", d=[
            "Lisy (&eInscriber Silicon Press&r, &eInscriber Logic Press&r, &eInscriber Calculation Press&r, &eInscriber Engineering Press&r) jsou potřeba na výrobu procesorů.",
            "Když lis ztratíš, nic se neděje: razítkovač umí každý lis zkopírovat z bloku železa.",
            "&aTip:&r Lisy si přesto dobře schovej, třeba hned do truhly u razítkovače."]),
        Q("ae_budding", "Pučící certus", dep=["ae_find"], items=[("ae2:damaged_budding_quartz", 1)], xp=25, d=[
            "Pučící certus (&eBudding Certus Quartz&r) je blok, na kterém rostou krystaly certusu – podobně jako ametyst.",
            "Bez Něžného doteku se při vykopání zhorší o jednu úroveň. Bezvadný (&eFlawless Budding Certus Quartz&r) se zhorší vždy, i s Něžným dotekem. Proto ho nech na místě.",
            "&aTip:&r Nový pučící blok vyrobíš tak, že hodíš do vody certusový blok (&eCertus Quartz Block&r) a nabitý certus. Vznikne &eDamaged Budding Certus Quartz&r."]),
        Q("ae_charged", "Nabitý certus", dep=["ae_compass", "storage:ae_meteor"], tasks=[adv("ae2:main/charged_quartz")], xp=25, icon="ae2:charged_certus_quartz_crystal", d=[
            "Certusový krystal vlož do nabíječky – vznikne nabitý certus (&eCharged Certus Quartz Crystal&r).",
            "Nabitý certus hozený do vody spolu s redstonem a netherovým křemenem se změní na 2 fluixové krystaly (&eFluix Crystal&r).",
            "&aTip:&r Nabitý certus + certusový prach ve vodě = 2 nové certusové krystaly. Nabíjet jde i Teslovou cívkou (&eTesla Coil&r) z &bCreate Crafts & Additions&r."]),
        Q("ae_accel", "Pěstování certusu", dep=["ae_budding", "storage:ae_charger", "ae_cables"], items=[("ae2:growth_accelerator", 1), ("ae2:crank", 1)], xp=40, d=[
            "Krystaly na pučícím certusu rostou samy velmi pomalu. Urychlovač růstu (&eGrowth Accelerator&r) položený vedle bloku je hodně zrychlí.",
            "Urychlovač potřebuje energii: shora nebo zespodu přiveď FE kabelem, nebo na něj dej kliku (&eWooden Crank&r).",
            "Sklízej jen plně vyrostlé shluky (&eCertus Quartz Cluster&r) – dají 4 krystaly. Nedorostlý krystal dá jen 1 prach.",
            "&aTip:&r Pučící blok (kromě bezvadného) se při růstu postupně kazí. Opravíš ho hozením do vody s nabitým certusem."]),
        Q("ae_circuits", "Plošné spoje", dep=["storage:ae_inscriber"], items=[("ae2:printed_silicon", 4), ("ae2:printed_logic_processor", 2), ("ae2:printed_calculation_processor", 2), ("ae2:printed_engineering_processor", 2)], xp=40, d=[
            "Procesor má tři vrstvy. Nejdřív v razítkovači vyraž plošné spoje: lis nahoru, materiál doprostřed.",
            "Logický lis + zlatý ingot, výpočetní lis + certusový krystal, inženýrský lis + diamant, křemíkový lis + křemík (&eSilicon&r).",
            "Křemík vyrobíš tavením certusového prachu. Prach dostaneš rozdrcením certusu v razítkovači nebo v drtiči Mekanismu.",
            "&aTip:&r Hotový procesor: vytištěný obvod nahoru, redstone doprostřed, vytištěný křemík dolů."]),
        Q("ae_cables", "Kabely", dep=["storage:ae_charger"], items=[("ae2:fluix_glass_cable", 16)], xp=20, d=[
            "Kabely (&eFluix ME Glass Cable&r) spojují zařízení AE2 do jedné sítě. Nejsou to trubky – předměty ani kapaliny jimi neposíláš.",
            "Vyrobíš je z křemenného vlákna (&eQuartz Fiber&r) a fluixových krystalů.",
            "&aTip:&r Barevné kabely se nespojí s kabely jiné barvy. Fluixový kabel se spojí se všemi."]),
        Q("ae_energy", "Energie pro síť", dep=["ae_cables"], items=[("ae2:energy_acceptor", 1)], xp=25, d=[
            "Síť AE2 potřebuje energii. Akceptor energie (&eEnergy Acceptor&r) převádí FE z jiných modů na energii AE (2 FE = 1 AE).",
            "Napoj ho na zdroj FE, třeba na generátor Mekanismu, a polož ho do sítě.",
            "&aTip:&r Bez cizího zdroje energie použij vibrační komoru (&eVibration Chamber&r). Spaluje palivo jako pec."]),
        Q("ae_resonance", "Energie bez paliva", dep=["ae_energy"], items=[("ae2:crystal_resonance_generator", 1)], xp=40, optional=True, d=[
            "Generátor krystalové rezonance (&eCrystal Resonance Generator&r) vyrábí energii pro síť bez paliva.",
            "V jedné síti ale funguje jen jeden.",
            "&aTip:&r Na malou síť to stačí. Velká síť s automatickou výrobou potřebuje víc – připoj akceptor energie."]),
        Q("ae_cells", "Bajty a typy", dep=["storage:ae_drive"], items=[("ae2:item_storage_cell_4k", 1)], xp=40, d=[
            "Paměťová buňka neuloží neomezeně věcí. Má dvě omezení: bajty (kolik kusů) a typy (kolik různých předmětů).",
            "Každá buňka pojme nejvýš 63 různých předmětů. 4k buňka (&e4k ME Item Storage Cell&r) pojme 4× víc kusů než 1k, ale typů stejně.",
            "&aTip:&r Buňku vylepšíš: v pracovním stole ji spoj s větší součástkou. Obsah zůstane a menší součástka se vrátí."]),
        Q("ae_workbench", "Rozdělení buněk", dep=["ae_cells"], items=[("ae2:cell_workbench", 1)], xp=25, optional=True, d=[
            "Ve stole na buňky (&eCell Workbench&r) nastavíš buňce filtr: bude přijímat jen vybrané věci.",
            "Do buňky tu vložíš i karty – třeba kartu přetečení (&eOverflow Destruction Card&r), která maže, co se už nevejde.",
            "&aTip:&r Filtr se hodí pro farmy: buňka jen na kámen nezaplní ostatní buňky."]),
        Q("ae_crafting_term", "Výrobní terminál", dep=["storage:ae_drive"], items=[("ae2:crafting_terminal", 1)], xp=30, d=[
            "Výrobní terminál (&eME Crafting Terminal&r) je terminál s pracovním stolem. Vyrábíš v něm přímo ze surovin v síti.",
            "Vyrobíš ho z terminálu, pracovního stolu a výpočetního procesoru.",
            "&aTip:&r Tlačítko + u receptu v JEI přenese recept rovnou do mřížky terminálu."]),
        Q("ae_channels", "Kanály", dep=["storage:ae_drive", "ae_cables"], items=[("ae2:fluix_smart_cable", 16), ("ae2:fluix_smart_dense_cable", 4)], xp=50, s="Pokročilý", **MS, d=[
            "Teď se síť začne zvětšovat a narazíš na kanály. Kanál je jako USB port: většina zařízení (terminál, disková jednotka, sběrnice) potřebuje jeden.",
            "Síť bez ovladače (&eME Controller&r) zvládne jen 8 takových zařízení. S ovladačem dá každá jeho strana 32 kanálů.",
            "Obyčejný kabel unese 8 kanálů, hustý (&eFluix ME Dense Smart Cable&r) 32. Na hustý kabel ale nejde přímo dát sběrnici ani terminál.",
            "{@pagebreak}",
            "Chytrý kabel (&eFluix ME Smart Cable&r) ukazuje světýlky, kolik kanálů jím vede. Používej ho, dokud kanálům nerozumíš.",
            "Dobrá síť vypadá jako strom: od ovladače husté kabely, z nich obyčejné a na každém obyčejném nejvýš 8 zařízení.",
            "&aTip:&r Barva kabelu s kanály nesouvisí. Barvy jen brání tomu, aby se dva kabely vedle sebe spojily."]),
        Q("ae_network_tool", "Síťový nástroj", dep=["ae_channels"], items=[("ae2:network_tool", 1)], xp=20, optional=True, d=[
            "Síťový nástroj (&eNetwork Tool&r) ukáže, kolik kanálů a energie síť používá a co v ní je.",
            "Má v sobě i malý inventář na karty vylepšení.",
            "&aTip:&r Stejné údaje uvidíš, když klikneš pravým tlačítkem na ovladač."]),
        Q("ae_io", "Import a export", dep=["storage:ae_drive"], items=[("ae2:import_bus", 1), ("ae2:export_bus", 1)], xp=40, d=[
            "Importní sběrnice (&eME Import Bus&r) bere věci z bloku, na který je položená, a ukládá je do sítě. Exportní (&eME Export Bus&r) posílá věci ze sítě do bloku.",
            "V exportní sběrnici nastav, které věci má posílat. Příklad: exportní sběrnice nahoře na peci posílá rudu, importní dole bere hotové ingoty.",
            "&aTip:&r Sběrnice jsou malé destičky na kabelu. Na jeden kabel jich jde dát víc, každou na jinou stranu."]),
        Q("ae_cards", "Karty vylepšení", dep=["ae_io"], items=[("ae2:speed_card", 1), ("ae2:capacity_card", 1)], xp=30, d=[
            "Karty se vkládají do sběrnic a dalších zařízení. Zrychlovací karta (&eAcceleration Card&r) zrychlí přesun, kapacitní karta (&eCapacity Card&r) přidá sloty filtru.",
            "Výrobní karta (&eCrafting Card&r) dovolí exportní sběrnici chybějící věc nechat vyrobit.",
            "&aTip:&r Které karty zařízení přijme, ukáže jeho okno a průvodce AE2 (klávesa G)."]),
        Q("ae_storage_bus", "Úložná sběrnice", dep=["ae_io"], items=[("ae2:storage_bus", 1)], xp=40, d=[
            "Úložná sběrnice (&eME Storage Bus&r) připojí do sítě obyčejnou truhlu, sud nebo šuplíky. Síť pak vidí jejich obsah a umí do nich ukládat.",
            "Skvěle funguje s šuplíky ze &bStorage Drawers&r: jejich obsah uvidíš v terminálu.",
            "&aTip:&r Velké neoptimalizované truhly s mnoha sloty síť zpomalují. Šuplíky jsou v pořádku."]),
        Q("ae_interface", "Rozhraní", dep=["ae_io"], items=[("ae2:interface", 1)], xp=40, d=[
            "Rozhraní (&eME Interface&r) je jako malá truhla napojená na síť. Nastavíš v něm, co má mít vždy na skladě, a samo si to ze sítě doplní.",
            "Ostatní stroje a trubky si z něj mohou brát. Věci, které do nenastaveného rozhraní vložíš, jdou do sítě.",
            "&aTip:&r Rozhraní je klíčem k pokročilým trikům s podsítěmi. Najdeš je v průvodci AE2."]),
        Q("ae_pattern_term", "Vzory receptů", dep=["ae_crafting_term"], items=[("ae2:pattern_encoding_terminal", 1), ("ae2:blank_pattern", 4)], xp=50, d=[
            "Automatická výroba začíná prázdným vzorem (&eBlank Pattern&r). Recept do něj zapíšeš v terminálu pro vzory (&eME Pattern Encoding Terminal&r).",
            "Výrobní vzor obsahuje recept z pracovního stolu. Zpracovací vzor (&eProcessing Pattern&r) říká, co poslat do stroje (třeba pece) a co se má vrátit.",
            "&aTip:&r Recept do terminálu přeneseš z JEI tlačítkem + u receptu."]),
        Q("ae_cpu", "Výrobní procesor", dep=["storage:ae_craft"], items=[("ae2:1k_crafting_storage", 1), ("ae2:crafting_accelerator", 1)], xp=60, s="Expert", **MS, d=[
            "Ruční výroba je minulost – teď síť vyrábí sama. Výrobní procesor (CPU) řídí jednu zakázku. Je to plný kvádr z výrobních bloků bez děr a musí v něm být aspoň jedno výrobní úložiště (&e1k Crafting Storage&r).",
            "Úložiště určuje, jak velkou zakázku CPU zvládne. Koprocesor (&eCrafting Co-Processing Unit&r) ji zrychlí. Volné místo vyplň výrobní jednotkou (&eCrafting Unit&r).",
            "&aTip:&r Jedno CPU = jedna zakázka. Chceš vyrábět dvě věci naráz? Postav dvě CPU."]),
        Q("ae_p2p", "P2P tunely", dep=["ae_channels"], items=[("ae2:me_p2p_tunnel", 2), ("ae2:memory_card", 1)], xp=50, d=[
            "P2P tunel (&eME P2P Tunnel&r) je jako portál mezi dvěma místy. Přenáší kanály, předměty, kapaliny, energii nebo redstone.",
            "Typ změníš kliknutím na tunel: kabelem = kanály, truhlou nebo násypkou = předměty, kbelíkem = kapaliny, redstonovou součástkou = redstone.",
            "Vstup a výstup propojíš paměťovou kartou (&eMemory Card&r): Shift + pravým tlačítkem na vstup, pak pravým na výstup.",
            "&aTip:&r ME P2P tunel přenese 32 kanálů i přes obyčejný kabel."]),
        Q("ae_wcraft", "Bezdrátová výroba", dep=["storage:ae_wireless"], items=[("ae2:wireless_crafting_terminal", 1), ("ae2:wireless_booster", 2)], xp=40, optional=True, d=[
            "Bezdrátový výrobní terminál (&eWireless Crafting Terminal&r) je výrobní terminál v kapse.",
            "Zesilovače (&eWireless Booster&r) vložené do přístupového bodu zvětší jeho dosah.",
            "&aTip:&r Přístupových bodů může být v síti víc – pokryješ tak celou základnu."]),
        Q("ae_quantum", "Kvantový můstek", dep=["ae_p2p"], items=[("ae2:quantum_ring", 8), ("ae2:quantum_link", 1)], xp=100, d=[
            "Kvantový můstek (&eQuantum Network Bridge&r) spojí dvě sítě na libovolnou vzdálenost, i mezi dimenzemi. Přenese 32 kanálů.",
            "Na každé straně postav 8 kvantových prstenců (&eME Quantum Ring&r) kolem jedné kvantové komory (&eME Quantum Link Chamber&r).",
            "Do obou komor vlož po jedné provázané singularitě (&eQuantum Entangled Singularity&r). Vzniknou v páru, když singularitu (&eSingularity&r) a endovou perlu zasáhne výbuch.",
            "&aTip:&r Singularitu vyrobí kondenzátor hmoty (&eMatter Condenser&r) z 256 000 předmětů. &cObě strany musí být načtené&r – použij chunk loader."]),
    ],
)

# =====================================================================================
# REFINED STORAGE
# =====================================================================================
RS = dict(
    key="refined_storage", group="tech", title="Refined Storage",
    subtitle="Jednodušší digitální úložiště", icon="refinedstorage:controller",
    quests=[
        Q("rs_intro", "Co je Refined Storage", tasks=[auto()], xp=10, s="Začátečník", icon="refinedstorage:grid", **MS, d=[
            "&bRefined Storage&r je digitální úložiště jako AE2, ale jednodušší: nemá kanály a všechno se prostě propojí kabelem.",
            "Ovladač (&eController&r) dodává síti energii (FE), disky v diskové jednotce ukládají věci a v mřížce (&eGrid&r) je vidíš a bereš.",
            "&aTip:&r Některé kroky jsou v kapitole &bÚložiště&r (mají v názvu „RS:“)."]),
        Q("rs_iron", "Křemenné železo", dep=["rs_intro"], items=[("refinedstorage:quartz_enriched_iron", 16)], xp=15, d=[
            "Základní materiál je křemenné železo (&eQuartz Enriched Iron&r): 3 železné ingoty + 1 netherový křemen = 4 kusy.",
            "Na kabely potřebuješ křemennou měď (&eQuartz Enriched Copper&r) – stejný recept, jen s mědí.",
            "&aTip:&r Netherový křemen najdeš v Netheru."]),
        Q("rs_silicon", "Křemík", dep=["rs_intro"], items=[("refinedstorage:silicon", 8)], xp=15, d=[
            "Křemík (&eSilicon&r) vyrobíš tavením netherového křemene v peci.",
            "Potřebuješ ho na procesory a paměťové části disků.",
            "&aTip:&r Vyrob si ho rovnou víc – spotřebuješ ho hodně."]),
        Q("rs_processors", "Procesory", dep=["rs_iron", "rs_silicon"], items=[("refinedstorage:basic_processor", 4), ("refinedstorage:improved_processor", 4), ("refinedstorage:advanced_processor", 4)], xp=40, d=[
            "Procesory se vyrábějí ve dvou krocích. 1) Surový procesor: pojivo (&eProcessor Binding&r) + kov + křemík + redstone. 2) Surový procesor upeč v peci.",
            "Základní (&eBasic Processor&r) je ze železa, vylepšený (&eImproved Processor&r) ze zlata a pokročilý (&eAdvanced Processor&r) z diamantu.",
            "&aTip:&r Pojivo vyrobíš z vlákna a slizu – z jednoho receptu je ho 8 kusů."]),
        Q("rs_casing", "Plášť a kabely", dep=["rs_iron"], items=[("refinedstorage:machine_casing", 1), ("refinedstorage:cable", 12)], xp=20, d=[
            "Plášť stroje (&eMachine Casing&r) je základ bloků Refined Storage: 8 křemenného železa a kámen.",
            "Kabel (&eCable&r) spojuje zařízení. Zařízení se propojí i tím, že stojí přímo vedle sebe.",
            "&aTip:&r Obarvené kabely a bloky se spojí jen se stejnou barvou nebo s neobarvenými (ve výchozí barvě)."]),
        Q("rs_cores", "Jádra", dep=["rs_processors"], items=[("refinedstorage:construction_core", 2), ("refinedstorage:destruction_core", 2)], xp=20, d=[
            "Stavební jádro (&eConstruction Core&r) = základní procesor + světlitový prach. Ničicí jádro (&eDestruction Core&r) = základní procesor + netherový křemen.",
            "Jádra jsou v mřížce, importéru, exportéru a dalších zařízeních.",
            "&aTip:&r Vyrob si jich rovnou několik."]),
        Q("rs_crafting_grid", "Výrobní mřížka", dep=["storage:rs_disk"], items=[("refinedstorage:crafting_grid", 1)], xp=30, d=[
            "Výrobní mřížka (&eCrafting Grid&r) je mřížka s pracovním stolem. Vyrábíš v ní přímo ze surovin v síti.",
            "Vyrobíš ji z mřížky, pokročilého procesoru a pracovního stolu.",
            "&aTip:&r Tlačítko + u receptu v JEI přenese recept rovnou do mřížky."]),
        Q("rs_disks", "Větší disky", dep=["storage:rs_disk"], items=[("refinedstorage:4k_storage_disk", 1)], xp=30, d=[
            "Větší disk (&e4k Storage Disk&r) pojme 4 000 předmětů. Jsou i 16k a 64k.",
            "Disk vylepšíš tak, že ho v pracovním stole spojíš s větší paměťovou částí (&e4k Storage Part&r). Obsah zůstane.",
            "&aTip:&r Prázdný disk rozebereš: drž ho v ruce a klikni pravým tlačítkem. Vrátí se ti paměťová část."]),
        Q("rs_import", "Import a export", dep=["storage:rs_disk"], items=[("refinedstorage:importer", 1), ("refinedstorage:exporter", 1)], xp=40, s="Pokročilý", **MS, d=[
            "Teď už síť nejen skladuje, ale i přesouvá věci sama. Importér (&eImporter&r) bere věci z bloku, na kterém je, a ukládá je do sítě. Exportér (&eExporter&r) posílá vybrané věci ze sítě do bloku.",
            "Příklad: exportér na peci posílá rudu, importér pod pecí bere ingoty.",
            "&aTip:&r Ve filtrech nastavíš, které věci mají projít."]),
        Q("rs_external", "Externí úložiště", dep=["storage:rs_disk"], items=[("refinedstorage:external_storage", 1)], xp=30, d=[
            "Externí úložiště (&eExternal Storage&r) připojí do sítě truhlu, sud nebo šuplíky. Jejich obsah uvidíš v mřížce.",
            "Hodí se, když už máš velký sklad a nechceš ho stěhovat.",
            "&aTip:&r Prioritou nastavíš, kam má síť ukládat nejdřív."]),
        Q("rs_upgrades", "Vylepšení", dep=["rs_import"], items=[("refinedstorage:upgrade", 1), ("refinedstorage:speed_upgrade", 1), ("refinedstorage:stack_upgrade", 1)], xp=30, d=[
            "Vylepšení se vkládají do importéru, exportéru a dalších zařízení. Základ (&eUpgrade&r) je z křemenného železa, skla a vylepšeného procesoru.",
            "Rychlost (&eSpeed Upgrade&r) zrychlí práci, stohování (&eStack Upgrade&r) přesune víc kusů naráz.",
            "&aTip:&r Regulátor (&eRegulator Upgrade&r) v exportéru udrží v cíli jen nastavené množství."]),
        Q("rs_constructor", "Stavění a ničení", dep=["rs_import"], items=[("refinedstorage:constructor", 1), ("refinedstorage:destructor", 1)], xp=30, optional=True, d=[
            "Konstruktor (&eConstructor&r) pokládá bloky ze sítě do světa. Destruktor (&eDestructor&r) bloky před sebou ničí a ukládá je do sítě.",
            "Ve filtrech nastavíš, které bloky.",
            "&aTip:&r Destruktor s vylepšením Štěstí (&eFortune I Upgrade&r a vyšší) dává víc surovin z rud."]),
        Q("rs_pattern_grid", "Mřížka vzorů", dep=["rs_crafting_grid"], items=[("refinedstorage:pattern_grid", 1)], xp=40, d=[
            "Mřížka vzorů (&ePattern Grid&r) zapisuje recepty do vzorů (&ePattern&r).",
            "Výrobní vzor = recept z pracovního stolu. Zpracovací vzor = co dát do stroje a co se má vrátit (třeba ruda → ingot v peci).",
            "&aTip:&r Recept přeneseš z JEI tlačítkem + u receptu."]),
        Q("rs_auto_upgrade", "Výroba na požádání", dep=["storage:rs_craft", "rs_upgrades"], items=[("refinedstorage:autocrafting_upgrade", 1)], xp=50, s="Expert", **MS, d=[
            "Síť teď umí vyrábět sama, když něco chybí. Vylepšení výroby (&eAutocrafting Upgrade&r) vlož do exportéru, rozhraní nebo konstruktoru.",
            "Když chybí věc, kterou má zařízení posílat, síť ji sama nechá vyrobit.",
            "&aTip:&r Exportér s tímto vylepšením a regulátorem udrží v truhle stálou zásobu."]),
        Q("rs_monitor", "Přehled výroby", dep=["storage:rs_craft"], items=[("refinedstorage:autocrafting_monitor", 1), ("refinedstorage:autocrafter_manager", 1)], xp=40, optional=True, d=[
            "Monitor výroby (&eAutocrafting Monitor&r) ukáže běžící zakázky a dovolí je zrušit.",
            "Správce výrobníků (&eAutocrafter Manager&r) ukáže všechny výrobníky a jejich vzory na jednom místě.",
            "&aTip:&r Hodí se, když máš výrobníků hodně."]),
        Q("rs_wireless", "Bezdrátový přístup", dep=["storage:rs_disk"], items=[("refinedstorage:wireless_transmitter", 1), ("refinedstorage:wireless_grid", 1)], xp=50, d=[
            "Bezdrátový vysílač (&eWireless Transmitter&r) zpřístupní síť na dálku. Bezdrátová mřížka (&eWireless Grid&r) je mřížka v kapse.",
            "Mřížku propojíš se sítí tak, že s ní klikneš Shift + pravým tlačítkem na zařízení sítě (třeba na ovladač). Mřížka potřebuje energii – nabij ji.",
            "&aTip:&r Dosah vysílače zvětší vylepšení dosahu (&eRange Upgrade&r)."]),
        Q("rs_network_tx", "Síť bez kabelů", dep=["rs_wireless"], items=[("refinedstorage:network_transmitter", 1), ("refinedstorage:network_receiver", 1), ("refinedstorage:network_card", 1)], xp=60, d=[
            "Síťový vysílač (&eNetwork Transmitter&r) a přijímač (&eNetwork Receiver&r) spojí části sítě bez kabelů.",
            "Síťovou kartu (&eNetwork Card&r) propoj s přijímačem (Shift + pravé tlačítko na přijímač) a vlož ji do vysílače.",
            "&aTip:&r Na vysílač i přijímač potřebuješ netheritové ingoty."]),
        Q("rs_security", "Zabezpečení sítě", dep=["storage:rs_disk"], items=[("refinedstorage:security_manager", 1), ("refinedstorage:security_card", 1)], xp=40, optional=True, d=[
            "Na serveru se hodí ochrana sítě. Správce zabezpečení (&eSecurity Manager&r) zakáže cizím hráčům všechno, co nepovolíš.",
            "Bezpečnostní karta (&eSecurity Card&r) nastaví práva jednoho hráče: klikni s ní pravým tlačítkem a vyber, co smí. Kartu pak vlož do správce zabezpečení.",
            "&aTip:&r Záložní karta (&eFallback Security Card&r) platí pro všechny hráče bez vlastní karty."]),
    ],
)

# Pořadí kapitol této oblasti v knize questů
CHAPTERS = [MEKANISM, MEK_POWER, STORAGE, AE2, RS]

# Předměty bez receptu v indexu (obtainable.txt nezná recepty typu mekanism:reaction) – ověřeno v datech Mekanismu
NO_RECIPE = {
    "mekanism:substrate": "Tlaková reakční komora: bio palivo + voda + vodík (data/mekanism/recipe/reaction/substrate/water_hydrogen.json)",
    "mekanism:pellet_polonium": "Tlaková reakční komora: polonium + voda + fluoritový prach (processing/lategame/polonium_pellet/from_reaction.json)",
    "mekanism:pellet_plutonium": "Tlaková reakční komora: plutonium + voda + fluoritový prach (processing/lategame/plutonium_pellet/from_reaction.json)",
}

# České překlady vlastních jmen (regex bez ohledu na velikost písmen -> anglický název). Stavbu ae2:meteorite
# („meteorit“ -> Meteorite) sem dát nejde: regex by chytal i anglické „Meteorite“ a běžné slovo meteorit.
PROPER_NAMES_CZ = {}
