# Call — Gardner Aerospace × BetterBark · Support Escalation
Date: 2026-06-25 · Call ID: call-065
Participants: [EXTERNAL] Renata Voss, HR Systems Manager (Gardner Aerospace) · [EXTERNAL] Devon Marsh, Employee Experience Specialist (Gardner Aerospace) · [INTERNAL] Ravi Patel, Support Engineer · [INTERNAL] Sam Oduya, CSM

[INTERNAL] Sam: Renata, Devon — thanks for making time. I brought Ravi from our support engineering team since Renata's ticket had some technical meat to it and I'd rather he hear it firsthand than get it thirdhand from me.
[EXTERNAL] Renata: Appreciate that. I've been burned by the telephone-game version of support before.
[INTERNAL] Ravi: Hi both. I read the ticket but I always learn more from the conversation, so treat me as a fresh set of ears.
[INTERNAL] Sam: Before we dig in — how's Gardner? You had that big program push to the manufacturing floor last we spoke.
[EXTERNAL] Renata: The floor rollout went well, actually. Better than the office rollout, if I'm honest. Machinists showed up.
[EXTERNAL] Devon: They showed up because we made it dead simple. One QR code by the time clock, scan, you're in. No friction.
[INTERNAL] Sam: A QR code by the time clock is genuinely clever. I'm stealing that for other manufacturing accounts.
[EXTERNAL] Devon: Steal away. It was Renata's idea, she gets the credit.
[INTERNAL] Sam: How'd you land on the time clock specifically?
[EXTERNAL] Devon: It's the one place every single person on the floor has to be, twice a day. Guaranteed eyeballs.
[INTERNAL] Sam: Guaranteed-eyeballs is exactly the adoption principle most rollouts miss. Nice.
[EXTERNAL] Devon: We got lucky it worked. It was a guess that paid off.
[EXTERNAL] Renata: I'll accept the credit and the blame, which brings us neatly to why we're here, because the thing I'm about to describe is making the floor rollout look bad and it's not my QR code's fault.
[INTERNAL] Sam: Ominous but well-segued. Take us through it.
[EXTERNAL] Renata: Okay. So context: Gardner is aerospace, we're a serious-quiet-focus culture, and a lot of our people are protective of their attention.
[INTERNAL] Ravi: The kind of culture where a buzzing phone is a genuine offense.
[EXTERNAL] Renata: Exactly. When they onboarded, a bunch of them went into the app and deliberately turned off notifications. Session reminders, nudges, the goal-tracking pings, all of it.
[INTERNAL] Ravi: So they opted out on purpose, not by accident.
[EXTERNAL] Renata: Very much on purpose. They don't want their phone buzzing on the shop floor or during focus time. It was a deliberate choice.
[INTERNAL] Ravi: Reasonable. And they successfully turned those off?
[EXTERNAL] Renata: Yes. It worked. For a while.
[INTERNAL] Ravi: I hear a "for a while."
[EXTERNAL] Renata: Then — and this is the problem — every time the mobile app updates, those settings get wiped. The notification preferences reset back to the defaults, which is everything ON. So people who explicitly opted out suddenly start getting buzzed again, and they're furious, because they made a choice and the app un-made it.
[INTERNAL] Ravi: Let me make sure I've got the shape. A member opts out of notifications. The app pushes an update. After the update, their notification preferences are back to the default all-on state, re-subscribing them to everything they'd turned off. Is that it?
[EXTERNAL] Renata: That's exactly it. The update resets them to defaults and re-opts-them-in.
[INTERNAL] Ravi: And this happens on every app update, or was it a one-time thing after a specific version?
[EXTERNAL] Renata: Every update, as far as we can tell. Devon's tracked it more closely than I have.
[EXTERNAL] Devon: Yeah. It's happened at least three times now, each time lining up with an app update. I keep a little log because people complain to me directly. After the update in — I want to say early May — I got eleven complaints in two days, all the same thing: "why is BetterBark buzzing me again, I turned this off." Then it went quiet. Then the next update, another wave.
[INTERNAL] Ravi: Eleven in two days is a real signal, not a fluke. Is this iOS, Android, or both?
[EXTERNAL] Devon: Both. I've got iPhone complainers and Android complainers in the same wave. It's not platform-specific from what I can see.
[INTERNAL] Ravi: Both platforms, correlated with app updates, resets opt-outs back to all-on. That's a clear reproduction pattern. Do you know if it's just the mobile app's notification settings, or does it also affect what they'd set on the web?
[EXTERNAL] Renata: Good question. We think it's the mobile settings specifically — the ones you set in the app itself. Devon, did anyone say their web preferences changed?
[EXTERNAL] Devon: No one mentioned web. The complaints are all "the app started buzzing me." Push notifications, specifically. Nobody complained about email changing.
[INTERNAL] Ravi: So it's scoped to the in-app push notification preferences, reset to default after an app update, on both platforms. That's a tight, useful description. I'm going to be honest with you — this is a real bug, and the "opted-out users get re-subscribed" part is the sharp edge, because it's not just annoying, it's the app overriding a deliberate user choice.
[EXTERNAL] Renata: That's exactly why it's escalated and not just a ticket sitting in a queue. In our culture, buzzing someone who explicitly asked not to be buzzed reads as the tool not respecting them. And these are the same skeptical machinists we worked hard to get onboarded. A few of them have threatened to just delete the app, and if they do, my whole floor rollout starts unraveling.
[INTERNAL] Sam: So the business impact is retention of the exact population you fought hardest to activate. That's the framing I want in the write-up — not "notifications are annoying," but "opted-out users are being silently re-subscribed on every update, threatening the floor adoption we just won."
[EXTERNAL] Renata: That's the framing. It's a trust thing more than a technical annoyance, though it's obviously also a technical bug.
[INTERNAL] Ravi: It's both, and I'll capture both. The mechanism — preferences not persisting across app updates, defaulting back to all-on — is the engineering description. The impact — deliberate opt-outs overridden, at-risk adoption — is the why-it-matters. Devon, that log you keep, with the dates of the complaint waves lined up against the app update dates — could you send me that? Correlating your complaint timestamps with our release dates would basically hand engineering the repro on a plate.
[EXTERNAL] Devon: I can absolutely send that. It's a scrappy spreadsheet but it's got dates and counts.
[INTERNAL] Ravi: Scrappy is fine, dates and counts are exactly what I need. That turns "customer says it resets" into "customer complaint spikes correlate one-to-one with our release dates," which is a much stronger case internally.
[EXTERNAL] Renata: Is there anything we can do in the meantime? Because the next update is presumably coming and I'd like to not have another wave.
[INTERNAL] Ravi: Let me be straight — I can't stop the reset from a support seat, that's an engineering fix. But two things I can offer. One, I can put a note in your account so that when this ships fixed, you're notified directly rather than finding out from a changelog. Two, for the most vocal opted-out members, there may be an account-level notification preference we can set server-side that's stickier than the in-app toggle — I need to verify that actually survives the update before I promise it, so let me test it and come back to you rather than send you down a false path.
[EXTERNAL] Renata: I'd rather you test it than promise it. Sending my machinists a workaround that also fails would be worse than doing nothing.
[INTERNAL] Ravi: Agreed completely, that's why I won't hand it over untested. I'll try it against a test account through a simulated update on our side and only tell you it works if it actually does.
[INTERNAL] Sam: And I want to set expectations on timeline honestly. Ravi files this today with Devon's correlation data. It's a clear, reproducible bug affecting a deliberate user setting, which usually gets it prioritized, but I'm not going to invent a date. What I can promise is you'll hear from us on where it lands, and Ravi comes back to you on the server-side workaround either way.
[EXTERNAL] Renata: That's a fair deal. I don't need a date, I need to know it's real and it's moving and I'm not going to be surprised by the next wave with no warning.
[INTERNAL] Sam: You won't be surprised — that's the part I can guarantee, the communication. Devon, when's your read on the next likely app update? Just so we're all watching the same window.
[EXTERNAL] Devon: Updates seem to come every few weeks. Historically I'd guess we're due within the next two, three weeks based on the pattern.
[INTERNAL] Ravi: Then let me prioritize testing that server-side workaround this week, so if a workaround exists it's in your hands before the next update rather than after the next wave.
[EXTERNAL] Renata: That would genuinely help. Thank you for treating this like the trust problem it is and not just a settings complaint.
[INTERNAL] Ravi: It's the trust problem that makes it worth prioritizing, honestly. A settings complaint I'd fix quietly. Users being silently re-opted-in against their explicit choice is the kind of thing that erodes a whole rollout, and those are worth moving on.
[INTERNAL] Sam: Let me recap so nothing drops. Ravi files the notification-preferences-reset bug today, scoped to in-app push, both platforms, resetting to all-on after app updates, with the opted-out-users-re-subscribed impact and Gardner's floor-adoption risk. Devon sends the complaint-wave log so we can correlate to release dates. Ravi tests a server-side notification-preference workaround this week and reports back honestly on whether it survives an update. And I flag the account so you're notified directly when the fix ships. Renata, Devon — did I get it all?
[EXTERNAL] Renata: You got it all. That's the most productive support call I've had in a while.
[EXTERNAL] Devon: I'll have that log to Ravi within the hour. It's already open on my other screen.
[INTERNAL] Ravi: Perfect, I'll watch for it. And Devon — the fact that you keep that log is why this call was useful. Most accounts just say "it feels like it happens a lot" and we're stuck.
[EXTERNAL] Devon: I'm a compulsive spreadsheet person. Finally paid off.
[INTERNAL] Sam: It absolutely paid off. Thanks, both — we'll be in touch this week.
[EXTERNAL] Renata: Thank you. Talk soon.
[EXTERNAL] Devon: Bye, and watch for the email.
[INTERNAL] Ravi: Watching for it. Bye.
