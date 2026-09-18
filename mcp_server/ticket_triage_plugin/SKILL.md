---
name: beaconworks-ticket-triage
description: Look up and search BeaconWorks support tickets and customer accounts (read-only) via the ticket-triage MCP server, for triage and reporting tasks.
---

# BeaconWorks Ticket Triage

Use the `lookup_ticket`, `lookup_customer`, and `search_tickets` MCP tools
from `mcp_server/server.py` to answer questions about open support tickets
and the accounts behind them.

## When to use this
- A question names a specific ticket id or customer id.
- A question asks "which tickets are high urgency / in billing / etc."

## What this skill will not do
- It will not draft or send a customer reply -- that requires the approval
  flow in the main dashboard app, per `data_room/company/approval_policy.md`.
- It will not return a fabricated customer record. If `lookup_customer`
  returns `{"error": ...}`, say so plainly; do not guess at the missing
  fields.

## Example
> "What's the status of the Harbor Bridge Financial account?"
1. Call `lookup_customer("CUST-0007")`.
2. It returns an error -- the record does not exist in the current table.
3. Report that honestly, and point to `TICKET-0008`, which documents the
   dashboard bug behind that gap, rather than inventing an account status.
