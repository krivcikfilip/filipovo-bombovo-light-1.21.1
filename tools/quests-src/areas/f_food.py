from engine import *

# Oblast f_food: Farmer's Delight, jeho doplňky (Delight addony), ExtraDelight a Pam's HarvestCraft 2.
# Všechna fakta ověřena v jarech/datech (recepty, loot tabulky, lang, bytecode) – viz závěrečná zpráva.

MS = dict(shape="hexagon", size=1.5)  # milník (přechod mezi úrovněmi)

FARMERS = dict(
    key="farmers_delight", group="food", title="Farmer's Delight",
    subtitle="Skutečné vaření: nůž, prkénko, hrnec a hostiny", icon="farmersdelight:cooking_pot",
    quests=[
        # ---------- Začátečník ----------
        Q("start", "Farmer's Delight", icon="farmersdelight:cooking_pot", tasks=[auto()], xp=10, s="Začátečník", **MS, d=[
            "&bFarmer's Delight&r je základ skoro všech jídelních modů v packu. Přidává nové plodiny, nůž, prkénko, hrnec a stovky jídel.",
            "V téhle kapitole se naučíš sbírat plodiny, krájet, vařit v hrnci a nakonec připravit hostiny pro celý tým.",
            "&aTip:&r Recept na každé jídlo najdeš v JEI. Najeď myší na předmět a zmáčkni R (recept) nebo U (k čemu se hodí).",
            "&aTip:&r Hodně receptů v packu mění doplňky (hlavně &bCreate Food&r a &bExtraDelight&r). Když se recept liší od popisu, věř JEI.",
        ]),
        Q("knife", "Pazourkový nůž", dep=["start"], items=[("farmersdelight:flint_knife", 1)], xp=10, d=[
            "Nůž (&eFlint Knife&r) je hlavní nástroj kuchaře. Vyrobíš ho z pazourku nad klackem.",
            "Nožem sklízíš slámu z trávy a obilí. Zvíře zabité nožem má šanci pustit i něco navíc, třeba šunku z prasete.",
            "&aTip:&r Nůž je i rychlá zbraň. Lepší nože vyrobíš ze železa, zlata nebo diamantu.",
        ]),
        Q("straw", "Sláma", dep=["knife"], items=[("farmersdelight:straw", 8)], xp=15, d=[
            "Sláma (&eStraw&r) je suché vlákno. Vyrábí se z ní lano, plátno a kompost.",
            "Vezmi nůž do ruky a rozbíjej jím trávu nebo zralou pšenici a rýži. Ze zralého obilí padá sláma vždy, z trávy jen občas.",
            "&aTip:&r Devět kusů slámy složíš do balíku slámy (&eStraw Bale&r) a zase zpátky.",
        ]),
        Q("rope", "Lano", dep=["straw"], items=[("farmersdelight:rope", 8)], xp=15, d=[
            "Lano (&eRope&r) vyrobíš ze dvou kusů slámy nad sebou. Dostaneš 4 kusy.",
            "Po laně se dá šplhat. Rajčata po něm rostou do výšky.",
            "&aTip:&r Ze 4 lan uděláš záchrannou síť (&eSafety Net&r), která tlumí pád.",
        ]),
        Q("canvas", "Plátno", dep=["straw"], items=[("farmersdelight:canvas", 2)], xp=10, optional=True, d=[
            "Plátno (&eCanvas&r) vyrobíš ze 4 kusů slámy (čtverec 2×2).",
            "Z plátna a klacků je košík (&eBasket&r). Z plátna jsou i cedule (&eCanvas Sign&r) a koberec (&eCanvas Rug&r).",
        ]),
        Q("wild", "Divoké plodiny", dep=["start"], items=[("farmersdelight:cabbage", 1), ("farmersdelight:tomato", 1), ("farmersdelight:onion", 1)], xp=20, d=[
            "Ve světě rostou divoké plodiny. Rozbij je a dostaneš plody a semínka.",
            "Divoké zelí (&eWild Cabbage&r) a řepa rostou na plážích. Cibule a mrkev v pláních a lesích. Rajčata (&eTomato Shrub&r) v savanách a pouštích. Brambory v chladných horách a tajgách.",
            "&aTip:&r Plodiny a semínka najdeš občas i v truhlách.",
        ]),
        Q("garden", "Vlastní záhon", dep=["wild"], items=[("farmersdelight:cabbage_seeds", 2), ("farmersdelight:tomato_seeds", 2)], xp=15, d=[
            "Semínka zelí (&eCabbage Seeds&r) a rajčat (&eTomato Seeds&r) zasaď na pole zorané motykou. Cibuli zasadíš celou, jako mrkev.",
            "Semínka padají z divokých plodin. Zelí a rajčata je dávají i při běžné sklizni.",
            "&aTip:&r Zelí nakrájené nožem na prkénku dá dva listy (&eCabbage Leaf&r).",
        ]),
        Q("rice", "Rýže", dep=["wild"], items=[("farmersdelight:rice", 4)], xp=15, d=[
            "Divoká rýže (&eWild Rice&r) roste v mělké vodě v bažinách a džunglích.",
            "Rýži zasaď do mělké vody. Nad hladinou vyroste lata (&eRice Panicle&r).",
            "&aTip:&r Latu nakrájej nožem na prkénku. Dostaneš rýži a slámu.",
        ]),
        Q("tomato_rope", "Rajčata na laně", dep=["garden", "rope"], tasks=[adv("farmersdelight:main/harvest_ropelogged_tomato")], icon="farmersdelight:tomato", xp=20, d=[
            "Rajčata umí růst do výšky, když nad nimi visí lano.",
            "Zasaď rajčata a přímo nad ně dej lano. Keř po laně vyleze nahoru a sklidíš z něj víc rajčat.",
            "Zralá rajčata utrhneš pravým tlačítkem. Quest se splní, až sklidíš rajčata z keře na laně.",
        ]),
        Q("board", "Prkénko", dep=["knife"], items=[("farmersdelight:cutting_board", 1)], xp=15, d=[
            "Prkénko (&eCutting Board&r) slouží ke krájení. Vyrobíš ho z prken a klacků.",
            "Polož prkénko, dej na něj surovinu (pravé tlačítko) a klikni na ni nožem. Kousky vyskočí ven.",
            "&aTip:&r Sekerou nebo lopatou se na prkénku zpracují jiné věci. Všechny recepty ukáže JEI.",
        ]),
        Q("cut_meat", "Krájení masa", dep=["board"], items=[("farmersdelight:minced_beef", 2), ("farmersdelight:bacon", 2)], xp=15, d=[
            "Syrová vepřová kotleta nakrájená nožem na prkénku dá 2 slaniny (&eRaw Bacon&r). Kuře, ryby a skopové se taky rozkrájí na menší kousky do receptů.",
            "Mleté maso (&eMinced Beef&r) je v tomto packu na 3 kroky. Syrové hovězí dej na pracovní stůl a dostaneš mleté hovězí (&eGround Beef&r).",
            "Mleté hovězí nakrájej nožem na prkénku na 2 masové kuličky (&eRaw Beef Meatball&r). Každou kuličku dej na pracovní stůl a vznikne &eMinced Beef&r.",
            "&aTip:&r Mleté maso upeč v peci, udírně nebo na táboráku a máš karbanátek (&eBeef Patty&r).",
        ]),
        Q("bark", "Kůra ze stromů", dep=["board"], items=[("farmersdelight:tree_bark", 4)], xp=10, d=[
            "Polož na prkénko kmen a klikni na něj sekerou. Dostaneš oloupaný kmen a kůru (&eTree Bark&r).",
            "Kůra se hodí do organického kompostu. Dá se z ní udělat i papír.",
        ]),
        Q("iron_knife", "Lepší nůž", dep=["knife"], items=[("farmersdelight:iron_knife", 1)], xp=15, optional=True, d=[
            "Železný nůž (&eIron Knife&r) vydrží déle. Vyrobíš ho stejně jako pazourkový, jen místo pazourku dáš železný ingot.",
            "Diamantový nůž (&eDiamond Knife&r) půjde později vylepšit na netheritový.",
        ]),
        Q("ham", "Šunka", dep=["knife"], items=[("farmersdelight:ham", 1)], xp=15, d=[
            "Šunka (&eHam&r) občas padá z prasat a hoglinů, ale jen když je zabiješ nožem.",
            "Šunku nakrájíš na prkénku na kotlety, nebo ji vyudíš v udírně na uzenou šunku (&eSmoked Ham&r).",
            "&aTip:&r Uzená šunka se hodí na hostinu s medem.",
        ]),
        Q("salad", "Míchaný salát", dep=["garden"], items=[("farmersdelight:mixed_salad", 1)], xp=20, d=[
            "Míchaný salát (&eMixed Salad&r) se nevaří. Slož ho na pracovním stole ze zelí, rajčete, řepy a misky.",
            "Míchaný salát dává na chvíli regeneraci. Hodí se, když potřebuješ rychle doplnit zdraví.",
        ]),
        Q("burger", "Hamburger", dep=["cut_meat", "garden", "pot"], items=[("farmersdelight:hamburger", 1)], xp=20, d=[
            "Hamburger (&eHamburger&r) slož na pracovním stole ze dvou housek (&eBun&r), pečeného masa (karbanátek nebo steak), cibule, zelí a rajčete.",
            "Housku upečeš v peci z těsta se solí (&eSalt Dough&r). To slož na pracovním stole ze 3 pšenic, soli a kbelíku vody.",
            "Sůl (&eSalt&r) uvaříš v hrnci z kbelíku vody.",
        ]),
        Q("sweets", "Melounový nanuk", dep=["start"], items=[("farmersdelight:melon_popsicle", 1)], xp=15, optional=True, d=[
            "Melounový nanuk (&eMelon Popsicle&r) slož na pracovním stole ze 4 plátků melounu, 2 ledů a klacku. Tvar ukáže JEI.",
            "&aTip:&r Sladkosti z Farmer's Delight (koláče, sušenky) se v tomto packu pečou jinak – hlavně v troubě z &bExtraDelight&r. Postup ukáže JEI.",
        ]),
        # ---------- Pokročilý ----------
        Q("stove", "Sporák", dep=["board"], items=[("farmersdelight:stove", 1)], xp=20, d=[
            "Sporák (&eStove&r) je zdroj tepla pro hrnec a pánev. Vyrobíš ho z cihel, železa a táboráku.",
            "Na sporák můžeš rovnou položit až 6 kusů syrového jídla a opéct je jako na táboráku.",
            "&cPozor:&r Hořící sporák pálí, když na něj šlápneš. Uhasíš ho lopatou nebo kbelíkem vody, zapálíš ho křesadlem.",
        ]),
        Q("pot", "Hrnec", dep=["stove"], items=[("farmersdelight:cooking_pot", 1)], xp=30, s="Pokročilý", **MS, d=[
            "Teď už nestačí péct maso na ohni. Hrnec (&eCooking Pot&r) je srdce kuchyně: vaří polévky, guláše a hlavní jídla až ze 6 surovin.",
            "Hrnec potřebuje teplo zespodu: sporák, táborák, oheň nebo magmatický blok. Mezi teplo a hrnec smíš dát i násypku.",
            "Do okna dej suroviny a do políčka pro nádobu misku (nebo jinou nádobu, kterou recept chce). Hotové jídlo si vezmi z výstupu.",
            "&aTip:&r Na hotový hrnec můžeš kliknout rovnou miskou v ruce. Rozbitý hrnec si jídlo uvnitř pamatuje.",
        ]),
        Q("skillet", "Pánev", dep=["stove"], items=[("farmersdelight:skillet", 1)], xp=20, d=[
            "Pánev (&eSkillet&r) je přenosný sporák a zároveň dobrá zbraň.",
            "Drž pánev v hlavní ruce a syrové jídlo v druhé ruce. Stoupni si k ohni nebo sporáku a drž pravé tlačítko.",
            "&aTip:&r Se Shiftem pánev položíš jako blok. Na sporáku pak smaží jako táborák.",
        ]),
        Q("skillet_use", "Smažení na pánvi", dep=["skillet"], tasks=[adv("farmersdelight:main/use_skillet")], icon="farmersdelight:fried_egg", xp=15, d=[
            "Usmaž cokoli na pánvi, kterou držíš v ruce. Quest se splní sám, jakmile se ti to povede.",
        ]),
        Q("tomato_sauce", "Rajčatová omáčka", dep=["pot", "garden"], items=[("farmersdelight:tomato_sauce", 2)], xp=20, d=[
            "Rajčatová omáčka (&eTomato Sauce&r) je základ těstovin, pizzy a mnoha dalších jídel.",
            "Uvaříš ji v hrnci ze dvou rajčat.",
        ]),
        Q("stew", "První guláš", dep=["pot"], items=[("farmersdelight:beef_stew", 1)], xp=20, d=[
            "Hovězí guláš (&eBeef Stew&r) uvaříš v hrnci ze syrového hovězího, mrkve a brambory.",
            "Jídla z hrnce dávají efekt &eNourishment&r (sytost). Dokud trvá, hlad ti neubývá. Výjimka: když tě léčí nasycení.",
            "&aTip:&r Lepší jídla dávají delší efekt. Délku vidíš v popisku jídla.",
        ]),
        Q("cooked_rice", "Vařená rýže", dep=["rice", "pot"], items=[("farmersdelight:cooked_rice", 4)], xp=15, d=[
            "Vařenou rýži (&eCooked Rice&r) uvaříš v hrnci z rýže.",
            "Je základem rolek, smažené rýže i velkých hostin.",
        ]),
        Q("pasta", "Těstoviny s kuličkami", dep=["tomato_sauce", "cut_meat"], items=[("farmersdelight:pasta_with_meatballs", 1)], xp=25, d=[
            "Syrové těstoviny (&eRaw Pasta&r) uvaříš v hrnci ze 2 pšenic a vejce. Dostaneš 4 kusy.",
            "V hrnci pak uvař těstoviny s mletým masem (&eMinced Beef&r) a rajčatovou omáčkou. Vznikne &ePasta with Meatballs&r.",
            "&aTip:&r Těstoviny dostaneš i tak, že nakrájíš těsto (&eWheat Dough&r) nožem na prkénku. Těsto se v tomto packu míchá v míse z &bExtraDelight&r.",
        ]),
        Q("drinks", "Nápoje", dep=["pot"], items=[("farmersdelight:milk_bottle", 4), ("farmersdelight:melon_juice", 1)], xp=15, optional=True, d=[
            "Z kbelíku mléka a 4 lahví vyrobíš 4 lahve mléka (&eMilk Bottle&r). Každá odstraní jeden efekt.",
            "Melounový džus (&eMelon Juice&r) slož na pracovním stole z plátku melounu, cukru a lahve. Trochu tě vyléčí.",
            "&aTip:&r Lahve mléka můžeš dávat do receptů místo celého kbelíku.",
        ]),
        Q("dogfood", "Psí žrádlo", dep=["pot", "rice"], items=[("farmersdelight:dog_food", 1)], xp=20, d=[
            "Psí žrádlo (&eDog Food&r) uvaříš v hrnci ze shnilého masa, kostní moučky, syrového masa a rýže.",
            "Nakrm jím ochočeného vlka. Na 5 minut dostane rychlost, sílu a odolnost.",
        ]),
        Q("horse_feed", "Krmivo pro koně", dep=["rice"], items=[("farmersdelight:horse_feed", 1)], xp=15, optional=True, d=[
            "Krmivo (&eHorse Feed&r) slož z balíku sena nebo balíku rýže, dvou jablek a zlaté mrkve.",
            "Nakrm jím ochočeného koně nebo jiné jezdecké zvíře. Na 5 minut bude rychlejší a skočí výš.",
        ]),
        Q("crates", "Zásoby do sklepa", dep=["garden"], items=[("farmersdelight:onion_crate", 1), ("farmersdelight:tomato_crate", 1)], xp=15, d=[
            "Bedny a pytle uloží 9 kusů jedné plodiny do jednoho bloku. Šetří místo v truhlách.",
            "Bednu cibule (&eOnion Crate&r) slož z 9 cibulí, bednu rajčat (&eTomato Crate&r) z 9 rajčat. Zpátky na plody je rozložíš na pracovním stole.",
            "&aTip:&r Stejně fungují pytel rýže (&eBag of Rice&r) a balík rýže (&eRice Bale&r).",
        ]),
        Q("cabinet", "Kuchyňská skříňka", dep=["board"], items=[("farmersdelight:oak_cabinet", 1)], xp=10, optional=True, d=[
            "Skříňka (&eCabinet&r) je úložný blok do kuchyně. Vyrobíš ji z dřevěných desek a poklopů.",
            "Uloží věci jako truhla. Existuje ve všech druzích dřeva.",
        ]),
        Q("variety", "Pestrá strava", dep=["pot"], items=[("farmersdelight:vegetable_soup", 1), ("farmersdelight:fried_rice", 1), ("farmersdelight:fruit_salad", 1), ("farmersdelight:egg_sandwich", 1)], xp=30, d=[
            "Mod &bSpice of Life: Onion&r odměňuje pestrou stravu. Pamatuje si posledních 32 snědených jídel a počítá z nich rozmanitost (&eDiversity&r).",
            "Nové a výživné jídlo rozmanitost zvedne. Když jíš pořád to samé, klesá.",
            "Bonusy (výchozí nastavení): 3 – srdce navíc, 5 – síla, 7 – regenerace, 10 – rychlost, 13 – tuhost brnění, 18 – síla II, 25 a 31 – další srdce.",
            "&cPozor:&r Po smrti se seznam snědených jídel vymaže. Rozmanitost uvidíš tlačítkem &eSOL&r v inventáři nebo v knize jídel (&eFood Book&r, z knihy a brambory).",
        ]),
        Q("appleskin", "Co ukazuje AppleSkin", dep=["variety"], items=[("farmersdelight:barbecue_stick", 1)], xp=10, optional=True, d=[
            "Mod &bAppleSkin&r ukazuje, co jídlo umí. V popisku jídla vidíš, kolik doplní hladu a nasycení.",
            "Když jídlo držíš v ruce, na liště hladu bliká, kolik ti ho doplní. Žlutý obrys na liště je nasycení: dokud ho máš, hlad neubývá.",
            "Špíz (&eBarbecue on a Stick&r) slož z rajčete, cibule, pečeného masa a klacku. Prohlédni si jeho hodnoty.",
        ]),
        # ---------- Expert ----------
        Q("compost", "Bohatá půda", dep=["straw", "bark"], items=[("farmersdelight:organic_compost", 1), ("farmersdelight:rich_soil", 4)], xp=30, d=[
            "Organický kompost (&eOrganic Compost&r) slož z hlíny, slámy, kostní moučky a buď shnilého masa, nebo kůry.",
            "Polož ho na zem a čekej. Postupně se změní na bohatou půdu (&eRich Soil&r). Rychleji to jde na slunci, u vody a vedle hub, podzolu nebo podhoubí.",
            "Bohatá půda občas sama pohnojí rostlinu nad sebou. Motykou z ní uděláš bohatou ornici (&eRich Soil Farmland&r).",
        ]),
        Q("colony", "Houbové kolonie", dep=["compost"], items=[("farmersdelight:brown_mushroom_colony", 1)], xp=25, d=[
            "Hnědá nebo červená houba zasazená na bohatou půdu se změní na houbovou kolonii (&eBrown Mushroom Colony&r, &eRed Mushroom Colony&r). Ta časem roste.",
            "Dospělou kolonii rozbij s nůžkami v ruce a dostaneš ji celou jako předmět. Když na ni nůžkami jen klikneš, sklidíš z ní houbu.",
            "&aTip:&r Na prkénku ji nožem nakrájíš na 5 hub. Kolonie se hodí i do některých receptů.",
        ]),
        Q("feast", "Hostina", dep=["stew"], items=[("farmersdelight:roast_chicken_block", 1)], xp=40, s="Expert", **MS, d=[
            "Teď vaříš ve velkém. Hostina je velké jídlo pro celý tým. Pečené kuře (&eRoast Chicken&r) slož na pracovním stole z pečeného kuřete, pečených brambor, mrkví, cibule, vejce, chleba a misky.",
            "Hostinu polož jako blok. Kdokoli si z ní pravým tlačítkem s miskou nabere porci.",
            "&aTip:&r Porce z hostin patří k nejlepším jídlům ve hře. Dávají dlouhý efekt &eNourishment&r.",
        ]),
        Q("honey_ham", "Šunka v medu", dep=["feast", "ham", "cooked_rice"], items=[("farmersdelight:honey_glazed_ham_block", 1)], xp=35, d=[
            "Šunku v medu (&eHoney Glazed Ham&r) slož z uzené šunky, lahve medu, sladkých bobulí, vařené rýže a misky.",
            "Uzenou šunku získáš, když šunku vyudíš v udírně.",
        ]),
        Q("shepherds_pie", "Pastýřský koláč", dep=["feast"], items=[("farmersdelight:shepherds_pie_block", 1)], xp=35, d=[
            "Pastýřský koláč (&eShepherd's Pie&r) slož ze tří kusů pečeného skopového, pečených brambor, cibule, mléka a misky.",
        ]),
        Q("stuffed_pumpkin", "Plněná dýně", dep=["feast", "pot"], items=[("farmersdelight:stuffed_pumpkin_block", 1)], xp=35, d=[
            "Plněnou dýni (&eStuffed Pumpkin&r) uvaříš v hrnci. Místo misky dej do políčka pro nádobu celou dýni.",
            "Dovnitř přijde rýže, cibule, hnědá houba, brambora, bobule a zelenina. Vaří se dvakrát déle než běžné jídlo.",
        ]),
        Q("rolls", "Rýžové rolky", dep=["cooked_rice", "board"], items=[("farmersdelight:kelp_roll", 1), ("farmersdelight:salmon_roll", 2)], xp=25, d=[
            "Rolku z řasy (&eKelp Roll&r) slož na pracovním stole z vařené rýže, mrkve a sušené řasy.",
            "Lososovou rolku (&eSalmon Roll&r) slož ze 2 plátků lososa a vařené rýže. Plátky ryb nakrájíš nožem na prkénku.",
        ]),
        Q("medley", "Talíř rolek", dep=["rolls", "feast"], items=[("farmersdelight:rice_roll_medley_block", 1)], xp=40, d=[
            "Talíř rolek (&eRice Roll Medley&r) je hostina z plátků rolky z řasy, lososových rolek, treskových rolek a misky.",
            "Rolku z řasy nakrájíš nožem na prkénku na plátky.",
        ]),
        Q("netherite_knife", "Netheritový nůž", dep=["iron_knife"], items=[("farmersdelight:netherite_knife", 1)], xp=50, optional=True, d=[
            "Diamantový nůž vylepšíš na kovářském stole netheritovým ingotem a šablonou vylepšení, stejně jako jiné nástroje.",
            "Je to nejlepší a nejodolnější nůž.",
        ]),
        Q("master_chef", "Mistr kuchař", dep=["feast", "pasta", "variety"], tasks=[adv("farmersdelight:main/master_chef")], icon="farmersdelight:roast_chicken_block", xp=100, optional=True, d=[
            "Velká výzva: sněz alespoň jednou každé hlavní jídlo z &bFarmer's Delight&r (27 jídel včetně hostin).",
            "Seznam uvidíš v postupu (Advancements) u úspěchu &eMaster Chef&r. Quest se splní sám.",
            "&aTip:&r Některá jídla se v tomto packu vaří jinak než v původním modu. Vždy se řiď JEI.",
        ]),
    ],
)

