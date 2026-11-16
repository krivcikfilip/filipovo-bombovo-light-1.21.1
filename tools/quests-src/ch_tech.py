from engine import Q, check, auto

CREATE = dict(
    key="create", group="tech", title="Create: The Basics",
    subtitle="Gears, belts and contraptions", icon="create:cogwheel",
    quests=[
        Q("alloy", "Andesite Alloy", items=[("create:andesite_alloy", 8)], xp=20, d=[
            "The heart of early Create. Mix andesite with iron nuggets (or zinc nuggets) in a crafting table.",
            "Almost every Create item has a &eponder&r scene - an animated tutorial shown from its tooltip."]),
        Q("shaft", "Shafts & Cogs", dep=["alloy"], items=[("create:shaft", 4), ("create:cogwheel", 2), ("create:large_cogwheel", 1)], xp=20, d=[
            "&eRotation&r is Create's power. Shafts carry it in a straight line, cogwheels carry it sideways.",
            "Small cog to large cog changes the speed - faster or slower."]),
        Q("wheel", "Water Wheel", dep=["shaft"], items=[("create:water_wheel", 1)], xp=25, d=[
            "Your first power source. Place it in flowing water - more water on the blades means more power."]),
        Q("goggles", "See the stress", dep=["wheel"], items=[("create:goggles", 1)], xp=20, d=[
            "Engineer's goggles show speed and &estress&r. Every machine uses stress units (SU); sources provide capacity.",
            "If a network is overstressed, everything stops."]),
        Q("wrench", "The Wrench", dep=["shaft"], items=[("create:wrench", 1)], xp=15, d=[
            "Rotate blocks with right-click, pick them up with shift + right-click."]),
        Q("millstone", "Millstone", dep=["wheel"], items=[("create:millstone", 1)], xp=20, d=[
            "Grinds items: gravel to flint, wheat to flour, flowers to dye. Feed it from the top."]),
        Q("press", "Mechanical Press", dep=["wheel"], items=[("create:mechanical_press", 1)], xp=25, d=[
            "Presses ingots into &esheets&r. Put a depot or belt under it."]),
        Q("sheets", "Iron Sheets", dep=["press"], items=[("create:iron_sheet", 8)], xp=20),
        Q("belt", "Conveyor Belts", dep=["wheel"], items=[("create:belt_connector", 4)], xp=20, d=[
            "Right-click two shafts with a belt to connect them. Belts move items and also carry rotation."]),
        Q("fan", "Encased Fan", dep=["belt"], items=[("create:encased_fan", 1)], xp=25, d=[
            "Blows items along. Put &elava&r behind it to smelt, &efire&r to smoke, &ewater&r to wash and &esoul fire&r to haunt.",
            "Bulk processing on a belt is one of Create's best tricks."]),
        Q("washing", "Wash some gravel", dep=["fan"], items=[("minecraft:iron_nugget", 16)], xp=20, d=[
            "Wash crushed ores or gravel with a fan through water for extra nuggets."]),
        Q("mixer", "Mixer & Basin", dep=["press"], items=[("create:mechanical_mixer", 1), ("create:basin", 1)], xp=30, d=[
            "A mixer above a basin makes alloys, doughs and shapeless recipes in bulk."]),
        Q("zinc", "Zinc", dep=["alloy"], items=[("create:raw_zinc", 8)], xp=20, d=[
            "Zinc ore generates in the overworld, often in large veins."]),
        Q("brass", "Brass", dep=["mixer", "zinc"], items=[("create:brass_ingot", 8)], xp=40, d=[
            "Copper + zinc in a heated basin (blaze burner, or a lit fire below) makes brass."]),
        Q("burner", "Blaze Burner", dep=["mixer"], items=[("create:blaze_burner", 1)], xp=40, d=[
            "Catch a blaze with an empty blaze burner. Feed it fuel to heat basins. Blaze cakes make it superheated."]),
        Q("casing", "Casings", dep=["alloy"], items=[("create:andesite_casing", 8)], xp=15, d=[
            "Apply andesite alloy to stripped logs to make casings - they are the base of many machines."]),
        Q("drill", "Drill & Saw", dep=["casing"], items=[("create:mechanical_drill", 1), ("create:mechanical_saw", 1)], xp=25, d=[
            "Machines that break blocks or cut trees. Put them on a contraption to make them move."]),
        Q("bearing", "Contraptions", dep=["drill"], items=[("create:mechanical_bearing", 1), ("create:super_glue", 1)], xp=30, d=[
            "A bearing or piston moves a whole structure. Glue blocks together with super glue.",
            "Windmills are a bearing + sails - great free power."]),
        Q("windmill", "Windmill", dep=["bearing"], items=[("create:windmill_bearing", 1), ("create:white_sail", 8)], xp=30),
        Q("harvester", "Automatic farming", dep=["bearing"], items=[("create:mechanical_harvester", 2)], xp=30, d=[
            "Harvesters on a moving contraption harvest crops and replant them."]),
        Q("deployer", "Deployer", dep=["brass"], items=[("create:deployer", 1)], xp=40, d=[
            "A robotic hand. It can use, place and click - needed for many sequenced recipes."]),
        Q("precision", "Precision Mechanism", dep=["deployer"], items=[("create:precision_mechanism", 1)], xp=60, d=[
            "A &esequenced assembly&r: press, deploy and deploy again on a belt. JEI shows the steps."]),
        Q("tube", "Electron Tube", dep=["brass"], items=[("create:electron_tube", 4)], xp=30),
        Q("arm", "Mechanical Arm", dep=["precision"], items=[("create:mechanical_arm", 1)], xp=50, d=[
            "Moves items between inputs and outputs. Right-click blocks with the arm in hand before placing to set targets."]),
        Q("fluids", "Fluids", dep=["casing"], items=[("create:fluid_pipe", 8), ("create:mechanical_pump", 1), ("create:fluid_tank", 2)], xp=30, d=[
            "Pumps move fluids through pipes. Tanks merge when you place them next to each other."]),
        Q("spout", "Spout", dep=["fluids"], items=[("create:spout", 1)], xp=30, d=[
            "Fills items on a belt or depot: water bottles, honey bottles and lots of food recipes."]),
        Q("steam", "Steam Engine", dep=["burner", "fluids"], items=[("create:steam_engine", 1)], xp=60, d=[
            "A steam engine on top of a fluid tank with water and blaze burners below it gives a lot of stress capacity.",
            "Bigger boilers and more burners give more power."]),
        Q("crafter", "Mechanical Crafter", dep=["precision"], items=[("create:mechanical_crafter", 9)], xp=50, d=[
            "Big automated crafting grids. Needed for some large recipes."]),
        Q("crushing", "Crushing Wheels", dep=["steam"], items=[("create:crushing_wheel", 2)], xp=60, d=[
            "Ore through crushing wheels gives &ecrushed ore&r plus bonus outputs - more ingots per ore."]),
        Q("vault", "Item Vault", dep=["brass"], items=[("create:item_vault", 1)], xp=30),
        Q("backtank", "Diving gear", dep=["brass"], items=[("create:copper_backtank", 1)], xp=40, d=[
            "The backtank stores air for underwater work and powers tools like the extendo grip."]),
        Q("jetpack", "Fly with Create", dep=["backtank"], items=[("create_jetpack:jetpack", 1)], xp=80, d=[
            "&bCreate Jetpack&r uses the air stored in a backtank. It has a normal and a hover mode."]),
    ],
)

