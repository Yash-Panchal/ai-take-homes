# Call — Maple Crest Bank × BetterUp · Support escalation
Date: 2026-06-19 · Call ID: call-075
Participants: [EXTERNAL] Corinne Boudreau, IT Security Manager (Maple Crest Bank) · [EXTERNAL] Devon Marsh, Help Desk Lead (Maple Crest Bank) · [INTERNAL] Ravi Patel, Support Engineer

[INTERNAL] Ravi Patel: Hi Corinne, hi Devon. Thanks for making time. Before we dig in — how long have you two been live on the platform? I want to know if this is a new rollout or something that changed.
[EXTERNAL] Corinne Boudreau: We've been live about eight months. The core coaching's been fine that whole time. This is new, tied to a security change we made recently.
[INTERNAL] Ravi Patel: That framing already helps — it narrows it to whatever changed. Devon, you're on the help desk side?
[EXTERNAL] Devon Marsh: Right, I run the internal help desk. I'm the one fielding the tickets from staff, so I've got the frontline view.
[INTERNAL] Ravi Patel: Perfect, that's exactly the perspective I need. I've got the ticket you opened in front of me but I'd rather hear it in your own words first. Support notes lose a lot.
[EXTERNAL] Corinne Boudreau: Appreciate that. So — context, we're a Canadian bank, all our staff are on Canadian mobile numbers. That matters, you'll see.
[INTERNAL] Ravi Patel: Noted. Go ahead.
[EXTERNAL] Corinne Boudreau: We turned on two-factor for the BetterUp login a few weeks back. Security requirement, non-negotiable on our side, all vendor apps need MFA.
[INTERNAL] Ravi Patel: Makes sense for a bank. You went with SMS codes for the second factor?
[EXTERNAL] Corinne Boudreau: SMS, yes. And that's where the problem is. Devon, you want to describe what the help desk is seeing?
[EXTERNAL] Devon Marsh: Sure. So we've been getting a steady trickle of tickets — people saying the text code doesn't work. They type it in and it's rejected as expired.
[INTERNAL] Ravi Patel: Expired. Okay. When they request a fresh code, does that one work?
[EXTERNAL] Devon Marsh: Sometimes. Sometimes they request three or four before one lands in time. It's inconsistent, which is the maddening part.
[INTERNAL] Ravi Patel: Let me pull on the timing. When someone requests a code, how long until the text actually arrives on the phone?
[EXTERNAL] Devon Marsh: That's the crux. It's slow. We timed it. From clicking "send code" to the SMS showing up on the phone, we're seeing five, six, sometimes seven minutes.
[INTERNAL] Ravi Patel: Five to seven minutes for the SMS to arrive.
[EXTERNAL] Devon Marsh: On the Canadian numbers, yes. And the code says it's only valid for five minutes. So by the time the text arrives, the window's already closed. The code's dead on arrival.
[INTERNAL] Ravi Patel: So the code expires before the SMS carrying it even reaches the handset. That's the failure.
[EXTERNAL] Devon Marsh: Exactly. It's not that people are typing slow. The text physically arrives after the code has already expired.
[EXTERNAL] Corinne Boudreau: We had one of our VPs stuck out of the app for twenty minutes cycling codes. That's when it got escalated to me.
[INTERNAL] Ravi Patel: I understand. Let me ask the key question — you said Canadian numbers specifically. Have you been able to compare against any non-Canadian numbers?
[EXTERNAL] Corinne Boudreau: We have, actually, because I anticipated you'd ask. We have two contractors on US mobile numbers. Their codes arrive in under thirty seconds. Every time.
[INTERNAL] Ravi Patel: That's an extremely useful data point. So on US numbers, sub-thirty-second delivery, codes work fine. On Canadian numbers, five-to-seven-minute delivery, codes expire before arrival.
[EXTERNAL] Corinne Boudreau: That's the pattern precisely. Same app, same flow, same five-minute expiry. The only variable is the phone number's country.
[EXTERNAL] Devon Marsh: I ran a little log. Twenty-two Canadian-number tickets in the last two weeks. Zero from the two US contractors. The split is total.
[INTERNAL] Ravi Patel: Twenty-two to zero. That's not noise, that's a clean signal. This points at the SMS delivery path to Canadian carriers being slow, and the five-minute expiry window not accommodating that latency.
[EXTERNAL] Corinne Boudreau: That's our read too. Either the codes need to live longer, or the delivery to Canada needs to be faster, but the combination as-is is unusable for us.
[INTERNAL] Ravi Patel: I want to be careful not to hand-wave. Let me confirm the specifics I'll write up: two-factor via SMS, code valid five minutes, Canadian mobile numbers see five-to-seven-minute SMS delivery so codes expire before arrival, US numbers deliver in under thirty seconds and work fine. Twenty-two Canadian tickets, zero US, over two weeks.
[EXTERNAL] Corinne Boudreau: That's an accurate summary. You can quote all of it.
[INTERNAL] Ravi Patel: This is a genuine defect on our side as far as I can see — the expiry window doesn't account for Canadian SMS latency, which effectively locks out an entire country's phone numbers. I'm filing this with your data attached.
[EXTERNAL] Corinne Boudreau: Thank you. What do we do in the meantime? Half our staff can't reliably log in.
[INTERNAL] Ravi Patel: Practical interim options. First — do you have the ability to use an authenticator app instead of SMS as the second factor? That sidesteps carrier delivery entirely.
[EXTERNAL] Corinne Boudreau: We can. We use authenticator apps for our own systems. I didn't realize it was an option on your side.
[INTERNAL] Ravi Patel: It is. In Admin, Security, MFA settings you can allow authenticator-app TOTP. I'd switch your Canadian staff to that as a workaround while engineering fixes the SMS timing. TOTP codes are generated on-device, no carrier latency.
[EXTERNAL] Devon Marsh: That would kill the ticket queue overnight. Can we mandate it for the Canadian numbers specifically?
[INTERNAL] Ravi Patel: You can allow both and steer Canadian users to the app. I'll send you the exact settings path and a short user-facing setup guide after this call.
[EXTERNAL] Corinne Boudreau: That's a good stopgap. But I don't want the SMS issue dropped just because we've worked around it.
[INTERNAL] Ravi Patel: It won't be. The workaround is for you; the bug filing is for the product. Those are separate and I'm doing both. I'll give you the ticket number so you can track it.
[EXTERNAL] Corinne Boudreau: Perfect. We're a regulated bank, so I'll need to reference that ticket in our own vendor risk log.
[INTERNAL] Ravi Patel: Understood, I'll make sure you have the reference. Devon, roughly how many Canadian numbers total, so I can convey scope?
[EXTERNAL] Devon Marsh: About four hundred and thirty staff on Canadian mobiles. Basically everyone. The two US contractors are the exception.
[INTERNAL] Ravi Patel: Four hundred thirty affected users. That's real scope, it'll help prioritize. Thank you.
[EXTERNAL] Devon Marsh: One more data point in case it matters — it's not tied to any one carrier on our end. We've got staff on Rogers, Bell, Telus, all three see it.
[INTERNAL] Ravi Patel: That's actually significant — it rules out a single-carrier issue and points at the delivery path to Canada broadly, not one provider. I'll include that.
[EXTERNAL] Devon Marsh: Figured it'd help you not chase a dead end. I checked because my first thought was "must be one flaky carrier." Nope, all of them.
[INTERNAL] Ravi Patel: You saved engineering a wasted investigation. That's genuinely useful diagnostic work.
[EXTERNAL] Corinne Boudreau: We appreciate you actually digging in rather than telling us to reboot our phones.
[INTERNAL] Ravi Patel: You did the diagnostic work for me with the US comparison. That's the cleanest bug report I've taken this month, genuinely.
[EXTERNAL] Devon Marsh: I'll take that as a compliment. I'll email you the raw ticket timestamps too if it helps engineering.
[INTERNAL] Ravi Patel: Please do, delivery timestamps are exactly what they'll want. Send them to the ticket thread.
[EXTERNAL] Corinne Boudreau: Will do. So — action items: you file the SMS-expiry bug with our data and give us the number, you send the authenticator-app workaround guide, Devon sends timestamps. Right?
[INTERNAL] Ravi Patel: That's the full list. I'll have the workaround guide to you within the hour so you can start unblocking people today.
[EXTERNAL] Corinne Boudreau: Today would be a relief. Thank you Ravi.
[INTERNAL] Ravi Patel: Of course. One last practical question — for the authenticator rollout, do your staff already have an authenticator app on their phones, or will they be installing fresh?
[EXTERNAL] Corinne Boudreau: Most have one already for our banking systems. So it's just adding our account to an app they know, not a new install. That's easy.
[INTERNAL] Ravi Patel: That makes the rollout much smoother — no "how do I install this" tickets, just "scan this QR code." I'll write the guide assuming they know the app.
[EXTERNAL] Devon Marsh: Perfect. That'll cut my ticket volume even faster. Familiar app, new entry, done.
[INTERNAL] Ravi Patel: Exactly. I'll get that to you within the hour. I'll be in the ticket thread the rest of the day if anything comes up. Talk soon.
[EXTERNAL] Devon Marsh: Thanks. Bye.
[EXTERNAL] Corinne Boudreau: Bye.
