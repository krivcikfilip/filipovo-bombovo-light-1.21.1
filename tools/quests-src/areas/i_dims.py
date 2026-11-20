from engine import *

# Úrovně hráče pro milníky (podnázev s=)
ZAC, POK, EXP = "Začátečník", "Pokročilý", "Expert"

# =====================================================================
#  NETHER (+ původní questy o Endu)
# =====================================================================
NETHER_END = dict(
    key="nether_end", group="explore", title="Nether a End",
    subtitle="Pekelný svět a cesta na konec hry", icon="minecraft:netherrack",
    quests=[
        Q("intro", "Nether a End", tasks=[auto()], icon="minecraft:netherrack", xp=10, d=[
            "&bNether&r je horký podzemní svět plný lávy, ohně a nebezpečných mobů. Vede do něj portál z obsidiánu.",
            "V této kapitole se na Nether připravíš, najdeš pevnost a bastion, vyrobíš netherit a otevřeš cestu do &bEndu&r.",
            "Nether rozšiřují mody &bIncendium&r, &bJaden's Nether Expansion&r, &bJust-In NETHER&r, &bNether Exotics&r a &bMoog's Nether Structures&r. Každý má v kapitole svou větev."]),

        # ---------- Začátečník: první kroky ----------
        Q("nether", "Vítej v pekle", dep=["intro"], tasks=[dim("minecraft:the_nether")], icon="minecraft:obsidian", xp=40,
          shape="hexagon", size=1.5, s=ZAC, d=[
            "Postav rám portálu z obsidiánu (&eObsidian&r). Nejmenší rám je 4 bloky široký a 5 bloků vysoký. Zapal ho křesadlem (&eFlint and Steel&r) a projdi.",
            "&cV Netheru nespi v posteli – vybuchne!&r Voda se tu hned vypaří.",
            "Vezmi si jídlo, bloky na stavění a křesadlo. Když ti ghast portál zhasne, zapal ho znovu."]),
        Q("gold", "Zlatá zbroj", dep=["nether"], items=[("minecraft:golden_helmet", 1)], xp=20, d=[
            "Piglini (prasečí lidé v Netheru) na tebe nezaútočí, když máš na sobě aspoň jeden kus zlaté zbroje.",
            "Stačí zlatá helma (&eGolden Helmet&r) z 5 zlatých ingotů.",
            "&cPozor:&r když otevřeš jejich truhlu nebo rozbiješ zlatý blok, rozzlobí se i tak."]),
        Q("barter", "Výměna s pigliny", dep=["gold"], tasks=[adv("minecraft:nether/distract_piglin")], icon="minecraft:gold_ingot", xp=20, d=[
            "Piglini milují zlato. Hoď piglinovi zlatý ingot (klávesa Q). Chvíli si ho prohlíží a pak ti hodí něco na oplátku.",
            "Můžeš dostat třeba obsidián, perly Enderu, provázky nebo lektvar ohnivzdornosti.",
            "&aTip:&r výměna je snadný zdroj perel Enderu, které budeš potřebovat na cestu do Endu."]),
        Q("fortress", "Netherová pevnost", dep=["nether"], tasks=[structure("betterfortresses:fortress")], icon="minecraft:nether_bricks", xp=40, d=[
            "Pevnost je obrovská stavba z netherových cihel. Mod &bYUNG's Better Nether Fortresses&r ji přestavěl – je větší a má víc místností a truhel.",
            "Žijí v ní ohniváci (&eBlaze&r) a wither kostlivci (&eWither Skeleton&r). Roste tu i pekelná bradavice.",
            "&aTip:&r v pevnosti je snadné se ztratit. Značkuj si cestu pochodněmi na jedné straně chodby."]),
        Q("blaze", "Ohnivé tyče", dep=["fortress"], items=[("minecraft:blaze_rod", 6)], xp=30, d=[
            "Ohniváci se objevují u líhní (&eMonster Spawner&r) v pevnosti. Po zabití z nich padá ohnivá tyč (&eBlaze Rod&r).",
            "Z tyče vyrobíš varný stojan a ohnivý prach. Ohnivý prach je potřeba na oči Enderu.",
            "&aTip:&r ohniváci střílí ohnivé koule. Sněhové koule je zraňují a lektvar ohnivzdornosti tě ochrání."]),
        Q("wart", "Pekelná bradavice", dep=["fortress"], items=[("minecraft:nether_wart", 4)], xp=20, d=[
            "Pekelná bradavice (&eNether Wart&r) roste na duší písku v pevnostech. Je základ skoro všech lektvarů.",
            "Zasaď ji doma na duší písek (&eSoul Sand&r). Roste i v Overworldu, takže ji stačí najít jen jednou."]),
        Q("brew", "Vař lektvary", dep=["wart", "blaze"], tasks=[adv("minecraft:nether/brew_potion")], icon="minecraft:brewing_stand", xp=30, d=[
            "Postav varný stojan (&eBrewing Stand&r) z ohnivé tyče a 3 dlažebních kostek. Jako palivo do něj dej ohnivý prach.",
            "Lahev vody + pekelná bradavice = základní lektvar (&eAwkward Potion&r). Ten + magmový krém (&eMagma Cream&r) = lektvar ohnivzdornosti.",
            "S ohnivzdorností ti oheň ani láva neublíží. Magmový krém padá z magmových kostek v Netheru."]),

        # ---------- Bastion a netherit (Pokročilý) ----------
        Q("bastion", "Bastion", dep=["gold"], tasks=[structure("minecraft:bastion_remnant")], icon="minecraft:gilded_blackstone", xp=50, d=[
            "Bastion je zřícenina z černého kamene, kde žijí piglini. Je tu hodně zlata a dobré truhly.",
            "&cPozor na piglinské surovce (&ePiglin Brute&c) – zlatá zbroj na ně nefunguje a útočí hned.&r",
            "V truhlách najdeš šablonu na vylepšení netheritu. Bez ní netheritovou výbavu nevyrobíš."]),
        Q("template", "Netheritová šablona", dep=["bastion"], items=[("minecraft:netherite_upgrade_smithing_template", 1)], xp=40, d=[
            "Kovářská šablona (&eSmithing Template&r) na vylepšení netheritu leží v truhlách bastionu.",
            "Při vylepšení se šablona spotřebuje. Kopii vyrobíš ze šablony, 7 diamantů a 1 bloku netherracku – dostaneš 2 šablony."]),
        Q("debris", "Starověké trosky", dep=["nether"], items=[("minecraft:ancient_debris", 2)], xp=60,
          shape="hexagon", size=1.5, s=POK, d=[
            "Teď už nejde jen o přežití. Netherit je nejlepší materiál běžného Minecraftu. Jeho ruda jsou starověké trosky (&eAncient Debris&r).",
            "Trosky jsou hluboko, nejčastěji kolem výšky Y 15. Vydrží výbuch, proto je hráči hledají pomocí TNT nebo vybuchujících postelí.",
            "Těžíš je diamantovým krumpáčem. Trosky nehoří v lávě, takže se ti neztratí."]),
        Q("netherite", "Netherit", dep=["debris"], items=[("minecraft:netherite_ingot", 1)], xp=100, d=[
            "Trosky přetav v peci na netheritový šrot (&eNetherite Scrap&r). 4 šroty + 4 zlaté ingoty = 1 netheritový ingot.",
            "Ještě silnější verze netheritu nabízí mod &bAdvanced Netherite&r. Najdeš ho v kapitole &bVýbava a boj&r."]),
        Q("netherite_gear", "Netheritová výbava", dep=["netherite", "template"], items=[("minecraft:netherite_pickaxe", 1)], xp=80, d=[
            "Netheritovou výbavu nevyrobíš přímo. Diamantovou věc vylepšíš na kovářském stole (&eSmithing Table&r).",
            "Do stolu dej šablonu, diamantový krumpáč a netheritový ingot. Očarování zůstanou.",
            "Netheritové věci nehoří v lávě a vydrží víc než diamantové."]),

        # ---------- Wither (Expert) ----------
        Q("skull", "Lebka wither kostlivce", dep=["fortress"], items=[("minecraft:wither_skeleton_skull", 3)], xp=60, d=[
            "Wither kostlivci v pevnosti občas upustí svou lebku (&eWither Skeleton Skull&r). Potřebuješ 3.",
            "&aTip:&r meč s očarováním Drancování (&eLooting&r) zvýší šanci, že lebka padne."]),
        Q("wither", "Wither", dep=["skull"], items=[("minecraft:nether_star", 1)], xp=150,
          shape="hexagon", size=1.5, s=EXP, d=[
            "Wither je boss, kterého si vyvoláš sám: 4 bloky duší písku do tvaru T a na ně 3 lebky wither kostlivců.",
            "&cWither ničí bloky kolem sebe. Bojuj s ním hluboko pod zemí nebo daleko od základny!&r",
            "Po smrti upustí hvězdu Netheru (&eNether Star&r). Z ní vyrobíš maják a v Incendiu s ní vyvoláš dalšího bosse."]),

        # ---------- Jaden's Nether Expansion ----------
        Q("ssv", "Údolí duší", dep=["nether"], tasks=[biome("minecraft:soul_sand_valley")], icon="minecraft:soul_sand", xp=20, d=[
            "Údolí duší (&eSoul Sand Valley&r) je modrý biom z duší písku. Mod &bJaden's Nether Expansion&r ho zaplnil duchy a novými stavbami.",
            "Žijí tu duchové &eApparition&r, &eVessel&r a &eEcto Slab&r. Z &eEcto Slab&r padají fantomové střepy (&ePhasmo Shard&r)."]),
        Q("soulglass", "Duší sklo", dep=["ssv"], items=[("netherexp:soul_glass", 4)], xp=20, d=[
            "Duší sklo (&eSoul Glass&r) vyrobíš z 1 skla a 4 fantomových střepů. Dostaneš 2 kusy.",
            "Přes duší sklo můžeš projít, jako by tam nebylo. Hodí se na tajné dveře."]),
        Q("jne_sanctum", "Svatyně v údolí duší", dep=["ssv"], tasks=[structure("netherexp:sanctum")], icon="netherexp:treacherous_candle", xp=50, d=[
            "Svatyně (&eSanctum&r) je strašidelný hrad v údolí duší. V jejích truhlách najdeš jídlo a zásoby.",
            "V aréně svatyně stojí svíce zrady (&eCierge of Treachery&r)."]),
        Q("cierge", "Svíce zrady", dep=["jne_sanctum"], tasks=[adv("netherexp:nether/soul_sand_valley/rekindled_betrayal")], icon="netherexp:treacherous_wax", xp=60, d=[
            "Zapal svíci zrady křesadlem. Spustí se vlny nepřátel, které chtějí svíci zničit. Ubraň ji!",
            "Za výhru dostaneš jiskru zrady (&eSpark of Treachery&r). Otevřeš s ní zamčené ohnivé truhly (&eBrazier Chest&r) ve svatyni.",
            "&aTip:&r rozbitou svíci opravíš plástvemi medu."]),
        Q("shotgun", "Brokovnicová pěst", dep=["cierge", "netherite"], items=[("netherexp:shotgun_fist", 1)], xp=100, optional=True, d=[
            "V ohnivých truhlách může být jádro brokovnice (&eShotgun Core&r). Z něj vyrobíš brokovnicovou pěst (&eShotgun-Fist&r).",
            "Recept: jádro brokovnice, 2 netheritové ingoty a lebka kostlivce. Náboje (&eShotgun Shell&r) vyrobíš z &eWraithing Flesh&r, uhlí a železného nugetu."]),

        # ---------- Just-In NETHER a Nether Exotics ----------
        Q("jin", "Kruorit", dep=["nether"], items=[("just_in_nether:cruorite", 1)], xp=40, d=[
            "Mod &bJust-In NETHER&r přidává býčí bojovníky (&eBullkin&r). Silný &eBullkindar&r žije v netherových pustinách a ve zkřiveném lese.",
            "Bullkindar po smrti upustí &eKindarx&r. Ten přetav ve vysoké peci (&eBlast Furnace&r) na kruorit (&eCruorite&r).",
            "Podobně z &ePigmar&r (pustiny a karmínový les) padá &ePigar&r a z něj je devourit (&eDevourite&r).", "&cV tomto packu z kruoritu ani devouritu nic nevyrobíš. Jsou to zatím sběratelské kovy.&r"]),
        Q("exotics", "Netherové ovoce", dep=["nether"], items=[("netherexotics:kiwano", 1), ("netherexotics:pitaya", 1)], xp=30, d=[
            "Mod &bNether Exotics&r přidává do Netheru zvláštní ovocné stromy a rostliny.",
            "&eKiwano&r dá na chvíli ohnivzdornost, ale i krátkou otravu. &ePitaya&r vyléčí efekt wither.",
            "Z ovoce a lahve vyrobíš džus se stejným účinkem."]),
        Q("rambutan", "Rambutanová helma", dep=["exotics"], items=[("netherexotics:rambutan_helmet", 1)], xp=20, optional=True, d=[
            "&eRambutan&r je chlupaté ovoce z Netheru. Když ho sníš, dostaneš regeneraci.",
            "Z 5 rambutanů vyrobíš rambutanovou helmu (&eRambutan Helmet&r). Když zakroutíš hlavou, vystřelí trny."]),

        # ---------- Incendium ----------
        Q("inc_biome", "Biomy Incendia", dep=["nether"], tasks=[adv("incendium:misc/root")], icon="minecraft:crimson_nylium", xp=30, d=[
            "Mod &bIncendium&r přidává do Netheru nové biomy a v nich vlastní stavby a nepřátele.",
            "Quest se splní, až vstoupíš do jednoho z nich: popelavé pustiny, pekelné duny, křemenné pláně, zvadlý les, sopečné delty, převrácený les nebo plačící údolí."]),
        Q("withered", "Neklidný duch", dep=["inc_biome"], tasks=[adv("incendium:withered_forest/kill_spirit")], icon="minecraft:wither_rose", xp=40, d=[
            "Zvadlý les (&eWithered Forest&r) je staré bojiště piglinů a wither kostlivců.",
            "Bloudí tu neklidní duchové. Zabij jednoho z nich."]),
        Q("pvillage", "Piglinská vesnice", dep=["inc_biome", "gold"], tasks=[adv("incendium:misc/loot_piglin_village")], icon="minecraft:gold_block", xp=40, d=[
            "V Incendiu žijí piglini i ve vesnicích s kovárnou, řeznictvím a farmami. Vesnice stojí v karmínovém a zkřiveném lese.",
            "Vykraď truhlu v piglinské vesnici. &cStráže se budou bránit.&r"]),
        Q("inc_sanctum", "Svatyně illagerů", dep=["inc_biome"], tasks=[structure("incendium:sanctum")], icon="minecraft:quartz_block", xp=50, d=[
            "Na křemenných pláních (&eQuartz Flats&r) stojí svatyně illagerů (&eSanctum&r).",
            "Uvnitř je trezor s pokladem. Hlídají ho stráže, které ti dávají únavu z těžby. Když je porazíš, únava zmizí."]),
        Q("castle", "Zakázaný hrad", dep=["inc_biome"], tasks=[structure("incendium:forbidden_castle")], icon="minecraft:polished_blackstone_bricks", xp=60,
          shape="hexagon", size=1.5, s=POK, d=[
            "Teď přijdou opravdové výzvy. V popelavých pustinách (&eAsh Barrens&r) stojí zakázaný hrad (&eForbidden Castle&r).",
            "Hrad je plný piglinů s kušemi, meči i lektvary. Vezmi si nejlepší zbroj, jídlo a lektvary léčení.",
            "V truhlách jsou vzácné zbraně a artefakty."]),
        Q("conquer", "Dobyvatel", dep=["castle"], tasks=[adv("incendium:ash_barrens/conquer_castle")], icon="minecraft:netherite_sword", xp=150, optional=True, d=[
            "Vtrhni do zakázaného hradu a zabij v něm úplně všechny pigliny.",
            "Tohle je jedna z nejtěžších výzev v Netheru. Jdi tam s netheritovou výbavou."]),
        Q("altar", "Pekelný oltář", dep=["inc_biome"], tasks=[structure("incendium:infernal_altar")], icon="minecraft:magma_block", xp=40, d=[
            "V pekelných dunách (&eInfernal Dunes&r) stojí pekelný oltář (&eInfernal Altar&r).",
            "Až budeš mít hvězdu Netheru, vyvoláš tu bosse."]),
        Q("inferno", "Vznášející se peklo", dep=["altar", "wither"], tasks=[adv("incendium:infernal_dunes/inferno/kill")], icon="minecraft:fire_charge", xp=200,
          shape="hexagon", size=1.5, s=EXP, d=[
            "Vrchol Netheru: hoď na oltář hvězdu Netheru (klávesa Q). Objeví se boss &eHovering Inferno&r.",
            "Boss létá, sesílá ohnivá kouzla a před smrtí zkusí poslední velké kouzlo. Přežij ho a porazíš ho.",
            "&cPotřebuješ ohnivzdornost, hodně léčení a dobrou zbraň na dálku.&r"]),

        # ---------- Moog's Nether Structures ----------
        Q("mns", "Netherové stavby", dep=["nether"], tasks=[structure("mns:crimson_forge")], icon="minecraft:crimson_planks", xp=20, optional=True, d=[
            "Mod &bMoog's Nether Structures&r přidává do Netheru desítky menších i velkých staveb.",
            "Najdi karmínovou kovárnu (&eCrimson Forge&r). Stojí v karmínovém lese."]),
        Q("mns_fortress", "Megapevnost", dep=["mns"], tasks=[structure("mns:mega_fortress")], icon="minecraft:red_nether_bricks", xp=60, optional=True, d=[
            "Jedna z největších a nejvzácnějších staveb z &bMoog's Nether Structures&r je megapevnost (&eMega Fortress&r).",
            "Je obrovská a dobře hlídaná. Vezmi si s sebou zásoby jako do pevnosti."]),

        # ---------- Alex's Mobs boss v Netheru (původní) ----------
        Q("mosco", "Zkřivený mosco", dep=["nether"], tasks=[kill("alexsmobs:warped_mosco")], icon="alexsmobs:spawn_egg_warped_mosco", xp=200, optional=True, d=[
            "&eWarped Mosco&r je obří zmutovaný komár a jeden z bossů modu &bAlex's Mobs&r.",
            "Vznikne, když krvavý komár (&eCrimson Mosquito&r) vysaje krev z houbového tvora &eMungus&r, který nese zkřivenou houbu.",
            "Je to silný boss. Z jeho svalu (&eWarped Muscle&r) a vaků (&eHemolymph Sac&r) vyrobíš zbraň &eHemolymph Blaster&r."]),

        # ---------- Cesta do Endu (původní questy) ----------
        Q("eyes", "Oči Enderu", dep=["blaze"], items=[("minecraft:ender_eye", 12)], xp=40, d=[
            "Oko Enderu (&eEye of Ender&r) vyrobíš z perly Enderu a ohnivého prachu.",
            "Perly padají z endermanů. Hodně jich získáš i výměnou s pigliny.",
            "Potřebuješ jich až 12 – tolik chybí v rámu portálu do Endu. Několik se ti rozbije při hledání pevnosti."]),
        Q("stronghold", "Sleduj oko", dep=["eyes"], tasks=[adv("minecraft:story/follow_ender_eye")], icon="minecraft:ender_eye", xp=40,
          shape="hexagon", size=1.5, s=EXP, d=[
            "Nether máš zvládnutý, další cíl je End. Cesta tam vede přes portál v pevnosti (&eStronghold&r) v Overworldu.",
            "Hoď oko Enderu do vzduchu (pravé tlačítko). Poletí směrem k pevnosti. Jdi za ním a házej znovu.",
            "Když oko spadne dolů, pevnost je přímo pod tebou. Mod &bYUNG's Better Strongholds&r z ní udělal velké bludiště. Najdi místnost s portálem a do prázdných rámů vlož oči Enderu."]),
        Q("end", "End", dep=["stronghold"], tasks=[dim("minecraft:the_end")], icon="minecraft:end_stone", xp=60, d=[
            "Projdi portálem do Endu. Ocitneš se na ostrově s Enderovým drakem.",
            "&cZ Endu se vrátíš jen tak, že draka porazíš, nebo zemřeš.&r Vezmi si luk, hodně šípů, bloky a dýni na hlavu proti endermanům.",
            "Další postup najdeš v kapitole &bEnd&r."]),
        Q("dragon_kill", "Enderův drak", dep=["end"], tasks=[kill("minecraft:ender_dragon")], icon="minecraft:dragon_head", xp=200, d=[
            "Drak se léčí z krystalů na vrcholcích obsidiánových věží. Nejdřív je rozstřel lukem. Některé mohou být chráněné klecí – k nim vylez.",
            "Mod &bYUNG's Better End Island&r přestavěl hlavní ostrov, takže vypadá jinak než ve vanille.",
            "Když drak sedí na portálu uprostřed, bij ho mečem. &cNedívej se endermanům do očí.&r"]),
        Q("dragon", "Dračí dech", dep=["dragon_kill"], items=[("minecraft:dragon_breath", 1)], xp=150, d=[
            "Drak během boje plive fialový dech. Naber ho do prázdné lahve (&eGlass Bottle&r).",
            "Dračí dech (&eDragon's Breath&r) je potřeba na lektvary s dlouhým oblakem (&eLingering Potion&r).",
            "&aTip:&r drak se dá vyvolat znovu – stačí položit 4 krystaly Endu na okraj portálu."]),
        Q("elytra", "Krovky", dep=["dragon", "the_end:end_city"], items=[("minecraft:elytra", 1)], xp=150, d=[
            "Krovky (&eElytra&r) visí v rámu na lodi u města v Endu. Město najdeš na vnějších ostrovech.",
            "S krovkami plachtíš vzduchem. Ohňostroj (&eFirework Rocket&r) tě v letu urychlí.",
            "Mod &bElytra Slot&r ti dá zvláštní slot na krovky, takže můžeš nosit i hrudní plát."]),
        Q("crystal", "Neobvyklý End", dep=["the_end:outer"], items=[("unusualend:shiny_crystal", 1)], xp=40, d=[
            "Mod &bUnusual End&r přidává na vnější ostrovy nové biomy, stavby a moby.",
            "Lesklý krystal (&eShiny Crystal&r) získáš z lesklého gloopstonu (&eShiny Gloopstone&r) v biomu &eGloopstone Highlands&r, z urn a z truhel.",
            "Další věci z tohoto modu najdeš v kapitole &bEnd&r."]),
        Q("voidworm", "Červ prázdnoty", dep=["the_end:outer"], tasks=[kill("alexsmobs:void_worm")], icon="alexsmobs:void_worm_eye", xp=250, optional=True, d=[
            "&eVoid Worm&r je obří boss z modu &bAlex's Mobs&r. Žije v prázdnotě pod ostrovy Endu.",
            "Vylákáš ho tak, že hodíš do prázdnoty Endu tajemného červa (&eMysterious Worm&r). Toho získáš, když dáš larvu krvavého komára (&eCrimson Mosquito Larva&r) do kapsidy (&eCapsid&r).",
            "Útoč hlavně na hlavu. Když zničíš článek těla, červ se rozdělí na dva. Bojuj na velké plošině a ber zbraně na dálku."]),
    ],
)