CREATE_ADDONS = dict(
    key="create_addons", group="tech", title="Create: Addons",
    subtitle="Electricity, cannons, oil and more", icon="createaddition:electric_motor",
    quests=[
        Q("start", "More Create", s="Finish the basics first", icon="create:brass_ingot", tasks=[auto()], xp=10, d=[
            "This pack has many Create addons. Each branch here introduces one of them."]),
        Q("wire", "Copper wire", dep=["start"], items=[("createaddition:copper_wire", 8), ("createaddition:rolling_mill", 1)], xp=25, d=[
            "&bCreate Crafts & Additions&r brings electricity (FE). The rolling mill makes rods and wires."]),
        Q("alternator", "Rotation to power", dep=["wire"], items=[("createaddition:alternator", 1)], xp=40, d=[
            "The alternator turns rotation into FE energy for Mekanism, AE2 or Refined Storage."]),
        Q("motor", "Power to rotation", dep=["wire"], items=[("createaddition:electric_motor", 1)], xp=40, d=[
            "The electric motor does the opposite - FE into rotation."]),
        Q("accumulator", "Store energy", dep=["alternator"], items=[("createaddition:modular_accumulator", 2)], xp=30),
        Q("tesla", "Tesla Coil", dep=["accumulator"], items=[("createaddition:tesla_coil", 1)], xp=30, d=[
            "Charges items and can be used for 'charging' recipes."]),
        Q("diesel", "Diesel power", dep=["start"], items=[("createdieselgenerators:diesel_engine", 1)], xp=40, d=[
            "&bCreate Diesel Generators&r - engines that burn fuel for strong, compact rotation."]),
        Q("oil", "Find oil", dep=["diesel"], items=[("createdieselgenerators:oil_scanner", 1)], xp=30, d=[
            "Scan for oil chunks, then pump crude oil out with a pumpjack."]),
        Q("pumpjack", "Pumpjack", dep=["oil"], items=[("createdieselgenerators:pumpjack_crank", 1), ("createdieselgenerators:pumpjack_head", 1), ("createdieselgenerators:pumpjack_bearing", 1)], xp=50),
        Q("distill", "Distillation", dep=["pumpjack"], items=[("createdieselgenerators:distillation_controller", 1)], xp=60, d=[
            "Refine crude oil into diesel and gasoline in a distillation tower."]),
        Q("big_diesel", "Bigger engines", dep=["distill"], items=[("createdieselgenerators:large_diesel_engine", 1)], xp=60),
        Q("newage", "Create: New Age", dep=["start"], items=[("create_new_age:generator_coil", 1), ("create_new_age:carbon_brushes", 1)], xp=40, d=[
            "Another electricity addon with magnets, generators and motors."]),
        Q("energiser", "Energiser", dep=["newage"], items=[("create_new_age:basic_energiser", 1)], xp=40, d=[
            "Overcharges metals using electricity."]),
        Q("reactor", "Nuclear!", dep=["energiser"], items=[("create_new_age:reactor_casing", 8), ("create_new_age:reactor_rod", 1)], xp=80, d=[
            "A thorium reactor that heats boilers. Read the ponder carefully - it can melt down."]),
        Q("cei", "Liquid experience", dep=["start"], items=[("create_enchantment_industry:mechanical_grindstone", 1), ("create_enchantment_industry:experience_hatch", 1)], xp=40, d=[
            "&bCreate Enchantment Industry&r turns XP into a fluid you can pump and store."]),
        Q("enchanter", "Blaze Enchanter", dep=["cei"], items=[("create_enchantment_industry:blaze_enchanter", 1)], xp=60, d=[
            "Automatic enchanting with liquid experience and enchanting templates."]),
        Q("printer", "Printer", dep=["cei"], items=[("create_enchantment_industry:printer", 1)], xp=40, d=[
            "Copies written books, enchanted books and name tags."]),
        Q("cannon", "Big Cannons", dep=["start"], items=[("createbigcannons:cannon_mount", 1)], xp=40, d=[
            "&bCreate Big Cannons&r - build cannons from barrels, chambers and a breech on a mount."]),
        Q("shot", "Ammunition", dep=["cannon"], items=[("createbigcannons:solid_shot", 4), ("createbigcannons:powder_charge", 4)], xp=40),
        Q("slicer", "Slice & Dice", dep=["start"], items=[("sliceanddice:slicer", 1)], xp=30, d=[
            "Automates Farmer's Delight cutting board recipes. The sprinkler waters crops."]),
        Q("excavation", "Endless ore", dep=["start"], items=[("createoreexcavation:vein_finder", 1), ("createoreexcavation:drilling_machine", 1)], xp=60, d=[
            "&bCreate Ore Excavation&r: find ore veins deep below and mine them forever with a drilling machine."]),
        Q("chunkload", "Contraption chunk loading", dep=["start"], items=[("create_power_loader:andesite_chunk_loader", 1)], xp=40, d=[
            "&bCreate Power Loader&r keeps chunks loaded while it is powered by rotation."]),
        Q("hypertube", "Hypertubes", dep=["start"], items=[("create_hypertube:hypertube", 16), ("create_hypertube:hypertube_entrance", 1)], xp=40, d=[
            "Pneumatic tubes that shoot players through them. Fast travel around your base."]),
        Q("teleporter", "Quantum teleporters", dep=["start"], items=[("createteleporters:teleporter", 1)], xp=60),
        Q("copycats", "Copycats", dep=["start"], items=[("create:copycat_panel", 4)], xp=15, d=[
            "Copycat blocks take the look of any block you click into them. &bCopycats+&r adds many more shapes."]),
        Q("sa_jetpack", "Brass jetpack", dep=["start"], items=[("create_sa:brass_jetpack_chestplate", 1)], xp=60, d=[
            "&bCreate Stuff & Additions&r: jetpacks, exoskeletons, drones, flamethrowers and metal tools."]),
        Q("sa_drone", "Drone", dep=["sa_jetpack"], items=[("create_sa:brass_drone_item", 1), ("create_sa:drone_controller", 1)], xp=60),
        Q("bnb", "Bits 'n' Bobs", dep=["start"], items=[("bits_n_bobs:large_nixie_tube", 1), ("bits_n_bobs:flywheel_bearing", 1)], xp=30, d=[
            "Nixie displays, flanged cogwheels, chain pulleys, lamps and industrial decoration."]),
        Q("connected", "Create: Connected", dep=["start"], items=[("create_connected:kinetic_battery", 1), ("create_connected:item_silo", 1)], xp=40, d=[
            "Extra kinetic parts: clutches, gearboxes, brakes, a kinetic battery that stores rotation and fan catalysts for new bulk-processing types."]),
        Q("dragons", "Dragons Plus", dep=["start"], items=[("create_dragons_plus:fluid_hatch", 1)], xp=30),
        Q("wolf", "Mechanical companion", dep=["start"], items=[("createmechanicalcompanion:mechanical_wolf_motherboard", 1)], xp=60, d=[
            "Build a mechanical wolf that follows you and can be upgraded with modules (radar, crossbow, light...)."]),
        Q("wrapped", "Create: Wrapped", dep=["start"], items=[("create_wrapped:wrapping_station", 1)], xp=20, d=[
            "Wrap items into gifts and make festive sweets."]),
        Q("trading", "Trading Floor", dep=["start"], items=[("trading_floor:trading_depot", 1)], xp=40, d=[
            "Put it in front of a villager and it trades automatically."]),
    ],
)

