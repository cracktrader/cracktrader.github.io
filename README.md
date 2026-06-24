# CrackTrader

Source for <https://cracktrader.github.io/>, the public front door for a private,
internally used runtime for quantitative research, simulation and execution.

The core product is not contained in this repository. This static site documents
selected architecture, runtime guarantees, operating modes and scoped engineering
evidence without publishing strategy logic, credentials, live data, trading results
or proprietary datasets.

Detailed technical documentation remains at
<https://cracktrader.github.io/docs/>.

## Local preview

```bash
python scripts/check_site.py
python -m http.server 4174
```
