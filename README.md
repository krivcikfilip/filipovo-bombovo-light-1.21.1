# Filipovo Bombovo 2

Modpack pro Minecraft **1.21.1 + NeoForge 21.1.266**, spravovaný přes [packwiz](https://packwiz.infra.link/).
Create + Create Aeronautics, MineColonies, Mekanism, AE2, spousta jídla, zvířat a struktur.

## Instalace pro hráče (Windows / Mac / Linux)

1. Nainstaluj [Prism Launcher](https://prismlauncher.org/) a přihlas se Microsoft účtem.
2. **Add Instance** → Minecraft **1.21.1** → loader **NeoForge 21.1.266** → OK.
3. Pravým na instanci → **Edit** → **Settings**:
   - *Java → Memory*: Maximum **8192 MiB** (min. 6144).
   - *Custom commands* → zaškrtni a do **Pre-launch command** vlož:
     ```
     "$INST_JAVA" -jar packwiz-installer-bootstrap.jar https://raw.githubusercontent.com/krivcikfilip/filipovo-bombovo-light-1.21.1/main/pack.toml
     ```
4. **Edit → Version → Open .minecraft** a do té složky stáhni
   [packwiz-installer-bootstrap.jar](https://github.com/packwiz/packwiz-installer-bootstrap/releases/latest).
5. Spusť instanci. Při prvním spuštění se stáhnou všechny mody (pár minut).
   Pokud installer ukáže mody, které nejde stáhnout automaticky (CurseForge), klikni na odkazy,
   stáhni je do složky *Downloads* a pokračuj.

Každé další spuštění pack sám aktualizuje.

## Pro správce packu

```
packwiz mr add <slug>     # přidat mod z Modrinthu
packwiz cf add <slug>     # přidat mod z CurseForge
packwiz update --all      # aktualizovat mody
packwiz refresh           # po ruční změně souborů
git add -A && git commit -m "..." && git push
```

## Poděkování a licence

- **Fossils & Archeology Revival** – © Team Fossils & Archeology ([GitHub](https://github.com/TeamFossilsArcheology/FossilsArcheologyRevival)).
  V packu je naše neoficiální úprava pro Minecraft 1.21.1 NeoForge. Kód je pod licencí MIT, grafika a modely
  zůstávají autorům (licence dovoluje šíření celého projektu v rámci modpacku). Chyby v tomto portu nehlaste původním autorům.
