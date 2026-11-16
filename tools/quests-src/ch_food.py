from engine import Q, check, auto

FARMERS = dict(
    key="farmers_delight", group="food", title="Farmer's Delight",
    subtitle="Real cooking", icon="farmersdelight:cooking_pot",
    quests=[
        Q("knife", "A knife", items=[("farmersdelight:flint_knife", 1)], xp=10, d=[
            "&bFarmer's Delight&r is the base of most food mods here. Knives harvest straw from grass and cut food on a cutting board."]),
        Q("board", "Cutting Board", dep=["knife"], items=[("farmersdelight:cutting_board", 1)], xp=15, d=[
            "Place an item on it and right-click with a knife (or axe / pickaxe for other recipes)."]),
        Q("wild", "Wild crops", items=[("farmersdelight:cabbage", 1), ("farmersdelight:tomato", 1), ("farmersdelight:onion", 1)], xp=20, d=[
            "Wild cabbages, tomatoes and onions grow in the world. Break them for seeds."]),
        Q("rice", "Rice", dep=["wild"], items=[("farmersdelight:rice", 4)], xp=15, d=[
            "Wild rice grows in shallow water in swamps and jungles. Plant it in water."]),
        Q("stove", "Stove", dep=["board"], items=[("farmersdelight:stove", 1)], xp=20, d=[
            "A heat source for the cooking pot and skillet. A campfire also works."]),
        Q("pot", "Cooking Pot", dep=["stove"], items=[("farmersdelight:cooking_pot", 1)], xp=25, d=[
            "Soups, stews and meals. Put the ingredients in, keep it heated and wait. Meals need a bowl."]),
        Q("skillet", "Skillet", dep=["stove"], items=[("farmersdelight:skillet", 1)], xp=20),
        Q("stew", "First stew", dep=["pot"], items=[("farmersdelight:beef_stew", 1)], xp=20, d=[
            "Meals give the &eNourishment&r (no hunger loss while healing) or &eComfort&r effect."]),
        Q("salad", "Mixed Salad", dep=["pot", "wild"], items=[("farmersdelight:mixed_salad", 1)], xp=20),
        Q("burger", "Hamburger", dep=["board", "wild"], items=[("farmersdelight:hamburger", 1)], xp=20),
        Q("feast", "A feast", dep=["stew"], items=[("farmersdelight:roast_chicken_block", 1)], xp=40, d=[
            "Feasts are placed as a block and served with bowls - one meal for the whole team."]),
        Q("compost", "Rich Soil", dep=["wild"], items=[("farmersdelight:organic_compost", 1), ("farmersdelight:rich_soil", 4)], xp=30, d=[
            "Rich soil makes mushrooms grow into colonies and boosts crops."]),
        Q("dogfood", "Dog Food", dep=["pot"], items=[("farmersdelight:dog_food", 1)], xp=20, d=[
            "Feed it to your dog for a big buff."]),
    ],
)

