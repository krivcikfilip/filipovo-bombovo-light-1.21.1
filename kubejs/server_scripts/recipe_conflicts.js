// Filipovo Bombovo 2 – opravy kolizí receptů (vygenerováno analýzou jarů, 2026-11-20)
// Kolize = stejný typ receptu, překrývající se vstup, jiný výstup -> stroj/blok bez výběru vezme jen jeden recept.
// Princip: zúžit vstup na předmět vlastního modu; když má vstup jen jednu variantu, přesunout jeden recept
// jinam (vysoká pec, mechanická pila Create), nebo odstranit duplikát, jehož výstup jde získat jinak.
// Polymorph (pracovní stůl, pec) to neřeší: FastFurnace si v peci pamatuje první nalezený recept a
// výběr Polymorphu ignoruje; udírna/táborák/prkénko/hrnec/stroje Create výběr nemají vůbec.
// Nová ID receptů: kubejs:recipe_conflicts/<původní namespace>/<původní cesta>

ServerEvents.recipes(event => {

  // ===== Pec, udírna, táborák (minecraft:smelting / smoking / campfire_cooking) =====
  // Popcorn: ExtraDelight jen ze svých zrn (+ Pam, který popcorn nemá). Corn Delight / Cultural Delights si nechají svá zrna.
  event.remove({ id: 'extradelight:smelting/popcorn_smelt' })
  event.custom({"type": "minecraft:smelting", "category": "food", "cookingtime": 200, "experience": 1.0, "ingredient": [{"item": "extradelight:corn_seeds"}, {"item": "pamhc2crops:cornseeditem"}], "result": {"count": 1, "id": "extradelight:popcorn"}}).id('kubejs:recipe_conflicts/extradelight/smelting/popcorn_smelt')
  event.remove({ id: 'extradelight:smoking/popcorn_smoke' })
  event.custom({"type": "minecraft:smoking", "category": "food", "cookingtime": 100, "experience": 1.0, "ingredient": [{"item": "extradelight:corn_seeds"}, {"item": "pamhc2crops:cornseeditem"}], "result": {"count": 1, "id": "extradelight:popcorn"}}).id('kubejs:recipe_conflicts/extradelight/smoking/popcorn_smoke')
  event.remove({ id: 'extradelight:campfire/popcorn_fire' })
  event.custom({"type": "minecraft:campfire_cooking", "category": "food", "cookingtime": 600, "experience": 1.0, "ingredient": [{"item": "extradelight:corn_seeds"}, {"item": "pamhc2crops:cornseeditem"}], "result": {"count": 1, "id": "extradelight:popcorn"}}).id('kubejs:recipe_conflicts/extradelight/campfire/popcorn_fire')
  // Grilovaná kukuřice: ExtraDelight z #c:crops/corn kromě kukuřice z Corn Delight (ta má vlastní grilled_corn).
  event.remove({ id: 'extradelight:smelting/corn_cob_smelt' })
  event.custom({"type": "minecraft:smelting", "category": "food", "cookingtime": 200, "experience": 1.0, "ingredient": {"type": "neoforge:difference", "base": {"tag": "c:crops/corn"}, "subtracted": {"item": "corn_delight:corn"}}, "result": {"count": 1, "id": "extradelight:grilled_corn_on_cob"}}).id('kubejs:recipe_conflicts/extradelight/smelting/corn_cob_smelt')
  event.remove({ id: 'extradelight:smoking/corn_cob_smoke' })
  event.custom({"type": "minecraft:smoking", "category": "food", "cookingtime": 100, "experience": 1.0, "ingredient": {"type": "neoforge:difference", "base": {"tag": "c:crops/corn"}, "subtracted": {"item": "corn_delight:corn"}}, "result": {"count": 1, "id": "extradelight:grilled_corn_on_cob"}}).id('kubejs:recipe_conflicts/extradelight/smoking/corn_cob_smoke')
  event.remove({ id: 'extradelight:campfire/corn_cob_fire' })
  event.custom({"type": "minecraft:campfire_cooking", "category": "food", "cookingtime": 600, "experience": 1.0, "ingredient": {"type": "neoforge:difference", "base": {"tag": "c:crops/corn"}, "subtracted": {"item": "corn_delight:corn"}}, "result": {"count": 1, "id": "extradelight:grilled_corn_on_cob"}}).id('kubejs:recipe_conflicts/extradelight/campfire/corn_cob_fire')
  // Kakaové boby existují jen jedny. Pec/udírna/táborák -> createfood:cacao_nibs (nemá jiný zdroj). extradelight:roasted_cocoa_beans dál jde v troubě ExtraDelight (Oven, 8 receptů).
  event.remove({ id: 'extradelight:smelting/roasted_cocoa_beans_smelt' })
  event.remove({ id: 'extradelight:smoking/roasted_cocoa_beans_smoke' })
  event.remove({ id: 'extradelight:campfire/roasted_cocoa_beans_fire' })
  // Káva: #c:coffee_beans obsahuje jen rusticdelight:coffee_beans -> kolize s rusticdelight:roasted_coffee_beans. Create Food suší kávová zrna Farmer's Respite (ta žádný recept v peci nemají; Pam zrna dělají hotcoffee).
  event.remove({ id: 'createfood:minecraft/smelting/dried_coffee_beans_from_smelting' })
  event.custom({"type": "minecraft:smelting", "category": "food", "cookingtime": 25, "experience": 0.35, "ingredient": {"item": "farmersrespite:coffee_beans"}, "result": {"count": 1, "id": "createfood:dried_coffee_beans"}}).id('kubejs:recipe_conflicts/createfood/minecraft/smelting/dried_coffee_beans_from_smelting')
  event.remove({ id: 'createfood:minecraft/smoking/dried_coffee_beans_from_smoking' })
  event.custom({"type": "minecraft:smoking", "category": "food", "cookingtime": 100, "experience": 0.35, "ingredient": {"item": "farmersrespite:coffee_beans"}, "result": {"count": 1, "id": "createfood:dried_coffee_beans"}}).id('kubejs:recipe_conflicts/createfood/minecraft/smoking/dried_coffee_beans_from_smoking')
  event.remove({ id: 'createfood:minecraft/campfire_cooking/dried_coffee_beans_from_campfire_cooking' })
  event.custom({"type": "minecraft:campfire_cooking", "category": "food", "cookingtime": 25, "experience": 0.1, "ingredient": {"item": "farmersrespite:coffee_beans"}, "result": {"count": 1, "id": "createfood:dried_coffee_beans"}}).id('kubejs:recipe_conflicts/createfood/minecraft/campfire_cooking/dried_coffee_beans_from_campfire_cooking')
  // Chipsy Create Food jen z vlastních plátků; rusticdelight:potato_slices -> baked_potato_slices.
  event.remove({ id: 'createfood:minecraft/smelting/potato_chips_from_smelting' })
  event.custom({"type": "minecraft:smelting", "category": "food", "cookingtime": 200, "experience": 0.35, "ingredient": {"item": "createfood:sliced_potato"}, "result": {"count": 1, "id": "createfood:potato_chips"}}).id('kubejs:recipe_conflicts/createfood/minecraft/smelting/potato_chips_from_smelting')
  event.remove({ id: 'createfood:minecraft/smoking/potato_chips_from_smoking' })
  event.custom({"type": "minecraft:smoking", "category": "food", "cookingtime": 100, "experience": 0.35, "ingredient": {"item": "createfood:sliced_potato"}, "result": {"count": 1, "id": "createfood:potato_chips"}}).id('kubejs:recipe_conflicts/createfood/minecraft/smoking/potato_chips_from_smoking')
  event.remove({ id: 'createfood:minecraft/campfire_cooking/potato_chips_from_campfire_cooking' })
  event.custom({"type": "minecraft:campfire_cooking", "category": "food", "cookingtime": 200, "experience": 0.1, "ingredient": {"item": "createfood:sliced_potato"}, "result": {"count": 1, "id": "createfood:potato_chips"}}).id('kubejs:recipe_conflicts/createfood/minecraft/campfire_cooking/potato_chips_from_campfire_cooking')
  // Táborák: sendvič z Expanded Delight -> expandeddelight:grilled_cheese (jiný zdroj nemá).
  event.remove({ id: 'createfood:minecraft/campfire_cooking/grilled_cheese_sandwich_from_campfire_cooking' })
  event.custom({"type": "minecraft:campfire_cooking", "category": "food", "cookingtime": 200, "experience": 0.1, "ingredient": {"item": "createfood:cheese_sandwich"}, "result": {"count": 1, "id": "createfood:grilled_cheese_sandwich"}}).id('kubejs:recipe_conflicts/createfood/minecraft/campfire_cooking/grilled_cheese_sandwich_from_campfire_cooking')
  // Duplikát Pam (z #c:crops/sweet_potato, kam patří i batát z Expanded Delight). Pam batát se dál peče přes bakedsweetpotatoitem_* z #c:crops/sweetpotato.
  event.remove({ id: 'pamhc2crops:bakedsweet_potatoitem_forge' })
  event.remove({ id: 'pamhc2crops:bakedsweet_potatoitem_smoker' })
  event.remove({ id: 'pamhc2crops:bakedsweet_potatoitem_campfire' })
  // Karbanátek FD jen z FD mletého masa; farm_and_charm:minced_beef -> cooked_beef / cooked_minced_beef.
  event.remove({ id: 'farmersdelight:beef_patty' })
  event.custom({"type": "minecraft:smelting", "category": "food", "cookingtime": 200, "experience": 0.35, "ingredient": {"item": "farmersdelight:minced_beef"}, "result": {"count": 1, "id": "farmersdelight:beef_patty"}}).id('kubejs:recipe_conflicts/farmersdelight/beef_patty')
  event.remove({ id: 'farmersdelight:beef_patty_from_smoking' })
  event.custom({"type": "minecraft:smoking", "category": "food", "cookingtime": 100, "experience": 0.35, "ingredient": {"item": "farmersdelight:minced_beef"}, "result": {"count": 1, "id": "farmersdelight:beef_patty"}}).id('kubejs:recipe_conflicts/farmersdelight/beef_patty_from_smoking')
  event.remove({ id: 'farmersdelight:beef_patty_from_campfire_cooking' })
  event.custom({"type": "minecraft:campfire_cooking", "category": "food", "cookingtime": 600, "experience": 0.35, "ingredient": {"item": "farmersdelight:minced_beef"}, "result": {"count": 1, "id": "farmersdelight:beef_patty"}}).id('kubejs:recipe_conflicts/farmersdelight/beef_patty_from_campfire_cooking')
  // Naturalist bral celé #c:eggs (i slepičí, dinosauří a striderova vejce). Bez nich -> fried_egg (FD/Fossil) a boiled_egg (My Nether's Delight) fungují.
  event.remove({ id: 'naturalist:cooked_egg' })
  event.custom({"type": "minecraft:smelting", "ingredient": {"type": "neoforge:difference", "base": {"tag": "c:eggs"}, "subtracted": [{"item": "minecraft:egg"}, {"tag": "fossil:cookable_eggs"}, {"tag": "mynethersdelight:boiled_egg_candidate"}]}, "result": {"id": "naturalist:cooked_egg"}, "experience": 0.35, "cookingtime": 200}).id('kubejs:recipe_conflicts/naturalist/cooked_egg')
  event.remove({ id: 'naturalist:cooked_egg_from_smoking' })
  event.custom({"type": "minecraft:smoking", "ingredient": {"type": "neoforge:difference", "base": {"tag": "c:eggs"}, "subtracted": [{"item": "minecraft:egg"}, {"tag": "fossil:cookable_eggs"}, {"tag": "mynethersdelight:boiled_egg_candidate"}]}, "result": {"id": "naturalist:cooked_egg"}, "experience": 0.35, "cookingtime": 200}).id('kubejs:recipe_conflicts/naturalist/cooked_egg_from_smoking')
  event.remove({ id: 'naturalist:cooked_egg_from_campfire_cooking' })
  event.custom({"type": "minecraft:campfire_cooking", "ingredient": {"type": "neoforge:difference", "base": {"tag": "c:eggs"}, "subtracted": [{"item": "minecraft:egg"}, {"tag": "fossil:cookable_eggs"}, {"tag": "mynethersdelight:boiled_egg_candidate"}]}, "result": {"id": "naturalist:cooked_egg"}, "experience": 0.35, "cookingtime": 200}).id('kubejs:recipe_conflicts/naturalist/cooked_egg_from_campfire_cooking')
  // Udírna: #c:eggplant obsahuje i nakrájený lilek -> kolize se smoked_cut_eggplant.
  event.remove({ id: 'culturaldelights:smelting/smoked_eggplant' })
  event.custom({"type": "minecraft:smoking", "ingredient": {"item": "culturaldelights:eggplant"}, "result": {"count": 1, "id": "culturaldelights:smoked_eggplant"}, "experience": 0.35, "cookingtime": 100}).id('kubejs:recipe_conflicts/culturaldelights/smelting/smoked_eggplant')
  // Deska Stal -> aether:music_disc_klepto (jiný zdroj nemá). Ostatní desky dál -> etched:blank_music_disc.
  event.remove({ id: 'etched:blank_music_disc' })
  event.custom({"type": "minecraft:smelting", "category": "misc", "cookingtime": 200, "experience": 0.2, "ingredient": {"type": "neoforge:difference", "base": {"tag": "c:music_discs"}, "subtracted": {"item": "minecraft:music_disc_stal"}}, "result": {"count": 1, "id": "etched:blank_music_disc"}}).id('kubejs:recipe_conflicts/etched/blank_music_disc')
  // Duše písek: pec -> create:scoria, vysoká pec -> netherexotics:soul_glass (oba jinak nezískatelné).
  event.remove({ id: 'netherexotics:soul_glass_recipe' })
  event.custom({"type": "minecraft:blasting", "category": "misc", "experience": 1, "cookingtime": 100, "ingredient": {"item": "minecraft:soul_sand"}, "result": {"id": "netherexotics:soul_glass"}}).id('kubejs:recipe_conflicts/netherexotics/soul_glass_recipe')
  // Oltář Aetheru: deska Otherside -> deep_aether:music_disc_a_morning_wish.
  event.remove({ id: 'aether:aether_tune_enchanting' })
  event.custom({"type": "aether:enchanting", "category": "enchanting_misc", "cookingtime": 500, "experience": 1.0, "ingredient": {"type": "neoforge:difference", "base": {"tag": "aether:accepted_music_discs"}, "subtracted": {"item": "minecraft:music_disc_otherside"}}, "result": {"count": 1, "id": "aether:music_disc_aether_tune"}}).id('kubejs:recipe_conflicts/aether/aether_tune_enchanting')

  // ===== Prkénko Farmer's Delight (farmersdelight:cutting) – nemá výběr výsledku =====
  // Kukuřice: Corn Delight nekrájí klasy Cultural Delights a ExtraDelight (ty mají vlastní recepty).
  event.remove({ id: 'corn_delight:cutting/corn' })
  event.custom({"type": "farmersdelight:cutting", "ingredients": [{"type": "neoforge:difference", "base": {"tag": "c:crops/corn"}, "subtracted": [{"item": "culturaldelights:corn_cob"}, {"item": "extradelight:corn_on_cob"}]}], "tool": {"tag": "c:tools/knife"}, "result": [{"item": {"id": "corn_delight:corn_seeds", "count": 2}}, {"item": {"id": "corn_delight:corncob"}}]}).id('kubejs:recipe_conflicts/corn_delight/cutting/corn')
  // Tortilla: každý mod krájí svou tortillu.
  event.remove({ id: 'corn_delight:cutting/tortilla_chip' })
  event.custom({"type": "farmersdelight:cutting", "ingredients": [{"item": "corn_delight:tortilla"}], "tool": {"tag": "c:tools/knife"}, "result": [{"item": {"id": "corn_delight:tortilla_chip", "count": 4}}]}).id('kubejs:recipe_conflicts/corn_delight/cutting/tortilla_chip')
  // Sýr: Create Food krájí jen svůj blok sýra (bochníky Expanded Delight mají vlastní plátky).
  event.remove({ id: 'createfood:farmersdelight/cutting/cheese_slice_from_cutting' })
  event.custom({"type": "farmersdelight:cutting", "ingredients": [{"item": "createfood:cheese_block"}], "tool": {"tag": "c:tools/knife"}, "result": [{"item": {"count": 7, "id": "createfood:cheese_slice"}}]}).id('kubejs:recipe_conflicts/createfood/farmersdelight/cutting/cheese_slice_from_cutting')
  // Čokoláda: ExtraDelight jen ze své tabulky; Create tabulka -> createfood:chocolate_chips.
  event.remove({ id: 'extradelight:cutting/milk_chocolate_chips' })
  event.custom({"type": "farmersdelight:cutting", "ingredients": [{"item": "extradelight:milk_chocolate_bar"}], "result": [{"item": {"count": 5, "id": "extradelight:milk_chocolate_chips"}}], "tool": {"tag": "c:tools/knife"}}).id('kubejs:recipe_conflicts/extradelight/cutting/milk_chocolate_chips')
  // Chorus koláč: každý mod krájí svůj.
  event.remove({ id: 'createfood:farmersdelight/cutting/chorus_fruit_pie_slice_from_cutting' })
  event.custom({"type": "farmersdelight:cutting", "ingredients": [{"item": "createfood:chorus_fruit_pie"}], "tool": {"tag": "c:tools/knife"}, "result": [{"item": {"count": 4, "id": "createfood:chorus_fruit_pie_slice"}}]}).id('kubejs:recipe_conflicts/createfood/farmersdelight/cutting/chorus_fruit_pie_slice_from_cutting')
  // Chorus ovoce -> ends_delight:chorus_fruit_grain. createfood:chorus_fruit_slice dál jde z praženého chorusu (…_from_cutting_alt).
  event.remove({ id: 'createfood:farmersdelight/cutting/chorus_fruit_slice_from_cutting' })
  // Houby: 4 vanilla houby mají vlastní plátky Create Food; mletá houba z ostatních (i z plátků) + mlýn/lis/stůl.
  event.remove({ id: 'createfood:farmersdelight/cutting/ground_mushroom_from_cutting' })
  event.custom({"type": "farmersdelight:cutting", "ingredients": [{"type": "neoforge:difference", "base": {"tag": "c:mushrooms"}, "subtracted": [{"item": "minecraft:brown_mushroom"}, {"item": "minecraft:red_mushroom"}, {"item": "minecraft:crimson_fungus"}, {"item": "minecraft:warped_fungus"}]}], "tool": {"tag": "c:tools/knife"}, "result": [{"item": {"count": 2, "id": "createfood:ground_mushroom"}}]}).id('kubejs:recipe_conflicts/createfood/farmersdelight/cutting/ground_mushroom_from_cutting')
  // Paprika (koření): ne z celých pečených paprik Rustic Delight (ty se krájí na plátky).
  event.remove({ id: 'createfood:farmersdelight/cutting/paprika_from_cutting' })
  event.custom({"type": "farmersdelight:cutting", "ingredients": [{"type": "neoforge:difference", "base": {"tag": "c:pepper"}, "subtracted": [{"item": "rusticdelight:roasted_bell_pepper_black"}, {"item": "rusticdelight:roasted_bell_pepper_blue"}, {"item": "rusticdelight:roasted_bell_pepper_green"}, {"item": "rusticdelight:roasted_bell_pepper_orange"}, {"item": "rusticdelight:roasted_bell_pepper_pink"}, {"item": "rusticdelight:roasted_bell_pepper_purple"}, {"item": "rusticdelight:roasted_bell_pepper_red"}, {"item": "rusticdelight:roasted_bell_pepper_white"}, {"item": "rusticdelight:roasted_bell_pepper_yellow"}]}], "tool": {"tag": "c:tools/knife"}, "result": [{"item": {"count": 2, "id": "createfood:paprika"}}]}).id('kubejs:recipe_conflicts/createfood/farmersdelight/cutting/paprika_from_cutting')
  // Těsto: sekáček (cleaver) z Farm & Charm je sekera i nůž -> těstoviny vs. malé těsto. Malé těsto jen sekerou, která není nůž.
  event.remove({ id: 'createfood:farmersdelight/cutting/wheat_dough_small_from_cutting' })
  event.custom({"type": "farmersdelight:cutting", "ingredients": [{"tag": "c:wheat_dough"}], "tool": {"type": "neoforge:difference", "base": {"tag": "minecraft:axes"}, "subtracted": {"tag": "c:tools/knife"}}, "result": [{"item": {"count": 2, "id": "createfood:wheat_dough_small"}}]}).id('kubejs:recipe_conflicts/createfood/farmersdelight/cutting/wheat_dough_small_from_cutting')
  // Citron: Fruits Delight krájí svůj citron, ExtraDelight svůj (+ Pam).
  event.remove({ id: 'fruitsdelight:cutting/lemon' })
  event.custom({"type": "farmersdelight:cutting", "ingredients": [{"type": "neoforge:difference", "base": {"tag": "c:foods/fruits/lemon"}, "subtracted": {"tag": "c:crops/lemon"}}], "result": [{"item": {"count": 4, "id": "fruitsdelight:lemon_slice"}}, {"item": {"count": 1, "id": "fruitsdelight:lemon_seeds"}}], "tool": {"tag": "c:tools/knife"}}).id('kubejs:recipe_conflicts/fruitsdelight/cutting/lemon')
  // Pomeranč: Fruits Delight krájí svůj, ExtraDelight svůj (+ Pam).
  event.remove({ id: 'fruitsdelight:cutting/orange' })
  event.custom({"type": "farmersdelight:cutting", "ingredients": [{"type": "neoforge:difference", "base": {"tag": "c:foods/fruits/orange"}, "subtracted": {"tag": "c:crops/orange"}}], "result": [{"item": {"count": 4, "id": "fruitsdelight:orange_slice"}}], "tool": {"tag": "c:tools/knife"}}).id('kubejs:recipe_conflicts/fruitsdelight/cutting/orange')
  // Neptuniový nůž má dávat víc filetů – běžný recept ho nemá přijímat.
  event.remove({ id: 'aquaculturedelight:cutting/fillet/fillet_four' })
  event.custom({"type": "farmersdelight:cutting", "ingredients": [{"tag": "aquaculturedelight:fillet_four"}], "result": [{"item": {"count": 4, "id": "aquaculture:fish_fillet_raw"}}, {"chance": 0.1, "item": {"count": 1, "id": "aquaculture:fish_bones"}}], "tool": {"type": "neoforge:difference", "base": {"tag": "c:tools/knife"}, "subtracted": {"tag": "aquaculturedelight:neptunium_knives"}}}).id('kubejs:recipe_conflicts/aquaculturedelight/cutting/fillet/fillet_four')
  event.remove({ id: 'aquaculturedelight:cutting/fillet/fillet_six' })
  event.custom({"type": "farmersdelight:cutting", "ingredients": [{"tag": "aquaculturedelight:fillet_six"}], "result": [{"item": {"count": 6, "id": "aquaculture:fish_fillet_raw"}}, {"chance": 0.1, "item": {"count": 1, "id": "aquaculture:fish_bones"}}], "tool": {"type": "neoforge:difference", "base": {"tag": "c:tools/knife"}, "subtracted": {"tag": "aquaculturedelight:neptunium_knives"}}}).id('kubejs:recipe_conflicts/aquaculturedelight/cutting/fillet/fillet_six')
  event.remove({ id: 'aquaculturedelight:cutting/fillet/fillet_ten' })
  event.custom({"type": "farmersdelight:cutting", "ingredients": [{"tag": "aquaculturedelight:fillet_ten"}], "result": [{"item": {"count": 10, "id": "aquaculture:fish_fillet_raw"}}, {"chance": 0.1, "item": {"count": 1, "id": "aquaculture:fish_bones"}}], "tool": {"type": "neoforge:difference", "base": {"tag": "c:tools/knife"}, "subtracted": {"tag": "aquaculturedelight:neptunium_knives"}}}).id('kubejs:recipe_conflicts/aquaculturedelight/cutting/fillet/fillet_ten')
  event.remove({ id: 'aquaculturedelight:cutting/fillet/fillet_twelve' })
  event.custom({"type": "farmersdelight:cutting", "ingredients": [{"tag": "aquaculturedelight:fillet_twelve"}], "result": [{"item": {"count": 12, "id": "aquaculture:fish_fillet_raw"}}, {"chance": 0.1, "item": {"count": 1, "id": "aquaculture:fish_bones"}}], "tool": {"type": "neoforge:difference", "base": {"tag": "c:tools/knife"}, "subtracted": {"tag": "aquaculturedelight:neptunium_knives"}}}).id('kubejs:recipe_conflicts/aquaculturedelight/cutting/fillet/fillet_twelve')
  event.remove({ id: 'aquaculturedelight:cutting/fillet/fillet_fourteen' })
  event.custom({"type": "farmersdelight:cutting", "ingredients": [{"tag": "aquaculturedelight:fillet_fourteen"}], "result": [{"item": {"count": 14, "id": "aquaculture:fish_fillet_raw"}}, {"chance": 0.1, "item": {"count": 1, "id": "aquaculture:fish_bones"}}], "tool": {"type": "neoforge:difference", "base": {"tag": "c:tools/knife"}, "subtracted": {"tag": "aquaculturedelight:neptunium_knives"}}}).id('kubejs:recipe_conflicts/aquaculturedelight/cutting/fillet/fillet_fourteen')
  // Stejná surovina jako recept ExtraDelight/Rustic Delight na prkénku. Varianta Create Food -> mechanická pila Create.
  event.remove({ id: 'createfood:farmersdelight/cutting/apple_slice_from_cutting' })
  event.custom({"type": "create:cutting", "ingredients": [{"item": "minecraft:apple"}], "processing_time": 50, "results": [{"id": "createfood:apple_slice", "count": 2}]}).id('kubejs:recipe_conflicts/createfood/farmersdelight/cutting/apple_slice_from_cutting')
  event.remove({ id: 'createfood:farmersdelight/cutting/bread_slice_from_cutting' })
  event.custom({"type": "create:cutting", "ingredients": [{"item": "minecraft:bread"}], "processing_time": 50, "results": [{"id": "createfood:bread_slice", "count": 3}]}).id('kubejs:recipe_conflicts/createfood/farmersdelight/cutting/bread_slice_from_cutting')
  event.remove({ id: 'createfood:farmersdelight/cutting/sliced_beetroot_from_cutting' })
  event.custom({"type": "create:cutting", "ingredients": [{"item": "minecraft:beetroot"}], "processing_time": 50, "results": [{"id": "createfood:sliced_beetroot", "count": 2}]}).id('kubejs:recipe_conflicts/createfood/farmersdelight/cutting/sliced_beetroot_from_cutting')
  event.remove({ id: 'createfood:farmersdelight/cutting/sliced_onion_from_cutting' })
  event.custom({"type": "create:cutting", "ingredients": [{"tag": "c:crops/onion"}], "processing_time": 50, "results": [{"id": "createfood:sliced_onion", "count": 2}]}).id('kubejs:recipe_conflicts/createfood/farmersdelight/cutting/sliced_onion_from_cutting')
  event.remove({ id: 'createfood:farmersdelight/cutting/sliced_tomato_from_cutting' })
  event.custom({"type": "create:cutting", "ingredients": [{"tag": "c:crops/tomato"}], "processing_time": 50, "results": [{"id": "createfood:sliced_tomato", "count": 2}]}).id('kubejs:recipe_conflicts/createfood/farmersdelight/cutting/sliced_tomato_from_cutting')
  event.remove({ id: 'createfood:farmersdelight/cutting/sliced_potato_from_cutting' })
  event.custom({"type": "create:cutting", "ingredients": [{"item": "minecraft:potato"}], "processing_time": 50, "results": [{"id": "createfood:sliced_potato", "count": 2}]}).id('kubejs:recipe_conflicts/createfood/farmersdelight/cutting/sliced_potato_from_cutting')
  // Brambora: prkénko -> rusticdelight:potato_slices (nejpoužívanější, 147 receptů). ExtraDelight plátky -> pila, jen z brambory (#c:crops/potato obsahuje i plátky Rustic Delight). Na pile se střídají s plátky Create Food, filtr pily vybere.
  event.remove({ id: 'extradelight:cutting/sliced_potato' })
  event.custom({"type": "create:cutting", "ingredients": [{"item": "minecraft:potato"}], "processing_time": 50, "results": [{"id": "extradelight:sliced_potato", "count": 4}]}).id('kubejs:recipe_conflicts/extradelight/cutting/sliced_potato')
  // Ender perla: prkénko -> ends_delight:ender_pearl_grain (quest Bublinkový čaj), pila -> endersdelight:ender_shard.
  event.remove({ id: 'endersdelight:cutting/ender_shard' })
  event.custom({"type": "create:cutting", "ingredients": [{"item": "minecraft:ender_pearl"}], "processing_time": 50, "results": [{"id": "endersdelight:ender_shard", "count": 2}]}).id('kubejs:recipe_conflicts/endersdelight/cutting/ender_shard')

  // ===== Hrnec Farmer's Delight (farmersdelight:cooking) =====
  // Jablko+cukr: hrnec -> rusticdelight:syrup (jiný zdroj nemá). Jablečný džem Create Food jde dál na stole a plničkou.
  event.remove({ id: 'createfood:farmersdelight/cooking/apple_jam_bottle_from_cooking' })
  // Jablko+cukr: karamelové jablko ExtraDelight dál z medu (farmersdelight:candy_apple) a v míchačce Create.
  event.remove({ id: 'farmersdelight:candy_apple_sugar' })
  // 3 jablka + cukr -> brewinandchewin:apple_jelly; jablečné pyré ExtraDelight v hrnci z medu.
  event.remove({ id: 'farmersdelight:apple_sauce' })
  event.custom({"type": "farmersdelight:cooking", "container": {"count": 1, "id": "minecraft:bowl"}, "cookingtime": 400, "experience": 0.35, "ingredients": [{"item": "minecraft:apple"}, {"item": "minecraft:apple"}, {"item": "minecraft:apple"}, {"item": "minecraft:honey_bottle"}], "recipe_book_tab": "meals", "result": {"count": 4, "id": "extradelight:apple_sauce"}}).id('kubejs:recipe_conflicts/farmersdelight/apple_sauce')
  // Cukr+máslo: hrnec -> extradelight:butterscotch. Karamel Create Food jde dál na stole a lisem.
  event.remove({ id: 'createfood:farmersdelight/cooking/toffee_from_cooking' })
  // Mléko+ocet: sýr ExtraDelight jen z octa ExtraDelight/Pam; ocet Create Food -> createfood:yogurt_bucket.
  event.remove({ id: 'farmersdelight:cheese_vinegar' })
  event.custom({"type": "farmersdelight:cooking", "cookingtime": 400, "experience": 1.0, "ingredients": [{"item": "minecraft:milk_bucket"}, {"type": "neoforge:compound", "children": [{"item": "extradelight:vinegar"}, {"item": "pamhc2foodcore:vinegaritem"}]}], "recipe_book_tab": "meals", "result": {"count": 2, "id": "extradelight:cheese"}}).id('kubejs:recipe_conflicts/farmersdelight/cheese_vinegar')

  // ===== Odšťavňovač Expanded Delight (expandeddelight:juicing) =====
  // Odšťavňovač -> džus Expanded Delight (quest ed_juice). Džus Create Food jde dál na stole a plničkou.
  event.remove({ id: 'createfood:expandeddelight/juicing/apple_juice_bottle_from_juicing' })
  event.remove({ id: 'createfood:expandeddelight/juicing/berry_juice_bottle_from_juicing' })
  event.remove({ id: 'createfood:expandeddelight/juicing/glow_berry_juice_bottle_from_juicing' })

  // ===== Create (mlýn, lis+tyglík, míchačka, praní) =====
  // Vápenec v mlýnu -> Create Aquatic Ambitions (vápníkový prášek + podezřelý kámen). Ledek z vápence dál na drtících kolech (create_mf:..._crushing).
  event.remove({ id: 'create_mf:saltpeter_from_limestone_recipe' })
  // Semínka pod lisem -> createdieselgenerators:plant_oil. Oba oleje jsou v #c:plantoil a všechny recepty (biomasa, bionafta, spalování) berou tag -> semenný olej není potřeba.
  event.remove({ id: 'createaddition:compacting/seed_oil' })
  // Totéž (slunečnicová semínka jsou v #c:seeds).
  event.remove({ id: 'adorablehamsterpets:create_compat/compacting_ahp_sunflower_seeds' })
  // Cukr+kakao+mléko s ohřevem -> tekutá čokoláda Create (quest Čokoláda). Tekutá horká čokoláda Farmer's Respite jde dál v konvici. Stejné ID má i recept ExtraDelight (lahev+mléko+sladidlo+tekutá čokoláda -> farmersdelight:hot_cocoa); který soubor vyhraje, nejde určit -> přidán znovu pod vlastním ID.
  event.remove({ id: 'create:mixing/hot_cocoa' })
  event.custom({"type": "create:mixing", "heat_requirement": "heated", "ingredients": [{"item": "minecraft:glass_bottle"}, {"tag": "c:drinks/milk"}, {"tag": "extradelight:sweetener"}, {"tag": "c:liquid_chocolate"}], "results": [{"id": "farmersdelight:hot_cocoa"}]}).id('kubejs:recipe_conflicts/create/mixing/hot_cocoa')
  // Mouka+voda v míchačce -> create:dough (quest Těsto). FD těsto dál ze 3 mouk + vody v míchačce, v míse i na stole.
  event.remove({ id: 'createfood:create/mixing/compat/farmersdelight/wheat_dough_from_mixing_water_farmersdelight' })
  // Rozpouštění: každý mod taví svou tabulku.
  event.remove({ id: 'createfood:create/mixing/dark_chocolate_fluid_from_mixing_melting' })
  event.custom({"type": "create:mixing", "heat_requirement": "heated", "ingredients": [{"item": "createfood:bar_of_dark_chocolate"}], "results": [{"amount": 250, "id": "createfood:dark_chocolate"}]}).id('kubejs:recipe_conflicts/createfood/create/mixing/dark_chocolate_fluid_from_mixing_melting')
  event.remove({ id: 'createfood:create/mixing/white_chocolate_fluid_from_mixing_melting' })
  event.custom({"type": "create:mixing", "heat_requirement": "heated", "ingredients": [{"item": "createfood:bar_of_white_chocolate"}], "results": [{"amount": 250, "id": "createfood:white_chocolate"}]}).id('kubejs:recipe_conflicts/createfood/create/mixing/white_chocolate_fluid_from_mixing_melting')
  // Praní: industrial iron window pane má zvětrat, ne se změnit na sklo.
  event.remove({ id: 'create:splashing/stained_glass_pane' })
  event.custom({"type": "create:splashing", "ingredients": [{"type": "neoforge:difference", "base": {"tag": "c:glass_panes"}, "subtracted": {"item": "create:industrial_iron_window_pane"}}], "results": [{"id": "minecraft:glass_pane"}]}).id('kubejs:recipe_conflicts/create/splashing/stained_glass_pane')
  // Vylévání: Create Food jen ze své lahve džemu; džem Fruits Delight -> tekutý džem Fruits Delight.
  event.remove({ id: 'createfood:create/emptying/apple_jam_fluid_from_emptying_bottle' })
  event.custom({"type": "create:emptying", "ingredients": [{"item": "createfood:apple_jam_bottle"}], "results": [{"item": {"id": "minecraft:glass_bottle"}}, {"amount": 500, "id": "createfood:apple_jam"}]}).id('kubejs:recipe_conflicts/createfood/create/emptying/apple_jam_fluid_from_emptying_bottle')
  event.remove({ id: 'createfood:create/emptying/berry_jam_fluid_from_emptying_bottle' })
  event.custom({"type": "create:emptying", "ingredients": [{"item": "createfood:berry_jam_bottle"}], "results": [{"item": {"id": "minecraft:glass_bottle"}}, {"amount": 500, "id": "createfood:berry_jam"}]}).id('kubejs:recipe_conflicts/createfood/create/emptying/berry_jam_fluid_from_emptying_bottle')
  event.remove({ id: 'createfood:create/emptying/chorus_fruit_jam_fluid_from_emptying_bottle' })
  event.custom({"type": "create:emptying", "ingredients": [{"item": "createfood:chorus_fruit_jam_bottle"}], "results": [{"item": {"id": "minecraft:glass_bottle"}}, {"amount": 500, "id": "createfood:chorus_fruit_jam"}]}).id('kubejs:recipe_conflicts/createfood/create/emptying/chorus_fruit_jam_fluid_from_emptying_bottle')
  event.remove({ id: 'createfood:create/emptying/glow_berry_jam_fluid_from_emptying_bottle' })
  event.custom({"type": "create:emptying", "ingredients": [{"item": "createfood:glow_berry_jam_bottle"}], "results": [{"item": {"id": "minecraft:glass_bottle"}}, {"amount": 500, "id": "createfood:glow_berry_jam"}]}).id('kubejs:recipe_conflicts/createfood/create/emptying/glow_berry_jam_fluid_from_emptying_bottle')
  event.remove({ id: 'createfood:create/emptying/melon_jam_fluid_from_emptying_bottle' })
  event.custom({"type": "create:emptying", "ingredients": [{"item": "createfood:melon_jam_bottle"}], "results": [{"item": {"id": "minecraft:glass_bottle"}}, {"amount": 500, "id": "createfood:melon_jam"}]}).id('kubejs:recipe_conflicts/createfood/create/emptying/melon_jam_fluid_from_emptying_bottle')

  // ===== Hmoždíř ExtraDelight (extradelight:mortar) =====
  // Olejnatá semínka: bez kukuřičných zrn (-> kukuřičná mouka) a kávy (-> mletá káva).
  event.remove({ id: 'extradelight:mortar/oil_seeds' })
  event.custom({"type": "extradelight:mortar", "fluidOut": {"amount": 100, "id": "extradelight:oil_fluid"}, "grinds": 4, "ingredient": {"type": "neoforge:difference", "base": {"tag": "c:seeds"}, "subtracted": [{"item": "minecraft:wheat_seeds"}, {"item": "extradelight:corn_seeds"}, {"item": "extradelight:soybeans"}, {"item": "extradelight:sunflower_seeds"}, {"tag": "c:seeds/corn"}, {"tag": "c:crops/coffee/cooked"}]}, "result": {"count": 1, "id": "minecraft:bone_meal"}}).id('kubejs:recipe_conflicts/extradelight/mortar/oil_seeds')

  // ===== Drcení (create:crushing) =====
  // Smrkový kmen: Create Propulsion (pryskyřice -> terpentýn) koliduje s Create Diesel Generators (#minecraft:logs -> štěpka).
  // Pryskyřice se přesouvá do mlýnku (create:milling). Drticí kola berou nejdřív drcení, mlýnský recept jen když drcení
  // neexistuje (Create CrushingWheelControllerBlockEntity.findRecipe) -> kola dál dělají štěpku, mlýnek pryskyřici.
  event.remove({ id: 'createpropulsion:crushing/spruce_log' })
  event.custom({"type": "create:milling", "ingredients": [{"item": "minecraft:spruce_log"}], "processing_time": 150, "results": [{"chance": 0.6, "id": "createpropulsion:pine_resin"}]}).id('kubejs:recipe_conflicts/createpropulsion/milling/spruce_log')
})
