# Call — Fenwick Capital × BetterBark · Admin Sync
Date: 2026-06-27 · Call ID: call-067
Participants: [EXTERNAL] Priyanka Rao, Director of HR Technology (Fenwick Capital) · [EXTERNAL] Colin Frost, IT Identity Engineer (Fenwick Capital) · [INTERNAL] Lena Kowalski, Implementation · [INTERNAL] Derek Okafor, CSM

[INTERNAL] Derek: Priyanka, Colin — good to see you. Lena's on with me because your agenda had "provisioning" on it three times and that's her language, not mine.
[EXTERNAL] Priyanka: Ha, guilty. I front-load the word so nobody thinks it's a soft call.
[INTERNAL] Lena: I saw "provisioning" three times and cleared my afternoon. Hi, Colin, I don't think we've met.
[EXTERNAL] Colin: We haven't. I own identity and access on the IT side. Priyanka owns the HR system, I own the plumbing between systems.
[INTERNAL] Lena: The plumbing person is my favorite person on any call. Let's talk pipes.
[INTERNAL] Derek: Before the pipes — Priyanka, how's Fenwick? Markets treating you okay?
[EXTERNAL] Priyanka: The markets are the markets, I stay out of that side. On the people side we're growing — we acquired a smaller shop and we're up about two hundred heads this quarter, which is exactly why the provisioning conversation is urgent.
[INTERNAL] Derek: Two hundred heads is a lot of onboarding. And I imagine some offboarding on the other end.
[EXTERNAL] Priyanka: That's the crux of it. Let me lay out the problem and then Colin can get technical. Right now, when someone joins Fenwick, they flow into our HR system, and eventually they get a BetterBark seat. When someone leaves — and in finance, people leave suddenly, sometimes escorted-out suddenly — we need their access to everything cut immediately. And BetterBark is currently a manual step in that process, which in our world is a compliance problem.
[INTERNAL] Lena: Tell me exactly how the offboarding works today for a BetterBark seat.
[EXTERNAL] Colin: Today it's manual and it's ugly. When someone's terminated, my team gets a ticket to revoke access across all systems.
[INTERNAL] Lena: And most of those revocations are automated, I assume?
[EXTERNAL] Colin: For most of our systems, yes — our identity provider pushes a deactivate signal and the account's gone in minutes. BetterBark isn't wired into that.
[INTERNAL] Lena: So how does BetterBark get handled?
[EXTERNAL] Colin: For BetterBark, someone has to log into your admin console and manually deactivate the user by hand. It's the odd one out.
[INTERNAL] Lena: So BetterBark is the one system that doesn't get the automatic deactivate signal, and a human has to remember to go turn it off manually.
[EXTERNAL] Colin: Exactly. And "a human has to remember" is the phrase that keeps a compliance officer up at night.
[INTERNAL] Lena: Has it actually bitten you, or is it a theoretical risk so far?
[EXTERNAL] Colin: It's bitten us. We've had cases where a terminated employee's BetterBark account stayed active for days because the manual step got missed in the shuffle of a busy termination.
[EXTERNAL] Priyanka: And in finance, an active account for a terminated employee — even a coaching account — is an audit finding. It doesn't matter that it's "just coaching." Our regulators care that access matched employment status, full stop.
[INTERNAL] Lena: Understood. So what you want is for BetterBark to plug into the same automated deprovisioning flow as your other systems — when your identity provider deactivates a user, BetterBark deactivates that user automatically, no human in the loop.
[EXTERNAL] Colin: Precisely. And to be specific about the mechanism, because I've had vendors offer me the wrong thing.
[INTERNAL] Lena: Please be specific, it saves us both a wasted cycle.
[EXTERNAL] Colin: I'm not asking for a webhook I have to build against, and I'm not asking for a nightly CSV sync. Those are both worse than what I have.
[INTERNAL] Lena: Understood — so what's the right mechanism?
[EXTERNAL] Colin: Our whole identity stack speaks SCIM. Every other system in our environment provisions and deprovisions via SCIM against our IdP. What I need is for BetterBark to support SCIM so that user lifecycle — create, update, and critically deactivate — is driven automatically from our identity provider.
[INTERNAL] Lena: That's a very precise ask and I appreciate the precision. SCIM support, so user lifecycle including deprovisioning is automated from your IdP, with the emphasis on the deactivate path because that's your compliance risk. Do I have that right?
[EXTERNAL] Colin: You have it exactly right. Provisioning-in would be nice, but honestly I can live with manual account creation. It's the deprovisioning-out that's the compliance gap. If SCIM only did the deactivate reliably, I'd be 90% happy.
[INTERNAL] Lena: That prioritization is useful — deprovisioning is the must-have, provisioning is the nice-to-have. I want to be straight with you: today we support SSO against your IdP for authentication, but we do not currently support SCIM for automated lifecycle management. So this is a feature gap, not a configuration I can just switch on.
[EXTERNAL] Colin: I suspected as much — I checked your SSO docs and saw authentication but no SCIM. I wanted to confirm I wasn't missing a hidden setting.
[INTERNAL] Lena: You're not missing anything, it genuinely isn't there today. Which means this is a feature request. I can't give you a delivery date, and I won't pretend otherwise. What I can do is write it up with your exact framing — SCIM support for automated deprovisioning, driven by the compliance requirement that access match employment status — and advocate for it.
[EXTERNAL] Priyanka: The compliance framing is the important part. This isn't a convenience request. This is "we may not be able to keep expanding our BetterBark footprint if we can't close this audit gap." We just added two hundred people. If our security team decides the manual deprovisioning is an unacceptable risk, that's a headwind on the whole account, not just an annoyance.
[INTERNAL] Derek: I want to make sure that lands in the write-up as more than color — the lack of SCIM deprovisioning is a potential blocker on Fenwick's continued expansion, per your security team's risk posture. That's a retention-and-growth flag, not just a feature wish.
[EXTERNAL] Priyanka: That's the accurate weight. We're not threatening anything — we like the program — but I have to represent that my security team is watching this.
[INTERNAL] Lena: Represented accurately. And Colin, so the request is as strong as possible internally — can you tell me which IdP you're on? SCIM's a standard, but the request is more concrete if I can say "customer runs X and needs SCIM against it."
[EXTERNAL] Colin: We're on a standard enterprise IdP, SCIM 2.0. I can put the exact version and our connector details in an email so it's documented.
[INTERNAL] Lena: Are you doing SCIM against BetterBark for any other coaching or benefits vendor today, out of curiosity? It helps to know if we're the outlier.
[EXTERNAL] Colin: Every other people-facing SaaS we run is on SCIM. You're genuinely the only one that isn't, which is why you stick out on the audit.
[INTERNAL] Lena: That's a strong data point for the write-up — "only non-SCIM system in the customer's people-tooling stack." SCIM 2.0, and yes please on the email — the more specific the connector details, the better the request reads to our team. I'll attach it.
[EXTERNAL] Colin: Will do. Is there anything I can do in the interim to make the manual process less risky? Because we're stuck with manual until this ships, however long that is.
[INTERNAL] Lena: A couple of things, and let me be honest about which are real. One that's real today: we can give your IT team a scoped admin role so that deprovisioning doesn't require an HR person to be the bottleneck — your identity team can do the deactivate directly as part of your existing termination runbook. It's still manual, but it's in your team's hands and workflow rather than a separate ask to Priyanka's team.
[EXTERNAL] Colin: That actually helps. If I can fold the manual BetterBark deactivate into my own termination checklist rather than firing a ticket to HR, that closes a lot of the timing gap. The delay was mostly the handoff.
[INTERNAL] Lena: Then let's set that up — a scoped admin role for your identity team, purely for user deactivation, so it's one line in your existing runbook. It's a workaround, not the fix, but it shrinks the window.
[EXTERNAL] Priyanka: I'm fine with Colin's team holding that. It's their process anyway.
[INTERNAL] Lena: The second thing I could offer is a periodic reconciliation report — I'd send you a list of active BetterBark accounts you could diff against your active-employee roster to catch any that slipped. But I'd rather that be a backstop than a primary control.
[EXTERNAL] Colin: A reconciliation report as a monthly backstop is smart — belt and suspenders. Even after we have SCIM I might keep that.
[INTERNAL] Lena: Then I'll set up both — the scoped IT admin role now, and a monthly active-accounts reconciliation export as a backstop. Neither replaces SCIM, but together they shrink the compliance gap while the real feature waits.
[INTERNAL] Derek: And on the feature itself — I'll be honest about the process. It goes into the product queue, I advocate, and I keep you posted on where it lands. Given it's a security-and-compliance-driven request from a growing finance account, it tends to get attention, but I'm not going to hand you a date I can't keep.
[EXTERNAL] Priyanka: That's the honest answer and I'll take honest over optimistic every time. As long as it's captured with the compliance weight and we've got the interim controls, I can defend this to my security team.
[INTERNAL] Lena: Let me recap so nothing's ambiguous. One: I write up the SCIM support request, deprovisioning as the must-have and provisioning as the nice-to-have, framed by the compliance requirement and Fenwick's expansion-risk. Colin sends the IdP and SCIM 2.0 connector specifics for the write-up. Two: we stand up a scoped IT-only admin role for deactivation so it folds into Colin's termination runbook. Three: I set up a monthly active-accounts reconciliation export as a backstop. And Derek advocates the feature and keeps you posted with no invented date. Complete?
[EXTERNAL] Colin: Complete, and better than I expected. I came in braced for "SSO is basically the same thing" and you didn't say that.
[INTERNAL] Lena: SSO is authentication, SCIM is lifecycle, and they are not the same thing — you'd have been right to walk out if I'd conflated them.
[EXTERNAL] Colin: Exactly. You passed the test you didn't know you were taking.
[INTERNAL] Lena: My favorite kind to pass. I'll get the interim controls moving this week and the write-up circulating.
[EXTERNAL] Priyanka: Thank you both. This was genuinely productive.
[INTERNAL] Derek: Thanks, both of you. Colin, watch for the admin-role setup from Lena. Priyanka, I'll keep the account flag warm on my side.
[EXTERNAL] Priyanka: Appreciated. Talk soon.
[EXTERNAL] Colin: Bye — sending the connector details now.
[INTERNAL] Derek: And I'll circle back within the week once the interim role's live. Bye, both.
[INTERNAL] Lena: Watching for the email. Bye.
