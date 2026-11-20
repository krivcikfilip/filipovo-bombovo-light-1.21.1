from engine import *

WELCOME = dict(
    key="welcome", group="start", title="Vítej v Bombovu 2",
    subtitle="Začni tady: kniha questů, ovládání a první rady", icon="ftbquests:book",
    quests=[
        Q("hello", "Vítej!", icon="ftbquests:book", tasks=[auto()], xp=20, s="Začátečník",
          shape="hexagon", size=1.5, d=[
            "Tahle kniha je &eprůvodce&r modpackem. Každá kapitola tě krok za krokem provede jedním modem nebo tématem.",
            "",
            "Úkoly se plní samy. Stačí mít věc v inventáři – nic se ti nevezme.",
            "Když quest splníš, klikni na něj a vyzvedni si odměnu (většinou zkušenosti).",
            "{@pagebreak}",
            "&aTip:&r Klikni v questu na obrázek předmětu. Otevře se jeho recept v &bJEI&r.",
            "Čáry mezi questy ukazují pořadí. Začni vlevo a pokračuj po čarách doprava.",
            "Kapitoly najdeš v levém sloupci. Po této kapitole pokračuj kapitolou &ePrvní dny&r.",
        ]),
        Q("jei", "Recepty v JEI", dep=["hello"], items=[("minecraft:chest", 1)], xp=15, d=[
            "&bJEI&r je seznam všech předmětů vpravo vedle inventáře. Ukáže ti, jak se co vyrábí.",
            "Najeď myší na předmět a zmáčkni &eR&r – uvidíš recept. Klávesa &eU&r ukáže, k čemu se předmět používá.",
            "Do hledání skočíš klávesami &eCtrl + F&r. Klávesa &eA&r uloží předmět do záložek.",
            "&aTip:&r Napiš do hledání @ a jméno modu (třeba @create) a uvidíš jen věci z toho modu.",
            "Zkus to hned: najdi recept na truhlu a vyrob si ji.",
        ]),
        Q("jade", "Co je to za blok?", dep=["hello"], tasks=[adv("minecraft:story/mine_stone")],
          icon="minecraft:stone_pickaxe", xp=15, d=[
            "&bJade&r ukazuje nahoře na obrazovce, na co se díváš: jméno bloku nebo zvířete a z jakého je modu.",
            "Ukáže i to, jaký nástroj potřebuješ. Když podržíš Shift, uvidíš víc podrobností.",
            "Nastavení Jade otevřeš klávesou 0 na numerické klávesnici.",
            "Úkol: vyrob si dřevěný krumpáč a vykopej kámen.",
        ]),
        Q("map", "Mapa a body", dep=["hello", "vanilla:iron"], items=[("minecraft:compass", 1)], xp=20, d=[
            "V rohu obrazovky máš minimapu (mod &bXaero's Minimap&r). Klávesa &eM&r otevře velkou mapu světa.",
            "Klávesa &eN&r vytvoří bod (waypoint), třeba u tvého domu. &eU&r otevře seznam bodů a &eY&r nastavení minimapy.",
            "Když umřeš, mapa ti ukáže místo smrti.",
            "Kompas ukazuje ke spawnu – k místu, kde ses poprvé objevil. Díky &bQuarku&r funguje i v Netheru: ukazuje k portálu, kterým jsi přišel.",
            "Úkol: vyrob si kompas ze 4 železných ingotů a redstonu.",
        ]),
        Q("death", "Když umřeš", dep=["hello"], tasks=[auto()], icon="minecraft:skeleton_skull", xp=10, d=[
            "Po smrti tvoje věci nezmizí. Zůstanou na místě smrti v těle tvé postavy (mod &bCorpse&r).",
            "Dojdi tam, klikni na tělo a vezmi si věci zpátky. Tělo samo nezmizí, dokud v něm něco je.",
            "Klávesa &eJ&r otevře historii smrtí – uvidíš, kde a kdy jsi zemřel.",
            "{@pagebreak}",
            "Užitečné příkazy (&bFTB Essentials&r): &e/back&r tě vrátí na poslední místo (i místo smrti), &e/sethome&r uloží domov a &e/home&r tě tam přenese. &e/spawn&r tě pošle na spawn.",
        ]),
        Q("friends", "Hrajeme spolu", dep=["hello"], tasks=[auto()], icon="minecraft:bell", xp=10, d=[
            "Truhly v dungeonech a stavbách jsou z modu &bLootr&r. Každý hráč v nich najde vlastní kořist, takže nikdo nikomu nic nevybere.",
            "&bCarry On&r: s prázdnýma rukama podrž Shift a klikni pravým tlačítkem na truhlu nebo zvíře. Zvedneš je i s obsahem.",
            "{@pagebreak}",
            "&bPing Wheel&r: boční tlačítko myši (tlačítko 5) ukáže ostatním hráčům značku tam, kam se díváš. Klávesu změníš v nastavení ovládání.",
            "Příkazem &e/tpa jméno&r požádáš kamaráda o teleport k němu. Kamarád musí žádost přijmout.",
        ]),
        Q("next", "Kam dál?", dep=["jei", "jade"], tasks=[adv("minecraft:story/smelt_iron")],
          icon="minecraft:iron_ingot", xp=25, s="Rozcestník", d=[
            "Úkol: přetav v peci železnou rudu na ingot. Pak jsi připravený na velké mody.",
            "Nevíš, jak na to? Projdi kapitolu &ePrvní dny&r.",
            "{@pagebreak}",
            "&bCreate&r (skupina Create): stroje na točivou sílu, továrny, vlaky. Skvělý první velký mod.",
            "&bTechnika a úložiště&r: Mekanism (elektřina a zpracování rud), úložné systémy a truhly.",
            "&bJídlo a farmaření&r: stovky nových jídel, farmy a vaření.",
            "{@pagebreak}",
            "&bKolonie a stavění&r: MineColonies (vlastní vesnice s obyvateli) a dekorace.",
            "&bPrůzkum a dimenze&r: Nether, End, Aether, Twilight Forest, nové stavby a příšery.",
            "Kapitoly v této skupině (&bZačínáme&r) ti pomůžou s batohy, užitečnými mody, Quarkem a výbavou.",
        ]),
        Q("warpstone", "Waystones", dep=["next", "create:crafter"], items=[("waystones:warp_stone", 1)],
          xp=40, s="Pokročilý", shape="hexagon", size=1.5, d=[
            "&bWaystones&r jsou kameny na rychlé cestování. Najdeš je v některých vesnicích a občas i volně v krajině.",
            "Klikni na waystone pravým tlačítkem. Tím ho aktivuješ. Pak se můžeš teleportovat mezi všemi waystony, které jsi aktivoval.",
            "Teleport stojí zkušenosti. Čím delší cesta, tím víc. Cesta do jiné dimenze stojí nejvíc.",
            "{@pagebreak}",
            "Varpový kámen (&eWarp Stone&r) otevře menu waystonů odkudkoliv. Používáním se pomalu opotřebovává.",
            "Vyrobíš ho z ender perel, ametystových úlomků a smaragdů.",
            "&cPozor:&r v tomhle packu se waystonové věci vyrábějí na mechanických craftovačích (&eMechanical Crafter&r) z modu &bCreate&r. JEI ti ukáže tvar receptu.",
        ]),
        Q("waystone", "Vlastní waystone", dep=["warpstone"], items=[("waystones:waystone", 1)], xp=40, d=[
            "Vlastní waystone (&eWaystone&r) si postav u domu nebo u farmy. Pak se tam kdykoliv vrátíš.",
            "Vyrábí se na mechanických craftovačích z kamenných cihel, andezitového pláště (&eAndesite Casing&r), ender perel a varpového kamene. Recept dá rovnou 2 kusy.",
            "&aTip:&r Po položení mu dej jméno, ať se v seznamu vyznáš.",
        ]),
        Q("return_scroll", "Svitek návratu", dep=["warpstone"], items=[("waystones:return_scroll", 1)], xp=25,
          optional=True, d=[
            "Svitek návratu (&eReturn Scroll&r) tě přenese k nejbližšímu waystonu, který jsi aktivoval. Po použití zmizí.",
            "Teleport svitkem je zdarma – nestojí žádné zkušenosti.",
            "Vyrábí se na mechanických craftovačích ze zlatých nuggetů, papíru a fialového barviva. Jeden recept dá 3 svitky.",
        ]),
        Q("warp_plate", "Teleportační desky", dep=["waystone"], items=[("waystones:warp_plate", 2)],
          xp=60, s="Expert", shape="hexagon", size=1.5, d=[
            "Varpová deska (&eWarp Plate&r) teleportuje na druhou desku. Stačí si na ni stoupnout a chvíli počkat. Je to zdarma.",
            "Jak je propojit: polož obě desky. Do první vlož spící střep (&eDormant Shard&r). Z něj se stane naladěný střep (&eAttuned Shard&r).",
            "Naladěný střep vezmi a vlož do druhé desky. Teď jsou desky propojené.",
            "{@pagebreak}",
            "Desky i střepy se vyrábějí na mechanických craftovačích. Potřebuješ varpový prach (&eWarp Dust&r): ender perla + ametystový úlomek dají 4 kusy.",
        ]),
        Q("backpack", "Batoh", dep=["hello"], items=[("sophisticatedbackpacks:backpack", 1)], xp=25, d=[
            "Batoh (&eBackpack&r) z modu &bSophisticated Backpacks&r je přenosná truhla. Vyrobíš ho z kůže, provázku a truhly.",
            "Otevřeš ho klávesou &eB&r, i když je jen v inventáři. Můžeš ho nosit i ve slotu na záda.",
            "Když podržíš Shift a klikneš s ním pravým tlačítkem na zem, položíš ho jako blok.",
            "Vylepšené batohy a upgrady najdeš v kapitole &eBatohy a truhly&r.",
        ]),
        Q("pickup", "Batoh sbírá za tebe", dep=["backpack", "vanilla:iron"], items=[("sophisticatedbackpacks:pickup_upgrade", 1)], xp=25, d=[
            "Upgrade na sbírání (&ePickup Upgrade&r) pošle sebrané věci rovnou do batohu.",
            "Vlož ho do slotu pro upgrady vlevo v okně batohu. Ve filtru nastavíš, které věci má sbírat.",
            "Vyrábí se ze základu upgradu (&eUpgrade Base&r), lepivého pístu, provázku a redstonu.",
        ]),
        Q("feeding", "Batoh tě nakrmí", dep=["pickup"], items=[("sophisticatedbackpacks:feeding_upgrade", 1)], xp=30, d=[
            "Upgrade na krmení (&eFeeding Upgrade&r) ti dá najíst z jídla v batohu, když dostaneš hlad.",
            "Recept je dražší: zlaté jablko, zlatá mrkev, třpytivý meloun a ender perla.",
            "&aTip:&r Dej do batohu hodně různých jídel. Pestrá strava ti přidá srdíčka (viz quest &eKniha jídel&r).",
        ]),
        Q("food", "Kniha jídel", dep=["hello"], items=[("solonion:food_book", 1)], xp=25, d=[
            "Mod &bSpice of Life Onion&r sleduje, jak pestře jíš. Hra si pamatuje tvých posledních 32 jídel.",
            "Čím víc různých jídel jíš, tím víc bonusů dostaneš – třeba srdíčka navíc nebo sílu. Když jíš pořád to samé, bonusy ztratíš.",
            "Kniha jídel (&eFood Book&r) ukáže tvoje bonusy a co jsi jedl. Vyrobíš ji z knihy a brambory.",
            "Spoustu nových jídel najdeš ve skupině &bJídlo a farmaření&r.",
        ]),
        Q("lunchbox", "Svačinová krabice", dep=["food", "vanilla:iron"], items=[("solonion:lunchbox", 1)], xp=30, d=[
            "Do svačinové krabice (&eLunchbox&r) dáš různá jídla. Když z ní jíš, sama vybere jídlo, které ti pomůže nejvíc – to, které jsi dlouho nejedl.",
            "Nejdřív si vyrob svačinový pytlík (&eLunchbag&r) z papíru. Ten pak v pracovním stole spoj se železným blokem.",
        ]),
        Q("chunks", "Ať to běží, i když tu nejsi", dep=["friends", "vanilla:obsidian"], items=[("chunkloaders:single_chunk_loader", 1)], xp=40, d=[
            "Farmy a stroje pracují jen tehdy, když je nějaký hráč poblíž. Chunk loader udrží svou oblast (chunk) zapnutou, i když jsi daleko.",
            "Nejdřív vyrob základní chunk loader (&eBasic Chunk Loader&r) ze železa, obsidiánu a ender perly. Rozložíš ho na 9 malých (&eSingle Chunk Loader&r).",
            "Klikni na chunk loader pravým tlačítkem a na mapě vyber, které chunky má držet.",
            "{@pagebreak}",
            "&cPozor:&r každý zapnutý chunk zatěžuje server. Zapínej jen to, co opravdu potřebuješ.",
            "Když nebudeš týden online, tvoje chunk loadery se vypnou.",
            "Větší chunk loadery najdeš v kapitole &eUžitečné mody&r.",
        ]),
    ],
)