DELIGHTS = dict(
    key="delight_addons", group="food", title="Další Delight doplňky",
    subtitle="Nové plodiny, nápoje a kuchyně z celého světa", icon="culturaldelights:avocado",
    quests=[
        Q("start", "Ještě víc jídla", dep=["farmers_delight:pot"], icon="farmersdelight:iron_knife", tasks=[auto()], xp=10, s="Začátečník", **MS, d=[
            "Tyhle doplňky rozšiřují &bFarmer's Delight&r o nové plodiny, nápoje, stroje a jídla. Jejich jídla se vaří v hrnci a krájí na prkénku z Farmer's Delight.",
            "Začni doplňky s plodinami, které rostou kolem tebe. Pak přijdou nápoje a kvašení a nakonec jídla z Netheru, Endu a Twilight Forestu.",
            "&aTip:&r Některá jídla z doplňků dávají efekt &eComfort&r (pohoda). Ten tě léčí, i když máš hlad.",
        ]),
        # --- Cultural Delights ---
        Q("cultural", "Cultural Delights", dep=["start"], items=[("culturaldelights:avocado", 1), ("culturaldelights:cucumber", 1), ("culturaldelights:eggplant", 1)], xp=25, d=[
            "&bCultural Delights&r přidává jídla z celého světa: tacos, kari, sushi, nakládané okurky i nápoje.",
            "Avokáda rostou na stromech v džunglích. Divoké okurky najdeš v bažinách, lilek v džunglích a kukuřici v pláních.",
            "&aTip:&r Z divokých rostlin dostaneš i semínka, takže si je můžeš pěstovat doma.",
        ]),
        Q("cult_vat", "Kvasná káď", dep=["cultural"], items=[("culturaldelights:vat", 1)], xp=25, d=[
            "Káď (&eVat&r) vyrobíš ze železa, prken, desky a plástve. Kvasí, pálí a chladí nápoje a jídla.",
            "Bez ničeho pod kádí probíhá kvašení. Se zdrojem tepla pod ní (například sporák) pálení, s ledem pod ní chlazení.",
            "Ocet (&eVinegar&r) vykvasíš z kbelíku vody, cukru a hnědé houby do lahve.",
        ]),
        Q("cult_pickle", "Nakládané okurky", dep=["cult_vat", "cult_salt"], items=[("culturaldelights:pickle", 4)], xp=25, d=[
            "Nakládané okurky (&ePickle&r) vykvasíš v kádi ze 4 okurek, octa a soli.",
            "&aTip:&r Ve stejné kádi vznikne i sýr, tofu nebo pivo. Recepty ukáže JEI.",
        ]),
        Q("cult_salt", "Sůl", dep=["cultural"], items=[("culturaldelights:salt", 4)], xp=20, d=[
            "Bloky soli (&eSalt Block&r) najdeš pod zemí v krápníkových jeskyních (&eDripstone Caves&r). Z jednoho bloku slož na pracovním stole 4 soli (&eSalt&r).",
            "&aTip:&r Sůl jde i pěstovat. Z bloku soli, vody a krápníku (&ePointed Dripstone&r) postavíš farmu na solné krápníky (&eSalt Spike&r).",
        ]),
        # --- Corn Delight ---
        Q("corn", "Corn Delight", dep=["start"], items=[("corn_delight:corn", 4), ("corn_delight:popcorn", 1)], xp=25, d=[
            "&bCorn Delight&r přidává kukuřici (&eMaize&r). Divoká kukuřice roste v mírných biomech, třeba v pláních a lesích.",
            "Z kukuřice na pracovním stole získáš zrno (&eCorn Kernel&r). Zrna zasadíš, nebo je upečeš v peci na popcorn (&ePopcorn&r).",
        ]),
        Q("taco", "Tacos", dep=["corn"], items=[("corn_delight:taco", 1)], xp=25, d=[
            "Syrovou tortillu (&eRaw Tortilla&r) slož ze tří kukuřic a kbelíku vody a upeč ji.",
            "Taco (&eTaco&r) pak slož z tortilly, zelí, cibule a pečeného masa.",
        ]),
        Q("cornbread", "Kukuřičný chléb", dep=["corn"], items=[("corn_delight:cornbread", 1)], xp=15, optional=True, d=[
            "Těsto (&eCornbread Batter&r) slož ze dvou kukuřic, mléka a vejce. Upeč ho v peci, udírně nebo na táboráku.",
        ]),
        # --- Expanded Delight ---
        Q("expanded", "Expanded Delight", dep=["start"], items=[("expandeddelight:juicer", 1), ("expandeddelight:cinnamon", 1)], xp=25, d=[
            "&bExpanded Delight&r přidává odšťavňovač, sýrový sud, skořici, burské oříšky, chilli, chřest, batáty a brusinky.",
            "Odšťavňovač (&eJuicer&r) ze sudu a železa dělá džusy do lahví. Skořicovníky rostou v džunglích.",
            "Skořici získáš takhle: kmen skořicovníku nakrájej sekerou na prkénku na tyčinky. Tyčinku pak rozdrť na prkénku paličkou (&eCrushing Mallet&r).",
        ]),
        Q("cheese", "Sýr ze sudu", dep=["expanded"], items=[("expandeddelight:cheese_wheel", 1)], xp=30, d=[
            "Sýrový sud (&eCask&r) vyrobíš ze sudů, kbelíku, železa a prken. Klikni na něj kbelíkem mléka.",
            "Mléko v sudu pomalu zraje na sýr. Rychleji to jde ve tmě a u vody. Hotový sýr vyndáš pravým tlačítkem.",
        ]),
        Q("ed_juice", "Čerstvý džus", dep=["expanded"], items=[("expandeddelight:apple_juice", 1)], xp=15, optional=True, d=[
            "Do odšťavňovače dej jablko a cukr a jako nádobu lahev. Vznikne jablečný džus (&eApple Juice&r).",
        ]),
        Q("mac_cheese", "Makaróny se sýrem", dep=["cheese", "farmers_delight:pasta"], items=[("expandeddelight:mac_and_cheese", 1)], xp=25, d=[
            "Makaróny se sýrem (&eMac and Cheese&r) uvaříš v hrnci z mléka, sýra, těstovin a soli.",
            "Pod dnem oceánů najdeš rudu soli (&eSalt Ore&r). Padá z ní kamenná sůl (&eSalt Rock&r), kterou rozdrtíš na prkénku paličkou na sůl.",
        ]),
        # --- Rustic Delight ---
        Q("rustic", "Rustic Delight", dep=["start"], items=[("rusticdelight:cotton_boll", 1)], xp=25, d=[
            "&bRustic Delight&r přidává bavlnu, papriky, kávu, palačinky a smažená jídla.",
            "Divoká bavlna roste v lesích, papriky a káva v džunglích. Z bavlny vyrobíš provázek.",
        ]),
        Q("cooking_oil", "Olej na smažení", dep=["rustic"], items=[("rusticdelight:cooking_oil", 1)], xp=20, d=[
            "Olej (&eCooking Oil&r) uvaříš v hrnci ze 6 semínek bavlny do lahve.",
            "S olejem a těstíčkem (&eBatter&r) smažíš kuře, ryby i houby. Těstíčko uvaříš z mléka, vejce a pšenice.",
        ]),
        Q("rustic_coffee", "Káva", dep=["rustic"], items=[("rusticdelight:coffee", 1)], xp=20, d=[
            "Kávová zrna upraž v peci. Ze 3 pražených zrn uvaříš v hrnci kávu (&eCoffee&r) do lahve.",
            "&aTip:&r S mlékem, medem nebo čokoládou vzniknou další druhy kávy.",
        ]),
        Q("pancakes", "Palačinky", dep=["cooking_oil"], items=[("rusticdelight:pancakes", 1)], xp=25, d=[
            "Palačinky (&ePancakes&r) potřebují těstíčko, sirup a cukr. Sirup uvaříš v hrnci z jablek nebo řepy s cukrem.",
            "Talíř palačinek se dá položit jako blok.",
        ]),
        # --- Fruits Delight ---
        Q("fruits", "Fruits Delight", dep=["start"], items=[("fruitsdelight:pineapple", 1), ("fruitsdelight:lemon", 1)], xp=25, d=[
            "&bFruits Delight&r přidává ovocné stromy a keře: hrušky, broskve, mango, kiwi, fíky, borůvky a další.",
            "Ananas roste divoce na plážích. Citrony rostou v pláních.",
            "&aTip:&r Džemy a želé z tohoto modu dávají zvláštní efekty. Popis efektu najdeš v popisku jídla.",
        ]),
        Q("fruit_rice", "Ananasová rýže", dep=["fruits", "farmers_delight:rice"], items=[("fruitsdelight:pineapple_fried_rice", 1)], xp=20, optional=True, d=[
            "Ananasovou smaženou rýži (&ePineapple Fried Rice&r) uvaříš v hrnci z ananasu, tří rýží, zelí a vejce.",
        ]),
        # --- Ocean's Delight ---
        Q("oceans", "Ocean's Delight", dep=["start"], items=[("oceansdelight:fugu_roll", 1)], xp=30, d=[
            "&bOcean's Delight&r přidává jídla z mořských tvorů: olihní, strážců a ryb.",
            "Čtverzubec (&ePufferfish&r) nakrájený nožem na prkénku dá 6 plátků fugu (&eFugu Slice&r). Dva plátky a vařená rýže dají rolku (&eFugu Roll&r).",
            "&aTip:&r Oliheň zabitá nožem pustí chapadla (&eTentacles&r).",
        ]),
        Q("guardian_soup", "Polévka ze strážce", dep=["oceans"], items=[("oceansdelight:guardian_soup", 1)], xp=35, optional=True, d=[
            "Strážci v oceánských monumentech pouštějí maso strážce (&eGuardian&r).",
            "Polévku (&eGuardian Soup&r) uvaříš v hrnci ze strážce, cibule, 2 vajec a 2 rajčat.",
        ]),
        # --- Miner's Delight ---
        Q("miners", "Miner's Delight", dep=["start"], items=[("minersdelight:copper_pot", 1)], xp=25, d=[
            "&bMiner's Delight&r přidává jídla do jeskyní: jeskynní mrkev, netopýří křídla, chapadla a měděný hrnec.",
            "Měděný hrnec (&eCopper Pot&r) je menší hrnec z mědi. Polévky z něj nabereš do měděných hrnků (&eCopper Cup&r).",
            "&aTip:&r Netopýři pouštějí křídla (&eBat Wing&r). Upeč je a máš jídlo na cesty.",
        ]),
        Q("cave_soup", "Jeskynní polévka", dep=["miners"], items=[("minersdelight:cave_carrot", 4), ("minersdelight:cave_soup", 1)], xp=20, d=[
            "Divoká jeskynní mrkev roste v jeskyních pod výškou Y 48.",
            "Jeskynní polévku (&eCave Soup&r) uvaříš z jeskynní mrkve, červené houby a dvou hnědých hub.",
        ]),
        # --- Abnormals Delight ---
        Q("abnormals", "Abnormals Delight", dep=["start"], items=[("abnormals_delight:maple_glazed_bacon", 1)], xp=25, d=[
            "&bAbnormals Delight&r propojuje Farmer's Delight s mody &bAutumnity&r a &bUpgrade Aquatic&r.",
            "Slanina v sirupu (&eMaple Glazed Bacon&r) = pečená slanina a javorový sirup (&eSyrup Bottle&r). Sirup uvaříš v peci z lahve mízy (&eSap Bottle&r).",
            "Když sekerou oloupeš javorový kmen, někdy z něj vznikne kmen s mízou (&eSappy Maple Log&r). Prázdnou lahví z něj nabereš mízu.",
        ]),
        Q("abnormals_perch", "Okoun s houbami", dep=["abnormals", "farmers_delight:colony"], items=[("abnormals_delight:perch_with_mushrooms", 1)], xp=30, optional=True, d=[
            "Okoun (&eRaw Perch&r) je ryba z modu &bUpgrade Aquatic&r. Syrového okouna získáš, když ho ve vodě zabiješ.",
            "Okouna s houbami (&ePerch with Mushrooms&r) uvaříš z okouna, kolonie červených hub, rýže a rajčete.",
        ]),
        # --- Aquaculture Delight ---
        Q("aquaculture", "Aquaculture Delight", dep=["start"], items=[("aquaculturedelight:crispy_fried_perch", 2)], xp=25, d=[
            "&bAquaculture Delight&r dělá jídla z ryb z modu &bAquaculture&r.",
            "Křupavého okouna (&eCrispy Fried Perch&r) uvaříš v hrnci z okouna nebo okounka (&eSmallmouth Bass&r), pšenice a vejce. Dostaneš dva.",
        ]),
        Q("bass_stew", "Rybí guláš z okounka", dep=["aquaculture"], items=[("aquaculturedelight:bass_stew", 1)], xp=20, d=[
            "Guláš (&eBass Stew&r) uvaříš v hrnci z okounka nebo okouna, zelí a houby. Servíruje se do misky.",
            "&aTip:&r Z křupavého okouna, pečené brambory a rajčatové omáčky složíš rybu s hranolky (&eFish and Chips&r).",
        ]),
        Q("neptunium_knife", "Neptuniový nůž", dep=["aquaculture"], items=[("aquaculturedelight:neptunium_knife", 1)], xp=40, optional=True, d=[
            "Neptuniový nůž (&eNeptunium Knife&r) vyrobíš z neptuniového ingotu a klacku.",
            "Neptunium vylovíš při rybaření. Najdeš ho i v truhle &eNeptune's Bounty&r, kterou můžeš vylovit z moře.",
        ]),
        # --- Chef's Delight ---
        Q("chefs", "Kuchař ve vesnici", dep=["start"], tasks=[adv("minecraft:adventure/trade")], icon="farmersdelight:skillet", xp=20, d=[
            "&bChef's Delight&r přidává dvě nová povolání vesničanů: kuchaře (&eCook&r) a šéfkuchaře (&eChef&r).",
            "Vesničan bez práce se stane kuchařem u pánve a šéfkuchařem u hrnce. Ve vesnicích mají i vlastní domky.",
            "Prodávají hotová jídla za smaragdy a kupují suroviny, třeba cukr nebo bobule. Quest se splní po prvním obchodu s jakýmkoli vesničanem.",
        ]),
        # --- Storage Delight ---
        Q("storage", "Storage Delight", dep=["start"], items=[("storagedelight:oak_drawer", 1), ("storagedelight:small_oak_drawers", 1)], xp=15, optional=True, d=[
            "&bStorage Delight&r přidává kuchyňský nábytek s úložným prostorem: šuplíky, skříňky se sklem a skříňky s pracovní deskou.",
            "Šuplík (&eOak Drawer&r) vyrobíš z dubových desek a 3 poklopů. Malé šuplíky (&eSmall Oak Drawers&r) z 8 desek a 1 poklopu.",
        ]),
        # --- Pokročilý: nápoje a kvašení ---
        Q("bnc", "Brewin' and Chewin'", dep=["start"], items=[("brewinandchewin:keg", 1)], xp=30, s="Pokročilý", **MS, d=[
            "Teď už nejen vaříš, ale i kvasíš. Kvašení chce čas a správnou teplotu.",
            "&bBrewin' and Chewin'&r přidává soudek (&eKeg&r) na kvašení nápojů a sýrů. Vyrobíš ho ze železa, prken a plástve.",
            "Do soudku dej suroviny a tekutinu (vodu, mléko nebo med). Za chvíli vznikne nápoj, který naliješ do korbelů (&eTankard&r).",
            "Každý recept chce jinou teplotu. Potřebnou teplotu ukáže JEI, aktuální vidíš v okně soudku.",
        ]),
        Q("beer", "Pivo", dep=["bnc"], items=[("brewinandchewin:tankard", 4), ("brewinandchewin:beer", 1)], xp=25, d=[
            "Korbely (&eTankard&r) vyrobíš z prken a železných nugetů.",
            "Pivo (&eBeer&r) vykvasíš z vody, pšenice, semínek pšenice a hnědé houby.",
            "&cPozor:&r Alkohol dává efekt &eTipsy&r – obraz se houpe. Nepij ho před bojem.",
        ]),
        Q("bnc_temp", "Teplo a chlad", dep=["bnc"], items=[("brewinandchewin:heating_cask", 1), ("brewinandchewin:ice_crate", 1)], xp=25, d=[
            "Ohřívací sud (&eHeating Cask&r) postavený u soudku zvýší teplotu. Bedna s ledem (&eIce Crate&r) ji sníží.",
            "Ohřívací sud vyrobíš z uhelných bloků, magmatického bloku, ohnivého prášku a dřeva. Bednu s ledem ze zhutněného ledu, provázku a dřeva.",
        ]),
        Q("bnc_cheese", "Zrající sýr", dep=["bnc_temp"], items=[("brewinandchewin:flaxen_cheese_wheel", 1)], xp=30, d=[
            "V teplém soudku vykvas z mléka, hnědé houby, dýňových semínek a cukru sýrovou hmotu. Nalij ji do plástve – vznikne nezralý sýr.",
            "Nezralý sýr (&eUnripe Flaxen Cheese Wheel&r) polož jako blok. Časem dozraje na sýr (&eFlaxen Cheese Wheel&r).",
            "Nožem z něj na prkénku nakrájíš klínky sýra (&eFlaxen Cheese Wedge&r).",
        ]),
        Q("pizza", "Pizza", dep=["bnc_cheese", "farmers_delight:tomato_sauce"], items=[("brewinandchewin:pizza", 1)], xp=30, d=[
            "Pizzu (&ePizza&r) slož na pracovním stole ze sýra, rajčatové omáčky, pšenice a dvou přísad navrch. Které přísady se hodí, ukáže JEI.",
            "Pizzu polož jako blok a nakrájej ji nožem na kousky.",
        ]),
        # --- Farmer's Respite ---
        Q("tea_bush", "Čajovník", dep=["start"], items=[("farmersrespite:tea_seeds", 2), ("farmersrespite:green_tea_leaves", 2)], xp=20, d=[
            "&bFarmer's Respite&r přidává čaj, kávu a konvici. Divoké čajovníky (&eWild Tea Bush&r) rostou v bažinách a džunglích.",
            "Zasaď semínka čaje (&eTea Seeds&r). Mladý keř dává zelené lístky, starší žluté a nejstarší černé.",
        ]),
        Q("respite", "Konvice a čaj", dep=["tea_bush"], items=[("farmersrespite:kettle", 1), ("farmersrespite:green_tea", 1)], xp=30, d=[
            "Konvici (&eKettle&r) vyrobíš z mědi, kbelíku, kůže a klacků. Potřebuje teplo zespodu, stejně jako hrnec.",
            "Nalij do konvice vodu kbelíkem a vlož lístky. Hotový čaj (&eGreen Tea&r) nabereš do lahví.",
            "&aTip:&r Čaje a káva dávají různé užitečné efekty. Popis najdeš v popisku nápoje.",
        ]),
        Q("black_tea", "Černý čaj", dep=["respite"], items=[("farmersrespite:black_tea", 1)], xp=20, optional=True, d=[
            "Černé lístky (&eBlack Tea Leaves&r) dává jen nejstarší čajovník. Uvař z nich černý čaj (&eBlack Tea&r).",
        ]),
        Q("respite_coffee", "Káva z Netheru", dep=["respite"], items=[("farmersrespite:coffee", 1)], xp=35, optional=True, d=[
            "Divoký kávovník (&eWild Coffee Bush&r) roste v Netheru v čedičových deltách (&eBasalt Deltas&r).",
            "Kávová zrna (&eCoffee Beans&r) uvař v konvici s vodou na kávu (&eCoffee&r).",
        ]),
        # --- Expert: jiné dimenze ---
        Q("nether", "My Nether's Delight", dep=["start"], items=[("mynethersdelight:hoglin_loin", 1)], xp=30, s="Expert", **MS, d=[
            "Teď se za surovinami vydáš do jiných dimenzí, takže se připrav na boj.",
            "&bMy Nether's Delight&r přidává jídla z Netheru: maso hoglinů a striderů, pálivé papriky a jídla z ghastů.",
            "Hoglin v Netheru pustí místo kotlet hoglinskou svíčkovou (&eHoglin Loin&r). Když ho zabiješ nožem, může pustit i kůži (&eHoglin Hide&r).",
            "&aTip:&r Upeč svíčkovou v peci nebo na táboráku a máš silné jídlo pro boj v Netheru.",
        ]),
        Q("nether_soil", "Nether kompost", dep=["nether", "farmers_delight:compost"], items=[("mynethersdelight:letios_compost", 1), ("mynethersdelight:resurgent_soil", 1)], xp=35, optional=True, d=[
            "Kompost Leteos (&eLeteos Compost&r) slož na pracovním stole z písku duší (nebo půdy duší), kořenů z Netheru, shnilého masa a kostní moučky. Přesný recept ukáže JEI.",
            "Položený kompost se časem změní na oživující půdu (&eResurgent Soil&r). Rostliny na ní rostou rychleji.",
        ]),
        Q("end", "End's Delight", dep=["start"], items=[("ends_delight:end_stove", 1)], xp=40, d=[
            "&bEnd's Delight&r přidává jídla z Endu: z chorusu, shulkerů a dokonce z draka.",
            "Sporák z Endu (&eEnd Stove&r) vyrobíš z praženého chorusu, cihel z endového kamene a táboráku. Hřeje hrnec jako běžný sporák.",
        ]),
        Q("bubble_tea", "Bublinkový čaj", dep=["end"], items=[("ends_delight:bubble_tea", 1)], xp=30, optional=True, d=[
            "Perlu Endu a plod chorusu nakrájíš nožem na prkénku na zrníčka (&eEnder Pearl Grain&r, &eChorus Fruit Grain&r).",
            "Bublinkový čaj (&eBubble Tea&r) uvaříš v hrnci z mléka, plodu chorusu a obou druhů zrníček.",
        ]),
        Q("enders", "Ender's Delight", dep=["end"], items=[("endersdelight:endstone_stove", 1)], xp=40, d=[
            "&bEnder's Delight&r je další doplněk s jídly z Endu. Jeho sporák (&eEndstone Stove&r) vyrobíš z obsidiánu, cihel z endového kamene, dračího dechu a táboráku.",
            "Endermani zabití nožem pustí oko (&eEnderman Sight&r), shulkeři měkkýše (&eShulker Mollusk&r) a endermiti kůrku (&eMite Crust&r).",
        ]),
        Q("chorus_juice", "Chorusový džus", dep=["enders"], items=[("endersdelight:chorus_juice", 1)], xp=20, optional=True, d=[
            "Chorusový džus (&eChorus Juice&r) slož na pracovním stole z plodu chorusu, cukru a lahve.",
        ]),
        Q("torchberry", "Sušenky z pochodňovníku", dep=["start"], items=[("twilightdelight:torchberry_cookie", 8)], xp=25, d=[
            "&bTwilight's Flavor & Delight&r přidává jídla z dimenze Twilight Forest: z jelenů, hydry, ghastů i z rostlin.",
            "Pochodňové bobule (&eTorchberries&r) rostou v Twilight Forestu. Bobule mezi dvěma pšenicemi dá 8 sušenek (&eTorchberry Cookie&r).",
        ]),
        Q("twilight", "Bludištní sporák", dep=["torchberry"], items=[("twilightdelight:maze_stove", 1)], xp=40, d=[
            "Bludištní sporák (&eMaze Stove&r) vyrobíš z rytířského kovu, cihel z bludiště, pochodňových bobulí a táboráku.",
            "Hřeje hrnec a jídla z Twilight Forestu na něm vaříš rychleji.",
            "&aTip:&r Ohnivý hrnec (&eFiery Cooking Pot&r) z ohnivých ingotů hřeje sám a nepotřebuje sporák.",
        ]),
        Q("ironwood_knife", "Nůž ze železného dřeva", dep=["torchberry"], items=[("twilightdelight:ironwood_knife", 1)], xp=25, optional=True, d=[
            "Nůž ze železného dřeva (&eIronwood Knife&r) vyrobíš z ingotu železného dřeva a klacku.",
            "Twilight Forest má i další nože: z ocelového listí, rytířského kovu, ohnivý a ledový.",
        ]),
        Q("extra", "ExtraDelight", dep=["start"], items=[("extradelight:mixing_bowl", 1), ("extradelight:oven", 1)], xp=30, d=[
            "&bExtraDelight&r je obří doplněk s desítkami kuchyňských strojů: mísa, hmoždíř, trouba, odpařovač, kvasná káď a další.",
            "Míchací mísu (&eMixing Bowl&r) vyrobíš z prken. Troubu (&eOven&r) z cihel, pece a terakoty.",
            "Všechno o ExtraDelight najdeš ve vlastní kapitole &eExtraDelight&r.",
        ]),
    ],
)