AERO = dict(
    key="aeronautics", group="tech", title="Create Aeronautics",
    subtitle="Build ships that really fly", icon="aeronautics:propeller_bearing",
    quests=[
        Q("start", "Physics!", s="Create Aeronautics + Simulated", icon="simulated:physics_assembler", tasks=[auto()], xp=10, d=[
            "&bCreate Aeronautics&r turns Create contraptions into real physical objects that fly, float and drive.",
            "You should know the Create basics first (shafts, bearings, glue).",
            "The server allows flight, so don't worry about being kicked while riding a ship."]),
        Q("assembler", "Physics Assembler", dep=["start"], items=[("simulated:physics_assembler", 1)], xp=40, d=[
            "Turns a glued structure into a &ephysics contraption&r. Everything glued to it moves together and has real weight."]),
        Q("levitite", "Levitite", dep=["start"], items=[("aeronautics:levitite", 8)], xp=40, d=[
            "A block that floats. Enough levitite and your ship lifts off without any engine.",
            "Pearlescent levitite is even stronger."]),
        Q("burner", "Hot air balloons", dep=["start"], items=[("aeronautics:adjustable_burner", 1)], xp=40, d=[
            "Envelope blocks (in every colour) form a balloon. The adjustable burner heats the air inside - control it with redstone to go up or down."]),
        Q("propeller", "Propellers", dep=["assembler"], items=[("aeronautics:propeller_bearing", 1), ("aeronautics:wooden_propeller", 1)], xp=40, d=[
            "A propeller bearing spins a propeller and pushes your ship. Faster rotation = more thrust."]),
        Q("smart_prop", "Smart Propeller", dep=["propeller"], items=[("aeronautics:smart_propeller", 1)], xp=60),
        Q("gyro", "Stay level", dep=["propeller"], items=[("aeronautics:gyroscopic_propeller_bearing", 1)], xp=60, d=[
            "A gyroscopic bearing keeps the ship stable and stops it from tipping over."]),
        Q("engine", "Portable Engine", dep=["assembler"], items=[("simulated:engine_assembly", 1)], xp=40, d=[
            "The engine assembly is the heart of the portable engine (it comes in all colours).",
            "A small engine that burns fuel and gives rotation on a moving ship."]),
        Q("steering", "Take the wheel", dep=["engine"], items=[("simulated:steering_wheel", 1), ("simulated:throttle_lever", 1)], xp=40, d=[
            "Steering wheel and throttle let you control your craft from the inside."]),
        Q("sensors", "Instruments", dep=["steering"], items=[("simulated:altitude_sensor", 1), ("simulated:velocity_sensor", 1)], xp=40, d=[
            "Sensors give redstone signals based on height or speed - autopilot material."]),
        Q("nav", "Navigation table", dep=["sensors"], items=[("simulated:navigation_table", 1)], xp=50),
        Q("rope", "Ropes & winches", dep=["assembler"], items=[("simulated:rope_winch", 1), ("simulated:rope_connector", 2)], xp=40, d=[
            "Hang cargo or tow things with ropes. &bClimbable Ropes&r lets you climb them."]),
        Q("dock", "Docking", dep=["rope"], items=[("simulated:docking_connector", 2)], xp=40, d=[
            "Docking connectors join two contraptions together or to the ground."]),
        Q("wheels", "Ground vehicles", dep=["assembler"], items=[("offroad:wheel_mount", 2), ("offroad:tire", 2)], xp=50, d=[
            "&bOffroad&r adds wheels and tires - build cars, trucks and rovers."]),
        Q("goggles", "Aviator's Goggles", dep=["propeller"], items=[("aeronautics:aviators_goggles", 1)], xp=30),
        Q("islands", "Sky islands", dep=["levitite"], items=[("aeroscapes:aerolite", 4)], xp=50, d=[
            "&bAero Islands&r adds floating islands in the sky. Fly up and explore them for aerolite and selenite."]),
        Q("cannon", "Armed airship", dep=["propeller"], items=[("aeronautics:mounted_potato_cannon", 1)], xp=40),
    ],
)