VANILLA = dict(
    key="vanilla", group="start", title="První dny",
    subtitle="Přežij první noc a dojdi až k diamantům a Netheru", icon="minecraft:iron_pickaxe",
    quests=[
        Q("start", "První dny", tasks=[auto()], icon="minecraft:oak_sapling", xp=10, s="Začátečník",
          shape="hexagon", size=1.5, d=[
            "Tahle kapitola je pro úplné nováčky. Naučíš se přežít první noc a pak se dostaneš až k diamantům a do Netheru.",
            "Plán na první den: nasbírej dřevo, vyrob nástroje, najdi jídlo a do setmění si postav úkryt nebo postel.",
            "Když nevíš, jak se něco vyrábí, najeď na předmět v questu a zmáčkni &eR&r (recept v JEI).",
        ]),
        Q("wood", "Dřevo a klacky", dep=["start"], items=[("minecraft:stick", 8)], xp=10, d=[
            "Drž levé tlačítko na kmeni stromu. Dřevo vykopeš i rukou.",
            "Z kmene vyrobíš prkna a ze dvou prken 4 klacky.",
            "&aTip:&r Mod &bFallingTree&r: když kácíš sekerou, spadne celý strom najednou. Když přitom držíš Shift, vykácíš jen jeden blok.",
        ]),
        Q("table", "Pracovní stůl", dep=["wood"], items=[("minecraft:crafting_table", 1)], xp=10, d=[
            "Pracovní stůl vyrobíš ze 4 prken. Polož ho a klikni na něj – dostaneš větší mřížku 3 × 3 na složitější recepty.",
            "Když jeden recept dává víc různých výsledků, mod &bPolymorph&r ukáže tlačítko, kterým si vybereš ten správný.",
        ]),
        Q("woodpick", "Dřevěný krumpáč", dep=["table"], items=[("minecraft:wooden_pickaxe", 1)], xp=10, d=[
            "Krumpáčem kopeš kámen a rudy. Bez krumpáče z kamene nic nedostaneš.",
            "Vyrobíš ho ze 3 prken a 2 klacků. Dřevěný krumpáč se brzy rozbije, tak ho hned vyměň za kamenný.",
        ]),
        Q("stone", "Doba kamenná", dep=["woodpick"], items=[("minecraft:stone_pickaxe", 1), ("minecraft:stone_sword", 1)],
          xp=15, d=[
            "Kamenné nástroje vydrží déle a kopou rychleji. Kamenný krumpáč už vykope i železnou rudu.",
            "Potřebuješ dlažební kámen (ten padá z kamene) a klacky.",
            "Meč se hodí na první noc – příšery v noci vylézají ze tmy.",
        ]),
        Q("axe", "Sekera", dep=["stone"], items=[("minecraft:stone_axe", 1)], xp=10, d=[
            "Sekerou kácíš stromy mnohem rychleji.",
            "Díky modu &bFallingTree&r stačí useknout spodní kmen a spadne celý strom. Každý kmen ale sekeru trochu opotřebuje.",
        ]),
        Q("torch", "Světlo", dep=["woodpick"], items=[("minecraft:torch", 16)], xp=10, d=[
            "Příšery se objevují jen ve tmě. Pochodně kolem domu je udrží dál.",
            "Pochodeň vyrobíš z uhlí a klacku. Uhlí najdeš jako černé tečky v kameni.",
            "&aTip:&r Když nemáš uhlí, upeč v peci dřevo. Vznikne dřevěné uhlí, které funguje stejně.",
        ]),
        Q("furnace", "Pec", dep=["stone"], items=[("minecraft:furnace", 1)], xp=10, d=[
            "V peci roztavíš rudy na ingoty a upečeš maso. Vyrobíš ji z 8 kusů dlažebního kamene.",
            "Nahoru dej to, co chceš upéct. Dolů palivo – uhlí, dřevo nebo prkna.",
        ]),
        Q("eat", "Nehladověj", dep=["start"], tasks=[adv("minecraft:husbandry/root")], icon="minecraft:cooked_beef", xp=10, d=[
            "Když máš prázdnou lištu jídla, přestaneš se léčit a začneš ztrácet život.",
            "Úkol: sněz cokoliv. Syrové maso ze zvířat upeč v peci – syté je mnohem víc.",
            "Snaž se jíst různá jídla. Pestrá strava ti dá bonusy (viz quest &eKniha jídel&r v kapitole Vítej).",
        ]),
        Q("bed", "Postel", dep=["wood"], tasks=[adv("minecraft:adventure/sleep_in_bed")], icon="minecraft:white_bed", xp=15, d=[
            "Postel vyrobíš ze 3 bloků vlny a 3 prken. Vlnu získáš z ovcí.",
            "Když se v posteli vyspíš, oživíš se po smrti u ní. Spát jde jen v noci nebo za bouřky.",
            "Na serveru se noc přeskočí, jen když spí dost hráčů najednou.",
            "Úkol: vyspi se v posteli.",
        ]),
        Q("mob", "Lovec příšer", dep=["stone"], tasks=[adv("minecraft:adventure/kill_a_mob")], icon="minecraft:stone_sword", xp=15, d=[
            "Úkol: poraz jakoukoliv nepřátelskou příšeru.",
            "&cPozor na creepery:&r tiše se připlíží a vybuchnou. Když syčí, rychle uteč.",
            "Kostlivci střílejí šípy – schovej se za roh a nech je přijít k sobě.",
        ]),
        Q("farm", "Políčko", dep=["table"], tasks=[adv("minecraft:husbandry/plant_seed")], icon="minecraft:wheat_seeds", xp=15, d=[
            "Semínka pšenice padají z trávy. Motykou udělej z hlíny pole a semínka zasaď.",
            "Pole potřebuje vodu blízko sebe, jinak roste pomalu.",
            "Zralou úrodu sklidíš pravým kliknutím – rostlina se sama znovu zasadí (mody &bRightClickHarvest&r a &bQuark&r).",
        ]),
        Q("breed", "Chov zvířat", dep=["farm"], tasks=[adv("minecraft:husbandry/breed_an_animal")], icon="minecraft:wheat", xp=15, d=[
            "Dvě zvířata stejného druhu nakrm jejich oblíbeným jídlem. Pak se jim narodí mládě.",
            "Krávy a ovce chtějí pšenici, prasata mrkev, slepice semínka.",
            "Vlastní chov znamená stálý přísun masa, kůže a vlny. Kůži budeš potřebovat na batoh.",
        ]),
        Q("iron", "Železo", dep=["furnace"], items=[("minecraft:iron_ingot", 10)], xp=20, s="Pokročilý",
          shape="hexagon", size=1.5, d=[
            "Železo je nejdůležitější kov. Železnou rudu (béžové tečky v kameni) najdeš v jeskyních a v horách.",
            "Rudu vykopej aspoň kamenným krumpáčem. Dostaneš surové železo – to v peci přetav na ingoty.",
            "&aTip:&r Později ti mody &bCreate&r a &bMekanism&r z jedné rudy udělají víc ingotů.",
        ]),
        Q("ironpick", "Železný krumpáč", dep=["iron"], items=[("minecraft:iron_pickaxe", 1)], xp=20, d=[
            "Železný krumpáč vykope i diamanty, zlato a redstone.",
            "Opotřebovaný nástroj nevyhazuj. Na kovadlině ho opravíš materiálem (tady železem) nebo spojíš s druhým stejným nástrojem.",
        ]),
        Q("armor", "Brnění", dep=["iron"], tasks=[adv("minecraft:story/obtain_armor")], icon="minecraft:iron_chestplate", xp=20, d=[
            "Brnění snižuje zranění. Úkol: vyrob si kus železného brnění. Pak si ho obleč.",
            "Celá sada (helma, kyrys, kalhoty a boty) stojí 24 železných ingotů.",
            "Lepší výbavu najdeš v kapitole &eVýbava a boj&r.",
        ]),
        Q("shield", "Štít", dep=["iron"], items=[("minecraft:shield", 1)], xp=15, d=[
            "Štít drž v druhé ruce (klávesa &eF&r ho přesune). Pravým tlačítkem kryješ útoky a šípy.",
            "Vyrobíš ho z 6 prken a 1 železného ingotu.",
        ]),
        Q("bucket", "Kbelík vody", dep=["iron"], items=[("minecraft:water_bucket", 1)], xp=15, d=[
            "Kbelík vyrobíš ze 3 železných ingotů. Naber do něj vodu.",
            "Voda uhasí oheň a zastaví lávu. Když vodu vyleješ pod sebe při pádu, nic se ti nestane.",
            "Láva + voda = obsidián. Ten budeš brzy potřebovat.",
        ]),
        Q("trade", "Obchod s vesničany", dep=["bed"], tasks=[adv("minecraft:adventure/trade")], icon="minecraft:emerald", xp=20, d=[
            "Ve vesnicích žijí vesničané. Za smaragdy prodávají nástroje, knihy s očarováním i jídlo.",
            "Úkol: udělej jeden obchod. Klikni na vesničana pravým tlačítkem.",
            "&aTip:&r Ve vesnicích často stojí waystone. Aktivuj ho, ať se sem snadno vrátíš.",
        ]),
        Q("diamond", "Diamanty!", dep=["ironpick"], tasks=[adv("minecraft:story/mine_diamond")], icon="minecraft:diamond",
          xp=40, s="Expert", shape="hexagon", size=1.5, d=[
            "Diamanty jsou hluboko pod zemí, v tmavém kameni (deepslate). Nejvíc jich je kolem výšky Y −59.",
            "Výšku ukáže výškoměr (&eAltimeter&r) ze &bSupplementaries&r nebo obrazovka F3.",
            "&cPozor:&r v hloubce je hodně lávy. Měj u sebe kbelík vody.",
        ]),
        Q("diamond_pick", "Diamantový krumpáč", dep=["diamond"], items=[("minecraft:diamond_pickaxe", 1)], xp=40, d=[
            "Diamantový krumpáč je rychlý a vydrží dlouho. Vykope i obsidián, na který železný nestačí.",
            "Vyrobíš ho ze 3 diamantů a 2 klacků.",
        ]),
        Q("obsidian", "Obsidián", dep=["diamond_pick", "bucket"], tasks=[adv("minecraft:story/form_obsidian")],
          icon="minecraft:obsidian", xp=30, d=[
            "Obsidián vznikne, když voda zateče na stojící lávu.",
            "Vykopeš ho diamantovým (nebo ještě lepším) krumpáčem. Trvá to dlouho.",
            "Úkol: získej obsidián do inventáře. Potřebuješ ho na portál do Netheru a na očarovací stůl.",
        ]),
        Q("enchant", "Očarovací stůl", dep=["obsidian"], items=[("minecraft:enchanting_table", 1)], xp=40, d=[
            "Očarovací stůl vyrobíš z knihy, 2 diamantů a 4 obsidiánů.",
            "V tomhle packu funguje očarování jinak (Quark &eMatrix Enchanting&r). Vlož předmět a lapis lazuli. Za lapis a zkušenosti vygeneruješ dílky očarování.",
            "Dílky přetáhni do mřížky. Dva stejné dílky spojíš do silnějšího.",
            "{@pagebreak}",
            "Knihovny kolem stolu (nejvíc 15) ti dají víc dílků a lepší očarování.",
            "Barevné svíčky na knihovnách mění, jaká očarování se objevují. Každá barva patří k jinému očarování.",
        ]),
        Q("bookshelf", "Knihovny", dep=["enchant"], items=[("minecraft:bookshelf", 8)], xp=25, optional=True, d=[
            "Knihovna se vyrábí ze 6 prken a 3 knih. Kniha je z papíru a kůže, papír z cukrové třtiny.",
            "Postav knihovny kolem očarovacího stolu s mezerou jednoho bloku. Mezi stolem a knihovnou nesmí nic stát.",
        ]),
        Q("anvil", "Kovadlina", dep=["iron"], items=[("minecraft:anvil", 1)], xp=25, d=[
            "Na kovadlině opravíš nástroje, spojíš očarované knihy s výbavou a přejmenuješ předměty.",
            "Vyrobíš ji ze 3 železných bloků a 4 železných ingotů. Každé použití stojí zkušenosti.",
        ]),
        Q("flint", "Křesadlo", dep=["iron"], items=[("minecraft:flint_and_steel", 1)], xp=15, d=[
            "Křesadlo zapálí oheň – a hlavně portál do Netheru.",
            "Vyrobíš ho ze železného ingotu a pazourku. Pazourek občas padá ze štěrku.",
        ]),
        Q("nether", "Portál do Netheru", dep=["obsidian", "flint"], tasks=[adv("minecraft:story/enter_the_nether")],
          icon="minecraft:flint_and_steel", xp=50, d=[
            "Postav rám z obsidiánu: 4 bloky široký a 5 vysoký (rohy můžeš vynechat, stačí 10 obsidiánů). Vnitřek zapal křesadlem.",
            "&cPozor:&r Nether je nebezpečný. Vezmi si brnění, jídlo a bloky na stavění. Postel tam vybuchne!",
            "Co v Netheru dělat, najdeš ve skupině &bPrůzkum a dimenze&r.",
            "{@pagebreak}",
            "&aZajímavost:&r Mod &bMutated Items&r – když do portálu hodíš třeba pec, redstone, křemen, nůžky nebo ohnivou tyč, mají 10% šanci, že se na druhé straně promění v nového tvora.",
        ]),
    ],
)