EXTRA = dict(
    key="extradelight", group="food", title="ExtraDelight",
    subtitle="Kuchyně plná strojů", icon="extradelight:oven",
    quests=[
        Q("start", "Kuchyně ExtraDelight", dep=["delight_addons:extra"], icon="extradelight:mixing_bowl", tasks=[auto()], xp=10, s="Začátečník", **MS, d=[
            "&bExtraDelight&r napodobuje skutečnou kuchyni. Místo pracovního stolu vaříš na strojích: mícháš v míse, drtíš v hmoždíři a pečeš v troubě.",
            "Začni mísou a hmoždířem. Pak přijde trouba, odpařovač soli a nakonec kvašení a čokoláda.",
            "&aTip:&r Postup každého receptu (i počet zamíchání) ukáže JEI.",
        ]),
        Q("utensils", "Vařečka a metla", dep=["start"], items=[("extradelight:wooden_spoon", 1), ("extradelight:whisk", 1)], xp=15, d=[
            "Vařečka (&eWooden Spoon&r) z prken a klacků a metla (&eWhisk&r) ze železných nugetů a klacku jsou nářadí k míchací míse.",
            "Pravým tlačítkem otevřeš mísu. Suroviny dej do políček, kbelík s tekutinou (mléko, voda) do políčka pro tekutinu.",
            "Pak na mísu opakovaně klikej vařečkou nebo metlou, dokud se vše nepromíchá. Vejce rozbiješ kliknutím vejcem na mísu.",
        ]),
        Q("mortar", "Hmoždíř", dep=["start"], items=[("extradelight:mortar_stone", 1), ("extradelight:pestle_stone", 1)], xp=15, d=[
            "Hmoždíř (&eMortar&r) vyrobíš ze 3 kamenů a paličku (&eStone Pestle&r) z kamene a klacku.",
            "Vlož do hmoždíře surovinu a pak na něj opakovaně klikej paličkou. Drtí koření, kakao, barviva i mouku.",
        ]),
        Q("flour", "Mouka", dep=["mortar"], items=[("extradelight:flour", 4)], xp=15, d=[
            "Semínka pšenice rozdrcená v hmoždíři dají mouku (&eFlour&r) a trochu oleje.",
            "Mouka je základ těsta, sušenek a dortů.",
        ]),
        Q("dough", "Těsto z mísy", dep=["flour", "utensils"], items=[("farmersdelight:wheat_dough", 3)], xp=15, d=[
            "Do mísy dej 3 mouky a kbelík vody. Zamíchej vařečkou a dostaneš 3 těsta (&eWheat Dough&r).",
            "Z těsta jsou chleby, těstoviny a koláče.",
        ]),
        Q("shaping", "Tvarovací stůl", dep=["flour"], items=[("extradelight:dough_shaping", 1)], xp=15, optional=True, d=[
            "Tvarovací stůl (&eDough Shaping Station&r) slož z mouky, prkna a klacku.",
            "Tvaruje těsto na různé druhy těstovin a sušenek. Možnosti ukáže JEI.",
        ]),
        Q("trays", "Plechy na pečení", dep=["start"], items=[("extradelight:sheet", 1), ("extradelight:tray", 1), ("extradelight:loaf_pan", 1)], xp=15, d=[
            "Trouba peče jen v nádobě. Plech (&eSheet Tray&r) je z těžké nášlapné desky. Pekáč (&eBaking Tray&r) a forma na chleba (&eLoaf Pan&r) mají navíc železné nugety.",
            "Nádoba se při pečení nespotřebuje. Kterou nádobu recept chce, ukáže JEI.",
        ]),
        Q("oven", "První pečení", dep=["trays"], items=[("extradelight:egg_in_the_basket", 1)], xp=20, d=[
            "Trouba (&eOven&r) potřebuje teplo zespodu, stejně jako hrnec z Farmer's Delight.",
            "Vejce v košíčku (&eEgg in a Basket&r) upeč na plechu z vejce a krajíce chleba (&eSlice of Bread&r).",
        ]),
        Q("evaporator", "Sůl z vody", dep=["start"], items=[("extradelight:evaporator", 1), ("extradelight:salt", 4)], xp=20, d=[
            "Odpařovač (&eEvaporator&r) vyrobíš z těžkých nášlapných desek a železných nugetů.",
            "Postav ho tak, aby nad ním bylo vidět nebe, a nalij do něj kbelík vody. Voda se pomalu odpaří a zůstane sůl (&eSalt&r).",
        ]),
        Q("butter", "Šlehačka a máslo", dep=["utensils"], items=[("extradelight:whipped_cream", 1), ("extradelight:butter", 1)], xp=25, s="Pokročilý", **MS, d=[
            "Teď už nestačí jen sypat suroviny do mísy – suroviny se zpracovávají ve více krocích.",
            "Mléko v míse ušlehej metlou na šlehačku (&eWhipped Cream&r). Když metlou šleháš šlehačku dál, vznikne máslo (&eButter&r). Přesný postup ukáže JEI.",
        ]),
        Q("cookies", "Cukrové sušenky", dep=["butter", "flour", "oven"], items=[("extradelight:sugar_cookie", 8)], xp=25, d=[
            "Těsto na sušenky (&eSugar Cookie Dough&r) zamíchej v míse z mouky, cukru, másla a vejce.",
            "Upeč ho v troubě na plechu. Dostaneš 8 sušenek (&eSugar Cookie&r).",
        ]),
        Q("drying", "Sušák", dep=["start"], items=[("extradelight:drying_rack_item", 1), ("extradelight:dried_fruit", 1)], xp=20, optional=True, d=[
            "Sušák (&eDrying Rack&r) vyrobíš z prken a provázků. Pomalu suší, co na něj položíš.",
            "Usuš na něm ovoce a dostaneš sušené ovoce (&eDried Fruit&r).",
        ]),
        Q("yeast", "Kvasnice", dep=["start"], items=[("extradelight:yeast_pot", 1), ("extradelight:yeast", 1)], xp=20, d=[
            "Kvasnicový hrnek (&eYeast Pot&r) slož z květináče, plátna, vody a sladidla (třeba cukru).",
            "Polož ho a počkej, až začne bublat. Pak na něj klikni prázdnou lahví a dostaneš kvasnice (&eYeast&r).",
        ]),
        Q("vinegar", "Ocet", dep=["yeast"], items=[("extradelight:vinegar_pot", 1), ("extradelight:vinegar", 1)], xp=20, d=[
            "Octový hrnek (&eVinegar Pot&r) slož jako kvasnicový, jen přidej dva kusy ovoce.",
            "Až začne bublat, nabereš z něj lahví ocet (&eVinegar&r).",
        ]),
        Q("melting", "Rozpouštěcí hrnec", dep=["start", "farmers_delight:pot"], items=[("extradelight:melting_pot", 1)], xp=20, d=[
            "Rozpouštěcí hrnec (&eMelting Pot&r) slož ze dvou hrnců z Farmer's Delight.",
            "Rozpouští čokoládu, led a další věci na tekutinu.",
        ]),
        Q("chiller", "Chladnička", dep=["melting"], items=[("extradelight:chiller", 1), ("extradelight:bar_mold", 1)], xp=30, d=[
            "Chladničku (&eChiller&r) slož ze železného bloku, kuchyňské skříňky a soudku (&eKeg&r). Soudek vyrobíš ze skla a sudu.",
            "Tekutina v ní ztuhne ve formě. Forma na tabulky (&eBar Mold&r) je z těžké nášlapné desky a 7 železných nugetů.",
        ]),
        Q("chocolate", "Čokoládová tabulka", dep=["chiller"], items=[("extradelight:milk_chocolate_bar", 1)], xp=30, d=[
            "Rozpuštěnou mléčnou čokoládu nech v chladničce ztuhnout ve formě. Dostaneš tabulku (&eMilk Chocolate Bar&r).",
            "Celý postup od kakaových bobů po čokoládu ukáže JEI.",
        ]),
        Q("vat", "Kvasná káď", dep=["vinegar"], items=[("extradelight:vat", 1), ("extradelight:lid", 1)], xp=35, s="Expert", **MS, d=[
            "Teď už nevaříš na pár kliknutí. Kvašení trvá i několik herních dní.",
            "Kvasná káď (&eFermentation Vat&r) je z mědi. Víko (&eVat Lid&r) z mědi a dřevěného tlačítka.",
            "Kvašení probíhá v krocích: nalij tekutinu (třeba ocet), vlož suroviny, později přidej sůl a zavři víko. Některé recepty trvají i několik dní.",
            "Co a kdy přidat a jestli má být víko zavřené, ukáže JEI u každého receptu.",
        ]),
        Q("kimchi", "Kimči", dep=["vat", "evaporator"], items=[("extradelight:kimchi_item", 2)], xp=40, optional=True, d=[
            "Kimči (&eKimchi&r) vykvasíš v kádi z vody, zelí, zázvoru, česneku a chilli prášku. Během kvašení přidej sůl.",
        ]),
        Q("tap", "Kohoutek a dřez", dep=["start"], items=[("extradelight:tap", 1), ("extradelight:oak_sink", 1)], xp=25, optional=True, d=[
            "Kohoutek (&eTap&r) z mědi, páky a dvou kbelíků vody je zdroj vody v kuchyni.",
            "Dřez (třeba &eOak Sink&r) dokončí kuchyni. Druhy dřezů najdeš v JEI.",
        ]),
        Q("hells_kitchen", "Pekelná kuchyně", dep=["vat", "farmers_delight:netherite_knife"], tasks=[adv("extradelight:hellskitchen")], icon="extradelight:netherite_spoon", xp=60, optional=True, d=[
            "Vylepši diamantový nůž a diamantovou vařečku (&eDiamond Spoon&r) na kovářském stole na netheritové. Quest se splní, až budeš mít netheritový nůž i netheritovou vařečku (&eNetherite Spoon&r).",
        ]),
    ],
)

