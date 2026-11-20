Dump registrů ze serveru (MC 1.21.1 NeoForge), 2026-11-20.
entities/biomes/structures/dimensions: /kubejs dump registry <registry> přes RCON (vícepaketové čtení, kompletní výpis).
advancements.txt: advancementy nejsou registr -> sesbíráno ze souborů data/<ns>/advancement/**.json
  (server jar + mods (vč. jar-in-jar) + world/datapacks + kubejs/data + moonlight-global-datapacks).
  Pár kusů může být vypnuto load-conditions. advancements_no_recipes.txt = totéž bez <ns>:recipes/*.
