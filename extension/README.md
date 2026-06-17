# PolyArc — Chrome extension (v0)

Free, honest decision-support overlaid on Polymarket market pages. Flags traps
(SafeBet) and shows fee-adjusted base rates (PolyTruth). **Facts, not advice** — no
tips, no "safe bet" promises, no telling you what or how much to bet.

## Run it (local dev)

1. **Start the backend API** (serves the cards from `pred_oltp`):
   ```bash
   OLTP_PG_DSN="host=localhost dbname=pred_oltp user=YOUR_USER password=YOUR_PASSWORD" \
     .venv/bin/python -m uvicorn polyarc.api:app --port 8088
   ```
2. **Load the extension**: Chrome → `chrome://extensions` → enable *Developer mode*
   → *Load unpacked* → select this `extension/` folder.
3. **Use it**: open any market on `polymarket.com`. The card appears bottom-right.
   Set a different backend URL in the extension popup if you host it elsewhere.

## Honest limitations (v0)

- **Coverage**: cards only appear for markets we've captured in `market_covariates`
  (~16K markets). Anything else → "Not yet analyzed" (we won't guess).
- **SafeBet flags are sparse**: wash-trading / concentration / resolution flags exist
  only where the detectors have already scanned; liquidity/spread flags are universal.
  A real launch needs continuous, broad scam-scanning (the main net-new infra).
- **Market-identity extraction** (slug / embedded clobTokenIds) is best-effort against
  a live SPA and may need tuning against Polymarket's current DOM.
- **Hosting**: for sharing beyond your own browser, the backend must be hosted
  somewhere the extension can reach (and locked down) — not localhost.

## The line we never cross

The tool is honest **always**, regardless of any position we hold. It observes; it
never steers. We never sell user data. If those ever bend, the whole thing rots.
