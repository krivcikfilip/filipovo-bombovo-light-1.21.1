from engine import Q

TRAINS = dict(
    key="trains", group="tech", title="Trains",
    subtitle="Create trains and Steam 'n' Rails", icon="create:controls",
    quests=[
        Q("track", "Lay the tracks", items=[("create:track", 32)], xp=30, d=[
            "Create trains run on their own tracks. &bSteam 'n' Rails&r adds tracks in every wood type, wide and narrow gauge, monorail and even invisible phantom tracks."]),
        Q("station", "Train station", dep=["track"], items=[("create:track_station", 1)], xp=40, d=[
            "Place the station on a track. Trains are assembled at a station: put a bogey on the track, glue blocks onto it and add controls."]),
        Q("controls", "Train controls", dep=["station"], items=[("create:controls", 1)], xp=40, d=[
            "The controls make the train drivable. Assemble the train in the station screen."]),
        Q("schedule", "Timetable", dep=["controls"], items=[("create:schedule", 1)], xp=40, d=[
            "A schedule tells the train where to go and how long to wait. Give it to a mob seated at the controls and the train drives by itself."]),
        Q("signal", "Signals", dep=["station"], items=[("create:track_signal", 2)], xp=40, d=[
            "Signals split the network into blocks so trains don't crash into each other. Needed as soon as two trains share a track."]),
        Q("observer", "Track observer", dep=["signal"], items=[("create:track_observer", 1)], xp=30, d=[
            "Gives a redstone signal when a train passes - open gates, ring bells, light lamps."]),
        Q("door", "Train doors", dep=["controls"], items=[("create:train_door", 2)], xp=20),
        Q("semaphore", "Semaphore", dep=["signal"], items=[("railways:semaphore", 1)], xp=25, d=[
            "A classic semaphore arm that shows a signal's state."]),
        Q("switch", "Track switch", dep=["track"], items=[("railways:track_switch_andesite", 1)], xp=30, d=[
            "A motorised switch that changes the direction of a junction, controlled by redstone or by the train's schedule."]),
        Q("coupler", "Track coupler", dep=["signal"], items=[("railways:track_coupler", 1)], xp=40, d=[
            "Couples or decouples train cars at a point on the track - automate freight trains that drop off wagons."]),
        Q("conductor", "Train crew", dep=["schedule"], items=[("railways:conductor_whistle", 1)], xp=40, d=[
            "&bSteam 'n' Rails&r adds conductors - little helpers for your trains - and the conductor whistle to command them."]),
        Q("fuel", "Fuel tank", dep=["controls"], items=[("railways:fuel_tank", 1)], xp=30, d=[
            "Trains can carry their own liquid fuel instead of needing a blaze burner refill."]),
        Q("handcar", "Handcar", dep=["track"], items=[("railways:handcar", 1)], xp=30, d=[
            "A small, cheap, human-powered rail vehicle - perfect for quick trips along the line."]),
        Q("locometal", "Locometal", dep=["controls"], items=[("railways:riveted_locometal", 8)], xp=20, d=[
            "Blocks for building real-looking locomotives: boilers, smokeboxes, vents. Paint them with the paint brush."]),
        Q("benchcart", "Benchcart", dep=["track"], items=[("railways:benchcart", 1)], xp=20, d=[
            "A minecart with a crafting table. There is also a jukebox cart."]),
        Q("headlight", "Bells & Whistles", dep=["locometal"], items=[("bellsandwhistles:headlight", 1)], xp=20, d=[
            "&bBells & Whistles&r adds train details: headlights, grab rails, steps, pilots and metro panels."]),
        Q("platform", "Station platform", dep=["headlight"], items=[("bellsandwhistles:station_platform", 8)], xp=20),
    ],
)

QUARK = dict(
    key="quark", group="start", title="Quark",
    subtitle="Small improvements you might miss", icon="quark:seed_pouch",
    quests=[
        Q("pouch", "Seed Pouch", items=[("quark:seed_pouch", 1)], xp=20, d=[
            "&bQuark&r adds hundreds of small vanilla-style improvements. This chapter shows the useful items.",
            "The seed pouch holds a lot of one kind of seed or crop, so they take only one slot."]),
        Q("trowel", "Trowel", items=[("quark:trowel", 1)], xp=20, d=[
            "Places a random block from your hotbar - great for natural-looking walls and paths."]),
        Q("crate", "Crate", items=[("quark:crate", 1)], xp=20, d=[
            "Stores many different items in one block. Handy for mixed materials."]),
        Q("pipe", "Pipes", items=[("quark:pipe", 8)], xp=20, d=[
            "Simple item pipes that push items forward. Encased pipes look tidier."]),
        Q("chute", "Chute", dep=["pipe"], items=[("quark:chute", 1)], xp=15, d=[
            "Drops items straight down - a cheap hopper alternative."]),
        Q("magnet", "Magnet", items=[("quark:magnet", 1)], xp=30, d=[
            "Powered by redstone, it pushes or pulls metal blocks - a new kind of redstone contraption."]),
        Q("abacus", "Abacus", items=[("quark:abacus", 1)], xp=15, d=[
            "Measures the distance between two blocks."]),
        Q("cloud", "Bottled cloud", items=[("quark:bottled_cloud", 1)], xp=20, d=[
            "Places a temporary block in mid-air, so you can start building where there is nothing to build on. Fill a bottle high up in the clouds."]),
        Q("pickarang", "Pickarang", items=[("quark:pickarang", 1)], xp=40, d=[
            "A pickaxe you throw like a boomerang. It mines the block it hits and comes back."]),
        Q("slime", "Slime in a bucket", items=[("quark:slime_in_a_bucket", 1)], xp=20, d=[
            "Catch a small slime. It gets excited when you are in a slime chunk."]),
        Q("tome", "Ancient Tome", items=[("quark:ancient_tome", 1)], xp=60, d=[
            "Found in dungeon loot. Combine it at an anvil with a maxed-out enchanted book to go one level above the normal maximum."]),
        Q("quill", "Pathfinder's Quill", items=[("quark:pathfinders_quill", 1)], xp=40, d=[
            "Shows the way to a specific biome."]),
        Q("potato", "Tiny Potato", items=[("quark:tiny_potato", 1)], xp=10, d=[
            "It believes in you."]),
    ],
)

