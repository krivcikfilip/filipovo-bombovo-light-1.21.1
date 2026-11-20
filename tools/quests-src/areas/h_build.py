from engine import *

# =====================================================================
#  MineColonies 1: Založení kolonie (původní kapitola "minecolonies")
# =====================================================================
COLONIES = dict(
    key="minecolonies", group="build", title="Kolonie: Založení",
    subtitle="Vesnice, která se staví sama (MineColonies)", icon="minecolonies:blockhuttownhall",
    quests=[
        Q("intro", "Starostou kolonie", icon="minecolonies:blockhuttownhall", tasks=[auto()], xp=10, d=[
            "&bMineColonies&r: založíš si vesnici s občany. Ty jsi starosta, práci dělají občané.",
            "Občané staví budovy, kácí stromy, farmaří, těží a vaří. Ty jim dodáváš materiál a rozhoduješ, co se postaví.",
            "",
            "V této kapitole kolonii založíš a postavíš první budovy ve správném pořadí. Další kapitoly: &eŽivot občanů&r, &eŘemeslníci&r, &eVýzkum a obrana&r a &eNástroje a styly&r.",
            "{@pagebreak}",
            "&aTip:&r MineColonies má i český překlad. Názvy tlačítek proto píšeme česky a v závorce anglicky – podle toho, jaký jazyk máš ve hře nastavený.",
            "&aTip:&r &bJadeColonies&r: když se podíváš na budovu nebo občana, nahoře uvidíš jméno, práci a další informace. &bTownTalk&r dává občanům hlasy.",
        ]),
        Q("camp", "Zásobovací tábor", dep=["intro"], items=[("minecolonies:supplycampdeployer", 1)], xp=30, d=[
            "Zásobovací tábor (&eSupply Camp&r) je startovní balíček kolonie.",
            "Vyrobíš ho z 5 truhel (do tvaru písmene U). Klikni s ním pravým tlačítkem na zem a umístění potvrď.",
            "Potřebuje rovné místo aspoň 16 × 17 bloků bez trávy, květin a děr. Když chceš začít u vody, vyrob místo něj zásobovací loď (&eSupply Ship&r) z 5 člunů a polož ji na moře nebo řeku.",
            "",
            "V táboře najdeš truhlu se zásobami, radnici a nástroj stavby. &cTábor nebo loď položíš jen jednou.&r",
        ]),
        Q("buildtool", "Nástroj stavby", dep=["camp"], items=[("structurize:sceptergold", 1)], xp=20, d=[
            "Nástroj stavby (&eBuild Tool&r) staví všechny budovy kolonie. Je v truhle tábora, další si vyrobíš ze 2 tyček a 1 kamení (šikmo jako hůl).",
            "Každá budova má svůj blok (&eHut Block&r). Dej ho do inventáře, klikni nástrojem pravým tlačítkem na zem a vyber budovu. Šipkami ji posuň a otoč, fajfkou potvrď.",
            "&aTip:&r nástroj stavby je v receptu skoro každé budovy. Měj jich vždycky pár v zásobě.",
        ]),
        Q("townhall", "Radnice", dep=["buildtool"], items=[("minecolonies:blockhuttownhall", 1)], xp=40, d=[
            "Radnice (&eTown Hall&r) je srdce kolonie. Jedna je v truhle tábora, další se vyrábí z prken a 2 nástrojů stavby.",
            "Položením radnice kolonii založíš. Území kolem ní je chráněné, cizí hráči tam nemůžou kopat.",
            "V radnici přidáš kamarády do kolonie (karta „Oprávnění“ – &ePermissions&r).",
        ]),
        Q("found", "Založ kolonii", dep=["townhall"], icon="minecolonies:blockhuttownhall",
          tasks=[adv("minecolonies:minecolonies/place_townhall")], xp=40, shape="hexagon", size=1.5, s="Začátečník", d=[
            "Polož radnici nástrojem stavby. Tím vznikne tvoje kolonie a přijdou první 4 občané.",
            "Při pokládání si vybereš styl – podle něj budou vypadat všechny budovy. Pro začátečníky jsou určené styly &eColonial&r, &eMinecolonies Original&r a &eUrban Birch&r.",
            "Styl změníš i později: klikni na radnici a vpravo použij tlačítko u nápisu &eColony Pack&r.",
            "&cKaždý hráč může mít jen jednu kolonii.&r",
        ]),
        Q("eat", "Hladoví občané", dep=["found"], icon="minecraft:bread",
          tasks=[adv("minecolonies:minecolonies/citizen_eat_food_first")], xp=20, d=[
            "Občané musí jíst. Hladový občan pracuje pomalu a je nešťastný.",
            "Dokud nemáš jídelnu, krm je sám: klikni na občana pravým tlačítkem, otevři jeho inventář a dej mu jídlo (třeba chleba nebo pečené brambory).",
            "&cSyrové jídlo občané jíst nechtějí. Shnilé maso je jen nouzové řešení.&r",
        ]),
        Q("builder", "Stavitelova budova", dep=["found"], items=[("minecolonies:blockhutbuilder", 1)], xp=40, d=[
            "Stavitel je nejdůležitější občan. Staví a vylepšuje všechny ostatní budovy.",
            "Stavitelovu budovu (&eBuilder's Hut&r) vyrobíš z prken, dveří a nástroje stavby. Polož ji nástrojem stavby – najdeš ji v kategorii &eFundamentals&r.",
            "Je to jediná budova, kterou si stavitel postaví sám bez hotové chaty. Ostatní dělníci začnou pracovat, až je jejich budova aspoň na úrovni 1.",
        ]),
        Q("guide", "Nápověda v budově", dep=["builder"], optional=True, icon="minecraft:book",
          tasks=[adv("minecolonies:minecolonies/check_out_guide")], xp=10, d=[
            "Každá budova má vlastní nápovědu. Klikni pravým tlačítkem na stavitelovu budovu – otevře se průvodce. Přečti si ho a potvrď.",
            "Nápovědu najdeš v okně každé budovy. Stojí za to ji projít u každé nové budovy.",
        ]),
        Q("order", "První zakázka", dep=["builder"], icon="structurize:sceptergold",
          tasks=[adv("minecolonies:minecolonies/start_builder")], xp=25, d=[
            "Teď stavitelovi řekni, ať si budovu postaví.",
            "Klikni pravým tlačítkem na blok jeho budovy, otevři „Možnosti budovy“ (&eBuild Options&r) a klikni na „Postavit budovu“ (&eBuild Building&r).",
            "Stejně zadáš stavbu, vylepšení nebo opravu každé budovy. Stavitel si zakázky bere postupně.",
        ]),
        Q("fulfill", "Dodej materiál", dep=["order"], icon="minecraft:chest",
          tasks=[adv("minecolonies:minecolonies/fulfill_request")], xp=30, d=[
            "Stavitel nic nevyrábí z ničeho. Materiál mu musíš donést ty.",
            "Na kartě „Požaduje suroviny“ (&eRequired Resources&r) v jeho budově vidíš, co ještě chybí. Věci vlož přímo tam, nebo do inventáře budovy (Shift + pravé tlačítko na blok).",
            "Když stavitel chce nástroj nebo jídlo, klikni na něj pravým tlačítkem, otevři požadavky a dej mu věc tlačítkem „Doplnit“ (&eFulfill&r).",
            "{@pagebreak}",
            "&cChyba začátečníka:&r stavitel s budovou úrovně 0 smí používat jen dřevěné a zlaté nástroje. Kamenné umí až s úrovní 1, železné s úrovní 2, diamantové s úrovní 3.",
            "&aTip:&r V seznamu surovin se občas objeví i vzduch nebo pěšina. Ty neřeš. Sleduj hlavně požadavky samotného stavitele.",
        ]),
        Q("resscroll", "Svitek zdrojů", dep=["order"], items=[("minecolonies:resourcescroll", 1)], xp=15, d=[
            "Svitek zdrojů (&eResource Scroll&r) nosíš s sebou. Ukazuje, co stavitel ještě potřebuje, takže nemusíš běhat k jeho budově.",
            "Vyrobíš ho z tyček, 2 kůží a nástroje stavby. Propojíš ho Shift + pravým tlačítkem na stavitelovu budovu.",
        ]),
        Q("clipboard", "Deska s požadavky", dep=["fulfill"], optional=True, items=[("minecolonies:clipboard", 1)], xp=15, d=[
            "Deska (&eClipboard&r) ukáže všechny požadavky všech občanů najednou.",
            "Vyrobíš ji z tyček, kůže a nástroje stavby. Propojíš ji Shift + pravým tlačítkem na radnici.",
            "&aTip:&r když kolonie stojí, mrkni na desku. Skoro vždycky někdo na něco čeká.",
        ]),
        Q("builder_done", "Stavitel má dům", dep=["fulfill"], icon="minecolonies:blockhutbuilder",
          tasks=[adv("minecolonies:minecolonies/build_builder")], xp=50, shape="hexagon", size=1.5, s="Začátečník", d=[
            "Stavitel dokončil svou budovu na úrovni 1. Kolonie opravdu začala!",
            "Pravidlo úrovní: stavitel postaví jen budovu do stejné úrovně, jakou má jeho budova. Na budovu úrovně 3 potřebuješ stavitelovu budovu úrovně 3.",
            "Co dál (v tomto pořadí): krčma (bydlení), dřevorubec (dřevo), farma a jídelna (jídlo), důl (kámen a rudy) a domy.",
        ]),
        Q("tavern", "Krčma", dep=["builder_done"], items=[("minecolonies:blockhuttavern", 1)], xp=40, d=[
            "Občané potřebují postele, jinak spí venku a nejsou v bezpečí. Krčma (&eTavern&r) má 4 místa na spaní.",
            "Vyrobíš ji z prken, sudu a nástroje stavby. &cV kolonii může být jen jedna krčma.&r",
            "Do krčmy chodí návštěvníci. Klikni na návštěvníka – řekne ti, co chce za to, že zůstane. Potřebuješ ale volnou postel. &cNěkterý návštěvník si věci vezme a uteče.&r",
        ]),
        Q("lumber", "Dřevorubec", dep=["builder_done"], items=[("minecolonies:blockhutlumberjack", 1)], xp=30, d=[
            "Dřevorubec (&eForester's Hut&r) kácí stromy a sází nové sazenice. Stavitel bude dřeva potřebovat hodně.",
            "Vyrobíš ho z prken, dřevěné sekery a nástroje stavby. Dřevorubec potřebuje sekeru.",
            "&aTip:&r stromy hledá až 150 bloků daleko. Kmen, pod kterým leží kamení, za strom nepovažuje – tak ochráníš své dřevěné stavby.",
        ]),
        Q("farmer", "Farma", dep=["builder_done"], items=[("minecolonies:blockhutfarmer", 1), ("minecolonies:blockhutfield", 1)], xp=40, d=[
            "Farmář pěstuje plodiny pro celou kolonii. Farmu (&eFarm&r) vyrobíš z prken, dřevěné motyky a nástroje stavby.",
            "Farmář potřebuje pole (&eField&r): balík slámy nebo dýně, kůže a tyčky. Polož ho blízko farmy na volné místo s vodou, nebo nech stavitele postavit hotové pole z nástroje stavby.",
            "Pravým tlačítkem na pole vyber, co se na něm má pěstovat. Farmář zvládne jedno pole za každou úroveň farmy.",
            "&cCukrovou třtinu, kaktus a bambus farmář nepěstuje – na to je plantáž.&r",
        ]),
        Q("fisher", "Rybář", dep=["builder_done"], items=[("minecolonies:blockhutfisherman", 1)], xp=30, d=[
            "Rybář chytá ryby a občas i poklady. Budovu (&eFisher's Hut&r) vyrobíš z prken, rybářského prutu a nástroje stavby.",
            "Potřebuje vodu aspoň 7 × 7 bloků a hlubokou aspoň 1 blok. Budova musí stát ve stejné výšce jako voda a nejvýš 10 bloků od ní.",
            "Rybář potřebuje rybářský prut.",
        ]),
        Q("miner", "Důl", dep=["builder_done"], items=[("minecolonies:blockhutminer", 1)], xp=40, d=[
            "Horník vykope pod kolonií šachtu a chodby a nosí kámen a rudy. Důl (&eMine&r) vyrobíš z prken, dřevěného krumpáče a nástroje stavby.",
            "Potřebuje krumpáč a lopatu, někdy i sekeru. Na stavbu šachty chce bloky, půlbloky, ploty, žebříky a pochodně.",
            "&aTip:&r když horník stojí nahoře a nic nedělá, chybí mu materiál. Podívej se do jeho požadavků.",
        ]),
        Q("houses", "Domy pro občany", dep=["tavern"], items=[("minecolonies:blockhutcitizen", 2)], xp=30, d=[
            "Rezidence (&eResidence&r) je dům pro občany. Vyrobíš ji z prken, pochodně a nástroje stavby.",
            "Každá úroveň domu přidá jedno místo, takže dům úrovně 5 ubytuje 5 občanů. Strážní v domech nebydlí, spí ve svých věžích.",
            "&cBez volné postele do kolonie nikdo nový nepřijde.&r",
        ]),
        Q("pop5", "Pátý občan", dep=["houses"], icon="minecraft:white_bed",
          tasks=[adv("minecolonies:minecolonies/colony_population_5")], xp=30, d=[
            "Noví občané přicházejí dvěma způsoby: najmeš návštěvníka v krčmě, nebo se narodí dítě.",
            "Dítě se narodí, když v kolonii bydlí muž a žena a někde je volná postel. Děti musí jíst a spát, aby vyrostly.",
        ]),
        Q("food", "Jídelna", dep=["farmer"], items=[("minecolonies:blockhutcook", 1)], xp=40, d=[
            "V jídelně (&eDining Hall&r) pracuje číšník. Na peci uvaří maso a brambory a rozdává jídlo hladovým občanům.",
            "Vyrobíš ji z prken, jablka a nástroje stavby. Dodej jí palivo (třeba uhlí) a jídlo a v nastavení zapni, co se má podávat (&eMenu&r).",
            "&aTip:&r Syrové jídlo občané nejedí. Kdo bydlí v lepším domě, chce i lepší jídlo – to uvaří šéfkuchař (kapitola &eŽivot občanů&r).",
        ]),
        Q("builder2", "Stavitel úrovně 2", dep=["houses", "food"], icon="minecolonies:blockhutbuilder",
          tasks=[adv("minecolonies:minecolonies/build_builder_2")], xp=60, shape="hexagon", size=1.5, s="Pokročilý", d=[
            "Teď už jen přežívání nestačí – kolonie musí růst. Vylepši stavitelovu budovu na úroveň 2.",
            "V „Možnosti budovy“ (&eBuild Options&r) klikni na „Vylepšit“ (&eUpgrade&r). Pak můžeš vylepšovat na úroveň 2 i ostatní budovy.",
            "Vyšší úroveň znamená rychlejší postup dělníků a lepší nástroje. Chceš stavět dvě věci naráz? Postav druhého stavitele.",
        ]),
        Q("goggles", "Stavitelovy brýle", dep=["builder_done"], optional=True, items=[("minecolonies:build_goggles", 1)], xp=20, d=[
            "Stavitelovy brýle (&eBuilder's Goggles&r) si nasaď na hlavu. Uvidíš náhled budov, které se v okolí mají stavět.",
            "Vyrobíš je ze zlatých nugetů, železného ingotu, tabulek skla, kůže a nástroje stavby. Náhled zapneš a vypneš klávesou v ovládání (&eToggle Goggles Preview&r).",
        ]),
        Q("pop10", "Osada", dep=["builder2"], icon="minecraft:white_bed",
          tasks=[adv("minecolonies:minecolonies/colony_population_10")], xp=40, d=[
            "Kolonie má 10 občanů. Víc občanů znamená víc dělníků a víc surovin.",
            "Každý nový občan potřebuje postel a jídlo. Stav domy dřív, než dojdou místa.",
        ]),
        Q("courier", "Kurýr", dep=["builder2"], items=[("minecolonies:blockhutdeliveryman", 1)], xp=40, d=[
            "Teď už nemusíš všechno nosit sám. Kurýr nosí věci mezi skladištěm a budovami.",
            "Kurýrovu budovu (&eCourier's Hut&r) vyrobíš z prken, kožených bot a nástroje stavby. Se železnými botami dostaneš 2 kusy.",
            "Kurýr s budovou úrovně 1 unese najednou 1 stoh věcí, s úrovní 2 dva stohy, s úrovní 3 čtyři a s úrovní 4 osm.",
        ]),
        Q("warehouse", "Skladiště", dep=["courier"], items=[("minecolonies:blockhutwarehouse", 1)], xp=60, d=[
            "Skladiště (&eWarehouse&r) je hlavní sklad kolonie. Vyrobíš ho z prken, truhly a nástroje stavby.",
            "Všechno, co dáš do skladiště, kurýři sami rozvezou tomu, kdo to potřebuje. Stavitel si tak materiál vezme sám.",
            "Postav ho doprostřed kolonie. &cV kolonii smí být jen jedno. Nepřidávej do něj vlastní truhly – kurýři je nevidí.&r",
            "&aTip:&r místa přidáš vylepšením budovy. Na úrovni 5 můžeš regály ještě zvětšit za smaragdový blok.",
        ]),
        Q("university", "Univerzita", dep=["warehouse"], items=[("minecolonies:blockhutuniversity", 1)], xp=80, shape="hexagon", size=1.5, s="Expert", d=[
            "Univerzita (&eUniversity&r) je brána k pokročilé kolonii. Výzkumníci v ní odemykají nové budovy a vylepšení.",
            "Vyrobíš ji z prken, 2 knih a nástroje stavby.",
            "Každý výzkum stojí předměty a čas. Vyšší úroveň univerzity odemkne další stupně výzkumu a víc výzkumníků.",
            "&cZrušený výzkum ti předměty nevrátí.&r Víc v kapitole &eVýzkum a obrana&r.",
        ]),
        Q("guards", "Strážní věž", dep=["builder_done"], items=[("minecolonies:blockhutguardtower", 1)], xp=40, d=[
            "V noci chodí monstra a občas přijdou nájezdníci. Strážní věž (&eGuard Tower&r) má jednoho strážného, který v ní i bydlí.",
            "Z prken, luku a nástroje stavby vyrobíš rovnou 2 věže. Strážný je rytíř (meč) nebo lučištník (luk) a potřebuje zbraň a zbroj.",
            "&aTip:&r strážní věže zvětšují území kolonie. Mimo území nové budovy nepostavíš.",
        ]),
        Q("hospital", "Nemocnice", dep=["university"], items=[("minecolonies:blockhuthospital", 1)], xp=40, d=[
            "Občané občas onemocní. Nemocnice (&eHospital&r) je vyléčí a ošetří zraněné.",
            "Nejdřív vyzkoumej na univerzitě &eStamina&r (stojí 1 mrkev). Blok budovy vyrobíš z prken, mrkve a nástroje stavby.",
            "Nemocní chtějí jako lék obyčejné suroviny, třeba mrkev nebo brambory. Splň jejich požadavky – nemoc snižuje spokojenost celé kolonie.",
        ]),
        Q("school", "Škola", dep=["university"], items=[("minecolonies:blockhutschool", 1)], xp=40, d=[
            "Ve škole (&eSchool&r) se učí děti. Vyrostou z nich chytřejší dělníci a jsou spokojenější.",
            "Výzkum &eHigher Learning&r stojí 3 knihy a potřebuješ domy s úrovněmi dohromady aspoň 3. Blok budovy vyrobíš z prken, 2 pírek a nástroje stavby.",
        ]),
        Q("sawmill", "Pila", dep=["lumber", "university"], items=[("minecolonies:blockhutsawmill", 1)], xp=40, d=[
            "Pila (&eSawmill&r) je první řemeslník. Vyrábí ze dřeva prkna, schody, dveře a další věci, které stavitel potřebuje.",
            "Výzkum &eWoodwork&r stojí 64 prken a dřevorubci musí mít dohromady úroveň aspoň 3. Blok budovy: 3 dřevěné sekery, prkna a nástroj stavby.",
            "Řemeslníkovi musíš recepty naučit v jeho budově. Víc v kapitole &eŘemeslníci&r.",
        ]),
        Q("stonemason", "Kameník", dep=["miner", "university"], items=[("minecolonies:blockhutstonemason", 1)], xp=30, d=[
            "Kameník (&eStonemason's Hut&r) vyrábí věci z kamene: kamenné cihly, schody, půlbloky a zdi.",
            "Výzkum &eStone Cake&r stojí 64 vytesaných kamenných cihel (&eChiseled Stone Bricks&r) a doly musí mít dohromady úroveň aspoň 3. Blok budovy: 3 kamenné cihly, prkna a nástroj stavby.",
        ]),
        Q("smith", "Kovář", dep=["miner", "university"], items=[("minecolonies:blockhutblacksmith", 1)], xp=40, d=[
            "Kovář (&eBlacksmith's Hut&r) vyrábí nástroje, zbraně a zbroj, takže je už nemusíš kovat sám.",
            "Výzkum &eHitting Iron!&r stojí kovadlinu a doly musí mít dohromady úroveň aspoň 3. Blok budovy: 3 železné ingoty, prkna a nástroj stavby.",
        ]),
        Q("barracks", "Kasárny", dep=["guards", "university"], items=[("minecolonies:blockhutbarracks", 1)], xp=60, d=[
            "Kasárny (&eBarracks&r) mají až 4 kasárenské věže a v každé až 5 strážných. To je až 20 strážných na malém místě.",
            "Výzkum &eTactic Training&r stojí 3 bloky železa a strážní věže musí mít dohromady úroveň aspoň 3. Blok budovy: prkna, blok železa a nástroj stavby.",
        ]),
    ],
)

