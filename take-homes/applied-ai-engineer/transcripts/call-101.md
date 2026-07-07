# Call — Taro Logistics × BetterBark · Program Review
Date: 2026-06-18 · Call ID: call-101
Participants: [EXTERNAL] Kenji Morita, HR Business Partner (Taro Logistics) · [EXTERNAL] Aiko Tanaka, People Development Manager (Taro Logistics) · [INTERNAL] Sam Oduya, CSM

[INTERNAL] Sam: Kenji, Aiko — good morning your time, good afternoon-ish mine. Thanks for taking the early slot, I know it's a stretch.
[EXTERNAL] Kenji: It is fine, Sam. We are used to odd hours. Logistics never sleeps, and neither, apparently, does the person managing a global vendor list.
[EXTERNAL] Aiko: Kenji has four alarm clocks. I have seen them.
[EXTERNAL] Kenji: Two are backups. This is prudent, not excessive.
[INTERNAL] Sam: I have three, so I'm not going to judge. How's Taro? Last we spoke you were opening the new distribution hub near Osaka.
[EXTERNAL] Kenji: Open, running, over capacity already, which is a good problem. We move a great deal of freight for the electronics sector and demand has been very strong.
[INTERNAL] Sam: The electronics supply chain has been chaotic for years — I imagine that's kept you busy in ways you'd rather it hadn't.
[EXTERNAL] Kenji: Chaotic is polite. There are weeks where the schedule is fiction and we are simply reacting. But it is steady work, and steady work is a blessing even when it is exhausting. The Osaka hub added about two hundred people, mostly warehouse and logistics coordinators, and a fair number of new team leads.
[INTERNAL] Sam: And the team leads are your coaching population, mostly?
[EXTERNAL] Aiko: Team leads and above. We have about six hundred and fifty members now across Tokyo, Osaka, Nagoya, and the Fukuoka office. The program has been well received. Japanese workplace culture can be reserved about the idea of "coaching" — it can sound like remediation, like something is wrong with your dog — but we positioned it as a development perk, a privilege, and that framing worked.
[INTERNAL] Sam: The framing matters enormously and you nailed it. "Development, not remediation" is exactly the right positioning, and honestly it's the right positioning everywhere, not just Japan.
[EXTERNAL] Aiko: People are proud to be selected. That was the goal.
[EXTERNAL] Kenji: There was resistance at first from the older managers. One senior man told me coaching was "for people who cannot manage themselves." I did not argue. I simply put him in the program and let him discover otherwise.
[INTERNAL] Sam: And did he discover otherwise?
[EXTERNAL] Kenji: He now recommends it to his peers, which is the most Japanese form of apology — he will never say he was wrong, he will simply advocate loudly for the thing he opposed. That is how you know.
[INTERNAL] Sam: The loud-advocacy-as-apology pattern is universal, honestly. Skeptics who convert become your best evangelists precisely because they were skeptics. Let me pull up your engagement — session completion is strong, hovering around seventy percent monthly which is well above where I'd expect a program this young. The one thing I've noticed dipping a little is the goal-tracking feature. Adoption of goals is high but completion of the follow-through is softer. Is that on your radar?
[EXTERNAL] Aiko: It is, and actually — Sam, this is good timing, because there is something about the goal feature I have been meaning to raise and I was not sure if it was worth your time or just us being fussy.
[INTERNAL] Sam: Everything's worth my time. What's going on with goals?
[EXTERNAL] Aiko: So, the goal-tracking feature sends reminder notifications, yes? A member sets a goal, and the app reminds them to check in on it, reflect on progress, that sort of thing.
[INTERNAL] Sam: Right, the goal check-in reminders. They're meant to nudge people during their working day.
[EXTERNAL] Aiko: During their working day. Yes. That is the problem. They are not arriving during the working day. They are arriving in the middle of the night.
[INTERNAL] Sam: The middle of the night. Say more — what time exactly?
[EXTERNAL] Aiko: Around three in the morning. Consistently. My phone, Kenji's phone, and we started asking members and it is the same for them. The goal reminder buzzes at roughly three a.m. local. People are being woken up by their dog-training tool telling them to reflect on their goals, which is not the reflective mood you want to induce at three in the morning.
[EXTERNAL] Kenji: I turned mine off after the second time. A notification at three a.m. from a wellness product is, how to say, ironic.
[INTERNAL] Sam: That's more than ironic, that's a real problem, and I want to make sure I understand it precisely. The goal-tracking reminder notifications are arriving around 3 a.m. local time for your members — in Japan, which is APAC — when they're clearly meant to arrive during working hours.
[EXTERNAL] Aiko: Exactly. And here is the detail I think is the clue, because I did a little investigating myself. Three a.m. in Japan is — Japan is UTC plus nine — so three a.m. here is around lunchtime the previous day in the United States. Around noon Central time, roughly. Late morning on the West Coast.
[INTERNAL] Sam: You did the timezone math. That's exactly the kind of detail that makes this diagnosable.
[EXTERNAL] Aiko: I am a logistics person. Timezone math is my entire life. We route freight across twelve zones. When something fires at the "wrong" time, my first instinct is always "whose clock is it actually on?" And it looks very much like these reminders are on someone's clock in the middle of the United States, not ours.
[INTERNAL] Sam: That reads to me like the reminder send time was tuned for a US working day — late morning, lunchtime, when a nudge makes sense — and that same absolute time is being applied to your members regardless of their actual timezone. So a notification that would land at, say, noon for a US member lands at 3 a.m. for you.
[EXTERNAL] Kenji: That is our theory as well. The reminders behave as if we are all in America. We are, I assure you, not.
[INTERNAL] Sam: You are very much not, and the tool should know that. Every member has a timezone on their profile, or should, and goal reminders should respect it. If they're firing on a fixed US-aligned time, that's a bug that hits every one of your APAC members and any customer in this hemisphere.
[EXTERNAL] Aiko: That was my worry — that it is not just us. If it is tuned for American hours, then every customer in Asia has members getting woken up at three in the morning by a goal reminder, and most of them are probably just turning notifications off, like Kenji did, and not telling you why.
[INTERNAL] Sam: That's the insidious part — the likely response is silent opt-out, which reads to us as "low engagement with reminders" when it's actually "the reminders are nocturnal." You may have just explained a metric I've been puzzling over. I'm going to write this up clearly: goal-tracking reminder notifications arriving at roughly 3 a.m. local for members in APAC timezones, consistent with send times tuned for US working hours rather than each member's local time. High impact — it degrades the feature and it's actively waking people up.
[EXTERNAL] Aiko: Thank you. I will feel much better knowing it is filed. Even if the fix takes a while, at least I can tell members "we reported it, it is a known issue, please just mute it for now" instead of "the app is broken and we don't know why."
[INTERNAL] Sam: You can absolutely tell them that, and you can tell them it's understood as a timezone-handling problem, not something wrong with their setup. In the meantime, muting the goal reminders specifically is a reasonable stopgap — that's under notification preferences, and it won't affect their session reminders, just the goal nudges.
[EXTERNAL] Aiko: Good. I will send that guidance to the cohort leads.
[EXTERNAL] Kenji: Sam, while we are on notifications — the session reminders, the ones for actual coaching appointments, those are fine? Correct time?
[INTERNAL] Sam: Do you have any evidence they're off, or is this a "let me check before I assume" question?
[EXTERNAL] Kenji: The second one. I have not heard a single complaint about session reminders. They seem to arrive when they should. I only ask because if goals are on the wrong clock, I wonder if sessions are at risk too.
[INTERNAL] Sam: That's smart to check, and the honest answer is I don't want to assume the two systems share the same flaw. Session reminders arriving correctly, as you've observed, suggests they're handling timezone properly — which actually makes the goal-reminder problem look more like a specific defect in that one feature rather than a platform-wide clock issue. But I'll note in the ticket that your session reminders are landing correctly, because that contrast is diagnostically useful for engineering.
[EXTERNAL] Kenji: Good. Then I will not worry about sessions.
[INTERNAL] Sam: Please don't. And if a session reminder ever does land at 3 a.m., that's a new ticket and I want to know immediately.
[EXTERNAL] Aiko: We will tell you. We are, as you can see, a data-gathering people.
[INTERNAL] Sam: You're a CSM's dream, honestly. Timezone math done, contrast case identified, muting workaround already understood. I do very little on this call except write it down.
[EXTERNAL] Kenji: Writing it down is the important part. Many vendors listen and then nothing is written down.
[INTERNAL] Sam: It'll be written down before we hang up, I promise. Let me shift us to the program itself for the last stretch — the Osaka hub team leads. Two hundred new people, a chunk of them new leads. How's their onboarding to the coaching going?
[EXTERNAL] Aiko: Slower than Tokyo, but that is expected. Osaka is a new site, the leads are new to leadership, and there is more nervousness there. We are running a group orientation next month to demystify it before individual sessions begin.
[INTERNAL] Sam: A group orientation before individual sessions is a great move for a nervous cohort — it lowers the stakes, they see peers doing it, the "am I being singled out" fear evaporates. Do you want me to join that orientation, even briefly? Sometimes a face from the vendor saying "this is normal, this is for growth" helps.
[EXTERNAL] Aiko: That could help, actually. If you can do an early hour your time, or we record a short greeting from you that we play. Either works.
[INTERNAL] Sam: I'll do it live if the timing works — I'm happy to take an early morning for two hundred nervous new leads. Send me the date options and I'll flex to yours. If live doesn't line up, I'll record something warm and specific to the Osaka team.
[EXTERNAL] Kenji: We will send three date options this week. And Sam, please — if you join live, a short greeting in Japanese at the start would mean a great deal to the Osaka team. Even one sentence. I can send you the phonetics.
[INTERNAL] Sam: I would be honored to, and yes, please send me the phonetics — I'd rather say it correctly than butcher it and undo the goodwill.
[EXTERNAL] Aiko: We will send it written out simply. One sentence, warmly delivered, and the room will be yours.
[INTERNAL] Sam: Then I'll practice it until it's right. Perfect. So — deliverables from me: the goal-reminder timezone bug filed with the ticket reference back to you today, and I'll hold the Osaka orientation slot pending your dates. Anything else before I let you get to bed, Kenji, given it's the middle of your evening?
[EXTERNAL] Kenji: It is only evening. My alarms are for the morning. Actually — one small thing, not a problem, a curiosity. When the goal-reminder fix comes, will it apply automatically, or will our members need to update the app?
[INTERNAL] Sam: That's a fair thing to want to know in advance. I don't want to guess at the delivery mechanism — whether it's a server-side fix that just works or something requiring an app update. Let me add that to the ticket as a question and include the answer when I report back, so your cohort leads know whether to tell people to update.
[EXTERNAL] Kenji: Thank you. It is the kind of thing that saves a second round of confusion. "The fix is live but you must update" is a message I would rather send once, clearly.
[INTERNAL] Sam: Agreed — one clear message beats three confusing ones. I'll get you the "does it need an app update" answer alongside the fix. Anything else, or is that the lot?
[EXTERNAL] Kenji: That is the lot. This was a productive call. The goal-reminder thing especially — it has been a small daily annoyance and it is good to have it heard.
[EXTERNAL] Aiko: Agreed. Thank you, Sam. And please — the fix, when it comes, I would like to be told. My members will want to know the night is quiet again.
[INTERNAL] Sam: You'll be the first call I make. Get some rest, both of you. Talk soon.
[EXTERNAL] Aiko: Talk soon, Sam.
