from engine import Q, check, dim, structure, auto

EXPLORE = dict(
    key="exploration", group="explore", title="Exploring the Overworld",
    subtitle="Structures, dungeons and loot", icon="minecraft:compass",
    quests=[
        Q("start", "A bigger world", icon="minecraft:filled_map", tasks=[auto()], xp=10, d=[
            "&bTectonic&r and &bTerralith&r make huge mountains and new biomes. Structures from &bYUNG's&r, &bTowns and Towers&r, &bMoog's&r, &bRepurposed Structures&r and &bIDAS&r are everywhere.",
            "Chests are &bLootr&r chests - each player gets their own loot."]),
        Q("dungeon", "Take a spawner home", dep=["start"], items=[("minecraft:spawner", 1)], xp=60, d=[
            "YUNG's catacombs, spider caves and skeleton dungeons replace the old tiny dungeons.",
            "A pickaxe with the &bReplication&r enchantment can pick up a spawner. &bApothic Spawners&r lets you upgrade it with items."]),
        Q("desert", "Desert temple", dep=["start"], tasks=[structure("betterdeserttemples:desert_temple")], icon="minecraft:sand", xp=30),
        Q("monument", "Ocean monument", dep=["start"], tasks=[structure("betteroceanmonuments:ocean_monument")], icon="minecraft:prismarine", xp=60),
        Q("stronghold", "Stronghold", dep=["start"], tasks=[structure("betterstrongholds:stronghold")], icon="minecraft:ender_eye", xp=60, d=[
            "Throw eyes of ender to find it. YUNG's stronghold is a real maze."]),
        Q("ancient", "Ancient City", dep=["stronghold"], tasks=[structure("minecraft:ancient_city")], icon="minecraft:sculk_catalyst", xp=100, d=[
            "Deep below in the deep dark. Be quiet - the Warden hears everything."]),
    ],
)

CREATURES = dict(
    key="creatures", group="explore", title="Creatures",
    subtitle="Alex's Mobs, Naturalist and friends", icon="alexsmobs:animal_dictionary",
    quests=[
        Q("dict", "Animal Dictionary", items=[("alexsmobs:animal_dictionary", 1)], xp=20, d=[
            "&bAlex's Mobs&r adds about 90 animals. The dictionary explains each one, including what it drops and how to tame it."]),
        Q("banana", "Bananas!", dep=["dict"], items=[("alexsmobs:banana", 1)], xp=15, d=[
            "Bananas drop from jungle leaves. Gorillas love them."]),
        Q("croc", "Crocodile scute", dep=["dict"], items=[("alexsmobs:crocodile_scute", 1)], xp=30),
        Q("roadrunner", "Meep meep", dep=["dict"], items=[("alexsmobs:roadrunner_feather", 1)], xp=25, d=[
            "Roadrunner feathers on boots make you faster on sand."]),
        Q("bear", "Bear fur", dep=["dict"], items=[("alexsmobs:bear_fur", 1)], xp=30),
        Q("net", "Catch a critter", items=[("naturalist:capture_net", 1)], xp=15, d=[
            "&bNaturalist&r: deer, bears, snails, butterflies, lions and more. The net catches small animals."]),
        Q("butterfly", "Butterfly", dep=["net"], items=[("naturalist:butterfly", 1)], xp=20),
        Q("venison", "Venison", dep=["net"], items=[("naturalist:venison", 1)], xp=15),
        Q("critters", "Critters and Companions", items=[("crittersandcompanions:dragonfly_wing", 1)], xp=20, d=[
            "Otters, ferrets, red pandas, koi, dragonflies and more."]),
        Q("hamster", "Adorable Hamsters", items=[("adorablehamsterpets:hamster_food_mix", 1)], xp=20, d=[
            "Tame a hamster with food mix. Hamsters sit on your shoulder and can sniff out ores!"]),
        Q("shark", "Ben's Sharks", items=[("benssharks:shark_tooth", 1)], xp=30),
    ],
)

