# Call — Vesper Finance × BetterUp · Support escalation
Date: 2026-06-24 · Call ID: call-122
Participants: [EXTERNAL] Aditi Menon, Program Operations Lead (Vesper Finance) · [INTERNAL] Priya Nair, CSM · [INTERNAL] Ravi Patel, Support Engineer

[INTERNAL] Priya Nair: Aditi, hi. I pulled Ravi from support onto this one since you mentioned it touches billing and I wanted the technical brain in the room.
[EXTERNAL] Aditi Menon: Smart. Hi Ravi. This is one of those things where I need someone who understands the mechanics, not just the account.
[INTERNAL] Ravi Patel: Hi Aditi. Happy to dig in. Give me the whole picture.
[EXTERNAL] Aditi Menon: Before we get into the weeds — Priya, quick renewal question so I don't forget. We're up in October, right?
[INTERNAL] Priya Nair: October, yes. Plenty of runway, we'll start that conversation late summer.
[EXTERNAL] Aditi Menon: Good. And roughly where's our utilization sitting? My CFO will ask before renewal and I like to have the number in my pocket.
[INTERNAL] Priya Nair: You're strong — mid-eighties percent monthly active across the finance and ops teams. Traders are your highest-engagement cohort, which surprises some people.
[EXTERNAL] Aditi Menon: It doesn't surprise me. Trading is a pressure cooker. The ones who use coaching are the ones who last.
[INTERNAL] Priya Nair: That's exactly the story the data tells. Your high-stress desks are your stickiest users.
[EXTERNAL] Aditi Menon: Good. Mid-eighties is a number I can wave at finance proudly. Okay, filing that away for October.
[INTERNAL] Priya Nair: Filed. Anything else on the account side before we hand it to Ravi? Seat count stable?
[EXTERNAL] Aditi Menon: Stable. We might add a small London desk later this year but nothing to action today.
[INTERNAL] Priya Nair: Noted, we'll fold London in whenever it's real. Okay — over to the reason you actually called.
[EXTERNAL] Aditi Menon: Right. The real reason I asked for this call. It's about session credits, and it's a money thing, which is why I'm being careful.
[INTERNAL] Priya Nair: Money things get our full attention. Go ahead.
[EXTERNAL] Aditi Menon: So the way our plan works, each member has a pool of session credits per period. They book a session, one credit gets used. Standard. We reconcile that against our internal budget allocations because finance tracks it by department.
[INTERNAL] Ravi Patel: Right, credit per booked session. That's the model.
[EXTERNAL] Aditi Menon: Here's the problem. We noticed our credit consumption was running higher than our session count. Like, meaningfully higher. Finance flagged it because the numbers didn't reconcile, and finance flagging you is never a fun day.
[INTERNAL] Ravi Patel: Higher credit consumption than actual sessions held. Okay. How big a gap?
[EXTERNAL] Aditi Menon: Enough that our operations analyst spent a week trying to figure out if we were miscounting. We weren't. Let me tell you what she found, because she's sharp and she nailed it down.
[INTERNAL] Ravi Patel: Please, this is exactly the detail I need.
[EXTERNAL] Aditi Menon: She isolated it to rescheduling. Specifically, when a member reschedules a session on short notice. She built a little tracking sheet and matched every anomaly to a reschedule.
[INTERNAL] Ravi Patel: Rescheduling. Okay. Walk me through the exact sequence, if she documented it.
[EXTERNAL] Aditi Menon: She did, meticulously. Member books a session. One credit gets held or deducted, fine. Then the member reschedules that session — moves it to a different time. And when they reschedule within a short window before the original slot, a SECOND credit gets deducted. So one session, two credits gone.
[INTERNAL] Ravi Patel: Let me make sure I've got the timing precisely. It's specifically when the reschedule happens close to the original appointment time?
[EXTERNAL] Aditi Menon: Yes. She pinned it to reschedules made within twenty-four hours of the original slot. If someone reschedules a week out, one credit, correct. If they reschedule the morning of, or the night before — inside that twenty-four-hour window — two credits get burned for the one session.
[INTERNAL] Ravi Patel: Double-decrement on a within-24-hour reschedule. So the system's probably treating the late reschedule like a late-cancellation-plus-rebook — charging for the abandoned slot and then charging again for the new booking.
[EXTERNAL] Aditi Menon: That's exactly her theory. It's as if it thinks you cancelled late and booked fresh, when really you just moved the same session.
[INTERNAL] Ravi Patel: That's a coherent explanation for the mechanism. And it's clearly wrong behavior — a reschedule is one session, it should cost one credit regardless of when you move it. A late-reschedule penalty policy might be intentional, but silently eating a second credit with no disclosure isn't a policy, it's a bug.
[EXTERNAL] Aditi Menon: Thank you. That's the distinction I needed someone to confirm. Because at first I wondered if it was an intentional late-reschedule fee. But there's nothing in our contract about that, no notice to the member, nothing in the UI. The credit just quietly vanishes.
[INTERNAL] Priya Nair: There's definitely no late-reschedule fee in your agreement, I can confirm that from the account side. This isn't a contracted policy being enforced.
[EXTERNAL] Aditi Menon: Right. So it's just... eating credits. And because it's tied to short-notice reschedules, which happen constantly in our world — traders' calendars are chaos — it adds up fast.
[INTERNAL] Ravi Patel: That's the impact I'll want to capture. High reschedule rate in your population, each within-24-hour reschedule double-charges, and it's directly billing-visible because you reconcile credits to budget. Do you have a rough number on how many credits you think were lost?
[EXTERNAL] Aditi Menon: Over the last two months, my analyst estimates somewhere between sixty and eighty credits lost to this. That's real money at our per-credit rate, and it's real reconciliation pain for finance every month.
[INTERNAL] Ravi Patel: Sixty to eighty credits, billing-visible, tied to a specific reproducible trigger. That's a strong, well-documented report. Can your analyst share the tracking sheet? Matched examples of the double-decrement would let engineering reproduce it instantly.
[EXTERNAL] Aditi Menon: Absolutely, she'll be thrilled someone wants her spreadsheet. She's been dying to be vindicated.
[INTERNAL] Ravi Patel: Tell her she's vindicated. This is a clean bug report. Let me restate it so we're aligned: rescheduling a session within twenty-four hours of the original slot deducts a second credit for what is a single session, with no disclosure to the member and no basis in the contract. It's billing-visible and it's cost Vesper an estimated sixty to eighty credits over two months.
[EXTERNAL] Aditi Menon: That's it exactly. You've got it.
[INTERNAL] Ravi Patel: I'm filing this today as a billing-impacting bug. Given it touches credits and money, I'll flag it accordingly so it doesn't sit.
[EXTERNAL] Aditi Menon: What about the credits we've already lost? Can those be recovered?
[INTERNAL] Priya Nair: Let me take that one. Once Ravi's got the bug confirmed and your analyst's data quantifies the loss, I'll work the credit remediation on the account side. I'm not going to promise a number on this call, but if the platform double-charged you, we make it right. That's not a maybe.
[EXTERNAL] Aditi Menon: That's what I hoped to hear. I wasn't looking to fight over it, I just want it fixed and squared.
[INTERNAL] Priya Nair: Understood, and you shouldn't have to fight. Fix from Ravi's side, remediation from mine, once we have the confirmed numbers.
[EXTERNAL] Aditi Menon: One question on the remediation — would that come back as credits added to our pool, or as a billing adjustment? Finance will want to know which bucket it lands in.
[INTERNAL] Priya Nair: Most likely credits restored to your pool, which is cleaner for everyone, but I'll confirm the exact mechanism with our billing team before I commit to it in writing.
[EXTERNAL] Aditi Menon: Credits back to the pool would be ideal, that reconciles neatly for us. But confirming first is the right move.
[INTERNAL] Priya Nair: I'll get you the definitive answer in writing so finance has something to file against. Perfect.
[EXTERNAL] Aditi Menon: Honestly this is the outcome I wanted — believed, fixed, and made whole.
[INTERNAL] Ravi Patel: You made it easy by bringing the diagnosis pre-baked. Have your analyst send me the sheet and I'll attach it to the ticket directly.
[EXTERNAL] Aditi Menon: She'll have it to you within the hour, she's been waiting for this moment her whole career.
[INTERNAL] Ravi Patel: One clarifying question for her sheet, so I ask precisely — when the second credit gets deducted, does it happen at the moment of the reschedule, or when the new session actually completes? That timing tells engineering where in the flow the double-count lives.
[EXTERNAL] Aditi Menon: She noticed it hits at the moment of reschedule, before the new session ever happens. So it's the act of rescheduling that triggers it, not attendance.
[INTERNAL] Ravi Patel: That's a crucial detail — it fires on the reschedule action itself, not on completion. That points straight at the reschedule handler double-counting. I'll put that front and center.
[EXTERNAL] Aditi Menon: She'll be delighted you asked. That was the exact thing she spent a day nailing down.
[INTERNAL] Ravi Patel: Then she saved engineering that day. I'll give her the recognition in the ticket, she earned it.
[INTERNAL] Priya Nair: And I'll circle the remediation timeline back to you once Ravi confirms, Aditi. Should be quick.
[EXTERNAL] Aditi Menon: Wonderful. Thank you both. This is why I don't dread these calls.
[INTERNAL] Priya Nair: We aim to be un-dreadable. Talk soon, Aditi.
[EXTERNAL] Aditi Menon: Bye, and thanks again.
[INTERNAL] Ravi Patel: Take care, Aditi. Watch your inbox for the ticket number.