# =====================================================================
#  END (nová kapitola)
# =====================================================================
THE_END = dict(
    key="the_end", group="explore", title="End",
    subtitle="Ostrovy v prázdnotě", icon="minecraft:end_crystal",
    quests=[
        Q("intro", "Za drakem", dep=["nether_end:dragon_kill"], tasks=[auto()], icon="minecraft:end_crystal", xp=10, d=[
            "Drak je poražený, ale End teprve začíná. Daleko od hlavního ostrova leží vnější ostrovy s městy, poklady a novými biomy.",
            "Tady je rozšiřují mody &bNullscape&r, &bUnusual End&r, &bEnderman Overhaul&r, &bMoog's End Structures&r a &bMedieval Buildings End Edition&r.",
            "&cPod ostrovy je prázdnota. Kdo do ní spadne, zemře a přijde o věci.&r Vždy měj u sebe bloky."]),

        # ---------- Začátečník ----------
        Q("gateway", "Brána do dálky", dep=["intro"], tasks=[adv("minecraft:end/enter_end_gateway")], icon="minecraft:ender_pearl", xp=40,
          shape="hexagon", size=1.5, s=ZAC, d=[
            "Po smrti draka se na okraji hlavního ostrova objeví malá brána (&eEnd Gateway&r) v rámu z podloží.",
            "Hoď do ní perlu Enderu, nebo do ní vleť. Přenese tě asi 1000 bloků daleko na vnější ostrovy.",
            "&aTip:&r u brány na druhé straně si postav malou plošinu, ať najdeš cestu zpátky."]),
        Q("outer", "Vnější ostrovy", dep=["gateway"], tasks=[biome("minecraft:end_highlands")], icon="minecraft:chorus_flower", xp=30, d=[
            "Vnější ostrovy jsou velké a roste na nich chorus (&eChorus Plant&r). Biom &eEnd Highlands&r tvoří vysoké ostrovy. Stojí na nich města a prastaré věže.",
            "Ovoce chorusu tě po snědení náhodně teleportuje. Upečené ovoce (&ePopped Chorus Fruit&r) je surovina na purpurové bloky."]),
        Q("eo_tooth", "Zub endermana", dep=["intro"], items=[("endermanoverhaul:enderman_tooth", 2)], xp=30, d=[
            "Mod &bEnderman Overhaul&r dal každému biomu vlastní druh endermana. Endermani v Endu mohou upustit zub (&eEnderman Tooth&r).",
            "Ze 2 zubů a klacku vyrobíš zkažený meč (&eCorrupted Blade&r). Zasažené nepřátele náhodně teleportuje."]),
        Q("eo_pearl", "Prastará perla", dep=["outer"], items=[("endermanoverhaul:ancient_pearl", 1)], xp=40, optional=True, d=[
            "Endermani z ostrovů Endu mohou upustit prastarou perlu (&eAncient Pearl&r).",
            "Když ji hodíš, vyvolá přátelského endermana, který za tebe bojuje. Shift + pravé tlačítko na něj ti perlu vrátí.",
            "Jiné druhy endermanů v Overworldu a Netheru pouštějí jiné perly. Přečti si jejich popis v JEI."]),

        # ---------- Pokročilý: města ----------
        Q("end_city", "Město v Endu", dep=["outer"], tasks=[structure("minecraft:end_city")], icon="minecraft:purpur_block", xp=60,
          shape="hexagon", size=1.5, s=POK, d=[
            "Teď tě čeká první velký poklad. Města v Endu (&eEnd City&r) jsou vysoké purpurové věže s truhlami plnými diamantové a železné výbavy.",
            "Hlídají je shulkeři – schovávají se ve schránkách a střílí střely, po kterých levituješ.",
            "U některých měst kotví loď. Na ní visí krovky."]),
        Q("levitate", "Vzhůru!", dep=["end_city"], tasks=[adv("minecraft:end/levitate")], icon="minecraft:shulker_shell", xp=20, optional=True, d=[
            "Nech se trefit střelou shulkera a vyleť do výšky 50 bloků.",
            "&cAž levitace skončí, spadneš. Měj u sebe vodu nebo krovky!&r"]),
        Q("shulker", "Schránky shulkerů", dep=["end_city"], items=[("minecraft:shulker_shell", 2)], xp=40, d=[
            "Ze shulkerů padají schránky (&eShulker Shell&r). 2 schránky a truhla dají shulkerovou krabici (&eShulker Box&r).",
            "Shulkerová krabice si po rozbití nechá všechny věci uvnitř. Můžeš ji nosit v inventáři i s obsahem."]),

        # ---------- Nullscape a stavby ----------
        Q("nullscape", "Pustina", dep=["outer"], tasks=[adv("nullscape:root")], icon="minecraft:obsidian", xp=30, d=[
            "Mod &bNullscape&r přetvořil vnější ostrovy na obří skály, krystalové vrcholy a stínové pustiny.",
            "Quest se splní, až vstoupíš do kteréhokoli jeho biomu. Mezi skalami se snadno ztratíš – měj u sebe souřadnice brány."]),
        Q("mes", "Strážní věž", dep=["outer"], tasks=[structure("mes:enderwatch_tower")], icon="minecraft:end_stone_bricks", xp=30, optional=True, d=[
            "Mod &bMoog's End Structures&r přidává do Endu přes dvacet staveb: věže, zahrady, zříceniny i vesmírné lodě.",
            "Najdi strážní věž (&eEnderwatch Tower&r)."]),
        Q("medievalend", "Středověký End", dep=["outer"], tasks=[structure("medievalend:house")], icon="minecraft:purpur_pillar", xp=30, optional=True, d=[
            "Mod &bMedieval Buildings End Edition&r staví v Endu středověké domy, svatyně, pyramidy, lodě a hrady.",
            "Najdi jeden z jeho domů."]),

        # ---------- Unusual End ----------
        Q("ue_gloop", "Gloopstonové kraje", dep=["outer"], tasks=[biome("unusualend:gloopstone_lands")], icon="unusualend:gloopstone", xp=30, d=[
            "Biom &eGloopstone Highlands&r z modu &bUnusual End&r je plný zeleného gloopstonu.",
            "Roste tu lesklý krystal a v hloubce prismalit. &cPozor na tvora &eEnder Trapper&c, který se schovává v kamení.&r"]),
        Q("ue_reef", "Zkřivený útes", dep=["outer"], tasks=[biome("unusualend:warped_reef")], icon="unusualend:warped_moss", xp=30, d=[
            "Biom &eWarped Reef&r jsou zelené ostrovy s vodou a zvláštními rybami. Žije tu ryba &eBolok&r, která umí proměňovat věci.",
            "Na útesu najdeš zkřivené lodě a stanice s truhlami. Ve vodě se dá i rybařit."]),
        Q("citrine", "Citrín", dep=["ue_reef"], items=[("unusualend:citrine_chunk", 2)], xp=30, d=[
            "Kousek citrínu (&eCitrine Chunk&r) získáš z citrínových shluků, rybařením v &eWarped Reef&r nebo z truhel na lodích.",
            "Z citrínu a provázků vyrobíš citrínový amulet."]),
        Q("prismalite", "Prismalit", dep=["ue_gloop"], items=[("unusualend:prismalite_gem", 1)], xp=40, d=[
            "Prismalitové střepy (&ePrismalite Shard&r) najdeš v hlubinách &eGloopstone Highlands&r, v urnách a truhlách.",
            "9 střepů dá prismalitový drahokam (&ePrismalite Gem&r)."]),
        Q("scrap", "Přízračný šrot", dep=["outer"], items=[("unusualend:enderling_scrap", 1)], xp=30, d=[
            "Přízračný šrot (&eSpectral Scrap&r) padá z nemrtvých enderlingů (&eUndead Enderling&r). Najdeš ho i v truhlách v domech a lodích.",
            "Je to poslední surovina, kterou potřebuješ na perleťový ingot."]),
        Q("pearlescent", "Perleťový ingot", dep=["citrine", "prismalite", "scrap", "nether_end:crystal"], items=[("unusualend:pearlescent_ingot", 1)], xp=100,
          shape="hexagon", size=1.5, s=EXP, d=[
            "Teď spojíš všechno, co jsi v Endu nasbíral. Perleťový ingot (&ePearlescent Ingot&r) je nejlepší kov z &bUnusual End&r.",
            "Recept: železný ingot, lesklý krystal, kousek citrínu, prismalitový drahokam a přízračný šrot.",
            "Z ingotů se vyrábí perleťová výbava a perleťový infuzér, který dává silné efekty."]),
        Q("golem_tower", "Prastará věž", dep=["outer"], tasks=[structure("unusualend:ancient_end_tower")], icon="unusualend:ancient_encased_end_stone", xp=40, d=[
            "Prastará věž (&eAncient End Tower&r) je pozůstatek dávných obyvatel Endu.",
            "Uvnitř stojí oltář golema (&eGolem Altar&r). Probudíš ho lahví dračího dechu (&eDragon's Breath&r)."]),
        Q("golem", "Golem z kamene Endu", dep=["golem_tower", "nether_end:dragon"], tasks=[kill("unusualend:endstone_golem")], icon="unusualend:golem_altar", xp=200, d=[
            "Použij na oltář golema lahev dračího dechu. Probudí se obří golem z kamene Endu (&eEndstone Golem&r).",
            "Je to boss. Přijď s nejlepší zbraní, zbrojí a dostatkem léčení."]),

        # ---------- Expert: drak znovu ----------
        Q("respawn", "Návrat draka", dep=["intro"], tasks=[adv("minecraft:end/respawn_dragon")], icon="minecraft:end_crystal", xp=100, optional=True, d=[
            "Draka můžeš vyvolat znovu. Polož 4 krystaly Endu (&eEnd Crystal&r) na okraje portálu uprostřed ostrova, na každou stranu jeden.",
            "Každý nový drak dá hodně zkušeností a otevře další bránu na vnější ostrovy."]),
        Q("egg", "Dračí vejce", dep=["intro"], tasks=[adv("minecraft:end/dragon_egg")], icon="minecraft:dragon_egg", xp=60, optional=True, d=[
            "Po prvním drakovi se na portálu objeví dračí vejce (&eDragon Egg&r). Když na něj klikneš, teleportuje se pryč.",
            "Vezmeš ho tak, že pod něj dáš pochodeň a vejce nad ní rozbiješ. Spadne na pochodeň a vypadne jako předmět."]),
    ],
)

