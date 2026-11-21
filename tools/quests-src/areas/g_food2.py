from engine import *

# =====================================================================
#  LET'S DO – farma, kuchyně, pekárna, sýry, pláž (+ první víno, pivo a čaj)
# =====================================================================
LETSDO = dict(
    key="lets_do", group="food", title="Let's Do: farma a kuchyně",
    subtitle="Farm & Charm, Bakery, Candlelight, Meadow, Vinery, Beachparty…", icon="vinery:wine_bottle",
    quests=[
        Q("intro", "Vítej na farmě", icon="farm_and_charm:crafting_bowl", tasks=[auto()], xp=10,
          shape="hexagon", size=1.5, s="Začátečník", d=[
            "Mody &bLet's Do&r přidávají nové plodiny, farmářské stroje a kuchyni, kde se vaří ručně krok za krokem.",
            "Základ je &bFarm & Charm&r: plodiny, mlýnek, kamna, hrnec a sila. Na něj navazují &bBakery&r (dorty), &bCandlelight&r (večeře), &bMeadow&r (sýry), &bVinery&r (víno), &bBrewery&r (pivo), &bHerbalBrews&r (čaj) a &bBeachparty&r (pláž).",
            "&aTip:&r Když se na stroj z těchto modů podíváš, ukáže se nápověda, co máš udělat (třeba „Right-Click: Stir“ = pravým tlačítkem míchej). Přesné recepty vždy najdeš v JEI."]),

        # ---------------- Farm & Charm: plodiny ----------------
        Q("fcrops", "Ječmen a oves", dep=["intro"], items=[("farm_and_charm:barley", 4), ("farm_and_charm:oat", 4)], xp=15, d=[
            "Nové plodiny nejdřív najdeš divoce rostoucí. Divoký ječmen (&eWild Barley&r) roste na pláních, u řek a v savaně, divoký oves (&eWild Oat&r) na loukách a v tajze.",
            "Když divokou rostlinu rozbiješ, dostaneš úrodu i semínka. Semínka pak zasaď na ornici jako pšenici.",
            "&aTip:&r Plodiny Farm & Charm rostou rychleji, když na ně prší."]),
        Q("veggies", "Zelenina a jahody", dep=["fcrops"], items=[("farm_and_charm:tomato", 4), ("farm_and_charm:lettuce", 2), ("farm_and_charm:onion", 2), ("farm_and_charm:strawberry", 4)], xp=20, d=[
            "Rajčata, salát, cibule a jahody také nejdřív najdi divoké. Rajčata rostou hlavně na pláních a v savaně, jahody skoro všude, kde je tráva.",
            "Z rajčete, salátu a jahody vyrobíš na pracovním stole semínka. Semínka pak zasaď na pole.",
            "&aTip:&r Z hromady zeleniny si můžeš vyrobit pytel (&eBag of Tomatoes&r…) – ušetříš místo v truhle."]),

        # ---------------- Farm & Charm: kuchyně ----------------
        Q("farm", "Miska a prkénko", dep=["intro"], items=[("farm_and_charm:crafting_bowl", 1), ("farm_and_charm:cutting_board", 1)], xp=20, d=[
            "Dva základní kuchyňské bloky. Oba polož na stůl nebo na zem.",
            "Do míchací misky (&eCrafting Bowl&r) vkládej suroviny pravým tlačítkem. Pak ji pravým tlačítkem míchej, dokud není hotovo.",
            "Krájecí prkénko (&eCutting Board&r) potřebuje nůž nebo sekáček – o tom je další úkol."]),
        Q("butter", "Máslo", dep=["farm"], items=[("farm_and_charm:butter", 4)], xp=15, d=[
            "Máslo (&eButter&r) je potřeba do spousty jídel.",
            "Vlož do míchací misky kbelík mléka a míchej. Z jednoho kbelíku jsou 4 kusy másla."]),
        Q("cleaver", "Sekáček", dep=["farm"], items=[("farm_and_charm:iron_cleaver", 1)], xp=15, d=[
            "Železný sekáček (&eIron Cleaver&r) je kuchyňský nůž i zbraň.",
            "Polož ho na krájecí prkénko. Pak se surovinou v ruce drž pravé tlačítko a surovina se nakrájí: z vepřového je slanina, z hovězího mleté maso, z těsta těstoviny.",
            "Na prkénku bez nástroje můžeš skládat jídla: polož na něj suroviny a klikni prázdnou rukou. Tak vzniknou třeba krmiva pro zvířata."]),
        Q("fstove", "Kamna a hrnec", dep=["farm"], items=[("farm_and_charm:stove", 1), ("farm_and_charm:cooking_pot", 1)], xp=25, d=[
            "Kamna (&eStove&r) jsou trouba s vlastním okénkem. Pečou chleby, koláče a pečeně. Potřebují palivo (uhlí, dřevo).",
            "Hrnec (&eCooking Pot&r) vaří polévky a guláš. Musí stát na zdroji tepla: na kamnech, táboráku nebo magmatu.",
            "&aTip:&r Polévky se nalévají do misky – tu dej do hrnce spolu se surovinami."]),
        Q("mincer", "Mlýnek a pekáč", dep=["fstove"], items=[("farm_and_charm:mincer", 1), ("farm_and_charm:roaster", 1)], xp=25, d=[
            "Mlýnek (&eMincer&r) mele maso, obilí i kosti. Vlož do něj surovinu a pravým tlačítkem toč klikou.",
            "Pekáč (&eRoaster&r) peče maso a hotová jídla. Stejně jako hrnec musí stát na zdroji tepla.",
            "&aTip:&r Mlýnek umí z kosti kostní moučku a ze shnilého masa hnojivo."]),
        Q("flour", "Mouka", dep=["mincer"], items=[("farm_and_charm:flour", 8)], xp=15, d=[
            "Pšenice semletá v mlýnku dá mouku (&eFlour&r) – z jedné pšenice jsou 4 mouky.",
            "Mouka je základ těsta, dortů i pekařského stolu z modu Bakery."]),
        Q("yeast", "Kvasnice", dep=["fstove"], items=[("farm_and_charm:yeast", 4)], xp=15, d=[
            "Kvasnice (&eYeast&r) se uvaří v hrnci z cukru, pšenice a kbelíku vody. Do hrnce přidej i misku.",
            "Z jednoho vaření je jich 12. Budeš je potřebovat na těsto, pivo i whisky."]),
        Q("dough", "Těsto", dep=["flour", "yeast"], items=[("farm_and_charm:dough", 5)], xp=20, d=[
            "Těsto (&eDough&r) zamícháš v misce z mouky, kvasnic a kbelíku vody.",
            "Z těsta upečeš chleba, nakrájíš těstoviny nebo uděláš preclíky."]),
        Q("bread", "Farmářský chléb", dep=["dough"], items=[("farm_and_charm:farmers_bread", 1)], xp=20, d=[
            "Farmářský chléb (&eFarmer's Bread&r) upečeš v kamnech z těsta a kbelíku vody.",
            "Hotový chléb jde položit na stůl jako blok – hezky vypadá v kuchyni."]),
        Q("soup", "Bramboračka", dep=["fstove", "veggies"], items=[("farm_and_charm:potato_soup", 1)], xp=20, d=[
            "Bramborová polévka (&ePotato Soup&r) je nejjednodušší polévka: brambora a cibule v hrnci, k tomu miska.",
            "Polévky dobře zasytí. Další recepty (guláš, rajská, ječná) najdeš v JEI u hrnce."]),
        Q("breakfast", "Farmářská snídaně", dep=["bread", "mincer", "butter", "veggies", "cleaver"], items=[("farm_and_charm:farmers_breakfast", 1)], xp=35,
          d=["Velká snídaně (&eFarmer's Breakfast&r) se skládá ze tří jídel: chleba, slaniny s vejci a pečené kukuřice.",
             "Slanina s vejci (&eBacon with Eggs&r) vznikne na pekáči (slanina, vejce, máslo, miska). Pečená kukuřice (&eRoasted Corn&r) v kamnech (2 kukuřice a máslo).",
             "&aTip:&r Jídla z Farm & Charm často dávají užitečné efekty. Uvidíš je v popisku jídla."]),

        # ---------------- Farm & Charm: zvířata a pole ----------------
        Q("animals", "Péče o zvířata", dep=["fcrops"], items=[("farm_and_charm:feeding_trough", 1), ("farm_and_charm:chicken_coop", 1)], xp=20, d=[
            "Do žlabu (&eFeeding Trough&r) nasyp semínka. Zvířata v okolí z něj sama žerou.",
            "Kurník (&eChicken Coop&r) pojme slepice a sbírá jejich vejce. Vejce si pak jen vybereš.",
            "&aTip:&r Napajedlo (&eWater Trough&r) zkracuje dobu, než se zvířata znovu rozmnoží."]),
        Q("feed", "Krmivo", dep=["animals", "cleaver"], items=[("farm_and_charm:chicken_feed", 3)], xp=15, d=[
            "Krmivo pro slepice (&eChicken Feed&r) složíš na krájecím prkénku bez nástroje: pšenice, mrkev a semínka.",
            "Slepice po něm snášejí víc vajec a ztrácejí víc peří. Podobně funguje krmivo pro koně (&eHorse Fodder&r) – kůň je pak rychlejší a skáče výš."]),
        Q("sprinkler", "Zavlažování", dep=["fcrops"], items=[("farm_and_charm:water_sprinkler", 1), ("farm_and_charm:timber_well", 1)], xp=25, d=[
            "Zavlažovač (&eWater Sprinkler&r) zalévá ornici kolem sebe, takže nevyschne. Pravým tlačítkem přepínáš tlak vody.",
            "Studna (&eTimber Well&r) pumpuje vodu ze zdroje pod sebou. Klikni na ni prázdnou rukou. Za deště se plní i sama a zvířata z ní pijí."]),
        Q("silo", "Silo a hnojivo", dep=["fcrops", "mincer"], items=[("farm_and_charm:silo_wood", 2), ("farm_and_charm:fertilizer", 4)], xp=30,
          shape="hexagon", size=1.5, s="Pokročilý", d=[
            "Ruční vaření umíš. Teď si farmu vylepšíš. Silo (&eWooden Silo&r) suší věci. Víc sil postavených vedle sebe a na sebe se spojí v jedno velké.",
            "Pravým tlačítkem do sila vlož kostní moučku. Po chvíli z ní je hnojivo (&eFertilizer&r). Prázdnou rukou otevřeš poklop a hotové věci vybereš.",
            "Silo suší i obilí pro pivovar (sušený ječmen, pšenici, kukuřici a oves). Hnojivo použité na pole pohnojí několik plodin najednou."]),
        Q("fsoil", "Hnojená půda", dep=["silo"], items=[("farm_and_charm:fertilized_soil", 1), ("farm_and_charm:pitchfork", 1)],
          tasks=[adv("farm_and_charm:main/use_pitchfork_on_fertilized_soil")], xp=35, d=[
            "Hnojenou půdu (&eFertilized Soil&r) vyrobíš z 9 hnojiv. Polož ji na pole.",
            "Použij na ni vidle (&ePitchfork&r). Rostliny v okolí pak porostou rychleji.",
            "Když je půda plná, motykou z ní uděláš hnojenou ornici. Plodiny na ní občas povyrostou samy, jako by dostaly kostní moučku."]),
        Q("carts", "Pluh a secí stroj", dep=["animals", "silo"], items=[("farm_and_charm:plow", 1), ("farm_and_charm:seeder", 1)], xp=35, d=[
            "Velká pole se ručně dělají pomalu. Pluh (&ePlow&r) a secí stroj (&eSeeder&r) jsou vozíky, které táhneš za sebou.",
            "Polož vozík a klikni na něj – zapřáhneš ho za sebe. Na ochočeného koně nebo osla ho zapřáhneš kliknutím na zvíře. Shift + pravé tlačítko vozík odepne.",
            "Pluh při jízdě orá (Shift + pravé tlačítko ho zapne a vypne). Do secího stroje dej semínka (Shift + pravé tlačítko) a při jízdě sám zasévá."]),
        Q("scarecrow", "Zlatý strašák", dep=["breakfast", "soup", "carts"], items=[("farm_and_charm:scarecrow", 1)], xp=100,
          shape="hexagon", size=1.5, s="Expert", d=[
            "Mistrovská zkouška Farm & Charm: uvař každé jídlo z tohoto modu (polévky, pečeně, saláty, snídaně…).",
            "Když máš všechna jídla, dostaneš za úspěch &bFarm & Charm&r odměnu – strašáka (&eScarecrow&r). Ten zrychluje růst rostlin v okolí.",
            "&aTip:&r Seznam všech jídel uvidíš v postupu (Advancements) u úspěchu &eFarm to Table&r."]),

        # ---------------- Bakery ----------------
        Q("bakery", "Pekárna", dep=["flour"], items=[("bakery:baker_station", 1), ("bakery:rolling_pin", 1)], xp=25, d=[
            "&bBakery&r přidává dorty, koláče, marmelády a sladké pečivo.",
            "Pekařský stůl (&eCaking Station&r) vyrobíš z cihel, dřevěných desek a mouky. Váleček (&eRolling Pin&r) z prken a dřevěných desek.",
            "Na stůl pokládáš těsto a tvaruješ ho přímo na něm: hnětením rukou, válečkem nebo nožem."]),
        Q("jam", "Marmeláda", dep=["bakery", "veggies"], items=[("bakery:small_cooking_pot", 1), ("bakery:strawberry_jam", 1)], xp=25, d=[
            "Hrnec na marmeládu (&eJam Pot&r) postav na zdroj tepla, třeba na táborák.",
            "Dej do něj 2 jahody a cukr. Během vaření ho pravým tlačítkem míchej, ať se nepřipálí. Hotovou marmeládu nabereš do sklenice (&eJar&r).",
            "Marmelády (jahodová, jablečná, čokoládová, ze sladkých a svítivých bobulí) se dávají na dorty, koláčky a chleba."]),
        Q("cakedough", "Těsto na dort", dep=["bakery", "butter"], items=[("bakery:cake_dough", 4)], xp=15, d=[
            "Těsto na dort (&eCake Dough&r) zamícháš v misce z mouky, cukru, vejce a mléka.",
            "Sladké těsto (&eSweet Dough&r) má místo mléka vodu. Z něj se dělají koláčky a croissanty."]),
        Q("cake", "Jahodový dort", dep=["jam", "cakedough"], items=[("bakery:strawberry_cake", 1)], xp=35, d=[
            "Polož těsto na dort na pekařský stůl. Vznikne korpus.",
            "Klikni na něj jahodovou marmeládou – a jahodový dort (&eStrawberry Cake&r) je hotový. Pravým tlačítkem ho vezmeš.",
            "Dort pak polož a krájej nožem. Ze sladkého těsta se stejně dělají cupcaky a sušenky (váleček, nůž, marmeláda)."]),
        Q("croissant", "Croissanty", dep=["bakery", "yeast", "cakedough"], items=[("bakery:croissant", 4)], xp=20, d=[
            "Croissanty (&eCroissant&r) upečeš v kamnech ze sladkého těsta, kvasnic a cukru.",
            "Pečivo z Bakery dává efekty, třeba &eSugar Rush&r (rychlejší chůze) nebo &eVitality&r (pomaleji ti ubývá hlad)."]),
        Q("bakery_banner", "Mistr pekař", dep=["cake", "croissant"], items=[("bakery:bakery_banner", 1)], xp=100,
          shape="hexagon", size=1.5, s="Expert", d=[
            "Upeč a sesbírej všechno pečivo z &bBakery&r – chleby, dorty, koláčky, marmelády.",
            "Odměnou je prapor pekárny (&eCompletionist Banner: Bakery&r). Když ho postavíš, dává hráčům v okolí odolnost (&eResistance&r)."]),

        # ---------------- Candlelight ----------------
        Q("candlelight", "Candlelight", dep=["fstove"], items=[("candlelight:cooking_pan", 1), ("candlelight:plate", 1)], xp=25, d=[
            "&bCandlelight&r je mod o slavnostních večeřích: jídla na talíři, prostírání a nábytek.",
            "Měděná pánev (&eCooking Pan&r) funguje jako pekáč a velký hrnec (&eCooking Pot&r) jako hrnec z Farm & Charm. Oba musí stát na zdroji tepla.",
            "Talíř (&ePlate&r) polož na stůl. Na něj se servírují hotová jídla."]),
        Q("mozzarella", "Mozzarella", dep=["farm"], items=[("candlelight:mozzarella", 3)], xp=15, d=[
            "Mozzarellu (&eMozzarella&r) zamícháš v misce z kbelíku mléka a kbelíku vody.",
            "Sýr potřebuješ do lasagní a těstovin. Místo ní můžeš použít i sýr z modu Meadow."]),
        Q("pasta", "Těstoviny", dep=["dough", "cleaver"], items=[("farm_and_charm:raw_pasta", 4)], xp=15, d=[
            "Syrové těstoviny (&eRaw Pasta&r) nakrájíš z těsta na prkénku se sekáčkem nebo semeleš v mlýnku."]),
        Q("bolognese", "Boloňská omáčka", dep=["candlelight", "mincer", "soup", "cleaver"], items=[("candlelight:bolognese", 1)], xp=25, d=[
            "Boloňská omáčka (&eBolognese&r) se dělá na pekáči nebo pánvi. Potřebuješ rajskou polévku, mleté hovězí, slaninu, cibuli, mrkev, lahev s vodou a misku.",
            "Rajskou polévku uvaříš v hrnci. Přesný recept ukáže JEI."]),
        Q("lasagne", "Lasagne", dep=["bolognese", "pasta", "mozzarella"], items=[("candlelight:lasagne", 1)], xp=35, d=[
            "Lasagne (&eLasagne&r) upečeš v kamnech z boloňské omáčky, těstovin a sýra.",
            "Z jednoho pečení jsou dvě. Polož je na talíř a máš hlavní chod."]),
        Q("dinner", "Prostřený stůl", dep=["candlelight"], items=[("candlelight:napkin", 1), ("candlelight:wine_glass", 1)], xp=30, d=[
            "Polož talíř na stůl a dej na něj hotový pokrm. Když ho sníš z talíře, dostaneš efekt &eWell Served&r – dokud trvá, nebudeš mít opravdový hlad.",
            "Ubrousek (&eNapkin&r), sklenice na víno (&eWine Glass&r) a svíčka nebo lampa poblíž vylepší prostírání (&eTable Setting&r).",
            "&aTip:&r Podívej se na talíř – nápověda ukáže, co na stole ještě chybí."]),
        Q("candle_banner", "Šéfkuchař", dep=["lasagne", "dinner"], items=[("candlelight:candlelight_banner", 1)], xp=100,
          shape="hexagon", size=1.5, s="Expert", d=[
            "Uvař každé jídlo z &bCandlelight&r.",
            "Odměnou je prapor (&eCompletionist Banner: Candlelight&r). Postavený dává hráčům v okolí odolnost vůči ohni.",
            "&aTip:&r Kuchařský oblek (čepice, kabát, kalhoty, boty) dává šanci na porci navíc z pánve a hrnce."]),

        # ---------------- Meadow ----------------
        Q("meadow_find", "Biom Meadow", dep=["intro"], icon="meadow:cheese_wheel", tasks=[biome("minecraft:meadow")], xp=15, d=[
            "&bMeadow&r je mod o horském životě: sýry, krávy &eHighland Cattle&r, buvoli &eWater Buffalo&r, horské květiny a sůl.",
            "Najdi biom &eMeadow&r – je vysoko v horách a je plný květin. Tam najdeš alpskou sůl a pasou se tam krávy &eHighland Cattle&r."]),
        Q("salt", "Alpská sůl", dep=["meadow_find"], items=[("meadow:alpine_salt", 4)], xp=15, d=[
            "Ruda alpské soli (&eAlpine Salt Ore&r) je v kamení na loukách. Vytav ji v peci.",
            "Sůl uvaříš i v kotli (&eCookpot&r) z kalcitu nebo vápence s vodou."]),
        Q("meadow", "Sýrárna", dep=["salt"], items=[("meadow:cheese_form", 1), ("meadow:cookpot", 1)], xp=25, d=[
            "Kotel (&eCookpot&r) postav na zdroj tepla a nalij do něj vodu. Vaří se v něm syřidlo, sůl a jídla.",
            "Lis na sýr (&eCheese Press&r) z mléka a syřidla udělá sýr."]),
        Q("rennet", "Syřidlo", dep=["meadow"], items=[("meadow:rennet", 2)], xp=20, d=[
            "Syřidlo (&eRennet&r) uvaříš v kotli z vejce a soli. Do kotle dej i skleněnou lahev a nezapomeň na vodu.",
            "Syřidlo srazí mléko na sýr."]),
        Q("meadowcheese", "Kolo sýra", dep=["rennet"], items=[("meadow:cheese_wheel", 1)], xp=30, d=[
            "Do lisu nalij mléko a přidej syřidlo (obojí pravým tlačítkem). Pak prázdnou rukou toč klikou dolů a nahoru.",
            "Hotové kolo sýra (&eCheese Wheel&r) vezmi prázdnou rukou. Na pracovním stole ho rozkrojíš na 4 plátky.",
            "&aTip:&r Mléko ovcí, koz, buvolů &eWater Buffalo&r a dalších zvířat dá jiné druhy sýra."]),
        Q("wbucket", "Mléko z buvola", dep=["meadow_find"], items=[("meadow:wooden_bucket", 1)], xp=15, d=[
            "Dřevěným kbelíkem (&eWooden Bucket&r) podojíš krávy, ovce, kozy i buvoly &eWater Buffalo&r. Každé zvíře dá jiné mléko.",
            "Buvoli &eWater Buffalo&r žijí v savaně, u řek a v bažinách."]),
        Q("fondue", "Fondue", dep=["meadowcheese"], items=[("meadow:fondue_pot", 1)], xp=25, d=[
            "Hrnec na fondue (&eFondue Pot&r) postav na zdroj tepla a vlož do něj sýr. Míchej ho, než se roztaví.",
            "Pak do něj namoč chleba – dostaneš sýrovou tyčinku (&eCheese Stick&r)."]),
        Q("meadow_banner", "Znalec sýrů", dep=["meadowcheese", "wbucket"], items=[("meadow:meadow_banner", 1)], xp=100,
          shape="hexagon", size=1.5, s="Expert", d=[
            "Vyrob všech 7 druhů sýra: obyčejný, ovčí, kozí, buvolí, obilný, ametystový a warpový.",
            "Odměnou je prapor (&eCompletionist Banner: Meadow&r). Postavený zrychluje těžení hráčům v okolí."]),

        # ---------------- Vinery (základy) ----------------
        Q("grapes", "Vinné hrozny", dep=["intro"], items=[("vinery:red_grape", 3), ("vinery:white_grape", 3)], xp=15, d=[
            "&bVinery&r je mod o vinařství. Divoké keře s hrozny rostou v lesích, na pláních, loukách, u řek a v horách.",
            "Pravým tlačítkem hrozny z keře otrháš. Když keř rozbiješ, dostaneš semínka. Semínka vyrobíš i z hroznu na pracovním stole.",
            "&aTip:&r V tajze, savaně a džungli rostou jiné odrůdy. Každá dá jinou šťávu."]),
        Q("wine", "Vinné lahve", dep=["grapes"], items=[("vinery:wine_bottle", 1)], xp=15, d=[
            "Do vinné lahve (&eWine Bottle&r) se stáčí šťáva i hotové víno. Ze 2 skleněných lahví vyrobíš 4 vinné lahve.",
            "Měj jich vždy pár po ruce."]),
        Q("gpot", "Šlapání hroznů", dep=["wine"], items=[("vinery:grapevine_pot", 1), ("vinery:red_grapejuice", 1)], xp=25, d=[
            "Káď na hrozny (&eGrapevine Pot&r) vyrobíš z prken a dřevěných desek.",
            "Pravým tlačítkem do ní dej 6 hroznů stejného druhu. Pak na ní skákej – hrozny rozšlapeš. V těžkém brnění to jde rychleji.",
            "Hotovou šťávu (&eRed Grapejuice&r) nabereš prázdnou vinnou lahví."]),
        Q("press", "Lis na jablka", dep=["wine"], items=[("vinery:apple_press", 1)], xp=25, d=[
            "Lis (&eApple Press&r) vyrobíš ze sudu, železného poklopu a klacků.",
            "V lisu nejdřív rozmačkáš jablka na kaši (&eApple Mash&r). Kaše s prázdnou vinnou lahví pak dá jablečný džus (&eApple Juice&r).",
            "Jablka padají i z jabloní z Vinery, které rostou na pláních a loukách."]),
        Q("barrel", "Kvasný sud", dep=["gpot"], items=[("vinery:fermentation_barrel", 1)], xp=30, d=[
            "Kvasný sud (&eFermentation Barrel&r) vyrobíš z obyčejného sudu a 2 klacků.",
            "Otevři ho a nalij do něj šťávu z lahví. Pak přidej přísady a prázdnou vinnou lahev. Po chvíli kvašení je víno hotové.",
            "Každé víno potřebuje jinou šťávu a jiné přísady. Najdeš je v JEI u sudu."]),
        Q("redwine", "První víno", dep=["barrel"], items=[("vinery:red_wine", 1)], xp=30,
          shape="hexagon", size=1.5, s="Pokročilý", d=[
            "Červené víno (&eRed Wine&r) je nejjednodušší: šťáva z červených hroznů a cukr.",
            "Víno dává efekt – červené víno pomalé padání. Jiná vína dávají třeba skok, neviditelnost nebo chůzi po vodě.",
            "Další vína, zrání a vzácné odrůdy najdeš v kapitole &bLet's Do: víno, pivo a čaj&r."]),

        # ---------------- Brewery (základy) ----------------
        Q("brewery", "Pivovar", dep=["fcrops"], items=[("brewery:wooden_brewingstation", 1), ("brewery:hops", 4)], xp=30, d=[
            "&bBrewery&r je mod o vaření piva a whisky. Pivo se vaří ve varně (&eWooden Brewing Station&r) – má kotel, pec a tlačítko časovače.",
            "Do kotle nalij kbelík vody a do pece přilož palivo. Pak vlož suroviny a stiskni tlačítko časovače. Co chybí, ti varna ukáže, když se na ni podíváš.",
            "Chmel (&eHops&r) najdeš divoký v tajze (&eWild Hops&r). Můžeš ho i zasadit a pěstovat."]),
        Q("beer", "Na zdraví!", dep=["brewery", "silo", "yeast"], items=[("brewery:beer_wheat", 1)], xp=30, d=[
            "Pšeničné pivo (&eWheat Beer&r) uvaříš z chmele, sušené pšenice a kvasnic. Pšenici usuš v silu.",
            "Hotové pivo stočíš do korbele (&eBeer Mug&r) – vyrobíš ho z prken. Whisky se stáčí do skleněných lahví.",
            "&cPozor:&r Moc pití způsobí opilost (&eIntoxication&r). Od úrovně III se motáš, od úrovně VI můžeš omdlít."]),

        # ---------------- HerbalBrews (základy) ----------------
        Q("herbal", "Čajové lístky", dep=["intro"], items=[("herbalbrews:tea_kettle", 1), ("herbalbrews:green_tea_leaf", 4)], xp=25, d=[
            "&bHerbalBrews&r je mod o čaji a kávě. Čaj se vaří v konvici (&eTea Kettle&r).",
            "Čajové lístky rostou na čajovníku. Jeho semínko je čajový květ (&eTea Blossom&r). Ten dostaneš z ibišku (roste v džungli), když ho utrhneš nůžkami. Zasaď ho a lístky (&eGreen Tea Leaf&r) sklízej.",
            "&aTip:&r Čajový květ občas vypadne i z levandule (roste v horách), ale jen když ji utrhneš rukou, ne nůžkami."]),
        Q("hb_dry", "Sušení čaje", dep=["herbal"], items=[("herbalbrews:dried_green_tea", 4)], xp=20, d=[
            "Čerstvé lístky se musí usušit. Z 9 lístků vyrob blok (&eGreen Tea Leaf Block&r) a polož ho venku na slunce.",
            "Blok časem uschne. Když ho rozbiješ, dostaneš sušený zelený čaj (&eDried Green Tea&r)."]),
        Q("tea", "Šálek čaje", dep=["hb_dry"], items=[("herbalbrews:green_tea", 1)], xp=25, d=[
            "Konvice musí stát na zdroji tepla – na sporáku (&eStove&r) z HerbalBrews nebo na sporáku z Farmer's Delight.",
            "Konvice potřebuje vodu a teplo. Vodu doplníš kbelíkem nebo lahví vody, teplo zvýšíš ohnivým práškem. Pak vlož sušený čaj a skleněnou lahev.",
            "Zelený čaj (&eGreen Tea&r) dává efekt &eBalanced&r: hráči v okolí dostanou extra srdíčka (pohlcení)."]),
        Q("coffee", "Káva", dep=["herbal"], items=[("herbalbrews:coffee", 1)], xp=25, d=[
            "Divoká káva (&eWild Coffee&r) roste v džungli. Dá ti kávová zrna (&eCoffee Beans&r), která můžeš zasadit.",
            "V konvici uvaříš zrna se skleněnou lahví. Káva (&eCoffee&r) dává efekt &eDeeprush&r – čím hlouběji těžíš, tím rychleji.",
            "&aTip:&r Káva s mlékem (&eMilk Coffee&r) má stejný efekt, ale vydrží déle."]),

        # ---------------- Beachparty ----------------
        Q("beach_find", "Na pláž!", dep=["intro"], icon="beachparty:coconut", tasks=[biome("minecraft:beach")], xp=10, d=[
            "&bBeachparty&r přidává palmy, kokosy, mušle, koktejly a plážové vybavení.",
            "Najdi biom &eBeach&r (pláž). Rostou tam palmy s kokosy a v písku najdeš mušle."]),
        Q("beach", "Kokosy a bar", dep=["beach_find"], items=[("beachparty:coconut", 2), ("beachparty:palm_bar", 1)], xp=25, d=[
            "Kokosy (&eCoconut&r) visí na palmách – rozbij je. Z palmového dřeva vyrobíš bar (&ePalm Bar&r).",
            "Kokos otevřeš tak, že ho hodíš (pravé tlačítko). Na zemi se rozbije na otevřený kokos (&eOpen Coconut&r)."]),
        Q("cocktail", "Koktejl", dep=["beach"], items=[("beachparty:coconut_cocktail", 1)], xp=25, d=[
            "Otevři bar a smíchej v něm koktejl. Kokosový koktejl (&eCoconut Cocktail&r) je z otevřeného kokosu, ledu a lahve medu.",
            "Další koktejly (melounový, medový, dýňový…) najdeš v JEI u baru."]),
        Q("seashell", "Mušle", dep=["beach_find"], items=[("beachparty:seashell", 2)], xp=15, d=[
            "Mušle (&eSeashell&r) leží v písku na plážích.",
            "Když mušli použiješ, otevře se. Většinou je v ní syrové maso slávky, ale někdy i zlato, smaragd nebo diamant."]),
        Q("artifact", "Plážový poklad", dep=["seashell"], items=[("beachparty:crocs", 1)], xp=35, d=[
            "Plážové poklady najdeš v truhlách staveb &eBuried Treasure&r, &eShipwreck&r, &eOcean Ruins&r a &eDesert Pyramid&r.",
            "Pantofle (&eCrocs&r) ti dovolí běhat po vodě. Další poklady jsou třeba nafukovací kruhy (rychlejší plavání) nebo brýle (menší zranění ohněm)."]),
        Q("beach_banner", "Král pláže", dep=["cocktail", "artifact"], items=[("beachparty:beachparty_banner", 1)], xp=100,
          shape="hexagon", size=1.5, s="Expert", d=[
            "Sesbírej všechny plážové poklady a namíchej všechny koktejly.",
            "Odměnou je prapor (&eCompletionist Banner: Beachparty&r). Postavený dává hráčům v okolí dýchání pod vodou."]),
    ],
)

