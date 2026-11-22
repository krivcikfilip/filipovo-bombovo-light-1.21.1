Datapack přes KubeJS (načítá se nad mody).
minecraft/worldgen/structure(_set)/trial_chambers.json = vanilla 1.21.1.
Důvod: Aero Islands (aeroscapes) přesouvá zkušební komnaty do biomu aeroscapes:deep_voidsea,
který se kvůli Terralithu (jeho overworld.json vyhrává) nikdy negeneruje -> komnaty by nebyly nikde.
Platí jen pro nově generované chunky.

bombovo/recipe/ore_vein_type/platinum.json + drilling/platinum.json (2026-11-22):
platinová žíla pro Create Ore Excavation (žíla jako zlatá; vrtání stress 256, zlato 192). Důvod: platinová ruda z Create Propulsion
se generuje jen v nových chuncích a svět je předgenerovaný -> platina by jinak nešla získat.
Žíly COE se umisťují podle chunku a soli, takže fungují i ve stávajícím světě.