# =====================================================================
#  AETHER
# =====================================================================
AETHER = dict(
    key="aether", group="explore", title="Aether",
    subtitle="Nebeská dimenze", icon="aether:golden_parachute",
    quests=[
        Q("intro", "Nebe nad hlavou", tasks=[auto()], icon="aether:aether_portal_frame", xp=10, d=[
            "&bThe Aether&r je nebeská dimenze plovoucích ostrovů. Má vlastní dřevo, kámen, rudy, zvířata a tři dungeony s bossy.",
            "V kapitole projdeš celý postup: od prvních nástrojů přes bronzový, stříbrný a zlatý dungeon až po nejlepší výbavu.",
            "Po ní můžeš pokračovat kapitolou &bDeep Aether&r."]),

        # ---------- Začátečník ----------
        Q("portal", "Portál do nebe", dep=["intro"], items=[("minecraft:glowstone", 4)], xp=15, d=[
            "Portál do Aetheru postavíš jako portál do Netheru, jen místo obsidiánu použiješ bloky světlitu (&eGlowstone&r).",
            "Rám je nejmenší 4 bloky široký a 5 vysoký. Na zapálení nalij dovnitř vodu z kbelíku.",
            "Světlit získáš v Netheru – visí ze stropu. Potřebuješ 10 bloků (rohy rámu nejsou nutné)."]),
        Q("aether", "Vstup do Aetheru", dep=["portal"], tasks=[dim("aether:the_aether")], icon="aether:aether_portal_frame", xp=40,
          shape="hexagon", size=1.5, s=ZAC, d=[
            "Jsi na plovoucích ostrovech. Dokud neporazíš posledního bosse (ducha slunce), je tu pořád den.",
            "&cKdyž spadneš z ostrova, propadneš se zpátky do Overworldu – a dopadneš z velké výšky.&r Padák (quest níže) tě zachrání.",
            "Nástroje z Aetheru těží bloky Aetheru rychleji než obyčejné nástroje. Začni tedy znovu od dřeva."]),
        Q("skyroot", "Nebeské dřevo a kámen", dep=["aether"], items=[("aether:skyroot_log", 8), ("aether:holystone", 16)], xp=20, d=[
            "Nebeský kořen (&eSkyroot Log&r) je zdejší dřevo. Svatý kámen (&eHolystone&r) je zdejší kámen.",
            "Z prken vyrobíš nebeské klacky (&eSkyroot Stick&r). Ty potřebuješ na všechny nástroje z Aetheru."]),
        Q("skyroot_tools", "Nástroje z kořene", dep=["skyroot"], items=[("aether:skyroot_pickaxe", 1)], xp=15, d=[
            "Nástroje z nebeského dřeva (&eSkyroot Pickaxe&r) jsou nejslabší, ale mají bonus: ze svatého kamene a ambrosiové rudy padá dvojnásobek.",
            "Hodí se i později na těžbu ambrosia."]),
        Q("holystone_tools", "Kamenné nástroje", dep=["skyroot"], items=[("aether:holystone_pickaxe", 1)], xp=15, d=[
            "Krumpáč ze svatého kamene (&eHolystone Pickaxe&r) vytěží zanitovou rudu.",
            "Občas při těžbě sám vyhodí střípek ambrosia."]),
        Q("ambrosium", "Ambrosium", dep=["skyroot"], items=[("aether:ambrosium_shard", 4)], xp=20, d=[
            "Střípky ambrosia (&eAmbrosium Shard&r) jsou zdejší uhlí. Ruda je ve svatém kameni a je nejčastější.",
            "Pohání oltář. Když ho sníš, vyléčí ti půl srdce."]),
        Q("torch", "Ambrosiová pochodeň", dep=["ambrosium"], items=[("aether:ambrosium_torch", 4)], xp=10, d=[
            "Střípek ambrosia nad nebeským klackem dá 4 ambrosiové pochodně (&eAmbrosium Torch&r).",
            "Svítí stejně jako běžná pochodeň. Slouží i jako palivo do inkubátoru pro moa."]),
        Q("zanite", "Zanit", dep=["holystone_tools"], items=[("aether:zanite_gemstone", 8)], xp=30, d=[
            "Zanit (&eZanite Gemstone&r) je zdejší železo. Fialová ruda je ve svatém kameni.",
            "Zanitové nástroje jsou tím rychlejší, čím víc jsou opotřebené. Po opravě jsou zase pomalé."]),
        Q("altar", "Oltář a mrazák", dep=["ambrosium", "zanite"], items=[("aether:altar", 1), ("aether:freezer", 1)], xp=30, d=[
            "Oltář (&eAltar&r) = 8 svatých kamenů a zanit. Funguje jako pec, ale místo pálení věci očaruje. Palivo je ambrosium.",
            "Mrazák (&eFreezer&r) = svaté kameny, ledový kámen (&eIcestone&r) a prkna. Věci zmrazí. Palivo je ledový kámen.",
            "Oltářem také opravíš poškozené nástroje a zbroj."]),
        Q("parachute", "Padák", dep=["aether"], items=[("aether:cold_parachute", 1)], xp=20, d=[
            "Studený padák (&eCold Parachute&r) vyrobíš ze 4 studených mraků (&eCold Aercloud&r). Jsou to bílé mraky, které se vznášejí mezi ostrovy.",
            "Padák se sám otevře, když spadneš z ostrova. Studený padák vydrží jen jedno použití. Zlatý padák (&eGolden Parachute&r) ze zlatých mraků vydrží 20 použití."]),
        Q("enchanting", "První očarování", dep=["altar"], items=[("aether:enchanted_berry", 2)], xp=20, d=[
            "Modré bobule (&eBlue Berry&r) rostou na keřích po celém Aetheru. Dej je do oltáře.",
            "Vznikne očarovaná bobule (&eEnchanted Berry&r), která zasytí mnohem víc.",
            "Stejně v oltáři vyrobíš léčivý kámen ze svatého kamene nebo sklo z rychlopísku (&eQuicksoil&r)."]),

        # ---------- Moa ----------
        Q("moa", "Inkubátor", dep=["altar", "torch"], items=[("aether:incubator", 1)], xp=40, d=[
            "Moa jsou velcí ptáci, na kterých můžeš létat. Inkubátor (&eIncubator&r) = 8 svatých kamenů a ambrosiová pochodeň.",
            "Do inkubátoru dej vejce moa a jako palivo ambrosiové pochodně. Líhnutí chvíli trvá."]),
        Q("moa_egg", "Vejce moa", dep=["moa"], items=[("aether:blue_moa_egg", 1)], xp=30, d=[
            "Divoké moa občas snesou vejce na zem. Vejce najdeš i v truhlách stříbrného dungeonu.",
            "Modrá moa (&eBlue Moa Egg&r) je nejběžnější a ve vzduchu skočí 3×. Bílá skočí 4×, černá dokonce 8×.",
            "Mládě krm okvětními lístky (&eAechor Petal&r) z nepřátelské rostliny &eAechor Plant&r. Moa, kterou vychováš z vejce, můžeš po dospění osedlat a létat na ní."]),

        # ---------- Pokročilý: bronzový dungeon ----------
        Q("zanite_armor", "Zanitová zbroj", dep=["zanite"], items=[("aether:zanite_chestplate", 1)], xp=30, d=[
            "Zanitová zbroj chrání stejně jako železná. Než půjdeš do dungeonu, vyrob si celou sadu.",
            "Do sady patří i zanitové rukavice (&eZanite Gloves&r). Nosí se ve slotu na doplňky."]),
        Q("ring", "Doplňky", dep=["zanite"], items=[("aether:zanite_ring", 1)], xp=20, d=[
            "Aether má sloty na doplňky: prsteny, přívěsky, rukavice a pláště. Otevřeš je tlačítkem v inventáři.",
            "Zanitový prsten (&eZanite Ring&r) zrychlí těžbu, ale brzy se opotřebí.",
            "&aTip:&r železný nebo zlatý prsten zmraz v mrazáku. Vznikne ledový prsten, se kterým zmrazíš vodu a lávu, po které jdeš."]),
        Q("bronze_find", "Bronzový dungeon", dep=["zanite_armor"], tasks=[structure("aether:bronze_dungeon")], icon="aether:carved_stone", xp=40,
          shape="hexagon", size=1.5, s=POK, d=[
            "Teď už nejde jen o suroviny – čekají tě dungeony. První je bronzový. Je schovaný uvnitř ostrovů a je postavený z vytesaného kamene (&eCarved Stone&r).",
            "Uvnitř jsou strážci (&eSentry&r) a truhly, které můžou být mimikové (&eChest Mimic&r) – ožijí a zaútočí."]),
        Q("bronze", "Slider", dep=["bronze_find"], items=[("aether:bronze_dungeon_key", 1)], xp=80, d=[
            "Boss bronzového dungeonu je &eSlider&r – obří kamenný blok, který po místnosti klouže a drtí tě.",
            "&cZraníš ho jen krumpáčem!&r Uhýbej mu z cesty.",
            "Po smrti upustí bronzový klíč (&eBronze Key&r). Jím otevřeš truhlu s pokladem za bossem."]),
        Q("bronze_loot", "Poklad Slidera", dep=["bronze"], tasks=[adv("aether:lance_loot")], icon="aether:valkyrie_lance", xp=40, optional=True, d=[
            "V pokladu může být Valkýří kopí (&eValkyrie Lance&r), kladivo (&eHammer of Kingbdogz&r) nebo strážní boty (&eSentry Boots&r).",
            "Kopí má dlouhý dosah a skvěle se hodí na další dungeon. Quest se splní, až kopí získáš."]),

        # ---------- Gravitit ----------
        Q("gravitite", "Gravitit", dep=["altar"], items=[("aether:enchanted_gravitite", 4)], xp=60, d=[
            "Gravititová ruda (&eGravitite Ore&r) je nejvzácnější ruda. Vytěžíš ji zanitovým krumpáčem. Když nad ní nic není, vyletí nahoru – padá vzhůru!",
            "Rudu dej do oltáře. Vznikne očarovaný gravitit (&eEnchanted Gravitite&r) a z něj vyrobíš výbavu.",
            "&aTip:&r rudu těž zespodu nebo nad ni dej blok, ať ti neuletí."]),
        Q("gravitite_tools", "Gravititové nástroje", dep=["gravitite"], items=[("aether:gravitite_pickaxe", 1)], xp=40, d=[
            "Gravititový krumpáč (&eGravitite Pickaxe&r) vytěží každou rudu.",
            "Pravým tlačítkem na blok ho nechá vyletět do vzduchu. Tak snadno přesuneš i velké kusy ostrova."]),
        Q("gravitite_armor", "Vzdoruj gravitaci", dep=["gravitite_tools"], tasks=[adv("aether:gravitite_armor")], icon="aether:gravitite_chestplate", xp=80, d=[
            "Vyrob celou gravititovou zbroj: helmu, hrudní plát, kalhoty, boty a rukavice (&eGravitite Gloves&r). Quest chce všech 5 kusů.",
            "S celou sadou skáčeš mnohem výš a nezraní tě pád."]),

        # ---------- Stříbrný dungeon ----------
        Q("silver_find", "Stříbrný dungeon", dep=["bronze"], tasks=[structure("aether:silver_dungeon")], icon="aether:angelic_stone", xp=60, d=[
            "Stříbrný dungeon je velký chrám z andělského kamene (&eAngelic Stone&r), který se vznáší nad ostrovy.",
            "Žijí v něm Valkýry (&eValkyrie&r). Bloky dungeonu nejdou rozbít, dokud neporazíš bosse."]),
        Q("medals", "Medaile vítězství", dep=["silver_find"], items=[("aether:victory_medal", 10)], xp=60, d=[
            "Každá poražená Valkýra upustí medaili vítězství (&eVictory Medal&r).",
            "Královna Valkýr s tebou bude bojovat, až jí přineseš 10 medailí.",
            "&aTip:&r Valkýry tvrdě bijí. Valkýří kopí z bronzového dungeonu má dlouhý dosah a hodí se na ně."]),
        Q("silver", "Královna Valkýr", dep=["medals"], items=[("aether:silver_dungeon_key", 1)], xp=100, d=[
            "Královna (&eValkyrie Queen&r) sedí na vrcholu dungeonu. Klikni na ni pravým tlačítkem a vyber souboj – musíš mít u sebe 10 medailí.",
            "Útočí zblízka a sesílá blesky. Po smrti ti dá stříbrný klíč (&eSilver Key&r) k pokladu.",
            "V pokladu bývá Valkýří zbroj, se kterou můžeš na chvíli létat, a kámen regenerace."]),

        # ---------- Expert: zlatý dungeon ----------
        Q("gold_find", "Zlatý dungeon", dep=["silver"], tasks=[structure("aether:gold_dungeon")], icon="aether:hellfire_stone", xp=80,
          shape="hexagon", size=1.5, s=EXP, d=[
            "Poslední zkouška Aetheru. Zlatý dungeon je ukrytý uvnitř velkého ostrova, kde rostou zlaté duby. Uvnitř je pekelný kámen (&eHellfire Stone&r).",
            "Dokud boss žije, je v Aetheru stále den a pekelný kámen nejde rozbít."]),
        Q("gold", "Duch slunce", dep=["gold_find"], items=[("aether:gold_dungeon_key", 1)], xp=150, d=[
            "Boss je duch slunce (&eSun Spirit&r). Střílí ohnivé a ledové krystaly a vyvolává ohnivé pomocníky.",
            "Udeř do ledového krystalu – odletí směrem, kam se díváš. Když ducha zasáhne, zmrazí ho. Útoč na něj, dokud je zmrazený.",
            "&cVezmi si lektvary ohnivzdornosti!&r Po smrti dá zlatý klíč (&eGold Key&r) a sluneční oltář, kterým ovládáš denní dobu."]),
        Q("phoenix", "Fénixova zbroj", dep=["gold"], tasks=[adv("aether:phoenix_armor")], icon="aether:phoenix_chestplate", xp=80, d=[
            "V pokladu zlatého dungeonu je fénixova zbroj (&ePhoenix Armor&r). Celá sada dá ohnivzdornost – můžeš plavat i v lávě.",
            "&cVe vodě se fénixova zbroj promění na obsidiánovou.&r Obsidiánová zbroj je ještě silnější než diamantová."]),
        Q("life_shard", "Střep života", dep=["gold"], items=[("aether:life_shard", 1)], xp=100, optional=True, d=[
            "Střep života (&eLife Shard&r) je vzácný poklad zlatého dungeonu.",
            "Když ho použiješ, dostaneš navždy jedno srdce navíc. Počet použitých střepů je omezený."]),

        # ---------- Deep Aether (původní quest) ----------
        Q("deep", "Deep Aether", dep=["zanite"], items=[("deep_aether:skyjade", 1)], xp=30, d=[
            "Mod &bDeep Aether&r přidává do Aetheru nové biomy, moby, materiály a dungeon s bossem.",
            "Nebeský jadeit (&eSkyjade Gemstone&r) je jeho první nový materiál. Rudu vytěžíš zanitovým krumpáčem a přetavíš v peci.",
            "Pokračuj kapitolou &bDeep Aether&r."]),
    ],
)