# =====================================================================
#  LET'S DO – pokročilé nápoje: víno, pivo a čaj
# =====================================================================
DRINKS = dict(
    key="lets_do_drinks", group="food", title="Let's Do: víno, pivo a čaj",
    subtitle="Vinery, Brewery a HerbalBrews do hloubky", icon="vinery:red_wine",
    quests=[
        Q("intro", "Sklep plný lahví", icon="brewery:beer_mug", tasks=[auto()], xp=10,
          shape="hexagon", size=1.5, s="Začátečník", d=[
            "Tato kapitola navazuje na kapitolu &bLet's Do: farma a kuchyně&r. Tam vyrobíš první víno, první pivo a první čaj.",
            "Tady pěstuješ vzácné odrůdy, necháváš víno zrát, vaříš whisky a mícháš čaje se silnými efekty.",
            "&aTip:&r Většina nápojů dává efekt. Najetím myši na nápoj ho uvidíš v popisku."]),

        # ---------------- Vinery ----------------
        Q("stems", "Vinná réva", dep=["intro", "lets_do:grapes"], items=[("vinery:grapevine_stem", 4), ("vinery:red_grape_seeds", 2)], xp=20, d=[
            "Kmínky révy (&eGrapevine Stem&r) vyrobíš z polen.",
            "Postav kmínek a pravým tlačítkem na něj zasaď semínka hroznů. Réva na něm vyroste a dává hrozny."]),
        Q("lattice", "Džunglová réva", dep=["stems"], items=[("vinery:oak_lattice", 4), ("vinery:jungle_grapes_red", 3)], xp=25, d=[
            "Džunglové hrozny (&eRed Jungle Grapes&r) rostou divoce v džungli a v biomu &eWooded Badlands&r.",
            "Jejich semínka se sázejí na mřížku (&eOak Lattice&r) – vyrobíš ji z klacků a prken. Réva po ní šplhá."]),
        Q("varieties", "Odrůdy z cest", dep=["stems"], items=[("vinery:savanna_grapes_red", 2), ("vinery:taiga_grapes_white", 2)], xp=25, d=[
            "Savanové hrozny rostou v savaně, tajgové hrozny v tajze a v horách.",
            "Každá odrůda dá jinou šťávu a z každé šťávy se dělají jiná vína. Sud pojme vždy jen jeden druh šťávy."]),
        Q("aging", "Zrání vína", dep=["intro", "lets_do:redwine"], items=[("vinery:oak_wine_rack_mid", 1)], xp=30,
          shape="hexagon", size=1.5, s="Pokročilý", d=[
            "Teď už nejde jen o to víno vyrobit. Víno stárne, jen když je uložené – ve stojanu na víno (&eOak Wine Rack&r) nebo v bedně na víno.",
            "Čím je víno starší, tím silnější a delší efekt dává. Nejlépe zraje ve sklepě, kam nesvítí obloha.",
            "&aTip:&r Na lahvi vidíš, kolik je vínu let."]),
        Q("cherry", "Třešňové víno", dep=["aging"], items=[("vinery:cherry_wine", 1)], xp=30, d=[
            "Třešně (&eCherry&r) padají z listí třešní z Vinery. Ty rostou na pláních a loukách.",
            "Třešňové víno (&eCherry Wine&r) je z červené šťávy a třešní. Dává neviditelnost."]),
        Q("magnetic", "Magnetické víno", dep=["aging", "lattice"], items=[("vinery:magnetic_wine", 1)], xp=35, d=[
            "Magnetické víno (&eMagnetic Wine&r) je z červené džunglové šťávy a železného ingotu.",
            "Dává efekt &eMagnet&r: předměty kolem tebe se k tobě samy přitahují."]),
        Q("jellie", "Lepší než zlaté jablko", dep=["magnetic", "varieties", "lets_do:press"], items=[("vinery:jellie_wine", 1)], xp=60, d=[
            "Víno &eJellie Wine&r je nejsilnější víno. Dává podobné, ale lepší efekty než zlaté jablko.",
            "Potřebuješ bílou šťávu a tři jiná vína: jablečné (&eApple Wine&r), &eChenet Wine&r a &eBolvar Wine&r. Každé je z jiné šťávy – recepty najdeš v JEI."]),
        Q("vinery_banner", "Vinařský mistr", dep=["jellie", "cherry"], items=[("vinery:vinery_standard", 1)], xp=100,
          shape="hexagon", size=1.5, s="Expert", d=[
            "Vyrob všech 25 vín a moštů z &bVinery&r.",
            "Odměnou je prapor (&eCompletionist Banner: Vinery&r). Postavený dává hráčům v okolí regeneraci II.",
            "&cPozor:&r Po vypití vína &eA Bottle of 'Creepers Crush'&r za pár sekund vybuchneš!"]),

        # ---------------- Brewery ----------------
        Q("dried", "Sušené obilí", dep=["intro", "lets_do:beer"], items=[("brewery:dried_barley", 2), ("brewery:dried_corn", 2), ("brewery:dried_oat", 2)], xp=20, d=[
            "Silo z Farm & Charm usuší ječmen, kukuřici i oves. Sušené obilí je základ všech piv a whisky.",
            "Ječmenné pivo, ovesné pivo i pivo z kopřiv vaříš ve dřevěné varně stejně jako pšeničné."]),
        Q("barrel", "Velký sud", dep=["dried"], items=[("brewery:barrel_main", 1)], xp=25, d=[
            "Velký sud (&eBig Barrel&r) vyrobíš ze 4 sudů.",
            "Pravým tlačítkem do něj uložíš nápoj a v sudu zraje. Shift + pravé tlačítko ho vyndá.",
            "&aTip:&r Podívej se na sud – uvidíš, jak moc nápoj už uzrál."]),
        Q("copper", "Měděná varna", dep=["dried"], items=[("brewery:copper_brewingstation", 1)], xp=40,
          shape="hexagon", size=1.5, s="Pokročilý", d=[
            "Whisky dřevěná varna neuvaří. Potřebuješ měděnou (&eCopper Brewing Station&r).",
            "Vylepšíš ji v kovářském stole: dřevěná varna + měděný ingot + kovářská šablona zdobení „Sentry“. Šablonu najdeš v truhlách ve stavbě &ePillager Outpost&r."]),
        Q("whiskey", "Whisky", dep=["copper"], items=[("brewery:whiskey_jojannik", 1)], xp=35, d=[
            "Whisky &eJoJannik Select&r uvaříš v měděné varně ze 2 sušených ječmenů a kvasnic.",
            "Každá whisky je z jiné kombinace sušeného obilí. Stáčí se do skleněných lahví."]),
        Q("breath", "Dechová zkouška", dep=["dried"], items=[("brewery:breathalyzer", 1)], xp=15, optional=True, d=[
            "Alkoholtester (&eBreathalyzer&r) ukáže, jak moc jsi opilý.",
            "Celý kroj z pivních slavností (klobouk &eBrewfest Hat&r, oblečení a boty) tě před opilostí úplně ochrání."]),
        Q("tent", "Najdi Brewfest Tent", dep=["intro"], icon="brewery:brewfest_hat", tasks=[structure("brewery:brewfest_tent")], xp=30, optional=True, d=[
            "Na pláních občas stojí stavba &eBrewfest Tent&r (stan pro pivní slavnost).",
            "Je vzácný, tak se při cestování po pláních rozhlížej."]),
        Q("netherite", "Netheritová varna", dep=["whiskey", "barrel"], items=[("brewery:netherite_brewingstation", 1)], xp=80,
          shape="hexagon", size=1.5, s="Expert", d=[
            "Nejlepší varna (&eNetherite Brewing Station&r). Vylepšíš měděnou varnu v kovářském stole s netheritovým ingotem a netheritovou šablonou.",
            "Jen v ní uvaříš whisky &eSmokey Reverie, Barrel-Aged&r, &eJameson Malt Whiskey&r a nejsilnější nápoj &eDark Brew&r.",
            "Za položení netheritové varny dostaneš prapor &bBrewery&r (zrychluje těžení v okolí)."]),
        Q("darkbrew", "Temný nápoj", dep=["netherite"], items=[("brewery:dark_brew", 1)], xp=80, d=[
            "&eDark Brew&r uvaříš v netheritové varně ze tří whisky: &eJoJannik Select&r, &eLilitu Single Malt&r a &eMaggoAllan, Aged&r.",
            "Všechny tři whisky nejdřív uvař v měděné varně."]),

        # ---------------- HerbalBrews ----------------
        Q("hstove", "Sporák na čaj", dep=["intro", "lets_do:tea"], items=[("herbalbrews:stove", 1)], xp=15, d=[
            "Sporák (&eStove&r) z HerbalBrews ohřívá konvici. Vyrobíš ho z táboráku, kamene a železných nugetů.",
            "Některé čaje potřebují víc tepla. Ohnivý prášek vložený do konvice teplo zvýší."]),
        Q("black", "Černý čaj", dep=["hstove"], items=[("herbalbrews:black_tea", 1)], xp=25, d=[
            "Z 9 sušených zelených čajů vyrob blok (&eDried Green Tea Leaf Block&r) a nech ho znovu uschnout. Vznikne černý čaj (&eDried Black Tea&r).",
            "Černý čaj (&eBlack Tea&r) uvaříš s cukrem. Efekt &eTough&r: při málo životech dostaneš odolnost a regeneraci."]),
        Q("oolong", "Oolong", dep=["black"], items=[("herbalbrews:oolong_tea", 1)], xp=30, d=[
            "Ze sušeného zeleného a černého čaje vyrob smíšený blok (&eMixed Tea Leaf Block&r). Když uschne, dá čaj oolong (&eDried Oolong Tea&r).",
            "Oolong (&eOolong Tea&r) dává efekt &eFortune&r – víc štěstí a lepší kořist."]),
        Q("flowers", "Květinové čaje", dep=["hstove"], items=[("herbalbrews:lavender_tea", 1), ("herbalbrews:hibiscus_tea", 1)], xp=30, d=[
            "Levandule roste v horách, ibišek v džungli. Na čaj potřebuješ květ levandule (&eLavender Blossom&r) – ten dostaneš, když levanduli utrhneš nůžkami.",
            "Levandulový čaj dává &eFeral&r (víc útoku a brnění), ibiškový &eLifeleech&r (bereš nepřátelům životy)."]),
        Q("jug", "Džbán", dep=["black"], items=[("herbalbrews:jug", 1)], xp=20, d=[
            "Do džbánu (&eJug&r) naliješ až tři různé čaje.",
            "Když se z něj napiješ, dostaneš efekty všech čajů naráz."]),
        Q("cauldron", "Bylinný kotel", dep=["oolong"], items=[("herbalbrews:cauldron", 1), ("herbalbrews:herbal_infusion", 1)], xp=40,
          shape="hexagon", size=1.5, s="Pokročilý", d=[
            "Kotel (&eBrewing Cauldron&r) spojí několik nápojů do jedné lahve (&eFlask&r).",
            "Jako katalyzátor potřebuje bylinný výluh (&eHerbal Infusion&r). Ten vyrobíš ze sušeného zeleného, černého a oolong čaje."]),
        Q("all_effects", "Všechny efekty naráz", dep=["cauldron", "flowers", "jug", "lets_do:coffee"], icon="herbalbrews:flask",
          tasks=[adv("herbalbrews:main/all_effects")], xp=80, d=[
            "Měj na sobě všech 7 efektů HerbalBrews najednou: &eBalanced&r, &eTough&r, &eDeeprush&r, &eFortune&r, &eFeral&r, &eLifeleech&r a &eBonding&r.",
            "&eBonding&r dává čaj maté (&eYerba Mate Tea&r). Maté roste v horách a jeho čaj potřebuje v konvici hodně tepla.",
            "&aTip:&r Džbán a lahev z kotle ti ušetří spoustu pití."]),
        Q("hb_banner", "Mistr čaje", dep=["all_effects"], items=[("herbalbrews:herbalbrews_banner", 1)], xp=100,
          shape="hexagon", size=1.5, s="Expert", d=[
            "Uvař všechny čaje a kávy z &bHerbalBrews&r.",
            "Odměnou je prapor (&eCompletionist Banner: Herbal Brews&r). Postavený dává hráčům v okolí extra srdíčka (pohlcení)."]),
    ],
)

