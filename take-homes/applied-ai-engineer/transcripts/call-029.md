# Call — Hanamura Trading × BetterBark · Quarterly Business Review
Date: 2026-06-18 · Call ID: call-029
Participants: [EXTERNAL] Kenji Watanabe, People Operations Director (Hanamura Trading) · [INTERNAL] Maya Chen, CSM

[INTERNAL] Maya: Kenji, morning — or, well, evening for you, right? What time is it there?
[EXTERNAL] Kenji: Just past nine. It's fine, I'm a night person. My family's asleep, so this is honestly the quiet part of my day.
[INTERNAL] Maya: I appreciate you staying up for it. We can keep it tight if you want.
[EXTERNAL] Kenji: No, no. I actually have a decent list this quarter, so let's use the time.
[INTERNAL] Maya: Perfect. Let me share the QBR deck and then we'll go off-script wherever you want. Can you see it?
[EXTERNAL] Kenji: I see the title slide. "Hanamura Trading — Q2 Review." Yes.
[INTERNAL] Maya: Great. So headline — you're in a really healthy spot. Activation across your enrolled population is at 74%, which is up from 66 last quarter.
[EXTERNAL] Kenji: That's better than I expected, honestly. We had a rough patch in April where I thought engagement was sliding.
[INTERNAL] Maya: What happened in April?
[EXTERNAL] Kenji: Reorg. We folded the Osaka logistics group into the main commercial org, and for a few weeks nobody knew who reported to whom. People stop doing their training sessions when they're worried about their jobs.
[INTERNAL] Maya: That's fair. But it recovered — May and June are both trending up. Your Tokyo commercial team especially, they're your power users.
[EXTERNAL] Kenji: They love it. My VP over there, Aiko, she's basically become an unpaid evangelist. She brings it up in her staff meetings.
[INTERNAL] Maya: We should send Aiko something. A mug or nothing, but something.
[EXTERNAL] Kenji: She'd frame the mug. Don't tempt me.
[INTERNAL] Maya: Noted for later. Okay, session volume — you did about 1,400 sessions this quarter, coaches are getting strong satisfaction scores, and your no-show rate is down to 4%, which is genuinely good.
[EXTERNAL] Kenji: The reminders help. The nudges. People complain about notifications until the day they miss a session because they turned them off.
[INTERNAL] Maya: The eternal tension. Alright, before I go into the coach-utilization slide — you said you had a list. Do you want to run it now while you're thinking of it, or after?
[EXTERNAL] Kenji: Let's do it now, actually, because the first one has been bugging me and I want to make sure I explain it right.
[INTERNAL] Maya: Go for it.
[EXTERNAL] Kenji: So. We onboarded a new cohort in early June. About 320 people, mostly from the Osaka and Fukuoka offices — the ones from the reorg who hadn't been enrolled yet.
[INTERNAL] Maya: Right, the folded-in group.
[EXTERNAL] Kenji: Yes. And rather than send 320 individual invites, my coordinator used the bulk import. The CSV upload, the members import.
[INTERNAL] Maya: The Admin > Members > Import flow, yeah.
[EXTERNAL] Kenji: Correct. She built the file from our HRIS export — name, email, team, employee ID in a custom column. Uploaded it. The tool said it succeeded. Green checkmark, "import complete," some number of members added.
[INTERNAL] Maya: Okay. And?
[EXTERNAL] Kenji: And then two weeks later people started emailing me saying they never got their welcome email and they can't find their account. At first I assumed they were in the wrong, you know, they typed their email wrong or they're looking in spam.
[INTERNAL] Maya: The usual suspects.
[EXTERNAL] Kenji: The usual suspects. So I tell my coordinator to check. And she goes into the members list and counts. And we're short. We uploaded 320 rows. There are 291 members in the system.
[INTERNAL] Maya: Twenty-nine missing.
[EXTERNAL] Kenji: Twenty-nine missing. And no error. No warning. Nothing said "29 rows failed." The import just... quietly did 291 of them and told us it was done.
[INTERNAL] Maya: That's not good. Let me make sure I understand — the file had 320 data rows, the import reported success, and 291 members landed, with no failure notice for the other 29.
[EXTERNAL] Kenji: Exactly. And here's the part that took us a while to see. My coordinator, she's sharp, she pulled the 29 missing ones into a separate list to see what they had in common. And it's the names.
[INTERNAL] Maya: The names?
[EXTERNAL] Kenji: The 29 that got skipped — every single one has a name written in kanji or katakana in the name field. Non-Latin characters. The ones that came through, either they had Latin-alphabet names, or the coordinator happened to have romanized them — Watanabe instead of 渡辺, that kind of thing.
[INTERNAL] Maya: Oh. So the rows where the member's name contained Japanese characters were the ones that silently dropped.
[EXTERNAL] Kenji: That's our theory, yes. We haven't proven it exhaustively but the correlation is 29 for 29. Every skipped row has non-Latin characters in the name. Every included row is Latin, or was romanized.
[INTERNAL] Maya: And to be clear, these people otherwise have valid data — real emails, real teams?
[EXTERNAL] Kenji: Completely valid. Same format as everyone else. The only difference is the script the name is written in. And most of our workforce writes their name in Japanese, obviously, so this isn't an edge case for us. It's a structural problem. If I re-run any import with real Japanese names, I'm going to lose rows every time.
[INTERNAL] Maya: Yeah. And the thing that makes this genuinely dangerous is the silence. If it had thrown an error — "29 rows failed, here they are" — you'd have caught it in five minutes. Instead you found out from angry members two weeks later.
[EXTERNAL] Kenji: That's the real issue for me. I don't even mind if certain rows can't import for some technical reason, as long as it tells me which ones. I can fix a list of 29. What I can't do is trust an import that lies about being complete.
[INTERNAL] Maya: No, that's exactly right, and I want to write this up carefully. Let me read it back to you so I capture it. CSV member import silently skips rows whose name field contains non-Latin characters — Japanese in your case. No error is shown, the import reports success, the rows simply don't appear. Confirmed with a 320-row file where 291 imported and the 29 skipped all had kanji or katakana names.
[EXTERNAL] Kenji: That's it. That's exactly it.
[INTERNAL] Maya: Can I get that CSV from you? Sanitized however you need — you can swap the emails for fakes, I just need the structure and a few of the names that failed so engineering can reproduce it.
[EXTERNAL] Kenji: Yes, I'll have my coordinator send you a scrubbed version tomorrow. I'll tell her to keep two or three real kanji names in it so you can see the exact characters.
[INTERNAL] Maya: Perfect, that'll help a lot. And in the meantime — for the 29 who are stuck — do you want me to just get them added manually? I can have support do it today rather than you waiting on the fix.
[EXTERNAL] Kenji: Please. They've been in limbo for two weeks, it's embarrassing.
[INTERNAL] Maya: I'll get a list from your coordinator and have them provisioned by end of day tomorrow. Separate from the bug — that's just cleanup.
[EXTERNAL] Kenji: Thank you. That takes the pressure off.
[INTERNAL] Maya: Of course. Okay, that was a big one. What else is on the list?
[EXTERNAL] Kenji: Smaller stuff. The mobile app — a couple of my people asked if there's a dark mode. Screens are hard on the eyes at night.
[INTERNAL] Maya: There is, actually — it shipped in the last mobile release. Settings, then Appearance. They can flip it to dark or set it to follow the phone's system setting.
[EXTERNAL] Kenji: Oh, good. I'll pass that along. That's the kind of thing people don't go looking for.
[INTERNAL] Maya: Fair. We could probably do better surfacing it. What else?
[EXTERNAL] Kenji: The reporting. Aiko wanted to know if she can see her team's engagement without me pulling it for her. Right now I'm the bottleneck — everything routes through my admin account.
[INTERNAL] Maya: She should have a manager view already if she's set as a team manager. Let me check your config after the call and confirm she's got the right role. If she does, she can see her own team's dashboard directly.
[EXTERNAL] Kenji: That would save me a weekly email. Yes, please check.
[INTERNAL] Maya: Will do. Anything else, or is that the list?
[EXTERNAL] Kenji: That's the list. The import thing was the one that had me worried. The rest is housekeeping.
[INTERNAL] Maya: Understood. Let me flip back to the deck for two minutes so you have the utilization numbers for your own reporting, then I'll let you get to bed.
[EXTERNAL] Kenji: Deal. Quick version.
[INTERNAL] Maya: Coach utilization — your allocated coaching hours are running at 81% consumption, which is right where you want it. You're not overpaying for unused capacity and you're not starving demand. If anything you might want to expand the pool slightly next quarter as the Osaka group ramps.
[EXTERNAL] Kenji: Assuming they can actually get into the system, yes.
[INTERNAL] Maya: Fair shot. Fair. That one's on us to fix.
[EXTERNAL] Kenji: I'm teasing. Mostly.
[INTERNAL] Maya: Deserved. Okay — I'll follow up on three things: the import bug written up with your CSV, manual provisioning for the 29 stuck members, and confirming Aiko's manager access. Anything I missed?
[EXTERNAL] Kenji: No, that's the full picture. Thank you for taking the name thing seriously. I half expected to be told it was our file.
[INTERNAL] Maya: It's not your file. A workforce with Japanese names uploading Japanese names is not an edge case, it's Tuesday. We should handle it.
[EXTERNAL] Kenji: I appreciate that. Alright, I'm going to go be a night person somewhere more comfortable.
[INTERNAL] Maya: Go. Sleep. I'll email you the recap tomorrow. Goodnight, Kenji.
[EXTERNAL] Kenji: Goodnight, Maya. Thank you.
