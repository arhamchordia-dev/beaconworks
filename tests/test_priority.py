import sys
import os
from datetime import datetime, timezone

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from src.lib.priority import compute_score

# High urgency, Enterprise, freshly opened -> weights only, no days-open term
now = datetime.now(timezone.utc)
fresh = compute_score({"urgency": "high", "created_date": now.isoformat()}, "Enterprise", now)
assert fresh == 70, f"expected 70, got {fresh}"

# Low urgency, SMB, 14+ days open (capped) -> full days-open term applies
stale = compute_score({"urgency": "low", "created_date": "2020-01-01T00:00:00+00:00"}, "SMB", now)
expected = round(0.3 * 40 + 0.4 * 30 + 30, 2)
assert stale == expected, f"expected {expected}, got {stale}"

print("test_priority.py: OK")
