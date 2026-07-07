# Call — Cedar Grove Schools × BetterUp · Check-in
Date: 2026-06-17 · Call ID: call-004
Participants: [EXTERNAL] Will Hastings, Program Admin (Cedar Grove Schools) · [INTERNAL] Priya Nair, CSM

[INTERNAL] Priya: Will, can you hear me okay? Your audio dropped for a second there at the top.
[EXTERNAL] Will: Yeah, sorry, I'm on the district wifi and it does this thing where it thinks about it before it commits. We're good now.
[INTERNAL] Priya: Perfect. So — how's the end of the school year treating you?
[EXTERNAL] Will: Two more weeks and then blessed silence. The district office is already in summer mode; I'm the last one answering email, which means I'm also the last one anyone can find to complain to.
[INTERNAL] Priya: The lonely lighthouse keeper of the district office.
[EXTERNAL] Will: That's exactly it. Everyone else has mentally checked out to their lake houses and I'm here fielding "the printer's broken" tickets that have nothing to do with me.
[INTERNAL] Priya: The printer is always broken. It's a constant of the universe. Is graduation done, at least, or is that still ahead of you?
[EXTERNAL] Will: Graduation was Saturday. Three ceremonies, one gym, ninety-eight degrees, and the AC picked that morning to quit. We got through it. Barely.
[INTERNAL] Priya: Oh, that's brutal. Ninety-eight in a gym is a health event, not a ceremony.
[EXTERNAL] Will: I saw two parents fanning themselves with the programs like it was a Baptist revival. But the kids walked, nobody fainted, we're calling it a win. Anyway — you didn't call to hear about the AC.
[INTERNAL] Priya: Well, thank you for answering mine — I promise it's not about a printer. How's the program landed this year overall? This was your first full year live, right?
[EXTERNAL] Will: First full year, yeah. Honestly, better than I expected. I was braced for the teachers to treat it as one more district mandate to ignore, but a decent chunk actually engaged. The instructional coaches especially — turns out people whose whole job is coaching kids are pretty open to being coached themselves.
[INTERNAL] Priya: That's a lovely bit of symmetry. Do you have a rough sense of where you landed on active usage, or is that a summer project?
[EXTERNAL] Will: I pulled the numbers last week before everyone scattered. Roughly two-thirds of the invited group booked at least one session, which for a district rollout is frankly shocking. Half of those came back for a second. I'm choosing to be delighted by that.
[INTERNAL] Priya: You should be. A second session is the real signal — first one's curiosity, second one's a decision. Any cohorts that lagged?
[EXTERNAL] Will: The administrative staff, a little. Front-office folks, facilities. Less obvious "what's in it for me" for them, and they're slammed. But even there it wasn't zero. I'll take it for year one.
[INTERNAL] Priya: Year one is about proving it's not a fad. Sounds like you did. And the mobile app — did people take to that, or is it all desktop?
[EXTERNAL] Will: More phone than I'd have guessed, actually. Teachers don't sit at a desk, so a lot of them booked from the app between classes. One of the coaches told me she does her sessions from her car in the parking lot before she drives home. Decompression zone, she called it.
[INTERNAL] Priya: The parking-lot session is a genre unto itself. We hear that a lot. Okay — what's on your list? You mentioned a couple things in your note.
[EXTERNAL] Will: Main thing, and it's the one that's been generating email: the scheduled reports are coming in at a weird time, and the timestamps inside them are off.
[INTERNAL] Priya: Off how — off by a little, or off by a lot?
[EXTERNAL] Will: Looks like about seven hours ahead of us. We're Pacific. A report that should say 9am shows up stamped around 4pm. So the timestamps inside the report just don't match when things actually happened in our day.
[INTERNAL] Priya: Seven hours ahead of Pacific. And it's the times printed inside the report, not the time the email arrives — or both?
[EXTERNAL] Will: Both, kind of. The email lands at an odd hour and the timestamps inside are shifted the same way. My directors read the weekly numbers against the school day — like, "how many sessions happened during the workday versus after" — so when the timestamps don't line up with reality, they think the data itself is wrong. And then I get three confused emails asking why sessions are happening at midnight.
[INTERNAL] Priya: Seven hours ahead of Pacific — that lines up almost exactly with UTC. It really sounds like the timestamps are rendering in UTC instead of your workspace timezone, which is set to Pacific.
[EXTERNAL] Will: That would explain the exact seven-hour thing. It's not random, it's a consistent shift.
[INTERNAL] Priya: A consistent offset is the tell. I want to say this is already on our radar from another customer who reported the same shape — scheduled reports rendering in UTC instead of the workspace timezone. Let me check, and if it's the same underlying issue, I'll attach your account so you're counted in the impact and you get the fix notification when it lands.
[EXTERNAL] Will: Whatever gets it fixed. It's been going on at least a month — I honestly assumed it was on purpose at first, like some setting I'd missed, until a director pushed back hard enough that I went looking.
[INTERNAL] Priya: Definitely not on purpose. Nobody designs a report to show your workday at midnight. Did you happen to check whether the in-app numbers are also shifted, or is it just the scheduled report exports?
[EXTERNAL] Will: Good question — the in-app dashboard looks right to me. It's the scheduled report, the one that gets emailed out as a PDF, that's off. The live view seems fine.
[INTERNAL] Priya: That's a useful detail and I'll include it — live view correct, scheduled/emailed report shifted to UTC. It narrows down where the bug lives. I'll confirm the linkage this week.
[EXTERNAL] Will: Appreciated. My directors will be relieved it's a known thing and not their data going haywire.
[INTERNAL] Priya: Exactly what I'll tell them through you — the data's real, the clock label on it is wrong. And honestly, that they're reading the reports closely enough to catch a seven-hour drift is a good problem to have. Most admins tell me nobody opens the thing.
[EXTERNAL] Will: Oh, they open it. One director treats the weekly report like it's the sports page. He's the one who noticed first. If anything he reads it too closely — he once asked me why a number went down by one and it was because somebody was out sick.
[INTERNAL] Priya: The engaged skeptic. Keep him — that's the person who'll defend the budget line when it matters. Anything else on the list?
[EXTERNAL] Will: One small aesthetic note, take it or leave it. The stock photo on the login page — the woman laughing at a salad-adjacent laptop — is deeply corny. The teachers make fun of it. Someone in the break room calls her "Salad Susan."
[INTERNAL] Priya: Salad Susan. Everyone makes fun of that photo, for what it's worth. She has survived three redesigns. At this point I think she has tenure.
[EXTERNAL] Will: A tenured stock photo. That's very us, actually — hard to fire. Give her a retirement party.
[INTERNAL] Priya: If she's ever quietly retired I'll make sure you get word. It's not going in a ticket — it's a running joke, not a request, and I know you're not actually asking me to redecorate the login page.
[EXTERNAL] Will: God, no. Do not file Salad Susan. I have a reputation to protect as someone who only escalates real things.
[INTERNAL] Priya: Your reputation is intact. Frankly it's why I answer your emails first — when you flag something, I know it's real.
[EXTERNAL] Will: That's the goal. I've watched other admins cry wolf so many times that support stops reading them. I'd rather send four emails a year and have all four matter.
[INTERNAL] Priya: You'd be shocked how rare that is. Your reputation is intact — the timezone thing is the only real item, and it's moving. Speaking of — how's the plan for next year? Are you expanding the program, holding steady?
[EXTERNAL] Will: Holding steady for next year, most likely. The district's budget cycle is its own special hell and I won't know the number until August. But there's appetite to bring in the newer schools — we had two open in the fall — if the money's there.
[INTERNAL] Priya: Two new schools opened in the fall? I didn't realize you were growing. What's driving that?
[EXTERNAL] Will: Housing, mostly. Whole subdivisions went up on the east side and the enrollment followed. It's a nice problem — most districts around here are shrinking and we're the one building. But it means every dollar gets fought over three times before it lands anywhere.
[INTERNAL] Priya: The joys of growth. If it firms up, loop me early and I'll help you build the case with the year-one engagement numbers. Instructional coaches leading adoption is a genuinely good story for a budget meeting.
[EXTERNAL] Will: That's a smart angle, actually. "The people whose job is coaching bought in first." I'll steal that.
[INTERNAL] Priya: Steal freely. And when you do know the number in August, even a rough range helps me get ahead of it on my side — I'd rather have the paperwork half-built than start cold in September.
[EXTERNAL] Will: I'll send you whatever I've got the second I've got it. Assuming I have signal. Which is not a given, and brings us to the fun part.
[INTERNAL] Priya: Okay — logistics, because I know you're about to vanish. What's your summer look like?
[EXTERNAL] Will: I'm out most of July. If anything needs me — a signature, a decision, anything — the week of July 20th is my one window. Before that I'm at my sister's, after that I'm at a cabin with genuinely no signal.
[INTERNAL] Priya: And your sister's place before that — that's still reachable, or is that also a signal desert?
[EXTERNAL] Will: Sister's is fine, she has actual internet, but I've promised the kids I'm not going to be the uncle glued to his phone. So reachable in theory, ignoring you in practice.
[INTERNAL] Priya: Understood. I'll treat the week of the 20th as the real window and leave you alone before it.
[EXTERNAL] Will: Appreciated. My nieces have a very strict no-laptop policy at the lake and they enforce it aggressively.
[INTERNAL] Priya: Noted, hard. Week of July 20th is the Will window. I'll make sure anything that needs you gets to you before you disappear — starting with confirming the report-timestamp linkage this week, so it's already in motion before you go.
[EXTERNAL] Will: That'd be ideal. I'd rather it be moving than land in my inbox the day I get back from the no-signal cabin.
[INTERNAL] Priya: It'll be moving. So: confirm the scheduled-report timezone issue is the known one and attach Cedar Grove this week; the numbers are real, only the clock label is off; nothing filed on Salad Susan; and I've got your July 20th window flagged. Anything I missed?
[EXTERNAL] Will: That's the whole picture. Short list, which I attribute to a genuinely quiet year on your end. That's a compliment.
[INTERNAL] Priya: I'll take a quiet year as the highest compliment there is. What's the cabin situation, out of curiosity — is this a family thing, or your own escape hatch?
[EXTERNAL] Will: Family place, way up north. My grandfather built it, no cell service, no wifi, and the whole family has agreed that's a feature and not a bug. You drive forty minutes to a gas station if you want to check email, which is exactly why nobody does.
[INTERNAL] Priya: That sounds genuinely restorative. The forced disconnect is the whole point.
[EXTERNAL] Will: It is. Last summer I didn't look at a screen for eleven days and came back a different person. Meaner, arguably, but rested.
[INTERNAL] Priya: Rested and mean is a strong summer. Go enjoy the cabin, Will. Have a good summer.
[EXTERNAL] Will: You too, Priya. Talk in July, if the signal cooperates.
