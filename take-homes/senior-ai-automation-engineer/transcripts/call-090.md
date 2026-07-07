# Call — BetterUp Internal · Support triage rotation sync
Date: 2026-06-20 · Call ID: call-090
Participants: [INTERNAL] Ravi Patel, Support Engineer · [INTERNAL] Lena Kowalski, Implementation · [INTERNAL] Derek Okafor, CSM · [INTERNAL] Sam Oduya, CSM

[INTERNAL] Ravi: Alright, triage rotation sync, the weekly thrill ride. Everyone here? I see Lena, Derek, Sam. Good.
[INTERNAL] Sam: Present and caffeinated.
[INTERNAL] Lena: Present and not, my machine died this morning so I'm running on tea, which is not the same.
[INTERNAL] Derek: Tea is a lifestyle choice, Lena, own it.
[INTERNAL] Lena: It's a hostage situation, not a choice. My grinder broke.
[INTERNAL] Ravi: Tragic. We'll hold a moment of silence for the grinder. Who's got the doc pulled up?
[INTERNAL] Derek: I've got it. Do we want to start with the rotation coverage or the escalation backlog?
[INTERNAL] Ravi: Coverage first, it's the boring administrative part and I want to get it out of the way before people mentally check out on me.
[INTERNAL] Sam: Rude, but fair.
[INTERNAL] Ravi: So next week. I'm on point Monday and Tuesday. Lena, you said you could take Wednesday and Thursday?
[INTERNAL] Lena: Wednesday yes, Thursday I've got the Nordvik implementation kickoff that's going to eat my whole afternoon. I can cover Thursday morning but I need someone for the afternoon.
[INTERNAL] Derek: I can float Thursday afternoon. My calendar's light.
[INTERNAL] Ravi: Great. And Friday?
[INTERNAL] Sam: I'll take Friday. Everyone always dumps Friday on me because I don't complain loudly enough.
[INTERNAL] Ravi: You just complained.
[INTERNAL] Sam: It doesn't count if it's true.
[INTERNAL] Lena: Put Sam down for Friday before he develops a spine about it.
[INTERNAL] Derek: Done. Rotation's covered. That was almost painless.
[INTERNAL] Ravi: Don't say that, you'll summon a P1. Okay, backlog. We came into the week with 34 open tickets, we're at 27 now, net down seven, which is good.
[INTERNAL] Sam: What drove the drop, anything notable or just steady churn?
[INTERNAL] Ravi: Mostly steady churn. A batch of "how do I reset my password" and "where's the export button" tickets that are really enablement questions dressed up as support tickets. I keep saying we should route those to the CSMs upfront.
[INTERNAL] Derek: We should. Half of what hits your queue is stuff a CSM could answer in one Slack message. What if we set up a first-pass filter, anything that's clearly a how-to gets bounced to the account's CSM before it becomes a ticket?
[INTERNAL] Ravi: I'd love that but let's not design a whole new workflow in a rotation sync, let's take it to the ops meeting. Note it, move on.
[INTERNAL] Lena: Noted. "Explore routing how-to questions to CSMs, discuss at ops."
[INTERNAL] Ravi: Perfect. Now the ones I actually want eyes on. We've got three that have been open more than five business days and I don't love that.
[INTERNAL] Derek: Which ones?
[INTERNAL] Ravi: First, the Beaumont Insurance thing. The Ping lockout. That one's mine and it's moving, engineering's got it, I gave the customer a status yesterday. It's high-sev but it's not stuck, it's just genuinely hard. I don't need help, I just want it visible.
[INTERNAL] Sam: That's the 24-hour hard lockout one? I saw the escalation fly by. Nasty.
[INTERNAL] Ravi: Very. But well-handled, the customer's happy with the responsiveness even if the fix isn't in yet. Leave it with me.
[INTERNAL] Derek: Consider it visible and not touched. What's number two?
[INTERNAL] Ravi: Second is an implementation handoff that stalled. Lena, this is yours, the Grafton Utilities SSO config. It's been waiting on their IT team to send us metadata for six days.
[INTERNAL] Lena: Ugh, yes. That's not us, that's them. Their IT is slammed. I've pinged twice. I don't think there's anything to do but keep nudging, it's blocked on the customer.
[INTERNAL] Ravi: Fine, but let's not let it rot silently. Can you set a nudge for every two business days and loop their CSM so there's account pressure too?
[INTERNAL] Lena: Who's on Grafton?
[INTERNAL] Derek: That's me. I'll lean on my champion there, they respond to me faster than to a support ping. I'll get their IT unstuck.
[INTERNAL] Lena: Perfect, tag me when the metadata lands and I'll finish the config same day.
[INTERNAL] Ravi: Good. Third one, and this is the annoying one. We've got a ticket that's basically a mystery. Customer says "reports look wrong" with zero specifics. No account context, no screenshot, no page, no repro. Sam I think it came in through one of yours but it's unclear.
[INTERNAL] Sam: "Reports look wrong" is not a ticket, it's a vibe.
[INTERNAL] Ravi: It's a vibe with a ticket number. I've asked for specifics twice and gotten nothing back. I'm inclined to move it to "waiting on customer" and let it auto-close if they don't respond in five days.
[INTERNAL] Derek: That's reasonable. We can't chase a ghost. If it's real they'll re-report with detail.
[INTERNAL] Sam: Agreed, park it. I'll do a soft check with the account just so it doesn't look like we ignored them, but yeah, no specifics, no ticket.
[INTERNAL] Ravi: Perfect. That's the aged three. Everything else in the queue is under five days and moving normally.
[INTERNAL] Lena: Can I raise a process thing quickly? The handoff from CSM to support is inconsistent. Sometimes I get a beautiful ticket with logs and repro steps, sometimes I get "customer mad, plz help." The Beaumont one was a great example of good handoff, the customer had logs ready. The reports-look-wrong one is the anti-example.
[INTERNAL] Ravi: Totally agree, and that's a training thing not a today thing. Let's add "handoff quality template" to the ops agenda alongside the CSM-routing idea. Two process items for ops, we're not solving them here.
[INTERNAL] Derek: Logged both. Ops agenda: CSM routing for how-to questions, and a handoff quality template.
[INTERNAL] Sam: We're very good at generating agenda items for meetings that aren't this one.
[INTERNAL] Ravi: It's how we survive. Okay, anything else burning? Any P1 smoke on the horizon anyone's hearing about from their accounts?
[INTERNAL] Derek: Nothing from mine beyond Beaumont, which is already in hand.
[INTERNAL] Sam: Quiet week for me too, knock on wood.
[INTERNAL] Lena: Nothing. Just the metadata I'm waiting on.
[INTERNAL] Sam: Before we wrap, one tiny non-urgent thing. The on-call phone handoff, whoever's got the physical escalation line, we keep forgetting to actually hand it off in the calendar. I got paged Saturday for a shift I wasn't on because the calendar still said me.
[INTERNAL] Ravi: Ugh, that's the second time. Was it a real page or a false alarm?
[INTERNAL] Sam: False alarm thankfully, a customer testing their webhook at 2am. But I was awake for nothing.
[INTERNAL] Lena: The eternal 2am webhook tester. There's always one.
[INTERNAL] Derek: Can we just automate the calendar handoff off the rotation sheet? Feels scriptable.
[INTERNAL] Ravi: Probably, but that's a "someone owns a small project" thing, not a today thing. Sam, since it bit you, want to own scoping it?
[INTERNAL] Sam: Sure, I'll scope automating the on-call calendar handoff and bring options to ops. Low priority, but I'd like to sleep.
[INTERNAL] Ravi: Reasonable ask. Noted as a third ops item, owned by Sam, low priority. Okay, now we're done early, which never happens. Recap: rotation is me Mon-Tues, Lena Wed and Thursday AM, Derek Thursday PM, Sam Friday. Derek unsticks Grafton's IT and loops Lena. Sam soft-checks the reports-look-wrong account then we park it for auto-close, and Sam also scopes the on-call calendar automation. Beaumont stays with me, visible not touched. Ops items: CSM routing, handoff template, and the on-call automation.
[INTERNAL] Derek: That's it.
[INTERNAL] Sam: A clean sync. Now I've definitely jinxed us.
[INTERNAL] Ravi: You absolutely have. See everyone next week, assuming no P1 tonight.
[INTERNAL] Lena: Thanks all.
[INTERNAL] Derek: Later.
