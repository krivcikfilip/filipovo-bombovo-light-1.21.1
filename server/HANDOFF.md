# Předávka: nasazení serveru „Filipovo Bombovo 2“

Tento dokument je pro Clauda (nebo člověka), který nasazuje nový modpack na server.
Na stejném serveru už běží **starý modpack** (Minecraft 1.20.1, Forge, „Filipovo Bombovo Light“).
**Starý svět ani starý server se nesmí poškodit.** Nový pack je s ním nekompatibilní (jiná verze MC) – jde o nový svět.

## Fakta o novém packu
| | |
|---|---|
| Minecraft | **1.21.1** |
| Loader | **NeoForge 21.1.266** |
| Java | **21** (starý server běží na 17 – nepřepisuj systémovou Javu, použij Docker nebo samostatnou JDK 21) |
| Repo packu | https://github.com/krivcikfilip/filipovo-bombovo-light-1.21.1 |
| packwiz URL | `https://raw.githubusercontent.com/krivcikfilip/filipovo-bombovo-light-1.21.1/main/pack.toml` |
| Počet modů | ~300 (Create + Create Aeronautics, MineColonies, Mekanism, AE2, Twilight Forest, Aether, Quark/IDAS, …) |
| Vlastní mod | `mods/fossil-neoforge-1.21.1-9.3.4.0.jar` – náš port Fossils & Archeology Revival, je přímo v repu a stahuje se přes packwiz jako ostatní |
| Hráči | 4, whitelist |

Mody se stahují nástrojem **packwiz-installer** z Modrinthu a CurseForge. Mody označené jako „client“ se na serveru automaticky vynechají (`-s server`). Všechny CurseForge mody v packu povolují automatické stažení (ověřeno).

## Krok 0 – průzkum a záloha (povinné)
1. Zjisti, jak běží starý server (Docker? systemd? screen/tmux? složka?), na jakém portu (typicky 25565) a kolik má stroj RAM (`free -h`), CPU (`nproc`) a místa (`df -h`).
2. **Udělej zálohu starého světa** (zkopíruj celou složku serveru nebo aspoň `world*`) a ověř, že záloha existuje.
3. Domluv se s uživatelem: nový server buď **nahradí** starý (starý se zastaví, ale jeho složka zůstane), nebo poběží **vedle** na jiném portu (např. 25566). Dva servery najednou potřebují RAM pro oba – starý ~6–8 GB, nový **8–10 GB**.

## Varianta A – Docker (doporučeno)
V repu je hotový `server/docker-compose.yml` (image `itzg/minecraft-server:java21`, sám nainstaluje NeoForge, stáhne pack přes `PACKWIZ_URL`, při každém restartu pack aktualizuje).
```
git clone https://github.com/krivcikfilip/filipovo-bombovo-light-1.21.1.git ~/filipovo-bombovo-2
cd ~/filipovo-bombovo-2/server
# uprav: WHITELIST, OPS (herní jména), MEMORY podle RAM, port pokud běží starý server ("25566:25565")
docker compose up -d
docker compose logs -f
```
Data světa jsou v `server/data/`. Dokumentace image: https://docker-minecraft-server.readthedocs.io/ (sekce „Modpacks → packwiz“ a „Server types → NeoForge“).

## Varianta B – bez Dockeru
1. JDK 21 do samostatné složky (např. Temurin: https://adoptium.net/temurin/releases/?version=21) – **neměň** výchozí Javu starého serveru.
2. Nová složka, např. `~/mc-bombovo2`:
   ```
   curl -LO https://maven.neoforged.net/releases/net/neoforged/neoforge/21.1.266/neoforge-21.1.266-installer.jar
   /cesta/k/jdk21/bin/java -jar neoforge-21.1.266-installer.jar --installServer
   curl -LO https://github.com/packwiz/packwiz-installer-bootstrap/releases/latest/download/packwiz-installer-bootstrap.jar
   /cesta/k/jdk21/bin/java -jar packwiz-installer-bootstrap.jar -g -s server https://raw.githubusercontent.com/krivcikfilip/filipovo-bombovo-light-1.21.1/main/pack.toml
   ```
3. `user_jvm_args.txt`: `-Xms8G -Xmx10G` (podle RAM; Aikar flags volitelně).
4. `eula.txt`: `eula=true`.
5. Start skriptem, který **před každým startem znovu spustí packwiz-installer** (aktualizace packu) a pak `./run.sh` (NeoForge ho vytvoří; v něm nastav cestu k Javě 21). Pro běh na pozadí systemd služba nebo tmux.

## server.properties (obě varianty)
- `allow-flight=true` – **nutné**, jinak server vyhazuje hráče na lodích (Create Aeronautics) a jetpackech
- `white-list=true` + whitelist 4 hráčů, op pro uživatele
- `view-distance=10`, `simulation-distance=8`, `spawn-protection=0`, `difficulty=normal`
- jiný `server-port`, pokud starý server běží dál

## Ověření po prvním startu
1. V logu musí být `Done (...)! For help, type "help"` a žádný crash. Zkontroluj `logs/latest.log` na `ERROR`, „Mixin apply failed“, „mod … requires …“.
2. Pokud server spadne na třídě z `net.minecraft.client` → nějaký mod je jen pro klienta: oprav to v repu packu (v souboru `mods/<mod>.pw.toml` nastav `side = "client"`, pak `packwiz refresh`, commit, push) – nebo to sepiš uživateli.
3. Připoj se klientem (Prism Launcher s tímtéž packem) a ověř, že se dá hrát.
4. Předgeneruj svět (v konzoli): `chunky radius 3000`, `chunky start` – s Tectonicem a strukturami výrazně pomůže výkonu. Běží to klidně hodinu+.
5. Zálohy: mod Simple Backups (do `simplebackups/`), případně cron se zálohou složky světa.

## Aktualizace packu
Pack se spravuje na Macu uživatele (packwiz) a pushuje na GitHub. Server si změny stáhne při **restartu** (Docker automaticky, varianta B přes startovací skript). Verze NeoForge se mění jen ručně (v compose `NEOFORGE_VERSION`, u varianty B novým installerem).

## Co nedělat
- Nemazat ani nepřepisovat složku / svět starého serveru.
- Neměnit systémovou Javu, na které běží starý server.
- Nepřidávat ručně jary do `mods/` na serveru – při dalším startu je packwiz-installer může smazat/přepsat; změny dělat v repu packu.
