# Call — Whitcomb Partners × BetterBark · Support escalation
Date: 2026-06-24 · Call ID: call-093
Participants: [EXTERNAL] Daniel Ford, Learning & Development Manager (Whitcomb Partners) · [INTERNAL] Sam Oduya, CSM · [INTERNAL] Ravi Patel, Support Engineer

[INTERNAL] Sam: Daniel, thanks for the time. How's the quarter at Whitcomb, busy season for consulting?
[EXTERNAL] Daniel: Always busy, we're heads-down on a couple of big client engagements. But I carved out time for this because it's been bugging our people and I want it sorted.
[INTERNAL] Sam: Appreciate you prioritizing it. I brought Ravi from support engineering along because you described something on the intake that sounded technical enough that I wanted the real expert on it, not me guessing my way through.
[INTERNAL] Ravi: Hi Daniel, happy to dig in.
[EXTERNAL] Daniel: Appreciate you both. It's a weird one and I honestly couldn't tell if it was us, our IT, or you.
[INTERNAL] Ravi: Those are my three favorite suspects and it's usually one of them. Lay it out for me, assume I know nothing about your setup.
[EXTERNAL] Daniel: Okay, some background first. We're a management consulting firm, everybody's on laptops, everybody does their coaching sessions from their desk or a conference room, in the browser. We don't really use the mobile app, our people basically live in Chrome all day.
[INTERNAL] Ravi: Got it, so whatever this is, it's the in-browser video session experience specifically, not mobile.
[EXTERNAL] Daniel: Exactly. And what's happening is, during a coaching session in the browser, the video freezes. Not right away. It's always well into the session. And it's been happening to enough of our consultants that they're complaining to me directly, which is how I know it's not a one-off fluke.
[INTERNAL] Ravi: When you say the video freezes, I want you to be really precise. What exactly freezes, and what keeps working?
[EXTERNAL] Daniel: So the video image just locks up. The coach's face freezes on screen like someone hit pause on a movie. But, and this is the key part, the audio keeps going. You can still hear the coach talking, the conversation continues, it's just the picture is frozen solid.
[INTERNAL] Ravi: That's a very specific and useful detail, audio continues, video freezes. And you said it's not immediate, it's later in the session. Do you have any sense of how far in?
[EXTERNAL] Daniel: I asked around specifically because I figured you'd want a number, and honestly I got a mess of answers. One partner swears it's 45 minutes on the dot every time. A couple of people said "half an hour-ish, maybe more." One just said "toward the end." Best I can pin it down: our sessions run 50 minutes, and it's always somewhere in the back half — never at the start, never early. Past that, the estimates disagree with each other.
[INTERNAL] Ravi: Somewhere in the back half, audio fine, video frozen — the spread in the estimates is normal, people make terrible clocks. And how do people recover, do they have to do anything?
[EXTERNAL] Daniel: They refresh the page. If they hit refresh, the video comes back and it's fine again, at least for a while. But it's disruptive, you're mid-sentence with your coach and suddenly you're reloading the page like it's 2003.
[INTERNAL] Ravi: Refresh recovers it. Okay, that's an important clue too. Is this Chrome specifically, or have you seen it in other browsers?
[EXTERNAL] Daniel: I can really only speak to Chrome because that's what we're standardized on firm-wide. IT locks us to Chrome. So I genuinely can't tell you if Firefox or Safari would do the same, we just never use them.
[INTERNAL] Ravi: That's completely fine, Chrome is a valid and clear data point, I'd rather you tell me what you actually know than guess. Now the timing question, which matters a lot. Do you have a sense of when this started? Was it always like this or is it recent?
[EXTERNAL] Daniel: It's recent, and this is the part that made me think it's on your end. We've been using browser sessions for over a year with zero issues. Then maybe five, six weeks ago the freezing started showing up. Nothing changed on our side. Same laptops, same Chrome, same network, same everything.
[INTERNAL] Ravi: Five or six weeks ago, that's a very helpful anchor. Let me push on the "nothing changed on our side" a little, not because I doubt you, but because it saves us a round trip. Any IT changes around then, new firewall, new VPN, a Chrome policy push, anything?
[EXTERNAL] Daniel: I checked with our IT before this call because I anticipated exactly that question. Nothing. No network changes, no browser policy changes, no VPN changes in that window. Our IT lead was pretty definitive about it, and he keeps a change log.
[INTERNAL] Ravi: I really appreciate you pre-checking, that saves us a whole back-and-forth of "have you tried." So let me summarize what I'm hearing and you tell me if I get it wrong: in-browser coaching sessions on Chrome, the video freezes somewhere in the second half of the session — your reports range from about half an hour in to one person's very confident 45 — while the audio continues uninterrupted, refreshing the page restores the video, and it began about five to six weeks ago with no corresponding change on your side.
[EXTERNAL] Daniel: That's a perfect summary. That's exactly it, word for word.
[INTERNAL] Ravi: That is a well-characterized issue even with the fuzzy timing, and it points at a specific media-connection behavior rather than your network. The combination of audio-continues, late-in-session onset, and refresh-fixing-it especially, that tells me the underlying connection to you is basically fine and it's the video stream itself stalling out.
[EXTERNAL] Daniel: So it's a real thing and not us doing something dumb?
[INTERNAL] Ravi: Based on everything you've described, this reads as a genuine platform-side issue with the browser video session, not your infrastructure. And I want to be clear, you gave me an unusually clean report, the details you collected are exactly what our engineers need to reproduce it.
[EXTERNAL] Daniel: Good. I'd rather over-prepare than have you fishing. So what do I tell my consultants in the meantime?
[INTERNAL] Ravi: Honestly, the refresh is your workaround for now. It's annoying but it works reliably, and importantly it doesn't drop the session, the audio keeps going so they don't miss a beat, a quick refresh brings the video right back. Not elegant, but functional.
[EXTERNAL] Daniel: It's fine as a stopgap. They're already doing it instinctively, I just want to be able to tell them "yes it's a known thing, it's filed, they're on it" so they stop thinking their laptop is dying or their connection is bad.
[INTERNAL] Ravi: You can absolutely tell them that. It's on our side, it's being filed today with your details, and the refresh is the interim move. Nothing wrong with their laptops or your network.
[EXTERNAL] Daniel: That's a relief, our IT was starting to get blamed and they're innocent for once.
[INTERNAL] Ravi: Vindicate your IT team, they earned it this time. Sam, from the account angle?
[INTERNAL] Sam: I'll track it on Whitcomb's account specifically so it doesn't disappear into the general queue, and I'll relay any timeline Ravi gets from engineering directly to you, Daniel, so you're never chasing us for status.
[EXTERNAL] Daniel: That's all I want, honestly. Just to know it's real, someone's on it, and I'll hear back without having to nag.
[INTERNAL] Ravi: It's real and I'm on it. Let me read back the ticket one more time so it's exact: in-browser coaching session video freezes in the second half of sessions on Chrome — customer estimates range from roughly 30 to 45 minutes in — while audio continues uninterrupted, page refresh restores video, onset roughly five to six weeks ago with no customer-side network or browser change. Recovery workaround is page refresh.
[EXTERNAL] Daniel: That's it, exactly.
[INTERNAL] Ravi: One small favor that would help, if any of your consultants can note the exact minute-mark next time it happens, and roughly how many people were on the call at the time, that'd give engineering another data point. But it's not blocking, I've got more than enough to open this properly.
[EXTERNAL] Daniel: I'll ask a couple of the ones who hit it most to log the minute and headcount next time. Easy enough.
[INTERNAL] Ravi: Perfect, that'd be gold if it's easy, but no pressure. And if any of them are technical enough to grab a browser console log when it happens, that's even better, but I know that's asking a lot of consultants mid-session.
[EXTERNAL] Daniel: A few of them are ex-engineers who wandered into consulting, so I might actually get you a console log from one of them. I'll ask the nerdiest partner.
[INTERNAL] Ravi: Bless the ex-engineers. A console log from the nerdiest partner would be genuinely useful, but again, only if it's no hassle for them.
[INTERNAL] Sam: Anything else going on at Whitcomb while we're all here? How's the broader program doing?
[EXTERNAL] Daniel: The program's great, actually, this video thing is the only wrinkle. Our partners love the coaching, it's become a real retention tool for us in a competitive talent market where everyone's poaching everyone.
[INTERNAL] Sam: Consulting talent wars are no joke. Are you using it more for the junior consultants or the partner track?
[EXTERNAL] Daniel: Both, but differently. Juniors use it for the "am I cut out for this brutal job" stuff, the up-or-out anxiety. Partners use it for the leadership and client-relationship side. Two very different needs, same platform.
[INTERNAL] Sam: That's a healthy spread across levels. The up-or-out pressure on juniors is real, I imagine coaching helps you hold onto the good ones through the rough first two years.
[EXTERNAL] Daniel: That's exactly the bet. We lose too many good juniors in year two to burnout before they hit their stride. If coaching keeps even a handful of them, it pays for itself several times over given what it costs to rehire and retrain.
[INTERNAL] Sam: The retention math on consulting is stark, one saved senior analyst dwarfs the whole program cost. Are you tracking that anywhere, or is it more felt than measured?
[EXTERNAL] Daniel: More felt right now, but I'm building a case for our managing partner with what data I can pull. Which, funny enough, is a different conversation for a different day, I don't want to derail the video thing.
[INTERNAL] Sam: Fair, but flag me when you're building that case, I can help you frame the retention story with the engagement data we do have. That's squarely my job.
[EXTERNAL] Daniel: I'll take you up on that in a few weeks. Right now the video freeze was the fire.
[INTERNAL] Sam: Understood, one thing at a time. Glad the core is strong and this is an isolated technical issue rather than a program problem.
[EXTERNAL] Daniel: Very isolated. If you'd asked me a month ago I'd have said "no issues at all." This is genuinely the one thing.
[INTERNAL] Sam: Then let's get the one thing buffed out. We'll make sure it doesn't linger.
[EXTERNAL] Daniel: Appreciate you both pulling Ravi in on short notice, that made this feel like a serious response instead of a black hole ticket.
[INTERNAL] Ravi: That's exactly what we're here for. I'll get this filed today with your details and Sam will keep you looped on timeline. Thanks Daniel.
[EXTERNAL] Daniel: Thank you both, genuinely. This is the fastest a support thing has moved for us in a while.
[INTERNAL] Sam: We aim to un-black-hole ourselves. I'll have Ravi's ticket number and any first update to you by early next week.
[EXTERNAL] Daniel: Perfect, I'll watch for it. Talk soon.
[INTERNAL] Sam: Take care Daniel.
