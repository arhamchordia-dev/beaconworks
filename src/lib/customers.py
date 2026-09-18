"""Customer lookups, backed by the fixture generated from the data room."""
import json
import os

_FIXTURES = os.path.join(os.path.dirname(__file__), "..", "fixtures", "customers.json")
with open(_FIXTURES) as f:
    CUSTOMERS = json.load(f)


def get_customer(customer_id: str):
    """
    Returns the customer record, or None if it does not exist.

    Seeded bug (lesson 15.3): CUST-0007 (Harbor Bridge Financial) is present
    in tickets.json and sales_transactions.csv but deliberately absent from
    customers.json, mirroring a real broken foreign-key reference. This
    function does NOT special-case it -- it returns None honestly. The bug
    lives in server.py, which currently does not check for that None result
    before using it. Fix the caller, not this function.
    """
    for c in CUSTOMERS:
        if c["customer_id"] == customer_id:
            return c
    return None


def list_customers():
    return CUSTOMERS
