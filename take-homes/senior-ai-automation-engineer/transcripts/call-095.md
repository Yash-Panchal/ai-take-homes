# Call — Northgate Security × BetterUp · Admin sync
Date: 2026-06-26 · Call ID: call-095
Participants: [EXTERNAL] Wesley Amara, Director of IT Operations (Northgate Security) · [EXTERNAL] Fatima Rahim, HRIS Administrator (Northgate Security) · [INTERNAL] Lena Kowalski, Implementation

[INTERNAL] Lena: Wesley, Fatima, thanks for the sync. Before we dive in, how's Northgate doing generally, I know summer's a big season for event security.
[EXTERNAL] Wesley: Slammed, in a good way. Festival season means we're standing up temporary teams for events constantly, which honestly is a preview of the exact pain we're here to talk about.
[EXTERNAL] Fatima: Festival season is when I most want to throw my laptop, so the timing of this call is perfect.
[INTERNAL] Lena: Then let's make it count. I set this up to talk through your team-structure management, so I want to use the time well. Where do you want to start?
[EXTERNAL] Fatima: Probably me first, since I'm the one currently drowning. Then Wesley can talk about the automation side, which is really the bigger ask.
[INTERNAL] Lena: Perfect, that's a good order. Fatima, what's the drowning?
[EXTERNAL] Fatima: So a little context on Northgate. We're a physical security firm, we do guarding contracts, alarm monitoring, event security, that kind of thing. And our org structure is insanely fluid because of how our business works.
[INTERNAL] Lena: How so? Walk me through the churn.
[EXTERNAL] Fatima: We win a new contract, say a shopping mall wants guards, and we spin up a team for that site. We lose a contract, that team dissolves. So we might create and tear down 20, 30 teams in a single month. It never stops.
[INTERNAL] Lena: That's an enormous amount of structural churn compared to most of our accounts. And right now, creating those teams in BetterUp is fully manual?
[EXTERNAL] Fatima: Painfully manual. Every time we win a site, I go into the admin console, hand-create the team, name it, configure it, and assign the members. For one team it's fine, five minutes. When we onboard a regional contract with 15 sites at once, I'm creating 15 teams by hand back to back and I want to throw my laptop across the room.
[INTERNAL] Lena: That's genuinely tedious, and error-prone at that volume too. Let me understand the shape of the pain, is it the team creation itself, or the member assignment, or both?
[EXTERNAL] Fatima: Both are annoying, but the team creation is the part that has literally no shortcut. There's a bulk CSV thing for adding members that I've started using, which helps a lot with assignment. But there's nothing for creating the teams themselves. That's all click, type, save, click new, type, save, repeat.
[INTERNAL] Lena: Good, that distinction matters a lot. So member management has a bulk path via CSV, but team creation is strictly one-at-a-time through the UI with no automation.
[EXTERNAL] Fatima: Exactly. And the CSV import for members has been a lifesaver for the assignment half. It's just the team-creation half that's still stuck in the stone age. And that's where Wesley comes in, because his answer to everything is "why are you doing that by hand."
[INTERNAL] Lena: Ha, a man after my own heart. Wesley, take it away.
[EXTERNAL] Wesley: Before I get on my soapbox, quick context on our scale so you understand the volume. We've got about 340 active sites right now, and the average site relationship lasts maybe eight to fourteen months before the contract ends or renews under a new structure.
[INTERNAL] Lena: So your entire team population turns over roughly annually, structurally speaking.
[EXTERNAL] Wesley: Effectively, yes. It's not that people leave, it's that the containers they sit in are constantly being created and destroyed as contracts churn. That's the fundamental shape of our business.
[INTERNAL] Lena: That's a genuinely different profile than most of my accounts, where teams are stable for years. Your teams are almost ephemeral by design.
[EXTERNAL] Wesley: Ephemeral is the perfect word. And a manual process built for stable orgs breaks completely against ephemeral ones. Which is my whole point. Because you shouldn't be doing that by hand, that's why. Here's the thing, Lena. All of this already exists in our systems. When we win a contract, our operations platform automatically provisions the site, creates the cost center, sets up the shift schedule, all of it. It's fully automated on our side.
[INTERNAL] Lena: So the team already gets created programmatically in your ops platform the moment you win the contract, and then BetterUp is the one place where a human has to manually re-key that same information.
[EXTERNAL] Wesley: Precisely. BetterUp is the only system in our entire stack where a human has to manually mirror an org change that every other system handles automatically. It's the odd one out, and it drives me up the wall.
[INTERNAL] Lena: I can hear that. And it's not just the toil, right, there's a data-quality angle.
[EXTERNAL] Wesley: Huge one. Fatima's human, she'll eventually typo a site name, or transpose a location code, or miss one during a big onboarding when she's doing 15 in a row. And then the team structures drift out of sync between our ops platform and BetterUp, and reconciling that drift is its own miserable job.
[EXTERNAL] Fatima: It's already happened twice. I created "Riverside Mall" in one system and "Riverside Plaza" in the other and it took a week to notice.
[INTERNAL] Lena: That's exactly the kind of silent drift that erodes trust in the data over time. So what you want, at the core, is a programmatic way to create teams.
[EXTERNAL] Wesley: Yes. An API endpoint to create teams. If I could call an API to create a team when our ops platform provisions a new site, I'd wire it into our existing provisioning automation in an afternoon and Fatima would never hand-create a team again. We already script every other part of the org change, we just need the hook on your side to complete the loop.
[INTERNAL] Lena: Let me capture this precisely because it's a clear and well-justified ask. You want an API endpoint to programmatically create teams, so you can integrate team creation into your existing contract-provisioning automation, which eliminates both the manual re-keying toil for Fatima and the data-drift risk between your ops platform and BetterUp.
[EXTERNAL] Wesley: That's it exactly. You nailed it.
[INTERNAL] Lena: And to nail down scope, is it just creating the team, or do you also need the API to handle naming, member assignment, and maybe archiving or deleting a team when a contract ends?
[EXTERNAL] Wesley: Creation is the priority and by far the biggest pain, and it has to include the name and ideally the initial member assignment. But honestly, the full lifecycle would be ideal, create, rename when a site gets renamed, and archive or delete when a contract ends, since teams die about as often as they're born for us.
[INTERNAL] Lena: If you had to pick the must-have versus the nice-to-have?
[EXTERNAL] Wesley: Create is the must-have. Rename and archive are the nice-to-haves. If I had create, I'd wire that up immediately and handle the deletions manually in a monthly batch, that's survivable. It's the constant creation that's the daily bleed.
[EXTERNAL] Fatima: If I could just get creation automated I'd genuinely cry with joy. The occasional deletion I can batch. The constant creation is what's killing me.
[INTERNAL] Lena: Understood. I'll file it with create-team as the primary, must-have ask, and note full-lifecycle, rename and archive, as the ideal extended scope. Now I want to be honest with you both, we do not have a public team-management API today. We have the admin console UI and the bulk CSV for members, but no programmatic team creation. So this is a genuine feature request, not something I can flip on for you.
[EXTERNAL] Wesley: I assumed as much, I'd have found it in your API docs otherwise, and I looked hard. There's a members surface hinted at but nothing for teams.
[INTERNAL] Lena: Your read is exactly right. What I can do is file this as a strongly-justified feature request. And frankly, Northgate is one of the best cases I could bring for it, extremely high team churn, existing automation maturity, a clear data-integrity argument, and a willing integration partner in you. Those are precisely the ingredients product looks for when prioritizing an API.
[EXTERNAL] Wesley: I'll gladly be a design partner. If there's a beta or an early version of the API, I want in. And I'll give you real integration feedback, edge cases and all, not fluff.
[INTERNAL] Lena: What's your stack on the provisioning side, out of curiosity? It helps me describe your integration story to product.
[EXTERNAL] Wesley: Our ops platform exposes webhooks on contract events, and we've got a middleware layer, mostly Python, that fans those out to the downstream systems. Adding a "create BetterUp team" call would just be one more handler in that layer.
[INTERNAL] Lena: That's a clean architecture and it makes the pitch stronger, you're not asking for a magic connector, you're asking for one REST endpoint you'll wire into an existing event-driven system. Product likes hearing the customer already has the plumbing.
[EXTERNAL] Wesley: Exactly. We've done this integration a dozen times with other vendors. BetterUp is genuinely the only one without the hook.
[INTERNAL] Lena: That's a compelling line and I'll use it. Can I quote the concrete numbers, the 20-to-30 teams a month, the 15-site regional onboarding, the Riverside naming mixup?
[EXTERNAL] Fatima: Please quote all of it. Quote the laptop-across-the-room part too, I stand by it.
[INTERNAL] Lena: The laptop shall be quoted for posterity. Concrete toil and a real data-quality incident like the Riverside one are exactly what move a feature up a roadmap, much more than a vague "it'd be nice."
[EXTERNAL] Wesley: What's a realistic timeline expectation? I don't want to build our provisioning roadmap around something that might be vaporware.
[INTERNAL] Lena: I won't give you a fake date, that would be doing you a disservice and it'd burn trust when it slipped. What I'll commit to is filing it with a strong business case, flagging you as a design partner, and coming back to you with product's actual read, whether it's on the near-term roadmap, under consideration, or genuinely not planned. You'll get a straight answer, not a "soon."
[EXTERNAL] Wesley: That's the professional answer and I respect it. So we build our plan around the manual process for now and treat the API as upside if and when it lands.
[INTERNAL] Lena: Exactly the right way to plan it, assume manual, treat the API as a bonus. In the meantime, Fatima, let me make sure you're squeezing everything out of the bulk member CSV so at least the assignment half is as fast as possible. Are you using the full column set?
[EXTERNAL] Fatima: Honestly I'm probably using it at 60 percent of its potential. I figured out the basics and stopped.
[INTERNAL] Lena: Then there's easy time to save there. I'll send you the best-practice guide with a couple of tips specifically for large batches, so at least the member half of a 15-site onboarding is quick even while team creation stays manual.
[EXTERNAL] Fatima: That would genuinely help. Every minute counts during a big onboarding.
[INTERNAL] Lena: Okay, let me recap so we're aligned. I'm filing a feature request for a team-management API, primary must-have is programmatic team creation including name and initial members, extended ask is full lifecycle rename and archive, with Northgate's churn numbers, the Riverside data-drift incident, and Wesley flagged as a willing design partner. I'll come back with product's honest roadmap read, no fake dates. And I'll send Fatima the bulk-CSV best-practice guide for the interim.
[EXTERNAL] Wesley: That covers everything I came in for, and then some.
[EXTERNAL] Fatima: Same. Thank you for taking the automation angle seriously. Most people just tell me to click faster or hire a temp.
[INTERNAL] Lena: Clicking faster is not a strategy, and neither is throwing a human at a machine's job. I'll get this filed today and send that CSV guide over. Thanks both.
[EXTERNAL] Wesley: Appreciated, Lena. One thing, when you get product's read, can you loop me directly rather than routing through Fatima? I'd rather be the technical point of contact on the API side.
[INTERNAL] Lena: Absolutely, I'll make you the primary contact on the feature request and copy Fatima. That way the technical thread goes to you and the ops thread stays with her.
[EXTERNAL] Wesley: Perfect, that's the right split. Talk soon.
[EXTERNAL] Fatima: Thanks Lena, and thanks for the CSV guide in advance.
