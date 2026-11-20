from engine import *

# =====================================================================
# VLAKY – Create 6 + Steam 'n' Rails + Bells & Whistles
# =====================================================================
TRAINS = dict(
    key="trains", group="create", title="Vlaky",
    subtitle="Koleje, vlaky, jízdní řády a nádraží", icon="create:controls",
    quests=[
        # ---------- Začátečník: suroviny a první vlak ----------
        Q("start", "Vlaky v Create", icon="create:track_station", tasks=[auto()], xp=10,
          shape="hexagon", size=1.5, s="Začátečník", d=[
            "Vlaky z &bCreate&r vozí hráče i náklad po vlastních kolejích. Jezdí daleko, rychle a umí jezdit samy podle jízdního řádu.",
            "Postup: vyrobíš robustní plát a vlakové pouzdro, položíš koleje a stanici, sestavíš vlak a naučíš ho jezdit samotného. Nakonec postavíš celou železniční síť.",
            "&aVlaky jsou pokročilá část Create. Nejdřív zvládni mosaz, pokladač a precizní strojek z kapitoly Create.&r",
            "&bSteam 'n' Rails&r přidává další koleje, výhybky a průvodčí. &bBells & Whistles&r přidává ozdoby pro vlaky a nádraží."]),
        Q("sturdy", "Robustní plát", dep=["start", "create:crushing", "create:spout"],
          items=[("create:sturdy_sheet", 4)], xp=30, d=[
            "Robustní plát (&eSturdy Sheet&r) je pevný plech z obsidiánu. Potřebuješ ho na vlakové pouzdro a na jízdní řády.",
            "Nejdřív rozdrť obsidián v drtících kolech (&eCrushing Wheel&r) na obsidiánovou moučku (&ePowdered Obsidian&r).",
            "Pak přijde sekvenční montáž na pásu: dávkovač (&eSpout&r) přidá k moučce lávu a mechanický lis ji dvakrát stiskne. Přesné kroky ukáže JEI.",
            "&aLávu do dávkovače přivedeš čerpadlem a potrubím, třeba z nádrže.&r"]),
        Q("casing", "Vlakové pouzdro", dep=["sturdy", "create:brass"],
          items=[("create:railway_casing", 4)], xp=30, d=[
            "Vlakové pouzdro (&eTrain Casing&r) je základ všech dílů železnice: stanic, ovládání, návěstidel i podvozků.",
            "Polož mosazné pouzdro (&eBrass Casing&r) a klikni na něj robustním plátem. Hromadně to za tebe udělá pokladač (&eDeployer&r).",
            "&aMosazné pouzdro vznikne, když klikneš mosazným ingotem na oloupaný kmen.&r"]),
        Q("track", "Polož koleje", dep=["start", "create:deployer"],
          items=[("create:track", 32)], xp=30, d=[
            "Vlaková kolej (&eTrain Track&r) je kolej jen pro vlaky z Create. Obyčejné koleje pro vozíky nestačí.",
            "Vyrábí se sekvenční montáží: na kamennou desku přidají pokladače dva nugety (železné nebo zinkové) a lis ji stiskne. Funguje i hladká kamenná nebo andezitová deska.",
            "Pokládání: klikni kolejí na položenou kolej a pak na místo, kam má vést. Položí se celý úsek, i se zatáčkou nebo svahem. Když při tom držíš klávesu sprintu, vznikne co nejdelší oblouk.",
            "&aKdyž držíš ve druhé ruce bloky, položí se pod koleje jako násyp.&r"]),
        Q("station", "Vlaková stanice", dep=["track", "casing"],
          items=[("create:track_station", 1)], xp=40, d=[
            "Vlaková stanice (&eTrain Station&r) je zastávka a zároveň místo, kde se vlak staví a rozebírá.",
            "Výroba: vlakové pouzdro a kompas dají 2 stanice.",
            "Pokládání: se stanicí v ruce klikni na kolej (tím ji vybereš) a pak stanici polož kousek vedle koleje.",
            "&cKe stanici umí vlak přijet jen ze směru, který stanice ukazuje.&r"]),
        Q("controls", "Ovládání vlaku", dep=["station", "create:precision"],
          items=[("create:controls", 1)], xp=40, d=[
            "Ovládací prvky vlaku (&eTrain Controls&r) jsou volant a pedály vlaku. Každý vlak je musí mít.",
            "Výroba: páka, vlakové pouzdro a precizní strojek.",
            "&aDruhé ovládání otočené na opačnou stranu dovolí vlaku odjíždět ze stanic oběma směry. Hodí se pro trať tam a zpět.&r"]),
        Q("first_train", "Sestav první vlak", icon="create:railway_casing", dep=["controls", "create:bearing"],
          tasks=[adv("create:train")], xp=60, shape="octagon", size=1.25, d=[
            "Teď z bloků uděláš jedoucí vlak. Postup:",
            "1. Otevři stanici (pravé tlačítko) a přepni ji do režimu sestavování (&eAssembly Mode&r).",
            "2. Klikni vlakovým pouzdrem na kolej u stanice. Vznikne podvozek. Dalším kliknutím změníš jeho vzhled.",
            "3. Na podvozek postav vagon a slep ho vteřinovým lepidlem (&eSuper Glue&r). Přidej ovládání vlaku.",
            "4. V okně stanice potvrď sestavení. Z bloků se stane vlak.",
            "{@pagebreak}",
            "Řízení: klikni na ovládání. Klávesy pohybu = jízda a zatáčení, kolečko myši = nejvyšší rychlost, drž mezerník = zastav u blízké stanice, Shift = konec řízení.",
            "&cVlak se dá rozebrat zpět na bloky jen ve stanici.&r Montážním klíčem ho můžeš přesunout na blízkou kolej."]),
        Q("seat", "Sedačky", dep=["controls"], items=[("create:white_seat", 2)], xp=15, d=[
            "Sedačka (&eSeat&r) je místo pro cestující. Na jedoucím vlaku na ní můžeš sedět ty, kamarád i zvíře.",
            "Sedačka přímo před ovládáním je místo strojvůdce. Usaď tam zvíře nebo vesničana a vlak bude moct jezdit sám.",
            "&aZvíře na vodítku usadíš snadno: klikni s ním na sedačku. Výroba: vlna a dřevěná deska.&r"]),
        Q("door", "Vlakové dveře", dep=["first_train"], items=[("create:train_door", 2)], xp=20, d=[
            "Vlakové dveře (&eTrain Door&r) jsou dveře do vagonů. Vyrobíš je z dřevěných dveří a vlakového pouzdra.",
            "V základním režimu se samy otevřou, když vlak zastaví, a zavřou se, když se rozjede.",
            "&aDo podlahy nebo střechy se hodí vlakový poklop (&eTrain Trapdoor&r).&r"]),
        Q("schedule", "Jízdní řád", dep=["first_train"], items=[("create:schedule", 1)], xp=40, d=[
            "Jízdní řád (&eTrain Schedule&r) je seznam příkazů pro strojvůdce: kam jet a na co čekat. Robustní plát a papír dají 4 jízdní řády.",
            "Vezmi ho do ruky, klikni pravým tlačítkem a přidávej řádky. Hlavní příkaz je &eTravel to Station&r (jeď do stanice). Za něj dej podmínku, třeba &eScheduled Delay&r (počkej) nebo &eCargo Inactivity&r (počkej na konec nakládky).",
            "Zapni &eLoop Forever&r a vlak bude jezdit pořád dokola.",
            "&aV názvu stanice můžeš použít hvězdičku *. Například „Nádraží *“ znamená jakékoli nástupiště, jehož jméno začíná slovem Nádraží. Vlak si vybere nejbližší volné.&r"]),
        # ---------- Pokročilý: automatické vlaky ----------
        Q("driver", "Vlak jezdí sám", icon="create:schedule", dep=["schedule", "seat"],
          tasks=[adv("create:conductor")], xp=60, shape="hexagon", size=1.5, s="Pokročilý", d=[
            "Teď už nemusíš řídit sám. Dej jízdní řád strojvůdci a vlak bude jezdit podle něj.",
            "Strojvůdce je zvíře nebo vesničan, který sedí na sedačce přímo před ovládáním. Klikni na něj s naprogramovaným jízdním řádem.",
            "&aStrojvůdcem může být i ohňohořák (&eBlaze Burner&r) položený před ovládáním. Nemusíš chytat žádné zvíře.&r",
            "Jízdní řád si od strojvůdce kdykoli vezmeš zpět. Když ho vložíš do stanice, sám se zkopíruje do každého vlaku, který tam zastaví."]),
        Q("signal", "Návěstidla", dep=["station"], items=[("create:track_signal", 2)], xp=40, d=[
            "Návěstidlo (&eTrain Signal&r) rozdělí trať na úseky. V jednom úseku smí být jen jeden vlak, takže se vlaky nesrazí.",
            "Výroba: vlakové pouzdro a elektronka dají 4 návěstidla. Pokládá se jako stanice: klikni na kolej a polož ho vedle ní.",
            "&cNávěstidla řídí jen vlaky s jízdním řádem. Když řídíš sám, musíš dávat pozor.&r",
            "Redstonem návěstidlo přepneš na červenou. Červené návěstidlo naopak dává signál pro komparátor.",
            "{@pagebreak}",
            "&eDvoukolejka:&r vlak s jízdním řádem nikdy neprojede návěstidlo z opačné strany. Výjimka je, když tam stojí druhé návěstidlo otočené opačně.",
            "Na dvou souběžných kolejích proto dej návěstidla na každé koleji jen jedním směrem. Každá kolej bude jednosměrná a vlaky se nepotkají čelně.",
            "&eKřižovatky:&r montážním klíčem přepneš návěstidlo do druhého režimu. Pak pustí vlak dál, jen když může další úsek hned zase opustit. Dej ho před křižovatku, ať se v ní vlaky nezaseknou."]),
        Q("observer", "Detektor vlaku", dep=["signal"], items=[("create:track_observer", 1)], xp=30, d=[
            "Detektor vlaku (&eTrain Observer&r) dá redstonový signál, když přes jeho značku projede vlak.",
            "Pokládá se jako stanice: klikni na kolej a polož ho vedle. Filtrem nastavíš, aby reagoval jen na vlak s určitým nákladem.",
            "&aPoužij ho na závory, světla, zvonek nebo počítání vlaků.&r"]),
        Q("psi", "Nakládka bez rukou", icon="create:portable_storage_interface", dep=["first_train"],
          tasks=[adv("create:portable_storage_interface")], xp=50, d=[
            "Ruční přenášení věcí z vlaku zdržuje. Přenosné úložné rozhraní (&ePortable Storage Interface&r) vlak naloží a vyloží samo.",
            "Výroba: andezitové pouzdro a šachta. Jedno rozhraní dej na vlak, druhé na nástupiště. Mezi nimi musí být mezera 1 nebo 2 bloky. Když se potkají, spojí se.",
            "Rozhraní na nástupišti pak funguje jako všechny truhly vlaku dohromady. Věci do něj posílej trychtýřem nebo šachtou, nebo je z něj vytahuj.",
            "&aV jízdním řádu použij podmínku &eCargo Inactivity&a – vlak odjede, až se nakládka zastaví.&r",
            "Vlakem můžeš posílat i balíky z Create. Klikni poštovní schránkou (&ePostbox&r) na stanici, polož ji poblíž a dej jí adresu. Vlak tu naloží balíky s cizí adresou a vyloží ty s její adresou."]),
        Q("fluid_if", "Cisterna", dep=["psi"], items=[("create:portable_fluid_interface", 1)], xp=30,
          optional=True, d=[
            "Přenosné rozhraní tekutin (&ePortable Fluid Interface&r) dělá totéž pro tekutiny. Vlak s nádržemi pak vozí vodu, lávu i jiné tekutiny.",
            "Výroba: měděné pouzdro (&eCopper Casing&r) a šachta. Místo trychtýřů k němu připoj potrubí."]),
        Q("fuel", "Palivo pro vlak", dep=["first_train"], items=[("railways:fuel_tank", 1)], xp=30, d=[
            "Vlak jezdí i bez paliva, ale s palivem jede rychleji. Hledá ho v truhlách a sudech, které jsou součástí vlaku. Palivo v trezoru (&eItem Vault&r) vlak nespotřebuje.",
            "Palivová nádrž (&eFuel Tank&r) ze &bSteam 'n' Rails&r veze tekuté palivo, například lávu. Obyčejnou vodu nepřijme.",
            "Výroba: nádrž (&eFluid Tank&r) mezi dvěma robustními pláty."]),
        Q("fuel_if", "Tankovací stanice", dep=["fuel", "psi"],
          items=[("railways:portable_fuel_interface", 1)], xp=25, optional=True, d=[
            "Přenosné rozhraní paliva (&ePortable Fuel Interface&r) doplní palivové nádrže vlaku přímo na nástupišti.",
            "Výroba: vlakové pouzdro a šachta. Staví se stejně jako přenosné úložné rozhraní: jedno na vlak, druhé na nástupiště."]),
        Q("whistle", "Tú tú!", icon="create:steam_whistle", dep=["first_train"],
          tasks=[adv("create:train_whistle")], xp=20, optional=True, d=[
            "Parní píšťala (&eSteam Whistle&r) na vlaku houká. Přidej ji na vlak před sestavením a za jízdy zmáčkni klávesu sprintu.",
            "Výroba: zlatý plát a měděný ingot."]),
        # ---------- Expert: velká síť ----------
        Q("display", "Odjezdová tabule", icon="create:display_board", dep=["driver", "signal"],
          tasks=[adv("create:display_board_0")], xp=60, shape="hexagon", size=1.5, s="Expert", d=[
            "Velké nádraží potřebuje přehled. Displejová tabule (&eDisplay Board&r) ukáže, kdy přijede který vlak.",
            "Postav tabuli a roztoč ji – potřebuje rotaci. Displejovým vysílačem (&eDisplay Link&r) klikni nejdřív na tabuli, pak ho polož na stanici. V jeho okně vyber &eTrain Station Summary&r.",
            "&aOd teď stavíš velkou síť: víc vlaků, nástupišť a křižovatek. Další questy jsou pro zkušené.&r"]),
        Q("long_train", "Dlouhý vlak", icon="create:railway_casing", dep=["display"],
          tasks=[adv("create:long_train")], xp=60, d=[
            "Postav vlak, který má aspoň 6 vagonů.",
            "Každý vagon stojí na vlastním podvozku (nebo na dvou) a je slepený zvlášť. Všechny vagony postav za sebou u stanice a sestav je najednou.",
            "&aDelší vlak uveze víc, ale potřebuje delší nástupiště.&r"]),
        Q("long_travel", "Dlouhá cesta", icon="create:white_seat", dep=["driver"],
          tasks=[adv("create:long_travel")], xp=50, optional=True, d=[
            "Vystup ze sedačky ve vlaku víc než 5000 bloků od místa, kde jsi nastoupil.",
            "&aVlaky jezdí i tam, kde svět není načtený (v nenačtených chuncích). Zastaví tam ve stanicích i na červené. Jen stroje na vlaku, třeba vrtáky, tam nepracují.&r"]),
        Q("portal", "Vlakem do Netheru", icon="minecraft:obsidian", dep=["display"],
          tasks=[adv("create:train_portal")], xp=50, optional=True, d=[
            "Polož kolej až těsně k netherskému portálu. Na druhé straně se sama vytvoří navazující kolej a vlak pak projede do druhé dimenze.",
            "&aV Netheru je každá vzdálenost 8× kratší. Trať přes Nether je nejrychlejší cesta na velkou dálku.&r"]),
        Q("coupler", "Spřáhlo", dep=["signal", "display"], items=[("railways:track_coupler", 1)], xp=40, d=[
            "Spřáhlo (&eTrain Coupler&r) ze &bSteam 'n' Rails&r spojí nebo rozpojí vagony bez rozebírání vlaku.",
            "Pokládá se jako stanice. Má dvě značky na koleji a na každé musí stát podvozek. Mezeru mezi značkami měníš kolečkem myši s montážním klíčem.",
            "Montážním klíčem přepínáš režim: spojování, rozpojování nebo obojí. Akci spustí redstonový signál.",
            "&aTak postavíš nákladní nádraží, kde lokomotiva nechá vagony a odjede pro další.&r"]),
        # ---------- Steam 'n' Rails: ruční vozítka a výhybky ----------
        Q("handcar", "Drezína", dep=["track"], items=[("railways:handcar", 1)], xp=30, d=[
            "Drezína (&eHandcar&r) je malé vozítko na ruční pohon. Nepotřebuje stanici ani vlakové pouzdro.",
            "Polož ji rovnou na koleje, nasedni a jeď. Jízda ti ubírá jídlo, protože jedeš vlastní silou. Montážním klíčem ji zase sebereš.",
            "&aVýroba potřebuje mimo jiné ovládací prvky udělátka (&eContraption Controls&a) a andezitové pouzdro.&r"]),
        Q("benchcart", "Vozík s pracovním stolem", dep=["track"], items=[("railways:benchcart", 1)], xp=20,
          optional=True, d=[
            "Vozík s pracovním stolem (&eMinecart with Workbench&r) vyrobíš z vozíku a pracovního stolu.",
            "Existuje i vozík s jukeboxem (&eMinecart with Jukebox&r).",
            "&aObojí jezdí po obyčejných kolejích pro vozíky, ne po vlakových.&r"]),
        Q("switch", "Výhybka", dep=["track"], items=[("railways:track_switch_andesite", 1)], xp=30, d=[
            "Andezitová výhybka (&eAndesite Track Switch&r) určuje, kam vlak na rozdvojení pojede.",
            "Pokládá se jako stanice: klikni na kolej u rozdvojení a polož výhybku vedle. Kliknutím ji přepneš doprava, se Shiftem doleva.",
            "Směr nastavíš i redstonem. Signálem do spodní části výhybku zamkneš. Komparátor z ní přečte směr: 0 rovně, 1 vlevo, 2 vpravo.",
            "&aVlaky s jízdním řádem si cestu přes rozdvojení najdou samy. Výhybka se hodí tam, kde chceš směr určit ty.&r"]),
        Q("switch_brass", "Mosazná výhybka", dep=["switch", "create:precision"],
          items=[("railways:track_switch_brass", 1)], xp=30, d=[
            "Mosazná výhybka (&eBrass Track Switch&r) umí totéž co andezitová. Navíc ji přepneš přímo z vlaku, který k ní přijíždí. Na jejím panelu nastavíš, jestli ji smí přepínat i vlaky s jízdním řádem.",
            "Výroba: páka, mosazné pouzdro a precizní strojek."]),
        Q("semaphore", "Semafor", dep=["signal"], items=[("railways:semaphore", 1)], xp=25, d=[
            "Semafor (&eSemaphore&r) je klasické rameno, které ukazuje stav návěstidla pod ním.",
            "Postav nad návěstidlo sloup, třeba z plotu nebo kovového nosníku, a semafor dej na něj. Výroba: železné pláty, plot, andezitové pouzdro a elektronka dají 4 semafory.",
            "&aU návěstidla pro křižovatky můžeš dát dva semafory nad sebe. Spodní se zavře, když je zablokovaná aspoň jedna cesta, horní až když jsou zablokované všechny.&r"]),
        # ---------- Steam 'n' Rails: průvodčí ----------
        Q("cap", "Čepice průvodčího", dep=["driver", "create:precision"],
          items=[("railways:white_conductor_cap", 1)], xp=30, d=[
            "Průvodčí (&eConductor&r) ze &bSteam 'n' Rails&r je malý pomocník. Vznikne, když nasadíš čepici průvodčího (třeba &eWhite Conductor's Cap&r) na blok andezitového pouzdra.",
            "Čepice se vyrábí sekvenční montáží z vlny: pila ji ořízne, pokladače přidají precizní strojek a provázek. Barvu změníš barvivem v pracovním stole.",
            "&aPrůvodčí může řídit vlak jako strojvůdce – posaď ho na sedačku před ovládání.&r"]),
        Q("conductor", "Píšťala průvodčího", dep=["cap"], items=[("railways:conductor_whistle", 1)], xp=40, d=[
            "Píšťala průvodčího (&eConductor Whistle&r) přivolá vlak k tobě.",
            "Klikni píšťalou na průvodčího, který sedí ve vlaku. Tím ji s vlakem spojíš. Pak klikni píšťalou na kolej nebo stanici a vlak tam přijede.",
            "Výroba: měděný ingot a mosazný nuget."]),
        Q("lens", "Dálková čočka", dep=["conductor"], items=[("railways:remote_lens", 1)], xp=30,
          optional=True, d=[
            "Dálková čočka (&eRemote Lens&r) ti ukáže svět očima průvodčího.",
            "Klikni čočkou na průvodčího, který nosí inženýrské brýle. Tím je spojíš a pak se můžeš dívat jeho očima.",
            "Výroba: precizní strojek, oko Enderu a mosazný plát."]),
        # ---------- Steam 'n' Rails: druhy kolejí ----------
        Q("track_wood", "Dřevěné koleje", dep=["track"], items=[("railways:track_oak", 16)], xp=20, d=[
            "&bSteam 'n' Rails&r přidává koleje s pražci z každého druhu dřeva. Vyrábí se jako běžná kolej, jen místo kamenné desky použij dřevěnou.",
            "Z dubové desky tak vznikne dubová kolej (&eOak Train Track&r). Jezdí se po ní stejně, liší se jen vzhledem.",
            "&aKolej z černého kamene (&eBlackstone Train Track&a) potřebuje zlaté nugety. Endová kolej (&eEnder Train Track&a) potřebuje desku z endových cihel. Kolej bez pražců (&eTieless Train Track&a) potřebuje skleněnou tabuli.&r"]),
        Q("wide", "Široký rozchod", dep=["track", "create:drill"],
          items=[("railways:track_create_andesite_wide", 16)], xp=30, d=[
            "Široká kolej (&eWide Andesite Train Track&r) má větší rozchod. Hodí se pro mohutné vlaky.",
            "Vyrábí se z běžné koleje: mechanická pila ji rozřízne, pokladač přidá desku a lis ji stiskne.",
            "&cNa širokou kolej potřebuješ široký podvozek.&r S vlakovým pouzdrem v ruce zmáčkni Alt – otevře se nabídka podvozků. Vyber v ní podvozek pro širokou kolej."]),
        Q("narrow", "Úzký rozchod", dep=["track", "create:drill"],
          items=[("railways:track_create_andesite_narrow", 16)], xp=30, d=[
            "Úzká kolej (&eNarrow Andesite Train Track&r) má menší rozchod. Je skvělá na malé vláčky.",
            "Vyrábí se z kamenné desky: pila ji ořízne, pokladač přidá nuget a lis ji stiskne.",
            "Na úzkou kolej patří úzký podvozek. Vybereš ho v nabídce podvozků (Alt s vlakovým pouzdrem v ruce)."]),
        Q("monorail", "Jednokolejka", dep=["track", "create:deployer"], items=[("railways:track_monorail", 6)], xp=40, d=[
            "Jednokolejka (&eMonorail Train Track&r) je jediná kolejnice na nosníku. Vypadá moderně a hodí se do měst.",
            "Vyrábí se z kovového nosníku (&eMetal Girder&r): pokladače přidají kovový držák a železný plát, lis vše stiskne. Vznikne 6 kusů.",
            "Jezdí po ní jednokolejkový podvozek (&eMonobogey&r) z nabídky podvozků."]),
        Q("phantom", "Neviditelná kolej", dep=["track"], items=[("railways:track_phantom", 16)], xp=30,
          optional=True, d=[
            "Fantomová kolej (&ePhantom Train Track&r) je neviditelná. Uvidíš ji jen tehdy, když ji držíš v ruce.",
            "Vyrábí se z blány fantoma: pokladače přidají dva železné ingoty a lis ji stiskne. Vznikne rovnou 32 kusů.",
            "&aS neviditelným podvozkem z nabídky podvozků pak vlak vypadá, jako by jel vzduchem.&r"]),
        # ---------- Vzhled lokomotivy: lokokov a Bells & Whistles ----------
        Q("locometal", "Lokokov", dep=["first_train"], items=[("railways:riveted_locometal", 8)], xp=20, d=[
            "Lokokov (&eLocometal&r) je sada kovových bloků pro stavbu opravdových lokomotiv: plechy, kotle, dýmnice, okna i dveře.",
            "Kamenořez udělá z jednoho železného bloku 8 kusů nýtovaného lokokovu (&eRiveted Locometal&r). Další tvary pak vybereš v kamenořezu.",
            "&aNěkteré bloky mají více variant. Podrž Alt a vyber si.&r"]),
        Q("paint", "Barvy na lokomotivu", dep=["locometal", "create:mixer"],
          items=[("railways:red_riveted_locometal", 8)], xp=30, d=[
            "Lokokov můžeš obarvit. Nejdřív vyrob barvu: v míchačce smíchej barvivo, hroudu jílu a vodu.",
            "Pak dej do tyglíku pod míchačkou lokokov a barvu – vyjde obarvený lokokov. Jedna dávka barvy stačí na 8 bloků.",
            "&aKromě běžných barev jsou i zvláštní odstíny, třeba kaštanová (&eMaroon&a). Vzniknou smícháním dvou barev.&r"]),
        Q("boiler", "Kotel lokomotivy", dep=["locometal", "create:crafter"],
          items=[("railways:locometal_boiler", 4)], xp=30, optional=True, d=[
            "Kotel z lokokovu (&eLocometal Boiler&r) je válcový blok. Vypadá jako kotel parní lokomotivy.",
            "Vyrábí se v mechanickém výrobníku (&eMechanical Crafter&r) ze sekaného lokokovu (&eSlashed Locometal&r), ohnivých tyčí a kbelíku. Vzniknou 4 kusy.",
            "&aNa kotel patří komín (&eDouble Smokestack&a) z táboráku a železných nugetů.&r"]),
        Q("headlight", "Světlomet", dep=["locometal"], items=[("bellsandwhistles:headlight", 1)], xp=20, d=[
            "&bBells & Whistles&r přidává drobnosti pro vlaky a nádraží. Začni světlometem (&eHeadlight&r) na předek lokomotivy.",
            "Výroba: pochodeň a železné nugety dají 2 světlomety."]),
        Q("platform", "Nástupiště", dep=["headlight"], items=[("bellsandwhistles:station_platform", 8)], xp=20, d=[
            "Blok nástupiště (&eStation Platform&r) postav podél koleje u stanice. Cestující pak nastupují pohodlně.",
            "Vyrobíš ho v kamenořezu z hladkého kamene (2 kusy) nebo v pracovním stole z hladkého kamene a hladké kamenné desky."]),
        Q("metro", "Metro", dep=["headlight"], items=[("bellsandwhistles:metro_casing", 4)], xp=15,
          optional=True, d=[
            "Pouzdro metra (&eMetro Casing&r) je zelený plech pro moderní vlaky a metro. Železný plát a zelené barvivo dají 4 kusy.",
            "Z pouzdra vyrobíš panely (&eMetro Panel&r) a okna (&eMetro Window&r). Vroubkovanou verzi (&eCorrugated Metro Casing&r) dostaneš v pracovním stole z jednoho pouzdra."]),
        Q("pilot", "Pluh lokomotivy", dep=["headlight"], items=[("bellsandwhistles:metal_pilot", 1)], xp=15,
          optional=True, d=[
            "Pluh (&ePilot&r) je mříž na předku lokomotivy. Je to ozdoba, která dodá lokomotivě opravdový vzhled.",
            "Kovový pluh (&eMetal Pilot&r) je ze železných plátů a nugetů. Jsou i verze z andezitu, mosazi, mědi a leštěných kamenů."]),
        Q("grab", "Madla a schůdky", dep=["headlight"], items=[("bellsandwhistles:brass_grab_rails", 4)], xp=15,
          optional=True, d=[
            "Madla, třeba mosazná (&eBrass Grab Bars&r), a schůdky, třeba mosazné (&eBrass Steps&r), dodají vagonu detaily.",
            "Vyrábí se z mosazi, mědi nebo andezitové slitiny, v pracovním stole i v kamenořezu."]),
    ],
)

