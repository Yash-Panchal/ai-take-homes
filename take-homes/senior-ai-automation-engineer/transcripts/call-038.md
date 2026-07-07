# Call — Ironbark Mining × BetterUp · Support Debrief
Date: 2026-06-25 · Call ID: call-038
Participants: [EXTERNAL] Fiona Blackwood, IT Infrastructure Manager (Ironbark Mining) · [INTERNAL] Ravi Patel, Support Engineer · [INTERNAL] Lena Kowalski, Implementation

[INTERNAL] Lena: Fiona, thanks for joining. This is really a debrief — we resolved the issue last week, and I wanted to close the loop properly and get it on the record so nobody re-opens it in three months. Ravi did the diagnosis so he'll walk us through it.
[EXTERNAL] Fiona: Appreciated. I like a proper post-mortem. Half the vendors I deal with fix a thing and never explain what happened, and then it recurs and everyone's surprised.
[INTERNAL] Ravi: My philosophy exactly. If we don't understand why it broke, we didn't really fix it. Hi Fiona.
[EXTERNAL] Fiona: Hi Ravi. Good to put a voice to the emails.
[INTERNAL] Lena: How are things out at the sites generally, Fiona? You're what, three mines and a corporate office?
[EXTERNAL] Fiona: Three active sites and head office, yes. Two in the outback that are genuinely remote — we're talking hundreds of kilometers from anything, on satellite and microwave links. Head office is in the city on proper fiber. And that geographic split turns out to be the whole story here, as you'll see.
[INTERNAL] Lena: I had a feeling it would be. Mining IT is a special kind of hard — you're running enterprise infrastructure in places that barely have roads.
[EXTERNAL] Fiona: That's the job. I've got a server room that shares a building with a diesel generator and a lot of red dust. My counterparts at banks have no idea what real infrastructure adversity looks like.
[INTERNAL] Lena: The dust alone. I've heard mining IT horror stories that would make a data-center engineer faint.
[EXTERNAL] Fiona: I could tell you about the time a goanna got into a comms cabinet, but we'd be here all day and it's not why we're on this call.
[INTERNAL] Ravi: I desperately want to hear the goanna story but I also respect the agenda.
[EXTERNAL] Fiona: I'll save it for the Christmas card. Okay, so remind me of the official version, and then I'll confirm it matches what we saw on our side.
[INTERNAL] Ravi: Sure. So the symptom your users reported was that the live video sessions — the in-browser coaching sessions — kept dropping. The connection would establish, the session would start, and then partway through it would just die. Sometimes reconnect, sometimes not.
[EXTERNAL] Fiona: That's what came to me. "The video keeps cutting out." Which is the least useful bug report in the world, but that's what I had to start with.
[INTERNAL] Ravi: The classic. And it wasn't everyone — it was specifically your head-office users. Your remote site people, the ones at the actual mines on satellite or cellular, they were fine.
[EXTERNAL] Fiona: Right, which is completely backwards from what you'd expect. You'd think the guys on a satellite link in the outback would have the problems, not the people at corporate on a fat fiber connection.
[INTERNAL] Ravi: Exactly, and that inversion was the first real clue. When your best-connected users have the problems and your worst-connected users don't, it's almost never bandwidth. It's something the good network is doing that the bad one isn't.
[EXTERNAL] Fiona: I'll admit that's not where my head went first. My first instinct was "it's the satellite links," because it's always the satellite links. I spent a day chasing that before I realized the satellite users were the ones who were fine.
[INTERNAL] Ravi: That's a completely reasonable first guess and it's the one most people make. The remote-site link is the obvious suspect. It just happened to be innocent this time.
[EXTERNAL] Fiona: Innocent for once. I nearly apologized to the satellite provider, which would have been a first.
[INTERNAL] Lena: Don't let them get used to it.
[EXTERNAL] Fiona: God, no. They'd bill me for the compliment. Go on, Ravi. This is where it got interesting.
[INTERNAL] Ravi: So the live sessions use websockets — a persistent two-way connection that stays open for the duration of the call. That's how the real-time video and audio flow. And what we found, working with your network team, was that your corporate network runs a TLS-inspecting proxy. A security appliance that decrypts, inspects, and re-encrypts traffic on the way out.
[EXTERNAL] Fiona: The deep-packet-inspection box. Yes. We're a mining company with a lot of regulatory and security requirements, so corporate traffic goes through inspection. The remote sites don't — they route differently, straight out.
[INTERNAL] Ravi: Right, and that's why the remote sites were fine — their traffic never hit the inspection appliance. The proxy was handling normal HTTPS requests just fine, but it wasn't correctly handling the websocket upgrade and the long-lived connection. It was terminating or interfering with the persistent connection after a while, which killed the session mid-call.
[EXTERNAL] Fiona: So it wasn't your platform at all. It was our security box mangling the websocket.
[INTERNAL] Ravi: Correct. Our side was behaving exactly as designed. The websocket was being disrupted in transit by the inspecting proxy. Once your network team added an exception so that our session traffic bypasses TLS inspection — or handles the websocket properly, depending on how you configured it — the drops stopped.
[EXTERNAL] Fiona: We whitelisted your session domains from inspection. Cleaner than trying to make the appliance handle websockets gracefully, which it apparently does badly.
[INTERNAL] Ravi: That's the right call, and it's a common one. TLS-inspecting proxies and long-lived websockets are a known bad marriage. You're not the first customer to hit it and you won't be the last.
[EXTERNAL] Fiona: That's oddly comforting. Misery loves company. So — and I want to be precise here for my own records — the fix is entirely on our side, and there's nothing broken in your product that you need to change?
[INTERNAL] Ravi: That's correct, and I want to be careful not to overclaim. This was your infrastructure interacting with a standard web technology in a way that broke it. Our platform didn't have a defect. The resolution was a network configuration change on your end, which you've made, and sessions have been stable since.
[EXTERNAL] Fiona: Confirmed stable on our end too. I checked with the head-office users before this call — zero drops since we made the change last Tuesday. A week clean.
[INTERNAL] Ravi: A week clean is exactly what I'd want to see before calling it resolved. So we're aligned: root cause was the corporate TLS-inspecting proxy interfering with the websocket connection, resolved by exempting our session traffic from inspection, verified by a week of clean sessions.
[EXTERNAL] Fiona: Confirmed on all three. I'll write that up for my own change log so when someone tweaks the proxy config in six months and breaks it again, there's a record of why we made the exception.
[INTERNAL] Lena: That's the exact right instinct, Fiona. The most common way these recur is someone "cleaning up" firewall exceptions later without knowing why they existed. Document the why.
[EXTERNAL] Fiona: My whole job is stopping people from breaking things they don't understand. Present company excepted.
[INTERNAL] Ravi: Ha. I'll take the exception.
[EXTERNAL] Fiona: Okay, so nothing to file on your end, then? I don't want you logging a phantom bug against your product for something that was our proxy.
[INTERNAL] Ravi: Nothing to file as a product defect, no. I'll log the case internally as resolved-third-party for our own knowledge base, so if another mining or high-security customer hits the same websocket-versus-inspection issue, the next engineer finds the answer fast. But that's a support knowledge entry, not a bug against the platform.
[EXTERNAL] Fiona: That's the right distinction and I appreciate you making it. I've seen vendors log their customers' network problems as product bugs and then their metrics look terrible for no reason.
[INTERNAL] Ravi: We try not to blame the product for the network, or vice versa. Honest attribution keeps everyone sane.
[EXTERNAL] Fiona: I wish more vendors operated that way. I've had support orgs insist a problem was theirs when it was mine, and vice versa, both out of some misguided instinct. The truth is less flattering and more useful.
[INTERNAL] Ravi: The truth is almost always more useful, even when it's "your goanna-adjacent network did it."
[EXTERNAL] Fiona: Especially then. At least I know how to keep goannas out of cabinets now. TLS-inspection-versus-websocket is a subtler beast.
[INTERNAL] Ravi: It really is, and it's the kind of thing that only reveals itself under exactly your conditions — high-security corporate network plus real-time features. A less locked-down customer would never hit it.
[EXTERNAL] Fiona: Lucky them. Alright, I feel good about the close. What about my head-office users going forward — is there anything I should watch for, any sign it's creeping back?
[INTERNAL] Ravi: The thing to watch is any change to that proxy configuration. As long as the exemption for our session traffic stays in place, you're fine. If sessions start dropping again at head office specifically, the very first thing to check is whether someone reverted or tightened the inspection rule.
[EXTERNAL] Fiona: That's a concrete tripwire. I'll put it in the runbook — "video dropping at head office equals check the proxy exemption first."
[INTERNAL] Ravi: That one line will save your future self a day of chasing satellites again.
[EXTERNAL] Fiona: My future self thanks you both. She's very busy and appreciates the shortcut.
[INTERNAL] Lena: While we're all here and it's a rare good mood — anything else on your infrastructure side worth raising, Fiona? SSO, provisioning, anything?
[EXTERNAL] Fiona: No, genuinely. SSO's been rock solid, provisioning works, and now that the video's stable I've got nothing to complain about, which makes me nervous but I'll take it.
[INTERNAL] Lena: The eerie calm of everything working. Enjoy it.
[EXTERNAL] Fiona: I'll enjoy it suspiciously. Alright — I think we've closed this properly. Root cause understood, fix applied on our side, verified clean, documented on both ends. That's a complete loop.
[INTERNAL] Ravi: That's a textbook close. Thanks for being such a good partner on the diagnosis, Fiona — your network team gave us exactly the packet captures we needed.
[EXTERNAL] Fiona: They live for that stuff. I'll pass on the compliment; it'll make their week.
[INTERNAL] Lena: Do. And I'll send a short recap email so we all have the same written record. Nothing to action from you, Fiona — this is just for the file.
[EXTERNAL] Fiona: Perfect. That's how a support issue should end. Thanks, both.
[INTERNAL] Ravi: Thanks, Fiona. Stay safe out there.
[EXTERNAL] Fiona: Always. Cheers.