VEHICLES = dict(
    key="vehicles", group="tech", title="Planes & Ships",
    subtitle="Immersive Aircraft and Small Ships", icon="immersive_aircraft:biplane",
    quests=[
        Q("parts", "Aircraft parts", items=[("immersive_aircraft:hull", 4), ("immersive_aircraft:sail", 2)], xp=20, d=[
            "&bImmersive Aircraft&r - simple planes you craft as an item and place. Hull, sails and engines are the parts."]),
        Q("engine", "Engine & propeller", dep=["parts"], items=[("immersive_aircraft:engine", 1), ("immersive_aircraft:propeller", 1)], xp=25),
        Q("airship", "Airship", dep=["engine"], items=[("immersive_aircraft:airship", 1)], xp=40, d=[
            "Slow and steady. Put fuel (coal, wood) in its inventory."]),
        Q("cargo", "Cargo Airship", dep=["airship"], items=[("immersive_aircraft:cargo_airship", 1)], xp=50),
        Q("biplane", "Biplane", dep=["engine"], items=[("immersive_aircraft:biplane", 1)], xp=60, d=[
            "Fast but needs a runway to take off."]),
        Q("gyrodyne", "Gyrodyne", dep=["engine"], items=[("immersive_aircraft:gyrodyne", 1)], xp=40, d=[
            "Human-powered helicopter - pedal by pressing forward!"]),
        Q("quad", "Quadrocopter", dep=["engine"], items=[("immersive_aircraft:quadrocopter", 1)], xp=50),
        Q("upgrade", "Upgrades", dep=["biplane"], items=[("immersive_aircraft:enhanced_propeller", 1)], xp=40, d=[
            "Upgrades go into the aircraft's inventory: better propellers, engines, boilers and landing gear."]),
        Q("sails", "Sail away", items=[("smallships:cotton_sails", 1)], xp=40, d=[
            "&bSmall Ships&r - real sailing ships (cog, brigg, galley, drakkar and more) in every wood type.",
            "Wind direction and the sail matter; galleys and drakkars can also be rowed.",
            "Every ship needs sails - start here."]),
        Q("shipcannon", "Ship cannons", dep=["sails"], items=[("smallships:cannon", 1), ("smallships:cannon_ball", 8)], xp=40),
        Q("warship", "Warship", dep=["cargo"], items=[("immersive_aircraft:warship", 1)], xp=80),
    ],
)