BACKPACKS = dict(
    key="backpacks", group="start", title="Batohy a truhly",
    subtitle="Víc místa: lepší batohy, upgrady a větší truhly", icon="sophisticatedbackpacks:iron_backpack",
    quests=[
        Q("start", "Víc místa!", dep=["welcome:backpack"], tasks=[auto()], icon="sophisticatedbackpacks:backpack",
          xp=10, s="Začátečník", shape="hexagon", size=1.5, d=[
            "V téhle kapitole zvětšíš batoh, naučíš ho sbírat, třídit a tavit věci a postavíš si větší truhly.",
            "Batoh se vylepšuje v pracovním stole. Věci a upgrady v něm při vylepšení zůstanou.",
            "Upgrady vkládáš do slotů vlevo v okně batohu. Lepší batoh má víc slotů na upgrady.",
            "{@pagebreak}",
            "&aTip:&r Batoh můžeš položit i na pohyblivou stavbu z modu &bCreate&r (třeba na vlak). Funguje tam dál jako úložiště.",
        ]),
        # --- batohy (páteř)
        Q("copper", "Měděný batoh", dep=["start"], items=[("sophisticatedbackpacks:copper_backpack", 1)], xp=15, d=[
            "Měděný batoh (&eCopper Backpack&r) má víc místa než obyčejný.",
            "Dej obyčejný batoh doprostřed pracovního stolu a kolem něj 8 měděných ingotů.",
        ]),
        Q("iron", "Železný batoh", dep=["copper"], items=[("sophisticatedbackpacks:iron_backpack", 1)], xp=20, d=[
            "Železný batoh (&eIron Backpack&r) je zase o kus větší.",
            "Vyrobíš ho z měděného batohu a 4 železných ingotů (nebo z obyčejného batohu a 8 ingotů).",
        ]),
        Q("gold", "Zlatý batoh", dep=["iron"], items=[("sophisticatedbackpacks:gold_backpack", 1)], xp=30, s="Pokročilý",
          shape="hexagon", size=1.5, d=[
            "Zlatý batoh (&eGold Backpack&r) má hodně místa a víc slotů na upgrady.",
            "Železný batoh obklop 8 zlatými ingoty.",
            "Teď se vyplatí pokročilé upgrady: pec v batohu a nádrž.",
        ]),
        Q("diamond", "Diamantový batoh", dep=["gold"], items=[("sophisticatedbackpacks:diamond_backpack", 1)], xp=40, d=[
            "Diamantový batoh (&eDiamond Backpack&r) – zlatý batoh obklop 8 diamanty.",
        ]),
        Q("netherite", "Netheritový batoh", dep=["diamond", "gear:netherite"], items=[("sophisticatedbackpacks:netherite_backpack", 1)],
          xp=80, s="Expert", shape="hexagon", size=1.5, d=[
            "Netheritový batoh (&eNetherite Backpack&r) je největší batoh v packu.",
            "Vylepšíš ho na kovářském stole: šablona netheritového vylepšení + diamantový batoh + netheritový ingot.",
        ]),
        # --- základní upgrady
        Q("base", "Základ upgradu", dep=["start", "vanilla:iron"], items=[("sophisticatedbackpacks:upgrade_base", 2)], xp=15, d=[
            "Základ upgradu (&eUpgrade Base&r) potřebuje skoro každý upgrade batohu.",
            "Vyrobíš ho z provázku, železných ingotů a kůže.",
        ]),
        Q("magnet", "Magnet", dep=["base", "welcome:pickup"], items=[("sophisticatedbackpacks:magnet_upgrade", 1)], xp=25, d=[
            "Magnet (&eMagnet Upgrade&r) přitahuje věci ze země do batohu, i když jsou kousek od tebe.",
            "Vylepšíš na něj upgrade na sbírání: přidej ender perly, železo, redstone a lapis lazuli.",
        ]),
        Q("crafting", "Stůl v batohu", dep=["base"], items=[("sophisticatedbackpacks:crafting_upgrade", 1)], xp=15, d=[
            "Upgrade s pracovním stolem (&eCrafting Upgrade&r) přidá do batohu záložku s mřížkou 3 × 3.",
            "Vyrábíš pak kdekoliv, přímo z věcí v batohu.",
        ]),
        Q("refill", "Doplňování", dep=["base"], items=[("sophisticatedbackpacks:refill_upgrade", 1)], xp=20, d=[
            "Upgrade na doplňování (&eRefill Upgrade&r) ti doplňuje vybrané věci v inventáři z batohu.",
            "Nastav do filtru třeba pochodně nebo bloky na stavění. Už ti nedojdou.",
        ]),
        Q("deposit", "Vysypání do truhly", dep=["base"], items=[("sophisticatedbackpacks:deposit_upgrade", 1)], xp=20, d=[
            "Upgrade na ukládání (&eDeposit Upgrade&r) vysype věci z batohu do truhly.",
            "Podrž Shift a klikni batohem pravým tlačítkem na truhlu. Ve filtru nastavíš, co se má vysypat.",
            "Opačně funguje &eRestock Upgrade&r – ten si věci z truhly vezme.",
        ]),
        Q("void", "Koš na smetí", dep=["base"], items=[("sophisticatedbackpacks:void_upgrade", 1)], xp=20, d=[
            "Upgrade koše (&eVoid Upgrade&r) maže věci, které nechceš – třeba hlínu nebo dlažební kámen.",
            "&cPozor:&r smaže všechno, co dáš do filtru. Nastav ho pečlivě.",
        ]),
        Q("tool_swapper", "Správný nástroj", dep=["base"], items=[("sophisticatedbackpacks:tool_swapper_upgrade", 1)], xp=25, d=[
            "Výměník nástrojů (&eTool Swapper Upgrade&r) ti při kopání sám vezme z batohu správný nástroj.",
            "Kopeš kámen? Vezme krumpáč. Kácíš strom? Vezme sekeru.",
        ]),
        Q("compacting", "Kompresor", dep=["base"], items=[("sophisticatedbackpacks:compacting_upgrade", 1)], xp=25, d=[
            "Kompresor (&eCompacting Upgrade&r) sám skládá věci do bloků, třeba 4 kusy do jednoho bloku. Ušetří místo.",
            "Obyčejný umí jen recepty 2 × 2. Pokročilý (&eAdvanced Compacting Upgrade&r) umí i 3 × 3, třeba 9 ingotů na blok.",
        ]),
        # --- větší sloty
        Q("stack1", "Víc věcí do slotu", dep=["base"], items=[("sophisticatedbackpacks:stack_upgrade_starter_tier", 1)], xp=25, d=[
            "Upgrade stohu (&eStack Upgrade&r) zvětší sloty batohu. Do jednoho slotu se vejde víc věcí.",
            "Startovní stupeň (&eStack Upgrade Starter Tier&r) dá 1,5× víc. Vyrobíš ho z 8 měděných bloků a základu upgradu.",
        ]),
        Q("stack2", "Stoh I", dep=["stack1"], items=[("sophisticatedbackpacks:stack_upgrade_tier_1", 1)], xp=30, d=[
            "První stupeň (&eStack Upgrade Tier 1&r) dá 2× víc věcí do slotu. Vyrobíš ho ze startovního stupně a 4 železných bloků.",
        ]),
        Q("stack3", "Stoh II", dep=["stack2"], items=[("sophisticatedbackpacks:stack_upgrade_tier_2", 1)], xp=40, d=[
            "Druhý stupeň (&eStack Upgrade Tier 2&r) dá 4× víc. Vyrobíš ho z prvního stupně a 8 zlatých bloků.",
        ]),
        Q("stack4", "Stoh III", dep=["stack3"], items=[("sophisticatedbackpacks:stack_upgrade_tier_3", 1)], xp=60, d=[
            "Třetí stupeň (&eStack Upgrade Tier 3&r) dá 8× víc. Potřebuje 8 diamantových bloků.",
        ]),
        Q("stack5", "Stoh IV", dep=["stack4", "gear:netherite"], items=[("sophisticatedbackpacks:stack_upgrade_tier_4", 1)], xp=100, d=[
            "Čtvrtý stupeň (&eStack Upgrade Tier 4&r) dá 16× víc věcí do slotu. Potřebuje 8 netheritových bloků.",
            "S tímhle je batoh skoro celý sklad.",
        ]),
        # --- pokročilé upgrady
        Q("smelting", "Pec v batohu", dep=["gold"], items=[("sophisticatedbackpacks:smelting_upgrade", 1)], xp=25, d=[
            "Upgrade pece (&eSmelting Upgrade&r) přidá do batohu záložku s pecí. Tavíš i na cestách.",
            "Vyrobíš ho z pece, železa, redstonu a základu upgradu.",
        ]),
        Q("auto_smelting", "Automatické tavení", dep=["smelting"], items=[("sophisticatedbackpacks:auto_smelting_upgrade", 1)], xp=40, d=[
            "Automatická pec (&eAuto-smelting Upgrade&r) si sama bere rudy i palivo z batohu a hotové ingoty do něj vrací.",
            "Vylepšíš ji z upgradu pece: přidej diamanty, zlato, násypky a redstone.",
        ]),
        Q("tank", "Nádrž", dep=["gold"], items=[("sophisticatedbackpacks:tank_upgrade", 1)], xp=25, d=[
            "Nádrž (&eTank Upgrade&r) změní část batohu na zásobník tekutin, třeba vody nebo lávy.",
            "Vyrobíš ji z 8 skleněných bloků a základu upgradu.",
        ]),
        Q("everlasting", "Nezničitelný batoh", dep=["netherite"], items=[("sophisticatedbackpacks:everlasting_upgrade", 1)], xp=100, d=[
            "Věčný upgrade (&eEverlasting Upgrade&r): batoh se nedá zničit. Nezmizí na zemi, neshoří a nespadne do prázdna (void).",
            "Je drahý: základ upgradu, 4 hvězdy z Netheru a 4 krystaly Endu (&eEnd Crystal&r).",
        ]),
        Q("inception", "Batoh v batohu", dep=["netherite"], items=[("sophisticatedbackpacks:inception_upgrade", 1)], xp=80, optional=True, d=[
            "Upgrade &eInception Upgrade&r dovolí dát batoh do jiného batohu.",
            "Potřebuješ hvězdu z Netheru, diamanty a ender oči.",
        ]),
        # --- Iron Chests
        Q("copper_chest", "Měděná truhla", dep=["start"], items=[("ironchest:copper_chest", 1)], xp=15, d=[
            "Mod &bIron Chests&r přidává větší truhly. Měděná truhla (&eCopper Chest&r) má 45 slotů (obyčejná 27).",
            "Obyčejnou truhlu obklop 8 měděnými ingoty.",
            "Další je železná truhla (&eIron Chest&r) s 54 sloty – najdeš ji v kapitole &eÚložiště&r.",
        ]),
        Q("upgrade_chest", "Vylepšení bez stěhování", dep=["copper_chest"], items=[("ironchest:wood_to_iron_chest_upgrade", 1)], xp=20, d=[
            "Vylepšení truhly (&eWood to Iron Chest Upgrade&r) změní položenou truhlu na lepší. Věci uvnitř zůstanou.",
            "Klikni s ním pravým tlačítkem na truhlu. Vyrábí se z 8 železných ingotů a prkna.",
            "Podobná vylepšení jsou i pro další stupně – najdeš je v JEI.",
        ]),
        Q("gold_chest", "Zlatá truhla", dep=["copper_chest", "storage:chest"], items=[("ironchest:gold_chest", 1)], xp=25, s="Pokročilý", d=[
            "Zlatá truhla (&eGold Chest&r) má 81 slotů. Železnou truhlu obklop 8 zlatými ingoty.",
        ]),
        Q("diamond_chest", "Diamantová truhla", dep=["gold_chest"], items=[("ironchest:diamond_chest", 1)], xp=40, d=[
            "Diamantová truhla (&eDiamond Chest&r) má 108 slotů. Vyrobíš ji ze zlaté truhly, 2 diamantů a 6 skleněných bloků.",
        ]),
        Q("crystal_chest", "Křišťálová truhla", dep=["diamond_chest"], items=[("ironchest:crystal_chest", 1)], xp=40, optional=True, d=[
            "Křišťálová truhla (&eCrystal Chest&r) je stejně velká jako diamantová, ale je průhledná. Skrz sklo vidíš, co je uvnitř.",
            "Diamantovou truhlu obklop 8 skleněnými bloky.",
        ]),
        Q("obsidian_chest", "Obsidiánová truhla", dep=["diamond_chest"], items=[("ironchest:obsidian_chest", 1)], xp=40, optional=True, d=[
            "Obsidiánová truhla (&eObsidian Chest&r) má také 108 slotů. Diamantovou truhlu obklop 8 obsidiány.",
            "Až budeš mít opravdu hodně věcí, podívej se na úložné systémy v kapitole &eÚložiště&r.",
        ]),
        # --- Ender Storage
        Q("ender_tank", "Sdílená nádrž", dep=["storage:ender"], items=[("enderstorage:ender_tank", 1)], xp=40, s="Expert",
          shape="hexagon", size=1.5, d=[
            "Ender nádrž (&eEnder Tank&r) funguje jako Ender truhla, jen na tekutiny. Dvě nádrže se stejnými barvami sdílejí obsah – i přes dimenze.",
            "Barvy nastavíš tak, že klikneš barvivem na jeden ze tří barevných proužků.",
            "Když klikneš diamantem na zámek, bude nádrž (i truhla) jen tvoje.",
            "Vyrobíš ji z ohnivých tyčí, vlny, obsidiánu, kotle a ender perly.",
        ]),
    ],
)