# =====================================================================
#  CREATE – automatizace jídla
# =====================================================================
CREATEFOOD = dict(
    key="create_food", group="food", title="Create: kuchyně",
    subtitle="Jídlo a pití vyráběné stroji Create", icon="sliceanddice:slicer",
    quests=[
        Q("start", "Jídlo a stroje", icon="create:mechanical_mixer", tasks=[auto()], xp=10,
          shape="hexagon", size=1.5, s="Začátečník", d=[
            "Stroje Create umí vařit. Míchačka míchá těsta a omáčky, lis lisuje, dávkovač (&eSpout&r) nalévá tekutiny a pokladač (&eDeployer&r) skládá jídla.",
            "Mody &bCreate Confectionery&r (sladkosti), &bCreate Food&r (dorty, koblihy), &bCreate Cafe&r (káva, bubble tea), &bCreate: Winery&r (víno) a &bSlice & Dice&r (krájení) přidávají hlavně recepty pro stroje.",
            "&bCreate: Central Kitchen&r propojí stroje Create s kuchyní Farmer's Delight. Začni v kapitole &bCreate&r – potřebuješ míchačku, lis a dávkovač."]),
        Q("dough", "Těsto", dep=["start", "create:millstone"], items=[("create:dough", 8)], xp=15, d=[
            "Mlýnský kámen (&eMillstone&r) semele pšenici na mouku (&eWheat Flour&r).",
            "Mouka a voda v míchačce dají těsto (&eDough&r). Stačí i mouku poslat větrákem přes vodu (praní)."]),
        Q("chocolate", "Čokoláda", dep=["start", "create:mixer", "create:burner"], items=[("create:bar_of_chocolate", 4)], xp=20, d=[
            "Tekutou čokoládu namícháš v míchačce s ohřevem (pod tyglíkem zapálený ohňohořák): cukr, kakaové boby a mléko.",
            "Lis nad tyglíkem s čokoládou z ní vylisuje tabulky (&eBar of Chocolate&r)."]),

        # ---------------- Create Confectionery ----------------
        Q("cocoa", "Drcené kakao", dep=["start", "create:press"], items=[("create_confectionery:crushed_cocoa", 4)], xp=15, d=[
            "&bCreate Confectionery&r přidává čokolády, karamel, marshmallow a perník.",
            "Mechanický lis rozdrtí kakaové boby na drcené kakao (&eCrushed Cocoa&r)."]),
        Q("cocoa_butter", "Kakaový prášek a máslo", dep=["cocoa", "create:crushing"], items=[("create_confectionery:cocoa_powder", 2), ("create_confectionery:cocoa_butter", 1)], xp=20, d=[
            "Drtící kola (&eCrushing Wheel&r) rozemelou drcené kakao na kakaový prášek (&eCocoa Powder&r) a se šancí 75 % i kakaové máslo (&eCocoa Butter&r).",
            "Kakaové máslo je základ hořké a bílé čokolády."]),
        Q("confectionery", "Marshmallow a karamel", dep=["chocolate"], items=[("create_confectionery:marshmallow", 4), ("create_confectionery:bar_of_caramel", 1)], xp=25,
          shape="hexagon", size=1.5, s="Pokročilý", d=[
            "Teď už vyrábíš sladkosti v celých linkách. Marshmallow (&eMarshmallow&r) namícháš s ohřevem: 2 cukry, sliz a voda. Z jednoho míchání je jich 8.",
            "Tekutý karamel je ze 2 cukrů a vody (taky s ohřevem). Lis nad tyglíkem z něj udělá tabulku (&eBar of Caramel&r)."]),
        Q("darkchoc", "Hořká a bílá", dep=["cocoa_butter", "confectionery"], items=[("create_confectionery:bar_of_black_chocolate", 1), ("create_confectionery:bar_of_white_chocolate", 1)], xp=25, d=[
            "Hořká čokoláda: cukr, kakaové máslo, 2 kakaové boby a mléko. Bílá: cukr, kakaové máslo a mléko. Obě s ohřevem.",
            "Tabulky z nich vylisuješ stejně jako mléčnou čokoládu."]),
        Q("candy", "Bonbony", dep=["confectionery", "create:spout"], items=[("create_confectionery:chocolate_candy", 4)], xp=25, d=[
            "Dávkovač naleje na karamelovou tabulku čokoládu – vznikne čokoládový bonbon (&eChocolate Candy&r).",
            "Stejně poleješ čokoládou marshmallow nebo bobule. Vyzkoušej i hořkou, bílou a rubínovou čokoládu."]),
        Q("hotchoc", "Horká čokoláda", dep=["cocoa_butter", "create:spout"], items=[("create_confectionery:hot_chocolate_bottle", 1)], xp=25, d=[
            "Horkou čokoládu namícháš s ohřevem z cukru, 2 kakaových prášků a mléka.",
            "Dávkovač ji naleje do skleněné lahve. Když k ní na pracovním stole přidáš marshmallow, vznikne uklidňující čokoláda (&eSoothing Hot Chocolate&r)."]),
        Q("gingerbread", "Perníček", dep=["candy"], items=[("create_confectionery:gingerbread_man", 1)], xp=35, d=[
            "Perníkové těsto (&eGingerdough&r) namícháš z cukru, pšeničné mouky, škvárové mouky (&eCinder Flour&r) a medu.",
            "Škvárová mouka je rozemletý netherrack. Lis z těsta vylisuje perníčka (&eGingerbread Man&r)."]),
        Q("ruby", "Rubínová čokoláda", dep=["darkchoc"], items=[("create_confectionery:bar_of_ruby_chocolate", 1)], xp=60,
          shape="hexagon", size=1.5, s="Expert", d=[
            "Nejvzácnější čokoláda. Do míchačky s ohřevem dej cukr, kakaové boby, mléko a dračí dech.",
            "Dračí dech nabereš do lahví u bosse &eEnder Dragon&r v Endu."]),

        # ---------------- Create Food ----------------
        Q("createfood", "Cukrářský sáček", dep=["start"], items=[("createfood:piping_bag", 1)], xp=15, d=[
            "&bCreate Food&r přidává stovky jídel: dorty, koblihy, zmrzliny, pizzy, hamburgery…",
            "Cukrářský sáček (&eEmpty Piping Bag&r) vyrobíš z měděného nugetu, papíru a provázku. Plní se polevou a zdobí se jím dorty."]),
        Q("cream", "Smetana", dep=["createfood", "create:mixer"], items=[("createfood:heavy_cream_bucket", 1)], xp=20, d=[
            "Míchačka rozdělí mléko na smetanu (&eHeavy Cream&r) a odtučněné mléko. Z kbelíku mléka je čtvrtina smetany.",
            "Smetanu potřebuješ na polevu a z ní se dělá i máslo (smetana a sůl)."]),
        Q("frosting", "Poleva", dep=["cream", "create:spout"], items=[("createfood:cream_frosting_piping_bag", 1)], xp=25, d=[
            "Smetanovou polevu namícháš ze smetany, 2 cukrů a 2 kusů másla.",
            "Dávkovač polevou naplní prázdný cukrářský sáček – vznikne sáček s polevou (&ePiping Bag&r)."]),
        Q("fcake", "Dort ze stroje", dep=["frosting"], items=[("createfood:cream_cake", 1)], xp=30, d=[
            "Těsto na dort namícháš z mléka, cukru, mouky, vejce a másla. Kbelík těsta upeč v peci – vznikne korpus (&eCake Base&r).",
            "Dávkovač naleje polevu přímo na korpus a dort (&eCake&r) je hotový. Jde to i na pracovním stole se sáčkem polevy."]),
        Q("donut", "Kobliha", dep=["frosting", "create:burner"], items=[("createfood:cream_donut", 1)], xp=40, d=[
            "Rostlinný olej vylisuješ lisem s ohřevem z mrkve, brambory a další zeleniny.",
            "Těsto na koblihy (&ePastry Base&r) je upečené sladké těsto s máslem. V míchačce s ohřevem ho usmažíš v oleji na korpus koblihy (&eDonut Base&r).",
            "Dávkovač ho poleje polevou – a máš koblihu (&eDonut&r)."]),

        # ---------------- Create Cafe ----------------
        Q("beans", "Pražená káva", dep=["start"], items=[("createcafe:roasted_coffee_beans", 4)], xp=15, d=[
            "&bCreate Cafe&r přidává kávu, ledovou kávu a bubble tea.",
            "Kávová zrna (&eCoffee Beans&r) občas vypadnou z trávy (bez nůžek). Opraž je v udírně."]),
        Q("cafe", "Káva ze stroje", dep=["beans", "create:millstone", "create:burner"], items=[("createcafe:coffee_bucket", 1)], xp=25, d=[
            "Mlýnský kámen nebo drtící kola semelou pražená zrna na mletou kávu (&eCoffee Grounds&r).",
            "V míchačce s ohřevem smíchej mletou kávu s vodou. Tekutou kávu nabereš kbelíkem z tyglíku nebo nádrže."]),
        Q("iced", "Ledová káva", dep=["cafe", "create:spout", "create:deployer"], items=[("createcafe:iced_coffee", 1)], xp=30, d=[
            "Kelímek (&eIced Coffee Cup&r) vyrobíš ze skla a desky z leštěného vápence.",
            "Pokladač do něj vloží led, dávkovač dolije kávu – a ledová káva (&eIced Coffee&r) je hotová."]),
        Q("boba", "Tapiokové perly", dep=["start", "create:press", "create:burner"], items=[("createcafe:boba", 4)], xp=30, d=[
            "Semínka manioku (&eCassava Seeds&r) padají z trávy. Zasaď je a sklízej kořeny (&eCassava Root&r).",
            "Kořeny rozemel na tapiokovou mouku. Lis ze 4 mouk udělá syrové perly a míchačka s ohřevem je uvaří v rozpuštěném cukru (&eBoba&r).",
            "Rozpuštěný cukr získáš, když v míchačce s ohřevem roztavíš cukr."]),
        Q("milktea", "Bubble tea", dep=["boba", "create:spout", "create:deployer"], items=[("createcafe:apple_milk_tea", 1)], xp=40, d=[
            "Kelímek (&eEmpty Boba Cup&r) je ze skla a desky z leštěného dioritu. Pokladač do něj vloží perly.",
            "Ovocný čaj namícháš s ohřevem z ovoce, mléka a rozpuštěného cukru. Dávkovač ho naleje do kelímku – třeba jablečný (&eApple Milk Tea&r)."]),
        Q("oreo", "Sušenka na lince", dep=["milktea", "create:precision"], items=[("createcafe:oreo", 4)], xp=60,
          shape="hexagon", size=1.5, s="Expert", d=[
            "Tohle je sekvenční montáž (&eSequenced Assembly&r): sušenka jede po pásu několika stroji za sebou.",
            "Těsto z mouky, kakaa a vody slisuj a upeč v udírně. Pak dávkovač přidá krém (rozpuštěný cukr + voda v míchačce) a pokladač přiloží druhou půlku. Výsledek: &eOreo&r.",
            "&aTip:&r Celý postup ukáže JEI u &eOreo&r."]),

        # ---------------- Create: Winery ----------------
        Q("pomace", "Hroznová drť", dep=["start", "create:press"], items=[("create_winery:red_grape_pomace", 2)], xp=15, d=[
            "&bCreate: Winery&r má vlastní hrozny (&eRed Grapes&r, &eWhite Grapes&r). Keře rostou na pláních, loukách a v lesích.",
            "Lis nad tyglíkem slisuje 3 hrozny na drť (&eRed Grape Pomace&r). Ze 3 jablek je jablečný mošt."]),
        Q("winery", "Vinný sklep", dep=["pomace"], items=[("create_winery:wine_cellar", 1)], xp=25, d=[
            "Vinný sklep (&eWine Cellar&r) vyrobíš z prken, dřevěné desky a železných ingotů (nebo andezitové slitiny).",
            "Vlož do něj drť a nech ji zrát. Z drti se stane víno."]),
        Q("merlot", "Merlot", dep=["winery"], items=[("create_winery:merlot", 1)], xp=25, d=[
            "Z červené drti dozraje třeba &eMerlot&r, z bílé &eChardonnay&r, z moštu cider.",
            "&cPozor:&r Víno většinou dává zpomalení a odolnost, někdy i nevolnost."]),
        Q("rose", "Růžové víno", dep=["merlot"], items=[("create_winery:rose", 1)], xp=30, d=[
            "Růžové víno (&eRosé&r) zraje ze dvou druhů drti najednou: červené a bílé.",
            "Hroznový džus bez zrání namícháš v míchačce z drti a cukru."]),

        # ---------------- Central Kitchen ----------------
        Q("ck_heat", "Automatická kuchyně", dep=["start", "create:burner", "create:arm", "farmers_delight:pot"], items=[("farmersdelight:pumpkin_soup", 2)], xp=35, d=[
            "&bCreate: Central Kitchen&r propojí Create s kuchyní Farmer's Delight.",
            "Ohňohořák (&eBlaze Burner&r) funguje jako zdroj tepla pro hrnec. Mechanická paže (&eMechanical Arm&r) do hrnce vkládá misky a hotové jídlo vybírá (umí to i trychtýř).",
            "Zkus si tak automaticky uvařit dýňovou polévku (&ePumpkin Soup&r)."]),
        Q("ck_cut", "Krájení stroji", dep=["start", "create:deployer", "farmers_delight:knife"], items=[("farmersdelight:salmon_slice", 8)], xp=30, d=[
            "Pokladač s nožem v ruce (režim použití) krájí suroviny na krájecím prkénku. Mechanická paže na prkénko suroviny přikládá.",
            "Krájet umí i mechanická pila. Nakrájej tak lososa na plátky (&eRaw Salmon Slice&r)."]),

        # ---------------- Slice & Dice ----------------
        Q("slicer", "Kráječ", dep=["start", "create:press"], items=[("sliceanddice:slicer", 1)], xp=25, d=[
            "&bSlice & Dice&r přidává kráječ (&eSlicer&r) – vyrobíš ho z ozubeného kola, andezitového pláště a otočného stolu.",
            "Postav ho nad pás, odkládací desku (&eDepot&r) nebo tyglík a pravým tlačítkem do něj vlož nůž nebo sekeru. Pak krájí jídlo podle receptů krájecího prkénka."]),
        Q("sprinkler", "Postřikovač", dep=["slicer", "create:fluids"], items=[("sliceanddice:sprinkler", 1)], xp=20, d=[
            "Postřikovač (&eSprinkler&r) dej pod potrubí a pusť do něj tekutinu.",
            "S vodou zalévá okolí, jako by pršelo. Jiné tekutiny působí jinak – třeba lektvar zasáhne tvory pod ním."]),
        Q("fertilizer", "Tekuté hnojivo", dep=["sprinkler", "create:mixer"], items=[("sliceanddice:fertilizer_bucket", 1)], xp=40,
          shape="hexagon", size=1.5, s="Expert", d=[
            "Tekuté hnojivo (&eLiquid Fertilizer&r) namícháš v míchačce ze stromového hnojiva (&eTree Fertilizer&r) a vody.",
            "Pusť ho potrubím do postřikovačů nad polem. Plodiny pod nimi rostou jako po kostní moučce – úplně bez práce."]),

        # ---------------- Spice of Life ----------------
        Q("diet", "Pestrá strava", dep=["start"], items=[("solonion:lunchbag", 1)], xp=30, d=[
            "Čím víc různých jídel sníš, tím víc srdíček máš. Stroje ti pomůžou vyrábět pestré menu.",
            "Do svačinového pytlíku (&eLunchbag&r) si dej různá jídla a nos je s sebou. Vyrobíš ho z papíru."]),
    ],
)

