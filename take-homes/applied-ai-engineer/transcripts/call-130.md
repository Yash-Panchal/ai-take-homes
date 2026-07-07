# Call — Ryecroft Analytics × BetterUp · Technical Sync
Date: 2026-06-26 · Call ID: call-130
Participants: [EXTERNAL] Nadia Osei, Staff Engineer, Platform (Ryecroft Analytics) · [EXTERNAL] Tim Brubaker, People Systems Lead (Ryecroft Analytics) · [INTERNAL] Ravi Patel, Support Engineer

[INTERNAL] Ravi: Hey Nadia, Tim — thanks for hopping on. Tim, you set this up, so what's the shape of it?
[EXTERNAL] Tim: Yeah, so this is mostly a Nadia show. Her team owns the integration between BetterUp and our internal people-data warehouse, and she's got a couple of engineering-level questions I can't answer. I'm here to nod and take notes.
[INTERNAL] Ravi: Perfect, I like talking to the people who actually own the pipes. Nadia, before we start — how long have you been running the integration? I want to calibrate how deep I can go.
[EXTERNAL] Nadia: Go as deep as you want. I built the original integration about eighteen months ago and I've maintained it since. I know your webhook payloads better than I know some of my coworkers' names.
[INTERNAL] Ravi: Ha, that's the level I hoped for. Then I won't explain what a webhook is, which is my favorite kind of call.
[EXTERNAL] Nadia: Please don't. If you say "so a webhook is like a phone call for computers" I'm hanging up.
[INTERNAL] Ravi: I would never insult you like that. Tim, apologies, that one's an inside joke — we get a lot of "explain it like I'm five" requests and it's nice when we don't have to.
[EXTERNAL] Tim: No offense taken. I'm the "explain it like I'm five" guy in most of my meetings. I've made peace with it.
[INTERNAL] Ravi: Nothing wrong with being the translator. Okay — Nadia, over to you.
[EXTERNAL] Nadia: Cool. So for context — we consume your webhooks. When a session completes, when a member gets enrolled, when engagement milestones hit, we take those events and land them in our warehouse so our people-analytics team can join them against other HR data.
[INTERNAL] Ravi: Right, you're one of our heavier webhook consumers. What's on your mind?
[EXTERNAL] Nadia: Two things. One's a config question, one's more of a reliability thing I want to flag. Config first because it's quick. We want to add a second endpoint — a staging one — so we can test schema changes without pointing at prod. Is that supported?
[INTERNAL] Ravi: It is. You can register multiple webhook endpoints and scope which event types go to each. I'll send you the setup doc and we can add your staging URL. Do you want all event types mirrored to staging, or a subset?
[EXTERNAL] Nadia: Subset. Just session and enrollment events. We don't need the whole firehose in staging.
[INTERNAL] Ravi: Easy. Do you want the staging endpoint to use the same secret for signature verification, or a separate one? Some teams like a separate secret so a staging leak can't affect prod.
[EXTERNAL] Nadia: Separate secret, definitely. I don't want staging and prod sharing anything. If someone fat-fingers the staging config I want the blast radius contained.
[INTERNAL] Ravi: Good instinct — separate secret it is. And do you verify signatures on your side today? Just checking your setup is sound while we're here.
[EXTERNAL] Nadia: We do. Every inbound webhook gets its signature verified before we process it. If it doesn't verify, we drop it and log it. I'm paranoid about accepting spoofed events into the warehouse.
[INTERNAL] Ravi: That's exactly right, and honestly better than a lot of consumers do. I have no notes on your security posture. I'll get you the multi-endpoint doc with the separate-secret setup and we can configure it this week.
[EXTERNAL] Nadia: Perfect. That's the easy one done. Okay — the reliability thing, which is the one I actually care about.
[INTERNAL] Ravi: I'm all ears. Lay it out.
[EXTERNAL] Nadia: We've been noticing that we sometimes get the same event more than once. Like, the exact same session-completed event will land in our queue twice, occasionally three times. Same session ID, same payload, just delivered multiple times.
[INTERNAL] Ravi: The same event delivered more than once. How often are you seeing it?
[EXTERNAL] Nadia: It's not constant, which is what makes it annoying. Most events come through exactly once. But maybe — I'd estimate a few out of every thousand? — show up as duplicates. Enough that it's not noise, but not so much that it's every event.
[INTERNAL] Ravi: And when you get the duplicate, is the payload identical, or is anything different — a different timestamp, a different delivery ID, anything?
[EXTERNAL] Nadia: That's a good question and I actually checked. The event payload is identical. Same session ID, same completion timestamp, same everything in the body. The delivery envelope has a different delivery timestamp because it arrives a few seconds or minutes later, but the actual event content is byte-for-byte the same. It's clearly the same underlying event being sent again, not a new event.
[INTERNAL] Ravi: Understood. And what's the impact on your side when a duplicate lands?
[EXTERNAL] Nadia: Right now we've built our own dedup layer to catch it, so it's not breaking anything today. But it's fragile. We're keying off the session ID plus event type and dropping anything we've already seen. The problem is that's our hack, and it means every consumer of your webhooks has to independently reinvent this. And if two duplicates race through our pipeline at the same time before the first one commits, our dedup can miss it and we double-count a session. Which for an analytics company is genuinely bad — we're literally in the business of accurate counts.
[INTERNAL] Ravi: That's a real concern, and I hear you on the fragility. What would the ideal behavior look like from your side?
[EXTERNAL] Nadia: Honestly, the clean fix is an idempotency key. If every webhook delivery carried a stable, unique identifier for the event itself — not the delivery, the event — then we could dedup reliably on that key instead of guessing based on payload contents. Send the same event twice, same idempotency key, we drop the second one with confidence. That's the industry-standard pattern and it would let us throw away our hacky dedup layer.
[INTERNAL] Ravi: A stable idempotency key on the event so you can safely dedup on it. That's a clear ask, and it's a good one — payload-based dedup is exactly as brittle as you're describing.
[EXTERNAL] Nadia: Right? I'd much rather trust a key you guarantee than fingerprint the body myself and hope you never change the schema.
[INTERNAL] Ravi: That's the crux of it — if we ever tweaked a payload field, your fingerprinting breaks silently. A dedicated key insulates you from that.
[EXTERNAL] Nadia: Exactly. So that's the flag. I don't need it fixed tomorrow, but I want it on your radar as the direction, because we're going to keep leaning on webhooks and this only gets more important as our volume grows.
[INTERNAL] Ravi: This is helpful, and I want to be straight with you — the duplicate-delivery behavior and the idempotency-key ask both sound familiar. I don't want to overstate it, but I believe this may already be tracked on our side. Let me confirm rather than assume, and either way your account and your specifics get attached, because the impact detail you gave — the analytics double-count risk — is exactly the kind of context that helps.
[EXTERNAL] Nadia: That's fine by me. If it's already tracked, great, add our voice to it. I'd just want to be looped in if there's a solution so we can adopt the key when it exists.
[INTERNAL] Ravi: Absolutely. When there's a supported idempotency mechanism, you'd be one of the first I'd tell, given you're already building around the gap.
[EXTERNAL] Nadia: Perfect. And in the meantime, is there anything I should know about the current delivery behavior — like, is a duplicate ever a signal that the first one failed, or is it purely spurious?
[INTERNAL] Ravi: Good instinct to ask. In the pattern you're describing — identical payload, no failure on your first receipt — it's a spurious re-delivery, not a retry of a failed one. So you're right to just dedup and move on; you're not missing a real second event.
[EXTERNAL] Nadia: Good, that's what I assumed but I wanted to hear it from you. I was slightly worried we were dropping legitimate re-sends.
[INTERNAL] Ravi: You're not. If your first receipt succeeded and the second is identical, dropping the second is correct.
[EXTERNAL] Tim: Can I ask a dumb question from the cheap seats?
[INTERNAL] Ravi: There are no dumb questions, Tim, only dumb webhooks.
[EXTERNAL] Tim: Ha. So does this mean our analytics numbers have been wrong this whole time?
[EXTERNAL] Nadia: No, Tim, our dedup has been catching almost all of them. I flagged the risk, not an actual known miscount. If we'd been double-counting sessions, the numbers would look insane and someone would've screamed by now.
[EXTERNAL] Tim: Okay, good. I don't want to explain wrong numbers to the CFO.
[INTERNAL] Ravi: Nadia's dedup is doing its job. The ask is to make that job unnecessary and bulletproof, which is the right long-term move.
[EXTERNAL] Nadia: Exactly. It works today, I just don't want it to be load-bearing forever.
[INTERNAL] Ravi: Understood, and well put. Let me read back what I'm capturing: you're seeing occasional duplicate webhook deliveries — same event, identical payload, delivered two or three times, a few per thousand — and you want a stable idempotency key so you can dedup reliably instead of fingerprinting payloads. Current impact is manageable via your own dedup layer but fragile, with a double-count risk under race conditions. That right?
[EXTERNAL] Nadia: That's a clean summary. Nailed it.
[INTERNAL] Ravi: Great. I'll confirm whether this matches something we're already tracking and attach your account and the analytics-accuracy context either way. And I'll get you the multi-endpoint setup doc for your staging URL.
[EXTERNAL] Nadia: Perfect. The staging endpoint's the quick win; the idempotency key is the one I'll be nagging you about at every sync.
[INTERNAL] Ravi: Nag away, that's how good things get prioritized. Anything else on your side?
[EXTERNAL] Nadia: That's my list. Tim?
[EXTERNAL] Tim: Nothing from me. I understood maybe sixty percent of that and I'm at peace with it.
[INTERNAL] Ravi: Sixty percent is a strong showing for a webhook conversation. I'll follow up with the doc and the tracking confirmation. Thanks both.
[EXTERNAL] Nadia: Thanks, Ravi. Talk soon.
[EXTERNAL] Tim: Cheers. Oh — one non-webhook thing, Ravi, quick. Do the standard engagement reports come as CSV or just the dashboard? My analytics people asked.
[INTERNAL] Ravi: The admin reports can export to CSV — it's in the reports view, there's an export option. I'll point your team to it.
[EXTERNAL] Tim: Great, that'll make them happy. That's genuinely all. Thanks both.
[INTERNAL] Ravi: Anytime. Talk soon.