UTILITY = dict(
    key="utility", group="start", title="Užitečné mody",
    subtitle="Kořist, nástroje, hudba, spawnery a chunk loadery", icon="supplementaries:wrench",
    quests=[
        Q("start", "Užitečné mody", tasks=[auto()], icon="minecraft:chest", xp=10, s="Začátečník",
          shape="hexagon", size=1.5, d=[
            "V packu je spousta malých modů, které usnadňují hru. Tady je najdeš pohromadě.",
            "&bLootr&r (kořist), &bSupplementaries&r a &bAmendments&r (užitečné bloky), &bEtched&r (vlastní hudba), &bChimes&r (zvonkohry), &bApothic Spawners&r (úprava spawnerů) a &bChunk Loaders&r.",
            "Každá větev začíná jednoduše a končí věcmi pro zkušené hráče.",
        ]),
        # --- Lootr
        Q("loot1", "Truhla jen pro tebe", dep=["start"], tasks=[adv("lootr:1chest")], icon="lootr:lootr_chest", xp=15, d=[
            "Truhly v dungeonech, chrámech a jiných stavbách patří modu &bLootr&r.",
            "Každý hráč v nich najde vlastní kořist. Když truhlu vybere kamarád, ty v ní pořád najdeš svoje věci.",
            "Úkol: otevři první takovou truhlu.",
        ]),
        Q("loot10", "Sběratel kořisti", dep=["loot1"], tasks=[adv("lootr:10loot")], icon="lootr:lootr_barrel", xp=25, d=[
            "Úkol: otevři 10 různých truhel, sudů nebo jiných nádob s kořistí.",
            "Kořist je i ve vozících v dolech a v rámečcích na zdi.",
        ]),
        Q("loot50", "Lovec pokladů", dep=["loot10"], tasks=[adv("lootr:50loot")], icon="lootr:lootr_shulker", xp=50,
          s="Pokročilý", shape="hexagon", size=1.5, d=[
            "Úkol: otevři 50 nádob s kořistí.",
            "Nejvíc truhel najdeš v dungeonech, dolech, pevnostech a chrámech. Hledej je ve skupině &bPrůzkum a dimenze&r.",
        ]),
        Q("trophy", "Trofej", dep=["loot50"], items=[("lootr:trophy", 1)], xp=100, s="Expert", shape="hexagon", size=1.5, d=[
            "Když otevřeš 100 nádob s kořistí, dostaneš trofej (&eCentennial Trophy&r).",
            "Postav si ji doma na čestné místo.",
        ]),
        # --- Supplementaries
        Q("wrench", "Klíč na otáčení", dep=["start", "building:supp"], items=[("supplementaries:wrench", 1)], xp=15, d=[
            "Klíč (&eWrench&r) ze &bSupplementaries&r otáčí položené bloky. Hodí se na schody, truhly nebo trubky.",
            "Vyrobíš ho ze 4 měděných ingotů.",
        ]),
        Q("altimeter", "Výškoměr", dep=["wrench"], items=[("supplementaries:altimeter", 1)], xp=15, d=[
            "Výškoměr (&eAltimeter&r) ukáže, v jaké jsi výšce (Y). Hodí se při hledání diamantů.",
            "Vyrobíš ho z měděných ingotů a redstonu.",
        ]),
        Q("cage", "Klec", dep=["wrench"], items=[("supplementaries:cage", 1)], xp=20, d=[
            "Do klece (&eCage&r) chytíš malé zvíře a přeneseš ho. Některá zvířata musíš nejdřív ochočit.",
            "Klec můžeš i položit jako blok – zvíře v ní bude vidět.",
        ]),
        Q("quiver", "Toulec", dep=["wrench"], items=[("supplementaries:quiver", 1)], xp=30, d=[
            "Toulec (&eQuiver&r) unese hodně šípů na jednom místě. Klávesou &eV&r vybíráš, který druh šípu z toulce se bude střílet.",
            "Nedá se vyrobit. Najdeš ho jen v truhlách, třeba v dungeonech, v lesních sídlech nebo v základnách pillagerů.",
            "Můžeš ho nosit i ve slotu na doplňky. Ten otevřeš tlačítkem u postavičky v inventáři.",
        ]),
        Q("bomb", "Bomby", dep=["wrench"], items=[("supplementaries:bomb", 4)], xp=20, optional=True, d=[
            "Bombu (&eBomb&r) hodíš a ona po chvíli vybuchne.",
            "Z jednoho TNT, železa a provázku vyrobíš 4 bomby.",
            "&cPozor:&r bomby ničí bloky – nehaž je u domu.",
        ]),
        Q("cannon", "Kanón", dep=["bomb"], items=[("supplementaries:cannon", 1)], xp=40, s="Pokročilý", d=[
            "Kanón (&eCannon&r) umí vystřelit skoro cokoliv. Klikni na něj a v jeho okně ho nabiješ.",
            "Vyrobíš ho ze železných ingotů, prken a dávkovače.",
        ]),
        Q("safe", "Sejf", dep=["cage", "gear:netherite"], items=[("supplementaries:safe", 1), ("supplementaries:key", 1)], xp=60,
          s="Expert", shape="hexagon", size=1.5, d=[
            "Sejf (&eSafe&r) je úložiště, které otevře jen jeho majitel nebo hráč se správným klíčem (&eKey&r).",
            "Sejf vyrobíš ze shulkerové schránky a netheritového ingotu. Klíč ze zlatého ingotu a 2 zlatých nuggetů.",
        ]),
        Q("globe", "Glóbus", dep=["altimeter"], items=[("supplementaries:globe", 1)], xp=30, optional=True, d=[
            "Glóbus (&eGlobe&r) je ozdoba s mapou světa. Když ho roztočíš hodně rychle, dostaneš ocenění.",
            "Najdeš ho v pokladech vraků lodí nebo ho prodává potulný obchodník.",
        ]),
        # --- Amendments
        Q("lantern", "Lucerna na zdi", dep=["start"], items=[("minecraft:lantern", 4)], xp=10, d=[
            "Mod &bAmendments&r vylepšuje obyčejné bloky. Třeba lucernu můžeš pověsit na zeď.",
            "Další vychytávky: koberec na schodech a půlblocích, zavěšený květináč, háček na nástroje a míchání lektvarů v kotli.",
            "Lucernu vyrobíš z pochodně a železných nuggetů.",
        ]),
        # --- Etched
        Q("blank_disc", "Prázdná deska", dep=["start", "building:etched"], items=[("etched:blank_music_disc", 1)], xp=20, d=[
            "Mod &bEtched&r umí nahrát vlastní písničku na hudební desku.",
            "Prázdnou desku (&eBlank Music Disc&r) získáš tak, že v peci roztavíš hudební desku (kromě desky Stal).",
            "Hudební desky najdeš v truhlách. Padají i z creepera, kterého zabije kostlivec.",
        ]),
        Q("etched_disc", "Vlastní písnička", dep=["blank_disc"], items=[("etched:etched_music_disc", 1)], xp=30, d=[
            "Na rycím stole (&eEtching Table&r) dej do slotů prázdnou desku a hudební štítek (&eMusic Label&r). Štítek vyrobíš ze 4 papírů.",
            "Do textového pole vlož odkaz na písničku a vezmi si hotovou desku (&eEtched Music Disc&r).",
            "Hraje v obyčejném jukeboxu a uslyší ji všichni kolem.",
        ]),
        Q("boombox", "Boombox", dep=["etched_disc"], items=[("etched:boombox", 1)], xp=30, d=[
            "Boombox (&eBoombox&r) je přenosný jukebox. Hraje, i když ho neseš.",
            "Vyrobíš ho z mědi, redstonu a jukeboxu.",
        ]),
        Q("album", "Album", dep=["etched_disc"], items=[("etched:album_jukebox", 1)], xp=40, optional=True, d=[
            "Hrací skříň na alba (&eAlbum Jukebox&r) pojme víc desek a hraje je jednu po druhé.",
            "Vyrobíš ji z jukeboxu, truhly, opakovače a redstonu.",
        ]),
        # --- Chimes
        Q("chimes", "Zvonkohra", dep=["start"], items=[("chimes:bamboo_chimes", 1)], xp=10, optional=True, d=[
            "Zvonkohra (&eBamboo Wind Chime&r) z modu &bChimes&r je ozdoba, která sama od sebe tiše cinká.",
            "Pověs ji pod strop nebo pod větev. Vyrobíš ji z dřevěného půlbloku, provázku a bambusu.",
            "Další druhy jsou ze železa, mědi, ametystu nebo skla.",
        ]),
        # --- Apothic Spawners
        Q("spawner_mod", "Upravený spawner", dep=["start", "exploration:spawner"], tasks=[adv("apothic_spawners:modifier")],
          icon="minecraft:sugar", xp=40, s="Pokročilý", d=[
            "S modem &bApothic Spawners&r vykopeš spawner krumpáčem s očarováním Hedvábný dotek (Silk Touch).",
            "Spawner pak můžeš vylepšit: drž předmět v ruce a klikni na spawner pravým tlačítkem. Co který předmět dělá, ukáže JEI.",
            "Úkol: uprav spawner. Třeba cukr zkrátí čekání mezi příšerami.",
        ]),
        Q("capturing", "Vajíčko z příšery", dep=["spawner_mod"], tasks=[adv("apothic_spawners:capturing")],
          icon="minecraft:zombie_spawn_egg", xp=40, optional=True, d=[
            "Očarování &eCapturing&r (Apothic Spawners) a &eReplication&r (Replication Enchantment) dávají šanci, že příšera upustí svoje spawnovací vajíčko.",
            "Vajíčkem pak změníš, jaká příšera ze spawneru leze: klikni s ním na spawner.",
            "Úkol: získej vajíčko pomocí očarování Capturing.",
        ]),
        Q("spawner_count", "Velká farma", dep=["spawner_mod"], tasks=[adv("apothic_spawners:spawncount")],
          icon="minecraft:fermented_spider_eye", xp=60, d=[
            "Kvašené pavoučí oko zvýší, kolik příšer se objeví najednou.",
            "Úkol: zvyš počet příšer ze spawneru až na 16.",
        ]),
        Q("spawner_ultimate", "Dokonalý spawner", dep=["spawner_count"], tasks=[adv("apothic_spawners:ultimate_spawner")],
          icon="minecraft:nether_star", xp=150, s="Expert", shape="hexagon", size=1.5, d=[
            "Úkol pro experty: spawner s nejkratším čekáním, ovládaný redstonem, bez umělé inteligence příšer (No AI), bez podmínek a bez nutnosti hráče poblíž.",
            "Potřebuješ: cukr a hodiny (kratší čekání), komparátor (ovládání redstonem), chorusové ovoce (No AI), kondukt (bez podmínek) a hvězdu z Netheru (bez hráče).",
        ]),
        # --- Chunk loaders
        Q("chunk_basic", "Chunk loader 3 × 3", dep=["welcome:chunks"], items=[("chunkloaders:basic_chunk_loader", 1)], xp=30, d=[
            "Základní chunk loader (&eBasic Chunk Loader&r) udrží zapnutou oblast 3 × 3 chunky.",
            "Vyrobíš ho ze železných ingotů, obsidiánu a ender perly. Z 9 malých chunk loaderů ho taky složíš zpátky.",
        ]),
        Q("chunk_advanced", "Chunk loader 5 × 5", dep=["chunk_basic"], items=[("chunkloaders:advanced_chunk_loader", 1)], xp=50,
          s="Pokročilý", d=[
            "Pokročilý chunk loader (&eAdvanced Chunk Loader&r) drží oblast 5 × 5 chunků. Stačí na velkou farmu nebo továrnu.",
            "Základní chunk loader obklop zlatými ingoty a ohnivým práškem.",
        ]),
        Q("chunk_ultimate", "Chunk loader 7 × 7", dep=["chunk_advanced"], items=[("chunkloaders:ultimate_chunk_loader", 1)], xp=80,
          s="Expert", shape="hexagon", size=1.5, d=[
            "Nejlepší chunk loader (&eUltimate Chunk Loader&r) drží oblast 7 × 7 chunků.",
            "Pokročilý chunk loader obklop diamanty, ender očima a redstonem.",
            "&cZapínej jen chunky, které opravdu potřebuješ.&r Server ti poděkuje.",
        ]),
    ],
)