GEAR = dict(
    key="gear", group="explore", title="Gear & Combat",
    subtitle="Weapons, armour and shields", icon="spartanshieldsunofficial:iron_tower_shield",
    quests=[
        Q("shield", "A real shield", items=[("spartanshieldsunofficial:iron_basic_shield", 1)], xp=20, d=[
            "&bSpartan Shields&r adds shields from many materials. Basic shields are light, tower shields block more but slow you down.",
            "Most metals in the pack work - iron is just the first milestone."]),
        Q("tower", "Tower shield", dep=["shield"], items=[("spartanshieldsunofficial:iron_tower_shield", 1)], xp=25),
        Q("diamond_shield", "Diamond shield", dep=["tower"], items=[("spartanshieldsunofficial:diamond_tower_shield", 1)], xp=40),
        Q("netherite", "Netherite", items=[("minecraft:netherite_ingot", 1)], xp=40, d=[
            "Netherite is not the end. &bAdvanced Netherite&r upgrades it further in four tiers."]),
        Q("an_iron", "Iron-infused netherite", dep=["netherite"], items=[("advancednetherite:netherite_iron_ingot", 1)], xp=60, d=[
            "Each tier is stronger than the last and adds its own bonus. JEI shows how to upgrade tools and armour."]),
        Q("an_gold", "Gold-infused netherite", dep=["an_iron"], items=[("advancednetherite:netherite_gold_ingot", 1)], xp=80),
        Q("an_emerald", "Emerald-infused netherite", dep=["an_gold"], items=[("advancednetherite:netherite_emerald_ingot", 1)], xp=100),
        Q("an_diamond", "Diamond-infused netherite", dep=["an_emerald"], items=[("advancednetherite:netherite_diamond_ingot", 1)], xp=150, d=[
            "The best netherite tier."]),
        Q("cruorite", "Cruorite", items=[("just_in_nether:cruorite", 1)], xp=40, d=[
            "&bJust-In Nether&r materials make modular weapons: swords, katanas, spears, hammers, bows and more."]),
        Q("devourite", "Devourite", dep=["cruorite"], items=[("just_in_nether:devourite", 1)], xp=50),
        Q("kiwano", "Kiwano armour", items=[("netherexotics:kiwano_chestplate", 1)], xp=40, d=[
            "&bNether Exotics&r adds armour and tools made from Nether fruit."]),
        Q("brass", "Brass armour", items=[("create_sa:brass_chestplate", 1)], xp=30, d=[
            "&bCreate Stuff & Additions&r adds copper, zinc and brass tools and armour."]),
    ],
)

LUMINOUS = dict(
    key="luminous", group="explore", title="Luminous",
    subtitle="Creatures, bosses and butterflies", icon="luminous_beasts:ultimate_bestiary",
    quests=[
        Q("bestiary", "Ultimate Bestiary", items=[("luminous_beasts:ultimate_bestiary", 1)], xp=20, d=[
            "The &bLuminous&r mods add new creatures, big boss-like beasts and structures in the Overworld and the Nether.",
            "The bestiary describes the beasts you meet."]),
        Q("net", "Butterfly net", items=[("luminous_butterflies:butterfly_net", 1)], xp=15, d=[
            "Catch butterflies and keep them in jars. There are many species to find."]),
        Q("encyclopedia", "Butterfly Encyclopedia", dep=["net"], items=[("luminous_butterflies:butterfly_encyclopedia", 1)], xp=20),
        Q("ent", "Tree Ent", dep=["bestiary"], items=[("luminous_beasts:tree_ent_trophy", 1)], xp=80, d=[
            "One of the big Luminous beasts. Defeat it and keep its trophy."]),
        Q("hermit", "Hermit King", dep=["bestiary"], items=[("luminous_beasts:hermit_king_trophy", 1)], xp=80, d=[
            "Another big beast - its trophy proves you beat it."]),
        Q("mummy", "Mummy", dep=["bestiary"], items=[("luminous_beasts:mummy_trophy", 1)], xp=80, d=[
            "A beast of the desert."]),
        Q("yeti", "Yeti", dep=["bestiary"], items=[("luminous_beasts:yeti_trophy", 1)], xp=80, d=[
            "A beast of the cold lands."]),
        Q("phoenix", "Phoenix", dep=["bestiary"], items=[("luminous_beasts:phoenix_trophy", 1)], xp=120, d=[
            "A fiery bird and one of the toughest Luminous beasts."]),
        Q("executioner", "Executioner", dep=["bestiary"], items=[("luminous_beasts:executioner_trophy", 1)], xp=120, d=[
            "A dangerous brute - bring good armour."]),
        Q("scrap", "Legendary scrap", dep=["ent", "hermit", "mummy", "yeti"], items=[("luminous_beasts:legendary_scrap", 1)], xp=80, d=[
            "Used to make smithing augments - upgrades that add special effects to your gear."]),
    ],
)