NETHER_END = dict(
    key="nether_end", group="explore", title="The Nether & The End",
    subtitle="Hot, dark and far away", icon="minecraft:netherrack",
    quests=[
        Q("nether", "Welcome to hell", tasks=[dim("minecraft:the_nether")], icon="minecraft:obsidian", xp=40, d=[
            "The Nether is overhauled by &bIncendium&r, &bNether Exotics&r, &bJaden's Nether Expansion&r and &bJust-In Nether&r. New biomes, mobs and structures."]),
        Q("blaze", "Blaze rods", dep=["nether"], items=[("minecraft:blaze_rod", 6)], xp=30, d=[
            "Blazes live in Nether fortresses - with YUNG's Better Nether Fortresses they are much bigger and full of loot."]),
        Q("bastion", "Bastion", dep=["nether"], tasks=[structure("minecraft:bastion_remnant")], icon="minecraft:gilded_blackstone", xp=50),
        Q("exotics", "Nether fruit", dep=["nether"], items=[("netherexotics:kiwano", 1), ("netherexotics:pitaya", 1)], xp=30, d=[
            "&bNether Exotics&r grows strange fruit trees in the Nether. Their juices give useful effects."]),
        Q("jin", "Just-In Nether", dep=["nether"], items=[("just_in_nether:cruorite", 1)], xp=40, d=[
            "New Nether mobs and materials. Cruorite makes modular weapons - see Gear & Combat."]),
        Q("debris", "Ancient Debris", dep=["nether"], items=[("minecraft:ancient_debris", 2)], xp=60),
        Q("netherite", "Netherite", dep=["debris"], items=[("minecraft:netherite_ingot", 1)], xp=100, d=[
            "&bAdvanced Netherite&r lets you upgrade netherite further with iron, gold, emerald and diamond."]),
        Q("soulglass", "Nether Expansion", dep=["nether"], items=[("netherexp:soul_glass", 4)], xp=20),
        Q("skull", "Wither skull", dep=["nether"], items=[("minecraft:wither_skeleton_skull", 3)], xp=60),
        Q("wither", "The Wither", dep=["skull"], items=[("minecraft:nether_star", 1)], xp=150, d=[
            "Fight it underground or far from your base!"]),
        Q("eyes", "Eyes of Ender", dep=["blaze"], items=[("minecraft:ender_eye", 12)], xp=40),
        Q("end", "The End", dep=["eyes"], tasks=[dim("minecraft:the_end")], icon="minecraft:end_stone", xp=60, d=[
            "&bNullscape&r and &bUnusual End&r change the outer islands completely, &bYUNG's Better End Island&r improves the dragon fight."]),
        Q("dragon", "Free the End", dep=["end"], items=[("minecraft:dragon_breath", 1)], xp=150, d=[
            "Defeat the Ender Dragon and collect its breath with a bottle."]),
        Q("elytra", "Elytra", dep=["dragon"], items=[("minecraft:elytra", 1)], xp=150, d=[
            "Find an End City ship. &bElytra Slot&r lets you wear it together with a chestplate."]),
        Q("crystal", "Unusual End", dep=["end"], items=[("unusualend:shiny_crystal", 1)], xp=40),
    ],
)

AETHER = dict(
    key="aether", group="explore", title="The Aether",
    subtitle="The heaven dimension", icon="aether:golden_parachute",
    quests=[
        Q("portal", "A portal to the sky", items=[("minecraft:glowstone", 4)], xp=15, d=[
            "Build a frame from &eglowstone&r (like a Nether portal) and light it with a &ewater bucket&r."]),
        Q("aether", "Enter the Aether", dep=["portal"], tasks=[dim("aether:the_aether")], icon="aether:aether_portal_frame", xp=40, d=[
            "Floating islands, friendly moas and dangerous dungeons. Falling off an island drops you back in the overworld - a parachute helps."]),
        Q("skyroot", "Skyroot & Holystone", dep=["aether"], items=[("aether:skyroot_log", 8), ("aether:holystone", 16)], xp=20, d=[
            "Aether tools are made of skyroot and holystone. Normal tools work worse here."]),
        Q("ambrosium", "Ambrosium", dep=["skyroot"], items=[("aether:ambrosium_shard", 4)], xp=20, d=[
            "Ambrosium powers the altar, freezer and incubator."]),
        Q("altar", "Altar & Freezer", dep=["ambrosium"], items=[("aether:altar", 1), ("aether:freezer", 1)], xp=30),
        Q("zanite", "Zanite", dep=["skyroot"], items=[("aether:zanite_gemstone", 8)], xp=30, d=[
            "Zanite tools get stronger the more damaged they are."]),
        Q("parachute", "Parachute", dep=["aether"], items=[("aether:cold_parachute", 1)], xp=20, d=[
            "Made from cold aerclouds. Saves you from a long fall."]),
        Q("moa", "Moa egg", dep=["altar"], items=[("aether:incubator", 1)], xp=40, d=[
            "Moa eggs come in several colours. Incubate one and ride your own giant bird."]),
        Q("bronze", "Bronze dungeon", dep=["zanite"], items=[("aether:bronze_dungeon_key", 1)], xp=80, d=[
            "Defeat the Slider in the bronze dungeon."]),
        Q("gravitite", "Gravitite", dep=["bronze"], items=[("aether:enchanted_gravitite", 4)], xp=60, d=[
            "Gravitite ore floats up when mined. Enchant it at the altar."]),
        Q("silver", "Silver dungeon", dep=["bronze"], items=[("aether:silver_dungeon_key", 1)], xp=100, d=[
            "The Valkyrie Queen waits at the top. Collect victory medals from valkyries first."]),
        Q("gold", "Gold dungeon", dep=["silver"], items=[("aether:gold_dungeon_key", 1)], xp=150, d=[
            "The Sun Spirit. Bring fire resistance."]),
        Q("ring", "Accessories", dep=["zanite"], items=[("aether:zanite_ring", 1)], xp=20, d=[
            "Aether rings, pendants and gloves go in the accessory slots (inventory button)."]),
        Q("deep", "Deep Aether", dep=["aether"], items=[("deep_aether:skyjade", 1)], xp=30, d=[
            "&bDeep Aether&r adds new biomes, mobs and a boss to the Aether. Skyjade is its first new material."]),
    ],
)

