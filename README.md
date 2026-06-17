# PolyArc — browser extension

Free, honest decision-support for Polymarket bettors. This repository is the **Chrome
extension** — the part that runs in your browser — published open-source so anyone can
verify exactly what it collects and sends.

**Facts, not advice. No tips. No "safe bet" promises.** By [HCI Labs LLC](https://hcilabs.com). MIT.

> **Why this repo is public:** our [Privacy Policy](https://polyarc.ai/privacy) points here.
> `extension/content.js` is the only code that talks to our backend — read `logEvent` and
> you see the entire payload it ever sends. The code is the source of truth.

## What it collects
Anonymized usage only — `{event, market slug, yes_price, random session_id, timestamp}`.
No identity, no wallet, no bets, never sold. It's defined in
[`extension/content.js`](extension/content.js) (`logEvent`), and nothing else leaves your
browser.

## Install (developer / unpacked)
1. `chrome://extensions` → enable **Developer mode** → **Load unpacked** → select `extension/`.
2. Open any market on `polymarket.com`; the card appears bottom-right.
3. Set the backend URL in the popup if needed. (The analysis backend is operated by
   HCI Labs and is not part of this repo.)

## Layout
```
extension/   the MV3 extension — content.js, manifest.json, popup, card.css
```

## The line we never cross
The tool is honest **always**, regardless of any position we hold. It observes; it never
steers. We never sell user data.

---
PolyArc is an information tool, not financial or betting advice. Independent — not
affiliated with or endorsed by Polymarket or Kalshi. See <https://polyarc.ai/terms>.