# =====================================================================
#  DEEP AETHER (nová kapitola)
# =====================================================================
DEEP_AETHER = dict(
    key="deep_aether", group="explore", title="Deep Aether",
    subtitle="Nové biomy a bouře nad Aetherem", icon="deep_aether:skyjade",
    quests=[
        Q("intro", "Hlubší Aether", dep=["aether:deep"], tasks=[auto()], icon="deep_aether:skyjade", xp=10, d=[
            "&bDeep Aether&r rozšiřuje Aether o nové biomy, stromy, jídlo, kombinátor, mosazný dungeon a bosse &eEye of the Storm&r.",
            "Navazuje na kapitolu &bAether&r. Nejlepší výbava odsud potřebuje i gravitit a poklad ze zlatého dungeonu."]),

        # ---------- Začátečník ----------
        Q("biomes", "Nové biomy", dep=["intro"], tasks=[biome("deep_aether:golden_heights")], icon="deep_aether:golden_heights_grass_block", xp=20,
          shape="hexagon", size=1.5, s=ZAC, d=[
            "Deep Aether přidává biomy jako zlaté výšiny (&eGolden Heights&r), zářící lesy (&eAerglow Forest&r) nebo jedovatou bažinu (&eYagroot Swamp&r).",
            "Najdi zlaté výšiny – ostrovy se zlatou trávou a zlatými květinami."]),
        Q("skyjade_tools", "Jadeitové nástroje", dep=["intro"], items=[("deep_aether:skyjade_pickaxe", 1)], xp=30, d=[
            "Jadeitový krumpáč (&eSkyjade Pickaxe&r) těží rychleji než diamantový. Čím víc je ale opotřebený, tím je pomalejší.",
            "Je to opak zanitu. Jadeitové nástroje si proto často opravuj na oltáři."]),
        Q("food", "Křepelka", dep=["intro"], items=[("deep_aether:raw_quail", 2)], xp=15, d=[
            "Křepelky (&eQuail&r) jsou zdejší slepice. Dávají syrové maso (&eRaw Quail&r) a snáší vejce.",
            "Ve vodě plavou zářící ryby (&eAerglow Fish&r)."]),
        Q("goldenleaf", "Zlatolisté bobule", dep=["intro"], items=[("deep_aether:goldenleaf_berries", 4)], xp=15, d=[
            "Zlatolisté bobule (&eGoldenleaf Berries&r) rostou na zlatých šlahounech (&eGolden Vines&r), které vyrůstají z rychlopísku (&eQuicksoil&r).",
            "Zmražené v mrazáku (&eFrozen Goldenleaf Berries&r) jsou surovina do kombinátoru."]),
        Q("combiner", "Kombinátor", dep=["skyjade_tools", "goldenleaf", "aether:altar"], items=[("deep_aether:combiner", 1)], xp=40, d=[
            "Kombinátor (&eCombiner&r) spojí 3 přísady v jeden předmět. Recept: nebeská prkna, svaté kameny, 3 jadeity a ambrosium.",
            "Základ každého receptu je zlatý jantar (&eGolden Amber&r) a zmražené zlatolisté bobule. Třetí přísada určuje výsledek.", "Zlatý jantar padá ze dřeva zlatých dubů, když ho kácíš zanitovou sekerou.",
            "Vyrobíš v něm třeba krmivo pro moa (&eMoa Fodder&r), které jim dá extra skoky nebo ohnivzdornost."]),
        Q("poison", "Fialová magie", dep=["intro"], tasks=[adv("deep_aether:transform_poison")], icon="deep_aether:poison_bucket", xp=30, optional=True, d=[
            "V jedovaté bažině (&eYagroot Swamp&r) je fialový jed. Když do něj hodíš některé předměty, promění se.",
            "Brambora zezelená na jedovatou a očarované věci z oltáře se vrátí do původní podoby. Všechny přeměny ukazuje JEI v kategorii &ePoison Conversion&r."]),

        # ---------- Pokročilý: mosazný dungeon ----------
        Q("brass_find", "Mosazný dungeon", dep=["combiner"], tasks=[structure("deep_aether:brass_dungeon")], icon="deep_aether:nimbus_stone", xp=60,
          shape="hexagon", size=1.5, s=POK, d=[
            "Po prvních krocích přichází dungeon. Mosazný dungeon (&eBrass Dungeon&r) je postavený z mrakového kamene (&eNimbus Stone&r) a vznáší se velmi vysoko v mracích.",
            "Hledej ho nad oblačnými biomy. Vezmi si padák a hodně bloků na stavění."]),
        Q("eots", "Oko bouře", dep=["brass_find"], tasks=[adv("deep_aether:brass_dungeon")], icon="deep_aether:brass_dungeon_key", xp=120, d=[
            "Boss mosazného dungeonu je &eEye of the Storm&r – dlouhý bouřkový had z větru.",
            "Fouká silný vítr. Když se přiblíží, udeř ho.",
            "Po smrti upustí mosazný klíč (&eBrass Key&r) k pokladu. V něm bývá bouřkový meč, bouřkový luk nebo plášť z mraků (&eCloud Cape&r), který dá dvojitý skok."]),
        Q("stormforged", "Bouřková zbroj", dep=["eots"], items=[("deep_aether:stormforged_chestplate", 1)], xp=80, optional=True, d=[
            "V pokladu mosazného dungeonu můžeš najít kus bouřkové zbroje (&eStormforged&r) nebo kovářskou šablonu na ni.",
            "Šablona + jadeitová zbroj + bouřková deska (&eSquall Plate&r) na kovářském stole = bouřková zbroj. Skoro tě nejde odhodit a odhazuje útočníky."]),

        # ---------- Expert: stratus ----------
        Q("sterling", "Stříbrný mrak", dep=["brass_find"], items=[("deep_aether:sterling_aercloud", 5)], xp=40, d=[
            "Stříbrný mrak (&eSterling Aercloud&r) se vznáší úplně nahoře, kam se těžko dostaneš.",
            "&cKdyž na něj stoupneš, zasáhne ho blesk a změní ho na obyčejný studený mrak.&r Těž ho zespodu nebo z boku."]),
        Q("chromatic", "Duhový mrak", dep=["sterling"], items=[("deep_aether:chromatic_aercloud", 5)], xp=50, d=[
            "Stříbrný mrak očaruj v oltáři. Vznikne duhový mrak (&eChromatic Aercloud&r).",
            "Očarování trvá dlouho a spotřebuje hodně ambrosia. Připrav si zásobu."]),
        Q("stratus_ingot", "Stratusový ingot", dep=["chromatic", "aether:gravitite"], items=[("deep_aether:stratus_ingot", 1)], xp=80,
          shape="hexagon", size=1.5, s=EXP, d=[
            "Teď vyrobíš nejsilnější kov nebe. Recept: 5 duhových mraků, očarovaný gravitit, zanit, ambrosium a jadeit.",
            "Stratusovým ingotem vylepšíš gravititovou výbavu na kovářském stole."]),
        Q("stratus_template", "Stratusová šablona", dep=["aether:gold"], items=[("deep_aether:stratus_smithing_template", 1)], xp=40, d=[
            "Kovářská šablona na stratus (&eStratus Smithing Template&r) je v pokladu zlatého dungeonu.",
            "Při vylepšení se spotřebuje. Kopii vyrobíš ze šablony, 7 diamantů (nebo očarovaného gravititu) a svatého kamene – dostaneš 2 šablony."]),
        Q("stratus_armor", "Stratusová zbroj", dep=["stratus_ingot", "stratus_template", "aether:gravitite_armor"], tasks=[adv("deep_aether:stratus_armor")], icon="deep_aether:stratus_chestplate", xp=150, d=[
            "Šablona + kus gravititové zbroje + stratusový ingot = kus stratusové zbroje. Vyrob helmu, hrudní plát, kalhoty a boty.",
            "Celá sada dá vysoký skok a výpad do strany (&eStratus Dash&r) na vlastní klávese. Klávesu si nastav v ovládání."]),
        Q("explorer", "Průzkumník Aetheru", dep=["biomes"], tasks=[adv("deep_aether:explore_aether")], icon="aether:golden_parachute", xp=100, optional=True, d=[
            "Navštiv všechny biomy Aetheru: čtyři nebeské lesy a louky z Aetheru i nové biomy z Deep Aetheru.",
            "Výzva pro trpělivé průzkumníky."]),
        Q("champion", "Šampion Aetheru", dep=["eots", "aether:gold"], tasks=[adv("deep_aether:aether_champion")], icon="deep_aether:medal_of_honor", xp=200, optional=True, d=[
            "Poraz všechny bosse Aetheru tak, že tě ani jednou nezasáhnou.",
            "Za bezchybné vítězství padají zvláštní odměny – třeba &eMedal of Honor&r od Královny Valkýr nebo &eSun Core&r od ducha slunce."]),
    ],
)