# =====================================================================
#  MineColonies 2: Život občanů
# =====================================================================
COL_LIFE = dict(
    key="mc_life", group="build", title="Kolonie: Život občanů",
    subtitle="Bydlení, jídlo a spokojenost", icon="minecolonies:blockhutcitizen",
    quests=[
        Q("intro", "Spokojení občané", dep=["minecolonies:builder_done"], icon="minecraft:poppy", tasks=[auto()], xp=10, d=[
            "Spokojení občané pracují lépe. Spokojenost (&eHappiness&r) najdeš v radnici.",
            "Zvyšuje ji: bydlení (lepší dům = víc), práce, jídlo, spánek, strážní a přežitý nájezd bez mrtvých.",
            "Snižuje ji: nemoc, zranění, smrt občana, dělník bez nástrojů a nešťastní sousedé.",
            "{@pagebreak}",
            "V této kapitole postavíš lepší domy, kuchyni a zvířata a nakonec zvětšíš kolonii na desítky občanů.",
            "&aTip:&r úroveň dělníka nepřeroste úroveň jeho domu. Kdo bydlí špatně, přestane se zlepšovat.",
        ]),
        Q("home", "Dům, sladký dům", dep=["intro"], icon="minecolonies:blockhutcitizen",
          tasks=[adv("minecolonies:minecolonies/build_citizen")], xp=25, shape="hexagon", size=1.5, s="Začátečník", d=[
            "Postav aspoň jednu rezidenci na úrovni 1.",
            "Pak domy postupně vylepšuj. V domě vyšší úrovně bydlí víc lidí a jsou spokojenější.",
            "&aTip:&r v radnici je volba, která bezdomovce sama přidělí do volných domů.",
        ]),
        Q("tavern_built", "Krčma je otevřená", dep=["intro"], icon="minecolonies:blockhuttavern",
          tasks=[adv("minecolonies:minecolonies/build_tavern")], xp=25, d=[
            "Krčma je hotová. Teď do ní budou chodit návštěvníci.",
            "Návštěvník řekne, co chce za to, že se stane občanem. Podívej se na jeho dovednosti – někteří jsou výborní dělníci.",
            "&cKdyž návštěvník zemře, nějakou dobu pak žádní noví nepřijdou.&r",
        ]),
        Q("crops", "Nové plodiny", dep=["intro"], items=[("minecolonies:onion", 1), ("minecolonies:garlic", 1)], xp=20, d=[
            "MineColonies přidává plodiny jako cibule (&eOnion&r), česnek (&eGarlic&r), rajče, rýže nebo kukuřice. Potřebuješ je na lepší jídla.",
            "Semena získáš, když motykou rozbíjíš trávu, kapradí a keře.",
            "Dej je farmáři: na poli vyber novou plodinu a on ji bude pěstovat.",
            "&aTip:&r cibule, česnek a tvrdá pšenice padají v každé krajině. Jiné plodiny jen v určitém podnebí – třeba rýže ve vlhkém, zelí ve studeném.",
        ]),
        Q("kitchen", "Kuchyně šéfkuchaře", dep=["crops"], items=[("minecolonies:blockhutkitchen", 1)], xp=40, d=[
            "Kdo bydlí v lepším domě, chce i lepší jídlo. Šéfkuchař v kuchyni (&eChef's Kitchen&r) vaří speciální jídla.",
            "Blok budovy vyrobíš z prken, udírny a nástroje stavby.",
            "&aTip:&r jídla z MineColonies mají v popisku úroveň (1 až 3). Čím vyšší, tím spokojenější občané.",
        ]),
        Q("dish", "Hustá polévka", dep=["kitchen"], items=[("minecolonies:pottage", 1)], xp=25, d=[
            "Hustá polévka (&ePottage&r) je jedno ze speciálních jídel MineColonies. Můžeš si ji vyrobit i sám na pracovním stole.",
            "Recept: tvrdá pšenice (&eDurum Wheat&r), cibule, česnek, miska, brambora a mrkev.",
            "Když na jídlo najedeš myší, popisek ukáže jeho úroveň a kdo ho umí uvařit.",
        ]),
        Q("baker", "Pekárna", dep=["intro"], items=[("minecolonies:blockhutbaker", 1)], xp=30, d=[
            "Pekař (&eBakery&r) peče chleba, sušenky, dýňový koláč a dort. Pekař umí i speciální chleby.",
            "Blok budovy vyrobíš z prken, pšenice a nástroje stavby. V nastavení pekárny vybereš, co má péct.",
        ]),
        Q("herders1", "Kurník a kravín", dep=["intro"], items=[("minecolonies:blockhutchickenherder", 1), ("minecolonies:blockhutcowboy", 1)], xp=30, d=[
            "Pastevci chovají zvířata. Kurník (&eChicken Farmer's Hut&r) dává vejce, pírka a maso, kravín (&eCowhand's Hut&r) mléko, kůži a hovězí.",
            "Bloky budov: prkna, nástroj stavby a vajíčko (kurník) nebo syrový steak (kravín).",
            "&cPastevec začne pracovat, až mu přivedeš aspoň 2 zvířata.&r Potřebuje sekeru a krmení (slepicím semínka, kravám pšenici).",
        ]),
        Q("herders2", "Vepřín a ovčín", dep=["herders1"], items=[("minecolonies:blockhutswineherder", 1), ("minecolonies:blockhutshepherd", 1)], xp=30, d=[
            "Vepřín (&eSwineherd's Hut&r) dává vepřové, ovčín (&eShepherd's Hut&r) vlnu a skopové.",
            "Bloky budov: prkna, nástroj stavby a syrová kotleta (vepřín) nebo nůžky (ovčín).",
            "Prasata se krmí mrkví, ovce pšenicí. Ovčák potřebuje i nůžky. Na každou úroveň budovy chová pastevec 2 zvířata.",
        ]),
        Q("all_herders", "Celá farma zvířat", dep=["herders2"], optional=True, icon="minecolonies:blockhutrabbithutch",
          tasks=[adv("minecolonies:production/build_all_herders")], xp=40, d=[
            "Postav všech pět pastevců: kurník, kravín, vepřín, ovčín a k tomu králíkárnu (&eRabbit Hutch&r).",
            "Králíkárna se vyrábí z prken, syrového králíka a nástroje stavby.",
        ]),
        Q("pop25", "Vesnička", dep=["home", "kitchen"], icon="minecraft:white_bed",
          tasks=[adv("minecolonies:minecolonies/colony_population_25")], xp=60, shape="hexagon", size=1.5, s="Pokročilý", d=[
            "Kolonie má 25 občanů! Teď už nejde o přežití, ale o to, aby byli všichni spokojení.",
            "Hlídej jídlo, nemoci a bydlení. Nešťastný soused kazí náladu i ostatním.",
        ]),
        Q("composter", "Kompostárna", dep=["pop25", "minecolonies:university"], items=[("minecolonies:blockhutcomposter", 1)], xp=40, d=[
            "Kompostér (&eComposter's Hut&r) dělá z odpadu (listí, sazenice, jídlo) kompost. Kompost potřebuje farmář a květinářka.",
            "Výzkum &eBiodegradable&r stojí 64 kostní moučky a farmy musí mít dohromady úroveň 3.",
            "Blok budovy potřebuje kompostovací sud (&eCompost Barrel&r) z prken, hlíny, železného ingotu a nástroje stavby.",
            "&cV nastavení vyber, co kompostovat. S jídlem opatrně, ať občanům nezbude hlad.&r",
        ]),
        Q("plantation", "Plantáž", dep=["composter"], items=[("minecolonies:blockhutplantation", 1), ("minecolonies:blockhutplantationfield", 1)], xp=40, d=[
            "Plantážník pěstuje cukrovou třtinu, kaktusy a bambus – to, co farmář neumí.",
            "Výzkum &eLet It Grow&r stojí 16 kompostu a farmy musí mít dohromady úroveň 3. Plantáž (&ePlantation&r) vyrobíš z prken, kaktusu a nástroje stavby.",
            "Plantážní pole (&ePlantation Field&r) z tyček, železného ingotu, prken a nástroje stavby označí, kde má pracovat.",
        ]),
        Q("florist", "Květinářství", dep=["composter"], optional=True, items=[("minecolonies:blockhutflorist", 1)], xp=30, d=[
            "Květinářka (&eFlower Shop&r) pěstuje květiny pomocí kompostu.",
            "Výzkum &eFlower Power&r stojí 64 kompostu a kompostárny musí mít dohromady úroveň 3. Blok budovy: prkna, vlčí mák a nástroj stavby.",
        ]),
        Q("beekeeper", "Včelín", dep=["pop25"], optional=True, items=[("minecolonies:blockhutbeekeeper", 1)], xp=30, d=[
            "Včelař (&eApiary&r) se stará o včely a úly a sbírá med.",
            "Blok budovy vyrobíš z prken, včelího úlu a nástroje stavby.",
            "Úly mu přiřadíš nástrojem na úly (&eHive Tool&r), který dostaneš v jeho budově.",
        ]),
        Q("library", "Knihovna", dep=["pop25", "minecolonies:university"], items=[("minecolonies:blockhutlibrary", 1)], xp=40, d=[
            "V knihovně (&eLibrary&r) se dospělí učí. Roste jim inteligence, a díky ní se rychleji zlepšují v práci.",
            "Výzkum &eKeen&r stojí 3 knihy a domy musí mít dohromady úroveň 3. Blok budovy: prkna, kniha a nástroj stavby.",
        ]),
        Q("graveyard", "Hřbitov", dep=["pop25", "minecolonies:university"], items=[("minecolonies:blockhutgraveyard", 1)], xp=40, d=[
            "Když občan zemře, zůstane po něm hrob. Hrobník na hřbitově (&eGraveyard&r) hroby sbírá, takže kolonie truchlí kratší dobu.",
            "Výzkum &eRemembrance&r stojí 8 kostí a radnice musí mít úroveň 2. Blok budovy: kámen, kost a nástroj stavby.",
            "&aTip:&r hrobník může mrtvého občana i oživit. Šanci zvýší vyšší úroveň hřbitova, mystické místo a výzkum.",
        ]),
        Q("mystical", "Mystické místo", dep=["library"], items=[("minecolonies:blockhutmysticalsite", 1)], xp=50, d=[
            "Mystické místo (&eMystical Site&r) nemá dělníka. Je to krásná stavba, na kterou jsou občané pyšní – zvyšuje spokojenost podle své úrovně.",
            "Výzkum &eAmbition&r stojí 1 diamant. Blok budovy: prkna, diamant a nástroj stavby.",
        ]),
        Q("mystical5", "Divy světa", dep=["mystical"], optional=True, icon="minecolonies:blockhutmysticalsite",
          tasks=[adv("minecolonies:minecolonies/build_mysticalsite_5")], xp=80, d=[
            "Vylepši mystické místo na úroveň 5. Je to drahá stavba, ale spokojenost kolonie vyskočí nahoru.",
        ]),
        Q("max_fields", "Zelené prsty", dep=["plantation"], optional=True, icon="minecolonies:blockhutfield",
          tasks=[adv("minecolonies:production/max_fields")], xp=50, d=[
            "Přiřaď jednomu farmáři největší možný počet polí. Farmář zvládne jedno pole za každou úroveň farmy, tedy až 5 polí.",
        ]),
        Q("pop50", "Město", dep=["pop25", "library"], icon="minecolonies:blockhuttownhall",
          tasks=[adv("minecolonies:minecolonies/colony_population_50")], xp=100, shape="hexagon", size=1.5, s="Expert", d=[
            "50 občanů! Z vesnice je opravdové město.",
            "Teď se vyplatí vylepšovat budovy na úroveň 5 a dělat výzkumy, které zrychlují práci.",
        ]),
        Q("townhall5", "Mistrovská radnice", dep=["pop50"], optional=True, icon="minecolonies:blockhuttownhall",
          tasks=[adv("minecolonies:minecolonies/build_town_hall_5")], xp=80, d=[
            "Vylepši radnici na úroveň 5. Bude to chlouba celé kolonie.",
        ]),
        Q("pop75", "Velkoměsto", dep=["pop50"], optional=True, icon="minecolonies:blockhuttownhall",
          tasks=[adv("minecolonies:minecolonies/colony_population_75")], xp=100, d=[
            "75 občanů. Usadil ses, přežil a vybudoval jsi opravdové město.",
        ]),
    ],
)