# =====================================================================
#  RYBAŘENÍ
# =====================================================================
FISHING = dict(
    key="fishing", group="food", title="Rybaření",
    subtitle="Aquaculture 2, Fish of Thieves a Unusual Fish", icon="aquaculture:iron_fishing_rod",
    quests=[
        Q("intro", "Na ryby!", icon="minecraft:fishing_rod", tasks=[auto()], xp=10,
          shape="hexagon", size=1.5, s="Začátečník", d=[
            "&bAquaculture 2&r přidává desítky ryb, lepší pruty, háčky, návnady a poklady. Každý biom (řeka, oceán, bažina, džungle…) má jiné ryby.",
            "&bFish of Thieves&r přidává ryby ze hry Sea of Thieves a &bUnusual Fish&r podivné mořské tvory.",
            "Začni obyčejným prutem a pak si vyrob železný."]),
        Q("rod", "Lepší prut", dep=["intro"], items=[("aquaculture:iron_fishing_rod", 1)], xp=15, d=[
            "Železný prut (&eIron Fishing Rod&r) vydrží déle než dřevěný. Vyrobíš ho ze železa, klacků a provázku.",
            "Pruty z Aquaculture se úplně nerozbijí. Opotřebovaný prut jen přestane fungovat, dokud ho neopravíš."]),
        Q("tackle", "Rybářská krabička", dep=["rod"], items=[("aquaculture:tackle_box", 1)], xp=15, d=[
            "Rybářská krabička (&eTackle Box&r) je úložiště i dílna na prut.",
            "Polož ji, otevři a vlož do ní prut. Pak mu přidáš háček, návnadu, vlasec a splávek."]),
        Q("worm_farm", "Farma na červy", dep=["rod"], items=[("aquaculture:worm_farm", 1)], xp=15, d=[
            "Farma na červy (&eWorm Farm&r) funguje jako kompostér. Házej do ní rostlinný odpad.",
            "Když je plná, vybereš z ní červa."]),
        Q("worm", "Návnada", dep=["worm_farm", "tackle"], items=[("aquaculture:worm", 4)], xp=10, d=[
            "Návnadu dej na prut v rybářské krabičce. Ryba pak zabere dřív.",
            "Návnadou jsou červ (&eWorm&r), pijavice (&eLeech&r) a střevle (&eMinnow&r). Pijavice a střevle občas chytíš na prut."]),
        Q("line", "Vlasec a splávek", dep=["tackle"], items=[("aquaculture:fishing_line", 1), ("aquaculture:bobber", 1)], xp=15, d=[
            "Vlasec (&eFishing Line&r) je z provázků a železného ingotu. Splávek (&eBobber&r) z hlíny a ulity nautila.",
            "Obojí jde do prutu v rybářské krabičce."]),
        Q("hooks", "Háčky", dep=["tackle"], items=[("aquaculture:iron_hook", 1), ("aquaculture:gold_hook", 1)], xp=20, d=[
            "Háček mění, jak prut funguje. Železný (&eIron Hook&r) šetří prut, zlatý (&eGold Hook&r) přidá štěstí – chytíš víc pokladů.",
            "Lehký háček nahodí dál, těžký blíž, redstonový ti dá víc času na zaseknutí a hudební (&eNote Hook&r) zahraje tón, když ryba zabere.",
            "Ze dvou železných háčků vyrobíš dvojitý (&eDouble Hook&r) – občas chytíš dvě věci najednou."]),
        Q("filletknife", "Filetovací nůž", dep=["rod"], items=[("aquaculture:iron_fillet_knife", 1)], xp=15, d=[
            "Filetovací nůž (&eIron Fillet Knife&r) je nástroj i zbraň.",
            "Dej ho na pracovní stůl spolu s rybou z Aquaculture a dostaneš filety. Funguje i jiný nůž."]),
        Q("knife", "Rybí filety", dep=["filletknife"], items=[("aquaculture:fish_fillet_raw", 4)], xp=15, d=[
            "Každý druh ryby dá jiný počet filetů (&eRaw Fish Fillet&r). Upečené filety dobře zasytí.",
            "Ryby z Aquaculture mají i váhu. Opravdu velký úlovek si můžeš vystavit na stěnu (&eOak Fish Mount&r)."]),
        Q("sushi", "Sushi", dep=["knife"], items=[("aquaculture:sushi", 1)], xp=20, d=[
            "Sushi (&eSushi&r) vyrobíš z filetu a mořské trávy.",
            "Mořskou trávu natrháš nůžkami pod vodou nebo ji občas vytáhneš prutem."]),
        Q("aquadelight", "Ryba s hranolky", dep=["knife", "farmers_delight:pot"], items=[("aquaculturedelight:fish_and_chips", 1)], xp=20, d=[
            "&bAquaculture Delight&r přidává rybí jídla do hrnce z Farmer's Delight.",
            "Ryba s hranolky (&eFish and Chips&r) je ze smaženého okouna, pečené brambory, rajčatové omáčky a misky. Smaženého okouna uvaříš v hrnci z okounka (&eSmallmouth Bass&r), pšenice a vejce."]),
        Q("treasure", "Poklad z hlubin", dep=["hooks"], items=[("aquaculture:treasure_chest", 1)], xp=40, d=[
            "Prut občas vytáhne místo ryby bednu: krabici (&eBox&r), schránku (&eLockbox&r) nebo truhlu s pokladem (&eTreasure Chest&r).",
            "Pravým tlačítkem ji otevřeš. V truhle s pokladem jsou železo, zlato, smaragdy i diamanty.",
            "&aTip:&r Zlatý háček a očarování Štěstí moří zvyšují šanci na poklad."]),
        Q("driftwood", "Naplavené dřevo", dep=["intro"], items=[("upgrade_aquatic:driftwood", 4)], xp=15, d=[
            "&bUpgrade Aquatic&r přidává nové mořské tvory, korály a naplavené dřevo.",
            "Kmeny naplaveného dřeva leží na plážích, u řek, v bažinách a v oceánech. Ze 4 kmenů vyrobíš 3 bloky dřeva (&eDriftwood&r)."]),
        Q("diamond_rod", "Diamantový prut", dep=["treasure"], items=[("aquaculture:diamond_fishing_rod", 1)], xp=40,
          shape="hexagon", size=1.5, s="Pokročilý", d=[
            "Teď už nechytáš jen na večeři, ale na poklady. Diamantový prut (&eDiamond Fishing Rod&r) vydrží nejdéle ze všech běžných prutů.",
            "Kombinuj ho se zlatým háčkem a dobrou návnadou."]),
        Q("neptunium", "Neptunium", dep=["diamond_rod"], items=[("aquaculture:neptunium_ingot", 1)], xp=60, d=[
            "Neptunium je vzácný kov z moře. Při rybaření občas vytáhneš neptuniový nuget (&eNeptunium Nugget&r) – 9 nugetů dá ingot.",
            "Vzácně vytáhneš i Neptunovu truhlu (&eNeptune's Bounty&r) s hotovou neptuniovou výbavou."]),
        Q("nep_gear", "Neptunova zbroj", dep=["neptunium"], items=[("aquaculture:neptunium_chestplate", 1)], xp=60, d=[
            "Neptuniové brnění má podvodní schopnosti: helma lepší vidění, hrudní plát dýchání pod vodou, kalhoty tě pod vodou nadnášejí a boty zrychlí plavání.",
            "Neptuniové nástroje se pod vodou nezpomalují a meč i sekera tam dávají víc zranění."]),
        Q("nep_rod", "Neptunův prut", dep=["neptunium"], items=[("aquaculture:neptunium_fishing_rod", 1)], xp=80,
          shape="hexagon", size=1.5, s="Expert", d=[
            "Nejlepší prut (&eNeptunium Fishing Rod&r). Ryby na něj berou dřív.",
            "Vyrobíš ho z neptuniových ingotů, klacků a provázku."]),
        Q("star_hook", "Hvězdný háček", dep=["nep_rod"], items=[("aquaculture:nether_star_hook", 1)], xp=100, d=[
            "Nejlepší háček (&eNether Star Hook&r): šetří prut jako diamantový a přidává štěstí.",
            "Vyrobíš ho z diamantového háčku a netherové hvězdy (padá z Withera)."]),

        # ---------------- Fish of Thieves ----------------
        Q("earthworms", "Žížaly", dep=["intro"], items=[("fishofthieves:earthworms", 2)], xp=10, d=[
            "Žížaly (&eEarthworms&r) občas vypadnou, když kopeš hlínu nebo trávu (ne u vody). Larvy (&eGrubs&r) najdeš v písku. Pijavice (&eLeeches&r) najdeš v písku nebo bahně u vody na plážích a u řek.",
            "Jsou to návnady na ryby z &bFish of Thieves&r."]),
        Q("splashtail", "Fish of Thieves", dep=["earthworms"], items=[("fishofthieves:splashtail", 1)], xp=15, d=[
            "&bFish of Thieves&r přidává 10 druhů ryb ze hry Sea of Thieves. Každý má několik barevných variant podle biomu, času a počasí.",
            "Ryby plavou ve vodě. Chytíš je do kbelíku s vodou nebo ulovíš. Splashtail (&eRaw Splashtail&r) žije v oceánech."]),
        Q("pondie", "Pondie", dep=["splashtail"], items=[("fishofthieves:pondie", 1)], xp=15, d=[
            "Pondie (&eRaw Pondie&r) žije v řekách a v lesních biomech."]),
        Q("plentifin", "Plentifin", dep=["splashtail"], items=[("fishofthieves:plentifin", 1)], xp=20, d=[
            "Plentifin (&eRaw Plentifin&r) žije v biomech &eWarm Ocean&r, &eLukewarm Ocean&r, &eLush Caves&r a &eDripstone Caves&r."]),
        Q("shoal", "Hejno", dep=["splashtail"], icon="fishofthieves:wildsplash", tasks=[adv("fishofthieves:shoal_hunter")], xp=25, d=[
            "Na hladině oceánů, řek a bažin se občas objeví hejno ryb (&eShoal&r).",
            "Nahoď do něj prut a lov tak dlouho, dokud hejno nezmizí."]),
        Q("ancientscale", "Ancientscale", dep=["plentifin"], items=[("fishofthieves:ancientscale", 1)], xp=30, d=[
            "Ancientscale (&eRaw Ancientscale&r) žije u staveb &eOcean Ruins&r, v biomu &eLukewarm Ocean&r a v jeskyních."]),
        Q("wrecker", "Wrecker", dep=["splashtail"], items=[("fishofthieves:wrecker", 1)], xp=40, d=[
            "Wreckery (&eRaw Wrecker&r) žijí u staveb &eShipwreck&r a u zatopených staveb &eRuined Portal&r.",
            "Najdi takovou stavbu a pátrej ve vodě kolem ní."]),
        Q("stormfish", "Stormfish", dep=["wrecker"], items=[("fishofthieves:stormfish", 1)], xp=40,
          shape="hexagon", size=1.5, s="Pokročilý", d=[
            "Stormfish (&eRaw Stormfish&r) se objevuje hlavně v oceánech a jen za deště nebo bouřky. Když prší, vyraz k moři.",
            "Teď už chytáš ryby, které mají zvláštní podmínky – sleduj počasí a stavby."]),
        Q("battlegill", "Battlegill", dep=["stormfish"], items=[("fishofthieves:battlegill", 1)], xp=50, d=[
            "Battlegill (&eRaw Battlegill&r) žije u staveb &eOcean Monument&r, &ePillager Outpost&r a &eTrial Chambers&r.",
            "&cPozor:&r U stavby &eOcean Monument&r číhají strážci."]),
        Q("devilfish", "Devilfish", dep=["stormfish"], items=[("fishofthieves:devilfish", 1)], xp=50, d=[
            "Devilfish (&eRaw Devilfish&r) žije jen hluboko pod zemí ve vodě v jeskyních. Nežije v biomech &eLush Caves&r ani &eDeep Dark&r."]),
        Q("fot_master", "Sběratel ryb", dep=["battlegill", "devilfish", "ancientscale", "pondie", "shoal"], icon="fishofthieves:stormfish_bucket",
          tasks=[adv("fishofthieves:fish_collectors")], xp=100, shape="hexagon", size=1.5, s="Expert", d=[
            "Chyť do kbelíku všech 10 druhů ryb z &bFish of Thieves&r: splashtail, pondie, islehopper, ancientscale, plentifin, wildsplash, devilfish, battlegill, wrecker a stormfish.",
            "Wildsplash žije v oceánech, na plážích, v džungli a v biomu &eLush Caves&r."]),

        # ---------------- Unusual Fish ----------------
        Q("unusual_fish", "Podivné ryby", dep=["intro"], items=[("unusualfishmod:cooked_unusual_fillet", 2)], xp=20, d=[
            "&bUnusual Fish&r přidává podivné vodní tvory. Každý žije jinde: v biomech &eWarm Ocean&r a &eDeep Ocean&r, v bažinách, řekách, džungli i v jeskyních.",
            "Když podivnou rybu ulovíš, upeč ji. Dostaneš podivný filet (&eCooked Unusual Fillet&r)."]),
        Q("unusual", "Humří rohlík", dep=["unusual_fish"], items=[("unusualfishmod:lobster_roll", 1)], xp=30, d=[
            "Humr &ePorcupine Lobster&r žije v biomu &eDeep Lukewarm Ocean&r. Když ho ulovíš, upustí syrový humří ocas a ostny.",
            "Ocas upeč a dej ho na pracovní stůl spolu s chlebem – vznikne humří rohlík (&eLobster Roll&r)."]),
        Q("spear", "Prizmarínové kopí", dep=["unusual"], items=[("unusualfishmod:prismarine_spear", 1)], xp=40, d=[
            "Prizmarínové kopí (&ePrismarine Spear&r) vyrobíš z humřích ostnů (&eLobster Spike&r) a prizmarínových střepů.",
            "Střepy padají ze strážců ve stavbě &eOcean Monument&r."]),
    ],
)

