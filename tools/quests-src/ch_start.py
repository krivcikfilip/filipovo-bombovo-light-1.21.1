from engine import Q, check, dim, auto

WELCOME = dict(
    key="welcome", group="start", title="Welcome to Filipovo Bombovo 2",
    subtitle="Read this first - the pack in five minutes", icon="ftbquests:book",
    quests=[
        Q("hello", "Welcome!", icon="ftbquests:book", tasks=[auto()], xp=20, d=[
            "This quest book is a &etutorial&r for the mods in this pack.",
            "Every chapter walks you through one mod (or a group of similar mods) from the first step to the cool stuff.",
            "",
            "Item quests complete as soon as the item is in your inventory - nothing gets taken. If you already made something, just open the book and claim it.",
            "Rewards are small on purpose: the pack is already being played, so they are a thank-you, not a shortcut.",
        ]),
        Q("waystone", "Waystones", dep=["hello"], items=[("waystones:waystone", 1)], xp=25, d=[
            "Waystones spawn in villages and you can craft your own.",
            "Right-click one to activate it, then teleport between all activated waystones for a bit of XP.",
            "A &ewarp stone&r or &ereturn scroll&r lets you travel without standing at a waystone.",
        ]),
        Q("warpstone", "Teleport from anywhere", dep=["waystone"], items=[("waystones:warp_stone", 1)], xp=40, d=[
            "The warp stone opens the waystone menu from anywhere. It needs to recharge after each use.",
        ]),
        Q("backpack", "More pockets", dep=["hello"], items=[("sophisticatedbackpacks:backpack", 1)], xp=25, d=[
            "&bSophisticated Backpacks&r - wear it on your back or carry it, and open it anywhere.",
            "Upgrades make it great: &epickup&r (auto-collects items), &emagnet&r, &efeeding&r (eats for you), &erefill&r and many more.",
            "Backpacks can be upgraded to iron, gold, diamond and netherite for more slots.",
        ]),
        Q("pickup", "Let the backpack do the work", dep=["backpack"], items=[("sophisticatedbackpacks:pickup_upgrade", 1)], xp=25, d=[
            "Put the upgrade into the backpack's upgrade slots. Set a filter so it only collects what you want.",
        ]),
        Q("feeding", "Never starve again", dep=["pickup"], items=[("sophisticatedbackpacks:feeding_upgrade", 1)], xp=30, d=[
            "The feeding upgrade eats food from the backpack when you get hungry. Very handy with &bSpice of Life&r.",
        ]),
        Q("death", "If you die", dep=["hello"], tasks=[auto()], icon="minecraft:skeleton_skull", xp=10, d=[
            "Your items stay in a &ecorpse&r where you died - nothing despawns. Walk back and open it.",
            "&e/back&r takes you back to where you died, &e/sethome&r and &e/home&r save your favourite places.",
        ]),
        Q("friends", "Playing together", dep=["hello"], tasks=[auto()], icon="minecraft:bell", xp=10, d=[
            "Chests in dungeons are &bLootr&r chests - every player gets their own loot, so nobody steals it from the others.",
            "&bCarry On&r lets you pick up chests (with their contents) and animals with empty hands while sneaking.",
        ]),
        Q("food", "Eat a varied diet", dep=["hello"], items=[("solonion:food_book", 1)], xp=25, d=[
            "&bSpice of Life&r rewards variety: every new food you eat increases your maximum health.",
            "The food book shows what you have already eaten. Lunchboxes let you carry many different meals.",
            "The pack has hundreds of foods - see the Food & Farming chapters.",
        ]),
        Q("lunchbox", "Packed lunch", dep=["food"], items=[("solonion:lunchbox", 1)], xp=30, d=[
            "A lunchbox automatically feeds you the food you haven't eaten recently.",
        ]),
        Q("chunks", "Keep your machines running", dep=["friends"], items=[("chunkloaders:single_chunk_loader", 1)], xp=40, d=[
            "Farms and machines only work while a player is nearby. A chunk loader keeps its area running even when you are away.",
            "Use them sparingly - every loaded chunk costs server performance.",
        ]),
    ],
)

VANILLA = dict(
    key="vanilla", group="start", title="The Basics",
    subtitle="Classic Minecraft milestones", icon="minecraft:iron_pickaxe",
    quests=[
        Q("wood", "Punch a tree", items=[("minecraft:oak_log", 16)], xp=10, d=[
            "Any log works for crafting, but this quest wants oak. FallingTree lets you chop the whole tree at once - just break the bottom log."]),
        Q("table", "Crafting", dep=["wood"], items=[("minecraft:crafting_table", 1)], xp=10),
        Q("stone", "Stone age", dep=["table"], items=[("minecraft:stone_pickaxe", 1)], xp=10),
        Q("furnace", "Smelting", dep=["stone"], items=[("minecraft:furnace", 1)], xp=10),
        Q("iron", "Iron age", dep=["furnace"], items=[("minecraft:iron_ingot", 16)], xp=20),
        Q("ironpick", "A real pickaxe", dep=["iron"], items=[("minecraft:iron_pickaxe", 1)], xp=20),
        Q("armor", "Suit up", dep=["iron"], items=[("minecraft:iron_chestplate", 1)], xp=20),
        Q("bed", "Sweet dreams", dep=["wood"], items=[("minecraft:white_bed", 1)], xp=10, d=[
            "Any color will do in-game, but the quest checks for a white bed."]),
        Q("diamond", "Diamonds!", dep=["ironpick"], items=[("minecraft:diamond", 3)], xp=40),
        Q("enchant", "Magic table", dep=["diamond"], items=[("minecraft:enchanting_table", 1)], xp=40, d=[
            "Surround it with bookshelves for better enchantments."]),
        Q("anvil", "Repairs", dep=["iron"], items=[("minecraft:anvil", 1)], xp=20),
        Q("nether", "Into the Nether", dep=["diamond"], tasks=[dim("minecraft:the_nether")], icon="minecraft:obsidian", xp=50, d=[
            "Build a portal from obsidian and light it. The Nether has its own chapter."]),
        Q("village", "Neighbours", dep=["bed"], tasks=[check()], icon="minecraft:emerald", xp=20, d=[
            "Find a village - with this pack they can be much bigger and have waystones, taverns and new professions."]),
        Q("trade", "Let's make a deal", dep=["village"], items=[("minecraft:emerald", 10)], xp=20),
    ],
)
