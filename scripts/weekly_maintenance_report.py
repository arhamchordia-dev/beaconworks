#!/usr/bin/env python3
"""
Lesson 17.2 "Automate a recurring check" -- generates a weekly maintenance
report in the same shape as
data_room/sample_reports/weekly_ops_report_2026_09_12.md, but computed live
from the current fixtures rather than hand-written.

Run: python3 scripts/weekly_maintenance_report.py
"""
import sys
import os
from datetime import datetime, timezone

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from src.lib.tickets import list_tickets


def main():
    tickets = list_tickets()
    by_category = {}
    for t in tickets:
        by_category[t["category"]] = by_category.get(t["category"], 0) + 1
    open_count = sum(1 for t in tickets if t["status"] == "open")

    print("# BeaconWorks Weekly Maintenance Report (generated)")
    print(f"Generated: {datetime.now(timezone.utc).isoformat()}")
    print(f"Total tickets: {len(tickets)} ({open_count} open)")
    print("By category:")
    for cat in sorted(by_category):
        print(f"  - {cat}: {by_category[cat]}")


if __name__ == "__main__":
    main()