TWILIGHT = dict(
    key="twilight", group="explore", title="The Twilight Forest",
    subtitle="A world of bosses", icon="twilightforest:naga_trophy",
    quests=[
        Q("portal", "Portal", items=[("minecraft:diamond", 1)], xp=15, d=[
            "Dig a 2x2 water pool, surround it with flowers and grass, then throw a &ediamond&r in. Lightning opens the portal."]),
        Q("enter", "Into the twilight", dep=["portal"], tasks=[dim("twilightforest:twilight_forest")], icon="twilightforest:magic_map", xp=40, d=[
            "Bosses must be beaten in order - areas are locked by curses until you do. A magic map shows the bosses' locations."]),
        Q("naga", "Naga", dep=["enter"], items=[("twilightforest:naga_trophy", 1)], xp=80, d=["The giant snake in the courtyard."]),
        Q("lich", "Lich", dep=["naga"], items=[("twilightforest:lich_trophy", 1)], xp=100, d=["Top of the Lich Tower. Reflect his fireballs."]),
        Q("steeleaf", "Steeleaf & Ironwood", dep=["naga"], items=[("twilightforest:steeleaf_ingot", 4), ("twilightforest:ironwood_ingot", 4)], xp=30),
        Q("mino", "Minoshroom", dep=["lich"], items=[("twilightforest:minoshroom_trophy", 1)], xp=100, d=["At the bottom of the labyrinth."]),
        Q("hydra", "Hydra", dep=["mino"], items=[("twilightforest:hydra_trophy", 1)], xp=150, d=["In the fire swamp."]),
        Q("fiery", "Fiery ingot", dep=["hydra"], items=[("twilightforest:fiery_ingot", 2)], xp=40),
        Q("knight", "Knight Phantoms", dep=["lich"], items=[("twilightforest:knight_phantom_trophy", 1)], xp=120, d=["Inside the goblin stronghold."]),
        Q("knightmetal", "Knightmetal", dep=["knight"], items=[("twilightforest:knightmetal_ingot", 4)], xp=40),
        Q("ghast", "Ur-Ghast", dep=["knight"], items=[("twilightforest:ur_ghast_trophy", 1)], xp=150, d=["In the Dark Tower."]),
        Q("carminite", "Carminite", dep=["ghast"], items=[("twilightforest:carminite", 4)], xp=30),
        Q("yeti", "Alpha Yeti", dep=["ghast"], items=[("twilightforest:alpha_yeti_trophy", 1)], xp=150),
        Q("queen", "Snow Queen", dep=["yeti"], items=[("twilightforest:snow_queen_trophy", 1)], xp=200, d=["Top of the Aurora Palace."]),
        Q("uncrafting", "Uncrafting Table", dep=["enter"], items=[("twilightforest:uncrafting_table", 1)], xp=40, d=[
            "Breaks items back into ingredients."]),
        Q("charm", "Charm of Life", dep=["enter"], items=[("twilightforest:charm_of_life_1", 1)], xp=40),
        Q("ram", "Questing Ram", dep=["enter"], items=[("twilightforest:quest_ram_trophy", 1)], xp=80, d=[
            "Feed the ram all 16 colours of wool."]),
    ],
)

