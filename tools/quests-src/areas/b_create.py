from engine import *

# Oblast Create (Create 6.0.10 + Create Goggles + Create Jetpack).
# Čísla stresu/rychlostí ověřena v kódu jaru create-1.21.1-6.0.10 (AllBlocks, CStress, CKinetics,
# BoilerData, PoweredShaftBlockEntity, PumpBlockEntity, FluidNetwork), recepty v $DB/data/create/recipe.

M = dict(shape="hexagon", size=1.5)  # milník

# ---------------------------------------------------------------------------
# 1) ZÁKLADY (původní kapitola "create" – 32 původních questů + nové)
# ---------------------------------------------------------------------------
CREATE = dict(
    key="create", group="create", title="Create: Základy",
    subtitle="Rotace, první stroje, mosaz a parní motor", icon="create:cogwheel",
    quests=[
        Q("intro", "Vítej v Create", tasks=[auto()], icon="create:cogwheel", xp=10, s="Začátečník", **M, d=[
            "&bCreate&r je mod o strojích, které pohání &erotace&r. Točící se hřídele a ozubená kolečka roztáčí lisy, míchačky, pásy a další stroje.",
            "Tahle kapitola tě provede od první slitiny přes mosaz až k parnímu motoru. Další kapitoly Create jdou do hloubky: energie, rudy, logistika, automatizace a nástroje.",
            "&aTip:&r Skoro každý předmět z Create má animovaný návod. Najeď myší na předmět a podrž klávesu z popisku („Podržte [W] pro dumání“ / „Hold [W] to Ponder“).",
        ]),
        Q("alloy", "Andezitová slitina", dep=["intro"], items=[("create:andesite_alloy", 8)], xp=20, d=[
            "&eAndezitová slitina&r (&eAndesite Alloy&r) je základ skoro všech strojů z Create.",
            "Vyrob ji v pracovním stole: 2 andezity a 2 železné nugety střídavě do čtverce 2×2. Místo železných nugetů jdou i zinkové.",
            "Andezit najdeš v jeskyních a v horách. Později bude slitinu vyrábět míchačka sama (kapitola Stroje a automatizace).",
        ]),
        Q("shaft", "Hřídele a kolečka", dep=["alloy"], items=[("create:shaft", 4), ("create:cogwheel", 2), ("create:large_cogwheel", 1)], xp=20, d=[
            "Rotace se šíří přes &ehřídele&r (&eShaft&r) rovně a přes &eozubená kolečka&r (&eCogwheel&r) do stran.",
            "2 slitiny nad sebou = 8 hřídelí. Kolečko = hřídel + prkno. Velké kolečko (&eLarge Cogwheel&r) = kolečko + prkno.",
            "Dvě kolečka vedle sebe se točí opačně. Malé a velké kolečko spojené našikmo mění rychlost: z velkého na malé 2× rychleji, z malého na velké 2× pomaleji.",
        ]),
        Q("crank", "Ruční klika", dep=["shaft"], items=[("create:hand_crank", 1)], xp=15, d=[
            "&eRuční klika&r (&eHand Crank&r) je nejjednodušší zdroj rotace. Vyrobíš ji ze 3 prken a andezitové slitiny.",
            "Polož ji na hřídel a drž pravé tlačítko. Se Shiftem se točí opačně.",
            "Každý zdroj dává &erychlost&r (otáčky, RPM) a &esílu&r (stres, jednotka SU). Klika dá 32 RPM a 256 SU. &cPři točení ti ubývá jídlo,&r na stálý provoz postav mlýnské kolo.",
        ]),
        Q("wheel", "Mlýnské kolo", dep=["shaft"], items=[("create:water_wheel", 1)], xp=25, d=[
            "&eMlýnské kolo&r (&eWater Wheel&r) je první stálý zdroj energie. Recept: hřídel uprostřed a kolem ní 8 prken.",
            "Polož ho tak, aby kolem něj &etekla&r voda – stojatá voda kolo neroztočí. Stačí proud na jedné straně, další strany už výkon nezvýší.",
            "Kolo se točí 8 RPM a dá 256 SU. &aTip:&r Víc kol na jedné hřídeli dá víc SU, jen se musí točit stejným směrem. Víc zdrojů je v kapitole Energie a stres.",
        ]),
        Q("casing", "Andezitové pouzdro", dep=["alloy"], items=[("create:andesite_casing", 8)], xp=15, d=[
            "&eAndezitové pouzdro&r (&eAndesite Casing&r) je kostra mnoha strojů.",
            "Kmen nejdřív oloupej sekerou (pravé tlačítko). Pak vezmi andezitovou slitinu a klikni s ní pravým na oloupaný kmen nebo oloupané dřevo.",
            "&aTip:&r Stejně vznikne měděné pouzdro (měděný ingot) a mosazné pouzdro (mosazný ingot).",
        ]),
        Q("press", "Mechanický lis", dep=["casing", "wheel"], items=[("create:mechanical_press", 1)], xp=25, d=[
            "&eMechanický lis&r (&eMechanical Press&r) lisuje ingoty na &epláty&r. Recept: hřídel, andezitové pouzdro a blok železa pod sebou.",
            "Roztoč ho a pod něj dej odkládací desku nebo pás. Předmět můžeš pod lis i jen hodit na zem.",
            "Lis bere 8 SU za každé RPM. Na 8 RPM z mlýnského kola je to 64 SU, takže jedno kolo (256 SU) ho utáhne.",
        ]),
        Q("sheets", "Železné pláty", dep=["press"], items=[("create:iron_sheet", 8)], xp=20, d=[
            "&eŽelezný plát&r (&eIron Sheet&r) vznikne lisováním železného ingotu. Stejně uděláš měděné, zlaté a mosazné pláty.",
            "Pláty jsou v receptech všude: vrtule, metla, brýle, potrubí, nádrže.",
            "&aTip:&r Lis nad pásem zpracuje celý proud ingotů sám. Pás zastaví předmět pod lisem a pustí ho dál až po vylisování.",
        ]),
        Q("goggles", "Inženýrské brýle", dep=["press"], items=[("create:goggles", 1)], xp=20, d=[
            "&eInženýrské brýle&r (&eEngineer's Goggles&r): provázek, 2 skla a zlatý plát. Nasaď si je na hlavu.",
            "Když se díváš na stroj, brýle ukážou jeho &estres&r: kolik SU stroj spotřebuje nebo kolik zdroj dodá. Ukazují i obsah nádrží a stav kotle.",
            "&cKdyž stroje chtějí víc SU, než zdroje dají, síť se přetíží a zastaví se celá.&r Pak přidej zdroj nebo stroje zpomal.",
        ]),
        Q("wrench", "Montážní klíč", dep=["press"], items=[("create:wrench", 1)], xp=15, d=[
            "&eMontážní klíč&r (&eWrench&r): 3 zlaté pláty, ozubené kolečko a klacek.",
            "Pravým tlačítkem otáčíš bloky. Shift + pravé tlačítko blok rychle sebere do inventáře.",
            "Klíčem také přepínáš režimy: obrátíš čerpadlo, nastavíš šipky mechanického výrobníku nebo uděláš okénko v potrubí.",
        ]),
        Q("depot", "Odkládací deska", dep=["casing"], items=[("create:depot", 1)], xp=15, d=[
            "&eOdkládací deska&r (&eDepot&r) je jako kousek pásu, který stojí na místě. Recept: andezitová slitina + andezitové pouzdro.",
            "Pravým tlačítkem na ni předmět položíš nebo ho vezmeš. Lis, pokladač nebo dávkovač nad ní předmět zpracuje.",
            "Mechanická paže z desky umí brát i na ni dávat.",
        ]),
        Q("millstone", "Mlýnský kámen", dep=["casing", "wheel"], items=[("create:millstone", 1)], xp=20, d=[
            "&eMlýnský kámen&r (&eMillstone&r) mele: štěrk na pazourek, pšenici na mouku, květiny na barviva, dlažební kámen na štěrk.",
            "Roztoč ho ozubeným kolečkem ze strany. Předměty hoď nebo vlož shora, hotové vyber pravým tlačítkem nebo trychtýřem.",
            "&cRudy mlýnský kámen nezpracuje,&r na ně potřebuješ drtící kola. Čím rychleji se točí, tím rychleji mele.",
        ]),
        Q("belt", "Mechanický pás", dep=["shaft"], items=[("create:belt_connector", 4)], xp=20, d=[
            "&eMechanický pás&r (&eMechanical Belt&r) vyrobíš ze 6 sušených chaluh. Klikni pásem na dvě hřídele a spojí se.",
            "Pás vozí předměty i hráče. Hřídele spojené pásem se točí stejně rychle a stejným směrem, pás tedy přenáší i rotaci.",
            "Pás může vést vodorovně, šikmo nebo svisle a měřit 2 až 20 bloků. Prázdnou rukou z něj předmět sebereš.",
        ]),
        Q("fan", "Zapouzdřený větrák", dep=["sheets"], items=[("create:encased_fan", 1)], xp=25, d=[
            "&eZapouzdřený větrák&r (&eEncased Fan&r): hřídel, andezitové pouzdro a vrtule. Fouká vzduch, směr a sílu určuje rotace.",
            "Když vzduch projde blokem, zpracuje předměty za ním: voda = &epraní&r, láva = &etavení&r, oheň nebo táborák = &euzení&r, duší oheň = &eprokletí&r.",
            "&cJídlo přes lávu shoří,&r na jídlo použij oheň. Rychlost větráku mění jen dosah, ne rychlost zpracování. Funguje i na pás a desku.",
        ]),
        Q("washing", "Praní větrákem", dep=["fan"], items=[("minecraft:iron_nugget", 16)], xp=20, d=[
            "Postav větrák, před něj vodu a za ni pošli pásem nebo hoď předměty. To je &ehromadné praní&r.",
            "Štěrk dá při praní občas pazourek (25 %) a železný nuget (12,5 %). Rozdrcená ruda dá 9 nugetů a bonus.",
            "&aTip:&r Praní také změní pšeničnou mouku na těsto a magmatický blok na obsidián.",
        ]),
        Q("mixer", "Míchačka a tyglík", dep=["sheets"], items=[("create:mechanical_mixer", 1), ("create:basin", 1)], xp=30, d=[
            "&eMechanická míchačka&r (&eMechanical Mixer&r) míchá suroviny v &etyglíku&r (&eBasin&r) pod sebou. Do tyglíku dej suroviny a míchačku roztoč.",
            "Zvládne všechny recepty bez pevného tvaru a speciální recepty Create: slitiny, těsto, čokoládu. Některé potřebují teplo z ohňohořáku.",
            "Výrobek vypadne bokem do desky nebo truhly pod tyglíkem. &aTip:&r Lis nad tyglíkem místo míchačky věci slisuje, např. 9 nugetů na ingot.",
        ]),
        Q("zinc", "Zinek", dep=["alloy"], items=[("create:raw_zinc", 8)], xp=20, d=[
            "&eZinková ruda&r (&eZinc Ore&r) je v Overworldu ve výškách od −63 do 70. Ze zinku a mědi vznikne mosaz.",
            "Surový zinek (&eRaw Zinc&r) roztav v peci na zinkový ingot.",
            "&aTip:&r Zinek je i v kameni &eazurín&r (&eAsurine&r). Drtící kola z něj zinek vydrtí.",
        ]),
        Q("burner", "Ohňohořák", dep=["sheets"], items=[("create:blaze_burner", 1)], xp=40, d=[
            "&eOhňohořák&r (&eBlaze Burner&r) je zdroj tepla. Nejdřív vyrob &eprázdný ohňohořák&r (&eEmpty Blaze Burner&r): 4 železné pláty a netherrack.",
            "V Netheru klikni prázdným hořákem na ohniváka (Blaze) a chytíš ho dovnitř. Jde to i přímo u spawneru ohniváků.",
            "Krm ho palivem (uhlí, dřevo), pak je &eohřátý&r. Ohňodort ho udělá &epřehřátý&r. Krmení zvládne pokladač nebo mechanická paže.",
        ]),
        Q("brass", "Mosaz", dep=["mixer", "zinc", "burner"], items=[("create:brass_ingot", 8)], xp=40, s="Pokročilý", **M, d=[
            "&eMosaz&r (&eBrass&r) otevírá pokročilé stroje. Do tyglíku dej měděný a zinkový ingot, pod něj ohřátý ohňohořák a nad něj míchačku. Vzniknou 2 mosazné ingoty.",
            "&cObyčejný oheň ani táborák pod tyglíkem nestačí,&r recept potřebuje ohňohořák s palivem.",
            "Teď už nestačí jen andezit. Z mosazi uděláš mosazné pouzdro, mosazné pláty, pokladač a precizní strojek.",
        ]),
        Q("copper_casing", "Měděné pouzdro", dep=["casing"], items=[("create:copper_casing", 4)], xp=15, d=[
            "&eMěděné pouzdro&r (&eCopper Casing&r) vznikne jako andezitové, jen kliknutím měděným ingotem na oloupaný kmen.",
            "Je potřeba na dávkovač, cedník a hadicovou kladku. Kliknutím na potrubí ho i zakryje.",
        ]),
        Q("brass_casing", "Mosazné pouzdro", dep=["brass"], items=[("create:brass_casing", 4)], xp=20, d=[
            "&eMosazné pouzdro&r (&eBrass Casing&r): klikni mosazným ingotem na oloupaný kmen.",
            "Je to kostra chytrých strojů: mechanický výrobník, mechanická paže, ovladač rychlosti otáček, prahový spínač.",
        ]),
        Q("rose_quartz", "Leštěný růženín", dep=["alloy"], items=[("create:polished_rose_quartz", 4)], xp=20, d=[
            "&eRůženín&r (&eRose Quartz&r): křemen a 8 redstonu v pracovním stole.",
            "Vyleštíš ho &ešmirglpapírem&r (&eSand Paper&r = papír + písek). Růženín drž v druhé ruce a se šmirglpapírem drž pravé tlačítko.",
            "Leštěný růženín je potřeba na elektronky. &aTip:&r Leštění zvládne i pokladač se šmirglpapírem.",
        ]),
        Q("tube", "Elektronka", dep=["rose_quartz", "sheets"], items=[("create:electron_tube", 4)], xp=30, d=[
            "&eElektronka&r (&eElectron Tube&r): leštěný růženín nad železným plátem.",
            "Elektronky jsou v pokladači, mechanickém výrobníku, mosazném trychtýři a tunelu i v chytré šachtě.",
        ]),
        Q("deployer", "Pokladač", dep=["brass", "tube"], items=[("create:deployer", 1)], xp=40, d=[
            "&ePokladač&r (&eDeployer&r) je robotická ruka. Recept: elektronka, andezitové pouzdro a &emosazná ruka&r (&eBrass Hand&r = mosazné pláty + slitina).",
            "Pracuje na místě 2 bloky před sebou: pokládá bloky, používá předměty, kliká na bloky, sklízí a útočí. Předmět mu dáš pravým klikem na jeho čelo.",
            "Nad deskou nebo pásem zpracovává předměty (v JEI recepty „Umístění“ / &eDeploying&r). Klíčem ho přepneš na levé tlačítko. Redstone signál ho zastaví.",
        ]),
        Q("precision", "Precizní strojek", dep=["deployer"], items=[("create:precision_mechanism", 1)], xp=60, s="Expert", **M, d=[
            "&ePrecizní strojek&r (&ePrecision Mechanism&r) se vyrábí &esekvenční montáží&r: jeden předmět projde řadou kroků, a to několikrát dokola.",
            "Začni zlatým plátem na pásu. Nad pás dej 3 pokladače: první drží ozubené kolečko, druhý velké kolečko, třetí železný nuget. Kus musí celou řadou projít 5×.",
            "Výsledek je náhodný: asi v 80 % případů vznikne strojek, jinak odpad (pláty, kolečka, nugety). Přesné kroky ukáže JEI.",
            "&aTip:&r Pás veď do kruhu, nebo vracej rozpracovaný kus (&eIncomplete Precision Mechanism&r) na začátek řady.",
        ]),
        Q("crafter", "Mechanický výrobník", dep=["brass_casing", "tube"], items=[("create:mechanical_crafter", 9)], xp=50, d=[
            "&eMechanický výrobník&r (&eMechanical Crafter&r): elektronka, mosazné pouzdro a pracovní stůl dají 3 kusy.",
            "Postav je vedle sebe do mřížky jako políčka pracovního stolu. Klíčem nastav šipky tak, aby všechny vedly k jednomu výstupu.",
            "Každý výrobník dostane jeden předmět. Když jsou všechny plné, výroba začne. U menšího receptu ji spustíš redstone pulsem.",
            "Velké recepty, třeba drtící kolo (mřížka 5×5), jdou vyrobit jen tady. V JEI mají název „Mechanická výroba“ (&eMechanical Crafting&r).",
        ]),
        Q("arm", "Mechanická paže", dep=["precision", "brass_casing"], items=[("create:mechanical_arm", 1)], xp=50, d=[
            "&eMechanická paže&r (&eMechanical Arm&r) přenáší předměty mezi místy ve svém dosahu.",
            "Před položením paži drž a klikej pravým na cíle: modrý = odkud bere, žlutý = kam dává. Levým klikem výběr zrušíš. Pak paži polož.",
            "Umí desky, pásy, trychtýře, ohňohořáky, truhly a další. Mosazný trychtýř jako cíl jí předá svůj filtr.",
        ]),
        Q("drill", "Vrták a pila", dep=["casing", "sheets"], items=[("create:mechanical_drill", 1), ("create:mechanical_saw", 1)], xp=25, d=[
            "&eMechanický vrták&r (&eMechanical Drill&r) těží blok před sebou. Čím rychlejší rotace, tím rychleji těží.",
            "&eMechanická pila&r (&eMechanical Saw&r) pokácí celý strom, když přeřízne jeho spodní kmen. Otočená nahoru zpracovává předměty.",
            "Nejvíc se hodí na pohyblivých strojích, víc v kapitole Stroje a automatizace.",
        ]),
        Q("bearing", "Ložisko a lepidlo", dep=["drill"], items=[("create:mechanical_bearing", 1), ("create:super_glue", 1)], xp=30, d=[
            "&eMechanické ložisko&r (&eMechanical Bearing&r) otáčí bloky před sebou. Když dostane rotaci, spojí je do jednoho &eudělátka&r (&eContraption&r).",
            "&eVteřinové lepidlo&r (&eSuper Glue&r): klikni na dva rohy a vše v kvádru mezi nimi drží pohromadě.",
            "Větrný mlýn má vlastní, větrné ložisko (další quest).",
        ]),
        Q("windmill", "Větrný mlýn", dep=["bearing"], items=[("create:windmill_bearing", 1), ("create:white_sail", 8)], xp=30, d=[
            "&eVětrné ložisko&r (&eWindmill Bearing&r) + aspoň 8 bloků plachet = větrný mlýn. &eVětrné plachty&r (&eWindmill Sail&r) se lepí samy, lepidlo nepotřebují.",
            "Postav plachty před ložisko a klikni na ložisko pravým. Každých 8 plachet = 1 RPM, nejvíc 16 RPM (128 plachet). Za každé RPM dá 512 SU.",
            "&aTip:&r Jako plachta se počítá i vlna, tu ale musíš přilepit. Směr otáčení nastavíš na panelu ložiska.",
        ]),
        Q("harvester", "Automatická sklizeň", dep=["bearing"], items=[("create:mechanical_harvester", 2)], xp=30, d=[
            "&eMechanický sklízeč&r (&eMechanical Harvester&r) na pohyblivém udělátku sklízí zralé plodiny a nechá je znovu růst.",
            "Dej ho na píst, ložisko nebo vozík a veď ho nad polem. Úrodu sebere truhla přilepená k udělátku.",
        ]),
        Q("fluids", "Tekutiny", dep=["sheets"], items=[("create:fluid_pipe", 8), ("create:mechanical_pump", 1), ("create:fluid_tank", 2)], xp=30, d=[
            "&ePotrubí&r (&eFluid Pipe&r) vede tekutiny. &eMechanické čerpadlo&r (&eMechanical Pump&r) je pohání. Šipka ukazuje směr toku, klíčem ho obrátíš.",
            "Čerpadlo táhne až 16 bloků daleko. Rychlejší rotace = rychlejší tok. Víc čerpadel otočených stejně se sčítá.",
            "&eNádrž&r (&eFluid Tank&r) se spojí se sousedními: základna až 3×3 a výška až 32 bloků. Ručně do ní nenaliješ, plní se potrubím.",
        ]),
        Q("spout", "Dávkovač", dep=["fluids", "copper_casing"], items=[("create:spout", 1)], xp=30, d=[
            "&eDávkovač&r (&eSpout&r): měděné pouzdro nad sušenou chaluhou. Plní předměty pod sebou na desce nebo na pásu.",
            "Plní lahve a kbelíky. Umí i recepty Create, třeba medové jablko nebo ohňodort. Tekutinu mu dodáš potrubím, ručně do něj nenaliješ.",
        ]),
        Q("steam", "Parní motor", dep=["burner", "fluids"], items=[("create:steam_engine", 1)], xp=60, s="Expert", **M, d=[
            "&eParní motor&r (&eSteam Engine&r): zlatý plát, andezitová slitina a blok mědi. Polož ho na nádrž, nádrž se tím stane &ekotlem&r.",
            "Klikni na motor hřídelí, tím vznikne výstup. Kotel potřebuje &evodu&r (čerpadlem), &eteplo&r (ohňohořáky pod nádrží) a &evelikost&r (aspoň 4 bloky nádrže).",
            "Brýle na kotli ukážou jeho úroveň a co chybí. Motor na plný výkon dá 16 384 SU při 64 RPM, to je jako 64 mlýnských kol. Návod je v kapitole Energie a stres.",
        ]),
        Q("crushing", "Drtící kola", dep=["crafter"], items=[("create:crushing_wheel", 2)], xp=60, d=[
            "&eDrtící kolo&r (&eCrushing Wheel&r) vyrobíš v mechanickém výrobníku (mřížka 5×5, dá 2 kola).",
            "Polož 2 kola s mezerou 1 bloku. Musí se točit proti sobě, aby předměty vtahovala do mezery. Předměty hoď nebo vlož shora.",
            "Drtí rudy s bonusy a umí i vše, co mlýnský kámen. Každé kolo bere 8 SU na RPM, pár tedy 16. Návod je v kapitole Zpracování rud.",
        ]),
        Q("vault", "Trezor", dep=["sheets"], items=[("create:item_vault", 1)], xp=30, d=[
            "&eTrezor&r (&eItem Vault&r): 2 železné pláty a sud. Velké úložiště pro stroje.",
            "Trezory vedle sebe se spojí: základna až 3×3, délka až trojnásobek šířky.",
            "&cRučně do trezoru nic nedáš ani nevezmeš.&r Použij trychtýř, šachtu, paži nebo dvířka na předměty (kapitola Logistika).",
        ]),
        Q("backtank", "Tlaková láhev", dep=["shaft"], items=[("create:copper_backtank", 1)], xp=40, d=[
            "&eMěděná tlaková láhev&r (&eCopper Backtank&r) se nosí na zádech a drží stlačený vzduch.",
            "Nabiješ ji tak, že ji položíš na zem a roztočíš hřídelí. Čím rychlejší rotace, tím rychleji se plní.",
            "Vzduch spotřebuje potápěcí helma, prodlužo rameno, bramborové dělo i jetpack. Víc v kapitole Nástroje a schémata.",
        ]),
        Q("jetpack", "Jetpack", dep=["backtank", "precision", "crafter"], items=[("create_jetpack:jetpack", 1)], xp=80, d=[
            "&bCreate Jetpack&r: jetpack je tlaková láhev s tryskami. Vyrábí se v mechanickém výrobníku z měděné láhve, krovek (Elytra), 2 precizních strojků, mosazných plátů, šacht a hřídele.",
            "Plní se jako láhev: polož ho a roztoč. Mezerník = nahoru, Shift = dolů, G = motor zapnout a vypnout, H = režim vznášení.",
        ]),
    ],
)

