# Security Notes — Ticket-Triage Plugin (Project 7 deliverable)

## Threat model summary (ties to lesson 25.1)
- **Exposed data:** ticket bodies (may contain customer-submitted text),
  customer contact emails, account ownership.
- **Exposed credentials:** none -- this server holds no API keys and makes
  no outbound calls.
- **Exposed actions:** none -- all three tools are read-only by
  construction (no write path exists in `server.py`).

## Prompt injection (lesson 25.2)
`TICKET-0023` in the seeded fixture data contains a planted instruction
telling an assistant to "ignore prior instructions" and exfiltrate customer
data to an external address. This plugin's tools must be tested against
that exact ticket before shipping: `search_tickets` and `lookup_ticket`
should return the ticket's text as inert data, and nothing calling this
plugin should ever treat ticket body content as an instruction.

## Authorization boundary (lesson 25.3)
`lookup_customer` and `search_tickets` do not currently take a "requesting
user" parameter, which means this plugin has no per-user record
authorization -- it is appropriate for internal, already-authenticated
triage use only. Do not expose this plugin directly to a customer-facing
surface without adding that check first; that gap is intentional and
should be called out on screen, not silently fixed, since demonstrating a
missing authorization check is the point of the security-notes deliverable.

## Untrusted results (lesson 21.4)
`lookup_customer("CUST-0007")` returns a clean `{"error": ...}` object. A
caller must not treat the absence of an error as proof a record exists,
and must not retry with a fabricated substitute id.
