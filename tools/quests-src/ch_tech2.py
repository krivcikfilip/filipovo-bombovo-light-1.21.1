from engine import Q, check

MEKANISM = dict(
    key="mekanism", group="tech", title="Mekanism",
    subtitle="Ore processing, machines and power suits", icon="mekanism:metallurgic_infuser",
    quests=[
        Q("osmium", "Osmium", items=[("mekanism:raw_osmium", 8)], xp=20, d=[
            "Mekanism starts with &eosmium&r ore, found deep underground. Smelt it into ingots."]),
        Q("infuser", "Metallurgic Infuser", dep=["osmium"], items=[("mekanism:metallurgic_infuser", 1)], xp=40, d=[
            "Infuses metals with carbon, redstone and more. Your first machine.",
            "Mekanism machines need FE power - Create alternators or Mekanism generators."]),
        Q("steel", "Steel", dep=["infuser"], items=[("mekanism:ingot_steel", 8)], xp=30, d=[
            "Iron + carbon in the infuser gives steel. Lots of Mekanism needs it."]),
        Q("circuit", "Basic Control Circuit", dep=["infuser"], items=[("mekanism:basic_control_circuit", 4)], xp=30),
        Q("casing", "Steel Casing", dep=["steel"], items=[("mekanism:steel_casing", 2)], xp=30),
        Q("heatgen", "Power: Heat Generator", dep=["osmium"], items=[("mekanismgenerators:heat_generator", 1)], xp=30, d=[
            "Burns fuel or sits next to lava for power. Solar and wind generators are free power later."]),
        Q("solar", "Solar power", dep=["heatgen"], items=[("mekanismgenerators:solar_generator", 2)], xp=30),
        Q("wind", "Wind power", dep=["heatgen"], items=[("mekanismgenerators:wind_generator", 1)], xp=40, d=[
            "Works better the higher you place it."]),
        Q("cable", "Cables", dep=["heatgen"], items=[("mekanism:basic_universal_cable", 16)], xp=15),
        Q("cube", "Energy Cube", dep=["cable", "circuit"], items=[("mekanism:basic_energy_cube", 1)], xp=30),
        Q("enrich", "2x ore: Enrichment Chamber", dep=["casing", "circuit"], items=[("mekanism:enrichment_chamber", 1)], xp=40, d=[
            "Ore processing tier 1: ore into 2 dusts. Smelt the dust."]),
        Q("smelter", "Energized Smelter", dep=["enrich"], items=[("mekanism:energized_smelter", 1)], xp=30),
        Q("crusher", "Crusher", dep=["enrich"], items=[("mekanism:crusher", 1)], xp=20),
        Q("purif", "3x ore: Purification Chamber", dep=["enrich"], items=[("mekanism:purification_chamber", 1), ("mekanism:advanced_control_circuit", 2)], xp=60, d=[
            "Tier 2: ore + oxygen into 3 clumps. Make oxygen with an electrolytic separator from water."]),
        Q("separator", "Electrolytic Separator", dep=["purif"], items=[("mekanism:electrolytic_separator", 1)], xp=40),
        Q("injection", "4x ore: Chemical Injection", dep=["purif"], items=[("mekanism:chemical_injection_chamber", 1), ("mekanism:elite_control_circuit", 2)], xp=80, d=[
            "Tier 3: ore + hydrogen chloride into 4 shards."]),
        Q("dissolution", "5x ore: Dissolution", dep=["injection"], items=[("mekanism:chemical_dissolution_chamber", 1), ("mekanism:chemical_washer", 1), ("mekanism:chemical_crystallizer", 1)], xp=120, d=[
            "Tier 4: the full chain gives 5 ingots per ore. JEI shows every step."]),
        Q("factory", "Factories", dep=["enrich"], items=[("mekanism:basic_smelting_factory", 1)], xp=40, d=[
            "Factories process several items at once. Upgrade machines into factories with tier installers."]),
        Q("upgrades", "Speed & Energy upgrades", dep=["enrich"], items=[("mekanism:upgrade_speed", 1), ("mekanism:upgrade_energy", 1)], xp=40),
        Q("configurator", "Configurator", dep=["casing"], items=[("mekanism:configurator", 1)], xp=20, d=[
            "Sets which side of a machine inputs and outputs. It has several modes."]),
        Q("transporter", "Logistical Transporter", dep=["configurator"], items=[("mekanism:basic_logistical_transporter", 16)], xp=30),
        Q("disassembler", "Atomic Disassembler", dep=["circuit"], items=[("mekanism:atomic_disassembler", 1)], xp=50, d=[
            "Pickaxe, axe and shovel in one, powered by energy. Has vein mining modes."]),
        Q("jetpack", "Jetpack", dep=["separator"], items=[("mekanism:jetpack", 1)], xp=60, d=[
            "Fill it with hydrogen. It has normal and hover modes."]),
        Q("miner", "Digital Miner", dep=["injection"], items=[("mekanism:digital_miner", 1)], xp=120, d=[
            "Mines ores in a large radius without digging tunnels. Set filters for what to mine."]),
        Q("teleporter", "Teleporter", dep=["injection"], items=[("mekanism:teleporter", 1)], xp=80),
        Q("tools", "Mekanism Tools", dep=["steel"], items=[("mekanismtools:steel_paxel", 1)], xp=30, d=[
            "&bMekanism Tools&r: paxels (pickaxe+axe+shovel) and armor from osmium, bronze, steel, refined glowstone and refined obsidian."]),
        Q("walkie", "Walkie-talkie", dep=["circuit"], items=[("mekanismadditions:walkie_talkie", 1)], xp=20, d=[
            "&bMekanism Additions&r: walkie-talkies, balloons, coloured plastic blocks and obsidian TNT."]),
        Q("otnt", "Obsidian TNT", dep=["walkie"], items=[("mekanismadditions:obsidian_tnt", 1)], xp=30, d=[
            "A much stronger TNT. Use it far away from your base."]),
        Q("meka", "MekaSuit", dep=["miner"], items=[("mekanism:mekasuit_bodyarmor", 1)], xp=200, d=[
            "The endgame power armor. Install modules with the module tweaker."]),
    ],
)

