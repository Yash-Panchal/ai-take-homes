# Call — Pemrose Insurance × BetterBark · Support Escalation / Check-in
Date: 2026-06-22 · Call ID: call-034
Participants: [EXTERNAL] Gloria Tan, HR Systems Analyst (Pemrose Insurance) · [INTERNAL] Ravi Patel, Support Engineer · [INTERNAL] Maya Chen, CSM

[INTERNAL] Maya: Gloria, thanks for hopping on. I pulled Ravi in from our support engineering side because you mentioned a technical thing in your email and I'd rather have the expert in the room than play telephone.
[EXTERNAL] Gloria: Smart. I appreciate that. I've been on too many calls where the CSM has to "check with engineering and get back to me."
[INTERNAL] Ravi: That's usually me on the other end of that game of telephone, so I'm happy to skip it. Hi Gloria.
[EXTERNAL] Gloria: Hi Ravi. Okay, do you want the housekeeping first or the actual issue?
[INTERNAL] Maya: Let's get the housekeeping out of the way so we can spend real time on the issue. How's the program running overall?
[EXTERNAL] Gloria: Fine, genuinely fine. We've got about 400 people enrolled, mostly claims and underwriting managers. Usage is steady, no complaints about the coaches. I'm the systems person, not the program person, so I mostly hear about it when something breaks.
[INTERNAL] Maya: And today something broke.
[EXTERNAL] Gloria: Something's annoying, which is worse in some ways because it's not dramatic enough for anyone to prioritize but it irritates people every single day.
[INTERNAL] Ravi: Those are my favorite. The papercuts. What's happening?
[EXTERNAL] Gloria: Okay. So when a member wants to find or change their coach, they go to the coach-search page. And they filter — we've got people who want a coach who speaks Spanish, people who want a specific specialty like conflict management, people who care about the coach's timezone because they work odd hours.
[INTERNAL] Ravi: Right, the standard filters — specialty, language, timezone.
[EXTERNAL] Gloria: Right. So they set their filters, they get a list of coaches, they click into one to read the full profile — the bio, the credentials, the whole thing. And then they decide "eh, not quite," and they hit the browser back button to go back to their filtered list.
[INTERNAL] Ravi: And the filters are gone.
[EXTERNAL] Gloria: The filters are gone. Completely reset. They're back to the full unfiltered list of every coach, and they have to re-select Spanish, re-select the specialty, re-select the timezone, all over again.
[INTERNAL] Ravi: Every time they hit back.
[EXTERNAL] Gloria: Every single time. So imagine you're comparing four coaches. You filter, you click coach one, you read, you hit back — filters gone. You re-filter, click coach two, read, hit back — filters gone. It's maddening. People are just giving up and picking whoever's at the top of the unfiltered list, which defeats the entire point of filtering.
[INTERNAL] Ravi: Yeah, that's a real problem, not a papercut, honestly. Let me make sure I've got the exact repro. You go to coach search, apply one or more filters — say language Spanish and specialty conflict management. You get a filtered result set. You click into a coach profile. Then you use the browser's back button, not an in-page "back to results" link — the actual browser back arrow.
[EXTERNAL] Gloria: The actual browser back button, correct. That's what people instinctively use.
[INTERNAL] Ravi: And when you land back on the search page, all the filter selections are cleared and you're seeing the full unfiltered list.
[EXTERNAL] Gloria: Exactly that. Cleared. Every filter, back to default.
[INTERNAL] Ravi: Is there an in-page way back — like a breadcrumb or a "Back to results" button on the profile?
[EXTERNAL] Gloria: There might be, but nobody uses it. When you've been on the internet for twenty years your thumb goes to the back button automatically. You don't hunt for an in-page link.
[INTERNAL] Ravi: No, you're right, and the product should handle the back button gracefully regardless. The expectation is that back returns you to the state you left. Losing the filter state on navigation-back is a bug.
[EXTERNAL] Gloria: Thank you. That's exactly how I'd put it. It's not that the feature doesn't work, it's that it doesn't persist.
[INTERNAL] Maya: Can I ask about scale — is this everyone, or a subset?
[EXTERNAL] Gloria: As far as I can tell it's everyone on our end. It's not one person's browser. I reproduced it myself on Chrome, and one of my colleagues saw the same thing on hers. It's just how the page behaves.
[INTERNAL] Ravi: Which browser were you on when you reproduced it?
[EXTERNAL] Gloria: Chrome, current version. My colleague was also on Chrome I think. I didn't test other browsers, to be honest — Chrome is what we're standardized on company-wide.
[INTERNAL] Ravi: That's fine, Chrome is the important data point. Was there anything different about your setup — incognito, extensions, anything weird?
[EXTERNAL] Gloria: No, totally vanilla. Regular Chrome window, logged in normally, on our corporate network. Nothing exotic.
[INTERNAL] Ravi: Perfect. That's a clean repro. Filters reset on browser-back, Chrome, standard session. I can work with that.
[EXTERNAL] Gloria: How long has this been a thing, do you know? I only started hearing about it recently but that might just be when people started complaining loudly enough to reach me.
[INTERNAL] Ravi: I can't tell you off the top of my head, but that's a useful question and I'll note it. When did the complaints start reaching you?
[EXTERNAL] Gloria: Last few weeks? Maybe a month. It could've been happening longer and people just suffered in silence until enough of them hit it.
[INTERNAL] Ravi: That's often how these go. Papercuts don't get reported until they draw enough blood collectively.
[EXTERNAL] Gloria: Grim but accurate.
[INTERNAL] Maya: So Ravi, on our side — is this something you write up, or is there a workaround we can give people today?
[INTERNAL] Ravi: I'll write it up with Gloria's repro attached — it's clean enough that engineering should be able to reproduce it immediately. As for a workaround, the honest answer is: for now, use the in-page "back to results" link if there is one, rather than the browser back button. That likely preserves state where the browser-back doesn't. But that's a "train your users to fight their instincts" workaround, which isn't a real fix.
[EXTERNAL] Gloria: It isn't, but I'll take it as a stopgap. I can put a one-liner in our internal help doc: "when browsing coaches, use the on-page back link, not your browser's back button." People will ignore it, but at least I documented it.
[INTERNAL] Ravi: That's the right move for now. And I'll push the actual fix — the page should retain filter state on navigation regardless of how you go back.
[EXTERNAL] Gloria: Great. That's really all I had, honestly. Everything else is boring and working.
[INTERNAL] Maya: Boring and working is my favorite status. Oh — did the reporting dashboard end up meeting your needs, by the way? You'd asked a while back about pulling engagement by department.
[EXTERNAL] Gloria: It did, once I found the right filters. It was more capable than I gave it credit for. I just hadn't clicked around enough. Turns out most of what I wanted was already there.
[INTERNAL] Maya: That's good to hear — and a fair reminder that we could surface those capabilities better. Glad it worked out.
[EXTERNAL] Gloria: It's on me for not exploring. It's genuinely fine now. Anything on the roadmap or renewal side you want to touch while we're here?
[EXTERNAL] Gloria: Not from me — that's more my boss's department. I just keep the machine running. If it schedules and it reports and people can log in, I'm happy.
[INTERNAL] Maya: Understood. I'll make sure your boss and I connect separately on the strategic stuff so you're not stuck in a renewal conversation you didn't sign up for.
[EXTERNAL] Gloria: Bless you. I'd rather debug SSO than talk pricing.
[INTERNAL] Ravi: A woman after my own heart.
[EXTERNAL] Gloria: Speaking of SSO — no issue, just confirming — we're on our standard SAML setup and it's been rock solid. I only mention it because the last vendor we had, their SSO fell over every other Tuesday.
[INTERNAL] Ravi: Good to hear ours behaves. If it ever does anything weird, you know where to find me. But steady SSO is how it should be.
[EXTERNAL] Gloria: It's been genuinely boring, which is the highest compliment I can give an auth system.
[INTERNAL] Ravi: Boring auth is the dream. Nobody writes songs about the login that just worked.
[EXTERNAL] Gloria: Ha. Okay, so what happens next on the filter thing? I want to be able to tell my people something concrete.
[INTERNAL] Ravi: I file it today with your repro. You'll get a ticket reference from me by email so you can track it. I can't promise a timeline on the fix, but I can promise it's logged accurately and doesn't get lost. And I'll flag the workaround in the same email so you can copy it into your help doc.
[EXTERNAL] Gloria: That's everything I need. Concrete beats vague.
[INTERNAL] Maya: Then let me recap: Ravi files the coach-search filter-reset bug with your Chrome repro and sends you a ticket reference plus the interim workaround, and I'll take the strategic conversation off your plate and route it to your leadership separately.
[EXTERNAL] Gloria: Perfect. This was refreshingly efficient. Thank you both.
[INTERNAL] Ravi: Thanks for the clean repro, Gloria — you'd make a good support engineer.
[EXTERNAL] Gloria: Don't threaten me with a good time. Bye, both.
[INTERNAL] Maya: Bye, Gloria. Talk soon.