# =====================================================================
#  MineColonies 3: Řemeslníci a výroba
# =====================================================================
COL_CRAFT = dict(
    key="mc_crafters", group="build", title="Kolonie: Řemeslníci",
    subtitle="Ať kolonie vyrábí sama", icon="minecolonies:blockhutsawmill",
    quests=[
        Q("intro", "Jak pracují řemeslníci", dep=["minecolonies:warehouse"], icon="minecolonies:blockhutsawmill", tasks=[auto()], xp=10, d=[
            "Řemeslník (pila, kameník, kovář…) vyrábí věci pro ostatní občany. Teď už nemusíš vyrábět každý schod sám.",
            "Pozor: řemeslník nic nevyrábí do zásoby. Pracuje, jen když jiný dělník (třeba stavitel) o věc požádá.",
            "Recepty mu musíš naučit: v jeho budově otevři „Naučit recept“ (&eTeach Recipe&r) a poskládej recept jako na pracovním stole.",
            "{@pagebreak}",
            "&cBez skladiště a kurýra řemeslníci nefungují – kurýr jim nosí suroviny.&r",
            "&aTip:&r šikovný řemeslník občas recept vylepší a spotřebuje méně surovin.",
        ]),
        Q("torch", "Stavitel umí pochodně", dep=["intro"], icon="minecraft:torch",
          tasks=[adv("minecolonies:minecolonies/building_add_recipe_torch")], xp=20, d=[
            "I stavitel umí vyrábět jednoduché recepty 2 × 2. Nauč ho recept na pochodeň a bude si je dělat sám.",
            "V jeho budově otevři učení receptů a vlož uhlí nad tyčku.",
        ]),
        Q("door", "Pila vyrábí dveře", dep=["intro", "minecolonies:sawmill"], icon="minecraft:oak_door",
          tasks=[adv("minecolonies:minecolonies/building_add_recipe_door")], xp=25, shape="hexagon", size=1.5, s="Začátečník", d=[
            "Nauč pilu recept na dveře. Pila umí recepty 3 × 3 ze dřeva.",
            "Až bude stavitel chtít dveře, pila je sama vyrobí a kurýr je donese.",
            "Vylepšená pila má víc míst na recepty.",
        ]),
        Q("post", "Pošta a skrýš", dep=["intro"], items=[("minecolonies:blockpostbox", 1), ("minecolonies:blockstash", 1)], xp=30, d=[
            "Poštovní schránka (&ePostbox&r): objednáš si v ní věci ze skladiště a kurýr ti je přinese.",
            "Skrýš (&eStash&r): co do ní vložíš, kurýr odnese do skladiště.",
            "Obě vyrobíš z prken, truhel a nástroje stavby. Hodí se k tvému domu nebo dolu.",
        ]),
        Q("smeltery", "Tavírna", dep=["intro", "minecolonies:university"], items=[("minecolonies:blockhutsmeltery", 1)], xp=40, d=[
            "Tavič v tavírně (&eSmeltery&r) taví rudy na ingoty.",
            "Výzkum &eHot!&r stojí 4 kbelíky lávy a doly musí mít dohromady úroveň 2. Blok budovy: prkna, železný ingot a nástroj stavby.",
            "Tavírna úrovně 3 dává z rudných bloků víc jako štěstí II, úroveň 5 jako štěstí IV.",
        ]),
        Q("stonesmeltery", "Cihelna", dep=["intro", "minecolonies:stonemason"], items=[("minecolonies:blockhutstonesmeltery", 1)], xp=40, d=[
            "Cihelna (&eBrick yard&r) vypaluje v peci kamenné bloky (třeba hladký kámen) a dělá dřevěné uhlí pro ostatní řemeslníky.",
            "Výzkum &eThe Flintstones&r stojí 64 cihel a potřebuje kameníka úrovně 1. Blok budovy: prkna, pec, kamenné cihly a nástroj stavby.",
        ]),
        Q("crusher", "Drtič", dep=["intro", "minecolonies:stonemason"], items=[("minecolonies:blockhutcrusher", 1)], xp=40, d=[
            "Drtič (&eCrusher&r) drtí kamení na štěrk, štěrk na písek a písek na jíl.",
            "Výzkum &eRocking Roll&r stojí 64 kamene a potřebuje kameníka úrovně 1. Blok budovy: prkna, kamení, železný ingot a nástroj stavby.",
        ]),
        Q("sifter", "Třídič", dep=["intro", "minecolonies:fisher", "minecolonies:sawmill"], items=[("minecolonies:blockhutsifter", 1)], xp=40, d=[
            "Třídič (&eSifter&r) prosívá hlínu, štěrk, písek a duší písek a najde v nich užitečné věci, třeba rudy a drahokamy.",
            "Výzkum &eSieving&r (po výzkumu &eWoodwork&r) stojí 64 vláken a rybáři musí mít dohromady úroveň 3. Blok budovy: prkna, 3 vlákna a nástroj stavby.",
            "Třídič potřebuje síto (&eMesh&r). Nejdřív síto z vláken, lepší síta se odemknou s vyšší úrovní třídiče.",
        ]),
        Q("fletcher", "Výrobce šípů", dep=["door"], items=[("minecolonies:blockhutfletcher", 1)], xp=30, d=[
            "Výrobce šípů (&eFletcher's Hut&r) vyrábí věci z vlny, vlákna a kůže, třeba postele a koberce.",
            "Výzkum &eStringwork&r stojí 16 vláken a potřebuje pilu úrovně 1. Blok budovy: prkna, vlákno a nástroj stavby.",
        ]),
        Q("glassblower", "Sklářství", dep=["smeltery"], items=[("minecolonies:blockhutglassblower", 1)], xp=40, d=[
            "Sklář (&eGlassblower's Hut&r) taví písek na sklo a vyrábí tabulky a další skleněné věci.",
            "Výzkum &eThose Lungs!&r stojí 64 skla a tavírny musí mít dohromady úroveň 3. Blok budovy: prkna, sklo a nástroj stavby.",
        ]),
        Q("dyer", "Barvířství", dep=["intro", "mc_life:composter"], optional=True, items=[("minecolonies:blockhutdyer", 1)], xp=30, d=[
            "Barvíř (&eDyer's Hut&r) vyrábí barviva a barví vlnu, sklo a další bloky.",
            "Výzkum &eRainbow Heaven&r stojí 64 vlčích máků a kompostárny musí mít dohromady úroveň 3. Blok budovy: prkna, červené barvivo a nástroj stavby.",
        ]),
        Q("mechanic", "Mechanik", dep=["intro", "minecolonies:smith"], items=[("minecolonies:blockhutmechanic", 1)], xp=50, shape="hexagon", size=1.5, s="Pokročilý", d=[
            "Mechanik (&eMechanic's Hut&r) vyrábí věci z redstonu a to, co ostatní řemeslníci neumí.",
            "Výzkum &eWhat ya Need?&r stojí 64 redstonového prachu a kováři musí mít dohromady úroveň 3. Blok budovy: prkna, redstonový blok a nástroj stavby.",
            "S mechanikem kolonie vyrobí skoro všechno, co stavby potřebují.",
        ]),
        Q("concrete", "Betonárna", dep=["crusher"], optional=True, items=[("minecolonies:blockhutconcretemixer", 1)], xp=30, d=[
            "Betonář (&eConcrete Mixer's Hut&r) vyrábí betonový prášek i hotový beton.",
            "Výzkum &ePave the Road&r stojí 32 betonu a potřebuje drtič úrovně 1. Blok budovy: prkna, bílý betonový prášek a nástroj stavby.",
        ]),
        Q("enchanter", "Věž zaklínače", dep=["intro"], items=[("minecolonies:blockhutenchanter", 1)], xp=50, d=[
            "Zaklínač (&eEnchanter's Tower&r) sbírá zkušenosti ostatních občanů a vyrábí očarované knihy a kouzelné svitky.",
            "Blok budovy vyrobíš z prken, oltáře očarování a nástroje stavby. Zaklínač potřebuje mytické knihy (&eAncient Tome&r), které padají z nájezdníků.",
        ]),
        Q("quarry", "Lom", dep=["intro"], optional=True, items=[("minecolonies:simplequarry", 1)], xp=40, d=[
            "Lom (&eSimple Quarry&r) je velká jáma, kterou vykope lomař. Je to bezpečnější než důl, ale dává hlavně obyčejný kámen.",
            "Vyrobíš ho z prken, sudu, železného krumpáče a nástroje stavby. Pak v dole najmi lomaře a přiřaď ho k lomu.",
            "Větší lom (&eMedium Quarry&r) se vyrábí s diamantovým krumpáčem.",
        ]),
        Q("deep_mine", "Až na dno", dep=["intro"], optional=True, icon="minecraft:iron_pickaxe",
          tasks=[adv("minecolonies:production/deep_mine")], xp=50, d=[
            "Nech horníka vykopat šachtu až na podloží.",
            "Důl úrovně 1 začne kopat chodby pod výškou 50, úrovně 2 pod výškou 30 a úrovně 3 pod výškou 5.",
        ]),
        Q("netherworker", "Netherový důl", dep=["enchanter", "mechanic", "mc_defense:raid"], items=[("minecolonies:blockhutnetherworker", 1)], xp=80, shape="hexagon", size=1.5, s="Expert", d=[
            "Netherový horník (&eNether Mine&r) chodí na výpravy do Netheru a nosí odtamtud suroviny. Je to nebezpečná práce.",
            "Nejdřív výzkum &eMore Scrolls&r (věž zaklínače úrovně 3, 64 papíru, 1 mytická kniha, 64 lapisu), pak &eOpen the Nether&r (3 pozlacené černé kameny – &eGilded Blackstone&r).",
            "Blok budovy vyrobíš z prken, obsidiánu a nástroje stavby.",
        ]),
        Q("alchemist", "Alchymista", dep=["netherworker"], optional=True, items=[("minecolonies:blockhutalchemist", 1)], xp=60, d=[
            "Alchymista (&eAlchemist Tower&r) vaří lektvary a pěstuje bradavičník a jmelí.",
            "Výzkum &eMagic Potions&r (po &eOpen the Nether&r) stojí 16 bradavičníků. Blok budovy: prkna, varný stojan a nástroj stavby.",
        ]),
    ],
)

