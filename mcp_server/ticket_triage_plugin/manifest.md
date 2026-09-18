# BeaconWorks Ticket-Triage Plugin (Project 7 package)

For lesson 22.3 "Package a skill and server" and the Project 7 deliverable
("MCP ticket-triage plugin with tests and security notes").

## Package tree
```
mcp_server/
  server.py                 -- the three read-only tools
  requirements.txt
  ticket_triage_plugin/
    manifest.md              -- this file
    SKILL.md                 -- the skill half of the package (22.3)
    security_notes.md         -- Project 7's required security notes
```

## Capabilities exposed
- `lookup_ticket(ticket_id)`
- `lookup_customer(customer_id)`
- `search_tickets(category, urgency)`

All three are read-only. No write, no external network call, no email
send -- consistent with the course's rule that MCP tools here never
replace the approval-gated write path in the main app (see
`data_room/company/approval_policy.md`).

## UI is optional (lesson 22.4)
The package works headless: any MCP client can call the three tools above
with no UI at all. A ticket-panel UI is an optional Apps-SDK-style add-on
demonstrated in 22.4, but installing this plugin on the web does not
deploy any lifecycle hook scripts -- match the course doc's own caution on
this point exactly.
