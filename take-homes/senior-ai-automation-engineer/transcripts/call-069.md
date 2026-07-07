# Call — Corvus Media × BetterUp · Program Review
Date: 2026-06-29 · Call ID: call-069
Participants: [EXTERNAL] Dr. Aisha Bello, Chief People Officer (Corvus Media) · [EXTERNAL] Nathan Wu, People Analytics Lead (Corvus Media) · [INTERNAL] Sam Oduya, CSM

[INTERNAL] Sam: Aisha, Nathan — thanks for the time. Aisha, congrats on the CPO title, I think this is our first call since you moved up.
[EXTERNAL] Aisha: Thank you, it's still got that new-office smell. Nathan's here because half of what I want to talk about is data, and he's the one who actually understands it.
[EXTERNAL] Nathan: I understand it, she decides what to do with it. Healthy division of labor.
[INTERNAL] Sam: The best kind. How's Corvus? Media's been a turbulent industry lately.
[EXTERNAL] Aisha: Turbulent is generous. We've had two rounds of restructuring in eighteen months, and the human cost of that is exactly what's on my mind for this call. Which, spoiler, is where BetterUp comes in.
[INTERNAL] Sam: Then let's get there. I set us up for a program review — usage snapshot, then whatever's driving your agenda. Given what you just said, maybe we flip it and lead with your agenda?
[EXTERNAL] Aisha: Let's flip it. The numbers are fine, Nathan can confirm, and I'd rather spend our hour on the thing I actually need.
[EXTERNAL] Nathan: Numbers are healthy — 720 of 800 seats active, completion in the low seventies, trending up since the coaching push in Q1. No concerns on utilization.
[INTERNAL] Sam: Good, then I won't belabor it. Aisha, the floor's yours.
[EXTERNAL] Aisha: Okay. Here's my situation. After two restructurings, my executive team is genuinely worried about the wellbeing of the organization — burnout, morale, the risk that our best people are quietly one bad week from leaving. And they keep asking me: "How is the org actually doing? Not vibes — do we have a read on it?"
[INTERNAL] Sam: A fair and hard question for a CPO to be asked.
[EXTERNAL] Aisha: Brutal question. And here's my problem. I know BetterUp is sitting on an incredibly rich signal about how our people are doing.
[INTERNAL] Sam: In what sense — the coaching conversations themselves?
[EXTERNAL] Aisha: Exactly. My members are having real coaching conversations about stress, confidence, burnout, career anxiety. That's the pulse of the organization.
[INTERNAL] Sam: It is. And I imagine you can't see any of it today.
[EXTERNAL] Aisha: I can't, and — critically — I don't want to see it at the level that would violate their trust. That's the tension I'm carrying.
[INTERNAL] Sam: Say more about that tension, because it's the crux.
[EXTERNAL] Aisha: The tension is this. I do not want to know what any individual is talking about with their coach. That's sacred, it's confidential.
[INTERNAL] Sam: Agreed, and I'd push back hard if you did want that.
[EXTERNAL] Aisha: Good, you should. The second my people think their coaching sessions feed a report to leadership, engagement dies overnight and deservedly so.
[INTERNAL] Sam: So the individual level is off the table entirely. What would you want instead?
[EXTERNAL] Aisha: I would give a lot for an anonymized, aggregate, org-level read. Something like: "wellbeing sentiment across the org trended down 8% this quarter, concentrated in these broad functions." Trends, not individuals. Direction, not detail.
[INTERNAL] Sam: So what you're describing is a wellbeing trend dashboard at the executive level — aggregate only, anonymized by design, that shows leadership the direction the organization is moving without ever exposing a single individual's data.
[EXTERNAL] Aisha: Exactly that. And the "by design" part is load-bearing. I don't want a report that's technically aggregate but could be reverse-engineered down to a person because a team only has three people in it. It has to be privacy-preserving in a way I can stand up in front of my workforce and defend. If I can't tell my people "leadership can see the org is stressed but literally cannot see you," it's worthless to me — worse than worthless, it's a liability.
[INTERNAL] Sam: The defensibility is the whole point — a dashboard you couldn't defend to your own workforce would do more harm than good. Nathan, from the analytics side, what would make this credible to you?
[EXTERNAL] Nathan: A few things. The first is minimum aggregation thresholds — no cell shown below, say, some floor like fifty people, so nothing's re-identifiable.
[INTERNAL] Sam: A suppression floor, so a small team can't be backed out. Makes sense. What else?
[EXTERNAL] Nathan: Trend over time rather than point-in-time snapshots, because the direction is what matters more than any single number.
[INTERNAL] Sam: Direction over snapshot. And the third?
[EXTERNAL] Nathan: The big one — ideally it's derived from something the members opt into knowing is aggregated, not scraped silently from private session content. The provenance has to be clean or I won't put my name on it.
[INTERNAL] Sam: That's an important design constraint and I want it captured precisely — minimum aggregation thresholds so nothing's re-identifiable, trend-over-time, and clean, opted-in provenance rather than silent extraction from private conversations. That last point especially — the data source has to be something members know is aggregated.
[EXTERNAL] Nathan: Right. There's a version of this that's an ethical disaster — mining private coaching transcripts for executive dashboards — and there's a version that's genuinely valuable and defensible. We only want the second one. If it can only be built the first way, we don't want it at all.
[INTERNAL] Sam: That's a crucial line and it's going straight into the write-up — the request is explicitly for the privacy-preserving version, and the customer would rather have nothing than the extractive version. That framing actually makes this a stronger and safer feature request, not a weaker one.
[EXTERNAL] Aisha: I'm glad you hear it that way. I was half-braced for you to just say "sure, we can pull sentiment from sessions!" and I'd have had to talk you down.
[INTERNAL] Sam: I would not have said that, and if a vendor does say that to you, run. To be clear about where we are today: we have manager and admin dashboards that show engagement and utilization — who's booking, completion rates, activity. What we do not have is an aggregate wellbeing-sentiment trend view at the executive altitude, built to your privacy constraints. So this is a genuine feature request, not a setting.
[EXTERNAL] Aisha: I assumed so. The engagement dashboards are great for "are people using it" but they don't answer "how are people doing." Those are different questions.
[INTERNAL] Sam: They're completely different questions and you've put your finger on exactly the gap. "Are they using it" versus "how are they doing." The second one is what your executive team is actually asking.
[EXTERNAL] Aisha: And I can't answer it right now, so I answer with anecdotes, which for a data-driven leadership team is a losing position. I'm the CPO standing up in front of the exec team with vibes while everyone else brings dashboards.
[INTERNAL] Sam: The "CPO with vibes among dashboards" image is going to help this request land internally — it's a real and common pain for people leaders, and it's exactly the kind of thing that differentiates a coaching platform from a scheduling tool. I'll write it up with your framing and Nathan's design constraints intact.
[EXTERNAL] Aisha: Please. And I'll be honest about the stakes, because you should have the full picture: my executive team is asking whether our people-development spend — which includes you — is measurably moving wellbeing. If I can't show them a credible read, the whole category, including this program, comes under scrutiny at budget time. So this isn't a nice-to-have for me. A defensible wellbeing read is close to existential for how I justify the investment.
[INTERNAL] Sam: That's important and I want it weighted correctly — this touches how Corvus justifies the entire people-development investment at budget time, which makes it retention-relevant, not just a feature wish. I'll represent it at that weight without overstating it as a threat, because I don't think you're threatening.
[EXTERNAL] Aisha: I'm not threatening. I'm describing the room I sit in. There's a difference and I appreciate you seeing it.
[INTERNAL] Sam: There's a big difference and I see it. Nathan, one more precision question — do you need this to be self-serve in a dashboard, or would a periodic delivered report satisfy the executive team initially?
[EXTERNAL] Nathan: A delivered report would satisfy the first ask honestly. A live dashboard is the dream, but a defensible quarterly aggregate report I could bring to the exec meeting would move us from vibes to data immediately. Start there, evolve to a dashboard.
[INTERNAL] Sam: That's a helpful phasing — a periodic aggregate report as the MVP, a live dashboard as the evolution. It also makes the request more tractable, which helps it get prioritized.
[EXTERNAL] Nathan: That's how I'd sequence it if I were building it. Prove the aggregation and privacy model with a report, then wrap a dashboard around it once it's trusted.
[INTERNAL] Sam: I'll write it exactly that way. I want to be straight on process — this is a feature request, so no date, and given it touches privacy and data ethics it'll get careful review, which is appropriate. I'll advocate and keep you posted on where it lands.
[EXTERNAL] Aisha: Careful review is the correct speed for this one. I'd be nervous if you told me it was easy.
[INTERNAL] Sam: It should not be easy — the easy version is the wrong version. Nathan, if you can write up your specific aggregation-threshold and provenance requirements in a short doc, I'll attach it — analytics-team-authored requirements are far more persuasive to our product team than me paraphrasing.
[EXTERNAL] Nathan: I can do that. A one-pager on aggregation floors, anonymization, and acceptable data provenance. I've basically already written it in my head.
[INTERNAL] Sam: Of course you have. How soon can you get it to me?
[EXTERNAL] Nathan: End of the week. It's mostly transcribing what's already up here.
[INTERNAL] Sam: End of week is perfect timing to attach before I file. Then get it out of your head and I'll attach it verbatim. Let me recap. One: I write up the anonymized org-level wellbeing trend request — aggregate-only, privacy-preserving by design, periodic report as MVP evolving to a dashboard, with the explicit note that Corvus wants only the defensible version, framed by the budget-justification stakes. Two: Nathan sends a one-pager on aggregation thresholds and data provenance to attach. And I advocate with no invented date. Did I capture it?
[EXTERNAL] Aisha: You captured it better than I said it. That's the whole thing.
[EXTERNAL] Nathan: One-pager coming this week. It'll be opinionated.
[INTERNAL] Sam: Opinionated is exactly what I want on this one. Thank you both — this was a genuinely important conversation and I don't take the trust dimension lightly.
[EXTERNAL] Aisha: Neither do we. That's why we're still your customer. Talk soon, Sam.
[INTERNAL] Sam: Talk soon. And Nathan — I genuinely look forward to the opinionated one-pager.
[EXTERNAL] Nathan: It'll be worth the wait. Bye.
[INTERNAL] Sam: Bye, both.
