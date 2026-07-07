# Call — Atlas Financial × BetterUp · Security Follow-up
Date: 2026-06-20 · Call ID: call-010
Participants: [EXTERNAL] Renee Park, IT Security Lead (Atlas Financial) · [INTERNAL] Tomás Vela, Implementation

[INTERNAL] Tomás: Renee, round two. Give me one second — let me close this other tab so my calendar stops pinging at me. Okay. How's the week been?
[EXTERNAL] Renee: Busy in the way that means nothing's on fire, which I'll take. It's audit season, so my whole world is spreadsheets and evidence requests right now.
[INTERNAL] Tomás: Audit season. The most wonderful time of the year.
[EXTERNAL] Renee: For someone, somewhere, sure. Not for me. Anyway — did the vendor letter on Friday's incident help with your auditors, since you asked?
[INTERNAL] Tomás: That's actually where I was headed. Did it land?
[EXTERNAL] Renee: It did, thank you. My audit lead read it, grunted approvingly, which for him is a standing ovation, and filed it. One incident officially put to bed. Now I've got two more items, both from the security team, both real.
[INTERNAL] Tomás: You said as much after Wednesday's review. Before we dig in — how much time do you have? I don't want to rush the precise parts.
[EXTERNAL] Renee: I blocked forty-five. Plenty. My next thing isn't until the top of the hour and it's a stand-up I can skip if I have to.
[INTERNAL] Tomás: Forty-five is more than enough. Let's take them in whatever order you want.
[EXTERNAL] Renee: Let's do the audit-log one first, it's cleaner. We need programmatic access to the audit log. There's a UI view today, which is genuinely fine for spot checks — if I want to see who changed a config last Tuesday, I click in and I see it.
[INTERNAL] Tomás: But spot checks aren't the use case.
[EXTERNAL] Renee: The UI's fine for the "who touched this on Tuesday" moment. It's just not a machine.
[INTERNAL] Tomás: Right — clicking around is great for a human being curious, terrible for a robot on a schedule.
[EXTERNAL] Renee: Right. Our SOC team needs to pull audit events into our SIEM on a nightly job. Automated, unattended, every night. So what I need is an API endpoint — filterable by time range, paginated, machine-readable. JSON, ideally. Give me "all audit events between these two timestamps," let me page through them, done.
[INTERNAL] Tomás: So an audit-log export API — time-range filterable, paginated, machine-readable — that a nightly job can hit without a human in the loop.
[EXTERNAL] Renee: Exactly. And I want to be clear about why the UI export button doesn't count, because someone will suggest it. A human clicking "export CSV" once a week is not continuous monitoring. It's a person, doing a manual task, on a schedule they'll eventually forget. Our SOC 2 auditors will keep writing it up as a control gap until an automated pull exists. Continuous monitoring means no human touches it.
[INTERNAL] Tomás: Understood — the manual CSV export doesn't satisfy the control because the control requires automation, not a diligent human. I'll file this as its own feature request: audit-log export API, SIEM-friendly, built for a nightly automated pull, with the SOC 2 continuous-monitoring context attached.
[EXTERNAL] Renee: And keep it separate from the role-mapping request from Wednesday. Different control, different auditors, honestly different people on my side own each one. I don't want them collapsed into one ticket where one blocks the other.
[INTERNAL] Tomás: Agreed, and that's an important distinction — the SAML group-to-role mapping from Wednesday and this audit-log export API are two independent items. I'll file them as two, cross-reference them so anyone reading sees they're both from Atlas, but they stand alone and neither gates the other.
[EXTERNAL] Renee: Perfect. Keep them separate. My auditors would find a way to blame me if one ticket blocking another made us miss a control.
[INTERNAL] Tomás: They sound like a fun crowd.
[EXTERNAL] Renee: They're paid to assume the worst. It's a feature, not a bug — I'd just rather they aim it at someone else. Okay, second item, and this one surfaced in yesterday's pilot group, so it's fresh.
[INTERNAL] Tomás: Go ahead.
[EXTERNAL] Renee: When one of our users changes their network password — our regular rotation — and then hits your app, they get stuck in a login loop. And I want to walk you through the exact loop, because I need you to file this precisely.
[INTERNAL] Tomás: Please, walk me through it step by step.
[EXTERNAL] Renee: Give me a second, I want to get the order right — I watched one of my users do it over the shoulder yesterday, so this is from life, not a guess.
[INTERNAL] Tomás: Take your time, I'm typing as you go.
[EXTERNAL] Renee: User changes their password on our side. Then they open your app. Your app bounces them to our IdP to authenticate. The IdP authenticates them just fine — new password, correct, no problem, IdP says "yes, this is them." IdP sends them back to your app. And then your side immediately bounces them right back to the IdP again. And around, and around. Authenticate, return, bounce, authenticate, return, bounce. Infinite.
[INTERNAL] Tomás: So it's a genuine redirect loop — they authenticate successfully every time, but your app keeps rejecting the returned session and kicking them back out to the IdP.
[EXTERNAL] Renee: That's it exactly. They never get in. Not "logged in briefly then out" — they never reach the app at all. It just spins between your login and our IdP until they give up.
[INTERNAL] Tomás: "Until they give up" being the part that turns into a ticket.
[EXTERNAL] Renee: Every time. The user tries twice, decides it's broken, and calls my helpdesk instead of figuring it out themselves.
[INTERNAL] Tomás: And is there any workaround?
[EXTERNAL] Renee: Clearing browser cookies for your domain breaks the loop. Once they wipe your cookies, they log in clean and they're fine. But that's a support call every single time — you can't tell four hundred people "clear your cookies" and expect that to scale.
[INTERNAL] Tomás: Half of them wouldn't know how to find their cookie settings, and the other half would clear the wrong browser.
[EXTERNAL] Renee: You've met our users. That's exactly how the first three tickets went — "which browser, where's the menu, what's a cookie." I'm not building a training program around that.
[INTERNAL] Tomás: No, that's not a workaround, that's a helpdesk queue. Now — I want to make sure I don't mis-file this, because there's a known issue that sounds adjacent and I do not want to conflate them. There's a tracked issue where SSO sessions expire earlier than the configured lifetime — but that one is specific to Okta-federated setups, and it's an early logout, not a loop. Users get kicked out sooner than they should, then log back in fine.
[EXTERNAL] Renee: Right, and I actually read about that one in your status-page history, and I want to be emphatic: this is not that. Two reasons. One — we are not on Okta. We're Azure AD. So the Okta-specific issue doesn't even apply to us architecturally.
[INTERNAL] Tomás: That alone rules it out. What's the second reason?
[EXTERNAL] Renee: Two — the symptom is the opposite shape. In the Okta issue, people are being logged out early but they can get back in. In ours, nobody is being logged out early at all — they can't get in in the first place after a password change. It's not a premature expiry, it's a hard redirect loop that blocks entry entirely until cookies are cleared. Early-logout-but-you-can-return versus cannot-enter-at-all. Different shape entirely.
[INTERNAL] Tomás: Agreed completely, and thank you for being that precise, because it would have been easy to file this against the wrong issue. So — this is its own distinct bug: Azure AD federated users, after a network password change, hit an infinite redirect loop between our app and their IdP, cannot log in at all, and clearing cookies for our domain is the only workaround. That is not the Okta early-expiry issue — different IdP, different symptom, and in this case people are locked out rather than logged out early.
[EXTERNAL] Renee: Filed exactly like that, yes. If it lands on the Okta ticket it'll get closed as a duplicate and we'll be stuck.
[INTERNAL] Tomás: I've seen that movie. Someone triages by keyword, sees "login" and "SSO," and merges two unrelated things into one grave.
[EXTERNAL] Renee: And then it's my problem to resurrect it three weeks later when nothing's moved. No thank you.
[INTERNAL] Tomás: It won't. It's its own item. How many users so far?
[EXTERNAL] Renee: Five, out of the forty-person pilot. Which is what you'd expect, because password rotation is staggered — not everyone hit their rotation date in the same week. So five have rotated and hit the loop; the other thirty-five just haven't rotated yet.
[INTERNAL] Tomás: So this isn't a five-user edge case, it's a five-so-far because only five have crossed the trigger.
[EXTERNAL] Renee: Nobody hit it in the first week of the pilot at all, which is exactly why — none of them had rotated yet.
[INTERNAL] Tomás: So the trigger's the rotation date, not the login. Makes sense.
[EXTERNAL] Renee: Precisely, and here's the math that matters for prioritization. At full rollout — four hundred users, ninety-day rotation policy — every single person hits a password change once a quarter. That's roughly four hundred people hitting this loop over a quarter, every quarter, forever. It would swamp our helpdesk. It turns a pilot annoyance into a rollout blocker.
[INTERNAL] Tomás: That projection absolutely belongs in the ticket, because you're right — "five pilot users" reads as minor, but "every one of four hundred users, every ninety days, on rotation" reads as a systemic blocker. The rotation math is the whole story. I'll put the repro and that projection right at the top.
[EXTERNAL] Renee: Good. The number is what'll get it taken seriously. Five is ignorable, four-hundred-a-quarter is not.
[INTERNAL] Tomás: You'd have made a good CSM, you know. You lead with the impact number instead of burying it.
[EXTERNAL] Renee: Years of learning that "please fix this" gets ignored and "this will cost us X" gets a meeting. Sad, but true.
[INTERNAL] Tomás: Understood. So I'm filing two new items today: the audit-log export API with the SOC 2 continuous-monitoring framing, and the Azure AD post-password-change redirect loop with the repro and the rotation math — explicitly flagged as distinct from the Okta early-expiry issue.
[EXTERNAL] Renee: And keep the role-mapping item from Wednesday moving too. That's still open, still the biggest one. Three things standing between us and September now — role mapping, audit API, and this login loop.
[INTERNAL] Tomás: All three tracked and pushed. Role mapping's already filed with the audit-blocker context; these two join it today. I'll send you the three ticket links so you can watch them and cite them to your auditors as "vendor is tracking."
[EXTERNAL] Renee: That's exactly what my auditors want to see — tracked, referenced, moving. Send them over.
[INTERNAL] Tomás: You'll have them by end of day. Same time next week to check progress?
[EXTERNAL] Renee: Book it. Weekly cadence is working for me through audit season — keeps me from having to chase you.
[INTERNAL] Tomás: Agreed, let's hold the standing weekly until you're through September. I'll keep the same slot.
[EXTERNAL] Renee: Works. If a week's ever quiet we'll just make it a five-minute check and get our afternoons back.
[INTERNAL] Tomás: Deal. I'll take a short call over a surprise any day.
[EXTERNAL] Renee: Book it. And Tomás — thanks for not filing the loop against the Okta ticket. The last vendor I worked with would have.
[INTERNAL] Tomás: Different IdP, opposite symptom — it's a different bug and it gets its own ticket. Talk next week, Renee.
