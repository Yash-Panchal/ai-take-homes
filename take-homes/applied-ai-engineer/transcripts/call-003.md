# Call — Atlas Financial × BetterBark · Onboarding / Security Review
Date: 2026-06-17 · Call ID: call-003
Participants: [EXTERNAL] Renee Park, IT Security Lead (Atlas Financial) · [INTERNAL] Tomás Vela, Implementation

[INTERNAL] Tomás: Renee, good morning. How's the rollout treating you — you sounded a little frayed in your email.
[EXTERNAL] Renee: Frayed is accurate. We're a regulated financial-services shop trying to stand up a new vendor, which means everything I do gets read three times by three different committees. My job this month is basically translating "the dog-training app" into a language my audit team will sign off on.
[INTERNAL] Tomás: I've done a few of these with banks and insurers. The pattern's always the same — the product is the easy part, the access-control paperwork is the mountain.
[EXTERNAL] Renee: You get it. My favorite part is that the training product itself, the actual thing people use — nobody's worried about that. It's genuinely well-liked. It's the plumbing behind it that gets me summoned to conference rooms.
[INTERNAL] Tomás: That's usually a good sign, honestly. When the complaints are all about paperwork and never about the app, the app is doing its job. How's your coffee situation this morning, by the way — you sound like it's been a two-cup start.
[EXTERNAL] Renee: Three, and it's not yet nine. My auditors run on a different clock than the rest of us. Speaking of which — you're an hour behind me, right? You're on the West Coast?
[INTERNAL] Tomás: Pacific, yeah. So this is a civilized hour for you and a slightly aspirational one for me. Don't worry, I've had enough caffeine to keep up.
[EXTERNAL] Renee: Good, because I have a hard forty minutes and a real agenda, so let me drive.
[INTERNAL] Tomás: Please. From your email I've got: the login incident from Friday, the provisioning question, and your security-review checklist.
[EXTERNAL] Renee: Correct. Three items. I keep my agendas short because if I put a fourth thing on the list, one of my committees will find a way to turn it into six.
[INTERNAL] Tomás: A woman who understands scope creep. I'll take notes as we go and read back the actions at the end so nothing slips.
[EXTERNAL] Renee: That's exactly the muscle I need from a vendor. Half of them just nod and I never hear about the thing again. Let's start with Friday because it has a clean resolution and I like to lead with a win.
[INTERNAL] Tomás: My favorite kind of incident — the solved kind. What happened?
[EXTERNAL] Renee: Friday morning, about twenty users couldn't log in. SAML assertions rejected as expired. Help desk lit up around 8:15, everyone in the Chicago office basically.
[INTERNAL] Tomás: Right, I saw the ticket come through. Where did it land — what was the root cause?
[EXTERNAL] Renee: Your support engineer spotted it, actually, and I want to give full credit because she was fast. The assertion timestamps were drifting. Our IdP servers had an NTP misconfiguration after a patch window Thursday night — the time sync didn't come back up correctly. Our clocks were about ninety seconds off.
[INTERNAL] Tomás: Ninety seconds off, so the assertions looked stale by the time they hit us.
[EXTERNAL] Renee: Exactly. Your side rejected the assertions as stale, which is precisely what it should do — that's the security control working. We fixed our time sync Friday afternoon, forced a re-sync across the IdP fleet, and logins have been clean since. Zero recurrence over the weekend.
[INTERNAL] Tomás: Ninety seconds. It's always the boring infrastructure thing, isn't it. Never the exotic one.
[EXTERNAL] Renee: Always. My team spent the first twenty minutes convinced it was your side, naturally, because that's the reflex. Then your engineer asked one question about our patch window and the whole thing unraveled in about four minutes. She was very gracious about it, too, considering we'd basically accused her product first.
[INTERNAL] Tomás: I'll pass that back to her — she'll appreciate hearing it landed well. What was her name, do you remember, so I credit the right person?
[EXTERNAL] Renee: I've got it in the ticket, I'll forward it. Anyway.
[INTERNAL] Tomás: So — confirmed resolved, and the root cause was entirely on the IdP side. A clock problem, not an assertion-handling problem on ours.
[EXTERNAL] Renee: Confirmed. Our incident, your correct behavior. I only bring it up so it's on the record and nobody re-litigates it three weeks from now when it shows up in an incident log.
[INTERNAL] Tomás: Understood — on the record, resolved, cause was your NTP config, our behavior was correct. I won't open anything on it; there's nothing to fix on our end. If your auditors want a statement to that effect I can put it in writing.
[EXTERNAL] Renee: That would actually help. A one-paragraph "vendor confirms assertions were rejected due to client-side clock drift, behavior was per spec" for the file. My auditors love a vendor letter.
[INTERNAL] Tomás: I'll draft that and send it this week. Your auditors will get their letter with the appropriately dry, per-spec language they love.
[EXTERNAL] Renee: The drier the better. If it has a single exclamation point in it they'll assume we're hiding something.
[INTERNAL] Tomás: No exclamation points, understood. I'll keep it as joyless as an incident report should be. Alright — provisioning.
[EXTERNAL] Renee: This is the real one, and it's the blocker for our security review. SSO works fine — that's not the issue. The issue is what happens after. Every user lands as a basic member, full stop. And then one of our admins has to go promote people by hand.
[INTERNAL] Tomás: Manually, one at a time, into the correct role.
[EXTERNAL] Renee: One at a time. For four hundred users at full rollout, that's not a process, it's a punishment. And it's error-prone — someone will fat-finger a finance manager into the wrong role and now I've got a segregation-of-duties finding.
[INTERNAL] Tomás: And "someone" is always the person who's been staring at the same screen for three hours by row two hundred.
[EXTERNAL] Renee: You've met my admins. Around row two hundred everyone's eyes glaze and that's precisely when the mistakes creep in. I'd rather not build the rollout on the assumption that a tired human clicks four hundred times without error.
[INTERNAL] Tomás: So what you need is role assignment driven automatically from group membership.
[EXTERNAL] Renee: Right. We need role assignment to happen automatically from SAML group membership, at login. Our IdP already exposes the groups in the assertion — finance-managers, people-admins, read-only-auditors, and so on. What I want is: you map an IdP group to a BetterBark role, and you apply that mapping on every login, so if someone's group changes on our side, their role changes on yours the next time they sign in.
[INTERNAL] Tomás: Let me play it back to be sure I've got it exactly. Group-to-role mapping, driven off the SAML assertion, evaluated on each login — not only at first provision. So membership changes on your side propagate to our roles automatically, without an admin touching anything.
[EXTERNAL] Renee: That's it precisely. Evaluated every login is the important part. First-provision-only doesn't help me, because people move between groups constantly and I need it to stay in sync, not snapshot once.
[INTERNAL] Tomás: Understood, and the "every login" distinction is exactly the kind of thing that gets lost if I file it sloppily, so I'm glad you emphasized it. And to be blunt about the stakes — what does this block, concretely?
[EXTERNAL] Renee: Without it we can't pass our access-review audit. Our controls require that access maps to a source of truth — our directory groups — not to whatever some admin clicked last Tuesday. Manual promotion means the source of truth is a human's memory, which fails the control. And without passing the audit, we can't go to full rollout. It is the single thing standing between us and turning on all four hundred seats.
[INTERNAL] Tomás: That's exactly the framing I need. I'll write it up as a feature request — SAML group-to-role mapping evaluated on every login — with the access-review audit context attached, because "this unblocks a 400-seat rollout at a regulated financial customer" changes how it gets prioritized versus a generic ask.
[EXTERNAL] Renee: Good. Make sure the audit framing is loud. "Nice to have" gets shelved; "blocks a regulated rollout" gets a meeting.
[INTERNAL] Tomás: I've learned that lesson the hard way. The requests that get built are the ones with a customer's rollout date and a regulator's name attached. I'll make sure both are in the first line, not buried in paragraph four.
[EXTERNAL] Renee: Perfect. If your product team wants to talk to an actual auditor about why the source-of-truth requirement is non-negotiable, I can put one on the phone. Nothing sharpens priorities like a real compliance officer explaining what a finding costs.
[INTERNAL] Tomás: I may take you up on that — an SME on the call does more than a paragraph from me ever could. I'll flag it if the request lands somewhere that a five-minute auditor conversation would unstick.
[EXTERNAL] Renee: Standing offer. Okay, that's two down.
[INTERNAL] Tomás: It'll be loud. What's checklist item three?
[EXTERNAL] Renee: This one, file under gossip, not evidence. A peer of mine at another firm — different industry, I honestly don't know which plan they're on — mentioned at a conference that your data exports "drop rows" on large pulls. That was the whole comment. "Watch their exports, they drop rows on big ones."
[INTERNAL] Tomás: Okay. And have you seen this yourself?
[EXTERNAL] Renee: No. Not once. We haven't even used exports yet — we're not far enough into rollout. I have zero first-hand experience with it. It's pure hearsay, one sentence from one person at a conference bar.
[INTERNAL] Tomás: I appreciate you flagging it as exactly that. Here's how I'll treat it: I'm not going to file a bug off a secondhand rumor with no repro, no account, and no data — that would just be noise in the tracker. But I don't want to wave it away either.
[EXTERNAL] Renee: That's the balance I want. Don't panic, don't dismiss.
[INTERNAL] Tomás: So — I'll ask internally whether anything matches that description, quietly, just to check. And when you do start using exports, let's run a large pull together and validate it row-for-row against source, so you have first-hand evidence for your audit file instead of a rumor. If it's clean, you can document it as tested. If it's not, then we have a real repro and I file it properly.
[EXTERNAL] Renee: That is the correct answer, and honestly better than I expected. An auditor won't accept "a vendor said it was fine," but "we ran a controlled export test and reconciled the counts" they'll take.
[INTERNAL] Tomás: The difference between a rumor and evidence is a reconciliation you can point at. Auditors are just very formal skeptics, and I respect that.
[EXTERNAL] Renee: You'd get along with mine. They'd probably try to recruit you.
[INTERNAL] Tomás: Then we'll build that into your validation phase — a documented export reconciliation test. Nothing filed today off the rumor itself; we'll let the test tell us if there's anything real.
[EXTERNAL] Renee: Perfect. Okay, timeline. If the role-mapping lands, we target full rollout for September. That's the long pole.
[INTERNAL] Tomás: September's realistic if the mapping gets prioritized soon, which the audit framing should help with. What else needs to be true for September on your side?
[EXTERNAL] Renee: The role mapping, the export test documented, and my own team finishing the data-flow diagram for our privacy review. That last one's on me, not you.
[INTERNAL] Tomás: If you want a hand on the data-flow diagram, I can send you our reference architecture doc — it lays out what data lives where, which usually saves customers a week of asking us questions one at a time.
[EXTERNAL] Renee: Send that, it'll save my analyst a lot of emails. He's the one drawing the boxes and arrows, and every unanswered question is another day the privacy review sits open.
[INTERNAL] Tomás: I'll get it over today so he's not blocked. It's a living doc, so if there's a version-drift question later, just ping me and I'll confirm you've got the current one.
[EXTERNAL] Renee: Appreciated. And genuinely — this is the least painful vendor call I've had all quarter, and I've had a lot of vendor calls this quarter.
[INTERNAL] Tomás: I'll take that as high praise given the competition. Alright, was there anything else on the checklist, or is that the three?
[EXTERNAL] Renee: That's the three. Alright, that's my list.
[INTERNAL] Tomás: Then let me read back my actions. One: the vendor letter confirming Friday's incident was client-side clock drift, our behavior per spec. Two: file the SAML group-to-role mapping request, evaluated every login, with the access-review audit blocker context front and center. Three: quietly check internally on the export rumor, and build a documented export-reconciliation test into your validation phase — nothing filed off the rumor itself. Four: send you the reference architecture doc for your data-flow diagram. That the full set?
[EXTERNAL] Renee: That's everything. You're organized, which for once makes my life easier.
[INTERNAL] Tomás: Regulated customers get the organized version of me. I'll confirm receipt on the role-mapping filing by end of week.
[EXTERNAL] Renee: Do that. Should we put a standing thirty on the calendar for two weeks out, so I have a checkpoint before I go back to the committees?
[INTERNAL] Tomás: Let's do it — I'll send an invite for a fortnight from today, same slot, so it's your civilized morning and not my aspirational one. If the filing gets a status update sooner I'll email you rather than making you wait for the meeting.
[EXTERNAL] Renee: That works. And send the letter and the reference doc before then so my file's building while I wait.
[INTERNAL] Tomás: Both go out this week. Go get your fourth coffee, Renee — you've earned it.
[EXTERNAL] Renee: Fourth is a myth I tell myself. Thanks, Tomás.
[INTERNAL] Tomás: Talk in two weeks, Renee.