# ---------------------------------------------------------------------------
# 2) ENERGIE A STRES
# ---------------------------------------------------------------------------
POWER = dict(
    key="create_power", group="create", title="Create: Energie a stres",
    subtitle="Zdroje, převody a parní kotel", icon="create:steam_engine",
    quests=[
        Q("p_intro", "Rychlost a stres", dep=["create:wheel"], tasks=[auto()], icon="create:stressometer", xp=10, s="Začátečník", **M, d=[
            "Každý zdroj v Create dává dvě věci: &erychlost&r (otáčky, RPM) a &esílu&r (stres, jednotka SU). Česky ve hře se stresu říká „kinetické napětí“.",
            "Stroj bere SU podle vzorce &edopad × RPM&r. Lis má dopad 8: na 16 RPM bere 128 SU, na 64 RPM už 512 SU.",
            "Zdroj má kapacitu taky „na RPM“: mlýnské kolo dá 32 × 8 RPM = 256 SU. Když spotřeba všech strojů přeroste kapacitu, celá síť se zastaví.",
            "&aTip:&r Rychlejší stroj pracuje rychleji, ale bere víc SU. Čísla vždy ukážou brýle. Elektromotory a další zdroje přidávají addony (kapitola s addony Create).",
        ]),
        Q("p_large_wheel", "Velké mlýnské kolo", dep=["p_intro"], items=[("create:large_water_wheel", 1)], xp=30, d=[
            "&eVelké mlýnské kolo&r (&eLarge Water Wheel&r): mlýnské kolo uprostřed a kolem něj 8 prken.",
            "Točí se jen 4 RPM, ale dá 512 SU, tedy dvakrát víc než malé kolo. I tady stačí tekoucí voda na jedné straně.",
            "&cZdroje na jedné síti se musí točit stejným směrem.&r Když se dva zdroje „perou“, díl mezi nimi se rozbije. Brýle ukážou, jestli všechny pomáhají.",
        ]),
        Q("p_shift", "Převody", dep=["p_intro"], tasks=[adv("create:shifting_gears")], icon="create:large_cogwheel", xp=25, d=[
            "Spoj velké a malé ozubené kolečko našikmo. Z velkého na malé = 2× rychleji, z malého na velké = 2× pomaleji.",
            "&cPřevod nepřidá sílu!&r Když zrychlíš 2×, každý stroj za převodem bere 2× víc SU. Kapacita zdroje zůstane stejná.",
            "Převody za sebou: 8 → 16 → 32 → 64 RPM. Nejvyšší rychlost je 256 RPM, rychlejší díl se rozbije.",
        ]),
        Q("p_gearbox", "Převodovka", dep=["p_shift"], items=[("create:gearbox", 1)], xp=20, d=[
            "&ePřevodovka&r (&eGearbox&r): 4 ozubená kolečka kolem andezitového pouzdra. Pošle rotaci do 4 stran v jedné rovině.",
            "Strany do rohu se točí zrcadlově, rovný směr se obrátí. &eSvislou převodovku&r (&eVertical Gearbox&r) dostaneš převedením v pracovním stole.",
        ]),
        Q("p_chain", "Řetězový pohon", dep=["p_gearbox"], items=[("create:encased_chain_drive", 2)], xp=20, d=[
            "&eZapouzdřený řetězový pohon&r (&eEncased Chain Drive&r): andezitové pouzdro a 3 železné nugety.",
            "Pohony položené v řadě si předávají rotaci a všechny se točí stejným směrem. Část řady může být otočená o 90°.",
        ]),
        Q("p_chain_shift", "Řetězová řadící páka", dep=["p_chain", "create:tube"], items=[("create:adjustable_chain_gearshift", 1)], xp=30, d=[
            "&eNastavitelná řetězová řadící páka&r (&eAdjustable Chain Gearshift&r): řetězový pohon + elektronka.",
            "Bez signálu se chová jako obyčejný pohon. S redstone signálem se pohony v řadě točí 2× rychleji (nebo 2× pomaleji, když páka není u zdroje).",
            "Slabší redstone signál nastaví poměr přesněji, mezi 1× a 2×.",
        ]),
        Q("p_clutch", "Spojka", dep=["p_gearbox"], items=[("create:clutch", 1)], xp=15, d=[
            "&eSpojka&r (&eClutch&r): andezitové pouzdro, hřídel a redstone. Vede rotaci rovně.",
            "Když dostane redstone signál, rozpojí se a stroje za ní stojí. Je to vypínač pro celou linku.",
        ]),
        Q("p_gearshift", "Řadící páka", dep=["p_gearbox"], items=[("create:gearshift", 1)], xp=15, d=[
            "&eŘadící páka&r (&eGearshift&r): andezitové pouzdro, ozubené kolečko a redstone. Vede rotaci rovně.",
            "S redstone signálem obrátí směr. Hodí se pro písty, kladky a jeřáby, které mají jezdit tam a zpět.",
        ]),
        Q("p_speedometer", "Tachometr", dep=["p_gearbox"], items=[("create:speedometer", 1)], xp=15, d=[
            "&eTachometr&r (&eSpeedometer&r): kompas na andezitovém pouzdře. Ukazuje rychlost hřídele.",
            "Komparátor u tachometru vyšle redstone signál podle rychlosti.",
        ]),
        Q("p_stress", "Stresometr", dep=["p_speedometer", "create:goggles"], items=[("create:stressometer", 1)], xp=30, s="Pokročilý", **M, d=[
            "&eStresometr&r (&eStressometer&r) vznikne převedením tachometru v pracovním stole. Polož ho do sítě a podívej se na něj v brýlích.",
            "Uvidíš kapacitu sítě, spotřebu a kolik SU zbývá. Teď už nestačí jen stavět, musíš počítat: sečti dopad strojů × jejich RPM.",
            "Plánuj s rezervou. Když síť jede těsně pod 100 %, stačí přidat jeden stroj a zastaví se všechno.",
            "&aTip:&r Komparátor u stresometru dá signál podle vytížení. Spojkou tak můžeš vypnout méně důležité stroje.",
        ]),
        Q("p_full", "Přesně na hraně", dep=["p_stress"], tasks=[adv("create:stressometer_maxed")], icon="create:stressometer", xp=30, optional=True, d=[
            "Vytiž síť přesně na 100 %. Spočítej spotřebu strojů a uber nebo přidej stroj, až stresometr ukáže plné vytížení.",
            "Pak zkus přidat ještě jeden stroj: síť se přetíží, všechno se zastaví a brýle ukážou „Přetížené“. Odeber ho a síť se zase rozjede.",
        ]),
        Q("p_windmill_max", "Silný vítr", dep=["p_intro", "create:windmill"], tasks=[adv("create:windmill_maxed")], icon="create:white_sail", xp=50, d=[
            "Postav větrný mlýn se 128 plachtami. Točí se pak nejvyšší rychlostí 16 RPM a dá 8 192 SU.",
            "Výkon mlýna závisí jen na počtu plachet. Tvar mlýna je jedno, počítají se jen bloky plachet.",
            "&aTip:&r Velký mlýn drží pohromadě lepidlo nebo radiální šasi (kapitola Stroje a automatizace).",
        ]),
        Q("p_controller", "Ovladač rychlosti", dep=["p_stress", "create:precision"], items=[("create:rotation_speed_controller", 1)], xp=40, d=[
            "&eOvladač rychlosti otáček&r (&eRotation Speed Controller&r): precizní strojek na mosazném pouzdře.",
            "Bere rotaci ze své osy a předá ji velkému ozubenému kolečku nad sebou. Rychlost nastavíš přesně na panelu na boku.",
            "&cOvladač nepřidá sílu:&r vyšší rychlost = vyšší spotřeba SU strojů za ním.",
        ]),
        Q("p_seq", "Sekvenční řadící páka", dep=["p_gearshift", "create:brass_casing", "create:tube"], items=[("create:sequenced_gearshift", 1)], xp=30, d=[
            "&eSekvenční řadící páka&r (&eSequenced Gearshift&r): mosazné pouzdro, ozubené kolečko a elektronka.",
            "Otáčí podle seznamu kroků, třeba „otoč o 90°, počkej, otoč zpět“. Kroky nastavíš pravým klikem.",
            "Redstone signál spustí celou sekvenci. Hodí se na brány, plošiny a stroje, které mají udělat přesný pohyb.",
        ]),
        Q("p_water", "Voda pro kotel", dep=["p_intro", "create:fluids"], tasks=[adv("create:water_supply")], icon="create:mechanical_pump", xp=25, d=[
            "Kotel pije hodně vody. Každá úroveň kotle potřebuje 10 mB vody za tick (200 mB za sekundu).",
            "Čerpadlo dodá tím víc, čím rychleji se točí. Na 256 RPM stačí jedno čerpadlo zhruba na 12 úrovní.",
            "Otevřený konec potrubí ve vodě vodu nasává, ale bere zdrojové bloky. Nekonečnou vodu dá hadicová kladka v jezeře nebo moři.",
        ]),
        Q("p_hose", "Hadicová kladka", dep=["p_water", "create:copper_casing"], items=[("create:hose_pulley", 1)], xp=30, d=[
            "&eHadicová kladka&r (&eHose Pulley&r): měděné pouzdro, blok sušených chaluh a měděný plát. Spouští hadici a čerpá nebo plní tekutinu.",
            "Ve velkém jezeře nebo moři (aspoň 10 000 bloků vody) bere vodu donekonečna a hladina neklesne. Ideální zdroj pro kotel.",
            "Rotace spouští hadici, opačná ji navine. Rychlost čerpání určuje čerpadlo v potrubí.",
        ]),
        Q("p_boiler", "Kotel běží", dep=["p_water", "create:steam"], tasks=[adv("create:steam_engine")], icon="create:fluid_tank", xp=40, d=[
            "Postav nádrž aspoň ze 4 bloků (např. 2×2), na její bok parní motor s hřídelí, pod ni ohňohořák a přiveď vodu.",
            "Ohňohořák s palivem dá kotli 1 úroveň tepla. Bez paliva hřeje jen &epasivně&r, stejně jako magmatický blok, láva nebo oheň pod nádrží.",
            "Pasivní kotel dá jen osminu výkonu jednoho motoru (2 048 SU). Pro plný výkon hořáky krm.",
        ]),
        Q("p_levels", "Kotel úrovně 4", dep=["p_boiler", "p_hose"], items=[("create:steam_engine", 4)], xp=60, s="Expert", **M, d=[
            "Úroveň kotle určuje to nejslabší ze tří: &eteplo&r (1 za ohřátý hořák, 2 za přehřátý), &evelikost&r (4 bloky nádrže na úroveň) a &evoda&r (10 mB za tick na úroveň).",
            "Každá úroveň pohání naplno jeden motor. Úroveň 4: 4 hořáky pod nádrží, aspoň 16 bloků nádrže (např. 2×2×4) a 40 mB vody za tick. 4 motory pak dají 65 536 SU.",
            "&cVíc motorů než úrovní nic nepřidá,&r výkon se mezi ně jen rozdělí. Brýle na kotli ukážou, co chybí.",
        ]),
        Q("p_cake", "Ohňodort", dep=["p_levels", "create_ores:o_cinder", "create:spout"], items=[("create:blaze_cake", 4)], xp=50, d=[
            "&eOhňodort&r (&eBlaze Cake&r) udělá hořák &epřehřátý&r. Přehřátý hořák dá kotli 2 úrovně tepla místo jedné.",
            "Lis v tyglíku slisuje uškvařenou mouku, vejce a cukr na &ekorpus&r (&eBlaze Cake Base&r). Dávkovač na něj nalije 250 mB lávy.",
            "Hořák dort sní a chvíli hoří naplno. Krm ho pokladačem nebo paží. &aTip:&r Míchačka nad tyglíkem s přehřátým hořákem udělá z dlažebního kamene lávu (50 mB z kusu).",
        ]),
        Q("p_max", "Plný výkon", dep=["p_cake"], tasks=[adv("create:steam_engine_maxed")], icon="create:steam_engine", xp=100, s="Expert", **M, d=[
            "Nejvyšší úroveň kotle je 18. Potřebuješ 9 přehřátých hořáků pod nádrží 3×3, aspoň 72 bloků nádrže (3×3×8) a 180 mB vody za tick (2 čerpadla na 256 RPM).",
            "Na kotel pak dej 18 parních motorů. Dohromady dají 294 912 SU – to utáhne celou továrnu.",
            "&aTip:&r Hořáky krm automaticky (paže, pokladač) a vodu ber z hadicové kladky v moři. Jinak kotel časem klesne.",
        ]),
        Q("p_whistle", "Parní píšťala", dep=["p_boiler"], items=[("create:steam_whistle", 1)], xp=15, optional=True, d=[
            "&eParní píšťala&r (&eSteam Whistle&r): zlatý plát a měděný ingot. Polož ji na nádrž s teplem.",
            "S redstone signálem píská. Další píšťalou na ní snížíš tón, klíčem přepneš oktávu. Hodí se jako alarm nebo signál.",
        ]),
    ],
)

