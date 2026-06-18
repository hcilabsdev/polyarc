#!/usr/bin/env bash
# Builds the Chrome Web Store upload package from the production manifest.
# Excludes dev-only files (manifest.dev.json, this script, README, scratch).
set -euo pipefail
cd "$(dirname "$0")"

VERSION=$(grep -o '"version": *"[^"]*"' manifest.json | head -1 | sed 's/.*"\([0-9.]*\)"/\1/')
OUT="polyarc-store-${VERSION}.zip"
rm -f "$OUT"

zip -r "$OUT" \
  manifest.json \
  content.js \
  card.css \
  popup.html \
  popup.js \
  icons/icon16.png icons/icon32.png icons/icon48.png icons/icon128.png \
  >/dev/null

echo "Built $OUT"
unzip -l "$OUT"