QUARK = dict(
    key="quark", group="start", title="Quark",
    subtitle="Drobná vylepšení, která snadno přehlédneš", icon="quark:seed_pouch",
    quests=[
        Q("start", "Co umí Quark", tasks=[auto()], icon="quark:seed_pouch", xp=10, s="Začátečník",
          shape="hexagon", size=1.5, d=[
            "&bQuark&r přidává stovky malých vylepšení. Spousta z nich funguje sama:",
            "Dvojité dveře se otevírají spolu. Cedulku upravíš pravým kliknutím. Motyka sklidí trávu a rostliny v širším pruhu.",
            "Po žebříku sjedeš rychleji, když se díváš dolů. Žebřík položíš i na žebřík pravým kliknutím – sjede dolů.",
            "{@pagebreak}",
            "V inventáři a truhlách jsou nová tlačítka: třídění věcí a rychlé přesouvání. V truhle můžeš i hledat.",
            "Nechtěný předmět zničíš, když ho v inventáři vezmeš a klikneš s ním pravým tlačítkem na kbelík lávy. Stojan na brnění má ruce.",
            "&aTip:&r Když v JEI najedeš na věc z Quarku, často u ní najdeš krátký popis.",
        ]),
        # --- užitečné předměty
        Q("pouch", "Pytlík na semínka", dep=["start"], items=[("quark:seed_pouch", 1)], xp=20, d=[
            "Pytlík na semínka (&eSeed Pouch&r) pojme hodně kusů jednoho druhu semínek nebo sazenic. Zabere jen jeden slot.",
            "Semínka do něj dáš kliknutím. Když ho držíš, sám sbírá semínka. Kliknutím na pole zasadíš celou plochu 3 × 3.",
            "Vyrobíš ho z kůže, provázku a semínka.",
        ]),
        Q("trowel", "Zednická lžíce", dep=["start"], items=[("quark:trowel", 1)], xp=20, d=[
            "Zednická lžíce (&eTrowel&r) pokládá náhodný blok z tvé lišty rychlého přístupu. Skvělé na přirozeně vypadající zdi a cesty.",
            "Když dáš stejný blok do víc slotů, bude se objevovat častěji. Lžíce se nikdy nerozbije.",
        ]),
        Q("crate", "Bedna", dep=["start"], items=[("quark:crate", 1)], xp=20, d=[
            "Bedna (&eStorage Crate&r) pojme až 640 věcí bez ohledu na to, kolik se jich vejde do stohu.",
            "Je skvělá na nástroje, výbavu a spoustu různých drobností.",
        ]),
        Q("abacus", "Počítadlo", dep=["start"], items=[("quark:abacus", 1)], xp=15, d=[
            "Počítadlo (&eAbacus&r) změří vzdálenost mezi dvěma bloky (až 48 bloků).",
            "Klikni s ním na první blok a pak se podívej na druhý.",
        ]),
        Q("rope", "Lano", dep=["start"], items=[("quark:rope", 3)], xp=15, d=[
            "Lano (&eRope Coil&r) pověs pod strop a šplhej po něm.",
            "Když klikneš lanem na lano, prodlouží se dolů. Se Shiftem ho zase vytáhneš nahoru.",
            "Vyrobíš ho z 6 provázků.",
        ]),
        Q("trough", "Koryto", dep=["start"], items=[("quark:feeding_trough", 1)], xp=15, d=[
            "Koryto (&eFeeding Trough&r) nakrmí zvířata za tebe. Dej do něj jejich jídlo a ona se z něj sama nakrmí a množí.",
            "Když je kolem moc zvířat, přestanou se množit.",
        ]),
        Q("glass_frame", "Skleněný rámeček", dep=["start"], items=[("quark:glass_item_frame", 1)], xp=10, optional=True, d=[
            "Skleněný rámeček (&eGlass Item Frame&r) je skoro neviditelný. Uvidíš jen předmět, který do něj dáš.",
            "Z 8 skleněných tabulí a rámečku vyrobíš 2 kusy.",
        ]),
        Q("torch_arrow", "Šíp s pochodní", dep=["start"], items=[("quark:torch_arrow", 8)], xp=10, optional=True, d=[
            "Šíp s pochodní (&eTorch Arrow&r) postaví pochodeň tam, kam dopadne. Rychle tak osvětlíš velkou jeskyni.",
        ]),
        Q("cloud", "Mrak v lahvi", dep=["start"], items=[("quark:bottled_cloud", 1)], xp=25, d=[
            "Mrak v lahvi (&eCloud in a Bottle&r) postaví dočasný blok ve vzduchu. Na něj pak můžeš stavět dál.",
            "Naber ho prázdnou lahví ve výšce mraků (Y 191 až 196).",
        ]),
        Q("slime", "Sliz v kbelíku", dep=["start"], items=[("quark:slime_in_a_bucket", 1)], xp=20, d=[
            "Klikni kbelíkem na malého slizouna a máš slizouna v kbelíku (&eBucket of Slime&r).",
            "Začne poskakovat, když jsi ve slizovém chunku – tam se slizouni objevují.",
        ]),
        Q("crab", "Krab", dep=["slime"], tasks=[adv("quark:content/crab_in_a_bucket")], icon="minecraft:bucket", xp=20, optional=True, d=[
            "Kraby najdeš na plážích. Chovat je můžeš pšenicí, kuřecím masem nebo rybou.",
            "Úkol: chyť kraba do kbelíku s vodou.",
        ]),
        # --- automatizace
        Q("chute", "Skluz", dep=["start"], items=[("quark:chute", 1)], xp=15, d=[
            "Skluz (&eChute&r) pustí věci z násypky nebo podavače rovnou na zem pod sebe. Je to levná náhrada násypky.",
            "Vyrobíš ho z prken a klacků.",
        ]),
        Q("pipe", "Trubky", dep=["chute"], items=[("quark:pipe", 8)], xp=20, d=[
            "Měděné trubky (&eCopper Pipe&r) posílají věci dál. Věci do nich dostaneš násypkou nebo podavačem.",
            "Věci padají nejdřív dolů, pak dopředu, pak do stran a až nakonec nahoru. Redstonový signál trubku vypne.",
            "Ze 2 měděných ingotů a skla vyrobíš 6 trubek.",
        ]),
        Q("randomizer", "Náhodný signál", dep=["chute"], items=[("quark:redstone_randomizer", 1)], xp=15, optional=True, d=[
            "Redstonový randomizér (&eRedstone Randomizer&r) pošle signál náhodně doleva nebo doprava.",
        ]),
        Q("magnet", "Magnet", dep=["pipe"], items=[("quark:magnet", 1)], xp=30, s="Pokročilý", shape="hexagon", size=1.5, d=[
            "Magnet (&eMagnet&r) zapnutý redstonem tlačí nebo přitahuje bloky ze železa nebo mědi.",
            "Je to nový druh redstonových strojů. Víc magnetů na jeden blok? Vyhraje ten nejsilnější.",
            "Vyrobíš ho z dlažebního kamene, železa, modrého barviva, chorusového ovoce a redstonu. Chorusové ovoce roste v Endu.",
        ]),
        Q("gravisand", "Gravitační písek", dep=["magnet"], items=[("quark:gravisand", 1)], xp=20, optional=True, d=[
            "Gravitační písek (&eGravisand&r) spadne jen po redstonovém signálu. Když spadnout nemůže, vyletí nahoru.",
            "Z 8 písku a ender perly vyrobíš 8 kusů.",
        ]),
        Q("watcher", "Endový sledovač", dep=["magnet"], items=[("quark:ender_watcher", 1)], xp=25, d=[
            "Endový sledovač (&eEnder Watcher&r) vyšle redstonový signál, když se na něj díváš. Čím přesněji míříš na střed, tím silnější signál.",
            "Hodí se na tajné dveře.",
        ]),
        Q("iron_rod", "Železná tyč", dep=["magnet"], items=[("quark:iron_rod", 1)], xp=30, d=[
            "Železná tyč (&eIron Rod&r) rozbije blok před sebou, když ji posune píst. Tak postavíš automatický důl nebo farmu.",
            "Vyrobíš ji ze železných ingotů a tyče z Endu (&eEnd Rod&r). Tu vyrobíš z ohnivé tyče a prasklého chorusového ovoce, nebo ji najdeš v Endu.",
        ]),
        # --- dobrodružství
        Q("heart", "Diamantové srdce", dep=["start"], items=[("quark:diamond_heart", 1)], xp=30, d=[
            "Diamantové srdce (&eHeart of Diamond&r) nosí kamenný tvoreček &eStoneling&r. Najdeš ho hluboko v jeskyních.",
            "Rozbij jeho skořápku a srdce vypadne. Neboj, Stonelingovi se nic nestane.",
            "Srdce potřebuješ na pickarang a na malou bramboru.",
        ]),
        Q("pickarang", "Pickarang", dep=["heart"], items=[("quark:pickarang", 1)], xp=40, d=[
            "Pickarang (&ePickarang&r) je krumpáč, který se hází jako bumerang. Vykope blok, do kterého narazí, a přinese ti ho zpátky.",
            "Vyrobíš ho z diamantů, prken a diamantového srdce. Dá se i očarovat.",
        ]),
        Q("flamerang", "Flamarang", dep=["pickarang", "gear:netherite"], items=[("quark:flamerang", 1)], xp=80, s="Expert", shape="hexagon", size=1.5, d=[
            "Flamarang (&eFlamarang&r) je netheritová verze pickarangu. Věci, které sebere, neshoří v lávě ani v ohni.",
            "Vylepšíš ho na kovářském stole: šablona netheritového vylepšení + pickarang + netheritový ingot.",
        ]),
        Q("potato", "Malá brambora", dep=["heart"], items=[("quark:tiny_potato", 1)], xp=10, optional=True, d=[
            "Malá brambora (&eTiny Potato&r) v tebe věří!",
            "Vyrobíš ji z brambory a diamantového srdce. Klikni na ni a pohlaď ji.",
        ]),
        Q("quill", "Brk hledače", dep=["start"], items=[("quark:pathfinders_quill", 1)], xp=40, d=[
            "Brk hledače (&ePathfinder's Quill&r) najde biom, který je na něm napsaný. Až ho najde, změní se v mapu.",
            "Koupíš ho od kartografa ve vesnici nebo od potulného obchodníka.",
        ]),
        Q("soul_bead", "Duševní korálek", dep=["quill"], items=[("quark:soul_bead", 1)], xp=40, optional=True, d=[
            "Duševní korálek (&eSoul Bead&r) padá z přízraků (&eWraith&r) v údolí duší v Netheru.",
            "Když ho použiješ, poletí směrem k nejbližší netherové pevnosti.",
        ]),
        Q("forgotten_hat", "Klobouk Zapomenutého", dep=["heart"], items=[("quark:forgotten_hat", 1)], xp=60, optional=True, d=[
            "Klobouk (&eForgotten Hat&r) padá ze Zapomenutého (&eForgotten&r). Ten žije hluboko pod zemí.",
            "&cPozor:&r má silnou výbavu a umí bojovat zblízka i na dálku.",
        ]),
        # --- očarování
        Q("tome", "Prastarý svazek", dep=["start"], items=[("quark:ancient_tome", 1)], xp=60, d=[
            "Prastarý svazek (&eAncient Tome&r) zvýší očarování o jednu úroveň – až o jednu nad normální maximum.",
            "Najdeš ho v truhlách: v knihovnách pevností (stronghold), v dungeonech, v pokladech bastionů, v lesních sídlech a v prastarých městech.",
            "Spoj ho na kovadlině s předmětem nebo knihou, která má stejné očarování na maximu.",
        ]),
        Q("overlevel", "Nad maximum", dep=["tome"], tasks=[adv("quark:content/overlevel_enchant")], icon="minecraft:enchanted_book",
          xp=80, s="Expert", shape="hexagon", size=1.5, d=[
            "Úkol: pomocí prastarého svazku dej předmětu očarování nad normální maximum, třeba &eSharpness VI&r.",
            "&aTip:&r Mistr knihovník ti svazek vymění, když mu dáš knihu se stejným očarováním na maximu.",
        ]),
        Q("influence", "Svíčky a očarování", dep=["start", "vanilla:enchant"], tasks=[adv("quark:content/influence")],
          icon="minecraft:candle", xp=40, d=[
            "Barevné svíčky na knihovnách u očarovacího stolu zvýší šanci na určitá očarování. Každá barva patří k jinému.",
            "Když pod svíčkou (nebo pod její knihovnou) je písek duší, šanci naopak sníží.",
            "Úkol: ovlivni očarování svíčkou.",
        ]),
    ],
)