# ---------------------------------------------------------------------------
# 3) ZPRACOVÁNÍ RUD
# ---------------------------------------------------------------------------
ORES = dict(
    key="create_ores", group="create", title="Create: Zpracování rud",
    subtitle="Drcení, praní a hromadné tavení", icon="create:crushed_raw_iron",
    quests=[
        Q("o_intro", "Víc z každé rudy", dep=["create:washing"], tasks=[auto()], icon="create:crushed_raw_gold", xp=10, s="Začátečník", **M, d=[
            "Create umí z rud dostat víc: &edrtící kola&r rozdrtí rudu, &evětrák&r drť vypere nebo roztaví a k tomu padají bonusy.",
            "Postup: ruda → drtící kola → rozdrcená ruda (krátce &edrť&r) → praní (nugety + bonus) nebo tavení (ingot).",
            "Než budeš mít drtící kola, můžeš větrákem tavit, udit, prát štěrk a písek. To je začátek této kapitoly.",
            "&cMlýnský kámen rudy nezpracuje.&r Je levný a hodí se na mouku a štěrk. Na rudy potřebuješ drtící kola – dražší, ale zvládnou drcení i mletí.",
        ]),
        Q("o_smelt", "Hromadné tavení", dep=["o_intro"], tasks=[adv("create:fan_processing")], icon="minecraft:lava_bucket", xp=20, d=[
            "Větrák foukající přes &elávu&r taví vše, co by roztavila pec: písek na sklo, drť na ingoty. Palivo nepotřebuje.",
            "Lávu dej před větrák a předměty za ni na pás nebo desku. Místo lávy jde i ohňohořák s palivem. &cJídlo tady shoří!&r",
            "&aTip:&r Rychlost zpracování je pořád stejná. Víc předmětů najednou = víc práce za stejný čas.",
        ]),
        Q("o_smoke", "Hromadné uzení", dep=["o_intro"], items=[("minecraft:dried_kelp", 64)], xp=15, d=[
            "Větrák přes &eoheň&r nebo &etáborák&r udí: syrové jídlo upeče a chaluhy usuší. Jídlo se tu nespálí.",
            "Ohňohořák bez paliva udí taky.",
            "&aTip:&r Ze sušených chaluh jsou mechanické pásy. Udírna u chaluhové farmy ti dá pásů, kolik chceš.",
        ]),
        Q("o_haunt", "Hromadné prokletí", dep=["o_intro", "create:brass"], items=[("create:haunted_bell", 1)], xp=30, d=[
            "Větrák přes &eduší oheň&r nebo duší táborák věci &eprokleje&r: písek na duší písek, dlažební kámen na černý kámen (&eBlackstone&r).",
            "Takhle vznikne i &eprokletý zvon&r (&eHaunted Bell&r) z &epodivuhodného zvonu&r (&ePeculiar Bell&r = blok mosazi + mosazný plát).",
            "Prokletý zvon v ruce nebo po zazvonění ukáže tmavá místa, kde se můžou rodit monstra.",
        ]),
        Q("o_sand", "Praní písku", dep=["o_intro"], items=[("minecraft:clay_ball", 16)], xp=15, d=[
            "Praním písku dostaneš hroudu jílu (25 %). Červený písek dá zlaté nugety, duší písek křemen.",
            "Drtící kola později udělají ze štěrku písek. Kámen → štěrk → písek → praní je jednoduchá linka bez těžení.",
        ]),
        Q("o_crush", "Drcení rud", dep=["o_intro", "create:crushing"], items=[("create:crushed_raw_iron", 16)], xp=40, s="Pokročilý", **M, d=[
            "Drtící kola rozdrtí surové železo na &erozdrcené surové železo&r (&eCrushed Raw Iron&r). K tomu s 75% šancí padne nuget zkušeností.",
            "Celý blok rudy (vytěžený s očarováním &eSilk Touch&r) dá víc: železná, zlatá a zinková ruda 1 drť + 75 % na druhou, hlubinné verze 2 + 25 %. Měděná ruda dá 5, hlubinná 7.",
            "Teď už rudu nedávej rovnou do pece. Drť ještě vyper (bonus) nebo roztav. Z 1 drti je vždy 1 ingot nebo 9 nugetů.",
        ]),
        Q("o_wash", "Praní drti", dep=["o_crush"], items=[("create:copper_nugget", 18)], xp=30, d=[
            "Drť pošli větrákem přes vodu. Z každé drti je 9 nugetů a k tomu bonus:",
            "železo → redstone (75 %), měď → hrouda jílu (50 %), zlato → křemen (50 %), zinek → střelný prach (25 %).",
            "Praní se vyplatí víc než tavení: kovu je stejně, ale bonus máš navíc. Nugety slisuje lis v tyglíku zpátky na ingoty.",
        ]),
        Q("o_gold", "Zlato", dep=["o_crush"], items=[("create:crushed_raw_gold", 8)], xp=25, d=[
            "Zlatá ruda se drtí stejně. Při drcení s 75% šancí padnou 2 nugety zkušeností, praním dostaneš navíc křemen.",
            "&aTip:&r Netherová zlatá ruda dá v drtících kolech rovnou 18 zlatých nugetů, to jsou 2 ingoty z jednoho bloku.",
        ]),
        Q("o_zinc", "Zinek ve velkém", dep=["o_crush"], items=[("create:crushed_raw_zinc", 16)], xp=25, d=[
            "Na mosaz potřebuješ hodně zinku. Drť zinkovou rudu, nebo kámen &eazurín&r (&eAsurine&r): dá 30 % drti a 30 % zinkového nugetu.",
            "Podobně &ešarlanit&r (&eCrimsite&r) dá železo, &eokrum&r (&eOchrum&r) zlato a &everidium&r (&eVeridium&r) měď. Tyto kameny najdeš pod zemí ve vrstvách.",
        ]),
        Q("o_mek", "Rudy z Mekanismu", dep=["o_crush"], items=[("create:crushed_raw_osmium", 8)], xp=25, d=[
            "Drtící kola zvládnou i suroviny z &bMekanismu&r: osmium, cín, olovo a uran. Praním z drti dostaneš 9 nugetů.",
            "&aTip:&r Mekanism má vlastní, ještě výnosnější zpracování rud (kapitola Mekanism).",
        ]),
        Q("o_xp", "Nugety zkušeností", dep=["o_crush"], items=[("create:experience_nugget", 18)], xp=25, d=[
            "Při drcení rud padají &enugety zkušeností&r (&eNugget of Experience&r). Pravým tlačítkem z nich získáš zkušenosti.",
            "9 nugetů dá &eblok zkušeností&r (&eBlock of Experience&r). Šetři je na opravy a očarování.",
        ]),
        Q("o_cinder", "Uškvařená mouka", dep=["o_crush"], items=[("create:cinder_flour", 8)], xp=20, d=[
            "Drcením netherracku vznikne &euškvařená mouka&r (&eCinder Flour&r), občas i 2 kusy.",
            "Je potřeba na ohňodort, který přehřeje ohňohořák (kapitola Energie a stres).",
        ]),
        Q("o_obsidian", "Obsidiánová moučka", dep=["o_crush"], items=[("create:powdered_obsidian", 4)], xp=25, optional=True, d=[
            "Drcením obsidiánu vznikne &eobsidiánová moučka&r (&ePowdered Obsidian&r). S 75% šancí se ti obsidián navíc vrátí celý.",
            "Z moučky se sekvenční montáží dělá &erobustní plát&r (&eSturdy Sheet&r) na vlaky. Postup je v kapitole Vlaky.",
        ]),
        Q("o_line", "Automatická rudná linka", dep=["o_wash", "o_smelt"], tasks=[adv("create:crusher_maxed_0000")], icon="create:crushing_wheel", xp=80, s="Expert", **M, d=[
            "Spoj vše dohromady: truhla s rudou → trychtýř → drtící kola → pás → větrák s vodou → lis nad tyglíkem (nugety na ingoty) → trezor.",
            "Úkol: roztoč drtící kola na 256 RPM, tak drtí nejrychleji. Pár kol pak bere 4 096 SU, na to už potřebuješ silný zdroj, třeba parní kotel.",
            "&aTip:&r Drť padá pod kola, zachyť ji pásem nebo deskou. Na vstup dej trychtýř nebo šachtu.",
        ]),
    ],
)

