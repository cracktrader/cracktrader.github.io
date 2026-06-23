# Cracktrader Engineering

The source for <https://cracktrader.github.io/>: a public engineering overview
of Cracktrader's runtime architecture, operating modes and evidence boundaries.

Cracktrader itself is private software for personal quantitative research and
trading. This repository contains only the static public site. It does not
contain strategies, credentials, live data or private implementation code.

Detailed technical documentation remains at
<https://cracktrader.github.io/docs/>.

## Local preview

```bash
python scripts/check_site.py
python -m http.server 4174
```