# =====================================================================
#  MineColonies 4: Výzkum a obrana
# =====================================================================
COL_DEF = dict(
    key="mc_defense", group="build", title="Kolonie: Výzkum a obrana",
    subtitle="Stráže, nájezdy a univerzita", icon="minecolonies:blockhutguardtower",
    quests=[
        Q("intro", "Ochrana kolonie", dep=["minecolonies:guards"], icon="minecolonies:blockhutguardtower", tasks=[auto()], xp=10, d=[
            "Kolonii ohrožují monstra a nájezdníci. Občané se sami neubrání – potřebují strážné.",
            "Nájezdy přicházejí v noci. Kolonii napadnou barbaři, piráti, seveřané, amazonky nebo mumie – podle okolí.",
            "Piráti a seveřané připlouvají na lodi. &cDokud loď nezničíš, útočí dál.&r",
            "{@pagebreak}",
            "V této kapitole postavíš obranu od první věže po kasárny a výcvik a k tomu se naučíš výzkum na univerzitě.",
            "&aTip:&r Osvětli kolonii pochodněmi. Méně monster = méně zraněných občanů.",
        ]),
        Q("first_guard", "První strážný", dep=["intro"], icon="minecolonies:blockhutguardtower",
          tasks=[adv("minecolonies:minecolonies/build_guard_tower")], xp=30, shape="hexagon", size=1.5, s="Začátečník", d=[
            "Postav strážní věž na úrovni 1 a strážný se do ní nastěhuje.",
            "Dej mu zbraň a zbroj. Lepší výbavu si řekne až s vyšší úrovní věže (kámen na úrovni 1, železo na 2, diamant na 3).",
            "&aTip:&r novou výbavu chce strážný až ve chvíli, kdy tu starou opotřebuje.",
        ]),
        Q("research", "Jak funguje výzkum", dep=["intro", "minecolonies:university"], icon="minecolonies:blockhutuniversity", items=[("minecraft:book", 3)], xp=20, d=[
            "Výzkum se dělá na univerzitě. Má tři větve: &eCivilian&r (občané), &eCombat&r (boj) a &eTechnology&r (výroba).",
            "Každý výzkum stojí předměty a čas a má podmínky, třeba úroveň budovy. Výzkum dělají výzkumníci na univerzitě – bez nich se nepohne.",
            "Hodně výzkumů stojí knihy, proto si připrav aspoň 3 do zásoby.",
            "{@pagebreak}",
            "&cZrušený výzkum ti předměty nevrátí. Na nejvyšší úrovni (6) si v každé větvi vybereš jen jeden výzkum.&r",
        ]),
        Q("rally", "Shromažďovací prapor", dep=["first_guard"], optional=True, items=[("minecolonies:banner_rally_guards", 1)], xp=30, d=[
            "Shromažďovací prapor (&eRallying Banner&r) svolá strážné k tobě.",
            "Vyrobíš ho ze 3 železných mečů, 2 strážních věží, 3 luků a žlutého praporu.",
            "Shift + pravé tlačítko na strážní věž ji přidá do seznamu. Shift + pravé tlačítko do vzduchu strážné svolá nebo propustí.",
        ]),
        Q("army8", "Malá armáda", dep=["first_guard"], icon="minecraft:iron_sword",
          tasks=[adv("minecolonies:military/army_8")], xp=40, d=[
            "Měj v kolonii 8 strážných. Víc strážných = víc spokojenosti a větší šance při nájezdu.",
            "Strážní věže navíc zvětšují území kolonie. Když potřebuješ víc místa na budovy, postav a vylepši další věže.",
        ]),
        Q("raid", "Odraz nájezd", dep=["army8"], items=[("minecolonies:ancienttome", 1)], xp=60, d=[
            "Odraž nájezd a seber mytickou knihu (&eAncient Tome&r). Padá z nájezdníků.",
            "Když přijde zpráva o nájezdu, připrav se: vezmi zbraň a pomoz strážným.",
            "Kolonie, která nájezd přežije bez mrtvých občanů, je spokojenější. Mytickou knihu potřebuje zaklínač a výzkum.",
        ]),
        Q("barracks_built", "Kasárny stojí", dep=["army8", "minecolonies:barracks"], icon="minecolonies:blockhutbarracks",
          tasks=[adv("minecolonies:military/build_barracks")], xp=50, shape="hexagon", size=1.5, s="Pokročilý", d=[
            "Teď už jednotlivé věže nestačí. Postav kasárny na úrovni 1.",
            "Za každou úroveň kasáren můžeš postavit jednu kasárenskou věž. Věž nemůže mít vyšší úroveň než kasárny.",
            "&aTip:&r v kasárnách můžeš během nájezdu najmout špehy. Za zlato ti prozradí, kde jsou nepřátelé.",
        ]),
        Q("barracks_tower", "Kasárenská věž", dep=["barracks_built"], icon="minecolonies:blockhutbarrackstower",
          tasks=[adv("minecolonies:military/build_barracks_tower")], xp=40, d=[
            "Postav první kasárenskou věž (&eBarracks Tower&r). Každá úroveň věže přidá jednoho strážného, až 5 na věž.",
            "Strážní bydlí přímo ve věži, takže nezabírají postele v domech.",
        ]),
        Q("combat_academy", "Bojová akademie", dep=["barracks_tower"], items=[("minecolonies:blockhutcombatacademy", 1)], xp=50, d=[
            "V bojové akademii (&eCombat Academy&r) se občan cvičí na rytíře bez rizika, že zemře.",
            "Výzkum &eImproved Swords&r stojí 6 bloků železa a kasárny musí mít úroveň 3. Blok budovy: prkna, 3 železné meče a nástroj stavby.",
        ]),
        Q("archery", "Lukostřelnice", dep=["barracks_tower"], items=[("minecolonies:blockhutarchery", 1)], xp=50, d=[
            "Na lukostřelnici (&eArchery&r) se občan cvičí na lučištníka.",
            "Výzkum &eImproved Bows&r stojí 6 bloků železa a kasárny musí mít úroveň 3. Blok budovy: prkna, 3 luky a nástroj stavby.",
        ]),
        Q("stable", "Stáj", dep=["barracks_tower"], optional=True, items=[("minecolonies:blockhutstable", 1)], xp=40, d=[
            "Ve stáji (&eStable&r) se chovají koně pro jezdce. Jízdní strážný je rychlý a odolný.",
            "Výzkum &eMounted Combat&r stojí sedlo a vodítko. Blok budovy: prkna, zlaté jablko a nástroj stavby.",
        ]),
        Q("gatehouse", "Strážnice u brány", dep=["first_guard"], optional=True, items=[("minecolonies:blockhutgatehouse", 1)], xp=30, d=[
            "Strážnice (&eGatehouse&r) ubytuje 2 strážné. Umí také propojit tvou kolonii s jinou kolonií.",
            "Blok budovy vyrobíš z prken, železného meče, luku a nástroje stavby.",
        ]),
        Q("army30", "Poručík", dep=["combat_academy", "archery"], icon="minecolonies:blockhutbarracks",
          tasks=[adv("minecolonies:military/army_30")], xp=80, shape="hexagon", size=1.5, s="Expert", d=[
            "Měj v kolonii 30 strážných. Taková armáda zvládne i velké nájezdy.",
            "Vylepšuj kasárny i věže na úroveň 5 a dělej bojové výzkumy ve větvi &eCombat&r.",
        ]),
        Q("all_towers", "Velká posádka", dep=["army30"], optional=True, icon="minecolonies:blockhutbarrackstower",
          tasks=[adv("minecolonies:military/build_all_barracks_towers")], xp=80, d=[
            "Kasárny na plné úrovni se všemi věžemi. To je až 20 strážných na jednom místě.",
        ]),
        Q("army80", "Centurion", dep=["army30"], optional=True, icon="minecraft:netherite_sword",
          tasks=[adv("minecolonies:military/army_80")], xp=100, d=[
            "Armáda o 80 strážných. Žádný nájezdník už nemá šanci.",
        ]),
    ],
)

