# Data‑Quality Dashboard (Monorepo)

This repository contains two main components:

| Directory | Purpose |
|---|---|
| `data_quality_dashboard/` | Python script that analyses CSV data quality (record counts, dedupe rates, quality scores). |
| `duckdb/` | The DuckDB source code extension (see its own `README.md`). |

## Quickstart – Data‑Quality Dashboard

```bash
# from the project root
python data_quality_dashboard/data_quality_dashboard.py
```

See the **Runbook** in `data_quality_dashboard/README.md` for adding a vendor, adding a field, or rerunning a batch.

## DuckDB Extension

The `duckdb/` directory is the official DuckDB repository (see its `README.md` for build/install instructions).

---
*Generated automatically – add or update READMEs as the project evolves.*