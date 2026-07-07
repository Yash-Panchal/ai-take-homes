# Call — Crane & Whitfield × BetterBark · Support escalation
Date: 2026-06-17 · Call ID: call-115
Participants: [EXTERNAL] Nadia Okonkwo, HR Systems Administrator (Crane & Whitfield) · [INTERNAL] Ravi Patel, Support Engineer

[INTERNAL] Ravi Patel: Morning Nadia. I saw you flagged something around new-member verification. Wanted to get on a call rather than trade emails all day.
[EXTERNAL] Nadia Okonkwo: Thank you, yes, email tennis was going nowhere. Appreciate the human.
[INTERNAL] Ravi Patel: How's everything else before we dig in? You all had a big cohort of new hires coming, I think.
[EXTERNAL] Nadia Okonkwo: We did, the summer associate class started two weeks ago. Forty-two of them. Bright-eyed, terrified, the usual.
[INTERNAL] Ravi Patel: Forty-two's a solid intake. Onboarding going smoothly otherwise?
[EXTERNAL] Nadia Okonkwo: Mostly. The badge printer had a meltdown on day one, which is a rite of passage at this point, but that's not your problem.
[INTERNAL] Ravi Patel: Badge printers are a universal constant of suffering.
[EXTERNAL] Nadia Okonkwo: Truly. Anyway. The thing I flagged. Let me try to describe it carefully because it took me a while to even believe what I was seeing.
[INTERNAL] Ravi Patel: Go for it, describe it however it makes sense to you.
[EXTERNAL] Nadia Okonkwo: So when we add a new member, they get an email to verify their account and set a password. Standard.
[INTERNAL] Ravi Patel: Right, the verification link.
[EXTERNAL] Nadia Okonkwo: A chunk of my new associates were telling me the link didn't work. They'd click it and get a page saying the link had expired. On a link they'd just received minutes ago.
[INTERNAL] Ravi Patel: Expired immediately? Not after sitting for a day?
[EXTERNAL] Nadia Okonkwo: Immediately. Some of them clicked within a minute of the email landing. "Expired."
[INTERNAL] Ravi Patel: Okay, that's not a normal expiry. Those tokens are good for a good while. Let me ask a few things. Is it everyone, or a subset?
[EXTERNAL] Nadia Okonkwo: A subset, but a big one. And that's the clue, I think. Let me keep going because I did some digging and I have a theory that I'd love you to shoot down or confirm.
[INTERNAL] Ravi Patel: I'm listening.
[EXTERNAL] Nadia Okonkwo: The people it happened to — they'd click the link, get "expired." But then if they went and requested a fresh link and clicked THAT one fast, sometimes it worked, sometimes it didn't. Totally inconsistent. Which drove me up a wall.
[INTERNAL] Ravi Patel: Inconsistent is the worst kind. Okay.
[EXTERNAL] Nadia Okonkwo: So I got nerdy about it. I noticed the affected people all had one thing in common. They're the ones on Outlook. Our firm runs Microsoft 365, and the associates are all in Outlook. But a handful of our contractors and a couple of partners use other mail clients, personal Gmail forwarding, that kind of thing, and THOSE people never had the problem.
[INTERNAL] Ravi Patel: Interesting. So the split is by mail client, not by device or network.
[EXTERNAL] Nadia Okonkwo: As far as I can tell, yes. Outlook people: broken. Everyone else: fine.
[INTERNAL] Ravi Patel: That is a really useful correlation. Keep going, you said you had a theory.
[EXTERNAL] Nadia Okonkwo: Here's my theory, and I'm not an email engineer so tell me if I'm being an idiot. We have a security layer on our email — the Microsoft safe-links thing. It scans URLs in incoming mail. My understanding is it actually visits the links to check if they're malicious before it lets the user click.
[INTERNAL] Ravi Patel: It does, yes. Safe Links rewrites and often pre-fetches URLs to detonate them in a sandbox.
[EXTERNAL] Nadia Okonkwo: Right. So my theory is: the scanner clicks the verification link before the human does. And if your verification link is one-time-use, the scanner burns it. So by the time the human clicks, the token's already been spent, and they see "expired."
[INTERNAL] Ravi Patel: ...Let me sit with that for a second, because that's a very clean explanation and I want to make sure it holds.
[EXTERNAL] Nadia Okonkwo: Take your time. I've been sitting with it for a week.
[INTERNAL] Ravi Patel: So the mechanism would be: single-use token in the verification URL. Outlook's Safe Links prefetches the URL to scan it. That prefetch consumes the single-use token. Then the human clicks and the token's already been redeemed, so they get "expired." And the non-Outlook users don't have a scanner prefetching, so their token survives until they click.
[EXTERNAL] Nadia Okonkwo: That's exactly my theory. And it explains the inconsistency too — sometimes the scanner is slow and the human beats it, sometimes the scanner wins the race.
[INTERNAL] Ravi Patel: The race condition explains the flakiness, yeah. That's actually a really coherent story. I want to be careful not to just agree because it sounds good, but the correlation with Outlook plus the one-time-use token plus the immediate-expiry symptom — that all points the same direction.
[EXTERNAL] Nadia Okonkwo: So I'm not crazy.
[INTERNAL] Ravi Patel: You're not crazy, and honestly this is a better diagnosis than a lot of my colleagues would produce. The behavior you're describing — Safe Links consuming a single-use token before the human clicks — is a real class of problem for anything with one-time links.
[EXTERNAL] Nadia Okonkwo: So what do we do? Because I've got another cohort starting in three weeks and I can't have half of them locked out.
[INTERNAL] Ravi Patel: A few things. Short-term, on your side, you could ask your Microsoft admins whether our verification domain can be excluded from Safe Links scanning. That would stop the prefetch. That's a legitimate mitigation and a lot of orgs do it for known-good senders.
[EXTERNAL] Nadia Okonkwo: I can raise that with our security team, though they're touchy about exclusions.
[INTERNAL] Ravi Patel: Understood, and that's why the real fix has to be on our end. A verification flow that gets broken by a link scanner is a design problem — the link shouldn't be consumed just by being fetched. The token should only be spent on the actual human confirmation, or the fetch and the confirm should be two steps.
[EXTERNAL] Nadia Okonkwo: That makes sense to me even as a non-engineer.
[INTERNAL] Ravi Patel: I'm going to write this up in detail. Your Outlook correlation and the prefetch mechanism are exactly what the engineering team will need to reproduce it. This isn't a "clear your cache" situation.
[EXTERNAL] Nadia Okonkwo: Thank you. I was worried you'd tell me to have everyone try incognito mode.
[INTERNAL] Ravi Patel: No incognito mode is going to save you from a scanner eating your token. This is a real one.
[EXTERNAL] Nadia Okonkwo: What's the timeline on something like this? Ballpark, no promises.
[INTERNAL] Ravi Patel: I genuinely can't promise a date, it depends on how they prioritize. But given it affects any customer running Outlook with Safe Links — which is a lot of enterprise customers — I'd expect it gets attention. I'll make the impact clear in the writeup.
[EXTERNAL] Nadia Okonkwo: That's fair. I appreciate the honesty over a fake date.
[INTERNAL] Ravi Patel: In the meantime, for your next cohort, the Safe Links exclusion is your best bet if security will allow it. If they won't, we can look at whether I can manually verify accounts on the backend for that cohort as a stopgap. Ugly, but it'd unblock you.
[EXTERNAL] Nadia Okonkwo: Let's hold that as plan B. I'll push for the exclusion first.
[INTERNAL] Ravi Patel: Good plan. Let me confirm one detail — are all your affected users specifically getting the word "expired," not "invalid" or "already used"?
[EXTERNAL] Nadia Okonkwo: "This link has expired." Every time. Which is misleading because it's not expired, it's spent.
[INTERNAL] Ravi Patel: Right, the error message itself is arguably wrong too — "expired" when it's really "already redeemed." I'll note that. It sends people down the wrong path, they assume they were slow.
[EXTERNAL] Nadia Okonkwo: Yes! Exactly. They keep apologizing to me for being slow and it's not their fault at all.
[INTERNAL] Ravi Patel: I'll capture all of it. Give me your associate count and roughly what fraction hit it, for the impact section?
[EXTERNAL] Nadia Okonkwo: Forty-two in this cohort, I'd say at least twenty-five hit it. So call it sixty percent. And it'll be every Outlook-based cohort going forward.
[INTERNAL] Ravi Patel: Sixty percent of an enterprise cohort. That's a strong number for the writeup. Okay. I've got what I need.
[EXTERNAL] Nadia Okonkwo: One last thing while I have you — is there any chance this same scanner issue affects the password-reset links too? Because we've had a few grumbles about those, though I haven't dug into it.
[INTERNAL] Ravi Patel: Honestly, I don't want to guess — if you can gather specifics on the password-reset grumbles, who, when, what they saw, I'll look at it separately rather than assume it's the same root cause. It could be, or it could be unrelated.
[EXTERNAL] Nadia Okonkwo: Fair. I don't have anything concrete on that yet, just vague mutterings. I'll collect real examples before I waste your time.
[INTERNAL] Ravi Patel: That's the right call. Vague mutterings are impossible to act on. Bring me specifics and we'll treat it as its own thing.
[EXTERNAL] Nadia Okonkwo: Deal. You've been great. Genuinely, this is the least frustrating support call I've had in months.
[INTERNAL] Ravi Patel: You did most of the diagnostic work on the verification links — I just confirmed it. I'll get that ticket filed today and loop you on the number so you can track it.
[EXTERNAL] Nadia Okonkwo: Perfect. And I'll go make friends with our Microsoft admins.
[INTERNAL] Ravi Patel: Bring them a coffee, they hold the keys. Talk soon, Nadia.
[EXTERNAL] Nadia Okonkwo: Thanks Ravi. Bye.
