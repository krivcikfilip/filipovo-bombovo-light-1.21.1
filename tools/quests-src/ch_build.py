from engine import Q, check, auto

COLONIES = dict(
    key="minecolonies", group="build", title="MineColonies",
    subtitle="Found a town that builds itself", icon="minecolonies:blockhuttownhall",
    quests=[
        Q("camp", "Supply Camp", items=[("minecolonies:supplycampdeployer", 1)], xp=30, d=[
            "&bMineColonies&r: you are the mayor, your citizens do the work.",
            "Start with a &esupply camp&r (on land) or a &esupply ship&r (on water). Right-click to preview, rotate it and confirm.",
            "It gives you a chest with starting supplies, including the town hall."]),
        Q("townhall", "Town Hall", dep=["camp"], items=[("minecolonies:blockhuttownhall", 1)], xp=40, d=[
            "Placing the town hall founds your colony. Pick a style (Stylecolonies and others add many).",
            "The colony claims land around it. Friends can be added as officers in the town hall GUI."]),
        Q("buildtool", "Build Tool", dep=["camp"], items=[("structurize:sceptergold", 1)], xp=20, d=[
            "The build tool places every hut. Choose the building, its style and level, then confirm."]),
        Q("builder", "Builder's Hut", dep=["townhall", "buildtool"], items=[("minecolonies:blockhutbuilder", 1)], xp=40, d=[
            "Your first and most important worker. The builder builds and upgrades everything.",
            "He asks for materials in his hut GUI - give them to him or put them in the warehouse.",
            "The &eclipboard&r shows everything your citizens are waiting for."]),
        Q("resscroll", "Resource Scroll", dep=["builder"], items=[("minecolonies:resourcescroll", 1)], xp=15, d=[
            "Shows what materials the builder still needs for his current job."]),
        Q("houses", "Homes", dep=["builder"], items=[("minecolonies:blockhutcitizen", 2)], xp=30, d=[
            "Citizens need beds. Each residence level adds more room."]),
        Q("food", "Feed the town", dep=["builder"], items=[("minecolonies:blockhutcook", 1)], xp=40, d=[
            "Hungry citizens work slowly. A restaurant with a cook keeps everyone fed."]),
        Q("farmer", "Farmer", dep=["food"], items=[("minecolonies:blockhutfarmer", 1), ("minecolonies:blockhutfield", 1)], xp=40, d=[
            "Place field blocks, assign seeds and the farmer takes care of the crops."]),
        Q("fisher", "Fisherman", dep=["food"], items=[("minecolonies:blockhutfisherman", 1)], xp=30),
        Q("courier", "Courier", dep=["builder"], items=[("minecolonies:blockhutdeliveryman", 1)], xp=40, d=[
            "Couriers carry items between huts and the warehouse."]),
        Q("warehouse", "Warehouse", dep=["courier"], items=[("minecolonies:blockhutwarehouse", 1)], xp=60, d=[
            "The colony's central storage. Put materials here and couriers deliver them where needed."]),
        Q("lumber", "Forester", dep=["builder"], items=[("minecolonies:blockhutlumberjack", 1)], xp=30),
        Q("miner", "Miner", dep=["builder"], items=[("minecolonies:blockhutminer", 1)], xp=40, d=[
            "Builds a mineshaft and mines ores for you."]),
        Q("guards", "Guard Tower", dep=["builder"], items=[("minecolonies:blockhutguardtower", 1)], xp=40, d=[
            "Guards protect citizens at night and fight off raids. Barracks hold many guards later."]),
        Q("barracks", "Barracks", dep=["guards"], items=[("minecolonies:blockhutbarracks", 1)], xp=60),
        Q("smith", "Blacksmith", dep=["miner"], items=[("minecolonies:blockhutblacksmith", 1)], xp=40),
        Q("sawmill", "Sawmill", dep=["lumber"], items=[("minecolonies:blockhutsawmill", 1)], xp=30),
        Q("stonemason", "Stonemason", dep=["miner"], items=[("minecolonies:blockhutstonemason", 1)], xp=30),
        Q("tavern", "Tavern", dep=["houses"], items=[("minecolonies:blockhuttavern", 1)], xp=40, d=[
            "Visitors arrive at the tavern. Hire them with items - they often have great skills."]),
        Q("school", "School", dep=["houses"], items=[("minecolonies:blockhutschool", 1)], xp=40),
        Q("university", "University", dep=["school"], items=[("minecolonies:blockhutuniversity", 1)], xp=80, d=[
            "Research unlocks new buildings, better workers and colony bonuses."]),
        Q("hospital", "Hospital", dep=["houses"], items=[("minecolonies:blockhuthospital", 1)], xp=40),
        Q("goggles", "Build Goggles", dep=["builder"], items=[("minecolonies:build_goggles", 1)], xp=20, d=[
            "Show building outlines and the work orders of builders."]),
    ],
)

BUILDING = dict(
    key="building", group="build", title="Building & Decoration",
    subtitle="Make it beautiful", icon="mcwroofs:oak_roof",
    quests=[
        Q("start", "Builder's paradise", icon="minecraft:bricks", tasks=[auto()], xp=10, d=[
            "This pack has a huge amount of decoration. Here are the main tools to find it all."]),
        Q("chipped", "Chipped", dep=["start"], items=[("chipped:botanist_workbench", 1), ("chipped:mason_table", 1), ("chipped:carpenters_table", 1)], xp=20, d=[
            "Chipped workbenches turn one block into dozens of variants."]),
        Q("rechiseled", "Rechiseled", dep=["start"], items=[("rechiseled:chisel", 1)], xp=15, d=[
            "Put blocks in the chisel to pick a different pattern. Many variants connect into larger textures."]),
        Q("macaw", "Macaw's mods", dep=["start"], items=[("mcwwindows:hammer", 1)], xp=20, d=[
            "Roofs, windows, doors, fences, bridges, lights, furniture - in every wood and stone type. The hammer changes the shape of placed Macaw's blocks."]),
        Q("handcrafted", "Handcrafted", dep=["start"], items=[("handcrafted:hammer", 1)], xp=20, d=[
            "Furniture in every wood type that you can sit on. The hammer changes shapes and colours."]),
        Q("refurbished", "Furniture: Refurbished", dep=["start"], items=[("refurbished_furniture:workbench", 1)], xp=20, d=[
            "MrCrayfish's furniture - working fridges, stoves, TVs, mailboxes and more. Everything is crafted in the workbench."]),
        Q("domum", "Architect's Cutter", dep=["start"], items=[("domum_ornamentum:architectscutter", 1)], xp=20, d=[
            "Domum Ornamentum combines two blocks into one textured block - used by many MineColonies styles."]),
        Q("supp", "Supplementaries", dep=["start"], items=[("supplementaries:rope", 8), ("supplementaries:sack", 1), ("supplementaries:jar", 1)], xp=20, d=[
            "Lots of small useful blocks: ropes, sacks, jars, globes, signposts, pedestals..."]),
        Q("createdeco", "Create Deco", dep=["start"], items=[("createdeco:industrial_iron_ingot", 4)], xp=15, d=[
            "Industrial decoration: lamps, catwalks, bars and metal sheets. Industrial iron is its main material."]),
        Q("etched", "Make your own music", dep=["start"], items=[("etched:etching_table", 1)], xp=25, d=[
            "&bEtched&r lets you burn your own songs onto music discs and play them for everyone on the server."]),
        Q("paintings", "Your own paintings", dep=["start"], items=[("immersive_paintings:painting", 1)], xp=15, d=[
            "&bImmersive Paintings&r lets you upload any image and hang it on the wall."]),
    ],
)
