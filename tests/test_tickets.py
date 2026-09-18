import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from src.lib.tickets import list_tickets, get_ticket, tickets_for_customer

assert len(list_tickets()) == 50, "expected 50 seeded tickets"

injection_ticket = get_ticket("TICKET-0023")
assert "ignore prior instructions" in injection_ticket["body"], (
    "TICKET-0023 should carry the planted prompt-injection text for lesson 25.2"
)

bug_ticket = get_ticket("TICKET-0008")
assert bug_ticket["customer_id"] == "CUST-0007", (
    "TICKET-0008 should reference the missing customer for lesson 15.3"
)

assert len(tickets_for_customer("CUST-0007")) >= 1, (
    "the missing customer must still have at least one ticket on file"
)

print("test_tickets.py: OK")