PAMS = dict(
    key="pams", group="food", title="Pam's HarvestCraft",
    subtitle="Stovky plodin, stromů a jídel z pracovního stolu", icon="pamhc2foodcore:potitem",
    quests=[
        Q("start", "Pam's HarvestCraft 2", icon="pamhc2foodcore:potitem", tasks=[auto()], xp=10, s="Začátečník", **MS, d=[
            "&bPam's HarvestCraft 2&r přidává přes sto plodin, desítky ovocných stromů a stovky jídel.",
            "Jídla se vyrábějí na pracovním stole pomocí kuchyňského nářadí. Nářadí se při vaření nespotřebuje a zůstane ti.",
            "Plodiny najdeš v divokých zahrádkách (třeba &eWindy Garden&r), ovoce na stromech v lesích.",
        ]),
        Q("garden", "Divoká zahrádka", dep=["start"], items=[("pamhc2crops:lettuceitem", 1)], xp=15, d=[
            "Zahrádky vypadají jako malé keříky. Rozbij je a dostaneš náhodnou plodinu.",
            "Větrná zahrádka (&eWindy Garden&r) roste v pláních a savanách. Dává třeba salát, kukuřici, cibuli nebo jahody.",
            "Každý biom má jinou zahrádku s jinými plodinami.",
        ]),
        Q("seeds", "Semínka", dep=["garden"], items=[("pamhc2crops:lettuceseeditem", 2)], xp=10, d=[
            "Když dáš plodinu na pracovní stůl, dostaneš z ní semínko, třeba ze salátu &eLettuce Seed&r.",
            "Semínka zasaď na zoranou hlínu jako pšenici.",
        ]),
        Q("garden_shaded", "Stinná zahrádka", dep=["garden"], items=[("pamhc2crops:garlicitem", 1)], xp=10, optional=True, d=[
            "Stinná zahrádka (&eShaded Garden&r) roste v lesích. Dává třeba česnek, pórek, ředkvičky nebo lanýže.",
        ]),
        Q("garden_soggy", "Bažinná zahrádka", dep=["garden"], items=[("pamhc2crops:blueberryitem", 1)], xp=10, optional=True, d=[
            "Bažinná zahrádka (&eSoggy Garden&r) roste v bažinách. Dává třeba borůvky, rýži, bavlnu nebo chřest.",
        ]),
        Q("garden_arid", "Pouštní zahrádka", dep=["garden"], items=[("pamhc2crops:cactusfruititem", 1)], xp=10, optional=True, d=[
            "Pouštní zahrádka (&eArid Garden&r) roste v suchých biomech. Dává třeba kaktusové ovoce, agáve nebo cizrnu.",
        ]),
        Q("garden_frost", "Mrazivá zahrádka", dep=["garden"], items=[("pamhc2crops:broccoliitem", 1)], xp=10, optional=True, d=[
            "Mrazivá zahrádka (&eFrost Garden&r) roste v jehličnatých lesích. Dává třeba brokolici, zelí, oves nebo maliny.",
        ]),
        Q("garden_tropical", "Tropická zahrádka", dep=["garden"], items=[("pamhc2crops:pineappleitem", 1)], xp=10, optional=True, d=[
            "Tropická zahrádka (&eTropical Garden&r) roste v džunglích a u oceánů. Dává třeba ananas, kávu, kiwi nebo zázvor.",
        ]),
        Q("tree", "Ovocné stromy", dep=["start"], items=[("pamhc2trees:cherryitem", 2)], xp=15, d=[
            "Ovocné stromy z Pam's rostou v lesích. Ovoce visí na stromě jako malý blok.",
            "Zralé ovoce utrhneš pravým tlačítkem. Strom pak plodí znovu.",
        ]),
        Q("orchard", "Vlastní sad", dep=["tree"], items=[("pamhc2trees:apple_sapling", 1)], xp=20, d=[
            "Sazenici ovocného stromu slož na pracovním stole z 8 kusů ovoce a libovolné sazenice.",
            "Jabloň (&eApple Sapling&r) tedy vyrobíš z 8 jablek a sazenice. Zasaď ji a z jabloně pak sklízej jablka.",
        ]),
        Q("tools", "Kuchyňské nářadí", dep=["start"], items=[("pamhc2foodcore:cuttingboarditem", 1), ("pamhc2foodcore:potitem", 1), ("pamhc2foodcore:skilletitem", 1)], xp=20, d=[
            "Základní nářadí z Pam's: prkénko (&eCutting Board&r), hrnec (&ePot&r) a pánev (&eSkillet&r). Vyrobíš je z mědi a dřeva.",
            "Nářadí dáš na pracovní stůl spolu se surovinami. Po vyrobení jídla ti nářadí zůstane.",
            "&cPozor:&r Tohle jsou předměty z Pam's, ne bloky z Farmer's Delight. Prkénko a pánev se jmenují stejně, tak se v JEI dívej, z jakého jsou modu.",
        ]),
        Q("water", "Voda a mléko do receptů", dep=["start"], items=[("pamhc2foodcore:freshwateritem", 8), ("pamhc2foodcore:freshmilkitem", 8)], xp=10, d=[
            "Kbelík vody na pracovním stole dá 8 čerstvé vody (&eFresh Water&r). Kbelík mléka dá 8 čerstvého mléka (&eFresh Milk&r).",
            "Recepty pak nespotřebují celý kbelík, ale jen jeden kus.",
        ]),
        Q("salt", "Sůl", dep=["tools", "water"], items=[("pamhc2foodcore:saltitem", 4)], xp=10, d=[
            "Hrnec (&ePot&r) a voda na pracovním stole dají sůl (&eSalt&r).",
            "Sůl je potřeba do těsta, sýra a mnoha dalších jídel.",
        ]),
        Q("butter_cheese", "Máslo a sýr", dep=["salt"], items=[("pamhc2foodcore:butteritem", 1), ("pamhc2foodcore:cheeseitem", 1)], xp=15, d=[
            "Hrnec a mléko na pracovním stole dají máslo (&eButter&r). Hrnec, mléko a sůl dají sýr (&eCheese&r).",
        ]),
        Q("toast", "Toast", dep=["butter_cheese"], items=[("pamhc2foodcore:toastitem", 2)], xp=10, d=[
            "Pánev, chléb a máslo na pracovním stole dají dva toasty (&eToast&r).",
        ]),
        Q("tools2", "Další nářadí", dep=["tools"], items=[("pamhc2foodcore:saucepanitem", 1), ("pamhc2foodcore:mixingbowlitem", 1), ("pamhc2foodcore:bakewareitem", 1), ("pamhc2foodcore:juiceritem", 1), ("pamhc2foodcore:grinderitem", 1)], xp=30, s="Pokročilý", **MS, d=[
            "Základy umíš. S dalším nářadím uvaříš stovky receptů. Každý kus vyrob jen jednou – při vaření se nespotřebuje.",
            "Kastrůlek (&eSaucepan&r) je z mědi a klacku, mísa (&eMixing Bowl&r) z prken a klacku. Pekáč (&eBakeware&r) a odšťavňovač (&eJuicer&r) z terakoty. Mlýnek (&eGrinder&r) z andezitu a klacku.",
        ]),
        Q("flour", "Mouka", dep=["tools2"], items=[("pamhc2foodcore:flouritem", 2)], xp=10, d=[
            "Mlýnek (&eGrinder&r) s pšenicí nebo bramborou na pracovním stole dá mouku (&eFlour&r).",
        ]),
        Q("dough", "Těsto", dep=["flour", "salt"], items=[("pamhc2foodcore:doughitem", 2)], xp=15, d=[
            "Mísa (&eMixing Bowl&r), mouka, voda a sůl na pracovním stole dají dvě těsta (&eDough&r).",
            "Z těsta jsou koláče, pečivo a těstoviny.",
        ]),
        Q("juice", "Jablečný džus", dep=["tools2"], items=[("pamhc2foodcore:applejuiceitem", 1)], xp=10, optional=True, d=[
            "Odšťavňovač (&eJuicer&r) a dvě jablka na pracovním stole dají jablečný džus (&eApple Juice&r).",
        ]),
        Q("pie", "Kuřecí koláč", dep=["tools2", "dough"], items=[("pamhc2foodcore:chickenpotpieitem", 1)], xp=25, d=[
            "Kuřecí koláč (&eChicken Pot Pie&r) slož z pekáče, syrového kuřete, brambory, mrkve a těsta.",
            "Spojuje maso a zeleninu, takže dobře zasytí.",
        ]),
        Q("roast", "Pečeně v hrnci", dep=["tools2"], items=[("pamhc2foodcore:potroastitem", 1)], xp=25, d=[
            "Pečeni (&ePot Roast&r) slož na pracovním stole z hrnce, syrového hovězího, brambory a mrkve. Dobře zasytí.",
        ]),
        Q("roller", "Váleček a olej", dep=["tools2"], items=[("pamhc2foodcore:rolleritem", 1), ("pamhc2foodcore:cookingoilitem", 2)], xp=15, d=[
            "Váleček (&eRoller&r) vyrobíš z kmene a dvou klacků.",
            "Váleček a zelenina (mrkev, brambora, řepa nebo dýně) na pracovním stole dají olej (&eCooking Oil&r).",
        ]),
        Q("dinner", "Kuřecí večeře", dep=["roller", "dough", "butter_cheese"], items=[("pamhc2foodcore:chickendinneritem", 1)], xp=50, s="Expert", **MS, d=[
            "Velké jídlo z více kroků. Smažené kuře (&eFried Chicken&r) = hrnec, mouka, syrové kuře a olej.",
            "Bramborová kaše (&eMashed Potatoes&r) = mísa, pečená brambora, máslo a sůl.",
            "Kuřecí večeře (&eChicken Dinner&r) = prkénko, smažené kuře, bramborová kaše a zelenina.",
        ]),
    ],
)

# Pořadí kapitol této oblasti v knize questů
CHAPTERS = [FARMERS, DELIGHTS, EXTRA, PAMS]

# Předměty bez receptu/loot table, které se dají ověřeně získat
NO_RECIPE = {
    "expandeddelight:cinnamon": "prkénko (farmersdelight:cutting): skořicová tyčinka + palička Crushing Mallet -> 2 skořice (data/expandeddelight/recipe/cutting/cinnamon_stick.json)",
}