# ---------------------------------------------------------------------------
# 4) LOGISTIKA
# ---------------------------------------------------------------------------
LOGI = dict(
    key="create_logistics", group="create", title="Create: Logistika",
    subtitle="Trychtýře, filtry a balíčková pošta", icon="create:packager",
    quests=[
        Q("l_intro", "Věci, které jezdí samy", dep=["create:belt"], tasks=[auto()], icon="create:andesite_funnel", xp=10, s="Začátečník", **M, d=[
            "Logistika znamená, že věci samy putují mezi stroji a truhlami.",
            "Začneš trychtýři, šachtami a pásy. Pak se naučíš třídit filtry a hlídat zásoby. Nakonec postavíš balíčkovou poštu, která doručí cokoli kamkoli.",
        ]),
        Q("l_funnel", "Andezitový trychtýř", dep=["l_intro"], items=[("create:andesite_funnel", 4)], xp=15, d=[
            "&eAndezitový trychtýř&r (&eAndesite Funnel&r): slitina nad sušenou chaluhou dá 2 kusy. Bere předměty z truhly nebo stroje, nebo je do nich dává.",
            "Normálně položený z truhly bere. Položený se Shiftem do ní dává. Klíčem ho otočíš i později. Na pásu bere nebo dává podle směru pásu.",
            "Bere po 1 kuse a redstone ho zastaví. &cMezi dvěma truhlami přímo nepřesouvá,&r mezi ně dej pás nebo šachtu.",
        ]),
        Q("l_chute", "Šachta", dep=["l_intro", "create:sheets"], items=[("create:chute", 8)], xp=15, d=[
            "&eŠachta&r (&eChute&r): 2 železné pláty a železný ingot dají 4 kusy. Vozí předměty dolů mezi inventáři.",
            "Větrák na konci šachty ji obrátí, pak vozí nahoru. Šachta položená na bok jiné šachty povede šikmo.",
        ]),
        Q("l_filter", "Filtry", dep=["l_funnel", "create:brass"], items=[("create:filter", 1), ("create:attribute_filter", 1)], xp=20, d=[
            "&eSeznam filtrů&r (&eList Filter&r): vlna mezi 2 železnými nugety. Pravým klikem do něj nastavíš předměty.",
            "Filtr vlož do &efiltrového slotu&r stroje (malé okénko na bloku). Stroj pak pracuje jen s vybranými věcmi.",
            "&eFiltr atributů&r (&eAttribute Filter&r, s mosaznými nugety) třídí podle vlastností, třeba „lze rozdrtit“ (&ecan be Crushed&r) nebo „lze sníst“ (&ecan be eaten&r).",
        ]),
        Q("l_brass_funnel", "Mosazný trychtýř", dep=["l_filter", "create:tube"], items=[("create:brass_funnel", 2)], xp=25, d=[
            "&eMosazný trychtýř&r (&eBrass Funnel&r): elektronka, mosazný ingot a sušená chaluha. Bere až celý stack najednou, přesný počet nastavíš na panelu.",
            "Má filtrový slot: dej do něj předmět nebo filtr a trychtýř propustí jen to.",
        ]),
        Q("l_tunnel", "Andezitový tunel", dep=["l_intro"], items=[("create:andesite_tunnel", 2)], xp=15, d=[
            "&eAndezitový tunel&r (&eAndesite Tunnel&r) zakryje pás. Když má otevřené boky, odebere z každého stacku 1 kus do strany. Zbytek jede dál.",
        ]),
        Q("l_brass_tunnel", "Mosazný tunel", dep=["l_tunnel", "create:tube"], items=[("create:brass_tunnel", 2)], xp=25, d=[
            "&eMosazný tunel&r (&eBrass Tunnel&r) má filtr na každé straně a třídí věci podle druhu.",
            "Tunely na souběžných pásech se spojí a rozdělují předměty mezi všechny pásy. Režim nastavíš na panelu: rozdělit, střídat (&eRound Robin&r), nejbližší, náhodně, synchronizovat.",
        ]),
        Q("l_smart_chute", "Chytrá šachta", dep=["l_chute", "create:tube"], items=[("create:smart_chute", 1)], xp=20, d=[
            "&eChytrá šachta&r (&eSmart Chute&r) je šachta s filtrem. Na panelu nastavíš, kolik kusů naráz pustí.",
            "Redstone signál ji zastaví.",
        ]),
        Q("l_hatch", "Dvířka na předměty", dep=["l_intro", "create:vault"], items=[("create:item_hatch", 1)], xp=15, d=[
            "&eDvířka na předměty&r (&eItem Hatch&r): slitina + železný poklop. Polož je na trezor nebo truhlu.",
            "Pravým klikem vložíš předmět z ruky do kontejneru. Shift + pravé tlačítko vloží vše kromě hotbaru.",
        ]),
        Q("l_ejector", "Zatížený katapult", dep=["l_intro", "create:depot"], items=[("create:weighted_ejector", 1)], xp=25, d=[
            "&eZatížený katapult&r (&eWeighted Ejector&r): zlatý plát, odkládací deska a ozubené kolečko. Hází předměty i hráče na vybrané místo.",
            "Drž ho a Shift + pravým klikem vyber cíl, pak ho polož. Cíl může být výš i níž, ale ne do strany. Potřebuje rotaci.",
            "Na panelu nastavíš, kolik kusů má čekat, než hodí.",
        ]),
        Q("l_threshold", "Prahový spínač", dep=["l_intro", "create:brass_casing", "create:tube"], items=[("create:stockpile_switch", 1)], xp=25, d=[
            "&ePrahový spínač&r (&eThreshold Switch&r) hlídá, jak plná je truhla, trezor nebo nádrž.",
            "Když obsah přeroste horní hranici, změní redstone signál. Vrátí ho, až obsah klesne pod dolní hranici. Hranice nastavíš v okně.",
            "&aTip:&r Spínač u skladu může spojkou vypnout výrobu, když je sklad plný.",
        ]),
        Q("l_observer", "Chytrý detektor", dep=["l_threshold"], items=[("create:content_observer", 1)], xp=20, d=[
            "&eChytrý detektor&r (&eSmart Observer&r) hlídá obsah kontejnerů, pásů, šachet a potrubí. S filtrem jen konkrétní věci.",
            "U trychtýře vyšle puls pokaždé, když jím projde předmět.",
        ]),
        Q("l_link", "Redstonový vysílač", dep=["l_intro", "create:sheets"], items=[("create:redstone_link", 2)], xp=20, d=[
            "&eRedstonový vysílač&r (&eRedstone Link&r) posílá redstone bez drátů až na 256 bloků. Vyrábí se z &evysílače&r (&eTransmitter&r) a andezitového pouzdra.",
            "Do dvou slotů dej předměty – to je „frekvence“. Spolu mluví jen vysílače se stejnou dvojicí. Shift + pravé tlačítko přepne na příjem.",
        ]),
        Q("l_display", "Displejový vysílač", dep=["l_link", "create:brass_casing"], items=[("create:display_link", 1)], xp=25, d=[
            "&eDisplejový vysílač&r (&eDisplay Link&r) ukazuje živé informace: obsah truhly, stres sítě, stav kotle a další.",
            "S vysílačem v ruce nejdřív klikni na cíl (cedule, displejová tabule, znaková výbojka). Pak ho polož na blok, ze kterého má číst. V okně vyber, co ukazovat.",
        ]),
        Q("l_board", "Displejová tabule", dep=["l_display", "create:tube"], items=[("create:display_board", 4)], xp=20, d=[
            "&eDisplejová tabule&r (&eDisplay Board&r): 2 slitiny a elektronka dají 2 kusy. Bloky vedle sebe tvoří jednu velkou obrazovku. Potřebuje rotaci.",
            "Pevný text napíšeš psací podložkou, živá data pošle displejový vysílač. Barvivem obarvíš řádek.",
        ]),
        Q("l_nixie", "Znaková výbojka", dep=["l_display", "create:tube"], items=[("create:nixie_tube", 2)], xp=15, optional=True, d=[
            "&eZnaková výbojka&r (&eNixie Tube&r): 2 elektronky dají 4 kusy. S redstone signálem ukáže jeho sílu.",
            "Psací podložkou na ni napíšeš text, barvivem změníš barvu.",
        ]),
        Q("l_cardboard", "Karton", dep=["l_intro", "create:mixer"], items=[("create:cardboard", 8)], xp=20, d=[
            "&eKarton&r (&eCardboard&r) je materiál na balíčky. Míchačka smíchá 4 kusy bambusu, cukrové třtiny nebo sazenic s 250 mB vody na &ebuničinu&r (&ePulp&r).",
            "Lis z buničiny udělá karton. 4 kartony dají &eblok kartonu&r, ten je v receptu balíkovače.",
        ]),
        Q("l_packager", "Balíkovač", dep=["l_cardboard", "l_funnel"], items=[("create:packager", 1)], xp=40, s="Pokročilý", **M, d=[
            "&eBalíkovač&r (&ePackager&r) zabalí obsah truhly do &ebalíčku&r. Přilož ho k truhle a dej mu redstone signál.",
            "Balíček je obyčejný předmět, vozí se pásem, šachtou nebo katapultem. Balíček vložený do balíkovače se rozbalí do jeho truhly.",
            "Teď už nevozíš jednotlivé věci, ale celé zásilky. &cBalíkovač nepřijme balíček, který se do truhly celý nevejde.&r",
        ]),
        Q("l_address", "Adresy", dep=["l_packager", "create:zinc"], items=[("create:package_filter", 1)], xp=25, d=[
            "Polož na balíkovač ceduli s nápisem, to je &eadresa&r. Každý balíček z něj ponese tento nápis.",
            "&eFiltr balíčků&r (&ePackage Filter&r, vlna a zinkové nugety) v trychtýři nebo tunelu propustí jen balíčky s danou adresou.",
        ]),
        Q("l_chain", "Řetězový dopravník", dep=["l_packager"], items=[("create:chain_conveyor", 2)], xp=30, d=[
            "&eŘetězový dopravník&r (&eChain Conveyor&r): velké ozubené kolečko a 4 andezitová pouzdra dají 2 kusy. Klikni řetězem na dva dopravníky a spojí se.",
            "Přenáší rotaci a vozí balíčky. Spojení měří až 32 bloků, jeden dopravník má nejvýš 4 spojení.",
            "S montážním klíčem v ruce se po řetězu můžeš svézt.",
        ]),
        Q("l_frogport", "Balíčkový žaboport", dep=["l_chain", "l_address"], items=[("create:package_frogport", 1)], xp=40, d=[
            "&eBalíčkový žaboport&r (&ePackage Frogport&r): slizová koule, trezor a slitina. S ním v ruce klikni na řetězový dopravník a polož ho poblíž.",
            "V jeho okně nastav adresu. Balíček s cizí adresou žába pošle po řetězu, balíček se svou adresou chytí.",
            "Žaboport bere z inventáře pod sebou i do něj dává, třeba z balíkovače. Tak vznikne pošta mezi budovami.",
        ]),
        Q("l_postbox", "Poštovní schránka", dep=["l_address"], items=[("create:white_postbox", 1)], xp=25, optional=True, d=[
            "&ePoštovní schránka&r (&ePostbox&r): barvivo, sud a slitina. S ní v ruce klikni na vlakovou stanici a polož ji poblíž.",
            "Balíčky s cizí adresou naloží vlak, který ve stanici zastaví. Balíčky s její adresou tu vlak vyloží. Funguje, i když u ní nikdo není a okolí není načtené.",
            "Jak postavit vlak, najdeš v kapitole Vlaky.",
        ]),
        Q("l_stock_link", "Skladový vysílač", dep=["l_packager", "l_link"], items=[("create:stock_link", 1)], xp=30, d=[
            "&eSkladový vysílač&r (&eStock Link&r): vysílač nad trezorem. Polož ho na balíkovač a zásoby jeho truhly se objeví v síti.",
            "Další díly připojíš tak, že jimi před položením klikneš na skladový vysílač.",
            "Signál má neomezený dosah, ale balíčky se musí dopravit: pásem, řetězem nebo vlakem.",
        ]),
        Q("l_keeper", "Skladník", dep=["l_stock_link"], items=[("create:stock_ticker", 1)], xp=40, d=[
            "&eSkladový ticker&r (&eStock Ticker&r): sklo, skladový vysílač a zlatý ingot. Před položením jím klikni na skladový vysílač.",
            "Před ticker posaď zvíře na sedačku (třeba &eWhite Seat&r) nebo polož ohňohořák. To je &eskladník&r (&eStock Keeper&r). Klikni na něj a objednávej věci ze všech připojených truhel.",
            "Objednané věci se zabalí do balíčků. Zadej adresu a balíčky dojedou k tobě.",
        ]),
        Q("l_requester", "Redstonový žadatel", dep=["l_keeper"], items=[("create:redstone_requester", 1)], xp=30, d=[
            "&eRedstonový žadatel&r (&eRedstone Requester&r) pošle stejnou objednávku při každém redstone pulsu. Nastavíš ji v jeho okně.",
            "&aTip:&r S časovačem signálu (&ePulse Timer&r) dostaneš pravidelné zásilky, třeba uhlí do pecí.",
        ]),
        Q("l_repackager", "Přebalovač", dep=["l_requester"], items=[("create:repackager", 1)], xp=25, d=[
            "&ePřebalovač&r (&eRe-Packager&r) vznikne z balíkovače v pracovním stole. Spojí části jedné objednávky zpátky do jednoho balíčku.",
            "Hodí se, když suroviny musí dorazit pohromadě a ve správném pořadí, třeba do mechanických výrobníků.",
        ]),
        Q("l_gauge", "Tovární měřidlo", dep=["l_keeper", "create:precision"], items=[("create:factory_gauge", 2)], xp=50, s="Expert", **M, d=[
            "&eTovární měřidlo&r (&eFactory Gauge&r): skladový vysílač + precizní strojek dají 2 kusy. Před položením klikni na skladový vysílač.",
            "Na balíkovači hlídá jeho truhlu a doplňuje ji ze sítě. Jinde hlídá celou síť: klikni na něj předmětem, který má sledovat.",
            "Podrž na něm pravé tlačítko a nastav cílové množství. Když zásoba klesne pod cíl, měřidlo samo objedná, co je potřeba.",
        ]),
        Q("l_factory", "Továrna na objednávku", dep=["l_gauge", "l_repackager"], tasks=[adv("create:factory_gauge")], icon="create:factory_gauge", xp=80, d=[
            "Propoj měřidla do receptu: měřidlo výrobku a měřidla surovin. V okně měřidla zadej adresu stroje, který výrobek dělá.",
            "Když výrobku ubude, síť tam pošle suroviny. Hotové výrobky musí jet zpátky do připojeného skladu. Zelené spojení = cíl je splněný.",
            "Na recepty z pracovního stolu stačí 3×3 mechanické výrobníky spojené klíčem. Měřidlo do nich balíčky rovnou rozbalí.",
        ]),
        Q("l_shop", "Vlastní obchod", dep=["l_keeper"], tasks=[adv("create:table_cloth_shop")], icon="create:andesite_table_cloth", xp=40, optional=True, d=[
            "Sklad obchodu napoj přes balíkovač a skladový vysílač. Do obchodu dej skladový ticker se skladníkem.",
            "S ubrusem (třeba &eWhite Table Cloth&r) v ruce klikni na skladníka a ubrus polož. Na boku nastav cenu.",
            "Ostatní hráči pak u ubrusu nakupují. Zboží se zabalí a doveze k pultu, platby se schovají ve skladovém tickeru.",
        ]),
    ],
)

