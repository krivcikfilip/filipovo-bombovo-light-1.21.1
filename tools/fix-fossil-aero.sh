#!/usr/bin/env bash
# Přestaví Fossils port s opraveným @ExpectPlatform balíčkem, ověří jar,
# vymění ho v packu, aktualizuje Aero Islands na NeoForge verzi a pushne.
set -euo pipefail
PACK="$HOME/Projects/filipovo-bombovo-2"
PORT="$HOME/Projects/fossils-revival-port"
PW="${PACKWIZ:-$(command -v packwiz || echo "$HOME/go/bin/packwiz")}"
JARNAME="fossil-neoforge-1.21.1-9.3.4.0.jar"

echo ">> 1/5 Stahuji změny packu (Accessories od serverového Clauda)"
cd "$PACK" && git pull --ff-only

echo ">> 2/5 Build Fossils"
cd "$PORT"
./gradlew clean :neoforge:build
JAR="$PORT/neoforge/build/libs/$JARNAME"

echo ">> 3/5 Kontrola jaru"
BAD=$(unzip -p "$JAR" 'com/github/teamfossilsarcheology/*' | LC_ALL=C grep -aoE 'teamfossilsarcheology/fossil/([a-z]+/)*neoforge/[A-Za-z]+Impl' | sort -u || true)
if [ -n "$BAD" ]; then
  echo "CHYBA: jar pořád odkazuje na neexistující neoforge třídy:"; echo "$BAD"; exit 1
fi
echo "OK: žádné odkazy na neoforge/*Impl"
git add common/build.gradle
git commit -m "Fix: @ExpectPlatform transform in common uses the forge sub-package on NeoForge" || true

echo ">> 4/5 Pack: nový jar + Aero Islands NeoForge verze"
cd "$PACK"
cp "$JAR" "mods/$JARNAME"
"$PW" -y update aeroscapes-islands
grep '^filename' mods/aeroscapes-islands.pw.toml
"$PW" refresh

echo ">> 5/5 Commit + push"
git add -A
git commit -m "Fossils: opravený jar (ExpectPlatform), Aero Islands -> NeoForge verze"
git push
echo "HOTOVO"
