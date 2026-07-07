# Call — Lumen Dance Academy × BetterBark · Support escalation
Date: 2026-06-22 · Call ID: call-091
Participants: [EXTERNAL] Bianca Torres, Studio Operations Manager (Lumen Dance Academy) · [INTERNAL] Maya Chen, CSM

[INTERNAL] Maya: Bianca, hi! How are rehearsals, is the summer showcase season upon you?
[EXTERNAL] Bianca: In full swing. We've got three recitals and a competition team traveling, so I'm running on coffee and adrenaline. But I'm good, thanks for asking.
[INTERNAL] Maya: The classic performing-arts summer. Where's the competition team headed?
[EXTERNAL] Bianca: Regionals in two weeks, then if they place, nationals in August. Which means chaos in August too. There's no off-season in dance, just different flavors of busy.
[INTERNAL] Maya: I don't know how you do it. Well, I appreciate you carving out time. You mentioned a photo issue when you booked, want to jump right in or catch up first?
[EXTERNAL] Bianca: Let's do the photo thing, it's small but it's been nagging at me and a couple of our instructors, and I want it off my plate before the travel chaos.
[INTERNAL] Maya: Totally, go for it, walk me through what's happening.
[EXTERNAL] Bianca: So we onboarded our new cohort of instructors onto the coaching platform, and part of setting up their profiles is uploading a headshot. And a bunch of them just cannot get their photo to upload.
[INTERNAL] Maya: Okay. What happens when they try, exactly?
[EXTERNAL] Bianca: They pick the photo, they hit upload, and after a second it just fails. And the error message is so unhelpful, it's like "something went wrong" or "upload failed, please try again."
[INTERNAL] Maya: So no actual reason given, just a generic failure.
[EXTERNAL] Bianca: No reason at all. So they try again, same thing, and they give up and message me thinking the whole platform is broken.
[INTERNAL] Maya: The generic error with no explanation is frustrating on its own, even setting aside the failure. Is this all of your instructors or just some?
[EXTERNAL] Bianca: That's the thing, it's not everybody. Some instructors uploaded their headshots totally fine, no problem. Others can't, no matter how many times they try. And I couldn't figure out the pattern at first, it seemed random.
[INTERNAL] Maya: But it sounds like you cracked it.
[EXTERNAL] Bianca: I think so, yeah. So these are dance instructors, right, and a lot of them are also professional performers with real photographer-taken headshots. And the ones who can't upload are exactly the ones using their fancy professional photos. High-resolution, straight from a photographer's camera.
[INTERNAL] Maya: And the ones who succeeded?
[EXTERNAL] Bianca: Just used a phone selfie or a cropped photo. Smaller, casual pictures. So it clicked, the successful ones are small files and the failing ones are big files.
[INTERNAL] Maya: That's a genuinely sharp diagnosis. Did you check the actual file sizes to confirm the hunch?
[EXTERNAL] Bianca: I did, because I figured you'd ask. One of the failing ones was like 12 megabytes, huge, straight off a DSLR at full resolution. And the ones that worked were one or two megabytes, phone-sized. So it's clearly a size thing.
[INTERNAL] Maya: That's better evidence than I usually get, honestly. So the large professional headshots fail, the smaller phone photos succeed, and the error gives you no clue that size is the problem.
[EXTERNAL] Bianca: Exactly. If it just said "your photo is too big, please use one under whatever the limit is," my instructors could fix it themselves in ten seconds. Instead it says "something went wrong" and they conclude the platform is junk.
[INTERNAL] Maya: You've basically written the bug report for me. Quick question, does it fail immediately when they hit upload, or does it look like it's trying for a while first?
[EXTERNAL] Bianca: It tries for a second or two, there's a little spinner, and then it fails. So it's not rejecting the file instantly, it's like it starts and then chokes partway.
[INTERNAL] Maya: That's a useful detail too, it attempts the upload and fails mid-process rather than validating and rejecting up front. Suggests it's not even checking the size before trying, it just falls over.
[EXTERNAL] Bianca: Right, which is why a plain-English "too big" message would be so much better than letting it try and die.
[INTERNAL] Maya: Completely agree. And what format are the failing images, do you know? JPEG, PNG, something else?
[EXTERNAL] Bianca: The failing ones I checked were JPEGs, big high-res JPEGs. I don't think it's a format thing, the small JPEGs upload fine. It's purely the size.
[INTERNAL] Maya: Good, so we can rule format out, same type succeeds when small. It's cleanly a size threshold. Let me confirm the specifics. The failing images are large, in the 8-to-12-megabyte-plus range, high-res JPEGs, and the error is a generic "something went wrong" that appears after a brief attempt, with no mention of size or any actionable guidance.
[EXTERNAL] Bianca: That's it exactly. It's not that they can't ever upload a photo, it's that the big ones fail with a useless message.
[INTERNAL] Maya: This is a real product issue, and it's actually a known pattern on our side. Profile photo uploads failing for large images with an unhelpful generic error. I want to file your specifics though, because your concrete file sizes and the "it's the professional headshots" detail will really help the team pin it down.
[EXTERNAL] Bianca: Happy to help. Do you want me to send you one of the failing images so you can see the size for yourself?
[INTERNAL] Maya: If it's easy, an example file, or even just the exact file size and dimensions, would be great to attach. It corroborates the report with hard numbers.
[EXTERNAL] Bianca: I'll grab a couple and send them over this afternoon. So the workaround for now is just, tell them to shrink the photo?
[INTERNAL] Maya: For right now, yes. If they resize or compress the image comfortably under 8 megabytes, it should go through. Any phone can resize, or they can just screenshot their headshot, which shrinks it automatically. Not elegant, but it unblocks them today.
[EXTERNAL] Bianca: The screenshot trick is clever, I'll pass that along, my instructors will find that easier than fiddling with resize settings.
[INTERNAL] Maya: It's the fastest low-tech fix. Screenshot the photo, upload the screenshot, done.
[EXTERNAL] Bianca: Perfect. I just wanted to make sure it wasn't only us doing something wrong. It felt like a bug and I didn't want to keep telling people "just try again" like a broken record.
[INTERNAL] Maya: You were right, it is on our side, and your instinct was spot on. The fix product needs to make is really twofold, handle the larger files properly, and at absolute minimum give an error that actually tells the user what's wrong. I'll note both explicitly.
[EXTERNAL] Bianca: The error message thing is honestly the bigger deal to me. Even if there has to be a size limit, just tell people what it is so they're not stuck guessing.
[INTERNAL] Maya: Completely agree, and I'll emphasize that in the writeup. A clear error would turn this from a support escalation into a ten-second self-serve fix. That's the higher-leverage change.
[EXTERNAL] Bianca: Exactly. I'd rather have a clear limit than a mysterious failure any day.
[INTERNAL] Maya: Noted loudly. Okay, I've got what I need. Let me read it back so we're aligned: profile photo upload fails for large images, roughly 8 megabytes and up, particularly professional-quality headshots straight off a DSLR, and returns only a generic unhelpful error with no mention of file size. Workaround is resize below the limit or screenshot the image. Recommend both handling the larger files and, critically, adding an actionable error message that names the size limit.
[EXTERNAL] Bianca: You captured it better than I did. That's exactly right.
[INTERNAL] Maya: You did the hard part by finding the pattern. Send me those sample files when you get a sec and I'll attach them to the report. I'll chase a timeline and keep you posted. Now, quick catch-up while I have you, how's utilization holding up during the crazy season?
[EXTERNAL] Bianca: Actually good. The instructors like having a coach to talk to about the stress of showcase season, the pushy dance parents, the competition pressure. It's a real outlet for them.
[INTERNAL] Maya: Dance parents are their own genre of stress, I've heard legends.
[EXTERNAL] Bianca: You have no idea. There should be coaching for the parents, honestly. Half our stress is managing the adults, not the kids.
[INTERNAL] Maya: Now there's an untapped market, "coaching for competition dance parents." I'd read that case study. How's the veteran instructor cohort doing, the ones who onboarded a while back?
[EXTERNAL] Bianca: They're great, they're the reason I expanded to the new cohort. My senior instructors use it a lot for the business side, a couple of them run their own studios on the side and coaching helps them with the owner-operator stress.
[INTERNAL] Maya: That's a nice adjacent use case, the studio-owner instructors getting small-business coaching value. Word of mouth from them probably helped the new cohort buy in.
[EXTERNAL] Bianca: Exactly, the new folks trusted it faster because the veterans vouched for it. That peer credibility did more than anything I could say as management.
[INTERNAL] Maya: Peer credibility beats a management memo every time. Are the new instructors, once they get past the photo hurdle, engaging okay otherwise?
[EXTERNAL] Bianca: Yeah, once they're set up they're fine, the photo thing was really the only friction in onboarding. Everything after that has been smooth.
[INTERNAL] Maya: Good, so it's a first-mile problem, not an ongoing one, which makes fixing that error message even more worth it. Alright, I'll let you get back to the chaos. Photo issue is filed with your details, I'll chase a timeline, you'll send the sample files, and your instructors unblock with the screenshot workaround in the meantime.
[EXTERNAL] Bianca: Thank you Maya, that's exactly what I needed. I'll send the sample files this afternoon before I lose the day.
[INTERNAL] Maya: Perfect. Break a leg with the recitals, or is that only for the dancers?
[EXTERNAL] Bianca: We say it to everyone, even the accountants. Oh, one last thing, should the instructors re-try the original big files once you've got a fix, or just leave the resized ones?
[INTERNAL] Maya: Leave the resized ones, they're perfectly fine as profile photos. No need to redo anything once it's fixed, this is purely so future uploads don't hit the wall. I'll let you know when it's resolved regardless.
[EXTERNAL] Bianca: Perfect, one less thing to chase people about. Thanks, talk soon!
[INTERNAL] Maya: Take care, Bianca, and good luck at regionals.