# Pořadí kapitol této oblasti v knize questů
CHAPTERS = [LETSDO, DRINKS, CREATEFOOD, FISHING]

# Předměty bez receptu/loot table v indexu, které se ale dají získat (ověřeno v datech modů)
NO_RECIPE = {
    "bakery:strawberry_cake": "Caking Station: Cake Dough položené na stůl + Strawberry Jam (bakery:blank_cake_interaction/strawberry_cake), dort se vezme pravým tlačítkem",
    "vinery:red_grapejuice": "Grapevine Pot: 6 červených hroznů, rozšlapat skákáním, nabrat do vinery:wine_bottle (GrapevinePotBlock)",
    "create_confectionery:marshmallow": "create:mixing heated: 2x cukr, sliz, 250 mB vody (marshmallow_recipe.json)",
    "create_confectionery:hot_chocolate_bottle": "create:filling: skleněná lahev + 250 mB hot_chocolate (hot_chocolate_bottle_recipe.json)",
    "create_confectionery:crushed_cocoa": "create:pressing kakaových bobů (crushed_cocoa_recipe.json)",
    "create_confectionery:cocoa_powder": "create:crushing drceného kakaa (cocoa_powder_and_butter_recipe.json)",
    "create_confectionery:cocoa_butter": "create:crushing drceného kakaa, šance 75 % (cocoa_powder_and_butter_recipe.json)",
    "create_confectionery:chocolate_candy": "create:filling: bar_of_caramel + 250 mB create:chocolate (chocolate_candy_recipe.json)",
    "create_confectionery:gingerbread_man": "create:pressing gingerdough (gingerbread_man_recipe.json)",
    "createcafe:coffee_bucket": "tekutina createcafe:coffee z create:mixing (heated, coffee_grounds + voda), nabrat kbelíkem",
    "aquaculture:worm": "Worm Farm (WormFarmBlock = kompostér, výstup AquaItems.WORM)",
    "aquaculture:fish_fillet_raw": "aquaculture:crafting_special_fish_fillet: ryba + nůž (tag c:tools/knife)",
    "sliceanddice:fertilizer_bucket": "tekutina sliceanddice:fertilizer z create:mixing (tree_fertilizer + voda), nabrat kbelíkem",
    "farmersdelight:salmon_slice": "farmersdelight:cutting minecraft:salmon + nůž (cutting/salmon.json); Central Kitchen: pokladač s nožem / mechanická pila",
}

# Přeložená vlastní jména (regex bez ohledu na velikost písmen -> anglický název ze hry)
PROPER_NAMES_CZ = {
    r"biom\w* louk": "Meadow",
    r"huňat\w* kr[aá]v": "Highland Cattle",
    r"vodn\w* buvol": "Water Buffalo",
    r"zakopan\w* poklad": "Buried Treasure",
    r"vrak\w* lod": "Shipwreck",
    r"podmořsk\w* ruin": "Ocean Ruins",
    r"zalesněn\w* badlands": "Wooded Badlands",
    r"základn\w* nájezdník": "Pillager Outpost",
    r"stan\w* pivní\w* slavnost": "Brewfest Tent",
    r"enderdrak": "Ender Dragon",
    r"vlažn\w* oceán": "Lukewarm Ocean",
    r"bujn\w* jeskyn": "Lush Caves",
    r"zničen\w* portál": "Ruined Portal",
}
