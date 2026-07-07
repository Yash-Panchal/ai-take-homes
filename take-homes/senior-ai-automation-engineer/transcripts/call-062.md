# Call — BetterUp Internal · QBR Prep Sync
Date: 2026-06-22 · Call ID: call-062
Participants: [INTERNAL] Priya Nair, CSM · [INTERNAL] Derek Okafor, CSM · [INTERNAL] Ravi Patel, Support Engineer

[INTERNAL] Priya: Okay, are we all here? Derek, you're frozen. Derek?
[INTERNAL] Derek: I'm here, I'm here, my camera's just being dramatic. Give it a second.
[INTERNAL] Priya: There you are. Ravi, thanks for hopping on — I know support prep isn't usually your circus.
[INTERNAL] Ravi: It's not, but you two keep citing my ticket data in QBRs and getting it slightly wrong, so I invited myself to fix that at the source.
[INTERNAL] Priya: When did we get it wrong?
[INTERNAL] Ravi: Last quarter Derek told an account they'd had "zero issues all year" when they'd had three. All resolved, but not zero.
[INTERNAL] Derek: They felt like zero.
[INTERNAL] Ravi: Feelings aren't ticket counts, Derek.
[INTERNAL] Derek: That's fair and also a personal attack.
[INTERNAL] Ravi: It can be both.
[INTERNAL] Priya: Deserved. Okay — this is prep for the joint QBR block next week. We've got four accounts back to back and I want us telling a consistent story. Let me pull up the list.
[INTERNAL] Derek: Which four?
[INTERNAL] Priya: Quarry Heights, Sterling Mutual, Harlow Health, and Pemberton. All mine or shared. Derek, you're on Quarry Heights with me since Roland likes you better.
[INTERNAL] Derek: Roland likes everyone who lets go of the bike at the right time. Long story.
[INTERNAL] Priya: I won't ask. Let's go account by account. Quarry Heights — Roland's mid-acquisition, program's stable, no issues, the QBR is basically a relationship-maintenance session. Story is "you're the calm in your chaos."
[INTERNAL] Derek: That's exactly the read. He told me the coaching program was the one thing not on fire this quarter. I'd lead with that and not overload him.
[INTERNAL] Priya: Agreed, keep it light. Sterling Mutual — this one has meat. Their security analyst is pushing for a read-only auditor role, it's a real feature request, Sam wrote it up. For the QBR we acknowledge it, show it's captured, don't overpromise.
[INTERNAL] Ravi: Just don't let anyone imply a date. That request touches access control and it's not trivial to build correctly. The last thing we want is a CSM saying "next quarter" in a room.
[INTERNAL] Priya: Noted, hard rule: no dates on the auditor role. Harlow Health — Gwen's got the coach bulk-reassignment pain, also a real feature request, and the orphaned-clinician risk angle is compelling. Story is "we heard you, it's escalated, here's the interim backend option."
[INTERNAL] Ravi: On the interim backend option — I want to be careful. We *can* script a batch coach reassignment on the backend, but it's not something I want to advertise as a standing service, or every account will want it weekly. For a genuine coach departure, sure. Not as a routine.
[INTERNAL] Priya: Good caveat. Frame it as an exception for real departures, not a feature. Pemberton — Danielle and Marcus flagged the video-freeze thing, forty minutes, Chrome, audio continues, refresh recovers. That one's a live bug I'm writing up separately. For the QBR I just want to say "we've got it, engineering's looking."
[INTERNAL] Ravi: Wait, the video freeze at forty minutes — Pemberton reported that too?
[INTERNAL] Priya: "Too"? Who else?
[INTERNAL] Ravi: I've seen the same shape come through support in the last couple weeks. I'm not going to name accounts because I'd have to check, but Pemberton's not the only one describing a Chrome video freeze around the same point in the session. I'll keep an eye on whether it's clustering.
[INTERNAL] Priya: That's exactly the kind of thing I want you watching. If it's multiple accounts, it's not a Pemberton quirk. I'll flag mine and you connect the dots on your side.
[INTERNAL] Ravi: Will do. Don't say "we know it's affecting multiple customers" in the QBR though — Danielle doesn't need to know she's part of a pattern, it just makes it sound bigger and scarier.
[INTERNAL] Derek: Agreed, keep the customer-facing framing account-local.
[INTERNAL] Priya: Fine. Account-local framing, pattern-watching stays internal. Quick one, Ravi — if it is clustering, what's your threshold for escalating it as a real multi-account bug versus coincidence?
[INTERNAL] Ravi: Three independent accounts with the same specific shape — same browser, same timing, same recovery — and I open a formal cross-account bug and loop engineering. Two could be coincidence, three is a pattern.
[INTERNAL] Priya: Good rule. So Pemberton's one data point in your bucket, not the whole thing.
[INTERNAL] Ravi: Exactly. I'll do the counting. You just file yours cleanly so it's a usable data point.
[INTERNAL] Priya: Understood. Okay, that's the four. Derek, division of labor — you take Quarry Heights lead, I take the other three, Ravi you're on standby for any support-data question.
[INTERNAL] Derek: Works. Can I make a suggestion? For Sterling, since it's a security-heavy account, can we have Ravi's actual ticket numbers ready in case they ask "how many issues have we had this year"? Nothing kills credibility like a CSM guessing.
[INTERNAL] Ravi: This is my entire reason for being on this call. Yes. Sterling's had four support tickets this year, all resolved, average resolution under a day. I'll drop the real numbers in the prep doc so nobody freelances.
[INTERNAL] Priya: See, this is why we invited you. Or you invited yourself. Either way.
[INTERNAL] Ravi: I invited myself and you're welcome.
[INTERNAL] Derek: Okay, unrelated, but I have to tell you both my petty dream and then we can move on. Every QBR season I fantasize about filing a completely fake P0 — like, "CRITICAL: the whole platform is down for one imaginary customer" — just to watch how fast product actually mobilizes. Like a fire drill they don't know is a drill.
[INTERNAL] Priya: Derek.
[INTERNAL] Derek: It's a fantasy, Priya. I'm not going to do it. I just want to know the response time.
[INTERNAL] Ravi: You realize I'm the person who'd get paged at 3am for your imaginary customer.
[INTERNAL] Derek: Which is exactly why it'll never happen. I like you too much and I fear your retaliation.
[INTERNAL] Ravi: Correct fear. For the record, filing a fake severity to game the process is a fireable thing and also deeply annoying, so let's all agree the joke stays a joke.
[INTERNAL] Derek: The joke stays a joke. It's purely a thought experiment I revisit when I'm bored. No P0s, real or imaginary, are being filed today.
[INTERNAL] Priya: Logging it as officially a joke so that if anyone ever reads this transcript they know Derek is all talk.
[INTERNAL] Derek: All talk, no P0. That should be on my headstone.
[INTERNAL] Ravi: I'll carve it. Can we get back to Sterling?
[INTERNAL] Priya: Yes. So Sterling — Sam owns the account relationship, but since he's out Thursday, I'm covering the QBR. I need the auditor-role write-up from Sam before the call so I represent it accurately. Derek, remind me to ping him.
[INTERNAL] Derek: Ping Sam for the Sterling auditor-role write-up. Adding it to your list out loud so it's real.
[INTERNAL] Priya: Thank you. Ravi, one more — for Harlow, if Gwen asks whether the backend batch reassignment is available *right now*, what do I tell her?
[INTERNAL] Ravi: Tell her it's possible for a genuine coach departure with a clean member list, it's not self-serve, and she should route it through you and you'll open a support request to me. Don't tell her a turnaround time — I'd need to see the list first.
[INTERNAL] Priya: Possible, not self-serve, route through me, no turnaround quoted. Got it. Anything else either of you want in the prep doc?
[INTERNAL] Derek: Just the Quarry Heights "you're the calm" framing and Roland's acquisition context so I don't walk in cold.
[INTERNAL] Priya: I'll add the acquisition context. Ravi?
[INTERNAL] Ravi: Real ticket numbers for all four accounts, going in the doc by end of day. And I'll flag privately if that video-freeze thing turns out to span more accounts, but that stays out of the customer QBRs.
[INTERNAL] Priya: Perfect division. Let me recap so we're aligned. Derek leads Quarry Heights with the calm-in-chaos framing. I take Sterling with no dates on the auditor role, Harlow with the interim-only backend caveat, and Pemberton with account-local framing on the video freeze. Ravi supplies real ticket numbers into the prep doc and watches the video-freeze pattern internally. I ping Sam for the Sterling write-up. And Derek files zero P0s, imaginary or otherwise.
[INTERNAL] Derek: Zero P0s. Confirmed under duress.
[INTERNAL] Ravi: Good enough for me. Doc's coming by five.
[INTERNAL] Priya: Then we're set. Thanks both — and Ravi, genuinely, thanks for inviting yourself, this was better with you on it.
[INTERNAL] Ravi: I'll invite myself more often. Regret it later. Bye.
[INTERNAL] Derek: Bye, team.
[INTERNAL] Priya: Bye.
