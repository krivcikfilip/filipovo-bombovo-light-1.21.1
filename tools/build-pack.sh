#!/usr/bin/env bash
# Postaví packwiz repo "Filipovo Bombovo 2" (NeoForge 1.21.1).
# Spouštěj z kořene složky filipovo-bombovo-2:  ./tools/build-pack.sh
set -u
cd "$(dirname "$0")/.."
ROOT="$(pwd)"
LOG="$ROOT/tools/build.log"
FAILED="$ROOT/tools/failed.txt"
: > "$LOG"; : > "$FAILED"

# --- 1) packwiz -------------------------------------------------------------
export PATH="$HOME/go/bin:/opt/homebrew/bin:/usr/local/bin:/usr/local/go/bin:$PATH"
if ! command -v packwiz >/dev/null 2>&1; then
  if ! command -v go >/dev/null 2>&1; then
    if command -v brew >/dev/null 2>&1; then
      echo ">> Instaluji Go přes Homebrew (potřeba pro packwiz)…"
      brew install go || { echo "Instalace Go selhala."; exit 1; }
    else
      echo "Chybí Go i Homebrew. Nainstaluj Go z https://go.dev/dl/ a spusť skript znovu."
      exit 1
    fi
  fi
  echo ">> Instaluji packwiz…"
  go install github.com/packwiz/packwiz@latest || { echo "Instalace packwiz selhala."; exit 1; }
fi
echo ">> packwiz: $(command -v packwiz)"

# --- 2) init ----------------------------------------------------------------
if [ ! -f pack.toml ]; then
  packwiz init --name "Filipovo Bombovo 2" --author "Filip" --version "1.0.0" \
    --mc-version 1.21.1 --modloader neoforge --neoforge-latest >>"$LOG" 2>&1 \
    || { echo "packwiz init selhal, viz tools/build.log"; exit 1; }
fi

mr() { # Modrinth
  for s in "$@"; do
    printf '   MR  %-55s' "$s"
    if packwiz -y mr add "https://modrinth.com/mod/$s" >>"$LOG" 2>&1; then echo ok; else echo CHYBA; echo "mr $s" >>"$FAILED"; fi
  done
}
cf() { # CurseForge
  for s in "$@"; do
    printf '   CF  %-55s' "$s"
    if packwiz -y cf add "https://www.curseforge.com/minecraft/mc-mods/$s" >>"$LOG" 2>&1; then echo ok; else echo CHYBA; echo "cf $s" >>"$FAILED"; fi
  done
}

# --- 3) mody ----------------------------------------------------------------
echo ">> Knihovny a optimalizace"
mr architectury-api balm cloth-config curios geckolib kotlin-for-forge moonlight resourceful-config \
   resourceful-lib supermartijn642s-config-lib supermartijn642s-core-lib creativecore cucumber \
   fzzy-config jamlib mint-lib mmlib moogs-structure-lib modonomicon patchouli placebo almanac \
   elysium-api caelus terrablender yungs-api citadel-1.21.1-port fusion-connected-textures athena-ctm \
   guideme fragmentum rpl
mr sodium iris lithium modernfix ferrite-core immediatelyfast entityculling badoptimizations \
   ai-improvements lmd clumps fastfurnace fastworkbench deuf-neoforge createbetterfps spark

echo ">> Create + Aeronautics"
mr create create-aeronautics aeronautics-structures aeroscapes-islands create-aeronautics-climbable-rope \
   create-big-cannons createaddition create-deco create-goggles create-jetpack create-ore-excavation \
   slice-and-dice create-stuff-additions create-waystones-recipes create-aquatic-ambitions bellsandwhistles \
   create-bits-n-bobs create-central-kitchen create-connected copycats create-diesel-generators \
   dynamic-village create-enchantment-industry escalated hypertube interiors create-let-the-adventure-begin \
   create-mechanical-companion create-more-features create-new-age create-power-loader \
   create-steam-n-rails-1.21.1 create-structures-arise create-trading-floor create-wrapped create-teleporters \
   rechiseled-create sophisticated-backpacks-create-integration sophisticated-storage-create-integration

echo ">> Tech a úložiště"
mr ae2 mekanism mekanism-generators mekanism-tools mekanism-additions refined-storage extended-crafting \
   storagedrawers sophisticated-core sophisticated-backpacks sophisticated-storage ender-storage chunk-loaders

