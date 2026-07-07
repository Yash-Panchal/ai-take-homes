# Call — Stallard Freight × BetterBark · Support Escalation
Date: 2026-06-19 · Call ID: call-020
Participants: [EXTERNAL] Roy Petrakis, IT Coordinator (Stallard Freight) · [INTERNAL] Ravi Patel, Support Engineer · [INTERNAL] Derek Okafor, CSM

[INTERNAL] Derek: Roy, thanks for hopping on. I pulled Ravi in from our support engineering side since you flagged this as a technical thing rather than an account thing.
[EXTERNAL] Roy: Appreciate it. I'm the guy who gets the "the app doesn't work" tickets internally, so I'd rather talk to someone technical than play telephone.
[INTERNAL] Ravi: That's me. Play telephone with me directly. Before we dig in — are you the only one on your side, or is anyone from your fleet ops joining?
[EXTERNAL] Roy: Just me. Our ops manager wanted to be here but there's a load stuck at a weigh station, so he's dealing with that. Trucking, everything's on fire somewhere.
[INTERNAL] Ravi: Understood, we can loop him in on the follow-up. And how do you want to handle this — screen share, or you describe and I ask questions?
[EXTERNAL] Roy: I'll describe. Half these phones aren't in front of me anyway, they're out on the road. I'm going off what drivers told me and a couple I looked at yesterday.
[INTERNAL] Ravi: That's fine, secondhand-but-detailed is workable. What are you seeing?
[EXTERNAL] Roy: Okay. So Stallard's a trucking outfit — dispatchers, drivers, yard crew. A big chunk of our people are on Android because that's what the company phones are. The rest are iPhone, mostly the office folks.
[INTERNAL] Ravi: Got it. Android-heavy fleet, iPhone office. Go on.
[EXTERNAL] Roy: Starting about — I want to say ten days ago? — I've had a wave of drivers telling me the app won't open on their phones. And when I say won't open, I mean it opens and immediately closes. Tap the icon, splash screen flashes, gone. Back to the home screen.
[INTERNAL] Ravi: Immediate crash on launch. Not a login problem, not a hang — it closes right after the splash.
[EXTERNAL] Roy: Right. It doesn't even get to the login. You never see a login screen. Splash, then poof.
[INTERNAL] Ravi: And this is Android specifically?
[EXTERNAL] Roy: That's the pattern I noticed. It's the Android users. My office people on iPhones aren't complaining. I use an iPhone myself and mine's totally fine, which is why it took me a bit to take the drivers seriously, honestly. I couldn't reproduce it on my own phone.
[INTERNAL] Ravi: That's a really useful data point — you can't repro on iOS, the crashers are all Android. Do you know roughly how many drivers, and are they all on the same app version?
[EXTERNAL] Roy: Volume-wise, I've had maybe fifteen, sixteen tickets. Could be more not bothering to file — drivers aren't big on tickets. On the version, that's a good question. I know some of them updated recently because the company MDM pushes updates. Let me think — yeah, the ones complaining are the ones who got the recent update.
[INTERNAL] Ravi: So the crashers updated to the newest version, and after that update the app crashes on launch for them.
[EXTERNAL] Roy: That lines up, yeah. I had one driver, Danny, who's sharp — he told me it was "totally fine until the phone updated it, now it won't even open." And he tried the usual stuff. Cleared cache, restarted the phone, nothing.
[INTERNAL] Ravi: Did anyone try uninstalling and reinstalling?
[EXTERNAL] Roy: Danny did. Reinstalled fresh, same thing — installs fine, opens, dies. So it's not a corrupted install.
[INTERNAL] Ravi: That rules out a lot. Clean reinstall still crashing on launch means it's the build itself on those devices, not leftover data. What Android versions are we talking — do the company phones vary, or are they standardized?
[EXTERNAL] Roy: They vary. It's a mix. We buy phones in batches so there's a spread of models and OS versions across the fleet. I couldn't tell you it's one specific Android version, if that's what you're getting at. It feels broader than that.
[INTERNAL] Ravi: That's what I'm probing — whether it's a specific OS version or the app version across the board. From what you're describing, it's tracking with the app update, and it's hitting a range of Android devices, while iOS is unaffected. Does that match?
[EXTERNAL] Roy: That matches exactly. It's not "old phones" or "one weird model." It's "Android phones that took the update." iPhones fine.
[INTERNAL] Derek: Roy, just so I understand the business impact — are these drivers blocked from something they need, or is it more of an annoyance?
[EXTERNAL] Roy: Bit of both. The drivers use the app for their dog-training sessions, which are supposed to help with the whole retention push we're doing — trucking has brutal turnover, that's the entire reason we bought this. So when a driver can't open the app, they can't do their session, and they shrug and go "well, I tried," and that's exactly the disengagement we're paying to prevent.
[INTERNAL] Derek: Understood. So it's directly undercutting the program's purpose for the population it's aimed at.
[EXTERNAL] Roy: Precisely. My drivers are the whole point and they're the ones locked out.
[INTERNAL] Ravi: Okay. Let me tell you what I'm hearing so you can correct me: after the recent app update, the Android app crashes on launch — splash screen, then close, before login — across a range of Android devices, while iOS is completely unaffected. Clean reinstall doesn't fix it. That the shape of it?
[EXTERNAL] Roy: That's it. You said it better than I did.
[INTERNAL] Ravi: I'll be straight with you — that shape is familiar. It may already be something we're tracking, so I want to confirm against what we've got rather than send you in circles. Either way I'm going to capture your specifics so your account is attached to it.
[EXTERNAL] Roy: I'd rather be attached to an existing thing than start from zero, honestly. Whatever gets my drivers back in fastest.
[INTERNAL] Ravi: Right. Here's what I need to nail it down: can you get me two or three device models and their Android OS versions from the crashing drivers, plus the exact app version they're on — it's in the phone's app settings, or if the MDM logs it, even easier. And roughly the date the update hit them.
[EXTERNAL] Roy: The MDM logs all of that. I can pull the update push date and the exact version it pushed. Model and OS spread I can get from a few driver phones. I'll have it to you today.
[INTERNAL] Ravi: That's ideal. With the MDM data I can match your version against what we know and confirm whether this is the thing I'm thinking of.
[EXTERNAL] Roy: While we're at it — is there anything I tell the drivers in the meantime? They're going to ask me "when's it fixed" and I need to say something.
[INTERNAL] Ravi: Honest answer: there's no clean client-side workaround if a clean reinstall doesn't help, because the crash is in the build. If any of them absolutely need to get into a session, the mobile web version in a browser should work as a fallback — it's not the app, so it sidesteps the crash. Not as nice, but it unblocks them.
[EXTERNAL] Roy: Mobile web in the browser. Okay. I can tell them that. Some of them will do it, some will wait. But at least it's an answer.
[INTERNAL] Ravi: One caveat on the mobile web — bookmark it for them, don't make them hunt for the URL. If they have to Google their way to the login every time, they won't. I'll send you the exact link to distribute.
[EXTERNAL] Roy: Good call. My drivers will not go hunting. If it's not one tap they're out. Send me the link and I'll push it through the MDM as a bookmark so it just appears on their home screen.
[INTERNAL] Ravi: Even better — a home-screen bookmark that opens the mobile web directly sidesteps the whole crash and it's basically indistinguishable from the app for their purposes. That might actually hold them until the real fix ships.
[EXTERNAL] Roy: That's a clean stopgap. Honestly if the bookmark works well enough they might not even notice when the app gets fixed.
[INTERNAL] Ravi: Ha — don't tell product that, they take pride in the native app. But yes, functionally the driver won't care as long as their session loads.
[EXTERNAL] Roy: My drivers care about exactly one thing: does it open when I tap it. That's the entire spec.
[INTERNAL] Ravi: That's a fair spec and right now the native app fails it on Android. The bookmark passes it. So that's the bridge.
[INTERNAL] Derek: And Roy, once Ravi confirms the tracking status, I'll make sure you get a reference and updates as it moves, so you're not the last to know when there's a fix.
[EXTERNAL] Roy: That's what I need. Right now my problem isn't the bug, it's that I've got nothing to tell fifteen angry drivers.
[INTERNAL] Ravi: Understood. Get me the MDM export and I'll turn the confirmation around fast. If it's what I think it is, you'll at least know there's already momentum behind the fix.
[EXTERNAL] Roy: Deal. Sending the MDM data within the hour. Version, push date, and a few device models.
[INTERNAL] Ravi: Perfect. That's everything I need to close the loop on which issue this is.
[EXTERNAL] Roy: Great. One more — should I have the crashing drivers hold off on any further updates, or does that not matter?
[INTERNAL] Ravi: Holding further updates won't help them — they're already on the version that's crashing, and there's no older version to roll back to through the MDM cleanly. Just get them onto the mobile web bookmark for now. When the fix ships, that'll come as an update they'll want.
[EXTERNAL] Roy: Got it. Bookmark now, take the fix update when it lands. That's clean enough to tell them.
[INTERNAL] Ravi: Exactly. Thanks for taking it seriously — I half expected "have you tried restarting" from you, honestly.
[EXTERNAL] Roy: I half expected it from you. We were both pleasantly surprised.
[INTERNAL] Ravi: You clearly did the restarting homework already. Danny did too. That saved us twenty minutes.
[EXTERNAL] Roy: Danny should work for you. Alright — Ravi, you'll send me the mobile web link, I send you the MDM export within the hour, and Derek loops in my ops manager on the follow-up?
[INTERNAL] Ravi: That's the plan. Link to you today, and once I confirm which issue this is I'll include the status in the same thread.
[INTERNAL] Derek: And I'll add your ops manager so he's not out of the loop while he's dealing with the weigh station.
[EXTERNAL] Roy: Perfect. That weigh station is going to be my whole afternoon, so thank you for making this part easy. Sending the export now.
[INTERNAL] Derek: Thanks Roy — talk soon.
[EXTERNAL] Roy: Bye now.
