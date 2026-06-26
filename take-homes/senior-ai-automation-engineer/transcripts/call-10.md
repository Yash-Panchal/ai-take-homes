# Call — Atlas Financial × BetterUp · Security Follow-up
Date: 2026-06-20 · Call ID: call-10
Participants: [EXTERNAL] Renee Park, IT Security Lead (Atlas Financial) · [INTERNAL] Tomás Vela, Implementation

[EXTERNAL] Renee: One more from our security team: we need programmatic access to the audit log. There's a UI view today, but we need an API endpoint to pull audit events into our SIEM on a nightly job. A manual CSV export won't satisfy continuous monitoring.
[INTERNAL] Tomás: So an audit-log export API, SIEM-friendly, not just the in-app view.
[EXTERNAL] Renee: Right. It's a hard requirement for our SOC 2, so it will keep coming up until it exists. Separate from the role-mapping ask — this is about getting events out.
[INTERNAL] Tomás: Understood, logging it as its own request.
