import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from src.lib.customers import get_customer

known = get_customer("CUST-0001")
assert known is not None, "CUST-0001 should exist"

# This is the seeded-bug assertion for lesson 15.3: the record genuinely
# does not exist. The test documents the bug's true cause -- it is not
# testing that the app crashes, it is testing that the DATA gap is real,
# so the fix belongs in server.py's handling, not in fabricating a record.
missing = get_customer("CUST-0007")
assert missing is None, "CUST-0007 is deliberately absent"

print("test_customers.py: OK")