# ---------------------------------------------------------------------------
# 5) STROJE A AUTOMATIZACE
# ---------------------------------------------------------------------------
AUTO = dict(
    key="create_auto", group="create", title="Create: Stroje a automatizace",
    subtitle="Udělátka, farmy a výrobní linky", icon="create:deployer",
    quests=[
        Q("a_intro", "Stroje, které se hýbou", dep=["create:casing"], tasks=[auto()], icon="create:mechanical_piston", xp=10, s="Začátečník", **M, d=[
            "&eUdělátko&r (&eContraption&r) je skupina bloků, které se hýbou spolu. Hýbe s nimi píst, ložisko, kladka, jeřáb nebo vozík.",
            "Na udělátko dej pracovní díly: vrták, pilu, sklízeč, pluh, pokladač. Pracují, když se udělátko hýbe. Truhla na udělátku sbírá, co vytěží.",
            "V této kapitole postavíš farmy a výrobní linky, které běží bez tebe.",
        ]),
        Q("a_glue", "Lepení", dep=["a_intro"], tasks=[adv("create:super_glue")], icon="create:super_glue", xp=15, d=[
            "Bloky se k udělátku musí přilepit. &eVteřinovým lepidlem&r klikni na dva rohy a vše v kvádru se slepí. Úderem s lepidlem v ruce oblast zrušíš.",
            "Bloky, které na něčem visí (pochodně, cedule), lepidlo většinou nepotřebují. Plachty se lepí samy.",
        ]),
        Q("a_piston", "Mechanický píst", dep=["a_intro"], items=[("create:mechanical_piston", 1), ("create:piston_extension_pole", 4)], xp=20, d=[
            "&eMechanický píst&r (&eMechanical Piston&r) posouvá bloky před sebou. Jak daleko, určují &eprodlužovací ojnice&r (&ePiston Extension Pole&r) za ním. Bez nich se nehne.",
            "Směr a rychlost určuje rotace, řadící páka ho pošle zpátky. Lepivý píst (&eSticky Mechanical Piston&r) bloky i přitáhne.",
            "Když se zastaví, udělátko se změní zpátky na bloky. Na panelu pístu to jde změnit.",
        ]),
        Q("a_gantry", "Portálový jeřáb", dep=["a_piston"], items=[("create:gantry_carriage", 1), ("create:gantry_shaft", 8)], xp=25, d=[
            "&eVozík portálového jeřábu&r (&eGantry Carriage&r) jezdí po &ehřídeli jeřábu&r (&eGantry Shaft&r) a veze přilepené bloky.",
            "Směr jízdy určuje natočení hřídele a směr její rotace. Hřídel s redstone signálem vozík zastaví.",
            "Jeřáby jdou skládat na sebe, pak se udělátko hýbe ve 2 nebo 3 osách.",
        ]),
        Q("a_pulley", "Lanová kladka", dep=["a_intro", "create:sheets"], items=[("create:rope_pulley", 1)], xp=20, d=[
            "&eLanová kladka&r (&eRope Pulley&r) spouští a zvedá bloky svisle. Směr a rychlost určuje rotace.",
            "&aTip:&r Prahový spínač u kladky změří, jak daleko je lano vysunuté.",
        ]),
        Q("a_chassis", "Šasi", dep=["a_glue"], items=[("create:linear_chassis", 3)], xp=20, d=[
            "&eLineární šasi&r (&eLinear Chassis&r) přilepí řadu bloků před sebou. Klikni slizovou koulí na jeho stěnu, tím ji uděláš lepivou. Klíčem nastavíš dosah.",
            "Stejná šasi vedle sebe se táhnou spolu. &eRadiální šasi&r (&eRadial Chassis&r) lepí bloky do kruhu kolem sebe, dobré na velké mlýny.",
        ]),
        Q("a_sticker", "Lepič", dep=["a_glue"], items=[("create:sticker", 1)], xp=15, optional=True, d=[
            "&eLepič&r (&eSticker&r) přilepí blok před sebou, když dostane redstone signál. Další signál blok zase pustí.",
            "Tak může udělátko blok vzít, odvézt a nechat jinde.",
        ]),
        Q("a_actors", "Pracující udělátko", dep=["a_piston", "create:drill"], tasks=[adv("create:contraption_actors")], icon="create:mechanical_drill", xp=30, s="Pokročilý", **M, d=[
            "Postav udělátko s vrtákem, pilou nebo sklízečem. Tyto díly pracují, když se udělátko hýbe.",
            "Přilep k udělátku truhlu nebo sud, vytěžené věci padají rovnou do ní.",
            "Teď už netěžíš ty, ale stroj. Pokladač na udělátku bere věci z jeho truhel – tak může zasít nebo položit bloky.",
        ]),
        Q("a_controls", "Ovládání udělátka", dep=["a_actors", "create:tube"], items=[("create:contraption_controls", 1)], xp=20, d=[
            "&eOvládací prvky udělátka&r (&eContraption Controls&r) zapnou a vypnou pracovní díly za jízdy.",
            "Filtrem vybereš, které díly ovládají. Dají se přilepit kamkoli na udělátko.",
        ]),
        Q("a_psi", "Přenosné rozhraní", dep=["a_actors", "create_logistics:l_chute"], items=[("create:portable_storage_interface", 2)], xp=30, d=[
            "&ePřenosné úložné rozhraní&r (&ePortable Storage Interface&r): andezitové pouzdro a šachta. Jedno dej na udělátko, druhé pevně na místo s mezerou 1–2 bloky.",
            "Když se míjí, spojí se. Pevné rozhraní pak vybírá (nebo plní) všechny truhly udělátka. Když se nic nepřesouvá, udělátko jede dál.",
        ]),
        Q("a_cart", "Montovna vozíků", dep=["a_glue"], items=[("create:cart_assembler", 1)], xp=25, d=[
            "&eMontovna vozíků&r (&eCart Assembler&r) leží na kolejích. S redstone signálem připojí přilepené bloky k projíždějícímu vozíku, bez signálu je zase rozloží.",
            "Udělátko na vozíku jezdí po obyčejných kolejích. Vrtáky a sklízeče tak pracují na dlouhé trase.",
        ]),
        Q("a_elevator", "Výtah", dep=["a_pulley", "create:brass_casing"], items=[("create:elevator_pulley", 1)], xp=30, optional=True, d=[
            "&eVýtahová kladka&r (&eElevator Pulley&r) vozí kabinu mezi patry. Na kabinu přilep redstonový kontakt (&eRedstone Contact&r), druhý dej proti němu v patře.",
            "Roztoč kladku a klikni na ni. Kontakty v patrech se změní na &ekontakty výtahu&r. Redstone puls na kontaktu zavolá výtah, posuvné dveře na kabině se otevírají samy.",
        ]),
        Q("a_farm", "Farma na plodiny", dep=["a_actors", "create:harvester"], items=[("create:mechanical_plough", 1)], xp=40, d=[
            "&eMechanický pluh&r (&eMechanical Plough&r) na udělátku dělá z hlíny ornici a rozbíjí měkké bloky, třeba trávu a květiny.",
            "Farma: pole a nad ním udělátko se sklízeči a truhlou, které jezdí tam a zpět (píst s řadící pákou). Sklízeč plodinu sklidí a nechá ji znovu růst.",
            "&aTip:&r Pokladač se semínky na udělátku zasadí prázdná místa.",
        ]),
        Q("a_trees", "Farma na stromy", dep=["a_intro", "create:drill", "create:deployer"], items=[("create:tree_fertilizer", 8)], xp=40, d=[
            "Pila pokácí celý strom, když přeřízne kmen u země. Pokladač naproti zasadí novou sazenici. Kmeny padají na zem, seber je trychtýřem nebo pásem.",
            "&eHnojivo&r (&eTree Fertilizer&r): 2 květiny, korál a kostní moučka dají 2 kusy. Vypěstuje strom i ve stísněném místě.",
            "&aTip:&r Druhý pokladač s hnojivem nebo kostní moučkou růst stromu urychlí.",
        ]),
        Q("a_cobble", "Generátor kamene", dep=["a_intro", "create:drill"], items=[("minecraft:cobblestone", 128)], xp=20, d=[
            "Postav obyčejný generátor kamene: láva a voda stečou k sobě a vznikne dlažební kámen. Před to místo dej mechanický vrták – bude kámen těžit pořád dokola.",
            "Vytěžený kámen vypadne na zem. Seber ho trychtýřem nebo pásem.",
            "&aTip:&r Mlýnský kámen udělá z kamene štěrk, drtící kola ze štěrku písek a větrák s lávou z písku sklo.",
        ]),
        Q("a_andesite", "Andezit bez těžení", dep=["a_cobble", "create:mixer"], items=[("minecraft:andesite", 64)], xp=40, d=[
            "Lis nad tyglíkem slisuje 2 pazourky, štěrk a 100 mB lávy na andezit. Štěrk i pazourek udělá mlýnský kámen z dlažebního kamene.",
            "Lávu dodá hadicová kladka v lávovém moři v Netheru (při aspoň 10 000 blocích lávy se nevyčerpá). Nebo ji udělá míchačka nad přehřátým ohňohořákem z dlažebního kamene.",
            "Tím máš andezit na slitinu bez kopání.",
        ]),
        Q("a_compacting", "Lisování v tyglíku", dep=["a_intro", "create:mixer"], tasks=[adv("create:compacting")], icon="create:basin", xp=20, d=[
            "Lis nad tyglíkem &ezhutňuje&r: udělá každý recept, který zaplní celé pole 2×2 nebo 3×3, a pár receptů navíc. Třeba 9 nugetů na ingot.",
            "Když dva recepty kolidují, vyber ten správný filtrem na lisu.",
        ]),
        Q("a_alloy", "Slitina ve velkém", dep=["a_compacting"], items=[("create:andesite_alloy_block", 4)], xp=40, d=[
            "Andezit a železný (nebo zinkový) nuget v tyglíku pod míchačkou dají andezitovou slitinu. Teplo není potřeba.",
            "Linka: trychtýře sypou andezit a nugety do tyglíku, výstup jde do truhly. Nugety dá praní štěrku nebo drti.",
            "&aTip:&r 9 slitin slisuj na blok, ušetříš místo.",
        ]),
        Q("a_brass", "Mosaz ve velkém", dep=["a_alloy", "create:brass"], items=[("create:brass_block", 4)], xp=50, d=[
            "Do tyglíku nad ohřátým ohňohořákem posílej měděné a zinkové ingoty v poměru 1 : 1. Míchačka z nich dělá mosaz pořád dokola.",
            "Hořák musí mít pořád palivo. Krm ho mechanickou paží nebo pokladačem.",
        ]),
        Q("a_feed", "Paže krmí hořák", dep=["a_brass", "create:arm"], tasks=[adv("create:arm_blaze_burner")], icon="create:blaze_burner", xp=30, d=[
            "Nastav mechanické paži jako vstup truhlu s uhlím a jako výstup ohňohořák. Paže pak hořák krmí sama.",
            "Paže nevezme víc, než může někam dát. S mosazným trychtýřem jako cílem bere jen to, co projde jeho filtrem.",
        ]),
        Q("a_saw", "Pila na pásu", dep=["a_intro", "create:drill"], tasks=[adv("create:saw_processing")], icon="create:mechanical_saw", xp=20, d=[
            "Pila otočená nahoru zpracuje předměty na pásu nebo hozené na ni. Umí recepty kameníkovy pily i recepty Create (v JEI „Řezání“ / &eSawing&r).",
            "&aTip:&r Pila nařeže z 1 andezitové slitiny 6 hřídelí. V pracovním stole jsou to jen 4.",
            "Když má výsledek víc možností, vyber ho filtrem na pile. Jinak se možnosti střídají.",
        ]),
        Q("a_deployer", "Triky s pokladačem", dep=["a_intro", "create:deployer"], tasks=[adv("create:deployer")], icon="create:deployer", xp=25, d=[
            "Pokladač se šmirglpapírem leští růženín. Se slitinou dělá pouzdra z oloupaných kmenů. Se semínky sází.",
            "S prázdným kbelíkem podojí krávu. Klíčem ho přepneš na levé tlačítko, pak těží nebo útočí.",
            "Redstone ho zastaví. &aTip:&r Krátké vypnutí signálu ho nechá udělat přesně jeden pohyb.",
        ]),
        Q("a_drain", "Cedník", dep=["create:spout"], items=[("create:item_drain", 1)], xp=20, d=[
            "&eCedník&r (&eItem Drain&r): železné mříže nad měděným pouzdrem. Vylévá tekutiny z předmětů, třeba z kbelíků a lahví.",
            "Předmět vlož z boku, přejede přes cedník a vyprázdní se. Tekutinu pak odčerpá potrubí.",
            "Spolu s dávkovačem přeléváš tekutiny mezi kbelíky a nádržemi.",
        ]),
        Q("a_honey", "Med z úlu", dep=["a_drain"], tasks=[adv("create:honey_drain")], icon="create:honey_bucket", xp=25, d=[
            "Potrubí s čerpadlem vysaje med přímo z úlu nebo včelího hnízda. Med je v Create tekutina.",
            "Dávkovač s ním plní lahve a dělá medová jablka. Lis v tyglíku z něj udělá blok medu.",
        ]),
        Q("a_many", "Velká linka", dep=["a_feed"], tasks=[adv("create:arm_many_targets")], icon="create:mechanical_arm", xp=60, s="Expert", **M, d=[
            "Nastav jedné mechanické paži 10 nebo víc výstupů. Jedna paže tak obslouží celou řadu strojů, třeba 10 tyglíků nebo hořáků.",
            "Režim rozdělování nastavíš na panelu: střídat, střídat bez přeskakování, nebo přednost má první cíl.",
            "Teď už máš všechno: zdroje, linky, třídění. Spoj je s balíčkovou logistikou a továrna pojede sama.",
        ]),
    ],
)

