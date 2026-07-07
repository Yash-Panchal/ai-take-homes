# Call — Harborline Media × BetterBark · Sync
Date: 2026-06-18 · Call ID: call-006
Participants: [EXTERNAL] Aisha Bello, People Ops (Harborline Media) · [INTERNAL] Tomás Vela, CSM

[INTERNAL] Tomás: Aisha, good afternoon. Can you hear me okay? I switched to the headset because the office HVAC is doing a jet-engine impression today.
[EXTERNAL] Aisha: Loud and clear. Better than the coffee shop I called you from last time, anyway.
[INTERNAL] Tomás: The one with the espresso machine that sounded like a fire alarm. I remember. How's the weather up your way?
[EXTERNAL] Aisha: Gray and drizzly, which is on-brand for us. Perfect weather for hiding indoors and doing admin work, honestly.
[INTERNAL] Tomás: Speaking of which — I hear you survived the reorg.
[EXTERNAL] Aisha: "Survived" is generous. We collapsed five content teams into three, renamed everything, and I personally moved about sixty people between teams in your admin panel over two days. I have moved more people in the last week than a furniture company.
[INTERNAL] Tomás: Five into three. Was this a cost thing or a "the org chart finally made no sense" thing?
[EXTERNAL] Aisha: The second one, mostly. We had a "Digital Video" team and a "Video" team and a "Streaming Content" team and nobody could tell you the difference, including the people on them. So leadership drew a cleaner map and I got to be the one who implements the map in every system we own.
[INTERNAL] Tomás: How many systems are we talking? I always underestimate that number for media companies.
[EXTERNAL] Aisha: You do not want the full list. Payroll, the HRIS, the badge system, three different content tools, and you. Every single one has its own idea of what a "team" is.
[INTERNAL] Tomás: The person who turns the org-chart PowerPoint into reality. Thankless work.
[EXTERNAL] Aisha: Utterly thankless. Nobody notices when it goes smoothly and everybody notices when someone lands on the wrong team. But it's mostly done now, which is why I could take this call without twitching.
[INTERNAL] Tomás: I'll take the no-twitching version of Aisha any day. Did you at least get a weekend out of it, or did the reorg eat that too?
[EXTERNAL] Aisha: I got Sunday. I spent most of it lying on the floor staring at the ceiling, but I'll count it.
[INTERNAL] Tomás: That counts. Well, that's a real stress test of the admin tools, moving sixty people and renaming five teams in two days. How did they hold up?
[EXTERNAL] Aisha: The editing itself was fine, honestly. The bulk move worked, the renames worked, nothing errored out or lost data. I want to give credit where it's due — the actual mechanics of moving people were smooth.
[INTERNAL] Tomás: I'll pass that along to the admin-tooling folks. They rarely hear it when things just work.
[EXTERNAL] Aisha: They should. The bulk-move flow saved me from clicking sixty times. Whoever built that, buy them a coffee.
[INTERNAL] Tomás: Noted. Good to hear. But I'm sensing a "but."
[EXTERNAL] Aisha: There's a but. There's a real bug we hit over and over, and it's about search, not the editing. After we rename a team or move a member, search keeps returning the old state for about ten minutes.
[INTERNAL] Tomás: Old state how — walk me through what you'd actually see.
[EXTERNAL] Aisha: So say I rename "Digital Video" to "Video Production." Somebody searches "Video Production" — the new name — and gets nothing. Empty. Or they search for a person I just moved, and search still shows them filed under the old team. And then, with no action from anyone, it quietly fixes itself. Ten minutes later the same search is correct.
[INTERNAL] Tomás: So the search index looks like it lags the edit by roughly ten minutes. The change is saved — the edit screen confirms it — but search keeps serving the old world for a bit before it catches up.
[EXTERNAL] Aisha: That's exactly what it looks like. And I can reproduce it on demand — I did it three times while I was documenting it for myself. Rename a test team, search immediately, stale result. Wait ten minutes, search again, correct result. Every single time.
[INTERNAL] Tomás: Reproducible-on-demand is gold. That takes it from "sometimes weird" to "here's the exact behavior." Roughly ten minutes each time, or does the lag vary?
[EXTERNAL] Aisha: Feels like about ten, give or take a couple. I didn't stopwatch it precisely, but it's in that ballpark consistently. Never seen it take an hour, never seen it be instant.
[INTERNAL] Tomás: The fact that you documented it for yourself at all — you're making my job easy. Most people just fire off "search is broken" and hang up.
[EXTERNAL] Aisha: I've been on the other side of that. Vague bug reports are how you get vague fixes. I'd rather do the homework once.
[INTERNAL] Tomás: That consistency is useful too. And during the reorg, when you were making a lot of changes fast, I imagine this compounded.
[EXTERNAL] Aisha: Oh, it was a mess. It caused a stream of "where did this person go" tickets to my desk. A manager would search for someone right after I moved them, get the old team or get nothing, and conclude I'd deleted the person or lost them. So I'm getting panicked messages while I'm mid-reorg, and the answer every time is "just wait ten minutes and search again," which is not a satisfying thing to tell a panicking manager.
[INTERNAL] Tomás: No, "have you tried waiting" is a terrible thing to have to say when someone thinks you deleted their direct report. The timing correlation with your reorg makes total sense — you were generating edits faster than the index could keep up, so the lag was constantly visible.
[EXTERNAL] Aisha: Right. On a normal week I'd probably never notice, because who searches for a team the instant it's renamed? But during a reorg you're renaming and searching constantly, so the gap is in your face all day.
[INTERNAL] Tomás: The perfect storm of "the one week you're hammering the exact thing that lags."
[EXTERNAL] Aisha: Exactly. If we reorged one team a month I'd never have caught it. Do it sixty times in two days and it's impossible to miss.
[INTERNAL] Tomás: That's a great way to put it, and I'll capture it. Can you send me the exact steps you just described — the rename-a-test-team, search-immediately, wait-ten, search-again sequence — and roughly the timestamps from one instance? A concrete before-and-after with times attached is exactly what engineering will want to reproduce it.
[EXTERNAL] Aisha: I'll send it today. I literally have notes from when I was testing it, so I can give you a clean sequence with the times. Do you want the team names too, or scrubbed?
[INTERNAL] Tomás: Real team names are fine and actually helpful — the renames are part of the repro. If any of it feels sensitive, scrub the person names, but the team-rename steps I'd love verbatim.
[EXTERNAL] Aisha: Easy. I'll use a throwaway test team so there's nothing sensitive at all. To be clear, though — this isn't rollout-blocking. The reorg is done, the dust has settled, search is correct now that I've stopped editing. I don't want you to treat it as a five-alarm fire.
[INTERNAL] Tomás: Understood — real bug, reproducible, not an emergency. I'll file it with the repro attached and flag it as "not urgent but confirmed and reproducible," which is honestly the sweet spot for getting something fixed properly rather than hot-patched.
[EXTERNAL] Aisha: That's the right framing. It'll bite us again eventually — the next reorg is never far away in media, we reshuffle content teams like it's a hobby — but it's not biting me today.
[INTERNAL] Tomás: In this business I believe you. Every media company I work with treats the org chart like a whiteboard.
[EXTERNAL] Aisha: A whiteboard with a leaky marker. Give it a quarter and someone will decide "Video Production" should really be two teams again.
[INTERNAL] Tomás: Then we file it now so it's fixed before the next reshuffle, rather than in the middle of one. Anything else from the trenches?
[EXTERNAL] Aisha: One tiny one, and it's purely cosmetic. On my phone, in the mobile app, the team-name font truncates long names with an ellipsis really aggressively. Like, "Editorial Stra..." — which could be "Editorial Strategy" or "Editorial Standards," and we have both now after the reorg. So I can't always tell which team I'm looking at on mobile.
[INTERNAL] Tomás: Is that causing an actual problem — people acting on the wrong team — or is it just annoying?
[EXTERNAL] Aisha: Honestly just annoying. On desktop the full name shows, so it's a mobile-only squint issue. Nobody's made a mistake because of it that I know of. It's a mild annoyance, I'm not really asking for anything, I just noticed it during all the renaming.
[INTERNAL] Tomás: I'll note it as a mild annoyance — filed in my brain rather than in Jira unless it grows up into something that actually causes a mix-up. If two teams ever get confused because of the truncation, that changes it from cosmetic to real, so flag me if that happens.
[EXTERNAL] Aisha: Fair. It won't, probably. It's a "why is the font like that" observation, not a complaint. The search thing is the real one.
[INTERNAL] Tomás: Good — I like knowing which one keeps you up at night versus which one's just a raised eyebrow.
[EXTERNAL] Aisha: The search one doesn't even keep me up anymore now that the reorg's done. It's more of a "let's not get ambushed by it next time" thing.
[INTERNAL] Tomás: Understood, and I've got the search one squarely as the priority. How'd engagement hold up through all this? Reorgs usually put a dent in it.
[EXTERNAL] Aisha: That's the part that genuinely surprised me — the numbers held. I expected people to check out during the uncertainty, and there was a dip the first week, but it recovered fast. Session volume's basically back to pre-reorg levels already.
[INTERNAL] Tomás: That's the platform earning its keep. Usually when the org's in turmoil, coaching is the first thing people drop, so holding steady through a five-into-three collapse is a real signal.
[EXTERNAL] Aisha: I think people leaned on their coaches during the uncertainty, honestly. "My team's being reorganized and I don't know who my manager is next week" is exactly the kind of thing you'd want to talk to a coach about.
[INTERNAL] Tomás: Did you see it in the dashboard, or is that a gut read from the hallway?
[EXTERNAL] Aisha: Both, actually. Session volume in the dashboard backs it up, and a couple of managers mentioned unprompted that their people were booking more sessions during the chaos.
[INTERNAL] Tomás: That's a lovely reframe and I might steal it — coaching as a stabilizer during change, not a casualty of it. Okay, let me read back so nothing slips. One: you're sending me the search-staleness repro today, with steps and rough timestamps from a test-team instance, and I file it as a confirmed, reproducible, non-urgent bug — search index lags team renames and member moves by about ten minutes, then self-corrects. Two: the mobile team-name truncation stays in my head as a cosmetic note unless it causes a real mix-up. That the full list?
[EXTERNAL] Aisha: That's it. One real bug with a clean repro, one font gripe you're allowed to ignore.
[INTERNAL] Tomás: My favorite ratio. I'll confirm the search bug is filed by Friday and send you the ticket link so you can watch it move.
[EXTERNAL] Aisha: Perfect. Are we still on for the quarterly review next month, or did the reorg blow up the calendar?
[INTERNAL] Tomás: Still on — I'll send a fresh invite since half your org's job titles changed. Same Thursday slot work for you?
[EXTERNAL] Aisha: Thursday's good. Push it to the afternoon if you can, mornings are meeting soup right now.
[INTERNAL] Tomás: Afternoon it is. I'll aim for after two your time.
[EXTERNAL] Aisha: Perfect. Thanks, Tomás — and thanks for not treating me like I broke it myself.
[INTERNAL] Tomás: You moved sixty people flawlessly. The tool couldn't keep its own search current — that's on us, not you. Talk soon, Aisha.