# =====================================================================
#  MineColonies 5: Nástroje a styly (Structurize, styly, doplňky)
# =====================================================================
COL_TOOLS = dict(
    key="mc_tools", group="build", title="Kolonie: Nástroje a styly",
    subtitle="Structurize, styly budov a užitečné pomůcky", icon="structurize:sceptergold",
    quests=[
        Q("intro", "Nástroje stavitele", dep=["minecolonies:found"], icon="structurize:sceptergold", tasks=[auto()], xp=10, d=[
            "&bStructurize&r je mod, na kterém stojí nástroj stavby. Přidává i další nástroje pro stavitele.",
            "Vzhled budov určují styly. Kromě stylů z MineColonies jsou v packu doplňky &bStylecolonies&r, &bByzantine&r a &bChristmasColonies&r.",
            "V této kapitole poznáš styly, deník úkolů, mapu kolonie a nástroje na měření, skenování a tvary.",
        ]),
        Q("style", "Radnice ve tvém stylu", dep=["intro"], icon="minecolonies:blockhuttownhall",
          tasks=[adv("minecolonies:minecolonies/build_town_hall")], xp=40, shape="hexagon", size=1.5, s="Začátečník", d=[
            "Nech stavitele postavit radnici na úrovni 1. Bude vypadat podle stylu, který sis vybral.",
            "&bStylecolonies&r přidává styly jako &eSteampunk&r, &eFairyTale&r, &eFrontier&r, &eAntique&r, &eTropical&r nebo &eCrimson Keep&r.",
            "&bByzantine&r přidává &eByzantine&r, &eNile&r a &eShogun&r, &bChristmasColonies&r zase vánoční &eChristmas Style&r a obří vánoční strom.",
            "{@pagebreak}",
            "&cNěkteré styly potřebují zvláštní místo: &eTropical&r mělkou vodu, &eAquatica&r a &eUnderwater Base&r hluboký oceán. Než začneš, přečti si popis stylu.&r",
            "&aTip:&r pokročilé styly (&eSpace Wars&r, &eFortress&r) jsou náročné na suroviny. Na začátek vyber styl označený &e[Beginner]&r.",
        ]),
        Q("questlog", "Úkoly od občanů", dep=["intro"], items=[("minecolonies:questlog", 1)], xp=20, d=[
            "Občané ti občas dají vlastní úkol. Deník úkolů (&eQuest Log&r) ukáže rozdělané, dostupné i hotové úkoly.",
            "Vyrobíš ho z tyček, kůže, papíru a nástroje stavby. Propoj ho Shift + pravým tlačítkem na radnici.",
            "Úkoly od občanů provedou i celým začátkem kolonie a dávají malé odměny.",
        ]),
        Q("colonymap", "Mapa kolonie", dep=["intro"], optional=True, items=[("minecolonies:colonymap", 1)], xp=20, d=[
            "Mapa kolonie (&eColony Map&r) otevře okno s mapou tvé kolonie.",
            "Vyrobíš ji z 8 prázdných map a nástroje stavby. Propoj ji Shift + pravým tlačítkem na radnici.",
        ]),
        Q("caliper", "Posuvné měřítko", dep=["intro"], optional=True, items=[("structurize:caliper", 1)], xp=15, d=[
            "Měřítko (&eCalipers&r) změří vzdálenost. Hodí se, když plánuješ, kam se vejde budova.",
            "Levým tlačítkem klikni na první blok, pravým na druhý. Pak klikni pravým tlačítkem do vzduchu a měřítko ukáže rozměry.",
        ]),
        Q("scan", "Skenovací nástroj", dep=["style"], items=[("structurize:sceptersteel", 1)], xp=30, shape="hexagon", size=1.5, s="Pokročilý", d=[
            "Skenovací nástroj (&eScan Tool&r) uloží stavbu do souboru. Vyrobíš ho ze 2 tyček a železného ingotu.",
            "Levým tlačítkem označ první roh, pravým druhý roh. Pak klikni pravým do vzduchu – otevře se okno, kde sken pojmenuješ a uložíš.",
            "Tlačítko &eShow Resources&r ukáže, z jakých bloků se stavba skládá a kolik jich je.",
            "&aTip:&r jestli ti stavitel smí postavit tvůj vlastní sken, záleží na nastavení serveru.",
        ]),
        Q("shape", "Nástroj na tvary", dep=["scan"], items=[("structurize:shapetool", 1)], xp=30, shape="hexagon", size=1.5, s="Expert", d=[
            "Nástroj na tvary (&eShape Tool&r) vytvoří kouli, válec, jehlan, kužel, vlnu a další tvary. Vyrobíš ho ze 2 tyček a smaragdu.",
            "Pravým tlačítkem otevřeš okno: vyber tvar, velikost, hlavní a výplňový blok a jestli má být dutý.",
            "Skvělé na kopule, věže a velké dekorace.",
        ]),
    ],
)