DELIGHTS = dict(
    key="delight_addons", group="food", title="More Delights",
    subtitle="Farmer's Delight addons", icon="culturaldelights:avocado",
    quests=[
        Q("start", "Even more food", icon="farmersdelight:iron_knife", tasks=[auto()], xp=10, d=[
            "These addons extend Farmer's Delight with new crops, drinks and dishes.",
            "Remember &bSpice of Life&r - every new food you eat gives you more max health!"]),
        Q("cultural", "Cultural Delights", dep=["start"], items=[("culturaldelights:avocado", 1), ("culturaldelights:cucumber", 1), ("culturaldelights:eggplant", 1)], xp=25, d=[
            "Avocados grow on trees; cucumbers, eggplants and corn grow wild."]),
        Q("corn", "Corn Delight", dep=["start"], items=[("corn_delight:corn", 4), ("corn_delight:popcorn", 1)], xp=25),
        Q("taco", "Taco night", dep=["corn"], items=[("corn_delight:taco", 1)], xp=25),
        Q("expanded", "Expanded Delight", dep=["start"], items=[("expandeddelight:juicer", 1), ("expandeddelight:cinnamon", 1)], xp=25, d=[
            "Juicer, cheese casks, cinnamon, peanuts, chili peppers and more."]),
        Q("cheese", "Cheese!", dep=["expanded"], items=[("expandeddelight:cheese_wheel", 1)], xp=30, d=[
            "Milk in a cask slowly turns into cheese."]),
        Q("miners", "Miner's Delight", dep=["start"], items=[("minersdelight:copper_pot", 1)], xp=25, d=[
            "Cave food - bat wings, squid, cave carrots. The copper pot cooks in a cup."]),
        Q("oceans", "Ocean's Delight", dep=["start"], items=[("oceansdelight:fugu_roll", 1)], xp=30),
        Q("rustic", "Rustic Delight", dep=["start"], items=[("rusticdelight:cotton_boll", 1)], xp=25),
        Q("respite", "Farmer's Respite", dep=["start"], items=[("farmersrespite:kettle", 1), ("farmersrespite:green_tea", 1)], xp=30, d=[
            "Tea and coffee from a kettle - drinks with nice buffs."]),
        Q("bnc", "Brewin' and Chewin'", dep=["start"], items=[("brewinandchewin:keg", 1)], xp=30, d=[
            "Ferment drinks and age cheese in a keg."]),
        Q("pizza", "Pizza party", dep=["bnc"], items=[("brewinandchewin:pizza", 1)], xp=30),
        Q("nether", "My Nether's Delight", dep=["start"], items=[("mynethersdelight:hoglin_loin", 1)], xp=30),
        Q("end", "End's Delight", dep=["start"], items=[("ends_delight:end_stove", 1)], xp=40, d=[
            "Cook dragon, shulker and chorus food in the End."]),
        Q("enders", "Ender's Delight", dep=["end"], items=[("endersdelight:endstone_stove", 1)], xp=40),
        Q("twilight", "Twilight's Flavor & Delight", dep=["start"], items=[("twilightdelight:maze_stove", 1)], xp=40),
        Q("fruits", "Fruits Delight", dep=["start"], items=[("fruitsdelight:pineapple", 1), ("fruitsdelight:lemon", 1)], xp=25),
        Q("extra", "ExtraDelight", dep=["start"], items=[("extradelight:mixing_bowl", 1), ("extradelight:oven", 1)], xp=30, d=[
            "Mixing bowl, oven, mortar and many more kitchen machines."]),
    ],
)

LETSDO = dict(
    key="lets_do", group="food", title="[Let's Do] Collection",
    subtitle="Farm & Charm, Vinery, Bakery, Brewery, Meadow...", icon="vinery:wine_bottle",
    quests=[
        Q("farm", "Farm & Charm", items=[("farm_and_charm:crafting_bowl", 1), ("farm_and_charm:cutting_board", 1)], xp=20, d=[
            "The base of the &bLet's Do&r mods: new crops (barley, oat, corn, lettuce, strawberry) and a cozy kitchen."]),
        Q("fcrops", "Barley & Oats", dep=["farm"], items=[("farm_and_charm:barley", 4), ("farm_and_charm:oat", 4)], xp=15),
        Q("fstove", "Stove & Cooking Pot", dep=["farm"], items=[("farm_and_charm:stove", 1), ("farm_and_charm:cooking_pot", 1)], xp=25),
        Q("mincer", "Mincer & Roaster", dep=["fstove"], items=[("farm_and_charm:mincer", 1), ("farm_and_charm:roaster", 1)], xp=25),
        Q("breakfast", "Farmer's Breakfast", dep=["fstove"], items=[("farm_and_charm:farmers_breakfast", 1)], xp=25),
        Q("animals", "Animal care", dep=["farm"], items=[("farm_and_charm:feeding_trough", 1), ("farm_and_charm:chicken_coop", 1)], xp=20, d=[
            "Troughs feed animals automatically, chicken coops collect eggs."]),
        Q("press", "Vinery", dep=["farm"], items=[("vinery:apple_press", 1)], xp=25, d=[
            "&bVinery&r: grapes grow wild in many biomes (red and white, with biome variants). Plant the seeds next to a grapevine stem.",
            "The apple press turns grapes and apples into juice."]),
        Q("barrel", "Fermentation", dep=["press"], items=[("vinery:fermentation_barrel", 1)], xp=30, d=[
            "Juice + time in a fermentation barrel = wine. Each wine gives a different effect."]),
        Q("wine", "Your first wine", dep=["barrel"], items=[("vinery:wine_bottle", 1)], xp=30),
        Q("bakery", "Bakery", dep=["farm"], items=[("bakery:baker_station", 1), ("bakery:rolling_pin", 1)], xp=25, d=[
            "Bread, cakes, tarts and jams."]),
        Q("cake", "A real cake", dep=["bakery"], items=[("bakery:strawberry_cake", 1)], xp=30),
        Q("brewery", "Brewery", dep=["farm"], items=[("brewery:wooden_brewingstation", 1), ("brewery:hops", 4)], xp=30, d=[
            "Build a brewing station multiblock and brew beer and whiskey."]),
        Q("beer", "Cheers!", dep=["brewery"], items=[("brewery:beer_wheat", 1)], xp=30),
        Q("candlelight", "Candlelight", dep=["fstove"], items=[("candlelight:cooking_pan", 1), ("candlelight:plate", 1)], xp=25, d=[
            "Fine dining: plated meals, furniture and decorations for a restaurant."]),
        Q("lasagne", "Lasagne", dep=["candlelight"], items=[("candlelight:lasagne", 1)], xp=30),
        Q("meadow", "Meadow", dep=["farm"], items=[("meadow:cheese_form", 1), ("meadow:cookpot", 1)], xp=25, d=[
            "Alpine life: cheese making, buffalo and water buffalo, wooden cauldrons."]),
        Q("meadowcheese", "Cheese wheel", dep=["meadow"], items=[("meadow:cheese_wheel", 1)], xp=30),
        Q("beach", "Beachparty", dep=["farm"], items=[("beachparty:coconut", 2), ("beachparty:palm_bar", 1)], xp=25, d=[
            "Palm trees, coconuts and cocktails. Find palm beaches."]),
        Q("cocktail", "Cocktail", dep=["beach"], items=[("beachparty:coconut_cocktail", 1)], xp=25),
        Q("herbal", "HerbalBrews", dep=["farm"], items=[("herbalbrews:tea_kettle", 1), ("herbalbrews:green_tea_leaf", 4)], xp=25),
        Q("tea", "A cup of tea", dep=["herbal"], items=[("herbalbrews:green_tea", 1)], xp=25),
        Q("coffee", "Coffee", dep=["herbal"], items=[("herbalbrews:coffee", 1)], xp=25),
    ],
)