# =====================================================================
# CREATE AERONAUTICS – létající stroje (Aeronautics, Simulated, Offroad, Sable)
# =====================================================================
AERO = dict(
    key="aeronautics", group="create", title="Létající stroje",
    subtitle="Create Aeronautics: lodě, které opravdu létají", icon="aeronautics:propeller_bearing",
    quests=[
        # ---------- Začátečník: sestavení a balón ----------
        Q("start", "Fyzika!", s="Začátečník", icon="simulated:physics_assembler", tasks=[auto()], xp=10,
          shape="hexagon", size=1.5, d=[
            "&bCreate Aeronautics&r udělá ze staveb z Create skutečné fyzikální stroje. Mají váhu, padají, plavou a létají. Fyziku počítají mody &bSimulated&r a &bSable&r.",
            "V kapitole postavíš nejdřív balón, pak loď s vrtulemi a řízením, auto na kolech a nakonec loď, která se řídí sama.",
            "&aPotřebuješ základy Create: hřídele, ložiska a vteřinové lepidlo.&r Server dovoluje létání, takže tě za let na lodi nevyhodí.",
            "&cNa tomto serveru jde najednou sestavit nejvýš 8192 bloků.&r"]),
        Q("assembler", "Fyzikální sestavovač", dep=["start", "create:bearing"],
          items=[("simulated:physics_assembler", 1)], xp=40, d=[
            "Fyzikální sestavovač (&ePhysics Assembler&r) je srdce každého létajícího stroje. Z bloků udělá fyzikální stroj (&eSimulated Contraption&r).",
            "Výroba: páka, andezitové pouzdro a dvě andezitové slitiny.",
            "Postup: slep bloky vteřinovým nebo medovým lepidlem. Sestavovač musí být uvnitř slepené oblasti. Pak drž na sestavovači pravé tlačítko a stáhni páku. Připojí se i bloky, které se dotýkají jen hranou.",
            "{@pagebreak}",
            "Rozebrat stroj zpět na bloky umí kterýkoli sestavovač. &cStroj ale musí stát skoro rovně, skoro v klidu a blízko země. Ve vzduchu ho rozebrat nejde.&r",
            "&aČásti stroje, které nic nedrží, se odtrhnou. Dva stroje spojíš kliknutím slizovou koulí.&r"]),
        Q("honey", "Medové lepidlo", dep=["assembler", "create:spout"],
          items=[("simulated:honey_glue", 1)], xp=25, d=[
            "Medové lepidlo (&eHoney Glue&r) je pohodlnější lepidlo pro fyzikální stroje. Lepí jen je, obyčejné stroje z Create ne.",
            "Vyrobíš ho dávkovačem: naplň železný plát medem.",
            "Klikni na dva rohy – vznikne slepený kvádr. Ctrl + kolečko myši ho zvětší nebo zmenší, s klávesou Alt položíš roh i do vzduchu.",
            "&aU složitých staveb je lepší než vteřinové lepidlo, protože nepřilepí nic navíc.&r"]),
        Q("diagram", "Plánek stroje", dep=["assembler"], items=[("simulated:contraption_diagram", 1)], xp=20, d=[
            "Plánek stroje (&eContraption Diagram&r) ukáže síly, které působí na tvůj stroj. Výroba: papír a fyzikální sestavovač. Klikni s ním na stroj.",
            "Každý blok má jinou váhu a vlastnosti. S nasazenými brýlemi je uvidíš v popisku bloku.",
            "&aTěžké bloky dávej doprostřed a dolů. Stroj se pak tolik nepřevrací.&r"]),
        Q("nameplate", "Jmenovka", dep=["assembler"], items=[("simulated:white_nameplate", 1)], xp=10,
          optional=True, d=[
            "Jmenovka (&eNameplate&r) dá tvému stroji jméno. Papír, tyčka a andezitová slitina dají 4 jmenovky.",
            "Klikni na ni a napiš jméno. Barvivem změníš barvu písma, plástvem medu text zamkneš. Všechny jmenovky na jednom stroji ukazují stejné jméno."]),
        Q("handle", "Madlo", dep=["assembler"], items=[("simulated:iron_handle", 1)], xp=10, optional=True, d=[
            "Madlo (&eIron Handle&r) se dá chytit. Drž na něm pravé tlačítko a přitáhneš se k němu, i na letící lodi.",
            "Se Shiftem naopak táhneš za madlo celý stroj. Výroba: železný nuget nad andezitovou slitinou."]),
        Q("envelope", "Obal balónu", dep=["start"], items=[("aeronautics:white_envelope", 16)], xp=20, d=[
            "Obal balónu (&eHot Air Envelope&r) je látka na stavbu balónu. Z obalů postav uzavřený prostor – to je balón.",
            "Výroba: 2 bílé vlny a 2 tyčky dají 4 obaly. Barvivem je obarvíš.",
            "&cBalón musí být vzduchotěsný. Těsní jen obaly a vlna, jinudy horký vzduch uteče.&r Hřídel vedoucí skrz balón obal tak, že na ni klikneš obalem.",
            "Bloky uvnitř balónu zmenšují jeho objem."]),
        Q("burner", "Hořák", dep=["envelope"], items=[("aeronautics:adjustable_burner", 1)], xp=40, d=[
            "Hořák horkého vzduchu (&eHot Air Burner&r) plní balón horkým vzduchem. Postav ho pod balón.",
            "Nepotřebuje palivo, stačí mu redstonový signál. Čím silnější signál, tím víc vzduchu. Nejvyšší výkon nastavíš na jeho panelu.",
            "Výroba: železné pláty, uhelný blok, redstone a andezitová slitina.",
            "&aJeden balón může plnit víc hořáků. Vztlak je ale omezený velikostí balónu – větší balón unese víc.&r"]),
        # ---------- Pokročilý: pohon a řízení ----------
        Q("balloon", "Poprvé ve vzduchu", icon="aeronautics:white_envelope", dep=["burner", "assembler"],
          tasks=[adv("aeronautics:head_in_the_clouds")], xp=60, shape="hexagon", size=1.5, s="Pokročilý", d=[
            "Postav první létající stroj – horkovzdušný balón:",
            "1. Postav plošinu a na ni fyzikální sestavovač a hořák.",
            "2. Nad hořák postav z obalů balón. Hořák ho plní zespodu a horký vzduch se drží nahoře.",
            "3. Vše slep lepidlem a sestav stroj pákou na sestavovači.",
            "4. Dej hořáku redstonový signál, třeba pákou na plošině. Balón se nafoukne a stroj vzlétne.",
            "{@pagebreak}",
            "&aČím výš letíš, tím je vztlak slabší. Stroj se ustálí ve výšce, kde se vztlak a váha vyrovnají. Silnějším signálem vystoupáš, slabším klesneš.&r",
            "&cBalón sám neumí letět dopředu. Na to potřebuješ vrtule.&r"]),
        Q("steam_vent", "Parní výduch", dep=["balloon", "create:steam"],
          items=[("aeronautics:steam_vent", 1)], xp=40, optional=True, d=[
            "Parní výduch (&eSteam Vent&r) plní balón párou místo horkého vzduchu.",
            "Potřebuje to samé co parní motor: kotel z nádrží, vodu a teplo. Výkon nastavíš panelem a redstonem. Víc výduchů potřebuje dost silný kotel.",
            "Výroba: zlatý plát na měděném bloku."]),
        Q("small_prop", "Malá vrtule", dep=["assembler"], items=[("aeronautics:andesite_propeller", 1)], xp=30, d=[
            "Andezitová vrtule (&eAndesite Propeller&r) je nejjednodušší pohon. Roztoč ji hřídelí a začne tlačit vzduch – a s ním celý stroj.",
            "Výroba: vrtule z Create (&ePropeller&r), dřevěná deska a hřídel. V pracovním stole ji předěláš na dřevěnou vrtuli (&eWooden Propeller&r) a zase zpět.",
            "Směr tahu otočíš opačnou rotací nebo montážním klíčem. Tah a proud vzduchu ukážou inženýrské brýle.",
            "&cVe velké výšce a při velké rychlosti vrtule táhne slaběji.&r"]),
        Q("propeller", "Velká vrtule", dep=["small_prop", "create:brass"],
          items=[("aeronautics:propeller_bearing", 1), ("aeronautics:wooden_propeller", 1)], xp=40, d=[
            "Vrtulové ložisko (&ePropeller Bearing&r) roztočí vrtuli, kterou si postavíš sám. Připojí se k bloku před sebou, podobně jako mechanické ložisko.",
            "Listy vrtule postav z větrných plachet (&eWindmill Sail&r). Vrtule musí mít aspoň 2 bloky plachet. Víc plachet = účinnější vrtule.",
            "Výroba: dřevěná deska, železný plát a mosazné pouzdro.",
            "&aDřevěná vrtule z úkolu je hotová malá vrtule – stačí ji roztočit.&r"]),
        Q("goggles", "Letecké brýle", dep=["propeller"], items=[("aeronautics:aviators_goggles", 1)], xp=20, d=[
            "Letecké brýle (&eAviator's Goggles&r) fungují stejně jako inženýrské brýle, jen vypadají jako pro pilota.",
            "Výroba: inženýrské brýle a kůže.",
            "&aS brýlemi uvidíš tah vrtulí, údaje o balónu a výšku i tlak vzduchu na výškoměru.&r"]),
        Q("gyro_mech", "Gyroskopický mechanismus", dep=["propeller", "create:deployer"],
          items=[("simulated:gyroscopic_mechanism", 1)], xp=40, d=[
            "Gyroskopický mechanismus (&eGyroscopic Mechanism&r) je díl pro chytré vrtule a senzor náklonu.",
            "Vyrábí se sekvenční montáží jako precizní strojek: na železný plát pokladače přidají ozubené kolečko, hřídel a mosazný nuget. Postup se opakuje 5×."]),
        Q("gyro", "Vrtulník", dep=["gyro_mech"], items=[("aeronautics:gyroscopic_propeller_bearing", 1)], xp=60, d=[
            "Gyroskopické vrtulové ložisko (&eGyroscopic Propeller Bearing&r) drží vrtuli svisle, i když se stroj nakloní. Proto se hodí na vrtulníky.",
            "Otočené dolů pomůže udržet stabilní i stavbu, která je nahoře těžší. Redstonový signál vrátí náklon vrtule na nulu.",
            "Výroba: dřevěná deska, gyroskopický mechanismus a mosazné pouzdro."]),
        Q("smart_prop", "Chytrá vrtule", dep=["gyro_mech"], items=[("aeronautics:smart_propeller", 1)], xp=60, d=[
            "Chytrá vrtule (&eSmart Propeller&r) je malá vrtule, která se sama naklání tak, aby mířila nahoru.",
            "Hodí se na malé létající stroje. Montážním klíčem otočíš směr tahu.",
            "Výroba: vrtule z Create, gyroskopický mechanismus a mosazné pouzdro dají 2 kusy."]),
        Q("wings", "Křídla a kormidla", dep=["propeller"], items=[("simulated:white_symmetric_sail", 2)], xp=30, d=[
            "Obyčejné větrné plachty (&eWindmill Sail&r) na letícím stroji fungují jako křídla. Čím rychleji letíš, tím víc nadnášejí. Tak postavíš letadlo.",
            "Souměrná plachta (&eSymmetric Sail&r) nenadnáší, jen brzdí vzduch. Natočená šikmo ke směru letu poslouží jako kormidlo nebo stabilizátor.",
            "Výroba: 2 plachty z Create dají 2 souměrné plachty. K blokům se přichytí samy, bez lepidla."]),
        Q("nozzle", "Vznášedlo", dep=["small_prop"], items=[("create:nozzle", 1)], xp=25, optional=True, d=[
            "Tryska (&eNozzle&r) na zapouzdřeném větráku odtlačuje fyzikální stroj od blízkých povrchů – od země, stěn i vody.",
            "&aVětráky s tryskami pod strojem udělají vznášedlo, které se drží nad zemí nebo nad vodou.&r"]),
        Q("engine", "Sestava motoru", dep=["assembler", "create:drill"],
          items=[("simulated:engine_assembly", 1)], xp=40, d=[
            "Sestava motoru (&eEngine Assembly&r) je hlavní díl přenosného motoru.",
            "Vyrábí se sekvenční montáží ze železného plátu: mechanická pila ho ořízne a lis stiskne. Opakuje se to 8×."]),
        Q("portable", "Přenosný motor", dep=["engine"], items=[("simulated:red_portable_engine", 1)], xp=40, d=[
            "Přenosný motor (&ePortable Engine&r) je zdroj rotace přímo na lodi. Pálí paliva jako pec, třeba uhlí nebo dřevo.",
            "Výroba: železný plát, sestava motoru a vysoká pec. Barvivem ho v pracovním stole přebarvíš.",
            "Směr otáčení se dá přepnout. Palivo do něj můžeš dodávat i automaticky.",
            "&aOhňodort (&eBlaze Cake&a) ho přetopí na vyšší výkon.&r"]),
        Q("steering", "Kormidelní kolo a plyn", dep=["portable"],
          items=[("simulated:steering_wheel", 1), ("simulated:throttle_lever", 1)], xp=40, d=[
            "Kormidelní kolo (&eSteering Wheel&r) dává přesnou rotaci. Drž na něm pravé tlačítko a otáčej myší. Se Shiftem skáče po 45°.",
            "Napoj ho hřídelí na ložisko, které otáčí směrovkou nebo vrtulí, a budeš zatáčet. &cLožisku musíš nastavit, že se nemá rozebírat.&r",
            "Plynová páka (&eThrottle Lever&r) dává plynule nastavitelný redstonový signál – klikni a táhni. Napoj ji na hořák a ovládáš výšku letu."]),
        Q("swivel", "Otočné ložisko", dep=["steering"], items=[("simulated:swivel_bearing", 1)], xp=40, d=[
            "Otočné ložisko (&eSwivel Bearing&r) připojí ke stroji druhý fyzikální stroj, který se může otáčet. Hodí se na kormidlo, otočnou věž nebo natáčecí motor.",
            "Připojí se k bloku před sebou. Bloky slep lepidlem a roztoč ozubené kolečko ložiska – část se sestaví.",
            "Rotace z hřídele projde ložiskem dál. Redstonový signál ložisko odemkne a pak se točí volně.",
            "Výroba: dřevěná deska, blok průmyslového železa a ozubené kolečko."]),
        # ---------- Expert: autopilot ----------
        Q("sensors", "Přístroje", dep=["steering"], s="Expert", shape="hexagon", size=1.5,
          items=[("simulated:altitude_sensor", 1), ("simulated:velocity_sensor", 1)], xp=40, d=[
            "Teď stroj naučíš řídit se sám. Senzory měří let a dávají redstonový signál – z nich postavíš autopilota.",
            "Výškoměr (&eAltitude Sensor&r) dává signál podle výšky. Rozsah nastavíš v jeho okně a signál umí i obrátit. Napoj ho na hořák a stroj udrží výšku.",
            "Rychloměr (&eVelocity Sensor&r) dává signál podle rychlosti ve směru, kam míří."]),
        Q("gimbal", "Senzor náklonu", dep=["sensors", "gyro_mech"],
          items=[("simulated:gimbal_sensor", 1)], xp=40, d=[
            "Senzor náklonu (&eGimbal Sensor&r) dává signál podle toho, jak je stroj nakloněný. Každá osa funguje zvlášť.",
            "Signál vychází na straně, která je níž. Napoj ho na vrtule na okrajích stroje a nižší strana přidá tah – stroj se srovná.",
            "Výroba: kompas, gyroskopický mechanismus a mosazné pouzdro."]),
        Q("nav", "Navigační stůl", dep=["sensors", "create:precision"], items=[("simulated:navigation_table", 1)], xp=50, d=[
            "Navigační stůl (&eNavigation Table&r) dává signál směrem k cíli. Vlož do něj navigační předmět, třeba kompas.",
            "Když stroj nemíří přímo k cíli, signál zeslábne. S tím postavíš autopilota, který stroj sám natáčí k cíli.",
            "Výroba: mosazný plát, precizní strojek a mosazné pouzdro."]),
        Q("optical", "Optický senzor", dep=["sensors"], items=[("simulated:optical_sensor", 1)], xp=30,
          optional=True, d=[
            "Optický senzor (&eOptical Sensor&r) vidí bloky před sebou až na 15 bloků. Síla signálu záleží na vzdálenosti překážky.",
            "Hodí se na hlídání přistání nebo proti nárazu do skály. Filtrem nastavíš, na jaké bloky reaguje."]),
        Q("typewriter", "Dálkové ovládání", dep=["sensors", "create:crafter", "create:precision"],
          items=[("simulated:linked_typewriter", 1)], xp=60, d=[
            "Psací stroj (&eLinked Typewriter&r) promění klávesnici v dálkové ovládání. Každé klávese přiřadíš frekvenci redstonového vysílače (&eRedstone Link&r).",
            "Klikni na něj a zapne se – převezme tvé klávesy pohybu i přiřazené klávesy. Se Shiftem otevřeš nastavení.",
            "Vyrábí se v mechanickém výrobníku z tlačítek, vysílače, zlatých plátů a precizního strojku."]),
        # ---------- Vozidla na kolech ----------
        Q("spring", "Pružina", dep=["assembler"], items=[("simulated:spring", 2)], xp=20, d=[
            "Pružina (&eSpring&r) spojí dva bloky pružným spojem. Je to základ odpružení.",
            "Montážním klíčem změníš tuhost. Kliknutím další pružinou ji prodloužíš, se Shiftem zkrátíš.",
            "Výroba: 2 železné pláty a železný nuget dají 2 pružiny."]),
        Q("wheels", "Vozidla na kolech", dep=["spring"],
          items=[("offroad:wheel_mount", 2), ("offroad:tire", 2)], xp=50, d=[
            "Na zemi jezdí stroje na kolech z &bOffroad&r. Uložení kola (&eWheel Mount&r) drží kolo a roztáčí ho rotací.",
            "Pneumatiku (&eTire&r) nasadíš kliknutím na přední stranu uložení. Signál shora kolo brzdí, signál z boku ho natočí na tu stranu.",
            "Tuhost odpružení nastavíš na panelu uložení.",
            "&aPřidej přenosný motor a zatáčení redstonem – a máš auto.&r"]),
        Q("big_tire", "Obří kola", dep=["wheels"], items=[("offroad:monstrous_tire", 1)], xp=20, optional=True, d=[
            "Kola jsou ve čtyřech velikostech: malá (&eSmall Tire&r), běžná, velká (&eLarge Tire&r) a obří (&eMonstrous Tire&r).",
            "Obří kolo vyrobíš z bloků sušené chaluhy a hřídele, velké z mechanických pásů."]),
        Q("borehead", "Razicí štít", dep=["wheels", "create:crushing"],
          items=[("offroad:borehead_bearing", 1), ("offroad:rockcutting_wheel", 1)], xp=60, d=[
            "Vrtací ložisko (&eBorehead Bearing&r) s kotouči (&eRock Cutting Wheel&r) je razicí štít. Kotouče těží bloky všude kolem sebe.",
            "Kotouče se přichytí samy. Na stroji musí být i úložiště, třeba truhla – vytěžené bloky padají do něj. Když se zaplní, těžba se zastaví.",
            "Ložisko se točí 4× pomaleji než vstupní rotace. Čím víc bloků těží najednou, tím je pomalejší – pomůže víc ložisek."]),
        # ---------- Lana a dokování ----------
        Q("coupling", "Lano", dep=["assembler"], items=[("simulated:rope_coupling", 2)], xp=20, d=[
            "Lanová spojka (&eRope Coupling&r) je lano pro fyzikální stroje. Výroba: provázky a železné nugety.",
            "Klikni s ní na naviják a pak na úchyt – natáhneš mezi nimi lano. Lano může být dlouhé nejvýš 40 bloků. Nůžkami ho přestřihneš."]),
        Q("rope", "Naviják", dep=["coupling"],
          items=[("simulated:rope_winch", 1), ("simulated:rope_connector", 2)], xp=40, d=[
            "Naviják (&eRope Winch&r) lano navíjí a odvíjí, když ho roztočíš. Úchyt (&eRope Connector&r) je pevný konec lana. Dva navijáky spojit nejde, dva úchyty ano.",
            "Tak spustíš náklad z lodi, vytáhneš auto nebo odtáhneš jiný stroj.",
            "&bClimbable Ropes&r ti dovolí po lanech šplhat. S montážním klíčem v ruce po laně sjedeš dolů."]),
        Q("dock", "Dokování", dep=["rope", "create:crafter"], items=[("simulated:docking_connector", 2)], xp=40, d=[
            "Dokovací spojka (&eDocking Connector&r) pevně spojí dva stroje, třeba loď s přístavem.",
            "Vysunuté spojky se k sobě natočí a po vyrovnání zacvaknou. Pak jimi tečou předměty a tekutiny oběma směry. Zasunutím jedné spojky se odpojíš.",
            "Komparátor ukáže, jak daleko je dokování. Vyrábí se v mechanickém výrobníku (2 kusy)."]),
        Q("plunger", "Vystřelovač přísavek", dep=["coupling", "create:crafter", "create:precision"],
          items=[("simulated:plunger_launcher", 1)], xp=30, optional=True, d=[
            "Vystřelovač přísavek (&ePlunger Launcher&r) střílí přísavky na laně. Dvě přísavky se spojí a přitáhnou bloky k sobě.",
            "Shift + pravé tlačítko přísavky odstraní. Když máš na zádech měděnou tlakovou láhev (&eCopper Backtank&r), bere si z ní vzduch."]),
        # ---------- Levitit ----------
        Q("end_powder", "Prach z endového kamene", dep=["start", "create:crushing", "create:mixer"],
          items=[("aeronautics:end_stone_powder", 8)], xp=40, d=[
            "Levitit je materiál, který sám nadnáší. Začíná prachem z endového kamene (&eEnd Stone Powder&r).",
            "Rozdrť endový kámen v drtících kolech. &cEndový kámen najdeš až v Endu.&r",
            "Pak je smíchej v míchačce: do tyglíku dej 4 prachy, 2 zinkové nugety a vodu, pod tyglík ohřátý ohňohořák. Vznikne tekutá směs levititu (&eLevitite Blend&r)."]),
        Q("levitite", "Levitit", icon="aeronautics:levitite", dep=["end_powder"],
          tasks=[adv("aeronautics:unidentified_floating_object")], xp=60, d=[
            "Levitit (&eLevitite&r) udrží stroj ve vzduchu bez hořáku a bez vrtulí. Sám ale stroj nahoru nezvedne – na stoupání potřebuješ vrtule nebo balón.",
            "Vzniká ze směsi teplem. Natoč směs do kbelíku a vylij do formy. Pak ji zapal: dej k ní pochodeň, táborák, magmatický blok nebo oheň, nebo ji zapal křesadlem.",
            "Krystal se pak rozroste celou směsí. Formu postav z jílu nebo bahna – tyto bloky se při krystalizaci rozpadnou a zůstane jen levitit. Quest se splní, jakmile ti levitit poprvé vykrystalizuje.",
            "&cZtuhlý levitit nejde vytěžit – při rozbití zmizí. Odlévej ho proto rovnou do stroje, kde ho chceš mít.&r",
            "&aPři pomalém pohybu levitit silně brzdí, při rychlém skoro vůbec.&r"]),
        Q("pearl", "Perleťový levitit", icon="aeronautics:pearlescent_levitite", dep=["levitite"],
          tasks=[adv("aeronautics:now_available_in_pink")], xp=30, optional=True, d=[
            "Perleťový levitit (&ePearlescent Levitite&r) je růžová varianta levititu.",
            "Vznikne, když směs zapálíš ohněm duší: pochodní duší, táborákem duší nebo ohněm duší."]),
        # ---------- Zbraně ----------
        Q("cannon", "Ozbrojená loď", dep=["assembler", "create:crafter"],
          items=[("aeronautics:mounted_potato_cannon", 1)], xp=40, d=[
            "Pevné bramborové dělo (&eMounted Potato Cannon&r) je blok, který střílí stejnou munici jako ruční bramborové dělo.",
            "Rotace dělo nabije, redstonový signál ho odpálí. Při trvalém signálu střílí pořád. Munici mu můžeš dodávat i automaticky.",
            "Vyrábí se v mechanickém výrobníku."]),
        # ---------- Aero Islands a Aeronautics Structures ----------
        Q("twig", "Aerolit", dep=["start"], items=[("aeroscapes:aerolite_twig", 4)], xp=20, optional=True, d=[
            "&bAero Islands&r přidává rudu aerolit (&eAerolite&r). Najdeš ji pod zemí ve většině biomů Overworldu.",
            "Z rudy padají aerolitové větvičky (&eAerolite Twig&r). Jsou velmi lehké. Když větvičku sníš, chvíli levituješ.",
            "&aZ větviček se dá složit stavební blok – viz další quest.&r"]),
        Q("islands", "Blok z aerolitu", dep=["twig"], items=[("aeroscapes:quickslate", 1)], xp=30, optional=True, d=[
            "Ruda aerolitu (&eAerolite&r) se nedá sebrat celá – vždy z ní padají větvičky, i s Hedvábným dotekem.",
            "Z 9 větviček ale složíš stavební blok (&eQuickslate&r)."]),
        Q("charm", "Aerolitový amulet", dep=["twig"], items=[("aeroscapes:aerolite_charm", 1)], xp=30,
          optional=True, d=[
            "Aerolitový amulet (&eAerolite Charm&r) tě vytáhne na povrch. Použij ho, když stojíš pod bloky, třeba v jeskyni.",
            "Výroba: provázek, 2 aerolitové větvičky, perla Enderu a křemen. Dobiješ ho v pracovním stole perlou Enderu."]),
        Q("selenite", "Selenit", dep=["start"], items=[("aeroscapes:selenite_shard", 4)], xp=20, optional=True, d=[
            "Selenit roste v geodách v zasněžených a horských biomech.",
            "Krystal selenitu (&eSelenite Crystal&r) zabrání líhnutí příšer ve svém malém okolí. Rozbitý krystal dá střepy (&eSelenite Shard&r), s Hedvábným dotekem celý krystal."]),
        Q("lamp", "Selenitová lampa", dep=["selenite"], items=[("aeroscapes:selenite_lamp", 1)], xp=30,
          optional=True, d=[
            "Selenitová lampa (&eSelenite Lamp&r) omezí líhnutí příšer ve velkém okolí. Musí být nabitá selenitovými střepy.",
            "Výroba: selenitový střep obklopený železnými nugety."]),
        Q("balloon_find", "Balón v divočině", icon="aeronautics:adjustable_burner", dep=["start"],
          tasks=[structure("morestructures:hotairballoon")], xp=30, optional=True, d=[
            "Ve světě občas stojí horkovzdušné balóny z modu &bCreate Aeronautics Structures&r. Jsou vzácné. Hledej je na pláních, loukách, v savaně, poušti nebo v badlands.",
            "Uvnitř je hotový balón: hořáky, obaly i fyzikální sestavovač. Prohlédni si ho – je to dobrá předloha pro tvůj první let."]),
        Q("cloud_disc", "Píseň oblaků", icon="aeronautics:music_disc_cloud_skipper", dep=["balloon"],
          tasks=[adv("aeronautics:song_of_the_sky")], xp=30, optional=True, d=[
            "Vyleť až do mraků, třeba svým létajícím strojem, a vyhoď tam hudební disk. Promění se v nový disk s písní &eCloud Skipper&r."]),
    ],
)