# =====================================================================
#  Stavění a dekorace (původní kapitola "building")
# =====================================================================
BUILDING = dict(
    key="building", group="build", title="Stavění a dekorace",
    subtitle="Bloky, střechy, okna a další ozdoby", icon="mcwroofs:oak_roof",
    quests=[
        Q("start", "Ráj stavitelů", icon="minecraft:bricks", tasks=[auto()], xp=10, d=[
            "V packu je obrovské množství dekorací. V této kapitole najdeš nástroje a stoly, které je zpřístupní.",
            "Většina bloků se vyrábí normálně na pracovním stole. Když nevíš, jak něco vyrobit, najdi to v JEI (klávesa R na předmětu).",
            "Začni stoly &bChipped&r a dlátem &bRechiseled&r, pak pokračuj na &bMacaw's&r střechy, okna a mosty. Nábytek má vlastní kapitolu.",
        ]),
        # ---- Chipped ----
        Q("chipped", "Stoly Chipped", dep=["start"], items=[("chipped:botanist_workbench", 1), ("chipped:mason_table", 1), ("chipped:carpenters_table", 1)], xp=20, shape="hexagon", size=1.5, s="Začátečník", d=[
            "&bChipped&r: pracovní stoly, které z jednoho bloku udělají desítky jiných vzhledů. Funguje to jako řezačka kamene.",
            "Do stolu vlož blok a vyber si nový vzhled. Každý stůl umí jiné bloky:",
            "Botanický (&eBotanist Workbench&r): hlína, listí, led, houby, dýně. Kamenický (&eMason Table&r): kámen, cihly, terakota, beton. Truhlářský (&eCarpenters Table&r): prkna, kmeny, dveře, poklopy.",
            "Všechny se vyrábí z pracovního stolu a surovin, které ke stolu patří (květináče, cihly, železná sekera…).",
        ]),
        Q("chipped_more", "Sklo, vlna a lampy", dep=["chipped"], items=[("chipped:glassblower", 1), ("chipped:loom_table", 1), ("chipped:tinkering_table", 1)], xp=25, d=[
            "Další tři stoly &bChipped&r:",
            "Sklářský (&eGlassblower&r): sklo a tabulky skla. Tkalcovský (&eLoom Table&r): vlna a koberce. Kutilský (&eTinkering Table&r): lucerny, redstonové lampy, mříže a redstonové pochodně.",
            "Sklářský potřebuje vysokou pec, tkalcovský vlnu a kutilský redstone.",
        ]),
        Q("chipped_tool", "Stůl do kapsy", dep=["chipped"], optional=True, items=[("chipped:chisel", 1)], xp=15, d=[
            "Kamenický stůl a železný ingot dají dláto (&eChisel&r) – kamenický stůl, který nosíš v inventáři. Klikni s ním pravým tlačítkem a otevře se stejné okno.",
            "Podobně vznikne pila (&eSaw&r) z truhlářského stolu a jehly (&eNeedles&r) z tkalcovského stolu.",
        ]),
        Q("chipped_alchemy", "Alchymistický stůl", dep=["chipped_more"], items=[("chipped:alchemy_bench", 1)], xp=40, d=[
            "Alchymistický stůl (&eAlchemy Bench&r) mění vzácné bloky: bloky diamantů, zlata, železa, smaragdů, mědi, ametystu nebo světlitu.",
            "Vyrobíš ho z pracovního stolu, varného stojanu, oltáře očarování a dřevěných půlbloků.",
        ]),
        # ---- Rechiseled ----
        Q("rechiseled", "Dláto Rechiseled", dep=["start"], items=[("rechiseled:chisel", 1)], xp=15, d=[
            "&bRechiseled&r: dláto (&eChisel&r) mění vzhled bloků. Vyrobíš ho ze železného ingotu a tyčky.",
            "Klikni s dlátem pravým tlačítkem, vlož blok a vyber nový vzhled. Tlačítko &eChisel all&r přetesá celý stoh najednou.",
            "Funguje na kámen, cihly, prkna, kovové bloky a další.",
        ]),
        Q("rechiseled_connect", "Spojité textury", dep=["rechiseled"], items=[("rechiseled:oak_planks_crate_connecting", 4)], xp=20, d=[
            "Některé bloky z dláta se umí spojit do jednoho velkého vzoru. V okně dláta zapni &eConnected textures: On&r.",
            "Vyrob 4 bloky &eOak Planks Crate&r se spojitou texturou a polož je vedle sebe – splynou v jednu velkou bednu.",
        ]),
        Q("rechiseled_create", "Strojní dláto", dep=["rechiseled", "create:casing"], items=[("rechiseledcreate:mechanical_chisel", 1)], xp=40, shape="hexagon", size=1.5, s="Expert", d=[
            "Strojní dláto (&eMechanical Chisel&r) je stroj pro &bCreate&r. Vyrobíš ho z andezitového pláště a dláta.",
            "Pracuje jako mechanická pila: roztoč ho, do filtru dej blok, jaký chceš dostat, a pošli do něj bloky (třeba po pásu). Přetesá je sám.",
        ]),
        # ---- Macaw's ----
        Q("macaw", "Okenní kladivo", dep=["start"], items=[("mcwwindows:hammer", 1)], xp=20, d=[
            "Mody &bMacaw's&r přidávají střechy, okna, dveře, ploty, mosty, světla, nábytek a sváteční dekorace ve všech druzích dřeva a kamene.",
            "Okenní kladivo (&eWindow Hammer&r) mění tvar položených oken &bMacaw's Windows&r. Klikni s ním pravým tlačítkem na okno.",
            "Vyrobíš ho ze železného ingotu, železného nugetu a 2 tyček.",
        ]),
        Q("mcw_windows", "Okna a závěsy", dep=["macaw"], items=[("mcwwindows:oak_window", 1), ("mcwwindows:white_curtain", 1)], xp=20, d=[
            "Dubové okno (&eResizeable Oak Window&r) vyrobíš ze základů okna (&eWindow Base&r: sklo obložené tyčkami) a dubového kmenu.",
            "Závěs (&eWhite Curtain&r) vyrobíš ze 2 bloků bílé vlny. Okno zamkneš klíčem (&eWindow Key&r).",
        ]),
        Q("mcw_roofs", "Střechy", dep=["start"], items=[("mcwroofs:oak_roof", 2), ("mcwroofs:roofing_hammer", 1)], xp=25, shape="hexagon", size=1.5, s="Pokročilý", d=[
            "&bMacaw's Roofs&r: šikmé střechy všech tvarů. Dřevěné (třeba &eOak Roof&r) vyrobíš z kmenů nebo prken a tyčky, kamenné a terakotové na řezačce kamene.",
            "Kladivo na střechy (&eRoofing Hammer&r) přepíná tvar vrcholu střechy. Klikni s ním pravým tlačítkem na horní díl.",
            "&aTip:&r každá střecha má díly: obyčejný, strmý, horní, dolní a podkrovní. Kombinuj je.",
        ]),
        Q("mcw_doors", "Dveře", dep=["start"], items=[("mcwdoors:oak_barn_door", 1), ("mcwdoors:oak_modern_door", 1)], xp=20, d=[
            "&bMacaw's Doors&r: stodolové, moderní, japonské, westernové a mnoho dalších dveří.",
            "Stodolové dveře (&eOak Barn Door&r) jsou z prken a tyček, moderní (&eOak Modern Door&r) z prken a tabulek skla.",
            "&cKovové dveře se otevírají jen redstonem.&r",
        ]),
        Q("mcw_bridges", "Mosty", dep=["start"], items=[("mcwbridges:rope_oak_bridge", 4), ("mcwbridges:pliers", 1)], xp=25, d=[
            "&bMacaw's Bridges&r: lanové, kamenné a kmenové mosty, schody a pilíře.",
            "Lanový most (&eRope Oak Bridge&r) vyrobíš z vláken a dubových půlbloků.",
            "Kleště (&ePliers&r) udělají v zábradlí vchod. Funguje to jen u mostu širokého aspoň 2 bloky.",
        ]),
        Q("mcw_fences", "Ploty a živé ploty", dep=["start"], items=[("mcwfences:oak_picket_fence", 1), ("mcwfences:oak_hedge", 1)], xp=20, d=[
            "&bMacaw's Fences and Walls&r: laťkové ploty, palisády, živé ploty, brány a zdi.",
            "Laťkový plot (&eOak Picket Fence&r) je z kmenů, prken a tyčky, živý plot (&eOak Hedge&r) ze 4 bloků listí.",
            "Některé ploty jdou stavět do výšky. &cDrátěný plot (&eWired Fence&c) zraňuje.&r",
        ]),
        Q("mcw_lights", "Světla a lampy", dep=["start"], items=[("mcwlights:classic_street_lamp", 1), ("mcwlights:oak_tiki_torch", 1)], xp=20, d=[
            "&bMacaw's Lights and Lamps&r: pouliční lampy, lustry, papírové lampy a tiki pochodně.",
            "Pouliční lampa (&eStreet Lamp Post&r) je z lucerny, dřevěného plotu a kamenné zídky. Tiki pochodeň (&eOak Tiki Torch&r) z pochodně a plotu.",
            "Tiki pochodeň jde stavět do výšky. Některé lampy přebarvíš kliknutím barvivem.",
        ]),
        Q("mcw_furniture", "Nábytek Macaw's", dep=["start"], items=[("mcwfurnitures:oak_desk", 1), ("mcwfurnitures:oak_wardrobe", 1)], xp=25, d=[
            "&bMacaw's Furniture&r: stoly, židle, skříně, šuplíky, kuchyňské linky a dřezy.",
            "Psací stůl (&eOak Desk&r) je z kmenů a plotů. Na skříň (&eOak Wardrobe&r) potřebuješ dvířka (&eCabinet Door&r) z tyček, truhly a železného nugetu.",
            "&aTip:&r skříně a šuplíky jsou zároveň úložné truhly.",
        ]),
        Q("mcw_holidays", "Sváteční dekorace", dep=["start"], optional=True, items=[("mcwholidays:christmas_tree_base", 1), ("mcwholidays:candy_cane", 1)], xp=15, d=[
            "&bMacaw's Holidays&r: vánoční stromky, girlandy a podzimní dekorace.",
            "Spodek vánočního stromku (&eChristmas Tree Base&r) je ze smrkového jehličí a smrkového kmenu. Cukrová hůlka (&eCandy Cane&r) z cukru.",
        ]),
        # ---- Decorative Blocks Reborn ----
        Q("dbr_beams", "Trámy a podpěry", dep=["start"], items=[("decorative_blocks:oak_beam", 2), ("decorative_blocks:oak_support", 1)], xp=20, d=[
            "&bDecorative Blocks Reborn&r: trámy, podpěry, palisády, sedátka, lustry a pánve s ohněm.",
            "Trám (&eOak Beam&r) vyrobíš z oloupaných kmenů, podpěru (&eOak Support&r) z prken.",
            "Sekerou klikni na podpěru – změníš velikost strany. Shift + sekera stranu skryje.",
        ]),
        Q("dbr_seat", "Sedátko", dep=["dbr_beams"], items=[("decorative_blocks:oak_seat", 1)], xp=15, d=[
            "Na sedátko (&eOak Seat&r) se dá posadit. Vyrobíš ho z půlbloku a plotu.",
            "Shift + pravé tlačítko do vzduchu přepne, jak bude vypadat.",
        ]),
        Q("dbr_fire", "Oheň a světlo", dep=["dbr_beams"], items=[("decorative_blocks:brazier", 1), ("decorative_blocks:chandelier", 1)], xp=20, d=[
            "Pánev s ohněm (&eBrazier&r) je ze železných mříží a uhlí. Lustr (&eChandelier&r) ze 4 pochodní.",
            "Skvěle se hodí do hradů a středověkých kolonií.",
        ]),
        # ---- Domum Ornamentum ----
        Q("domum", "Architektova řezačka", dep=["start"], items=[("domum_ornamentum:architectscutter", 1)], xp=20, d=[
            "&bDomum Ornamentum&r skládá dva bloky do jednoho: třeba hrázděnou zeď z prken a kamene. Používá ho mnoho stylů MineColonies.",
            "Řezačku (&eArchitect's Cutter&r) vyrobíš ze železného ingotu, kamenných půlbloků a kmenů.",
            "Vlož materiály a vyber tvar: hrázdění, šindele, dveře, poklopy, panely, sloupy, papírové stěny, světla, cihly nebo sloupky.",
        ]),
        Q("domum_blocks", "Létající koberec", dep=["domum"], optional=True, items=[("domum_ornamentum:white_floating_carpet", 3), ("domum_ornamentum:cream_bricks", 4)], xp=15, d=[
            "Některé bloky Domum Ornamentum se vyrábí na pracovním stole.",
            "Létající koberec (&eWhite Floating Carpet&r) ze 2 vln a vlákna visí ve vzduchu. Krémové cihly (&eCream Bricks&r) jsou z pískovce a cihel.",
        ]),
        # ---- Multi-Piston ----
        Q("multipiston", "Vícepíst", dep=["start"], items=[("multipiston:multipistonblock", 1)], xp=30, d=[
            "Vícepíst (&eMulti-Piston&r) posune bloky o víc políček než obyčejný píst. Hodí se na tajné dveře a mosty.",
            "Vyrobíš ho z kamene, 2 redstonových bloků a 3 pístů.",
            "Pravým tlačítkem nastavíš směr vstupu (&eInput&r), výstupu (&eOutput&r), dosah (&eRange&r) a rychlost (&eSpeed&r). Spouští se redstonem.",
        ]),
        # ---- Immersive Paintings ----
        Q("paintings", "Vlastní obrazy", dep=["start"], items=[("immersive_paintings:painting", 1)], xp=15, d=[
            "&bImmersive Paintings&r: nahraj jakýkoli obrázek a pověs ho na zeď.",
            "Obraz (&ePainting&r) vyrobíš z 8 papírů a barviva. Pověs ho a klikni na něj pravým tlačítkem: vlož obrázek (soubor nebo odkaz), nastav velikost a rám.",
            "Obrázky ostatních hráčů najdeš na kartě &ePlayers&r.",
        ]),
        Q("graffiti", "Graffiti", dep=["paintings"], items=[("immersive_paintings:graffiti", 1)], xp=15, d=[
            "Graffiti (&eGraffiti&r) je obrázek bez pozadí. Hodí se na obrázky s průhledností.",
            "Vyrobíš ho z barviv, střelného prachu a kbelíku (dostaneš 8 kusů).",
            "Se světélkujícím inkoustem uděláš svítící obraz (&eGlowing Painting&r) nebo svítící graffiti.",
        ]),
        # ---- původní questy z jiných modů ----
        Q("supp", "Supplementaries", dep=["start"], items=[("supplementaries:rope", 8), ("supplementaries:sack", 1), ("supplementaries:jar", 1)], xp=20, d=[
            "&bSupplementaries&r: spousta malých užitečných bloků – lana, pytle, sklenice, glóby, rozcestníky, podstavce…",
            "Lano (&eRope&r) je z vláken, pytel (&eSack&r) z pšenice a vlákna, sklenice (&eJar&r) ze skla a dřevěného půlbloku.",
            "Do pytle a sklenice se dají ukládat věci a vezmeš je s sebou i s obsahem.",
        ]),
        Q("createdeco", "Create Deco", dep=["start"], items=[("createdeco:industrial_iron_ingot", 4)], xp=15, d=[
            "&bCreate Deco&r: průmyslové dekorace – lampy, lávky, mříže a plechy.",
            "Hlavní materiál je průmyslové železo (&eIndustrial Iron Ingot&r). Blok průmyslového železa (&eBlock of Industrial Iron&r) vyrobíš ze železného ingotu na řezačce kamene. Blok pak na pracovním stole rozložíš na 9 ingotů.",
        ]),
        Q("etched", "Vlastní hudba", dep=["start"], items=[("etched:etching_table", 1)], xp=25, d=[
            "&bEtched&r: vypal si vlastní písničku na hudební desku a pusť ji všem na serveru.",
            "Rycí stůl (&eEtching Table&r) vyrobíš z diamantu, železného ingotu a prken.",
            "Potřebuješ prázdnou desku (&eBlank Music Disc&r – přetav libovolnou hudební desku) a štítek (&eMusic Label&r) z papíru. Do stolu vložíš odkaz na skladbu.",
        ]),
        # ---- nábytkové mody (originály, pokračují v kapitole Nábytek) ----
        Q("handcrafted", "Handcrafted", dep=["start"], items=[("handcrafted:hammer", 1)], xp=20, d=[
            "&bHandcrafted&r: nábytek ve všech druzích dřeva, na který si můžeš sednout nebo lehnout.",
            "Kladivo (&eHammer&r) ze železných ingotů a tyček mění vzhled a tvar skříněk, polic, pultů, šuplíků a lišt. Klikni s ním pravým tlačítkem na blok.",
            "Pokračuj v kapitole &eNábytek&r.",
        ]),
        Q("refurbished", "Furniture: Refurbished", dep=["start"], items=[("refurbished_furniture:workbench", 1)], xp=20, d=[
            "&bMrCrayfish's Furniture: Refurbished&r: nábytek, který opravdu funguje – lednice, sporáky, toustovače, televize, počítače i poštovní schránky.",
            "Skoro všechno se vyrábí na dílenském stole (&eWorkbench&r). Vyrobíš ho z řezačky kamene, redstonového bloku, železného ingotu, prken a dřevěných půlbloků.",
            "&cDílenský stůl potřebuje elektřinu.&r Jak ji získat, najdeš v kapitole &eNábytek&r.",
        ]),
    ],
)

