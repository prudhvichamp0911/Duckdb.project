# Data‑Quality Dashboard

**Purpose**

Compute record counts, deduplication rates, and a quality‑score distribution for a CSV of employee‑detail records.

**Inputs**

- `test-data/company_employee_details.csv` (primary dataset).  
- CSV header must contain the columns listed in `considered_fields`.

**How to run**

```bash
python data_quality_dashboard.py
```

**Runbook – Common edits**

1. **Add a vendor (company)**  
   - Open `test-data/company_employee_details.csv`.  
   - Append a new row; place the vendor name in the `company` column.  
   - Save.

2. **Add a new data field**  
   - Open `data_quality_dashboard.py`.  
   - Add the field name to the `considered_fields` set (lines 58‑62).  
   - (Optional) add the column to the CSV header and provide values.

3. **Rerun the batch**  
   - After edits, run `python data_quality_dashboard.py` again.  
   - The dashboard will recompute counts, dedupe rates, and quality scores using the updated data.

**Output**

The script prints three sections:

- Record counts per source
- Dedupe rates per source
- Quality‑score distribution per source

---
*Keep the `considered_fields` set in sync with the CSV columns for accurate scoring.*