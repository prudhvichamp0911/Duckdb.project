#!/usr/bin/env python3
"""Data quality dashboard: record counts, dedupe rates, quality score distribution per source."""

import csv
from collections import defaultdict
from pathlib import Path

DATA_DIR = Path(__file__).parent / "test-data"
CSV_PATH = DATA_DIR / "company_employee_details.csv"


def load_records(path: Path):
    """Load CSV records, skipping header."""
    records = []
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            records.append(row)
    return records


def compute_record_counts(records):
    """Record counts per source (company)."""
    counts = defaultdict(int)
    for r in records:
        counts[r["company"]] += 1
    return dict(counts)


def compute_dedupe_rates(records):
    """Dedupe rates per source: % of records that are duplicates (by employee_id within source)."""
    by_company = defaultdict(list)
    for r in records:
        by_company[r["company"]].append(r)

    rates = {}
    for company, recs in by_company.items():
        total = len(recs)
        employee_ids = [r["employee_id"] for r in recs]
        unique_ids = set(employee_ids)
        duplicates = total - len(unique_ids)
        rates[company] = round(duplicates / total * 100, 2) if total else 0.0
    return rates


def compute_quality_score(records):
    """Compute a quality score per source based on data completeness.

    Score is based on: non-null fields / total fields per record, averaged per source.
    Fields considered: company, department, employee_id, age, salary, annual_bonus,
    prior_years_experience, full_time, part_time, contractor.
    """
    by_company = defaultdict(list)
    for r in records:
        by_company[r["company"]].append(r)

    scores = {}
    considered_fields = {
        "company", "department", "employee_id", "age",
        "salary", "annual_bonus", "prior_years_experience",
        "full_time", "part_time", "contractor",
    }

    for company, recs in by_company.items():
        total = len(recs)
        total_fields = 0
        non_null_fields = 0
        for r in recs:
            for field in considered_fields:
                val = r.get(field, "")
                total_fields += 1
                if val not in ("", "0.0", "0", "1.0", "0.0", "0.5") and val is not None:
                    non_null_fields += 1
        scores[company] = round(non_null_fields / total_fields * 100, 2) if total_fields else 0.0
    return scores


def main():
    records = load_records(CSV_PATH)

    record_counts = compute_record_counts(records)
    dedupe_rates = compute_dedupe_rates(records)
    quality_scores = compute_quality_score(records)

    print("=" * 60)
    print("DATA QUALITY DASHBOARD")
    print("=" * 60)

    print("\n--- Record Counts per Source ---")
    for company in sorted(record_counts):
        print(f"  {company}: {record_counts[company]} records")

    print("\n--- Dedupe Rates per Source ---")
    for company in sorted(dedupe_rates):
        print(f"  {company}: {dedupe_rates[company]}% duplicate records")

    print("\n--- Quality Score Distribution per Source ---")
    for company in sorted(quality_scores):
        print(f"  {company}: quality score {quality_scores[company]}%")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()