# =====================================================================
#  TWILIGHT FOREST – postup bossů (původní kapitola)
# =====================================================================
TWILIGHT = dict(
    key="twilight", group="explore", title="Soumračný les",
    subtitle="Svět plný bossů", icon="twilightforest:naga_trophy",
    quests=[
        Q("intro", "Soumračný les", tasks=[auto()], icon="twilightforest:twilight_oak_sapling", xp=10, d=[
            "&bThe Twilight Forest&r je dimenze věčného soumraku plná lesů, staveb a bossů.",
            "Bossové jdou v pevném pořadí. Oblasti dál v lese jsou prokleté (tma, mráz, oheň, kyselý déšť), dokud neporazíš správného bosse.",
            "Co máš splnit, aby kletba zmizela, ukážou pokroky (&eAdvancements&r) Twilight Forest."]),
        Q("portal", "Portál", dep=["intro"], items=[("minecraft:diamond", 1)], xp=15, d=[
            "Vykopej jámu 2 × 2 a naplň ji vodou. Kolem jámy musí být bloky hlíny nebo trávy. Na každý z nich zasaď květinu nebo trávu.",
            "Do vody hoď diamant (klávesa Q). Udeří blesk a voda se změní na portál.",
            "&cBlesk může zapálit okolí – nestav portál vedle dřevěného domu.&r"]),
        Q("enter", "Do soumraku", dep=["portal"], tasks=[dim("twilightforest:twilight_forest")], icon="twilightforest:twilight_oak_log", xp=40,
          shape="hexagon", size=1.5, s=ZAC, d=[
            "Jsi v Soumračném lese. Je tu pořád soumrak a hustý les plný zvířat i příšer.",
            "Postup: Naga → Lich → potom tři větve (bažina, temný les, sníh) → vysočina.",
            "Kapitola &bSoumračný les: výbava&r ukazuje zbroj, nástroje a kouzelné stromy z tohoto světa."]),
        Q("magic_map", "Kouzelná mapa", dep=["enter"], items=[("twilightforest:magic_map", 1)], xp=30, d=[
            "Kouzelná mapa ukáže okolí i stavby bossů. Nejdřív vyrob zaměřovač (&eMagic Map Focus&r): havraní pírko, svítící bobule (&eTorchberries&r) a světlitový prach.",
            "Havrani (&eRaven&r) žijí v lesích. Svítící bobule visí z kořenů v jeskyních.",
            "Zaměřovač obklop 8 papíry. Prázdnou mapu pak použij pravým tlačítkem."]),
        Q("charm", "Talisman života", dep=["enter"], items=[("twilightforest:charm_of_life_1", 1)], xp=40, d=[
            "Talisman života (&eCharm of Life I&r) tě jednou zachrání před smrtí, jako totem. Stačí ho mít v inventáři.",
            "Najdeš ho v truhlách – třeba v dutých stromech nebo ve skrýších pod padlými kmeny.",
            "&aTip:&r 4 talismany I dají talisman II, který tě zachrání s víc životy."]),
        Q("ram", "Úlohový beran", dep=["enter"], items=[("twilightforest:quest_ram_trophy", 1)], xp=80, optional=True, d=[
            "V háji úloh (&eQuest Grove&r) stojí obří beran (&eQuesting Ram&r). Chce sníst vlnu všech 16 barev.",
            "Dej mu postupně jednu vlnu od každé barvy. Odmění tě bloky drahých kovů a trofejí."]),

        # ---------- Naga a Lich ----------
        Q("naga_court", "Nádvoří nagy", dep=["enter"], tasks=[structure("twilightforest:naga_courtyard")], icon="twilightforest:nagastone_head", xp=30, d=[
            "Nádvoří nagy (&eNaga Courtyard&r) je ohrazená zahrada z kamene nagy (&eNagastone&r). Najdeš ho v běžném lese.",
            "Uvnitř čeká první boss. Kouzelná mapa ti nádvoří pomůže najít."]),
        Q("naga", "Naga", dep=["naga_court"], items=[("twilightforest:naga_trophy", 1)], xp=80, d=[
            "Naga je obří had. Rychle se plazí a vrhá se na tebe.",
            "Po smrti upustí šupiny nagy (&eNaga Scale&r) a trofej. Šupina zlomí kletbu na věži Licha."]),
        Q("lich_tower", "Věž Licha", dep=["naga"], tasks=[structure("twilightforest:lich_tower")], icon="twilightforest:twisted_stone", xp=30, d=[
            "Věž Licha (&eLich Tower&r) je vysoká věž se špičatou střechou. Dokud neporazíš nagu, chrání ji kletba.",
            "Ve věži jsou knihovny a nepřátelé. Lich čeká v nejvyšším patře."]),
        Q("lich", "Lich", dep=["lich_tower"], items=[("twilightforest:lich_trophy", 1)], xp=100, d=[
            "Lich je mocný čaroděj. Chrání ho štít, vyvolává stínové kopie a pomocníky.",
            "Jeho kouzelné střely můžeš odrazit úderem zpátky na něj.",
            "Upustí jedno ze 4 žezel. Jeho porážka zruší kletbu bažiny, temného lesa a zasněženého lesa."]),
        Q("uncrafting", "Rozebírací stůl", dep=["mino"], items=[("twilightforest:uncrafting_table", 1)], xp=40, d=[
            "Rozebírací stůl (&eUncrafting Table&r) rozloží vyrobený předmět zpátky na suroviny. Stojí to zkušenosti.",
            "Recept: 8 pracovních stolů a zaměřovač bludiště (&eMaze Map Focus&r). Ten padá z minotaurů v labyrintu."]),

        # ---------- Větev bažina: Minoshroom → Hydra ----------
        Q("swamp", "Bažina", dep=["lich"], tasks=[biome("twilightforest:swamp")], icon="twilightforest:huge_lily_pad", xp=30,
          shape="hexagon", size=1.5, s=POK, d=[
            "Po Lichovi se otevírají tři větve. Můžeš je dělat v libovolném pořadí.",
            "První je bažina (&eTwilight Swamp&r). Dokud neporazíš Licha, trápí tě tu hlad a roje komárů.",
            "Pod bažinou je labyrint s minotaury."]),
        Q("labyrinth", "Labyrint", dep=["swamp"], tasks=[structure("twilightforest:labyrinth")], icon="twilightforest:mazestone_brick", xp=40, d=[
            "Labyrint (&eMinotaur Labyrinth&r) je bludiště z bludištního kamene pod bažinou.",
            "Minotauři v něm pouštějí zaměřovač bludiště. Z něj vyrobíš mapu bludiště, rozebírací stůl a později mapu rud."]),
        Q("mino", "Minoshroom", dep=["labyrinth"], items=[("twilightforest:minoshroom_trophy", 1)], xp=100, d=[
            "&eMinoshroom&r je houbový minotaur v nejhlubší části labyrintu. Útočí obří sekerou.",
            "Upustí stroganov (&eMeef Stroganoff&r), trofej a diamantovou minotauří sekeru."]),
        Q("stroganoff", "Mocný stroganov", dep=["mino"], tasks=[adv("twilightforest:progress_labyrinth")], icon="twilightforest:meef_stroganoff", xp=40, d=[
            "Sněz stroganov od Minoshrooma. Tvoje tělo si zvykne na žár ohnivé bažiny.",
            "Bez toho tě v ohnivé bažině pálí oheň a nedá se tam přežít."]),
        Q("fire_swamp", "Ohnivá bažina", dep=["stroganoff"], tasks=[biome("twilightforest:fire_swamp")], icon="twilightforest:fire_jet", xp=30, d=[
            "Ohnivá bažina (&eFire Swamp&r) je plná lávy a ohnivých trysek. Uprostřed je doupě hydry.",
            "Vezmi si lektvary ohnivzdornosti a hodně jídla."]),
        Q("hydra", "Hydra", dep=["fire_swamp"], items=[("twilightforest:hydra_trophy", 1)], xp=150, d=[
            "Hydra je obří vícehlavý drak. Plive oheň, hlavami kouše a zničené hlavy jí po chvíli dorostou.",
            "Drž se v pohybu a nestůj v plamenech.",
            "Upustí ohnivou krev (&eFiery Blood&r), kotletu hydry a trofej."]),
        Q("fiery", "Ohnivý ingot", dep=["hydra"], items=[("twilightforest:fiery_ingot", 2)], xp=40, d=[
            "Ohnivý ingot (&eFiery Ingot&r) = železný ingot + ohnivá krev (od hydry) nebo ohnivé slzy (od Ur-Ghasta).",
            "Z ohnivých ingotů je ohnivá zbroj, meč a krumpáč, který rovnou taví rudy."]),

        # ---------- Větev temný les: Knight Phantoms → Ur-Ghast ----------
        Q("dark_forest", "Temný les", dep=["lich"], tasks=[biome("twilightforest:dark_forest")], icon="twilightforest:darkwood_sapling", xp=30, d=[
            "Druhá větev je temný les (&eDark Forest&r) s hustými stromy. Dokud neporazíš Licha, oslepuje tě tma.",
            "Pod lesem je rytířská pevnost (&eKnight Stronghold&r). Na povrchu nad ní je zřícenina s podstavcem."]),
        Q("pedestal", "Podstavec trofejí", dep=["dark_forest"], tasks=[adv("twilightforest:progress_trophy_pedestal")], icon="twilightforest:trophy_pedestal", xp=40, d=[
            "Ve zřícenině nad rytířskou pevností stojí podstavec na trofej (&eTrophy Pedestal&r).",
            "Polož na něj trofej bosse, třeba nagy nebo Licha. Zmizí štíty, které zavírají vchod do pevnosti.",
            "Podstavec reaguje jen na hráče, kteří už porazili Licha."]),
        Q("knight", "Rytířští fantomové", dep=["pedestal"], items=[("twilightforest:knight_phantom_trophy", 1)], xp=120, d=[
            "V pevnosti žijí skřetí rytíři (&eGoblin Knight&r). Z jejich brnění padají úlomky (&eArmor Shard&r).",
            "V hrobce na konci pevnosti se probudí rytířští fantomové (&eKnight Phantom&r). Je jich víc a musíš porazit všechny.",
            "Po posledním z nich zůstane trofej. Teprve potom tě pustí věž uprostřed temného lesa."]),
        Q("knightmetal", "Rytířský kov", dep=["knight"], items=[("twilightforest:knightmetal_ingot", 4)], xp=40, d=[
            "9 úlomků brnění dá shluk úlomků (&eArmor Shard Cluster&r). Shluk přetav v peci na rytířský kov (&eKnightmetal Ingot&r).",
            "Z rytířského kovu je silná zbroj, nástroje a štít."]),
        Q("dark_tower", "Temná věž", dep=["knight"], tasks=[structure("twilightforest:dark_tower")], icon="twilightforest:towerwood", xp=40, d=[
            "Uprostřed temného lesa stojí temná věž (&eDark Tower&r) z věžového dřeva.",
            "Uvnitř jsou mizející bloky, zamčené dveře a karminitoví golemové. Klíč od zamčených dveří (&eTower Key&r) najdeš v truhlách věže."]),
        Q("ghast_trap", "Past na ghasta", dep=["dark_tower"], tasks=[adv("twilightforest:ghast_trap")], icon="twilightforest:ghast_trap", xp=50, d=[
            "Na vrcholu věže létá &eUr-Ghast&r. Sám dolů nesleze.",
            "V místnosti pod ním jsou pasti na ghasty (&eGhast Trap&r). Zabij v jejich blízkosti malé karminitové ghasty a past se nabije.",
            "Nabitou past aktivuj redstonovým signálem (třeba páčkou). Past stáhne Ur-Ghasta dolů."]),
        Q("ghast", "Ur-Ghast", dep=["ghast_trap"], items=[("twilightforest:ur_ghast_trophy", 1)], xp=150, d=[
            "Ur-Ghast je obří ghast. Střílí ohnivé koule a pláče ohnivými slzami.",
            "Bij ho, dokud ho past drží u země. Upustí ohnivé slzy (&eFiery Tears&r), karminit a trofej."]),
        Q("carminite", "Karminit", dep=["ghast"], items=[("twilightforest:carminite", 4)], xp=30, d=[
            "Karminit (&eCarminite&r) padá z Ur-Ghasta. Vyrobíš ho i z esence vrtáků (&eBorer Essence&r), rudého prachu a slzy ghasta.",
            "Z karminitu jsou zvláštní bloky: mizející a znovu se objevující bloky, stavitel a reaktor."]),

        # ---------- Větev sníh: Alpha Yeti → Snow Queen ----------
        Q("snowy", "Zasněžený les", dep=["lich"], tasks=[biome("twilightforest:snowy_forest")], icon="twilightforest:arctic_fur", xp=30, d=[
            "Třetí větev je zasněžený les (&eSnowy Forest&r). Dokud neporazíš Licha, zmrzneš tu.",
            "Žijí tu yetiové. Jejich vůdce sedí v jeskyni (&eYeti Cave&r)."]),
        Q("yeti", "Alfa Yeti", dep=["snowy"], items=[("twilightforest:alpha_yeti_trophy", 1)], xp=150, d=[
            "&eAlpha Yeti&r je vůdce yetiů. Je silný a hází po tobě led.",
            "Upustí srst alfa yetiho (&eAlpha Yeti Fur&r), ledové bomby a trofej. Se srstí v inventáři tě už nezmrazí ledovec."]),
        Q("glacier", "Ledovec", dep=["yeti"], tasks=[biome("twilightforest:glacier")], icon="minecraft:packed_ice", xp=30, d=[
            "Ledovec (&eTwilight Glacier&r) je zamrzlá krajina za zasněženým lesem. Stojí na něm polární palác (&eAurora Palace&r).",
            "Palác je vysoký a hlídaný. Vezmi si hodně bloků a jídla."]),
        Q("queen", "Sněhová královna", dep=["glacier"], items=[("twilightforest:snow_queen_trophy", 1)], xp=200, d=[
            "Sněhová královna (&eSnow Queen&r) čeká na vrcholu polárního paláce.",
            "Upustí trojitý luk (&eTri-Bow&r) nebo luk naváděných šípů (&eSeeker Bow&r) a trofej."]),

        # ---------- Expert: vysočina ----------
        Q("merge", "Velké finále", dep=["hydra", "ghast", "queen"], tasks=[adv("twilightforest:progress_merge")], icon="twilightforest:snow_queen_trophy", xp=150,
          shape="hexagon", size=1.5, s=EXP, d=[
            "Teď přichází nejtěžší část lesa. Porážka hydry, Ur-Ghasta a Sněhové královny zruší kyselý déšť nad vysočinou.",
            "Vysočina (&eTwilight Highlands&r) jsou vysoké hory na okraji lesa."]),
        Q("troll", "Trollí jeskyně", dep=["merge"], tasks=[adv("twilightforest:troll")], icon="twilightforest:trollsteinn", xp=60, d=[
            "Pod vysočinou jsou trollí jeskyně (&eTroll Cave&r). Najdi trolla a zabij ho.",
            "Z trollů padají kouzelné fazole (&eMagic Beans&r)."]),
        Q("beanstalk", "Fazolový stonek", dep=["troll"], tasks=[adv("twilightforest:beanstalk")], icon="twilightforest:magic_beans", xp=60, d=[
            "V trollích jeskyních je zářící úrodná půda (&eUberous Soil&r). Zasaď do ní kouzelné fazole.",
            "Vyroste obří stonek až do mraků. Po něm vylez nahoru."]),
        Q("giants", "Obři v oblacích", dep=["beanstalk"], items=[("twilightforest:giant_pickaxe", 1)], xp=100, d=[
            "V mracích stojí dům obrů. Obří horník (&eGiant Miner&r) po smrti upustí obrův krumpáč (&eGiant's Pickaxe&r).",
            "Jen obrův krumpáč rozbije obří bloky, třeba obrovský obsidián (&eGiant Obsidian&r)."]),
        Q("lamp", "Lampa škváry", dep=["giants"], items=[("twilightforest:lamp_of_cinders", 1)], xp=120, d=[
            "V trollích jeskyních je trezor obalený obrovským obsidiánem. Prorazíš ho obrovým krumpáčem.",
            "Uvnitř je lampa škváry (&eLamp of Cinders&r). Spálí trnité keře, které blokují cestu na náhorní plošinu."]),
        Q("plateau", "Konec cesty", dep=["lamp"], tasks=[adv("twilightforest:progression_end")], icon="twilightforest:lamp_of_cinders", xp=150, d=[
            "Projdi trním (&eThornlands&r) až na poslední náhorní plošinu (&eFinal Plateau&r).",
            "Stojí tu Poslední hrad (&eFinal Plateau Castle&r). V této verzi modu (4.8) ještě není dokončený – tady postup lesa končí.",
            "Gratulujeme, prošel jsi celým Soumračným lesem!"]),

        # ---------- Materiály (původní) ----------
        Q("steeleaf", "Ocelový list a železodřevo", dep=["enter"], items=[("twilightforest:steeleaf_ingot", 4), ("twilightforest:ironwood_ingot", 4)], xp=30, d=[
            "Ocelový list (&eSteeleaf&r) najdeš v truhlách – v dutých kopcích, labyrintu, rytířské pevnosti a temné věži.",
            "Železodřevo vyrobíš: živý kořen (&eLiveroot&r) + surové železo + zlatý nuget = 2 surová železodřeva (&eRaw Ironwood&r). Ty přetav v peci.",
            "Živý kořen vytěžíš z živých kořenů pod zemí. Co z obou materiálů vyrobit, ukazuje kapitola výbavy."]),
    ],
)

