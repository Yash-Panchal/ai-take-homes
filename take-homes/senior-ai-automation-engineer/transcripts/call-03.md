# Call — Atlas Financial × BetterUp · Onboarding
Date: 2026-06-17 · Call ID: call-03
Participants: [EXTERNAL] Renee Park, IT Security Lead (Atlas Financial) · [INTERNAL] Tomás Vela, Implementation

[EXTERNAL] Renee: The one real blocker for our security review is role provisioning. SSO works fine, but every user lands as a basic member and an admin has to promote them by hand. We need the user's role assigned automatically from their SAML group membership at login — IdP group maps to BetterUp role.
[INTERNAL] Tomás: So group-to-role mapping driven off the SAML assertion, applied on each login.
[EXTERNAL] Renee: Right. Without it we can't pass our access-review audit, and we can't go to full rollout. It's the thing standing between us and turning everyone on.
[INTERNAL] Tomás: That's clear. I'll write it up with your audit context attached.