echo ">> Zvířata a moby"
mr alexs-mobs-1.21.1 alexs-caves-unofficial-port naturalist \
   critters-and-companions adorable-hamster-pets bens-sharks enderman-overhaul fowlplay fish-of-thieves \
   unusual-fish aquaculture upgrade-aquatic autumnity blueprint luminous-tag luminous-beasts \
   luminousbutterflies luminous-monsters luminous-nether the-luminous-mod mutated-items

echo ">> Jídlo"
mr farmers-delight appleskin abnormals-delight aquaculture-delight chefs-delight corn-delight ends-delight \
   enders-delight miners-delight my-nethers-delight oceans-delight twilight-delight expanded-delight \
   cultural-delights rustic-delight brewin-and-chewin farmers-respite-unofficial-port extradelight \
   fruits-delight storage-delight pams-harvestcraft-2-food-core pams-harvestcraft-2-crops \
   pams-harvestcraft-2-trees create-food create-confectionery create-cafe create-winery \
   lets-do-farm-charm lets-do-bakery-farmcharm-compat lets-do-brewery-farmcharm-compat \
   lets-do-candlelight-farmcharm-compat lets-do-vinery lets-do-meadow lets-do-beachparty lets-do-herbalbrews

echo ">> Svět, dimenze a struktury"
mr tectonic terralith aether deep-aether ad-astra incendium nullscape unusual_end jadens-nether-expansion \
   just-in-nether nethers-exoticism towns-and-towers explorify repurposed-structures-forge \
   moogs-voyager-structures mvsi-moogs-voyager-structures-integrated mes-moogs-end-structures \
   mns-moogs-nether-structures medieval-buildings medieval-buildings-end-edition create-structures-overhaul \
   yungs-better-dungeons yungs-better-mineshafts yungs-better-strongholds yungs-better-desert-temples \
   yungs-better-jungle-temples yungs-better-ocean-monuments yungs-better-witch-huts yungs-bridges \
   yungs-extras yungs-better-end-island yungs-better-nether-fortresses structurify lootr

echo ">> Dekorace a stavění"
mr macaws-bridges macaws-doors macaws-fences-and-walls macaws-furniture macaws-holidays \
   macaws-lights-and-lamps macaws-roofs macaws-windows handcrafted another-furniture chipped rechiseled \
   decorative-blocks-reborn supplementaries amendments immersive-paintings etched better-fishtanks chimes

echo ">> Doprava, QoL a UI"
mr waystones xaeros-minimap xaeros-world-map xaeros-minimap-world-map-waystones-compatibility-forge \
   small-ships immersive-aircraft elytra-slot carry-on fallingtree rightclickharvest ping-wheel corpse \
   advanced-netherite spartan-shields-unofficial trimseffects jei jade jade-addons-forge \
   justenoughbreeding just-enough-professions-jep just-enough-resources-jer searchables mouse-tweaks \
   inventory-essentials inventoryhudplus item-highlighter obscure-tooltips advancement-plaques \
   better-advancements chat-heads emojiful 3dskinlayers sound-physics-remastered ambientsounds \
   visuality-forge dimension-viewer polymorph attributefix more-hitboxes simple-backups chunky \
   better-compatibility-checker byzantine-styles-pack-for-minecolonies cAHzWsm8 \
   kubejs almostunified spice-of-life-onion crash-assistant idas zeta

echo ">> CurseForge (MineColonies a další)"
cf minecolonies structurize blockui domum-ornamentum multi-piston towntalk stylecolonies \
   christmascolonies jadecolonies the-twilight-forest building-gadgets refurbished-furniture catalogue \
   configured iron-chests ftb-essentials connectivity apothic-spawners ftb-quests-forge

# --- 4) dokončení -----------------------------------------------------------
packwiz refresh >>"$LOG" 2>&1
echo
echo "Hotovo. Modů v packu: $(ls mods/*.pw.toml 2>/dev/null | wc -l | tr -d ' ')"
if [ -s "$FAILED" ]; then
  echo "Nepodařilo se přidat ($(wc -l < "$FAILED" | tr -d ' ')):"; cat "$FAILED"
else
  echo "Všechno se přidalo bez chyby."
fi
echo "Napiš Claudovi, že je hotovo – zkontroluje duplicity a závislosti."
