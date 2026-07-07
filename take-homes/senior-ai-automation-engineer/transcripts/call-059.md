# Call — Sterling Mutual × BetterUp · Admin Sync
Date: 2026-06-18 · Call ID: call-059
Participants: [EXTERNAL] Yvonne Castellanos, Director of People Operations (Sterling Mutual) · [EXTERNAL] Preet Sandhu, Information Security Analyst (Sterling Mutual) · [INTERNAL] Sam Oduya, CSM · [INTERNAL] Lena Kowalski, Implementation

[INTERNAL] Sam: Morning, everyone. I've got Lena from our implementation team on with me since Yvonne mentioned there'd be some technical questions from security. Preet, welcome.
[EXTERNAL] Preet: Thanks. First time on one of these, so bear with me if I ask something obvious.
[INTERNAL] Sam: There are no obvious questions from security, only expensive ones. Ask away.
[EXTERNAL] Yvonne: Ha. Preet's here because we're going through our annual controls review and the auditors are asking pointed questions about all our vendors, BetterUp included.
[INTERNAL] Sam: Which audit framework, if you can say? It helps me point you at the right documentation.
[EXTERNAL] Preet: SOC 2 Type II for us, and the auditor's leaning on the CC6 access-control criteria this year. That's where most of my questions come from.
[INTERNAL] Sam: That's helpful context — CC6 is exactly the access-control family, so your questions will be well-targeted. We've got a current SOC 2 report I can share under NDA if your team hasn't pulled it.
[EXTERNAL] Preet: We have last year's. I'll want the current one once it's out, but that's a follow-up.
[INTERNAL] Sam: I'll flag it for you the moment the new report drops. Understood. Let me set the agenda — I want to make sure we cover your actual controls questions, so I'll keep the usage stuff brief. Quick health check, then we hand the floor to Preet. That work, Yvonne?
[EXTERNAL] Yvonne: Perfect. And honestly the usage is fine, so keep it short.
[INTERNAL] Sam: Music to my ears. Thirty seconds then: you're at 640 of 700 seats active, completion's steady at 68%, and your renewal in September looks like a formality unless something dramatic happens. Nothing dramatic is going to happen, right?
[EXTERNAL] Yvonne: Not on my watch. We're happy. This is a controls conversation, not a satisfaction one.
[INTERNAL] Sam: Then I'll gladly move on. Preet, the floor is yours.
[EXTERNAL] Preet: Great. So our audit this year is heavy on access controls and least-privilege. The auditors want us to demonstrate that for every system holding employee data, we can show who has access, what they can do, and that the access is appropriate to their role.
[INTERNAL] Lena: That's a common ask and one we're well set up for. Let me walk you through the admin roles we support and you tell me where the gaps are.
[EXTERNAL] Preet: Please.
[INTERNAL] Lena: Today we have three roles: Super Admin — full configuration and user management; Admin — user management and reporting but limited config; and Manager — sees only their own team's engagement, no config. Plus regular members who see only themselves.
[EXTERNAL] Preet: Okay. And within Admin, can you scope what data an Admin sees? Like, region-scoped admins?
[INTERNAL] Lena: Yes — you can scope Admins and Managers to specific teams or business units, so a regional admin sees only their region. That's configured per admin.
[EXTERNAL] Preet: Good, that'll satisfy one of the controls. Here's the one I think you might not have, and it's the one my auditor cares most about. I need a role that can see everything — all the configuration, all the access logs, all the settings — but can change absolutely nothing. A pure read-only observer.
[INTERNAL] Lena: Say more about "everything" — do you mean member data, or configuration and logs specifically?
[EXTERNAL] Preet: Configuration and logs, specifically. Not the coaching content, not the session notes — those are sensitive and the auditor doesn't want them and neither do I. I mean: who's an admin, what roles are assigned, what the SSO configuration is, what integrations are enabled, the login history, the audit trail of setting changes. All of that, viewable, with zero ability to modify.
[INTERNAL] Lena: So the mental model is an auditor account. It can inspect the entire administrative surface — settings, role assignments, integrations, logs — read-only, and it is structurally incapable of making a change, even accidentally.
[EXTERNAL] Preet: Exactly that. The "structurally incapable" part is the whole point. Right now, from what I understand, to see all of that I'd have to give the auditor a Super Admin account, which means during the audit window there's an account that could reconfigure our entire tenant. That's the opposite of what an audit is supposed to prove.
[INTERNAL] Sam: That's a sharp way to put it — the tool you use to prove least-privilege currently forces you to violate least-privilege.
[EXTERNAL] Preet: Right. It's a little ironic. My auditor actually flagged it as a finding last year — "privileged account provisioned for read-only audit purposes." I got dinged for using your product correctly.
[INTERNAL] Lena: That's exactly the kind of thing I want to capture. So to be precise about the ask: a distinct role — call it Auditor or Read-Only Admin — that has full visibility into configuration, role assignments, integration settings, security settings, and the audit/login logs, and has no write, no create, no delete capability anywhere. Correct?
[EXTERNAL] Preet: Correct. And ideally the role itself is visible in the audit log — like, "auditor account viewed the SSO config on this date" — so we can prove the auditor only looked and didn't touch. But that's a nice-to-have. The core need is the read-only-everything role.
[INTERNAL] Lena: I'm noting the view-logging as a secondary want but flagging the core role as the primary. How often would you use it — is this a once-a-year audit thing or ongoing?
[EXTERNAL] Preet: Both, honestly. Once a year for the external auditor, but our internal security team would use it continuously. I'd want to periodically review the admin roster and integration settings myself without holding a privileged account I don't need day to day.
[INTERNAL] Sam: So it's not a niche audit-week feature — it's how your own security team would prefer to operate the rest of the year.
[EXTERNAL] Preet: Yes. I don't want write access to BetterUp. I've never wanted it. I just want to see.
[INTERNAL] Lena: That framing is going straight into the request — "security team wants continuous read-only visibility, does not want and actively does not want write access." The impact is clean: today the only way to get full visibility is a privileged account, which creates an audit finding.
[EXTERNAL] Yvonne: Can I add the business-impact angle? This is starting to affect renewals — not with you, with our clients. Sterling's a financial services firm, and our own enterprise clients are pushing these controls requirements down to us and our vendors. If I can't check the "read-only auditor role" box on a vendor questionnaire, it's a mark against the tool when I renew internally.
[INTERNAL] Sam: That's important and I want it in the record — this isn't only Preet's audit, it's showing up in Sterling's own client questionnaires, which makes it a retention-adjacent request.
[EXTERNAL] Yvonne: Retention-adjacent, yes. I don't want to overstate it — we're not leaving over this — but it's a recurring friction point every audit season and it'd be genuinely valuable to solve.
[INTERNAL] Lena: Understood, and I'll represent it at that weight — a real, recurring, audit-season pain that touches Sterling's own client obligations, not a hair-on-fire. Preet, one more precision question: do you need the auditor role scoped, or does the auditor always see the whole tenant?
[EXTERNAL] Preet: Whole tenant for the external auditor. For internal use, scoping would be a bonus but not required. Start with whole-tenant read-only and we're already way ahead of where we are now.
[INTERNAL] Lena: Whole-tenant read-only as the MVP, scoping as a later refinement. That's a clean phasing.
[EXTERNAL] Preet: That's exactly how I'd build it too, for what it's worth.
[INTERNAL] Sam: I want to be straight with you on process. This is a well-formed feature request, not a bug, so I can't promise a date — it goes into the product queue and I'll advocate for it. But given that it touches security controls and shows up on questionnaires, it tends to get attention. I'll write it up with your framing and the audit-finding detail intact.
[EXTERNAL] Preet: That's all I can ask. Honestly, the fact that you didn't try to tell me Super Admin is "basically fine" is already better than most vendors.
[INTERNAL] Sam: Super Admin is not basically fine and you're correct to say so. Lena, anything else you need to specify the request?
[INTERNAL] Lena: I think I have it. Read-only auditor role, full visibility into config/roles/integrations/security settings/logs, no write anywhere, whole-tenant to start, view-logging and scoping as secondary. Preet, if you have your auditor's exact finding language from last year, drop it in an email and I'll attach it — it's persuasive to have the external framing.
[EXTERNAL] Preet: I can pull that. It's a one-liner but it's a damning one-liner.
[INTERNAL] Lena: Damning one-liners are the best supporting evidence. I'll take it.
[INTERNAL] Sam: While we've got Preet — anything else on the security side? SSO, data retention, anything the audit surfaced?
[EXTERNAL] Preet: SSO's fine, we're on our own IdP and it's behaved. No expiry weirdness, no lockouts, sessions last exactly as long as we configure them.
[INTERNAL] Sam: Good to hear — session behavior is a common one to poke at, so a clean bill there is worth noting.
[EXTERNAL] Preet: It's been solid. Data retention — I might have questions later once I read your DPA more carefully, but nothing today.
[INTERNAL] Sam: When you get there, I can get our security team on a call directly rather than playing telephone through me. Just say the word.
[EXTERNAL] Preet: Appreciate it. That might be the follow-up.
[INTERNAL] Sam: Yvonne, anything on your side before we wrap? Program, seats, anything?
[EXTERNAL] Yvonne: No, I got what I came for — Preet got a real answer and I got a story to tell the auditors that isn't "the vendor said no." That's a good call.
[INTERNAL] Sam: Then let me recap the commitments. Lena writes up the read-only auditor role request with Preet's audit-finding framing and Yvonne's questionnaire angle. Preet sends the auditor's finding language and, when ready, we set up a direct security-to-security call on data retention. I'll advocate the feature and keep you posted on where it lands in the queue — with the honest caveat that I can't give a date.
[EXTERNAL] Yvonne: That's the honest answer and I prefer it. Thank you both.
[EXTERNAL] Preet: Yeah, thanks. This was less painful than I expected.
[INTERNAL] Lena: High praise from security. I'll take it. Talk soon, both.
[INTERNAL] Sam: Thanks, everyone. I'll have the write-up circulating by end of week.
[EXTERNAL] Yvonne: Perfect. Bye.
[EXTERNAL] Preet: Bye.
