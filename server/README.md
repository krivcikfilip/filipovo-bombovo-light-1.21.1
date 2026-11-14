# Server

Potřeba: Linux s Dockerem (Docker Engine + compose plugin), ideálně 16 GB RAM, 4+ jádra.

```
git clone https://github.com/krivcikfilip/filipovo-bombovo-light-1.21.1.git
cd filipovo-bombovo-light-1.21.1/server
nano docker-compose.yml          # doplň WHITELIST a OPS
docker compose up -d
docker compose logs -f           # první start trvá pár minut (stahuje se ~300 modů)
```

Užitečné:
- konzole serveru: `docker attach filipovo-bombovo` (odpojení Ctrl+P, Ctrl+Q)
- předgenerování světa (doporučeno před hraním, v konzoli): `chunky radius 3000` a `chunky start`
- restart (zároveň aktualizuje pack): `docker compose restart`
- zálohy dělá mod Simple Backups do `data/simplebackups/`