ALEXSCAVES = dict(
    key="alexs_caves", group="explore", title="Alex's Caves",
    subtitle="Six rare underground biomes", icon="alexscaves:cave_tablet",
    quests=[
        Q("tablet", "Cave Tablet", items=[("alexscaves:cave_tablet", 1)], xp=30, d=[
            "&bAlex's Caves&r biomes are rare and deep. Cave tablets from cave structures point you to one.",
            "Combine a tablet with a map in a cartography table to make a cave map."]),
        Q("book", "Cave Book", dep=["tablet"], items=[("alexscaves:cave_book", 1)], xp=20),
        Q("magnetic", "Magnetic Caves", dep=["tablet"], items=[("alexscaves:raw_scarlet_neodymium", 1), ("alexscaves:raw_azure_neodymium", 1)], xp=60, d=[
            "Floating magnetic rocks and robots. Neodymium makes magnets and the galena gauntlet."]),
        Q("primordial", "Primordial Caves", dep=["tablet"], items=[("alexscaves:amber", 1), ("alexscaves:dinosaur_chop", 1)], xp=60, d=[
            "A lost world with real dinosaurs! Bring friends."]),
        Q("toxic", "Toxic Caves", dep=["tablet"], items=[("alexscaves:uranium", 1)], xp=60, d=[
            "Radioactive. Wear protection - and stay away from the nuclear bombs."]),
        Q("abyssal", "Abyssal Chasm", dep=["tablet"], items=[("alexscaves:sea_glass_shards", 1)], xp=60, d=[
            "Deep under the ocean, total darkness. A submarine is the best way to explore it."]),
        Q("submarine", "Submarine", dep=["abyssal"], items=[("alexscaves:submarine", 1)], xp=100),
        Q("forlorn", "Forlorn Hollows", dep=["tablet"], items=[("alexscaves:guanostone", 1), ("alexscaves:pure_darkness", 1)], xp=80, d=[
            "Scary bats and the darkest place in the game."]),
        Q("candy", "Candy Cavity", dep=["tablet"], items=[("alexscaves:candy_cane", 1), ("alexscaves:block_of_chocolate", 1)], xp=60, d=[
            "Everything is made of sweets. Some of it is alive."]),
    ],
)

ADASTRA = dict(
    key="ad_astra", group="explore", title="Ad Astra",
    subtitle="Rockets and other planets", icon="ad_astra:tier_1_rocket",
    quests=[
        Q("steel", "Steel", items=[("ad_astra:steel_ingot", 8)], xp=20, d=[
            "&bAd Astra&r takes you to the Moon, Mars, Venus, Mercury and Glacio.",
            "Start with steel - smelt iron in the Etrionic Blast Furnace (or use steel from other mods via tags)."]),
        Q("furnace", "Etrionic Blast Furnace", items=[("ad_astra:etrionic_blast_furnace", 1)], xp=20),
        Q("compressor", "Compressor", dep=["steel"], items=[("ad_astra:compressor", 1), ("ad_astra:steel_plate", 8)], xp=25),
        Q("workbench", "NASA Workbench", dep=["compressor"], items=[("ad_astra:nasa_workbench", 1)], xp=40, d=[
            "Rockets are built here from nose cones, plates, fins and engines."]),
        Q("fuel", "Fuel", dep=["compressor"], items=[("ad_astra:fuel_refinery", 1), ("ad_astra:fuel_bucket", 1)], xp=40, d=[
            "Refine oil into rocket fuel. Diesel Generators' crude oil works."]),
        Q("suit", "Space suit", dep=["compressor"], items=[("ad_astra:space_helmet", 1), ("ad_astra:space_suit", 1), ("ad_astra:space_pants", 1), ("ad_astra:space_boots", 1)], xp=60, d=[
            "No air in space! Fill the suit with oxygen in an oxygen loader."]),
        Q("oxygen", "Oxygen Loader", dep=["suit"], items=[("ad_astra:oxygen_loader", 1)], xp=30),
        Q("rocket1", "Tier 1 Rocket", dep=["workbench", "fuel"], items=[("ad_astra:tier_1_rocket", 1), ("ad_astra:launch_pad", 1)], xp=100),
        Q("moon", "The Moon", dep=["rocket1", "oxygen"], tasks=[dim("ad_astra:moon")], icon="ad_astra:desh_ingot", xp=150, d=[
            "Desh ore is found on the Moon."]),
        Q("desh", "Desh", dep=["moon"], items=[("ad_astra:desh_ingot", 8)], xp=40),
        Q("base", "Moon base", dep=["moon"], items=[("ad_astra:oxygen_distributor", 1), ("ad_astra:solar_panel", 2)], xp=60, d=[
            "An oxygen distributor fills a sealed room with air."]),
        Q("rocket2", "Tier 2 Rocket", dep=["desh"], items=[("ad_astra:tier_2_rocket", 1)], xp=120),
        Q("mars", "Mars", dep=["rocket2"], tasks=[dim("ad_astra:mars")], icon="ad_astra:ostrum_ingot", xp=200),
        Q("ostrum", "Ostrum", dep=["mars"], items=[("ad_astra:ostrum_ingot", 8)], xp=50),
        Q("rocket3", "Tier 3 Rocket", dep=["ostrum"], items=[("ad_astra:tier_3_rocket", 1)], xp=150),
        Q("venus", "Venus", dep=["rocket3"], tasks=[dim("ad_astra:venus")], icon="ad_astra:calorite_ingot", xp=250, d=[
            "Very hot - you need a netherite space suit."]),
        Q("calorite", "Calorite", dep=["venus"], items=[("ad_astra:calorite_ingot", 8)], xp=60),
        Q("rocket4", "Tier 4 Rocket", dep=["calorite"], items=[("ad_astra:tier_4_rocket", 1)], xp=200),
        Q("glacio", "Glacio", dep=["rocket4"], tasks=[dim("ad_astra:glacio")], icon="ad_astra:jet_suit", xp=300, d=[
            "A frozen planet in another solar system."]),
        Q("rover", "Rover", dep=["moon"], items=[("ad_astra:tier_1_rover", 1)], xp=60),
    ],
)

