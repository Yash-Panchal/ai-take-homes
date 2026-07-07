# Call — Granite Peak Outfitters × BetterBark · Admin sync
Date: 2026-06-25 · Call ID: call-080
Participants: [EXTERNAL] Fiona Delacroix, Finance Manager (Granite Peak Outfitters) · [EXTERNAL] Wes Hartland, HR Operations (Granite Peak Outfitters) · [INTERNAL] Lena Kowalski, Implementation

[INTERNAL] Lena Kowalski: Hi Fiona, hi Wes. Thanks for the time. Wes, you and I have talked before, Fiona I think this is our first call?
[EXTERNAL] Fiona Delacroix: First time, yes. I'm on the finance side, Wes pulled me in because this touches billing.
[INTERNAL] Lena Kowalski: Perfect, glad you're here. Wes, you set this up as an admin sync — what's on your list?
[EXTERNAL] Wes Hartland: Couple of housekeeping things and then the bigger one, which is really Fiona's, about how billing works. Let's do housekeeping first, it's quick.
[INTERNAL] Lena Kowalski: Go for it.
[EXTERNAL] Wes Hartland: First, we added the seasonal retail crew last month and I want to confirm they provisioned cleanly. I think they did but want to double-check.
[INTERNAL] Lena Kowalski: Let me look. Your last bulk upload was — yes, the 30th of May, one hundred and twelve members, all provisioned, no errors in the log. Clean.
[EXTERNAL] Wes Hartland: Great, that's what I hoped. Second thing — a couple of those folks are already leaving, seasonal churn. I just deactivate them in the admin console, right?
[INTERNAL] Lena Kowalski: Correct, Admin, Members, select them, Deactivate. Frees the seat for reuse. You've done it before, same flow.
[EXTERNAL] Wes Hartland: Cool. And when the seasonal folks come back next year, I just reactivate rather than re-adding them fresh?
[INTERNAL] Lena Kowalski: Right, reactivate keeps their history. Re-adding creates a brand-new record. For returning seasonals, reactivate is the way.
[EXTERNAL] Wes Hartland: Good, that saves the re-onboarding hassle. A lot of them come back every season, so that's handy.
[INTERNAL] Lena Kowalski: It's built for exactly your pattern — a workforce that ebbs and flows. Deactivate in the off-season, reactivate when they return.
[EXTERNAL] Wes Hartland: Perfect. That's my housekeeping. Fiona, you're up.
[EXTERNAL] Fiona Delacroix: Right. So this is the real reason I'm on. It's about how our invoices come through, and it's a finance headache more than a product complaint.
[INTERNAL] Lena Kowalski: Tell me the headache, that's what I'm here for.
[EXTERNAL] Fiona Delacroix: So right now we get one invoice from you. One line, total seats, total dollars. Simple on your end.
[INTERNAL] Lena Kowalski: Right, single consolidated invoice for the whole account.
[EXTERNAL] Fiona Delacroix: The problem is, internally, we don't run as one bucket. We have distinct departments with their own budgets — retail, warehouse, corporate, guiding operations. Each has its own cost center.
[INTERNAL] Lena Kowalski: And each department's leadership owns their own P&L.
[EXTERNAL] Fiona Delacroix: Exactly. So when your single invoice hits, I have to manually split it across four cost centers. And I have to figure out how many seats belong to each department to allocate the dollars fairly.
[INTERNAL] Lena Kowalski: How many departments are we talking, and roughly how many seats each?
[EXTERNAL] Fiona Delacroix: Four departments. Retail's the biggest at around two hundred, warehouse about one-fifty, corporate maybe a hundred, and guiding operations the rest.
[INTERNAL] Lena Kowalski: So no trivial rounding — each department is a meaningful chunk of the bill. How are you doing that split today?
[EXTERNAL] Fiona Delacroix: By hand. I pull the member roster, tag each person to their department off a separate HR spreadsheet, count heads per department, then apportion the invoice total by headcount. Every single month.
[INTERNAL] Lena Kowalski: That sounds like a couple of hours of reconciliation monthly.
[EXTERNAL] Fiona Delacroix: Two to three hours, and it's error-prone. If Wes moves someone between departments and I don't catch it, my allocation's wrong and a department gets over- or under-charged.
[EXTERNAL] Wes Hartland: Which then lands on me, because the department head emails asking why their coaching bill went up.
[INTERNAL] Lena Kowalski: So there's a real workflow cost here, and it's recurring. What would the ideal look like from your side, Fiona?
[EXTERNAL] Fiona Delacroix: Honestly? If the invoice itself broke out the cost by department. So instead of one line "600 seats, X dollars," it'd say "retail: 200 seats, this much; warehouse: 150 seats, this much; corporate; guiding; each on its own line."
[INTERNAL] Lena Kowalski: A per-department billing split on the invoice, with seats and dollars allocated per department, so finance can map each line straight to a cost center.
[EXTERNAL] Fiona Delacroix: Yes. That's it precisely. Then I just forward each line to the right cost center and I'm done. No manual apportioning, no spreadsheet cross-referencing.
[INTERNAL] Lena Kowalski: That would eliminate the two-to-three hours and the allocation errors entirely. And it would use the department assignment you already maintain in the platform, presumably.
[EXTERNAL] Fiona Delacroix: Right — Wes already tags everyone to a department in your system for the org chart. That data exists. It just doesn't flow to the invoice.
[EXTERNAL] Wes Hartland: That's the frustrating part. The department structure is already in there. It's just not connected to billing.
[INTERNAL] Lena Kowalski: That's a strong point — the data's already captured, it's the billing document that doesn't surface it. Let me make sure I've got the request crisply so I can take it to our billing product team.
[EXTERNAL] Fiona Delacroix: Please.
[INTERNAL] Lena Kowalski: The ask: on the invoice, split the charge by department — using the department assignments already in the platform — showing seats and dollar amount per department, so finance can allocate each department's coaching spend to its own cost center without manual reconciliation. Right?
[EXTERNAL] Fiona Delacroix: That is exactly right. You said it better than I did.
[INTERNAL] Lena Kowalski: I want to be straight with you — this isn't something the product does today, and it's not a quick config toggle. It's a billing feature that would need product work. But it's a clear, well-justified request and I'm logging it as such with your workflow cost attached.
[EXTERNAL] Fiona Delacroix: I figured it wasn't a switch you could flip. I just want it on the list, because it's real money and real time.
[INTERNAL] Lena Kowalski: It's going on the list with your numbers — two-to-three hours monthly, four cost centers, allocation-error risk. That impact framing is what moves these things.
[EXTERNAL] Wes Hartland: And if there's any interim way to make Fiona's life easier before that exists?
[INTERNAL] Lena Kowalski: The one thing I can offer today — the bulk CSV export of the member roster shipped recently. It includes department if you've tagged it. Fiona, that at least gives you a clean per-department headcount export instead of cross-referencing a separate HR sheet.
[EXTERNAL] Fiona Delacroix: Oh, that would help. Right now I'm pulling the roster and the HR sheet separately and matching them. If the roster export already has the department column, that's half my work gone.
[INTERNAL] Lena Kowalski: It does, as long as Wes's department tags are current. It's Admin, Members, "Export all CSV." That's the interim; the invoice split is the real fix I'm filing.
[EXTERNAL] Wes Hartland: I keep the department tags current, so that export should be accurate. That's a nice stopgap, Fiona.
[EXTERNAL] Fiona Delacroix: It is. Doesn't solve the invoice, but it saves me the matching step. I'll take it.
[INTERNAL] Lena Kowalski: One question so I frame the request well — is this a nice-to-have, or is it causing a real problem with your department heads today?
[EXTERNAL] Fiona Delacroix: It's causing friction. When my allocation's off by even a few seats, a department head disputes their charge and it escalates to our CFO. It's happened twice this year.
[INTERNAL] Lena Kowalski: So there's an actual escalation cost, not just Fiona's time. That's exactly the kind of impact that gets a feature prioritized.
[EXTERNAL] Wes Hartland: The last dispute took a week to resolve. That's a week of finger-pointing over a spreadsheet error that shouldn't be possible.
[INTERNAL] Lena Kowalski: I'll put the escalation history in the write-up. "Manual allocation causes billing disputes that reach the CFO" is a much stronger case than "it takes a few hours."
[EXTERNAL] Fiona Delacroix: Exactly. It's not the hours, it's the credibility hit when I get it wrong.
[INTERNAL] Lena Kowalski: Good. So to recap: your seasonal crew provisioned clean, deactivation flow confirmed, I'm filing the per-department invoice-split feature request with your workflow cost, and I'll send Fiona the CSV export path as an interim. Anything else?
[EXTERNAL] Fiona Delacroix: That's everything from finance. Thank you for taking the invoice thing seriously, most vendors tell me to just deal with it.
[INTERNAL] Lena Kowalski: It's a legitimate ask and a common one for multi-department accounts. You won't be the last to want it. Wes, anything to add?
[EXTERNAL] Wes Hartland: Nope, you covered my housekeeping and Fiona's big one. Good call.
[INTERNAL] Lena Kowalski: Then I'll follow up in writing with the export path and the request confirmation. Thanks both.
[EXTERNAL] Fiona Delacroix: Thank you, Lena.
[EXTERNAL] Wes Hartland: Thanks. Bye.
[INTERNAL] Lena Kowalski: Take care. Bye now.