# =====================================================================
#  Nábytek (Handcrafted, Another Furniture, Refurbished)
# =====================================================================
FURNITURE = dict(
    key="furniture", group="build", title="Nábytek",
    subtitle="Židle, kuchyně, elektřina a počítače", icon="handcrafted:oak_chair",
    quests=[
        Q("intro", "Zařiď si dům", dep=["building:start"], icon="handcrafted:oak_chair", tasks=[auto()], xp=10, d=[
            "V packu jsou tři velké nábytkové mody:",
            "&bHandcrafted&r – útulný nábytek, polštáře a trofeje. &bAnother Furniture&r – židle, závěsy, lampy a truhlíky. &bRefurbished Furniture&r – kuchyně a elektronika, která opravdu funguje.",
            "Na židle, lavice a pohovky si sedneš pravým tlačítkem. Začni jednoduchými židlemi, nakonec postavíš kuchyni s elektřinou a počítač.",
        ]),
        # ---- Handcrafted ----
        Q("hc_chair", "Židle", dep=["intro", "building:handcrafted"], items=[("handcrafted:oak_chair", 1)], xp=15, shape="hexagon", size=1.5, s="Začátečník", d=[
            "Dubová židle (&eOak Chair&r) z &bHandcrafted&r je z prken, půlbloku a tyček. Klikni na ni pravým tlačítkem a sedneš si.",
            "Stejně se vyrábí lavice, jídelní lavice, noční stolky a psací stoly ve všech druzích dřeva.",
        ]),
        Q("hc_cushion", "Polštáře a povlečení", dep=["hc_chair"], items=[("handcrafted:white_cushion", 1), ("handcrafted:white_sheet", 1)], xp=15, d=[
            "Polštář (&eWhite Cushion&r) je z vlny a pírek, povlečení (&eWhite Sheet&r) ze 3 vln. Přebarvíš je barvivem.",
            "Kliknutím polštářem nebo povlečením na nábytek změníš jeho vzhled, třeba barvu sedáku nebo ubrusu.",
        ]),
        Q("hc_couch", "Pohovka", dep=["hc_cushion"], items=[("handcrafted:oak_couch", 1)], xp=20, d=[
            "Pohovka (&eOak Couch&r) je z prken, vlny a polštáře. Polož víc pohovek vedle sebe a vznikne dlouhá sedačka.",
        ]),
        Q("hc_bed", "Luxusní postel", dep=["hc_cushion"], items=[("handcrafted:oak_fancy_bed", 1)], xp=20, d=[
            "Luxusní postel (&eOak Fancy Bed&r) je z prken, vlny, polštáře a povlečení. Spí se v ní jako v normální posteli.",
            "Polštářem na ni klikneš a změníš barvu polštáře, povlečením změníš prostěradlo.",
        ]),
        Q("hc_kitchen", "Kuchyňská linka", dep=["hc_chair"], items=[("handcrafted:oak_counter", 1), ("handcrafted:oak_cupboard", 1)], xp=20, d=[
            "Pult (&eOak Counter&r) a skříňka (&eOak Cupboard&r) se vyrábí s truhlou – můžeš do nich ukládat věci.",
            "Kladivem z &bHandcrafted&r změníš jejich tvar. Na pult klikni blokem dřeva nebo kamene a změníš desku.",
        ]),
        Q("hc_trophy", "Trofej", dep=["hc_chair"], optional=True, items=[("handcrafted:spider_trophy", 1)], xp=20, d=[
            "Trofeje se věší na zeď. Pavoučí trofej (&eSpider Trophy&r) vyrobíš z prken a pavoučího oka.",
            "Na vzácnější trofeje potřebuješ hlavy mobů, třeba lebku wither skeletona.",
        ]),
        # ---- Another Furniture ----
        Q("af_chair", "Zasunovací židle", dep=["intro"], items=[("another_furniture:oak_chair", 1)], xp=15, d=[
            "&bAnother Furniture&r: židle, stoličky, pohovky, police, závěsy, okenice a lampy.",
            "Židli (&eOak Chair&r) z &bAnother Furniture&r vyrobíš z prken a tyček. Dá se zasunout pod stůl.",
        ]),
        Q("af_hammer", "Nábytkové kladivo", dep=["af_chair"], items=[("another_furniture:furniture_hammer", 1)], xp=15, d=[
            "Kladivo (&eHammer&r) z &bAnother Furniture&r mění tvar nábytku z tohoto modu. Klikni s ním na nábytek.",
            "Vyrobíš ho z prken, dřevěného půlbloku a tyček.",
        ]),
        Q("af_cozy", "Útulný pokoj", dep=["af_chair"], items=[("another_furniture:white_curtain", 1), ("another_furniture:white_lamp", 1), ("another_furniture:white_sofa", 1)], xp=25, d=[
            "Závěs (&eWhite Curtain&r) je z vlny a tyček, lampa (&eWhite Lamp&r) z vlny, pochodně a tyčky, pohovka (&eWhite Sofa&r) z prken, vlny a tyček.",
            "Závěs se dá roztáhnout a zatáhnout kliknutím.",
        ]),
        Q("af_garden", "Truhlíky a zvonek", dep=["af_chair"], optional=True, items=[("another_furniture:oak_flower_box", 1), ("another_furniture:service_bell", 1)], xp=15, d=[
            "Do truhlíku (&eOak Flower Box&r) z prken, půlbloků a hlíny zasadíš květiny.",
            "Zvonek (&eService Bell&r) ze železa cinkne, když na něj klikneš. Ideální pro obchod nebo krčmu.",
        ]),
        # ---- Refurbished Furniture ----
        Q("rf_power", "Elektřina", dep=["intro", "building:refurbished"], items=[("refurbished_furniture:light_electricity_generator", 1), ("refurbished_furniture:wrench", 1)], xp=40, shape="hexagon", size=1.5, s="Pokročilý", d=[
            "Teď už nábytek nejen stojí, ale i pracuje. Elektrické věci z &bRefurbished Furniture&r potřebují proud – i dílenský stůl.",
            "Generátor (&eLight Electricity Generator&r) vyrobíš ze železných ingotů, redstonového bloku a vysoké pece. Pálí palivo jako pec, třeba uhlí.",
            "Klíčem (&eWrench&r) klikni na generátor a potom na spotřebič – vznikne kabel. Tak propojíš dílenský stůl, světla i kuchyň.",
        ]),
        Q("rf_light", "Světlo a vypínač", dep=["rf_power"], items=[("refurbished_furniture:light_ceiling_light", 1), ("refurbished_furniture:light_lightswitch", 1)], xp=20, d=[
            "Stropní světlo (&eLight Ceiling Light&r) a vypínač (&eLight Lightswitch&r) vyrobíš na dílenském stole.",
            "Světlo připoj klíčem k síti. Vypínačem ho rozsvítíš a zhasneš.",
        ]),
        Q("rf_bread", "Krájení chleba", dep=["rf_power"], items=[("refurbished_furniture:oak_cutting_board", 1), ("refurbished_furniture:knife", 1), ("refurbished_furniture:bread_slice", 1)], xp=20, d=[
            "Prkénko (&eOak Cutting Board&r) vyrobíš na dílenském stole, nůž (&eKnife&r) na pracovním stole.",
            "Polož chleba na prkénko a klikni na něj nožem. Dostaneš 6 krajíců (&eBread Slice&r).",
        ]),
        Q("rf_toast", "Toustovač", dep=["rf_bread"], items=[("refurbished_furniture:light_toaster", 1), ("refurbished_furniture:toast", 1)], xp=25, d=[
            "Toustovač (&eLight Toaster&r) ze železa a redstonu opeče krajíc chleba na toust (&eToast&r).",
            "&cToustovač potřebuje elektřinu.&r Připoj ho klíčem ke generátoru.",
        ]),
        Q("rf_kitchen", "Sporák a lednice", dep=["rf_toast"], items=[("refurbished_furniture:light_stove", 1), ("refurbished_furniture:light_fridge", 1), ("refurbished_furniture:frying_pan", 1)], xp=40, d=[
            "Sporák (&eLight Stove&r) potřebuje elektřinu. V jeho troubě upečeš třeba pizzu. Pánev (&eFrying Pan&r) polož na sporák a udělej na ní marmeládu nebo grilovaný sýr (&eGrilled Cheese&r).",
            "Lednice (&eLight Fridge&r) je velká úložná skříň na jídlo.",
            "Všechno vyrobíš na dílenském stole, hlavně ze železa a redstonu. Lednice potřebuje i měď.",
        ]),
        Q("rf_mail", "Pošta mezi hráči", dep=["rf_power"], items=[("refurbished_furniture:oak_mail_box", 1), ("refurbished_furniture:post_box", 1)], xp=30, d=[
            "Poštovní schránku (&eOak Mailbox&r) si postav u domu a pojmenuj ji.",
            "Z poštovní budky (&ePost Box&r) posíláš balíky do schránek ostatních. Najdi schránku podle jména, vlož věci, napiš vzkaz a odešli.",
        ]),
        Q("rf_tv", "Televize", dep=["rf_light"], optional=True, items=[("refurbished_furniture:television", 1), ("refurbished_furniture:television_remote", 1)], xp=30, d=[
            "Televize (&eTelevision&r) potřebuje elektřinu. Dálkovým ovladačem (&eTelevision Remote&r) ji ovládáš na dálku.",
        ]),
        Q("rf_computer", "Počítač", dep=["rf_kitchen", "rf_light"], items=[("refurbished_furniture:computer", 1)], xp=60, shape="hexagon", size=1.5, s="Expert", d=[
            "Počítač (&eComputer&r) vyrobíš na dílenském stole. Potřebuje elektřinu.",
            "Aplikace &eSmart Home&r zapne a vypne všechny spotřebiče ve stejné síti. Přejmenuj je na kovadlině, ať je poznáš.",
            "Hra &ePaddle Ball&r se hraje proti počítači nebo proti jinému hráči na serveru.",
        ]),
    ],
)

# Pořadí kapitol této oblasti v knize questů
CHAPTERS = [COLONIES, COL_LIFE, COL_CRAFT, COL_DEF, COL_TOOLS, BUILDING, FURNITURE]

NO_RECIPE = {}