# ---------------------------------------------------------------------------
# 6) NÁSTROJE A SCHÉMATA
# ---------------------------------------------------------------------------
TOOLS = dict(
    key="create_tools", group="create", title="Create: Nástroje a schémata",
    subtitle="Výbava inženýra a stavění podle plánů", icon="create:schematicannon",
    quests=[
        Q("t_intro", "Výbava inženýra", dep=["create:wrench"], tasks=[auto()], icon="create:wrench", xp=10, s="Začátečník", **M, d=[
            "Create má i nástroje: poznámky, kufřík, potápěčskou výstroj, dalekosáhlou ruku a dělo na brambory.",
            "Na konci kapitoly se naučíš uložit stavbu do &eschématu&r a nechat ji postavit &eschématikanónem&r.",
        ]),
        Q("t_goggle_helmet", "Brýle na helmě", dep=["t_intro", "create:goggles"], items=[("creategoggles:goggle_iron_helmet", 1)], xp=20, d=[
            "Mod &bCreate Goggles&r připevní inženýrské brýle na helmu. V pracovním stole dej vedle sebe helmu a brýle.",
            "Máš pak ochranu helmy i informace z brýlí. Jde to s každou helmou od kožené po netheritovou, i s potápěcí.",
            "Drtící kola helmu s brýlemi zase rozeberou.",
        ]),
        Q("t_clipboard", "Psací podložka", dep=["t_intro"], items=[("create:clipboard", 1)], xp=15, d=[
            "&ePsací podložka&r (&eClipboard&r): slitina, papír a prkno. Pravým klikem si do ní píšeš poznámky a seznamy.",
            "Kopíruje nastavení: pravým klikem na blok (třeba filtr) ho zkopíruješ, levým klikem na jiný blok ho vložíš. Shift + pravým klikem ji připevníš na blok.",
        ]),
        Q("t_blueprint", "Výrobní plánek", dep=["t_intro"], items=[("create:crafting_blueprint", 1)], xp=15, d=[
            "&eVýrobní plánek&r (&eCrafting Blueprint&r): obraz a pracovní stůl. Pověs ho na zeď a do jeho políček nastav recepty.",
            "Pak stačí kliknout na políčko a předmět se vyrobí ze surovin, které neseš. Nemusíš chodit k pracovnímu stolu.",
        ]),
        Q("t_toolbox", "Kufřík na nářadí", dep=["t_intro"], items=[("create:brown_toolbox", 1)], xp=20, d=[
            "&eKufřík na nářadí&r (&eBrown Toolbox&r): ozubené kolečko, 2 zlaté pláty, truhla a kůže. Pojme hodně kusů z 8 různých druhů předmětů.",
            "Polož ho v dílně. Hráči poblíž podrží klávesu kufříku a vezmou si nářadí na dálku. Když ho sebereš, obsah v něm zůstane.",
        ]),
        Q("t_diving", "Potápěčská výstroj", dep=["t_intro", "create:backtank"], items=[("create:copper_diving_helmet", 1), ("create:copper_diving_boots", 1)], xp=30, d=[
            "&eMěděná potápěcí helma&r (&eCopper Diving Helmet&r) s nabitou tlakovou lahví na zádech ti dovolí dýchat pod vodou. Vzduch v láhvi pomalu ubývá.",
            "&eMěděné potápěcí boty&r (&eCopper Diving Boots&r): pod vodou rychleji klesáš, chodíš a skáčeš. Mechanický pás tě v nich neveze.",
        ]),
        Q("t_netherite_diving", "Potápění v lávě", dep=["t_diving"], items=[("create:netherite_diving_helmet", 1), ("create:netherite_backtank", 1)], xp=60, s="Expert", **M, d=[
            "Netheritovou helmu a láhev vyrobíš na kovářském stole: měděný díl + netheritový ingot + šablona netheritového vylepšení.",
            "S plnou sadou tě chrání před ohněm a lávou a v lávě lépe vidíš. &cMusíš mít i netheritové kalhoty a boty.&r Vzduch v láhvi pořád ubývá.",
        ]),
        Q("t_armored", "Obrněná láhev", dep=["t_intro", "create:backtank"], items=[("creategoggles:iron_backtank", 1)], xp=25, d=[
            "&bCreate Goggles&r spojí tlakovou láhev s náprsníkem. V pracovním stole dej vedle sebe náprsník a měděnou láhev.",
            "Máš pak brnění i vzduch v jednom slotu. Jde to s koženým, kroužkovým, železným, zlatým i diamantovým náprsníkem.",
        ]),
        Q("t_extendo", "Prodlužo rameno", dep=["t_intro", "create:precision", "create:crafter"], items=[("create:extendo_grip", 1)], xp=40, d=[
            "&eProdlužo rameno&r (&eExtendo Grip&r) v druhé ruce výrazně prodlouží tvůj dosah. Vyrábí se v mechanickém výrobníku.",
            "Normálně se opotřebovává. S tlakovou lahví na zádech bere místo toho vzduch.",
        ]),
        Q("t_potato", "Bramborové dělo", dep=["t_extendo", "create:fluids"], items=[("create:potato_cannon", 1)], xp=40, d=[
            "&eBramborové dělo&r (&ePotato Cannon&r) střílí vhodné předměty z tvého inventáře, třeba brambory. Vyrábí se v mechanickém výrobníku.",
            "S tlakovou lahví na zádech bere vzduch místo životnosti.",
        ]),
        Q("t_symmetry", "Hůlka souměrnosti", dep=["t_extendo"], items=[("create:wand_of_symmetry", 1)], xp=40, optional=True, d=[
            "&eHůlka souměrnosti&r (&eWand Of Symmetry&r) zrcadlí stavění. Klikni s ní na zem a objeví se zrcadlo. Se Shiftem otevřeš nastavení.",
            "Dokud je hůlka v hotbaru, každý blok se položí i zrcadlově na druhou stranu.",
        ]),
        Q("t_linked", "Propojený ovladač", dep=["t_intro", "create_logistics:l_link"], items=[("create:linked_controller", 1)], xp=30, d=[
            "&ePropojený ovladač&r (&eLinked Controller&r) má 6 tlačítek, která ovládají redstonové vysílače.",
            "Klikni ovladačem na přijímač a stiskni jedno z tlačítek – tím ho na přijímač naladíš. Shift + pravým klikem otevřeš ruční nastavení.",
            "Pravým klikem ovladač zapneš, pak pohybové klávesy posílají signály. Dá se položit na řečnický pult.",
        ]),
        Q("t_quill", "Uložení stavby", dep=["t_intro"], items=[("create:schematic_and_quill", 1)], xp=25, s="Pokročilý", **M, d=[
            "&eSchéma s brkem&r (&eSchematic And Quill&r): prázdné schéma (papír + světle modré barvivo) a pírko.",
            "Pravým klikem vyber 2 rohy stavby. Ctrl + kolečko myši posune stěnu výběru. Dalším pravým klikem stavbu ulož do souboru na svém počítači.",
            "Teď už nemusíš stavět blok po bloku – stavbu jednou uložíš a pak ji postavíš znovu kdekoli.",
        ]),
        Q("t_table", "Schématický stůl", dep=["t_quill"], items=[("create:schematic_table", 1)], xp=20, d=[
            "&eSchématický stůl&r (&eSchematic Table&r) nahraje uložený soubor na prázdné schéma. Vlož prázdné schéma a vyber soubor ze seznamu.",
            "Soubory jsou ve složce &eschematics&r ve složce hry. Můžeš tam dát i schémata od kamarádů.",
        ]),
        Q("t_schematic", "Hologram stavby", dep=["t_table"], items=[("create:schematic", 1)], xp=20, d=[
            "S hotovým &eschématem&r (&eSchematic&r) v ruce uvidíš hologram stavby. Nástroji na obrazovce ho posuneš a otočíš.",
            "Shift + pravé tlačítko otevře okno pro přesné souřadnice.",
        ]),
        Q("t_cannon", "Schématikanón", dep=["t_schematic"], items=[("create:schematicannon", 1)], xp=60, s="Expert", **M, d=[
            "&eSchématikanón&r (&eSchematicannon&r) postaví stavbu ze schématu sám. Vlož do něj schéma, vedle něj dej truhlu s materiálem a do kanónu střelný prach.",
            "V jeho okně stavbu spustíš. Co chybí, ukáže seznam.",
            "&aTip:&r Skladník (kapitola Logistika) umí objednat materiál podle seznamu, který kanón vytiskne na psací podložku.",
        ]),
        Q("t_jetpack", "Netheritový jetpack", dep=["create:jetpack", "t_netherite_diving"], items=[("create_jetpack:netherite_jetpack", 1)], xp=80, d=[
            "Netheritový jetpack vyrobíš na kovářském stole: jetpack + netheritový ingot + šablona netheritového vylepšení.",
            "Je to netheritová tlaková láhev s tryskami. Ovládá se stejně jako obyčejný jetpack.",
        ]),
    ],
)

# Pořadí kapitol této oblasti v knize questů
CHAPTERS = [CREATE, POWER, ORES, LOGI, AUTO, TOOLS]

NO_RECIPE = {
    "create:schematic": "vznikne zápisem souboru na prázdné schéma ve Schematic Table (tooltip stolu)",
}
