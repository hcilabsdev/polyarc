# Privacy

The canonical, always-current Privacy Policy is at **<https://polyarc.ai/privacy>**.
The short version:

- We log **anonymized usage** — which markets you view, when, and the price at the time,
  under a **random per-install ID** — to see if the tool is useful and to study aggregate
  market attention. The entire payload is `{event, market, yes_price, session_id, ts}`.
- We do **not** collect your identity, wallet, or bets (side or size). We **never
  front-run you** — only the crowd's aggregate attention, never an individual's bet.
- We **never sell your data**. Our grades stay honest regardless of any position we hold.
- The **one exception** is the Premium waitlist: if you choose to give us your email, it's
  stored separately, used only to notify you at launch, and never sold.

**The code is the source of truth.** `extension/content.js` (`logEvent`) is the only code
that sends anything to our backend — read it and confirm this matches. The backend can't
receive more than the client sends.

Questions / removal: privacy@hcilabs.com · Operated by HCI Labs LLC (Georgia, USA).
