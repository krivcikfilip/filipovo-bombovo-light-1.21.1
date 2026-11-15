# Filipovo Bombovo 2

Modpack pro Minecraft **1.21.1 + NeoForge 21.1.266**, spravovaný přes [packwiz](https://packwiz.infra.link/).
Create + Create Aeronautics, MineColonies, Mekanism, AE2, spousta jídla, zvířat a struktur.

## Instalace pro hráče (Windows / Mac / Linux)

1. Nainstaluj [Prism Launcher](https://prismlauncher.org/) a přihlas se Microsoft účtem
   (*Accounts → Add Microsoft*).
2. **Add Instance → Import** a do pole vlož odkaz:
   ```
   https://github.com/krivcikfilip/filipovo-bombovo-light-1.21.1/raw/main/dist/Filipovo-Bombovo-2.zip
   ```
   (nebo vyber stažený soubor `Filipovo-Bombovo-2.zip`) → **OK**.
3. Spusť instanci **Filipovo Bombovo 2**. Poprvé se stáhnou všechny mody (pár minut).
   Pokud Prism nabídne stažení Javy 21, potvrď.
4. Ve hře je v seznamu serverů rovnou **Filipovo Bombovo 2** (play.filipkrivcik.cz).

Každé další spuštění pack sám aktualizuje. Paměť je nastavená na 10 GB
(*Edit → Settings → Java*, pokud máš jen 16 GB RAM nebo míň, dej 6–8 GB).
Shadery se zapínají a vypínají v menu na klávese **O**.

Ruční varianta bez zipu: nová instance 1.21.1 + NeoForge 21.1.266, do `.minecraft` dát
[packwiz-installer-bootstrap.jar](https://github.com/packwiz/packwiz-installer-bootstrap/releases/latest)
a jako *Pre-launch command* nastavit
`"$INST_JAVA" -jar packwiz-installer-bootstrap.jar https://raw.githubusercontent.com/krivcikfilip/filipovo-bombovo-light-1.21.1/main/pack.toml`.

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
