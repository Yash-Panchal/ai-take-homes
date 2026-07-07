# Call — Overton Academy × BetterUp · Onboarding
Date: 2026-06-18 · Call ID: call-116
Participants: [EXTERNAL] Marcus Bell, Director of Faculty Development (Overton Academy) · [INTERNAL] Lena Kowalski, Implementation

[INTERNAL] Lena Kowalski: Hi Marcus, good to finally put a voice to the emails. How's the rollout going on your end?
[EXTERNAL] Marcus Bell: Hi Lena. It's going. We're mid-onboarding, so it's the chaotic-but-hopeful phase.
[INTERNAL] Lena Kowalski: My favorite phase. That's where I earn my keep. So the goal of today is to make sure the implementation is landing cleanly and clear any blockers. Sound right?
[EXTERNAL] Marcus Bell: Exactly. We've got the summer window to get everyone set up before the fall term buries us.
[INTERNAL] Lena Kowalski: Smart to do it now. How many people are you bringing on total?
[EXTERNAL] Marcus Bell: A hundred and eighty faculty and staff, give or take. We're a mid-sized independent school, K through 12.
[INTERNAL] Lena Kowalski: Nice. And you're bringing them in via the CSV import, right? I saw the roster file come through.
[EXTERNAL] Marcus Bell: Yes. Our HR system spits out a roster, I cleaned it up, and I've been importing them in batches. Uploaded about a hundred and twenty so far.
[INTERNAL] Lena Kowalski: How's the import experience been? Any headaches with the file format?
[EXTERNAL] Marcus Bell: The import itself is fine. It chews through the file, tells me how many it added. No complaints there.
[INTERNAL] Lena Kowalski: Good. That's usually where the pain is, so I'm glad it's smooth. Anything else surfacing?
[EXTERNAL] Marcus Bell: There is one thing that's got me scratching my head. Might be nothing, might be me doing something dumb.
[INTERNAL] Lena Kowalski: Those are my two favorite outcomes because both are easy. What's up?
[EXTERNAL] Marcus Bell: So I imported a batch of about forty faculty on Monday. The import said success, forty added. Great. Then a couple of our department heads went in to organize people into teams, assign coaches, that kind of thing.
[INTERNAL] Lena Kowalski: Right, the setup work after import.
[EXTERNAL] Marcus Bell: And they couldn't find the people they'd just imported. They'd search for a teacher by name in the member search, and nothing would come up. Like the person didn't exist.
[INTERNAL] Lena Kowalski: The person you'd just successfully imported wouldn't show up in search.
[EXTERNAL] Marcus Bell: Right. My department head, Cynthia, she was convinced the import had failed. She was ready to redo the whole thing. I talked her off the ledge.
[INTERNAL] Lena Kowalski: Please tell me she didn't re-import everyone.
[EXTERNAL] Marcus Bell: She did not, thank god. Because here's the weird part. The next morning, they were all there. Every single one. Searchable, findable, no problem.
[INTERNAL] Lena Kowalski: Overnight they appeared.
[EXTERNAL] Marcus Bell: Overnight. Like they needed to sleep on it. So the import worked, the people existed, but there was this gap where they were invisible to search for the rest of the day.
[INTERNAL] Lena Kowalski: How long roughly between the import and when they became searchable? You said Monday to Tuesday morning.
[EXTERNAL] Marcus Bell: I imported around eleven Monday morning. They tried searching Monday afternoon, maybe two, three o'clock — nothing. By the time Cynthia logged in Tuesday around eight, all there.
[INTERNAL] Lena Kowalski: So somewhere between Monday afternoon and Tuesday morning, the search caught up.
[EXTERNAL] Marcus Bell: That's the pattern. And it's happened on more than one batch now, so it's not a fluke. Import, invisible in search for the rest of the day, fine the next morning.
[INTERNAL] Lena Kowalski: Can you find the imported people any other way during that gap? Like if you browse the full member list rather than searching?
[EXTERNAL] Marcus Bell: Good question. Cynthia said she could see the total member count went up. So the count reflected them. It was specifically the search that couldn't find them by name.
[INTERNAL] Lena Kowalski: That's a helpful distinction — the record exists, the count reflects it, but the name search can't surface them until the next day.
[EXTERNAL] Marcus Bell: Yes, that's it exactly. Is that normal? Am I supposed to wait a day?
[INTERNAL] Lena Kowalski: You shouldn't have to, no. Let me be straight with you — this sounds familiar, it may already be something we're tracking on our side. But I want to capture your specifics because there's a wrinkle worth noting.
[EXTERNAL] Marcus Bell: What's the wrinkle?
[INTERNAL] Lena Kowalski: The version I've seen described has usually been about members added via the invite flow — you invite someone individually, and they're not searchable until the next index build. What you're describing is the same next-day-searchability symptom, but coming from the bulk CSV import path, not individual invites.
[EXTERNAL] Marcus Bell: Ah. So it might be the same underlying thing but I'm hitting it through a different door.
[INTERNAL] Lena Kowalski: That's my suspicion, and it's worth flagging that it reproduces through CSV import too, not just invites. If the search index only rebuilds on a schedule, it wouldn't matter how the member got created — invite or bulk import, either way they'd be invisible to search until the next rebuild.
[EXTERNAL] Marcus Bell: That would explain the overnight thing. There's some nightly rebuild and my people are stuck waiting for it.
[INTERNAL] Lena Kowalski: That's the shape of it, yeah. The record's created immediately, but the search index that powers name lookup lags behind until the next build, which sounds like it runs overnight.
[EXTERNAL] Marcus Bell: Okay. Well, at least I understand it now. It's disruptive because our whole setup workflow depends on finding people to sort them into teams.
[INTERNAL] Lena Kowalski: Right, and that's the real impact — it's not cosmetic, it stalls your entire post-import organization step for the rest of the day. For a school trying to get set up in a tight summer window, that's a real drag.
[EXTERNAL] Marcus Bell: It is. If I import a batch in the morning, I basically can't touch team assignments until tomorrow. Doubles my timeline.
[INTERNAL] Lena Kowalski: I'm going to make sure your scenario is attached to whatever we're tracking, with a clear note that it also happens on CSV import at scale, not just single invites. Your batch sizes and the timing you gave me are exactly the kind of detail that helps.
[EXTERNAL] Marcus Bell: Happy to help. Forty at a time, and it's every batch, reliably.
[INTERNAL] Lena Kowalski: Perfect. In the meantime, here's a workaround so you're not blocked: do your imports at the end of the day rather than the morning. That way the overnight index build catches them up, and they're searchable by the time you sit down to do team assignments the next day.
[EXTERNAL] Marcus Bell: Oh, that's clever. Front-load the imports, do the sorting the day after. I can work with that.
[INTERNAL] Lena Kowalski: It's a duct-tape fix, but it'll keep you moving through the summer window while the real fix works its way through.
[EXTERNAL] Marcus Bell: I'll take duct tape today over a perfect fix in three months. Thank you.
[INTERNAL] Lena Kowalski: That's the implementation mindset. Anything else on the setup? Coaches assigned okay, teams structuring the way you want?
[EXTERNAL] Marcus Bell: Teams are good once I can actually see the people. Coach matching's been smooth. The faculty seem into it, which surprised me — I expected more resistance.
[INTERNAL] Lena Kowalski: Educators tend to lean in once they realize it's development and not surveillance.
[EXTERNAL] Marcus Bell: That was exactly the fear I had to manage. "Is this the administration spying on us." Once they got that it's private coaching, the temperature dropped.
[INTERNAL] Lena Kowalski: Good framing on your part. That's half the battle in a school.
[EXTERNAL] Marcus Bell: I've been doing this long enough to know where the landmines are.
[INTERNAL] Lena Kowalski: Clearly. One logistics question before we wrap — for the rest of the roster, sixty more faculty, do you want to keep doing forty-at-a-time batches, or would you rather I help you get them all in one larger import?
[EXTERNAL] Marcus Bell: Is one big import safer, or riskier? I don't want to blow something up right before the term.
[INTERNAL] Lena Kowalski: The import itself handles a single larger file fine — it's just a bigger batch. The only thing that changes is you'll have more people invisible-to-search for that one day, but if you run it end-of-day like we said, they'll all surface together overnight.
[EXTERNAL] Marcus Bell: Then let's do one clean import of the remaining sixty at end of day, and I'll do all my team-sorting the morning after. Fewer moving parts.
[INTERNAL] Lena Kowalski: That's the cleanest path. One import, one overnight wait, one sorting session. I'll be around that afternoon if you want me on standby while you run it.
[EXTERNAL] Marcus Bell: I'd take that. Belt and suspenders for the big one.
[INTERNAL] Lena Kowalski: Consider me on standby. Okay — I'll log the search-lag issue with your CSV-import detail today, send you a written note so you have the reference, and confirm the end-of-day import workaround in that same email.
[EXTERNAL] Marcus Bell: That's everything I need. This was a productive twenty minutes.
[INTERNAL] Lena Kowalski: Glad to hear it. Get the rest of that roster in — end of day, remember — and ping me if anything else pops up.
[EXTERNAL] Marcus Bell: Will do. Thanks Lena, appreciate you making sense of the ghost teachers.
[INTERNAL] Lena Kowalski: Haunting resolved. Talk soon, Marcus.