# =====================================================================
#  TWILIGHT FOREST – výbava a kouzelné stromy (nová kapitola)
# =====================================================================
TWILIGHT_GEAR = dict(
    key="twilight_gear", group="explore", title="Soumračný les: výbava",
    subtitle="Zbroj, nástroje a kouzelné stromy", icon="twilightforest:knightmetal_chestplate",
    quests=[
        Q("intro", "Výbava ze soumraku", dep=["twilight:enter"], tasks=[auto()], icon="twilightforest:ironwood_chestplate", xp=10, d=[
            "Každý boss Soumračného lesa ti dá surovinu na lepší výbavu. Tady najdeš, co z ní vyrobit.",
            "Druhá polovina kapitoly jsou kouzelné stromy. Mají jádro, které pracuje za tebe."]),

        # ---------- Začátečník ----------
        Q("liveroot", "Živý kořen", dep=["intro"], items=[("twilightforest:liveroot", 4)], xp=15, shape="hexagon", size=1.5, s=ZAC, d=[
            "Pod zemí rostou kořeny. Světlejší živé kořeny (&eLiveroots&r) dávají živý kořen (&eLiveroot&r).",
            "Je to základ železodřeva – první dobré výbavy v lese."]),
        Q("ironwood_armor", "Železodřevěná zbroj", dep=["liveroot"], items=[("twilightforest:ironwood_chestplate", 1)], xp=30, d=[
            "Výbava ze železodřeva má očarování hned po výrobě. Třeba hrudní plát (&eIronwood Chestplate&r) má Ochranu.",
            "Každý kus má jiné očarování. Které, ukáže popis předmětu."]),
        Q("steeleaf_pick", "Ocelolistý krumpáč", dep=["twilight:steeleaf"], items=[("twilightforest:steeleaf_pickaxe", 1)], xp=30, d=[
            "Ocelolistý krumpáč (&eSteeleaf Pickaxe&r) má od výroby očarování Štěstí II. Víc rudy z každého bloku!",
            "Ocelolistý hrudní plát má od výroby Ochranu proti výbuchům II."]),
        Q("naga_armor", "Zbroj ze šupin", dep=["twilight:naga"], tasks=[adv("twilightforest:naga_armors")], icon="twilightforest:naga_chestplate", xp=40, d=[
            "Ze šupin nagy vyrobíš tuniku (8 šupin) a kalhoty (7 šupin).",
            "Tunika má Ochranu před ohněm III, kalhoty Ochranu III. Šupiny padají jen z nagy, takže ji možná budeš muset porazit vícekrát."]),
        Q("travellers", "Cestovatelská výbava", dep=["intro"], items=[("twilightforest:travellers_boots", 1)], xp=40, optional=True, d=[
            "Tříslovina (&eTannin&r) = lahev vody, sazenice, kořenová vlákna a listí soumračného dubu. Tříslovina + kůže = upravená kůže.",
            "Upravenou kůži polož na sušák (třeba &eTwilight Oak Drying Rack&r) ze 3 dřevěných půlbloků. Za 5 minut z ní je vyčiněná kůže (&eTanned Leather&r).",
            "Ze 4 vyčiněných kůží a 2 provázků vyrobíš cestovatelské boty (&eTraveller's Boots&r)."]),

        # ---------- Mapy a pomůcky ----------
        Q("maze_map", "Mapa bludiště", dep=["twilight:labyrinth"], items=[("twilightforest:maze_map", 1)], xp=30, d=[
            "Zaměřovač bludiště (&eMaze Map Focus&r) obklop 8 papíry. Vznikne mapa bludiště.",
            "Mapa ukazuje chodby labyrintu ve tvé výšce. Hledání Minoshrooma je s ní mnohem snazší."]),
        Q("ore_map", "Mapa rud", dep=["maze_map"], tasks=[adv("twilightforest:ore_map")], icon="twilightforest:ore_map", xp=60, optional=True, d=[
            "Mapa bludiště + blok diamantů + blok zlata + blok železa = mapa rud (&eBlank Maze/Ore Map&r).",
            "Kromě chodeb ukazuje i rudy ve tvé výšce. Je ale hodně drahá."]),
        Q("mazebreaker", "Rozbíječ bludiště", dep=["twilight:mino"], items=[("twilightforest:mazebreaker_pickaxe", 1)], xp=60, optional=True, d=[
            "V labyrintu je tajný trezor. Uvnitř leží krumpáč &eMazebreaker&r.",
            "Je to vzácný krumpáč, který najdeš jen tady."]),
        Q("charm2", "Silnější talisman", dep=["twilight:charm"], items=[("twilightforest:charm_of_life_2", 1)], xp=40, optional=True, d=[
            "4 talismany života I dají talisman života II (&eCharm of Life II&r). Zachrání tě s víc životy.",
            "V truhlách najdeš i talisman zachování (&eCharm of Keeping I&r). Když zemřeš, nechá ti část věcí."]),

        # ---------- Pokročilý: výbava z bossů ----------
        Q("scepters", "Žezla moci", dep=["twilight:lich"], tasks=[adv("twilightforest:lich_scepters")], icon="twilightforest:lifedrain_scepter", xp=100, optional=True, d=[
            "Lich upustí jedno ze 4 žezel: soumraku, čerpání života, zombíků nebo zpevnění.",
            "Každé má omezený počet nábojů. Kolik jich zbývá, vidíš v popisu předmětu.",
            "Získej všechna 4 – Licha budeš muset porazit vícekrát."]),
        Q("knight_armor", "Rytířská zbroj", dep=["twilight:knightmetal"], items=[("twilightforest:knightmetal_chestplate", 1)], xp=50,
          shape="hexagon", size=1.5, s=POK, d=[
            "S rytířským kovem začíná silná výbava. Vyrob si rytířskou zbroj (&eKnightmetal&r).",
            "Rytířský meč a krumpáč dávají větší poškození obrněným nepřátelům, sekera neobrněným."]),
        Q("block_chain", "Blok na řetězu", dep=["knight_armor"], items=[("twilightforest:block_and_chain", 1)], xp=40, optional=True, d=[
            "Rytířský prsten (&eKnightmetal Loop&r) = 4 ingoty rytířského kovu do kruhu.",
            "Blok rytířského kovu + 3 ingoty + prsten = blok na řetězu (&eBlock and Chain&r). Hodíš ho jako kouli na řetězu – rozbíjí bloky i nepřátele."]),
        Q("phantom_armor", "Fantomova zbroj", dep=["twilight:knight"], items=[("twilightforest:phantom_helmet", 1)], xp=60, optional=True, d=[
            "Rytířští fantomové občas upustí fantomovu helmu nebo brnění (&ePhantom Helmet&r).",
            "&aFantomova zbroj ti po smrti zůstane – nikdy o ni nepřijdeš.&r"]),
        Q("fiery_set", "Ohnivá výbava", dep=["twilight:fiery"], tasks=[adv("twilightforest:fiery_set")], icon="twilightforest:fiery_sword", xp=60, d=[
            "Měj v inventáři ohnivý krumpáč nebo meč a aspoň jeden kus ohnivé zbroje.",
            "Ohnivá zbroj pálí útočníky. Ohnivý meč zapaluje a ohnivý krumpáč rovnou taví rudy.",
            "&aTip:&r ohnivou výbavu vyrobíš i ze železné – dej železnou věc do stolu s ohnivou krví nebo slzami."]),
        Q("arctic", "Arktická zbroj", dep=["twilight:snowy"], items=[("twilightforest:arctic_chestplate", 1)], xp=30, d=[
            "Yetiové a zimní vlci pouštějí arktickou srst (&eArctic Fur&r). Z ní vyrobíš arktickou zbroj.",
            "Arktickou zbroj můžeš obarvit jako koženou."]),
        Q("yeti_armor", "Yetiho zbroj", dep=["twilight:yeti"], items=[("twilightforest:yeti_chestplate", 1)], xp=50, d=[
            "Ze srsti alfa yetiho vyrobíš yetiho zbroj (&eYeti Jacket&r). Má očarování Ochrana.",
            "Zchladí a zpomalí útočníky, kteří tě zasáhnou."]),
        Q("queen_bow", "Luk královny", dep=["twilight:queen"], items=[("twilightforest:triple_bow", 1)], xp=40, optional=True, d=[
            "Trojitý luk (&eTri-Bow&r) vystřelí naráz tři šípy.",
            "Sněhová královna upustí buď tento luk, nebo luk naváděných šípů. Možná ji budeš muset porazit znovu."]),

        # ---------- Kouzelné stromy ----------
        Q("hollow_tree", "Dutý strom", dep=["intro"], tasks=[structure("twilightforest:hollow_tree")], icon="twilightforest:twilight_oak_log", xp=30, d=[
            "Obří duté stromy (&eHollow Tree&r) rostou v lesích Soumračného lesa. Uvnitř je truhla, kterou hlídají pavouci.",
            "V truhle dutého stromu mohou být sazenice kouzelných stromů. Jinde je nenajdeš."]),
        Q("time_tree", "Strom času", dep=["hollow_tree"], items=[("twilightforest:time_sapling", 1)], xp=60,
          shape="hexagon", size=1.5, s=EXP, d=[
            "Kouzelné stromy pracují za tebe. Každý má uvnitř jádro, které pracuje samo.",
            "Ze sazenice stromu času (&eTree of Time Sapling&r) vyroste strom s časovými hodinami (&eTimewood Clock&r). Urychlují růst rostlin a dalších bloků v okolí.",
            "Jádro zapneš a vypneš pravým tlačítkem. &cKdyž jádro vytěžíš, dostaneš jen obyčejný kmen!&r"]),
        Q("trans_tree", "Strom proměny", dep=["hollow_tree"], items=[("twilightforest:transformation_sapling", 1)], xp=60, d=[
            "Strom proměny (&eTree of Transformation&r) má srdce proměny (&eHeart of Transformation&r).",
            "Postupně mění biom v okolí. Stromy proto sázej s rozmyslem."]),
        Q("mining_tree", "Hornický strom", dep=["hollow_tree"], items=[("twilightforest:mining_sapling", 1)], xp=60, d=[
            "Hornický strom (&eMiner's Tree&r) má hornické jádro (&eMinewood Core&r).",
            "Jádro jako magnet přitahuje rudy z okolí k sobě. Rudy pak snadno vytěžíš u kmene."]),
        Q("sorting_tree", "Třídicí strom", dep=["hollow_tree"], items=[("twilightforest:sorting_sapling", 1)], xp=60, d=[
            "Třídicí strom (&eSorting Tree&r) má třídicí motor (&eSortingwood Engine&r).",
            "Přesouvá věci mezi truhlami v okolí – každý předmět dá do truhly, kde už stejný předmět je. Udělá ti pořádek ve skladu."]),
        Q("powder", "Prášek proměny", dep=["twilight:dark_tower"], items=[("twilightforest:transformation_powder", 1)], xp=30, optional=True, d=[
            "Prášek proměny (&eTransformation Powder&r) promění jednoho tvora na jiného. JEI ukáže, koho na koho.",
            "Vaří se ve varném hrnci (&eCooking Pot&r): pekelná bradavice, kvašené pavoučí oko, ryba čtverzubec, jedovatá brambora, shnilé rajče a esence vrtáků (&eBorer Essence&r). Jako nádobu potřebuješ plátno (&eCanvas&r).", "Esence vrtáků padá z vrtáků (&eTowerwood Borer&r) v temné věži."]),
    ],
)

# Pořadí kapitol této oblasti v knize questů
CHAPTERS = [NETHER_END, THE_END, AETHER, DEEP_AETHER, TWILIGHT, TWILIGHT_GEAR]

NO_RECIPE = {}