FOSSILS = dict(
    key="fossils", group="explore", title="Fossils & Archeology",
    subtitle="Bring dinosaurs back to life", icon="fossil:analyzer",
    quests=[
        Q("fossil", "Dig up a fossil", items=[("fossil:fossil_bio", 1)], xp=20, d=[
            "&bFossils and Archeology Revival&r - ported to 1.21.1 just for this pack!",
            "Fossil blocks are found underground. They drop bio fossils, plant fossils and relic scraps."]),
        Q("relic", "Relic scrap", dep=["fossil"], items=[("fossil:relic_scrap", 1)], xp=15),
        Q("dinopedia", "Dinopedia", dep=["fossil"], items=[("fossil:dinopedia", 1)], xp=15, d=[
            "Right-click a creature to see its age, hunger and mood."]),
        Q("sifter", "Sifter", dep=["fossil"], items=[("fossil:sifter", 1)], xp=25, d=[
            "Sift sand and gravel for fossils, amber and pottery."]),
        Q("analyzer", "Analyzer", dep=["fossil"], items=[("fossil:analyzer", 1)], xp=40, d=[
            "Analyzes bio fossils, relics and frozen meat into &eDNA&r. Needs fuel."]),
        Q("goo", "Bio Goo", dep=["analyzer"], items=[("fossil:bio_goo", 2)], xp=20, d=[
            "The analyzer turns fossils into random &eDNA&r. Bio goo feeds the embryo in the culture vat."]),
        Q("vat", "Culture Vat", dep=["goo"], items=[("fossil:culture_vat", 1)], xp=40, d=[
            "DNA + bio goo in the culture vat grows an egg (dinosaurs) or an embryo (mammals, injected into an animal with a syringe). Watch out - sometimes it fails and something nasty comes out.",
            "Place eggs somewhere warm and wait for them to hatch. Babies imprint on the first player they see."]),
        Q("feeder", "Feeder", dep=["vat"], items=[("fossil:feeder", 1)], xp=30, d=[
            "Dinosaurs eat from a feeder (plants on one side, meat on the other)."]),
        Q("whip", "Whip", dep=["vat"], items=[("fossil:whip", 1)], xp=30, d=["Command and ride your dinosaurs."]),
        Q("worktable", "Worktable", dep=["relic"], items=[("fossil:worktable", 1)], xp=25, d=[
            "Repairs ancient tools and restores broken swords."]),
        Q("sword", "Ancient sword", dep=["worktable"], items=[("fossil:ancient_sword", 1)], xp=60),
        Q("amber", "Mosquito in amber", dep=["sifter"], items=[("fossil:amber_chunk_mosquito", 1)], xp=60, d=[
            "Just like in the movies."]),
        Q("key", "Ancient key", dep=["sword"], items=[("fossil:ancient_key", 1)], xp=80, d=[
            "Opens the way to Anu, the Nether boss of the mod."]),
    ],
)