# =====================================================================
# LETADLA A LODĚ – Immersive Aircraft + Small Ships
# =====================================================================
VEHICLES = dict(
    key="vehicles", group="tech", title="Letadla a lodě",
    subtitle="Immersive Aircraft a Small Ships", icon="immersive_aircraft:biplane",
    quests=[
        Q("start", "Letadla a lodě", icon="immersive_aircraft:biplane", tasks=[auto()], xp=10,
          shape="hexagon", size=1.5, s="Začátečník", d=[
            "&bImmersive Aircraft&r přidává hotová letadla. Vyrobíš je v pracovním stole, položíš na zem a letíš. Nic nestavíš blok po bloku.",
            "&bSmall Ships&r přidává plachetnice. Postaví je loděnice z prken, vlny a provázků.",
            "&aTato letadla jsou jednodušší než stroje z Create Aeronautics. Hodí se, když chceš hlavně rychle cestovat.&r"]),
        # ---------- Immersive Aircraft: díly ----------
        Q("parts", "Díly letadel", dep=["start"],
          items=[("immersive_aircraft:hull", 4), ("immersive_aircraft:sail", 2)], xp=20, d=[
            "Každé letadlo se skládá z dílů. Trup (&eHull&r) je z kmenů a železných ingotů. Plachta (&eSail&r) je z bílých koberců a provázku.",
            "&aTyto díly si vyrob dopředu – budeš jich potřebovat hodně.&r"]),
        Q("boiler", "Kotel", dep=["parts"], items=[("immersive_aircraft:boiler", 1)], xp=20, d=[
            "Kotel (&eBoiler&r) je srdce motoru. Výroba: měděné ingoty a pec."]),
        Q("engine", "Motor a vrtule", dep=["boiler"],
          items=[("immersive_aircraft:engine", 1), ("immersive_aircraft:propeller", 1)], xp=25, d=[
            "Motor (&eEngine&r) vyrobíš z kotle, vysoké pece, dvou pístů a dlažebních kamenů. Vrtule (&ePropeller&r) je ze železných ingotů.",
            "&aMotor potřebuje skoro každé letadlo.&r"]),
        Q("gyrodyne", "Vírník", dep=["parts"], items=[("immersive_aircraft:gyrodyne", 1)], xp=40, d=[
            "Vírník (&eGyrodyne&r) je vrtulník na lidský pohon. Nemá motor a nepotřebuje palivo – roztáčíš ho vlastní silou a ubírá ti jídlo.",
            "Po nasednutí rotor roztlač. Na obrazovce uvidíš, kolik síly ještě chybí. Pak můžeš vzlétnout.",
            "Výroba: 2 plachty, 2 trupy a vrtule."]),
        Q("airship", "Vzducholoď", dep=["engine"], items=[("immersive_aircraft:airship", 1)], xp=40, d=[
            "Vzducholoď (&eAirship&r) je pomalá, ale snadno se řídí. Je to ideální první letadlo. Výroba: 6 plachet, 2 trupy a motor.",
            "Polož ji na volnou zem a nasedni. Shift + pravé tlačítko otevře její inventář.",
            "Do slotu na palivo dej to, co hoří v peci: uhlí, dřevo nebo prkna. Funguje i ohnivý prach (&eBlaze Powder&r).",
            "&aPoškozené letadlo opravíš kliknutím pravým tlačítkem. Každé kliknutí trochu opraví a stojí trochu jídla.&r"]),
        Q("quad", "Kvadrokoptéra", dep=["engine"], items=[("immersive_aircraft:quadrocopter", 1)], xp=40, d=[
            "Kvadrokoptéra (&eQuadrocopter&r) je skvělá na stavění ve výšce.",
            "Výroba: 4 vrtule, 4 bambusy a motor. Má jen malý inventář a jeden slot na vylepšení."]),
        Q("biplane", "Dvouplošník", dep=["engine"], items=[("immersive_aircraft:biplane", 1)], xp=60, d=[
            "Dvouplošník (&eBiplane&r) je rychlé a spolehlivé letadlo. Výroba: 3 trupy, motor a vrtule.",
            "&cPotřebuje dlouhou rovnou plochu na rozjezd.&r Vylepšený podvozek rozjezd zrychlí."]),
        Q("hopper", "Bambusový hopper", dep=["biplane"], items=[("immersive_aircraft:bamboo_hopper", 1)], xp=60, d=[
            "Bambusový hopper (&eBamboo Hopper&r) je velké letadlo pro tři lidi. Má plováky, takže přistane i na vodě.",
            "Výroba je drahá: 2 dvouplošníky, trup, motor a bambusové bloky. Má 2 sloty na zbraně a 4 na vylepšení."]),
        Q("cargo", "Nákladní vzducholoď", dep=["airship"], items=[("immersive_aircraft:cargo_airship", 1)], xp=50, d=[
            "Nákladní vzducholoď (&eCargo Airship&r) uveze celý sklad – má navíc 4 velké přihrádky.",
            "Výroba: vzducholoď, trup a 4 truhly.",
            "&cJe pomalá, spotřebuje hodně paliva a nemá místo na zbraň.&r"]),
        # ---------- Immersive Aircraft: vylepšení ----------
        Q("upgrade", "Vylepšení", dep=["biplane"], items=[("immersive_aircraft:enhanced_propeller", 1)], xp=40,
          shape="hexagon", size=1.5, s="Pokročilý", d=[
            "Vylepšení (&eAircraft Upgrade&r) vkládáš do slotů pro vylepšení v inventáři letadla. Každé letadlo jich má jiný počet.",
            "Vylepšená vrtule (&eEnhanced Propeller&r): motor +5 %, odpor vzduchu −75 %. Výroba: vrtule a měděné ingoty.",
            "&aPřesné hodnoty každého vylepšení ukáže jeho popisek.&r"]),
        Q("pipes", "Robustní potrubí", dep=["upgrade"], items=[("immersive_aircraft:sturdy_pipes", 1)], xp=20, d=[
            "Robustní potrubí (&eSturdy Pipes&r): výkon motoru +8 %. Výroba: měděné a železné ingoty."]),
        Q("gears", "Průmyslová ozubená kola", dep=["upgrade"], items=[("immersive_aircraft:industrial_gears", 1)], xp=30, d=[
            "Průmyslová ozubená kola (&eIndustrial Gears&r): spotřeba paliva −20 %. Výroba: měděné a železné ingoty a páka.",
            "&aPotřebuješ je i na válečnou loď a na rotační dělo.&r"]),
        Q("steel_boiler", "Ocelový kotel", dep=["upgrade"], items=[("immersive_aircraft:steel_boiler", 1)], xp=30, d=[
            "Ocelový kotel (&eSteel Boiler&r): výkon motoru +20 %, ale spotřeba paliva +50 %.",
            "Výroba: kotel, vysoká pec a železné ingoty."]),
        Q("eco", "Ekologický motor", dep=["upgrade"], items=[("immersive_aircraft:eco_engine", 1)], xp=40, d=[
            "Ekologický motor (&eEco Engine&r): spotřeba paliva −75 %, ale výkon motoru −20 %. Ideální na dlouhé lety.",
            "Výroba: motor, zlaté ingoty, slizové koule a cihly."]),
        Q("nether_engine", "Motor z Netheru", dep=["upgrade"], items=[("immersive_aircraft:nether_engine", 1)], xp=60, d=[
            "Motor z Netheru (&eNether Engine&r): výkon motoru +30 %, spotřeba paliva +30 %.",
            "Výroba: motor, netheritový ingot, ohnivé tyče, magmový krém a netherové cihly."]),
        Q("gyroscope", "Gyroskop", dep=["upgrade"], items=[("immersive_aircraft:gyroscope", 1)], xp=30, d=[
            "Gyroskop (&eGyroscope&r) úplně vyruší vliv větru a trochu stabilizuje let. Výroba: kompas a 2 komparátory.",
            "&aZa deště a bouřky fouká silnější vítr, tam se gyroskop hodí nejvíc.&r"]),
        Q("dials", "Pokročilý gyroskop", dep=["gyroscope"], items=[("immersive_aircraft:gyroscope_dials", 1)], xp=30, d=[
            "Pokročilý gyroskop (&eAdvanced Gyroscope&r) umí totéž co gyroskop a přidá mechanickou palubní desku s ukazateli.",
            "Výroba: gyroskop, 3 hodiny, nótový blok a páka."]),
        Q("hud", "Elektronický gyroskop", dep=["gyroscope"], items=[("immersive_aircraft:gyroscope_hud", 1)], xp=30, d=[
            "Elektronický gyroskop (&eElectronic Gyroscope&r) umí totéž co gyroskop a přidá elektronickou palubní desku.",
            "Výroba: gyroskop, redstonová lampa, zlato, skleněná tabule, nótový blok a páka."]),
        Q("hull_reinforcement", "Zesílení trupu", dep=["upgrade"],
          items=[("immersive_aircraft:hull_reinforcement", 1)], xp=30, d=[
            "Zesílení trupu (&eHull Reinforcement&r): odolnost letadla +100 %. Výroba: 3 trupy a železné ingoty."]),
        Q("landing_gear", "Vylepšený podvozek", dep=["upgrade"],
          items=[("immersive_aircraft:improved_landing_gear", 1)], xp=30, d=[
            "Vylepšený podvozek (&eImproved Landing Gear&r): rychlost rozjezdu +75 %. Dvouplošník se rychleji odlepí od země.",
            "Výroba: železné ingoty a uhlí."]),
        # ---------- Immersive Aircraft: zbraně a válečná loď ----------
        Q("telescope", "Teleskop", dep=["airship"], items=[("immersive_aircraft:telescope", 1)], xp=20, d=[
            "Zbraně a přístroje (&eAircraft Weapon&r) dáváš do slotu na zbraň. Většina letadel má jeden, hopper a válečná loď dva, nákladní vzducholoď žádný.",
            "Teleskop (&eTelescope&r) je větší dalekohled. Výroba: dalekohled a měděný ingot."]),
        Q("crossbow", "Těžká kuše", dep=["telescope"], items=[("immersive_aircraft:heavy_crossbow", 1)], xp=30, d=[
            "Těžká kuše (&eHeavy Crossbow&r) střílí silné šípy. Munice: šípy v inventáři letadla.",
            "Výroba: kuše, háček na nástražný drát a kmen."]),
        Q("rotary", "Rotační dělo", dep=["telescope", "gears"], items=[("immersive_aircraft:rotary_cannon", 1)], xp=40, d=[
            "Rotační dělo (&eRotary Cannon&r) rychle pálí. Munice: střelný prach v inventáři letadla.",
            "Výroba: dávkovač, průmyslová ozubená kola a měděný ingot."]),
        Q("bomb_bay", "Pumovnice", dep=["telescope"], items=[("immersive_aircraft:bomb_bay", 1)], xp=40, d=[
            "Pumovnice (&eBomb Bay&r) shazuje TNT. Munice: TNT v inventáři letadla.",
            "&aBomby neničí bloky, ale těžce zraní vše, co zasáhnou.&r"]),
        Q("warship", "Válečná loď", dep=["cargo", "gears"], items=[("immersive_aircraft:warship", 1)], xp=80,
          shape="hexagon", size=1.5, s="Expert", d=[
            "Válečná loď (&eWarship&r) je létající pevnost: pomalá, ale odolná a těžce ozbrojená.",
            "Má 3 sloty na palivo, 2 na zbraně a 6 na vylepšení.",
            "Výroba: nákladní vzducholoď, 2 motory, 3 trupy, 2 plachty a průmyslová ozubená kola."]),
        # ---------- Small Ships ----------
        Q("dockyard", "Loděnice", dep=["start"], items=[("smallships:dockyard", 1)], xp=40, d=[
            "Loděnice (&eDockyard&r) staví lodě ze &bSmall Ships&r. Polož ji u vody a otevři ji.",
            "V záložce stavby (&eBuild&r) vyber typ lodi a dřevo. Materiál se bere z tvého inventáře: hodně prken, bílá vlna, provázky a u většiny lodí železo. Loď se po chvíli objeví na vodě poblíž.",
            "&cVoda musí být dost velká a hluboká. Loděnice napíše, kolik bloků hloubky loď potřebuje.&r",
            "Výroba loděnice: pracovní stůl, sud, papír, vlna, provázky, vodítka a železný ingot.",
            "{@pagebreak}",
            "&eTypy lodí&r (cena v prknech): galéra, drakkar a dau 96, karavela 120, cog 192, briga 240, galeona 336.",
            "&eGalley&r (galéra): plachta i vesla, 2 děla, taranuje bez poškození, rychlejší v teplých vodách. &eDrakkar&r: plachta i vesla, až 10 štítů na bocích, prorazí led, rychlejší ve studených vodách.",
            "&eCog&r: 1 stěžeň, až 4 děla. &eBrigg&r (briga): 2 stěžně, až 6 děl. &eGalleon&r (galeona): 3 stěžně, až 10 děl a plná rychlost i se všemi děly.",
            "&eCaravel&r (karavela): pluje i proti větru. &eDhow&r (dau): plná rychlost i s plným nákladem."]),
        Q("sails", "Pod plachtami", dep=["dockyard"], items=[("smallships:cotton_sails", 1)], xp=40, d=[
            "Plachtu rozvineš nebo svineš klávesou R. Nápověda s dalšími klávesami se ukazuje na obrazovce, když lodi velíš.",
            "Na lodi záleží na větru. Vítr do zad dá většině lodí velký bonus, boční vítr menší. Galéru a drakkar můžeš se svinutou plachtou pohánět vesly.",
            "Bavlněné plachty (&eCotton Sails&r) jsou vylepšení: loď je rychlejší. Instaluješ je v loděnici v záložce úprav (&eModify&r). Loď musí být do 16 bloků od loděnice."]),
        Q("scantlings", "Železné žebrování", dep=["sails"], items=[("smallships:iron_scantlings", 1)], xp=30, d=[
            "Železné žebrování (&eIron Scantlings&r) zvýší odolnost lodi. Instaluje se v loděnici stejně jako plachty.",
            "&aV loděnici loď také opravíš – zvlášť trup a zvlášť plachty.&r"]),
        Q("plating", "Měděné oplechování", dep=["sails"], items=[("smallships:copper_plating", 1)], xp=30, d=[
            "Měděné oplechování (&eCopper Plating&r) zlepší ovladatelnost lodi. Instaluje se v loděnici."]),
        Q("shipcannon", "Lodní děla", dep=["dockyard"],
          items=[("smallships:cannon", 1), ("smallships:cannon_ball", 8)], xp=40, d=[
            "Lodní dělo (&eShip Cannon&r) namontuješ v loděnici na levobok (&ePort&r) nebo pravobok (&eStarboard&r). Každá pozice stojí 1 dělo.",
            "Dělové koule (&eCannon Ball&r) dej do inventáře lodi. Míření a střelbu ti ukáže nápověda na obrazovce.",
            "&cS více děly je většina lodí pomalejší. Galeona ne.&r"]),
        Q("chained", "Řetězová střela", dep=["shipcannon"], items=[("smallships:chained_shot", 2)], xp=20,
          optional=True, d=[
            "Řetězová střela (&eChained Shot&r) má o 25 % menší dostřel i poškození, ale silně ničí plachty.",
            "Výroba: 4 dělové koule a řetěz dají 2 kusy."]),
        Q("grape", "Kartáčová střela", dep=["shipcannon"], items=[("smallships:grape_shot", 1)], xp=20,
          optional=True, d=[
            "Kartáčová střela (&eGrape Shot&r) má krátký dostřel, ale je zničující proti posádce.",
            "Výroba: střelný prach obklopený železnými nugety."]),
        Q("powder", "Jemný prach", dep=["shipcannon"], items=[("smallships:fine_grain_powder", 3)], xp=20,
          optional=True, d=[
            "Jemný prach (&eFine-Grain Powder&r) se spotřebuje při nabíjení a zvýší dostřel o 50 %.",
            "Výroba: kostní moučka, střelný prach a dřevěné uhlí dají 3 kusy."]),
    ],
)

# Pořadí kapitol této oblasti v knize questů
CHAPTERS = [TRAINS, AERO, VEHICLES]