CREATEFOOD = dict(
    key="create_food", group="food", title="Create Kitchen",
    subtitle="Automate your food", icon="sliceanddice:slicer",
    quests=[
        Q("start", "Food meets machines", icon="create:mechanical_mixer", tasks=[auto()], xp=10, d=[
            "&bCreate: Central Kitchen&r lets Create machines make Farmer's Delight food: the mixer cooks, the deployer cuts, the spout fills.",
            "&bCreate Food&r, &bConfectionery&r, &bCafe&r and &bWinery&r add hundreds of recipes made only with Create machines."]),
        Q("dough", "Dough", dep=["start"], items=[("create:dough", 8)], xp=15, d=[
            "Flour (millstone) + water in a mixer."]),
        Q("chocolate", "Chocolate", dep=["start"], items=[("create:bar_of_chocolate", 4)], xp=20),
        Q("confectionery", "Confectionery", dep=["chocolate"], items=[("create_confectionery:marshmallow", 4), ("create_confectionery:bar_of_caramel", 1)], xp=25),
        Q("hotchoc", "Hot chocolate", dep=["confectionery"], items=[("create_confectionery:hot_chocolate_bottle", 1)], xp=25),
        Q("createfood", "Create Food", dep=["dough"], items=[("createfood:piping_bag", 1)], xp=25, d=[
            "Pizzas, cakes, donuts, ice cream... JEI lists all of them under Create Food."]),
        Q("cafe", "Create Cafe", dep=["start"], items=[("createcafe:coffee_bucket", 1)], xp=30, d=[
            "Bubble tea, coffee and syrups."]),
        Q("winery", "Create Winery", dep=["start"], items=[("create_winery:wine_cellar", 1)], xp=30),
        Q("slicer", "Slice & Dice", dep=["start"], items=[("sliceanddice:slicer", 1)], xp=25),
        Q("sprinkler", "Sprinkler", dep=["slicer"], items=[("sliceanddice:sprinkler", 1)], xp=20, d=[
            "Fill it with water through pipes to water crops - faster growth."]),
        Q("diet", "Food variety", dep=["start"], items=[("solonion:lunchbag", 1)], xp=30, d=[
            "The more different foods you eat, the more hearts you get. Automate a menu!"]),
    ],
)

