"""Ticket lookups, backed by the fixture generated from the data room."""
import json
import os

_FIXTURES = os.path.join(os.path.dirname(__file__), "..", "fixtures", "tickets.json")
with open(_FIXTURES) as f:
    TICKETS = json.load(f)


def list_tickets():
    """
    Lists tickets. NOTE (lesson 13.4 "Make and inspect a small change"):
    this function deliberately does not support filtering by status yet --
    adding a `status` filter here (and a matching query param in server.py)
    is the small, reviewable change that lesson walks through. Do not add
    it ahead of time; the diff is the point of the lesson.
    """
    return TICKETS


def get_ticket(ticket_id: str):
    for t in TICKETS:
        if t["ticket_id"] == ticket_id:
            return t
    return None


def tickets_for_customer(customer_id: str):
    return [t for t in TICKETS if t["customer_id"] == customer_id]
