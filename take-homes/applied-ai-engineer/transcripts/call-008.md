# Call — Northwind Logistics × BetterBark · Support
Date: 2026-06-19 · Call ID: call-008
Participants: [EXTERNAL] Marcus Reed, HR Director (Northwind Logistics) · [INTERNAL] Sam Oduya, CSM

[INTERNAL] Sam: Marcus, twice in one week — lucky me. Did the hiring panel go okay yesterday?
[EXTERNAL] Marcus: We made two offers, both accepted, so I'll call it a win. Now I just have to onboard them into the cornfield DC, which brings its own joy. But that's not why I'm here.
[INTERNAL] Sam: The cornfield DC — I still can't picture it. That's the Columbus one, the new build surrounded by actual corn?
[EXTERNAL] Marcus: Corn as far as the eye can see. You drive twenty minutes past the last gas station and then there's a distribution center the size of an airport. It's surreal in July.
[INTERNAL] Sam: I grew up near farmland, so that image is weirdly comforting to me. Big box in the middle of nowhere.
[EXTERNAL] Marcus: Then you'd feel right at home. The parking lot alone is bigger than the town I recruit half the crew from.
[INTERNAL] Sam: That tracks. Recruiting local, or busing people in for the season?
[EXTERNAL] Marcus: Both. We hire everyone within thirty miles and then run shuttles for the rest. It's a whole logistics problem before anyone even touches a package.
[INTERNAL] Sam: I'd pay to see it. Peak season ramping up out there?
[EXTERNAL] Marcus: Ramping is generous — it's a stampede. We hire in waves this time of year and the whole DC doubles in headcount by August. Which is exactly why the thing I'm about to tell you matters, but let me not get ahead of myself.
[INTERNAL] Sam: No, you booked a support slot, so something's actually broken this time as opposed to hiding behind a filter chip.
[EXTERNAL] Marcus: Ha. Yes. Two things, and I'll tell you up front one of them is going to sound dumber than the other.
[INTERNAL] Sam: My favorite kind of agenda. Real one first?
[EXTERNAL] Marcus: Real one first. A bunch of our warehouse folks on Android say the app won't open anymore. It crashes the second they tap the icon. Like, splash screen, then straight back to the home screen. Doesn't even get to the login.
[INTERNAL] Sam: Crash on launch — it dies before you can even sign in. When did this start?
[EXTERNAL] Marcus: Right after the last app update. That's the pattern. The ones who updated are the ones crashing. The ones who haven't updated yet are totally fine. And the iPhone people are all fine across the board.
[INTERNAL] Sam: So it's Android-only, and specifically Android that's taken the latest update. Non-updated Android is fine, iOS is fine. That's a very clean correlation — the update broke launch on Android.
[EXTERNAL] Marcus: That's how it reads to me, and I'm not exactly a mobile engineer. But the shape's obvious: update the Android app, it stops opening.
[INTERNAL] Sam: How many people are we talking about?
[EXTERNAL] Marcus: A dozen or so have actually reached me. But here's the thing you have to understand about warehouse workers — that dozen means the real number is triple that, easy.
[INTERNAL] Sam: Say more about that math.
[EXTERNAL] Marcus: Warehouse folks don't file tickets. If an app doesn't open, they don't email HR about it, they just... stop using it. They've got a job to do on a clock. A broken app isn't a problem they escalate, it's a thing they shrug at and move on from. So for every one who bothered to tell me, there are two or three who just quietly stopped opening it and I'll never hear from them.
[INTERNAL] Sam: Right — the silent-failure population. That's actually an important detail for the write-up, because it means the crash count from tickets is going to massively undercount the real impact. A dozen reported at a site like yours could easily be thirty-plus actually hitting it.
[EXTERNAL] Marcus: Exactly. And these are the people I most want engaged, because getting their dogs trained is the whole reason we bought this. If the app silently dies for warehouse workers after an update, that's my adoption number quietly bleeding out and I don't even see it happening.
[INTERNAL] Sam: That's the real cost and I'll say so in the ticket — not just "app crashes," but "app crashes for exactly the population that won't report it, so the visible number understates it."
[EXTERNAL] Marcus: You get it. That's why I like working with you and not the ticket portal. The portal would've made me pick a severity from a dropdown and then argued with me about it.
[INTERNAL] Sam: The dropdown and I have a complicated relationship. Anyway — the crew that's affected, are these mostly new hires or your seasoned folks?
[EXTERNAL] Marcus: Mix. But it lands hardest on the seasonal wave because they're the ones we just told "download the app, this is how you book your dog's training." First impression of the whole program is a splash screen and then nothing.
[INTERNAL] Sam: That's the worst possible first touch. You spend all the onboarding energy pointing them at it and it faceplants on launch.
[EXTERNAL] Marcus: Right in front of a supervisor holding a clipboard, no less. It doesn't inspire confidence in the "we invested in your growth" speech.
[INTERNAL] Sam: Now — this matches an issue I believe is already tracked from another customer after the 4.2 release. Same shape: Android crash on launch, correlated with the update, iOS unaffected.
[EXTERNAL] Marcus: So it's not just us. Somehow that's comforting and infuriating at the same time.
[INTERNAL] Sam: The universal support emotion. Let me confirm it's the same one, and I'll attach Northwind to it so your count is represented and you get the fix notice when it ships. Do you know roughly which Android versions or device models your folks are on? If it's concentrated on a particular OS version, that helps engineering.
[EXTERNAL] Marcus: It's a mess of cheap Android phones, honestly — whatever's on sale. I can ask the two supervisors to poll their crews for makes and models if that'd help.
[INTERNAL] Sam: It would, genuinely. Even a rough "mostly Samsung, mostly Android 13" narrows the repro. No rush — send it whenever the supervisors get a minute. In the meantime, the practical workaround for anyone stuck: if they haven't updated, tell them to hold off updating; if they already did and it's crashing, uninstalling and reinstalling the previous version sometimes gets them back in, though that's fiddly on Android.
[EXTERNAL] Marcus: I'll pass "don't update" down the chain. The reinstall dance I won't inflict on warehouse crews, they'll mutiny. Better to just get it fixed.
[INTERNAL] Sam: Fair. The fix is the real answer.
[EXTERNAL] Marcus: How do these things usually move once you attach us? I'm not asking for a promise, I just want to know what to tell my comms director when she inevitably asks.
[INTERNAL] Sam: Honest answer: attaching a second affected customer with your kind of impact framing tends to help it get prioritized, but I won't quote you a date I can't stand behind. What I can promise is you'll get the fix notice the moment it ships, and I'll ping you directly on top of that.
[EXTERNAL] Marcus: That's all I need. A straight answer and a heads-up beats a fake date every time.
[INTERNAL] Sam: Okay — the second thing. The one that's going to sound dumber.
[EXTERNAL] Marcus: Right. And I want you to know our comms director made me raise it. This is not my initiative.
[INTERNAL] Sam: Establishing your alibi. Noted. Go.
[EXTERNAL] Marcus: She noticed the confirmation emails your system sends have "BetterBrak" — B-E-T-T-E-R-B-R-A-K — in the footer. Your own company name, misspelled, right there in the email footer. BetterBrak.
[INTERNAL] Sam: Oh no.
[EXTERNAL] Marcus: Oh yes. BetterBrak. Every confirmation email, apparently.
[INTERNAL] Sam: That's — yeah, that's genuinely embarrassing. In the footer, so it's on every one of them.
[EXTERNAL] Marcus: Every one. And she called it, quote, "a P0 brand catastrophe" and said she's, quote, "genuinely alarmed." She used the word alarmed. About a typo. I told her I'd relay it with a straight face and I am now doing that, and I want you to know that face is costing me a great deal.
[INTERNAL] Sam: Your professionalism is noted and honored. Okay — let me split this fairly. In fairness to your comms director: a typo of our own company name in every single outbound email footer is genuinely embarrassing, and we absolutely should fix it. It's sloppy and it's the kind of thing a sharp-eyed customer notices. So she's not wrong to flag it.
[EXTERNAL] Marcus: She will be pleased to hear she's not wrong. She lives for that.
[INTERNAL] Sam: In fairness to reality, though: nobody's data is at risk, nothing is broken, no member is blocked, no session is missed. It's a spelling error in a footer. So I'll get it fixed — it's a quick copy change — but I'm not going to wake anyone up in the middle of the night for it, and it's not a P0 in the sense that word actually means.
[EXTERNAL] Marcus: That's exactly the energy I was hoping for. She'll be told it was escalated with maximum urgency. You and I will know the truth. Everyone gets to keep their dignity.
[INTERNAL] Sam: A little diplomacy makes the world go round. I'll log the typo as a low-priority copy fix — real, worth doing, not dramatic — and it'll get cleaned up in the normal course. Your comms director's vigilance is appreciated and will be described in the most flattering possible terms.
[EXTERNAL] Marcus: Perfect. Send her a thank-you and she'll be insufferable for a week, but a happy insufferable.
[INTERNAL] Sam: The best kind. Is she the one who caught the thing on the printed badges last year, or is that a different crusade?
[EXTERNAL] Marcus: Same one. She has a genuine gift for finding the one wrong letter on anything with our name near it. In fairness it's a useful gift, I just wish it came with a volume knob.
[INTERNAL] Sam: Every team needs one. I'd rather have the person who spots "BetterBrak" than the person who ships it. Anything else while I have you, or is that the two?
[EXTERNAL] Marcus: That's the two. Fix the crashing app before the typo, in case that needed saying.
[INTERNAL] Sam: It didn't, but confirmed and I appreciate you saying it out loud — the crash is the priority, the footer is housekeeping. So: I'll confirm the Android crash-on-launch is the tracked 4.2 issue and attach Northwind so your count and the silent-failure framing are represented; you'll poll the supervisors for device models when you can; and I'll log the "Bettreup" footer typo as a low-priority copy fix. Send you tracking links for both?
[EXTERNAL] Marcus: Send them. My comms director will want the typo one framed and mounted.
[INTERNAL] Sam: I'll make it look very official. And good luck with the August stampede — sounds like you'll need every one of those two new hires.
[EXTERNAL] Marcus: And then some. Go onboard your cornfield hires is basically my whole July.
[INTERNAL] Sam: Go do exactly that, Marcus. The cornfield awaits.
[EXTERNAL] Marcus: The cornfield calls. Thanks, Sam.
[INTERNAL] Sam: Anytime. Talk soon.
