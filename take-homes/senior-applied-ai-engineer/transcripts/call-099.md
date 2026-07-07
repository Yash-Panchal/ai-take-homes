# Call — Drummond Steel × BetterUp · Support Escalation Debrief
Date: 2026-06-16 · Call ID: call-099
Participants: [EXTERNAL] Curtis Vane, IT Systems Lead (Drummond Steel) · [INTERNAL] Ravi Patel, Support Engineer · [INTERNAL] Derek Okafor, CSM

[INTERNAL] Derek: Curtis, appreciate you making the time. I brought Ravi from our support engineering side because he was closest to the ticket, and I figured a joint debrief beats me relaying things secondhand.
[EXTERNAL] Curtis: No, that's the right call. I've been on both sides of the "CSM plays telephone with the engineer" game and it never ends well.
[INTERNAL] Ravi: I'll try to earn my seat then.
[EXTERNAL] Curtis: Ha. Well, first things first — it's fixed. So this is more of a "let's understand what happened" than a "come save us" call. I want to make sure nobody on either side thinks there's a fire still burning.
[INTERNAL] Derek: Good to hear it up front. How's the plant otherwise? You're the Pittsburgh site, right?
[EXTERNAL] Curtis: Pittsburgh's headquarters, but I cover all four mills — Pittsburgh, the one outside Gary, Birmingham Alabama, and the little specialty shop in Ohio. IT for a steel company is mostly keeping thirty-year-old machines talking to five-year-old software, so a coaching platform is honestly the easy part of my week.
[INTERNAL] Derek: I'll take "easy part of your week," we'll put it on a mug.
[INTERNAL] Ravi: I'm going to hold you to the mug.
[EXTERNAL] Curtis: You'll be waiting. Anyway. Rollout's been good. We've got about six hundred people on it now — plant managers, shift supervisors, the safety leadership track especially has been popular. Steel is a business where a bad safety culture literally kills people, so anything that makes our supervisors better listeners, I'm for it.
[INTERNAL] Derek: The stakes in your industry make the safety-leadership angle land differently than it does at, say, a software company. It's not abstract.
[EXTERNAL] Curtis: There's nothing abstract about a molten steel pour. You listen to your crew or someone gets hurt. Coaching that makes a supervisor actually hear a worker's "hey, that doesn't look right" — that's not a soft skill to us, that's a hard safety control.
[INTERNAL] Derek: The safety leadership cohort numbers have been strong on our side too. Engagement's above where most manufacturing accounts land.
[EXTERNAL] Curtis: The guys grumble about it and then quietly do the sessions. That's how you know it's working with this crowd. If they said they loved it I'd assume they were lying.
[INTERNAL] Ravi: That's a very steel answer.
[EXTERNAL] Curtis: We are a very steel people.
[INTERNAL] Derek: So walk us through last week. From my seat it looked like a login storm — a bunch of your users couldn't get in, and then it cleared.
[EXTERNAL] Curtis: That's the shape of it, yeah. Let me give you the whole thing because the details matter and I want your team to have them for the record. Tuesday morning, right around shift change, my helpdesk starts getting tickets. "Can't log into the coaching app." First three, I figure it's the usual — somebody forgot a password, somebody's on the wrong URL. But it kept coming. By nine we had maybe forty tickets and they were all from the Birmingham site.
[INTERNAL] Ravi: Only Birmingham. That's the part that jumped out at me when I picked it up.
[EXTERNAL] Curtis: Right, and that's the tell in hindsight, but in the moment I didn't clock it. Pittsburgh's fine, Gary's fine, Ohio's fine. Just Birmingham throwing errors. And the error people described was weird — they'd put in their credentials, the page would spin, and then it'd just bounce them back to the login screen. No "wrong password," no lockout message. Just... nothing. Back to start.
[INTERNAL] Derek: That's an unnerving one because it doesn't tell you anything.
[EXTERNAL] Curtis: Exactly. A clear error I can act on. Silence I have to go dig for. So I opened the ticket with you all, and I'll say — your first responder was quick. Within the hour.
[INTERNAL] Ravi: That would've been the frontline team; it escalated to me by early afternoon once they saw it wasn't an account-level thing.
[EXTERNAL] Curtis: Which is where it got interesting. Because I was convinced it was you. Sorry, but I was. Forty people can't log in, it's the vendor, right? That's the natural assumption.
[INTERNAL] Ravi: It's the correct first assumption. I'd assume the same. What we did on our end — I pulled the auth logs for your workspace, filtered to the Birmingham users, and the pattern was that the login requests were arriving at our servers, but they were arriving without the authorization header that carries the session token. So from our side the request looked like an anonymous, unauthenticated hit, and we did exactly what we're supposed to do with those — bounce them to login.
[EXTERNAL] Curtis: And that's the "silence" the users saw. You weren't rejecting them, you literally never saw them as logged in.
[INTERNAL] Ravi: Right. The token was being created fine on the first step. Something between the user's browser and us was dropping the header on the follow-up requests.
[EXTERNAL] Curtis: Which points a big finger back at my side.
[INTERNAL] Ravi: It pointed at the network path, is how I'd put it. Could've been us, could've been in between. The header-stripping pattern is specific enough that I asked whether anything had changed on the Birmingham network recently, because "one site only, headers missing" is almost always a middlebox.
[EXTERNAL] Curtis: And that question is what cracked it, so credit where it's due. Because the answer was yes. Birmingham had gotten a new web proxy appliance the previous Friday. Corporate security's initiative — they're rolling out a standardized proxy across all the mills and Birmingham was the pilot site. Lucky them.
[INTERNAL] Derek: Ah. So the timing lined up almost exactly.
[EXTERNAL] Curtis: Friday it goes in, Monday's light because it's Monday, Tuesday morning shift-change is the first real load, and boom. The proxy was doing some kind of header normalization — "sanitizing" is the word the vendor used, which is a lovely word for "breaking" — and in the process it was stripping the authorization header on requests to certain domains. Yours included.
[INTERNAL] Ravi: Header sanitization on a forward proxy — yeah, we see that maybe a few times a year. Usually it's a well-meaning security default that's too aggressive. The proxy thinks it's protecting against something and instead it's amputating the thing that makes authenticated sessions work.
[EXTERNAL] Curtis: That's precisely what it was. I got the proxy vendor on the phone, we found the setting — there was an allowlist for domains that should pass headers through untouched, and of course yours wasn't on it because it was a fresh appliance with defaults. We added your domains, our SSO provider's domains, a couple of others, pushed the config, and within about twenty minutes Birmingham was logging in clean.
[INTERNAL] Ravi: And you confirmed it held? Sometimes these proxy changes need a device reboot or a cache clear to fully take.
[EXTERNAL] Curtis: We had a supervisor keep hammering login for half an hour and it was solid. Then Wednesday's full shift, no tickets. Thursday, no tickets. It's done. The other three mills, by the way, we've now pre-added your domains to the proxy allowlist before we roll the appliance out to them, so we shouldn't repeat this when Gary and the others get their turn.
[INTERNAL] Ravi: That's the right move, and honestly that's the thing I'd have asked you to do. Proactive allowlisting before the rollout hits the other sites.
[INTERNAL] Derek: So to state it plainly for my own notes — this was the Birmingham proxy stripping the auth header, root cause on the customer's network, resolved by allowlisting our domains. Nothing on our platform to change.
[EXTERNAL] Curtis: Correct. I want to be really clear about that, Derek, because I don't want your team chasing a ghost. It was ours. Your proxy — sorry, our proxy — ate the header. Your product did exactly what it should when handed a request with no credentials. If anything I was impressed that Ravi's logs were detailed enough to see the header was missing rather than malformed. That's what let me go yell at the right vendor.
[INTERNAL] Ravi: That's genuinely useful feedback, thank you. The header-present-vs-missing distinction in the logs is something we added maybe a year ago for exactly this reason — proxy problems used to be almost impossible to diagnose from our side.
[EXTERNAL] Curtis: It shows. I've had vendor support relationships where the answer to everything is "clear your cache and it's probably your network" with zero evidence, and it drives me up a wall because sometimes it IS my network but I need you to prove it, not just assert it.
[INTERNAL] Derek: The "prove it, don't assert it" bar is a good one. We try to live by it.
[EXTERNAL] Curtis: You cleared it this time. Now — while I've got you both — one thing that's NOT a bug, I just want to sanity-check my own understanding. The session length setting. We have ours set to eight hours because our shifts are long and I hate people re-logging mid-shift. That's an admin setting I control, right? Not something on your end?
[INTERNAL] Ravi: Correct, that's yours — Admin, Security, session settings. You can set it up to twelve hours. If people are getting logged out before your configured window, that's a different conversation, but if eight hours is holding, that's working as intended.
[EXTERNAL] Curtis: Eight's holding fine. I just wanted to confirm I wasn't going to discover next week that the proxy was also messing with that. It's not — people stay logged in the full shift. Good.
[INTERNAL] Derek: Anything else on the tech side, or can we spend the last few minutes on the fun stuff?
[EXTERNAL] Curtis: What's the fun stuff to a CSM?
[INTERNAL] Derek: Expanding your safety leadership cohort, obviously. That's my idea of a party.
[EXTERNAL] Curtis: Ha. Actually, not a crazy topic. We're bringing the Ohio specialty shop's supervisors on next quarter — they got skipped in the first wave because they're small, forty people, and the argument was they were too small to matter. I disagree. Small crew, high-precision work, one mistake is expensive in a way that a big mill absorbs and a small shop doesn't.
[INTERNAL] Derek: I'd argue the small precision shop is exactly where leadership coaching pays back fastest. Fewer people means each supervisor's behavior is a bigger fraction of the culture.
[EXTERNAL] Curtis: That's my argument to the CFO too, almost word for word. I'll steal your phrasing.
[INTERNAL] Derek: Steal freely. Do you want me to put together a small-cohort proposal — pricing and rollout timeline for the Ohio forty?
[EXTERNAL] Curtis: Yeah, send it. Low pressure, next quarter's budget, but I want it in hand so when the window opens I can move fast.
[INTERNAL] Derek: You'll have it by end of week. Ravi, anything you want to leave Curtis with?
[INTERNAL] Ravi: Just — if the proxy rollout to Gary or the others turns up anything even slightly weird, open a ticket and reference this one. I'll flag it so it comes to me and we can compare notes fast instead of rediscovering the whole thing.
[EXTERNAL] Curtis: Appreciated. I've got this ticket number saved. If Gary throws the same error I'll know exactly what to look at, and honestly I'll probably fix it before I even call you.
[INTERNAL] Ravi: That's the dream outcome for a support engineer, someone who doesn't need me.
[EXTERNAL] Curtis: Don't worry, steel finds new and creative ways to break things. You'll hear from me eventually.
[INTERNAL] Derek: On the Ohio proposal — do you want me to include a rough rollout timeline, or just pricing for now?
[EXTERNAL] Curtis: Include a timeline. The CFO won't approve a number without knowing when the people actually start, he thinks in cash flow and calendars. Pricing plus "here's when they onboard" is the package that gets a yes.
[INTERNAL] Derek: Pricing plus onboarding timeline, packaged for the CFO's cash-flow brain. Done. On that ominous note — thanks, Curtis. Proposal Friday, and glad Birmingham's back to normal.
[EXTERNAL] Curtis: Thanks both. Genuinely good support experience. Rare enough that I notice. Talk soon.
