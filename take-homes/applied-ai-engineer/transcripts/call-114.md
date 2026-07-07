# Call — Galway Foods × BetterBark · Support escalation
Date: 2026-06-16 · Call ID: call-114
Participants: [EXTERNAL] Deirdre Foran, IT Service Manager (Galway Foods) · [INTERNAL] Ravi Patel, Support Engineer

[INTERNAL] Ravi Patel: Hi Deirdre, thanks for hopping on. I've got the ticket open in front of me — this is the one you filed a few weeks back about the mobile app crashing?
[EXTERNAL] Deirdre Foran: That's the one. Thanks for following up. Honestly the timing is a bit funny because things have changed since I opened it.
[INTERNAL] Ravi Patel: Oh? Changed how?
[EXTERNAL] Deirdre Foran: Let me back up and give you the whole picture, because I think I know what happened and I want to close the loop properly rather than leave you chasing a ghost.
[INTERNAL] Ravi Patel: I appreciate that. Take your time.
[EXTERNAL] Deirdre Foran: Actually, before I get into it — is this call being recorded? I only ask because I'm going to name our internal device-management setup and I want to know where it lands.
[INTERNAL] Ravi Patel: It's recorded for support quality, stays internal to our support org, nothing external. If you'd rather I not capture specifics of your infrastructure, just say and I'll keep it general in my notes.
[EXTERNAL] Deirdre Foran: No, that's fine, internal support is fine. I just like to know. Occupational habit, I'm an IT person, we're paranoid by trade.
[INTERNAL] Ravi Patel: Healthy paranoia. It's why your systems stay up. So — the trickle of complaints.
[EXTERNAL] Deirdre Foran: Right. So back in, what, late May, we started getting a trickle of complaints. People opening the app on their phones and it just closing on them. Boom, back to the home screen.
[INTERNAL] Ravi Patel: On launch specifically, or mid-session?
[EXTERNAL] Deirdre Foran: On launch, mostly. They'd tap the icon, see the splash, and then poof.
[INTERNAL] Ravi Patel: Okay. And how many people are we talking?
[EXTERNAL] Deirdre Foran: That's the thing — it was maybe eight or nine people out of our three hundred users. Not everyone. Which made it hard to pin down.
[INTERNAL] Ravi Patel: That pattern is useful, actually. When it's a subset it's usually device or OS specific. Do you know what phones the affected folks were on?
[EXTERNAL] Deirdre Foran: Here's where it gets interesting. I did a little detective work because I was annoyed. Almost all of them were on older Android handsets. A couple of Samsungs, an older Pixel, a Motorola that should probably be in a museum.
[INTERNAL] Ravi Patel: And nobody on iOS reported it?
[EXTERNAL] Deirdre Foran: Not a soul. All Android, all older devices, all running an OS version that was a couple of releases behind.
[INTERNAL] Ravi Patel: That's a very specific fingerprint. When you filed the ticket, we had a couple of similar reports floating around, so I want to make sure I'm not conflating yours with something else.
[EXTERNAL] Deirdre Foran: Right, well, hold that thought, because here's the punchline. Our IT team pushed a device-management update in early June. Part of it forced OS updates on anything that had fallen behind. Standard security hygiene, nothing to do with your app.
[INTERNAL] Ravi Patel: Ah.
[EXTERNAL] Deirdre Foran: And after those phones updated their OS, the crashes stopped. Completely. I've been sitting on it for two weeks now watching, and not a single new complaint.
[INTERNAL] Ravi Patel: Not one?
[EXTERNAL] Deirdre Foran: Zero. I even went back to two of the loudest complainers and asked them to try to reproduce it. They can't. It just works now.
[INTERNAL] Ravi Patel: So the OS update on those devices resolved it.
[EXTERNAL] Deirdre Foran: That's my read. Whether it was the OS itself, or the app got a chance to update cleanly once the OS was current, I couldn't tell you. But the symptom is gone and I can't make it come back.
[INTERNAL] Ravi Patel: That's a clean result, honestly. I'd rather have "it's gone and I can't reproduce it" than a lingering mystery.
[EXTERNAL] Deirdre Foran: Same. So I don't want to waste your engineering team's time. As far as I'm concerned this can be closed.
[INTERNAL] Ravi Patel: Let me make sure I capture your reasoning so the closure note isn't just "customer says it's fine." You had roughly eight users, all older Android devices behind on OS updates, crashing on launch. Your IT forced OS updates in early June, and since then the crashes have stopped entirely across all affected users, with no reproduction possible.
[EXTERNAL] Deirdre Foran: That's a perfect summary. You should write my incident reports.
[INTERNAL] Ravi Patel: I've had practice. One question just so I'm being thorough — did anyone who was NOT behind on their OS ever hit this? Anyone on a current Android?
[EXTERNAL] Deirdre Foran: No. That's what made me confident it was the old-OS cohort. Everyone current was totally fine the whole time.
[INTERNAL] Ravi Patel: Good. That lines up. I'm comfortable marking this resolved on your side. I'm not going to file anything on the product side since the affected population self-resolved via the OS update and there's no reproducible defect on current devices.
[EXTERNAL] Deirdre Foran: Makes sense to me. If it comes back I'll scream.
[INTERNAL] Ravi Patel: Please do, and reference this ticket number so I have the history.
[EXTERNAL] Deirdre Foran: Will do. While I've got you — unrelated — is there any way to see who's actually logging in versus who's just got an account gathering dust?
[INTERNAL] Ravi Patel: There is, yeah. Admins have an engagement view in the dashboard. Are you an admin on the account?
[EXTERNAL] Deirdre Foran: I think so? I set most of it up.
[INTERNAL] Ravi Patel: If you set it up you almost certainly are. Log into the web admin, look under the members section, there's an activity column and some filters. I can send you a walkthrough link.
[EXTERNAL] Deirdre Foran: That'd be great. I'm trying to figure out our real active number before renewal season so I'm not paying for ghosts.
[INTERNAL] Ravi Patel: Smart. I'll include the export options too — you can pull the roster to a spreadsheet if you'd rather slice it yourself.
[EXTERNAL] Deirdre Foran: Oh, you can export the roster now? Last I checked I was copy-pasting like an animal.
[INTERNAL] Ravi Patel: There's a proper CSV export now, it's fairly recent. Admin, members, there's an export-all button.
[EXTERNAL] Deirdre Foran: That alone made this call worth it.
[INTERNAL] Ravi Patel: Happy to spread joy through spreadsheets. Anything else on your list while we're on?
[EXTERNAL] Deirdre Foran: Well — one non-urgent thing, since you're here and clearly know your stuff. Our device-management push forced OS updates. Going forward, is there a minimum OS version your app officially supports? So I can set our policy to keep everyone above the line and avoid this whole class of problem.
[INTERNAL] Ravi Patel: Good question, and exactly the right instinct. We publish supported OS versions in our help center — I'll include the link when I send the docs. Generally we support the current and two prior major versions of each OS. Anything older than that we can't guarantee.
[EXTERNAL] Deirdre Foran: Current and two back. That's a clean rule I can build a policy around.
[INTERNAL] Ravi Patel: It's the industry norm, roughly. If you keep your fleet within that window you'll dodge most compatibility surprises, not just with us.
[EXTERNAL] Deirdre Foran: That's genuinely useful. I'll set the device-management minimum to match. Cheaper than fielding crash complaints.
[INTERNAL] Ravi Patel: Far cheaper. And it means the next OS-related weirdness gets prevented rather than diagnosed.
[EXTERNAL] Deirdre Foran: Prevention over diagnosis. That's the dream in IT.
[INTERNAL] Ravi Patel: The dream we rarely get. Anything else while I'm being useful?
[EXTERNAL] Deirdre Foran: No, that's it now. Crashes gone, export exists, OS policy sorted, life is good.
[INTERNAL] Ravi Patel: Then I'll close the crash ticket with the OS-update resolution and email you the admin walkthrough plus the export docs, and I'll add the supported-OS-versions link too.
[EXTERNAL] Deirdre Foran: Perfect. Thanks Ravi, you made that painless.
[INTERNAL] Ravi Patel: That's the goal. And genuinely, thanks for doing the legwork on your end — the OS correlation made this an easy diagnosis.
[EXTERNAL] Deirdre Foran: I aim to be the customer support engineers don't dread.
[INTERNAL] Ravi Patel: You're in rare company. Take care, Deirdre.
[EXTERNAL] Deirdre Foran: You too. Bye now.