GEAR = dict(
    key="gear", group="explore", title="Výbava a boj",
    subtitle="Zbraně, brnění, štíty a ozdoby s efekty", icon="spartanshieldsunofficial:iron_tower_shield",
    quests=[
        Q("start", "Výbava a boj", tasks=[auto()], icon="minecraft:iron_sword", xp=10, s="Začátečník",
          shape="hexagon", size=1.5, d=[
            "Postup výbavy: dřevo → kámen → železo → diamant → netherit → &bAdvanced Netherite&r.",
            "Cestou si vyrobíš lepší štíty (&bSpartan Shields&r), ozdobíš brnění vzory s efekty (&bTrimsEffects&r) a získáš vzácné zbraně.",
            "Základní nástroje a první brnění najdeš v kapitole &ePrvní dny&r.",
        ]),
        # --- štíty (Spartan Shields)
        Q("wood_shield", "Dřevěný štít", dep=["start"], items=[("spartanshieldsunofficial:wooden_basic_shield", 1)], xp=10, d=[
            "Mod &bSpartan Shields&r přidává štíty z mnoha materiálů. Hrubý dřevěný štít (&eCrude Wooden Shield&r) je základ všech malých štítů.",
            "Vyrobíš ho z prken a klacku.",
            "V popisku štítu uvidíš, jak moc tě chrání a jestli umí úder štítem (&eShield Bash&r).",
        ]),
        Q("shield", "Železný štít", dep=["wood_shield"], items=[("spartanshieldsunofficial:iron_basic_shield", 1)], xp=20, d=[
            "Železný štít (&eIron Plated Shield&r) vyrobíš z dřevěného štítu a 4 železných ingotů.",
            "Stejně fungují i další kovy z packu. JEI ti ukáže, které.",
            "&aTip:&r Na štít můžeš dát vlajku (prapor), jako na obyčejný štít.",
        ]),
        Q("wood_tower", "Dřevěný věžový štít", dep=["wood_shield"], items=[("spartanshieldsunofficial:wooden_tower_shield", 1)], xp=10, d=[
            "Věžový štít (&eWooden Tower Shield&r) je větší a kryje víc těla. Je základem všech věžových štítů.",
            "Vyrobíš ho z prken a klacku (víc prken než malý štít).",
        ]),
        Q("tower", "Železný věžový štít", dep=["wood_tower", "shield"], items=[("spartanshieldsunofficial:iron_tower_shield", 1)], xp=25, d=[
            "Železný věžový štít (&eIron Tower Shield&r) vyrobíš z dřevěného věžového štítu a 6 železných ingotů.",
            "Porovnej popisky malého a věžového štítu a vyber si, co ti víc vyhovuje.",
        ]),
        Q("deflect", "Odraz šíp", dep=["shield"], tasks=[adv("minecraft:story/deflect_arrow")], icon="minecraft:arrow", xp=15, d=[
            "Úkol: zablokuj štítem šíp nebo jinou střelu.",
            "Drž pravé tlačítko a dívej se na nepřítele. Kostlivci ti pak skoro neublíží.",
        ]),
        Q("diamond_shield", "Diamantový věžový štít", dep=["tower"], items=[("spartanshieldsunofficial:diamond_tower_shield", 1)], xp=40, d=[
            "Diamantový věžový štít (&eDiamond Tower Shield&r) vydrží mnohem víc ran.",
            "Vyrobíš ho z dřevěného věžového štítu a 6 diamantů.",
        ]),
        Q("obsidian_shield", "Obsidiánový štít", dep=["shield"], items=[("spartanshieldsunofficial:obsidian_basic_shield", 1)], xp=25, optional=True, d=[
            "Obsidiánový štít (&eBulky Obsidian Shield&r) vyrobíš z dřevěného štítu a obsidiánu.",
        ]),
        Q("netherite_shield", "Netheritový štít", dep=["diamond_shield", "netherite"], items=[("spartanshieldsunofficial:netherite_tower_shield", 1)],
          xp=80, d=[
            "Netheritový věžový štít (&eNetherite Tower Shield&r) je nejodolnější obyčejný štít.",
            "Vylepšíš ho na kovářském stole: šablona netheritového vylepšení + diamantový věžový štít + netheritový ingot.",
        ]),
        # --- zbraně a brnění
        Q("bow", "Luk a šípy", dep=["start"], items=[("minecraft:bow", 1), ("minecraft:arrow", 16)], xp=15, d=[
            "Luk vyrobíš z klacků a provázku. Provázek padá z pavouků.",
            "Šípy jsou z pazourku, klacku a pírka.",
            "&aTip:&r Toulec ze &bSupplementaries&r unese hodně šípů (kapitola &eUžitečné mody&r).",
        ]),
        Q("crossbow", "Kuše", dep=["bow"], tasks=[adv("minecraft:adventure/ol_betsy")], icon="minecraft:crossbow", xp=15, optional=True, d=[
            "Kuše střílí silněji než luk a dá se nabít dopředu.",
            "Úkol: vystřel z kuše.",
        ]),
        Q("golden_apple", "Zlaté jablko", dep=["start"], items=[("minecraft:golden_apple", 1)], xp=20, d=[
            "Zlaté jablko tě rychle vyléčí a dá ti pár srdíček navíc. Vezmi si ho na každý těžký boj.",
            "Vyrobíš ho z jablka a 8 zlatých ingotů.",
        ]),
        Q("diamond_sword", "Diamantový meč", dep=["start"], items=[("minecraft:diamond_sword", 1)], xp=25, d=[
            "Diamantový meč je velký skok proti železnému. Vyrobíš ho ze 2 diamantů a klacku.",
            "Očaruj ho. Nejlepší jsou &eSharpness&r (víc poškození) a &eLooting&r (víc kořisti z příšer).",
        ]),
        Q("shiny", "Diamantové brnění", dep=["diamond_sword"], tasks=[adv("minecraft:story/shiny_gear")], icon="minecraft:diamond_chestplate",
          xp=40, s="Pokročilý", shape="hexagon", size=1.5, d=[
            "Úkol: vyrob si kus diamantového brnění.",
            "Celá sada stojí 24 diamantů. Diamantové brnění se později vylepší na netheritové, takže se neztratí.",
        ]),
        Q("trim", "Ozdoba s efektem", dep=["shiny"], tasks=[adv("minecraft:adventure/trim_with_any_armor_pattern")],
          icon="minecraft:sentry_armor_trim_smithing_template", xp=40, d=[
            "Ozdoby brnění (trims) dáš na brnění na kovářském stole: šablona ozdoby + kus brnění + materiál (třeba zlato, smaragd nebo měď).",
            "Šablony najdeš v truhlách různých staveb. Každá stavba má jiný vzor. Kopii šablony vyrobíš z 7 diamantů – recept ukáže JEI.",
            "{@pagebreak}",
            "Mod &bTrimsEffects&r dává ozdobám efekty. Když máš stejný vzor na 3 kusech brnění, dostaneš efekt I. Na všech 4 kusech efekt II.",
            "Například: Sentry = odolnost, Dune = rychlost, Coast = dýchání pod vodou, Eye = regenerace, Spire = síla, Snout = odolnost vůči ohni, Rib = spěch, Flow = skok.",
            "&cPozor:&r efekty dostanou i příšery, které mají ozdobené brnění.",
        ]),
        Q("trim_all", "Sběratel vzorů", dep=["trim"], tasks=[adv("minecraft:adventure/trim_with_all_exclusive_armor_patterns")],
          icon="minecraft:silence_armor_trim_smithing_template", xp=150, optional=True, d=[
            "Úkol pro experty: použij na kovářském stole každou ze vzácných šablon: Spire, Snout, Rib, Ward, Silence, Vex, Tide a Wayfinder.",
            "Většinou jsou v truhlách v End City, v bastionech, v pevnostech v Netheru, v prastarých městech a v lesních sídlech. Tide padá z Elder Guardiana a Wayfinder najdeš v ruinách (Trail Ruins).",
        ]),
        # --- netherit
        Q("netherite", "Netherit", dep=["shiny"], items=[("minecraft:netherite_ingot", 1)], xp=40, d=[
            "Netheritový ingot vyrobíš ze 4 netheritových úlomků a 4 zlatých ingotů. Úlomky se tají z prastarých trosek (Ancient Debris) z Netheru.",
            "Jak je najít, se dozvíš ve skupině &bPrůzkum a dimenze&r.",
            "Netherit ale není konec. Mod &bAdvanced Netherite&r ho vylepší ještě ve čtyřech stupních.",
        ]),
        Q("netherite_armor", "Netheritové brnění", dep=["netherite"], tasks=[adv("minecraft:nether/netherite_armor")],
          icon="minecraft:netherite_chestplate", xp=100, s="Expert", shape="hexagon", size=1.5, d=[
            "Úkol: získej celou sadu netheritového brnění (všechny 4 kusy).",
            "Na kovářském stole dej šablonu netheritového vylepšení, diamantový kus brnění a netheritový ingot. Očarování zůstanou.",
            "Šablonu najdeš v truhlách bastionů v Netheru. Nevyhazuj ji – z ní, 7 diamantů a 1 netherracku (&eNetherrack&r) vyrobíš 2 šablony.",
            "Netheritové věci neshoří v lávě.",
        ]),
        # --- Advanced Netherite
        Q("an_iron", "Netherit-železo", dep=["netherite"], items=[("advancednetherite:netherite_iron_ingot", 1)], xp=60, d=[
            "Ingot &eNetherite-Iron Ingot&r vyrobíš z netheritového ingotu a 4 železných ingotů.",
            "Každý stupeň Advanced Netherite je silnější než ten předchozí a má vlastní bonusy. Podrž Shift nad předmětem a uvidíš je.",
            "Bonusy jsou třeba víc surovin z rud, víc kořisti z příšer nebo to, že tě některé příšery nechají na pokoji.",
        ]),
        Q("an_tools", "Lepší nástroje", dep=["an_iron"], items=[("advancednetherite:netherite_iron_pickaxe", 1)], xp=60, d=[
            "Nástroje a brnění vylepšíš na kovářském stole: šablona netheritového vylepšení + netheritový nástroj + ingot &eNetherite-Iron Ingot&r.",
            "Výsledek je &eNetherite-Iron Pickaxe&r. Další stupně vylepšuješ stejně, vždy z předchozího stupně.",
        ]),
        Q("an_gold", "Netherit-zlato", dep=["an_iron"], items=[("advancednetherite:netherite_gold_ingot", 1)], xp=80, d=[
            "Ingot &eNetherite-Gold Ingot&r vyrobíš z ingotu &eNetherite-Iron Ingot&r a 4 zlatých ingotů.",
        ]),
        Q("an_emerald", "Netherit-smaragd", dep=["an_gold"], items=[("advancednetherite:netherite_emerald_ingot", 1)], xp=100, d=[
            "Ingot &eNetherite-Emerald Ingot&r vyrobíš z ingotu &eNetherite-Gold Ingot&r a 4 smaragdů.",
        ]),
        Q("an_diamond", "Netherit-diamant", dep=["an_emerald"], items=[("advancednetherite:netherite_diamond_ingot", 1)], xp=150,
          s="Expert", shape="hexagon", size=1.5, d=[
            "Ingot &eNetherite-Diamond Ingot&r je nejlepší stupeň. Vyrobíš ho z ingotu &eNetherite-Emerald Ingot&r a 4 diamantů.",
        ]),
        Q("an_armor", "Nejlepší brnění", dep=["an_diamond", "netherite_armor"], tasks=[adv("advancednetherite:nether/netherite_diamond_armor")],
          icon="advancednetherite:netherite_diamond_chestplate", xp=200, optional=True, d=[
            "Úkol pro experty: získej celou sadu brnění &eNetherite-Diamond&r (všechny 4 kusy).",
            "Každý kus musíš vylepšit přes všechny čtyři stupně. Šablon budeš potřebovat hodně.",
        ]),
        # --- vzácné věci
        Q("totem", "Totem nesmrtelnosti", dep=["shiny"], tasks=[adv("minecraft:adventure/totem_of_undying")], icon="minecraft:totem_of_undying",
          xp=60, optional=True, d=[
            "Totem nesmrtelnosti tě jednou zachrání před smrtí, když ho držíš v ruce. Pak zmizí.",
            "Padá z vyvolávačů (Evoker) v lesních sídlech a při nájezdech na vesnici.",
            "Úkol: přežij smrt díky totemu.",
        ]),
        Q("mace", "Palcát", dep=["netherite_armor"], items=[("minecraft:mace", 1)], xp=100, optional=True, d=[
            "Palcát je silná zbraň: čím z větší výšky na nepřítele skočíš, tím silněji udeříš.",
            "Vyrobíš ho z těžkého jádra (&eHeavy Core&r) a větrné tyče (&eBreeze Rod&r). Obojí najdeš ve zkušebních komnatách (Trial Chambers).",
        ]),
        Q("elytra", "Křídla a slot", dep=["netherite_armor"], tasks=[adv("minecraft:end/elytra")], icon="minecraft:elytra", xp=60, optional=True, d=[
            "Krovky (elytra) najdeš na lodích u měst v Endu.",
            "Díky modu &bElytra Slot&r je můžeš dát do slotu na záda. Na hrudi pak dál nosíš brnění. Sloty otevřeš tlačítkem u postavičky v inventáři.",
            "Do slotu na záda patří i batoh, takže si možná budeš muset vybrat.",
        ]),
        # --- materiály z modů
        Q("brass", "Mosazné brnění", dep=["start", "create:brass"], items=[("create_sa:brass_chestplate", 1)], xp=30, d=[
            "Mod &bCreate Stuff & Additions&r přidává brnění z mosazi. Kyrys (&eBrass Chestplate&r) vyrobíš z 8 mosazných ingotů.",
            "Mosaz se vyrábí v míchačce z modu Create (viz kapitoly Create).",
        ]),
        Q("kiwano", "Kiwano brnění", dep=["start", "nether_end:exotics"], items=[("netherexotics:kiwano_chestplate", 1)], xp=40, d=[
            "Mod &bNether Exotics&r přidává brnění a nástroje z ovoce z Netheru.",
            "Kyrys (&eKiwano Chestplate&r) vyrobíš z 8 slupek kiwana (&eKiwano Peel&r). Slupka ti zůstane, když kiwano sníš.",
            "Kiwano brnění zmírňuje popáleniny. Kiwano nástroje vykopané věci rovnou přetaví.",
        ]),
        Q("cruorite", "Kruorit", dep=["start", "nether_end:jin"], items=[("just_in_nether:cruorite", 1)], xp=40, d=[
            "Kruorit (&eCruorite&r) je vzácný kov z modu &bJust In Nether&r.",
            "Získáš ho přetavením suroviny &eKindarx&r ve vysoké peci. &eKindarx&r padá z tvora &eBullkindar&r v Netheru.",
            "&cV tomto packu ho zatím na nic nepoužiješ.&r Zbraně z něj vyrábí jiný mod, který v packu není. Ber ho jako sběratelský kov.",
        ]),
        Q("devourite", "Devourit", dep=["cruorite"], items=[("just_in_nether:devourite", 1)], xp=50, d=[
            "Devourit (&eDevourite&r) získáš přetavením suroviny &ePigar&r ve vysoké peci. &ePigar&r padá z tvora &ePigmar&r v Netheru.",
            "&cStejně jako kruorit ho v tomto packu zatím na nic nepoužiješ.&r Je to sběratelský kov.",
        ]),
    ],
)

# Pořadí kapitol této oblasti v knize questů
CHAPTERS = [WELCOME, VANILLA, BACKPACKS, UTILITY, QUARK, GEAR]

# Předměty bez receptu/loot table v datech, ale ověřeně získatelné
NO_RECIPE = {
    "quark:ancient_tome": "Quark přidává do truhel kódem (config tools.ancient_tomes: stronghold_library, simple_dungeon, bastion_treasure, woodland_mansion, ancient_city, monster_box) + výměna u mistra knihovníka",
    "etched:etched_music_disc": "vyrábí se na Etching Table z Blank Music Disc + Music Label a URL (GUI, ne recept)",
}