PAMS = dict(
    key="pams", group="food", title="Pam's HarvestCraft",
    subtitle="Hundreds of crops and trees", icon="pamhc2foodcore:potitem",
    quests=[
        Q("tools", "Kitchen tools", items=[("pamhc2foodcore:cuttingboarditem", 1), ("pamhc2foodcore:potitem", 1), ("pamhc2foodcore:skilletitem", 1)], xp=20, d=[
            "&bPam's HarvestCraft 2&r crops come from wild gardens and fruit trees in matching biomes.",
            "Its recipes use kitchen tools that stay in the crafting grid."]),
        Q("tools2", "More tools", dep=["tools"], items=[("pamhc2foodcore:saucepanitem", 1), ("pamhc2foodcore:mixingbowlitem", 1), ("pamhc2foodcore:bakewareitem", 1), ("pamhc2foodcore:juiceritem", 1), ("pamhc2foodcore:grinderitem", 1)], xp=30),
        Q("pie", "Pot pie", dep=["tools2"], items=[("pamhc2foodcore:chickenpotpieitem", 1)], xp=25),
        Q("roast", "Pot roast", dep=["tools2"], items=[("pamhc2foodcore:potroastitem", 1)], xp=25),
    ],
)

FISHING = dict(
    key="fishing", group="food", title="Fishing",
    subtitle="Aquaculture, Fish of Thieves and more", icon="aquaculture:iron_fishing_rod",
    quests=[
        Q("rod", "Better rods", items=[("aquaculture:iron_fishing_rod", 1)], xp=15, d=[
            "&bAquaculture 2&r: new rods, hooks, bait and dozens of fish depending on biome."]),
        Q("tackle", "Tackle box", dep=["rod"], items=[("aquaculture:tackle_box", 1)], xp=15, d=[
            "Stores hooks, bait and fishing line. Hooks change how the rod behaves."]),
        Q("worm", "Bait", dep=["rod"], items=[("aquaculture:worm", 4)], xp=10, d=[
            "Worms come from breaking dirt and grass. Put bait in the rod's GUI."]),
        Q("knife", "Fish fillets", dep=["rod"], items=[("aquaculture:fish_fillet_raw", 4)], xp=15, d=[
            "Fillet any fish with a fillet knife. &bAquaculture&r fish depend on the biome, &bFish of Thieves&r adds Sea of Thieves fish with variants by time and weather."]),
        Q("sushi", "Sushi", dep=["knife"], items=[("aquaculture:sushi", 1)], xp=20),
        Q("treasure", "Treasure", dep=["rod"], items=[("aquaculture:treasure_chest", 1)], xp=40, d=[
            "Sometimes the rod pulls up a lockbox or treasure chest."]),
        Q("neptunium", "Neptunium", dep=["treasure"], items=[("aquaculture:neptunium_ingot", 1)], xp=60, d=[
            "A rare metal from treasure - makes great tools."]),
        Q("unusual", "Unusual fish", dep=["rod"], items=[("unusualfishmod:lobster_roll", 1)], xp=30, d=[
            "&bUnusual Fish Mod&r adds strange sea creatures - some are dangerous, some taste great."]),
        Q("driftwood", "Upgrade Aquatic", dep=["rod"], items=[("upgrade_aquatic:driftwood", 4)], xp=15, d=[
            "&bUpgrade Aquatic&r adds new ocean life, corals, jellyfish and driftwood washed up on beaches."]),
        Q("tank", "Fish tank", dep=["rod"], items=[("betterfishtanks:glass_container", 1)], xp=20),
        Q("aquadelight", "Aquaculture Delight", dep=["knife"], items=[("aquaculturedelight:fish_and_chips", 1)], xp=20),
        Q("splashtail", "Fish of Thieves", dep=["rod"], items=[("fishofthieves:splashtail", 1)], xp=15, d=[
            "&bFish of Thieves&r adds the fish from Sea of Thieves. Each species has several colour variants that depend on the biome, time and weather."]),
        Q("stormfish", "Stormfish", dep=["splashtail"], items=[("fishofthieves:stormfish", 1)], xp=40, d=[
            "Only bites during a thunderstorm. Grab your rod when the sky goes dark."]),
        Q("wrecker", "Wrecker", dep=["splashtail"], items=[("fishofthieves:wrecker", 1)], xp=40, d=[
            "Wreckers live around shipwrecks and ocean ruins. Fish near a wreck to find one."]),
    ],
)
