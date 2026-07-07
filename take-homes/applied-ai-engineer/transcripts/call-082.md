# Call — Twin Pines Farms × BetterBark · Support escalation
Date: 2026-06-29 · Call ID: call-082
Participants: [EXTERNAL] Hank Brubaker, Operations Manager (Twin Pines Farms) · [EXTERNAL] Lacey Dunn, Executive Assistant (Twin Pines Farms) · [INTERNAL] Ravi Patel, Support Engineer

[INTERNAL] Ravi Patel: Hi Hank, hi Lacey. Thanks for hopping on. Before the ticket — how long have you two been running sessions through the platform? Helps me know if this is new behavior.
[EXTERNAL] Hank Brubaker: We've been on it about a year now. Rolled it out to the leadership team last summer.
[INTERNAL] Ravi Patel: And the calendar syncing — has that always worked, or is this recent?
[EXTERNAL] Lacey Dunn: That's the thing, it used to be fine. This started maybe a month ago. Before that, reschedules updated cleanly as far as I remember.
[INTERNAL] Ravi Patel: A recent onset is a useful clue — it means something changed rather than it always being broken. Okay. I've got your ticket open but I'd rather you tell me what's happening in your own words. What are we looking at?
[EXTERNAL] Hank Brubaker: Well, Lacey deals with the calendars more than me, so she'll have the details. But the short version is our meeting times are getting crossed up.
[INTERNAL] Ravi Patel: Okay. Lacey, take it from the top whenever you're ready.
[EXTERNAL] Lacey Dunn: Sure. So I book and manage a lot of the coaching sessions for our leadership team. I'm the one who reschedules when Hank inevitably moves things.
[EXTERNAL] Hank Brubaker: In my defense, I run a farm. Weather votes on my calendar.
[EXTERNAL] Lacey Dunn: He's not wrong. Anyway — the problem is what happens after I reschedule a session.
[INTERNAL] Ravi Patel: Walk me through a specific reschedule.
[EXTERNAL] Lacey Dunn: Okay. So Hank had a coaching session booked for, say, 2pm. Something comes up, I go into the platform and move it to 4pm. The reschedule goes through fine, the platform shows 4pm, the coach sees 4pm.
[INTERNAL] Ravi Patel: So far the reschedule itself is working correctly.
[EXTERNAL] Lacey Dunn: Right. But then the calendar invite on Hank's actual calendar still says 2pm. The old time. It didn't update.
[INTERNAL] Ravi Patel: The calendar invite kept the original 2pm even though the session moved to 4pm.
[EXTERNAL] Lacey Dunn: Exactly. So Hank sees 2pm on his calendar, shows up to nothing, because the coach is expecting him at 4pm. Twice now he's sat there confused.
[EXTERNAL] Hank Brubaker: I logged in early like a good boy and nobody was there. Felt like a fool.
[INTERNAL] Ravi Patel: That's a real problem — the source of truth in the app is right, but the calendar the person actually looks at is wrong. How many times has this bitten someone before you escalated?
[EXTERNAL] Lacey Dunn: At least four or five reschedules that I know of. Two ended with someone showing up to an empty session. The rest I caught before they did.
[INTERNAL] Ravi Patel: So it's consistent enough that you've started manually verifying every reschedule. That's real ongoing toil.
[EXTERNAL] Lacey Dunn: Every single one now. I don't trust it, so I double-check, which defeats the purpose of having the calendar sync at all.
[INTERNAL] Ravi Patel: Good way to put it — the sync exists to save you work and instead it's creating verification work. Let me narrow it down. What calendar system is Hank on? Outlook, Google, something else?
[EXTERNAL] Lacey Dunn: Hank's on Outlook. We're a Microsoft shop for the leadership team.
[INTERNAL] Ravi Patel: Outlook. Okay, that's important. Have you seen this happen on any other calendar system, or is it just the Outlook folks?
[EXTERNAL] Lacey Dunn: Funny you ask. Our field ops guys use Google Calendar, and I reschedule for a couple of them too. Their invites update fine. It's only Hank and the other Outlook people where the old time sticks.
[INTERNAL] Ravi Patel: That's a very clean distinction. So on Google Calendar the rescheduled time updates correctly, but on Outlook the invite holds the original time.
[EXTERNAL] Lacey Dunn: That's exactly the pattern. Google updates, Outlook doesn't. I've done both in the same afternoon and watched it happen.
[INTERNAL] Ravi Patel: That side-by-side comparison is extremely useful — same action, same day, only difference is Outlook versus Google, and only Outlook fails to update. That points squarely at the Outlook calendar sync.
[EXTERNAL] Lacey Dunn: I'm glad it makes sense to you. I thought I was going crazy for a while.
[INTERNAL] Ravi Patel: You're not. Let me confirm the specifics I'll write up: when a session is rescheduled, the Outlook calendar invite continues to show the original time instead of the new time, while Google Calendar invites update correctly to the new time. Is that accurate?
[EXTERNAL] Lacey Dunn: That's word for word accurate. You can quote me.
[EXTERNAL] Hank Brubaker: And it's not a one-off. It's every reschedule for the Outlook people, near as we can tell.
[INTERNAL] Ravi Patel: Every reschedule, that's good to know — consistent, not intermittent. How many of your leadership are on Outlook and hitting this?
[EXTERNAL] Lacey Dunn: Six of them, including Hank. All Outlook, all affected. The two Google users are fine.
[INTERNAL] Ravi Patel: Six affected. Alright. I want to be transparent — this sounds familiar to me, so it may already be tracked on our side, but I'm going to write it up with your details regardless so your account is attached to it.
[EXTERNAL] Lacey Dunn: That's fine. I just want it fixed so I stop double-checking every reschedule manually.
[INTERNAL] Ravi Patel: Understood. Let me give you a workaround for right now so Hank stops showing up at the wrong time. After you reschedule in the platform, the reliable fix on Outlook is to manually delete the stale invite and re-add the correct time, or have Hank check the app itself as the source of truth rather than his Outlook calendar.
[EXTERNAL] Lacey Dunn: I've kind of been doing the manual delete-and-re-add already, just to be safe. It's annoying but it works.
[INTERNAL] Ravi Patel: It works but it's exactly the manual toil you shouldn't have to do. That's why I'm filing the underlying bug — the workaround is a band-aid, the sync should just update.
[EXTERNAL] Hank Brubaker: As long as I stop looking like the guy who can't read a calendar, I'm happy.
[INTERNAL] Ravi Patel: We'll get you there. For now, treat the app time as gospel and Lacey's manual re-add as the safety net. I'll get you the ticket reference so you can track the real fix.
[EXTERNAL] Lacey Dunn: Perfect. And is there anything on my side I should check — like a setting in how the calendar's connected?
[INTERNAL] Ravi Patel: Good question, and worth ruling out. Let me confirm — the Outlook calendar connection was set up through the standard integration, not a manual ICS feed?
[EXTERNAL] Lacey Dunn: Standard integration. Hank connected his Outlook through the settings when he onboarded. Nothing custom.
[INTERNAL] Ravi Patel: Then this isn't a config issue on your end. It's the sync behavior itself. You've set it up correctly.
[EXTERNAL] Lacey Dunn: Good, one less thing to worry about being my fault. One more question — does it matter whether I reschedule from the web or the mobile app? I use both.
[INTERNAL] Ravi Patel: Good instinct to check. Have you noticed a difference between the two when you reschedule?
[EXTERNAL] Lacey Dunn: Now that I think about it, no. I've done it from both and the Outlook invite stays on the old time either way. Web or app, same problem.
[INTERNAL] Ravi Patel: That's helpful — it means the issue isn't in one client, it's in the calendar sync itself downstream of the reschedule. I'll note it happens regardless of where you initiate.
[EXTERNAL] Lacey Dunn: Makes sense. I just didn't want to be doing it wrong on one of them.
[INTERNAL] Ravi Patel: You're not. Your diagnostic work — the Google-versus-Outlook comparison — is honestly better than most bug reports I get.
[EXTERNAL] Hank Brubaker: Lacey runs a tight ship. That's why we keep her.
[EXTERNAL] Lacey Dunn: I'll add that to my raise argument, thank you Hank.
[INTERNAL] Ravi Patel: I'll put it in writing so you have documentation. Free reference from support.
[INTERNAL] Ravi Patel: Documented, for the record. Okay — to recap: I'm filing the Outlook reschedule sync bug with your details, noting Google works and Outlook doesn't, six affected users. I'll send you the ticket reference and the manual workaround steps in writing.
[EXTERNAL] Lacey Dunn: That covers it. Thank you for actually listening, Ravi.
[INTERNAL] Ravi Patel: Of course. I'll be in the ticket thread if anything else surfaces. Thanks both.
[EXTERNAL] Hank Brubaker: Thanks. Back to the fields for me. Bye.
[EXTERNAL] Lacey Dunn: Bye, Ravi.
[INTERNAL] Ravi Patel: Take care. Bye now.