STORAGE = dict(
    key="storage", group="tech", title="Storage",
    subtitle="Chests, drawers and digital storage", icon="storagedrawers:controller",
    quests=[
        Q("chest", "A better chest", items=[("ironchest:iron_chest", 1)], xp=15, d=[
            "&bIron Chests&r: bigger chests in copper, iron, gold, diamond, crystal and obsidian. Upgrade items convert chests in place."]),
        Q("sophchest", "Sophisticated Storage", items=[("sophisticatedstorage:chest", 1)], xp=20, d=[
            "Chests and barrels that take the same upgrades as backpacks (sorting, compacting, void...)."]),
        Q("sophcontroller", "Storage Controller", dep=["sophchest"], items=[("sophisticatedstorage:controller", 1)], xp=40, d=[
            "Connects all touching sophisticated storages into one - put items in the controller and they go where they fit."]),
        Q("compact", "Compacting Drawer", items=[("storagedrawers:compacting_drawers_3", 1)], xp=25, d=[
            "&bStorage Drawers&r hold lots of one item and show it on the front. The compacting drawer also converts nuggets / ingots / blocks automatically."]),
        Q("dcontroller", "Drawer Controller", dep=["compact"], items=[("storagedrawers:controller", 1)], xp=40),
        Q("ender", "Ender Storage", items=[("enderstorage:ender_chest", 1), ("enderstorage:ender_pouch", 1)], xp=40, d=[
            "Chests linked by a 3-colour code. Same colours = same inventory, even across dimensions. Share a code with friends!"]),
        Q("gadget", "Building Gadgets", items=[("buildinggadgets2:gadget_building", 1)], xp=40, d=[
            "Places many blocks at once. The exchanging and copy-paste gadgets are amazing for big builds."]),
        Q("copypaste", "Copy & Paste", dep=["gadget"], items=[("buildinggadgets2:gadget_copy_paste", 1)], xp=60),
        Q("ae_meteor", "Applied Energistics 2", items=[("ae2:certus_quartz_crystal", 8)], xp=30, d=[
            "&bAE2&r - digital storage and autocrafting. Start by finding a &emeteorite&r: it has a mysterious cube with the inscriber presses.",
            "AE2 has a built-in guide book that explains everything in detail."]),
        Q("ae_charger", "Charger & Fluix", dep=["ae_meteor"], items=[("ae2:charger", 1), ("ae2:fluix_crystal", 8)], xp=40),
        Q("ae_inscriber", "Inscriber", dep=["ae_charger"], items=[("ae2:inscriber", 1)], xp=40, d=[
            "Uses the presses from meteorites to make processors."]),
        Q("ae_proc", "Processors", dep=["ae_inscriber"], items=[("ae2:logic_processor", 4), ("ae2:calculation_processor", 4), ("ae2:engineering_processor", 4)], xp=60),
        Q("ae_drive", "ME Network", dep=["ae_proc"], items=[("ae2:controller", 1), ("ae2:drive", 1), ("ae2:terminal", 1), ("ae2:item_storage_cell_1k", 1)], xp=80, d=[
            "Controller + drive + cells + terminal = all your items in one searchable screen. Connect with fluix cables."]),
        Q("ae_craft", "Autocrafting", dep=["ae_drive"], items=[("ae2:pattern_provider", 1), ("ae2:molecular_assembler", 1), ("ae2:crafting_unit", 1)], xp=120, d=[
            "Encode patterns, put them in a pattern provider next to a molecular assembler and build a crafting CPU."]),
        Q("ae_wireless", "Wireless terminal", dep=["ae_drive"], items=[("ae2:wireless_terminal", 1), ("ae2:wireless_access_point", 1)], xp=60),
        Q("rs_start", "Refined Storage", items=[("refinedstorage:controller", 1)], xp=40, d=[
            "&bRefined Storage&r is the simpler alternative to AE2 - no channels, everything just connects.",
            "Pick one of the two systems for your base; both work well."]),
        Q("rs_disk", "Disks & Grid", dep=["rs_start"], items=[("refinedstorage:disk_drive", 1), ("refinedstorage:1k_storage_disk", 1), ("refinedstorage:grid", 1)], xp=60),
        Q("rs_craft", "RS Autocrafting", dep=["rs_disk"], items=[("refinedstorage:autocrafter", 1), ("refinedstorage:pattern", 4)], xp=80),
    ],
)
