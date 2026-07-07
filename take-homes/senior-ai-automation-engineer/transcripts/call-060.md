# Call — Harlow Health × BetterUp · Program Review
Date: 2026-06-19 · Call ID: call-060
Participants: [EXTERNAL] Gwen Achterberg, Program Manager, Clinician Wellbeing (Harlow Health) · [EXTERNAL] Tobias Reyes, Coordinator (Harlow Health) · [INTERNAL] Maya Chen, CSM

[INTERNAL] Maya: Gwen, Tobias, hi. How's the hospital system treating you this month?
[EXTERNAL] Gwen: The hospital system is the hospital system. It never gets calmer, you just get more tired. But the coaching program is a bright spot, so this is a call I actually look forward to.
[INTERNAL] Maya: I'll try to keep it a bright spot then. Tobias, I don't think we've met on a call — you're new to the coordinator seat?
[EXTERNAL] Tobias: Newish. Two months. I took over the day-to-day ops from Priyanka when she moved to the clinical side.
[INTERNAL] Maya: Ah, I remember Priyanka. Tell her the coaching world misses her ruthless spreadsheets.
[EXTERNAL] Gwen: We all miss her ruthless spreadsheets. Tobias is learning them like the Dead Sea Scrolls.
[EXTERNAL] Tobias: I found one this morning with a tab called "DO NOT DELETE — ASK PRIYANKA" and Priyanka no longer answers those questions, so.
[INTERNAL] Maya: The archaeology of the departed coordinator. A universal experience. Okay — I've got us for the program review. My plan: engagement snapshot, then the clinician-specific stuff you flagged, then Tobias's ops questions. Good?
[EXTERNAL] Gwen: Good.
[INTERNAL] Maya: Sharing the dashboard. So — you're at 890 active clinicians against 1,000 seats. For a clinician population, that activation rate is honestly exceptional. Physicians are famously hard to get into any program.
[EXTERNAL] Gwen: They are. The thing that cracked it was framing coaching as burnout prevention rather than "development." Nobody with an MD wants to be "developed." Everybody wants to not burn out.
[INTERNAL] Maya: That reframe is gold and I'm going to steal it, credited to you, for other healthcare accounts.
[EXTERNAL] Gwen: Steal freely. If it helps another clinician not quit medicine, take it.
[INTERNAL] Maya: Completion's at 74%, which is up four points. The night-shift nurses in particular are engaging more than last quarter — did something change there?
[EXTERNAL] Tobias: That was one of Priyanka's last moves. She got the scheduling changed so night-shift clinicians could book coaching during their overlap hours. Made it possible instead of theoretical.
[INTERNAL] Maya: Smart. Okay, Gwen, the thing you flagged — you wrote "coach continuity problem" on the invite, which sounded ominous.
[EXTERNAL] Gwen: It's not ominous, it's operational, but it's been a genuine headache and I want to talk it through. Here's the situation. We had a coach — a really good one, our clinicians loved her — leave the platform last month. She had, I think, thirty-something of our members assigned to her.
[INTERNAL] Maya: Okay. And when a coach leaves, those members need to move to a new coach.
[EXTERNAL] Gwen: Right. And here's the problem. There's no way to do that in bulk. When she left, I had to go in and reassign each of those thirty-some members to a new coach one at a time. Click into the member, change the coach, save, next member, over and over. It took me most of an afternoon.
[INTERNAL] Maya: One at a time, through the individual member records. No batch action.
[EXTERNAL] Gwen: None that I could find. And Tobias looked too.
[EXTERNAL] Tobias: I looked. There's no "select all of Coach X's members and reassign to Coach Y" anywhere. I even checked the admin bulk-actions menu because that's where bulk stuff usually lives. Bulk deactivate is there, bulk invite is there, but no bulk reassign.
[EXTERNAL] Tobias: I even checked the help docs assuming I was just missing a button. Nothing there either.
[INTERNAL] Maya: You weren't missing it — it genuinely isn't there. But checking the docs first was the right move.
[INTERNAL] Maya: So the pattern you'd want is: coach leaves, admin picks the departing coach, sees their full member list, and reassigns the whole group — or subsets of it — to one or more new coaches in a single action.
[EXTERNAL] Gwen: Exactly. And ideally I could split them — like, put fifteen with Coach A and fifteen with Coach B, because you don't always want to dump one coach's entire caseload on a single replacement. But even a straight "move all of Coach X's people to Coach Y" would have saved me the afternoon.
[INTERNAL] Maya: The one-to-many split is a good detail. Let me make sure I have the impact right. Thirty-some members, done individually, most of an afternoon. And I imagine there's a risk angle too?
[EXTERNAL] Gwen: There's a big risk angle, and this is the part that actually worries me more than my afternoon. When you're doing thirty of these by hand, you will miss one. I'm almost certain I missed at least one member for a day or two — they were sitting there assigned to a coach who no longer exists on the platform, and they had no active coach until I caught it. For a burnout-prevention program, a clinician falling through the cracks because of a manual reassignment error is exactly the failure mode we can't have.
[INTERNAL] Maya: That's the sharpest version of the impact — it's not just tedious, it's error-prone in a way that leaves members without a coach. "Clinician silently orphaned during manual reassignment" is going into the write-up in those words.
[EXTERNAL] Gwen: Please. That's the fear. These are people we're specifically trying to catch before they fall, and the tooling made me the weak link.
[INTERNAL] Maya: Understood, and it's a fair critique. This is a feature request rather than a bug — the reassignment works, there's just no bulk path — so I want to be honest that I can't give you a delivery date. But the framing you've given, especially the orphaned-member risk in a clinical context, is exactly the kind of thing that gets a request prioritized. I'll write it up today.
[EXTERNAL] Gwen: That's fair. I don't expect a date. I just want it in the system with the right weight, because it's going to happen again — coaches leave, that's normal, and every time one does, I'm back to the afternoon.
[INTERNAL] Maya: It's a recurring, predictable event, which is the best argument for tooling. Coaches leaving isn't an edge case, it's a certainty. Tobias, when the next one happens, if it's before this ships, loop me in early and I'll see if our team can do a backend batch move to spare you the afternoon.
[EXTERNAL] Tobias: That'd be a lifesaver. Is that something you can do now, backend?
[INTERNAL] Maya: For a genuine coach-departure with a clear list, our support engineers can sometimes script a batch reassignment on the backend. It's not self-serve and it's not instant, but it beats clicking thirty times. I'll flag it as an option, not a promise.
[EXTERNAL] Gwen: Even knowing that's a possibility helps. Okay, that's the big one. The rest is lighter.
[INTERNAL] Maya: Let's hear the lighter stuff.
[EXTERNAL] Gwen: The wellbeing content library — our clinicians want more short-form stuff. The long modules are great but a physician between patients has four minutes, not forty. Anything under five minutes gets consumed voraciously.
[INTERNAL] Maya: That's useful content-strategy feedback and I'll pass it to the content team — "clinical population wants sub-five-minute modules, time-starved." Not a product defect, just demand signal, but a good one.
[EXTERNAL] Gwen: Exactly, just a wish. Our clinicians consume content in the cracks between patients, so length is everything.
[INTERNAL] Maya: That's a useful design constraint for the content team to hear — "assume four minutes, not forty." I'll frame it that way.
[EXTERNAL] Gwen: Perfect. And Tobias had a reporting thing.
[EXTERNAL] Tobias: Yeah, small one. When I export the engagement report, the department names come through as codes instead of names — like "DEPT_0447" instead of "Emergency Medicine." Is there a mapping somewhere, or is that just how it exports?
[INTERNAL] Maya: That's likely because the departments were imported with codes as the display name rather than the friendly name — it's a configuration thing on the import, not a bug. If you send me the export, I can confirm and show you where to set friendly names so future exports read cleanly.
[EXTERNAL] Tobias: Oh, so it's fixable on our side. Great, I'll send the export.
[INTERNAL] Maya: Fixable on the config, yes. Probably a fifteen-minute fix once I see it. Anything else, Tobias, while you've got me and Priyanka doesn't answer her scrolls?
[EXTERNAL] Tobias: That's my list. Everything else I've either figured out or haven't broken yet.
[INTERNAL] Maya: "Haven't broken yet" is the correct posture two months in. One thing — has Priyanka's handoff doc been enough, or are there gaps I can help fill? I'd rather you learn from me than from a haunted spreadsheet.
[EXTERNAL] Tobias: The handoff was decent. The gaps are the "why" behind things — like, I know the seasonal deactivation process, but not why it's timed the way it is. Context, not clicks.
[INTERNAL] Maya: That's a fair gap and an easy one to close. Want me to do a thirty-minute "why the program is built the way it is" session with you sometime? Just the reasoning, not the buttons.
[EXTERNAL] Tobias: Honestly, yes. That would save me a lot of reverse-engineering.
[INTERNAL] Maya: Let's book it. I'll send some times next week — low-key, just context transfer.
[EXTERNAL] Tobias: Appreciate it. I'll take all the context I can get before the next big cycle.
[INTERNAL] Maya: Then it's on the list. Gwen, renewal-wise you're in good shape — Q1 next year, plenty of runway, and the numbers make it easy.
[EXTERNAL] Gwen: We're not going anywhere. As long as coaches keep being reassignable — eventually in bulk — we're happy.
[INTERNAL] Maya: On that note, let me recap. One: I write up the bulk coach-reassignment request today, with the orphaned-clinician risk and the one-to-many split, flagged as a recurring operational need — no date promised. Two: next coach departure before it ships, loop me in for a possible backend batch move. Three: pass along the sub-five-minute content demand to content. Four: you send me the engagement export, Tobias, and I show you the friendly-name department fix. Complete?
[EXTERNAL] Gwen: Complete. You're as organized as Priyanka, which is the highest compliment I have.
[INTERNAL] Maya: I will accept the Priyanka comparison and retire undefeated. Take care of your clinicians, both of you.
[EXTERNAL] Tobias: Thanks Maya. Sending that export now.
[EXTERNAL] Gwen: Thanks, Maya. Talk soon.
[INTERNAL] Maya: Bye, both.
