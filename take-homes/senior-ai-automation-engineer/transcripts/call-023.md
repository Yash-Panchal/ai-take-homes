# Call — Nordvik Shipping × BetterUp · QBR
Date: 2026-06-23 · Call ID: call-023
Participants: [EXTERNAL] Henrik Bauer, VP HR (Nordvik Shipping) · [EXTERNAL] Lise Andersen, HR Operations Analyst (Nordvik Shipping) · [INTERNAL] Maya Chen, CSM

[INTERNAL] Maya: Henrik, Lise — welcome. Quarterly review. I've got the standard deck but Henrik, you mentioned wanting to keep it tight, so tell me what actually matters to you this quarter.
[EXTERNAL] Henrik: Tight is correct. I have a board thing after this. Let's do: are people using it, is it working, and then Lise has a reporting requirement that's become important. That last one is the real reason we asked for the full slot.
[INTERNAL] Maya: Then we'll spend our time there. Quick on the first two: activation is 71% across your 800 seats, steady quarter over quarter. Your shore-side staff engage well; your seafaring crew less so, which is expected given connectivity at sea.
[EXTERNAL] Henrik: The ships are always going to lag. I've made peace with it. Bandwidth on a container vessel is not what it is in the office.
[EXTERNAL] Lise: And just so it's on the record, the seafaring numbers aren't a program failure, they're a physics failure. There's no coaching app that beats a satellite blackout.
[INTERNAL] Maya: Agreed, and I'll never present the ship numbers as an adoption problem — it's a connectivity constraint, full stop. Right, and your shore numbers carry the program. Completion rates on the shore side are actually strong — better than most logistics accounts I run.
[EXTERNAL] Henrik: Give me the shore-side completion number specifically, I want it for my own deck.
[INTERNAL] Maya: Shore-side session completion is running about 82% — meaning of the sessions booked, 82% actually happen and aren't cancelled or no-showed. Logistics as a sector usually sits in the 60s, so you're well above.
[EXTERNAL] Henrik: 82. Good. The ships drag that down if you blend them, yes?
[INTERNAL] Maya: They do — blended you're around 71%, because the seafaring crew book and then miss when they lose connectivity mid-voyage. If you report shore-side separately it's a much better story, and it's a fair separation to make given the connectivity reality.
[EXTERNAL] Henrik: I'll report it separately then. The board doesn't need to know a sailor missed a session because he was in the middle of the Pacific.
[INTERNAL] Maya: That's a defensible cut and I'll give you both numbers labeled clearly so nobody accuses you of cherry-picking. Shore-side and blended, side by side.
[EXTERNAL] Henrik: Good. I never cherry-pick, I "provide appropriate context." Legal taught me that phrasing.
[INTERNAL] Maya: I'm stealing "appropriate context" for my own reports. Okay — the second question, is it working.
[EXTERNAL] Henrik: Good. That's the population we're really investing in anyway — the operations and commercial staff on land. Fine. Lise, take it, this is your thing.
[EXTERNAL] Lise: Okay. So this is the thing that's turned into a headache for me specifically. Nordvik is organized in a way that matters here — everyone belongs to a cost center and a region. Cost center is finance's world; region is operational. Every employee has both, and those two attributes drive basically all of our internal reporting.
[INTERNAL] Maya: Cost center and region as core attributes on every person. Got it.
[EXTERNAL] Lise: Right. Now — when I pull data out of your platform, I get member name, email, activation status, session counts, that whole standard set. What I cannot get is cost center or region, because your system doesn't know they exist. There's nowhere to put them.
[INTERNAL] Maya: So the platform has no field for cost center or region on a member profile, and therefore they're not in your exports.
[EXTERNAL] Lise: Exactly. And here's why it's a problem and not just a nice-to-have. My CFO wants coaching engagement broken down by cost center, because that's how he thinks about everything — cost center is his native language. And our COO wants it by region, because she runs the org geographically. I currently cannot give either of them what they want from your data.
[INTERNAL] Maya: How are you handling it now, if the data isn't there?
[EXTERNAL] Lise: Manually, and it's miserable. I export the member list from you, then I export a separate roster from our HRIS that has everyone's cost center and region, and I VLOOKUP the two together in a spreadsheet by email address. Every single month. It takes me the better part of a day and it breaks constantly because people's emails don't always match perfectly between systems.
[INTERNAL] Maya: So you're stitching our export to your HRIS roster by hand, monthly, and it's brittle on the email match.
[EXTERNAL] Lise: Brittle is generous. Last month twelve people fell out of the join because their email in your system was a nickname format and their HRIS email was formal — like "j.smith" versus "john.smith" — and I didn't catch it until the CFO asked why a whole cost center looked empty. That was a fun afternoon.
[INTERNAL] Maya: That's a real failure mode, and it's exactly the kind of thing that erodes trust in the numbers even when the numbers are fine.
[EXTERNAL] Lise: Right! The data's correct, my process is just held together with tape and a prayer. And it's not scalable — we're growing, we just acquired a regional carrier, so now there are more cost centers and more regions, and my spreadsheet is going to buckle.
[INTERNAL] Maya: So what would solve this cleanly — and I want to get your exact ask right — is the ability to store custom attributes like cost center and region directly on the member profile in our platform, so they'd flow through to the exports natively. Then you'd pull one report from us that already has cost center and region on it, no VLOOKUP.
[EXTERNAL] Lise: Yes. That's precisely it. Custom fields on the member profile — cost center, region, and honestly I'd love a couple more like "business unit" and "employee type" — that come out in the export. Then I hand the CFO his cost-center cut and the COO her regional cut straight from your system, and I never open that cursed spreadsheet again.
[INTERNAL] Maya: And ideally those custom fields would be settable when you provision members — so as you onboard the acquired carrier's people, you'd stamp their cost center and region up front rather than backfilling.
[EXTERNAL] Lise: That would be the dream. Set it at provisioning, whether that's the CSV import or through the admin panel, and then it just persists on the profile and appears in every export from then on.
[INTERNAL] Henrik: Maya, I want to be blunt about why this matters to me and not just to Lise. My CFO decides whether we renew and expand. If I can hand him engagement broken down by his cost centers, this becomes a tool he understands and defends. If I can't, it stays a fuzzy "people thing" he tolerates. The custom fields are, weirdly, a renewal argument.
[INTERNAL] Maya: That's an important framing and I'm going to carry it. This isn't a cosmetic reporting nicety — it's the difference between the CFO seeing this as a governable line item versus an opaque one. Let me make sure I capture the whole shape: custom fields on member profiles — cost center and region at minimum, ideally business unit and employee type too — settable at provisioning via CSV or admin, persisting on the profile, and flowing through to all data exports.
[EXTERNAL] Lise: And to be clear on scope so it's filed right — I need it on every member, not just new hires. The whole roster, all 800, because the CFO wants historicals too. New-only would be useless to me.
[INTERNAL] Maya: Important distinction — backfillable for existing members and settable for new ones. I'll say both explicitly, because "new members only" wouldn't solve your reporting problem at all.
[EXTERNAL] Lise: Right, it has to cover the people I already have. Okay — but yes, that sentence you said before. Can I marry that sentence.
[INTERNAL] Maya: I'll put it in the request verbatim. This is a genuine product gap, not a config I can flip on for you — there's no place to store those attributes today — so I'm filing it as a feature request with your account and Henrik's renewal rationale attached. It's a common enough need with matrixed and multi-entity orgs that it'll resonate.
[EXTERNAL] Henrik: How common? Because if we're the only ones asking, it dies in a backlog.
[INTERNAL] Maya: You're not the only ones — organizations with cost-center accounting or multi-region structures hit this regularly, and the acquisition angle you have makes it sharper. I can't promise a timeline, but I can promise it's a recognized pattern and I'll represent the demand honestly, yours included.
[EXTERNAL] Henrik: That's all I can ask. Represent it well.
[INTERNAL] Maya: I will. Lise, in the meantime, one thing that might reduce your VLOOKUP pain: if you can get the emails to match exactly between our system and your HRIS — standardize on the formal format on our side — you'd stop losing people in the join. It doesn't fix the missing fields, but it makes your stopgap less brittle.
[EXTERNAL] Lise: That's fair. I can push to normalize the emails on your side to match HRIS. It won't kill the spreadsheet but it'll stop the silent drop-outs, which is the part that burned me.
[INTERNAL] Maya: Exactly — it de-risks the failure mode that embarrassed you with the CFO. I'll send you a short note on how to bulk-update the member emails to the formal format.
[EXTERNAL] Lise: Please. That alone saves me a bad afternoon.
[INTERNAL] Henrik: Good. Maya, we're at time — I've got the board. Recap for me quickly?
[INTERNAL] Maya: You've got it: I file the custom-fields feature request — cost center, region, and ideally business unit and employee type, settable at provisioning and flowing to exports — with your renewal rationale attached. I send Lise the email-normalization note as an interim measure. And I'll follow up with a request reference so you can point the CFO to it.
[EXTERNAL] Henrik: Good. That last part matters — a reference number makes it real to him. Thank you, Maya. Lise, anything else?
[EXTERNAL] Lise: No, that's the whole mountain. Thank you — genuinely, this has been on my plate for months and it's the first time someone's written it down the way I actually mean it.
[INTERNAL] Maya: That's the job. Go to your board, Henrik. Lise, watch for that email today.
[EXTERNAL] Henrik: Appreciated. Talk next quarter.
[EXTERNAL] Lise: Oh — one more tiny thing before Henrik runs, and it's not a problem, just a question. The acquired carrier's people, when I onboard them, is there a bulk way or is it one at a time?
[INTERNAL] Maya: Bulk. You've got a CSV import for member provisioning — Admin, Members, import. You map the columns and it creates them in one go. I'll include the import guide with the email-normalization note so it's all in one place.
[EXTERNAL] Lise: Perfect, that saves me from adding two hundred people by hand. Thank you.
[INTERNAL] Maya: Of course. And once the custom-fields request lands, that same import would carry the cost center and region columns — which is the whole point.
[EXTERNAL] Lise: Full circle. Okay, now I'm actually done. Henrik, go to your board.
[EXTERNAL] Henrik: Going. Thank you both — genuinely productive. Maya, we'll see the request reference and the pricing options at the renewal.
[INTERNAL] Maya: You will. Have a good board meeting, Henrik.
[EXTERNAL] Henrik: They're never good, but they're mercifully short.
[INTERNAL] Maya: The best kind of board meeting. Go — I've got everything I need from here.
[EXTERNAL] Henrik: Good. Bye now.
[EXTERNAL] Lise: Bye, Maya. And thank you again — really.
[INTERNAL] Maya: Talk next quarter. Bye both.
