# Call — Southgate Retail × BetterBark · Admin Sync
Date: 2026-06-16 · Call ID: call-044
Participants: [EXTERNAL] Derek Whitlow, HRIS Administrator (Southgate Retail) · [INTERNAL] Sam Oduya, CSM

[INTERNAL] Sam: Derek, thanks for making time. I know end of quarter's a mess for you.
[EXTERNAL] Derek: It's always a mess. Retail runs on seasonal churn and I'm the guy holding the churn hose. What are we covering?
[INTERNAL] Sam: I had three: your Q3 seat forecast, the manager-dashboard rollout you asked about, and then whatever's on your list. That work?
[EXTERNAL] Derek: Works. Can we do forecast last? It's the least interesting and I know the number in my head anyway.
[INTERNAL] Sam: Sure. Before we start — did the calendar move I sent go through okay? I bumped us thirty minutes because I had a conflict.
[EXTERNAL] Derek: It went through. My calendar's a warzone so one more shuffle didn't register. I'm just glad it wasn't at eight, I'm useless before coffee.
[INTERNAL] Sam: Noted, no eight a.m. syncs. Let's do the manager dashboard first, then — you asked about the rollout last month.
[EXTERNAL] Derek: Right. That's actually going well. We turned it on for the district managers and they like the team engagement view. A couple asked for a PDF export but I told them to just screenshot it for now.
[INTERNAL] Sam: PDF export of the team summary is a request we're hearing, I'll note it, but no promise on timing. Screenshot's the workaround for the moment.
[EXTERNAL] Derek: That's what I figured. It's not blocking anyone, just a nice-to-have. My district managers screenshot everything anyway, they live in slide decks.
[INTERNAL] Sam: Fair enough. How's adoption of the dashboard itself — are they actually opening it, or did they nod and forget?
[EXTERNAL] Derek: Better than I expected. Maybe two-thirds check it before their team meetings. The other third I'll never reach, they're old-school, they manage by walking around.
[INTERNAL] Sam: Two-thirds is a genuinely good number for a first rollout. I wouldn't chase the walk-around third too hard.
[EXTERNAL] Derek: I'm not going to. Some of them are my best managers, they just don't need a dashboard to know their team's mood. Okay, that's the dashboard. It's fine.
[INTERNAL] Sam: Then what's on your list?
[EXTERNAL] Derek: The big one is offboarding. You know our headcount balloons for holiday and then we shed a couple thousand seasonal workers in January. When we offboard, I need to deactivate people in bulk, and I've hit a wall with it.
[INTERNAL] Sam: Tell me about the wall.
[EXTERNAL] Derek: So the way I do it, I pull the list of terms from Workday, filter to the ones who had a BetterBark seat, and I've got a CSV of member IDs. Then in the admin panel I select them and hit deactivate. Small batches, fine. Fifty, a hundred, no problem.
[INTERNAL] Sam: And the big batches?
[EXTERNAL] Derek: The big batches are where it falls apart. Anything over about two hundred at once and the thing just spins. The progress spinner sits there, and then eventually the page either times out or throws a generic error and dumps me back to the member list.
[INTERNAL] Sam: Okay. And when it fails like that — what state are the accounts in?
[EXTERNAL] Derek: That's the part that made me actually put it on the agenda. It's not all-or-nothing. Some of them get deactivated and some don't. So I'm left with a partial. And here's the kicker — it doesn't tell me which ones went through and which didn't. No report, no confirmation list, nothing. Just the error and a shrug.
[INTERNAL] Sam: So you can't tell from the failure what actually happened.
[EXTERNAL] Derek: Right. I have to go back and manually re-check every single member ID against the roster to see who's still active. On a batch of five hundred that's my whole afternoon gone, and I'm doing it because the tool half-finished the job and then lied to me about it.
[INTERNAL] Sam: That's a real problem. Let me make sure I've got the shape of it — bulk deactivate over roughly two hundred members times out, leaves some deactivated and some not, and there's no report telling you which is which, so you're stuck reconciling by hand.
[EXTERNAL] Derek: You've got it exactly. And the timing is what worries me. Right now it's June, I'm doing maintenance offboarding, forty here, sixty there. In January I'm going to need to deactivate somewhere north of two thousand people in a compressed window. If it can't handle two hundred cleanly, January is going to be a catastrophe.
[INTERNAL] Sam: The January volume is the part that makes this urgent rather than annoying. I want to get this written up with that context — the partial state and the missing report are both bad on their own, but the seasonal spike is what makes it a real risk for you.
[EXTERNAL] Derek: Please do. My workaround right now is chunking it into batches of a hundred and fifty and babysitting each one, which works but it's absurd. I'm a systems administrator manually clicking through pages like it's 2009.
[INTERNAL] Sam: You shouldn't have to do that. Have you had any of them silently fail even in the small batches, or is a hundred and fifty reliably clean?
[EXTERNAL] Derek: A hundred and fifty's been clean so far. I've done maybe a dozen of those since spring and I haven't caught a partial in that range. It's specifically when I get greedy and try to do the whole list.
[INTERNAL] Sam: That's a useful data point. Suggests it's a timeout on the operation rather than random flakiness. I'll pass that along. Roughly how long does it spin before it dies — a few seconds, a minute?
[EXTERNAL] Derek: On the big ones, maybe thirty, forty seconds of spinner and then it dies. It's not instant, which is what made me think it's genuinely trying and giving up, not rejecting it up front. It gets partway, times out, and bails with whatever it's half-done.
[INTERNAL] Sam: Thirty to forty seconds before it times out and bails partway — that's consistent with hitting an operation timeout mid-batch, which is exactly why you end up with the partial state. Good detail, that helps engineering enormously.
[EXTERNAL] Derek: Whatever it is, I need it fixed or I need a supported way to do a big batch before January. Even if the answer is "here's an import-style job that runs in the background and emails you a result file," I'd take that in a heartbeat.
[INTERNAL] Sam: Noted, and honestly that background-job-with-a-result-file shape is exactly the kind of thing that would solve the underlying pain. I'll write up both the defect and your target outcome so product sees the whole picture.
[EXTERNAL] Derek: Good. I don't need it tomorrow. I need it before the holiday hiring wave, which means realistically I need to know by October whether it's coming, so I can plan around it if it's not.
[INTERNAL] Sam: That's fair and I'll flag the October decision point. One clarifying thing — when it errors and dumps you back, does it give you any error code or reference number at all, or is it truly just a generic message?
[EXTERNAL] Derek: Truly generic. "Something went wrong, please try again." No code, no ID, nothing I could give you to trace it. If there were even an error reference I could hand you I'd feel better.
[INTERNAL] Sam: I'll note the absence of any error reference too — that's part of the problem, it makes it undiagnosable from your side. Let me get this in front of the right people and I'll come back to you with where it stands.
[EXTERNAL] Derek: Appreciate it. Okay — seat forecast, since I promised. Q3 I'm holding roughly flat, maybe a hundred more seats as we onboard the summer supervisors. The real jump is Q4 for holiday, and I'll have firm numbers for you by August.
[INTERNAL] Sam: Flat Q3, spike Q4, numbers in August. Do you provision the holiday seats all at once or stagger them?
[EXTERNAL] Derek: All at once, usually first week of November. Which, now that I say it out loud, is the same bulk-operation problem in the other direction. If activation has the same ceiling I'm in trouble twice.
[INTERNAL] Sam: Good catch. I don't have reports of bulk activation choking the same way, but let's not assume — I'll ask specifically and confirm before November so you're not surprised.
[EXTERNAL] Derek: Yeah, please. I'd rather find out in a quiet meeting than at 6am on a provisioning morning.
[INTERNAL] Sam: We all would. How do you handle the activation side today — same CSV-and-select flow?
[EXTERNAL] Derek: Same flow, opposite button. I select the new hires and hit activate. I've never pushed it past a couple hundred at once because I stagger onboarding over the first week anyway, so I honestly don't know if it has the same wall.
[INTERNAL] Sam: That staggering might be why you've never hit it. I'll get you a straight answer on the activation ceiling so you can decide whether to keep staggering or do it in one shot.
[EXTERNAL] Derek: Either's fine as long as I know the limit going in. Surprises are the enemy.
[INTERNAL] Sam: Surprises are the enemy. While we're on holiday planning — do the seasonal folks get the same training access as permanent staff, or a lighter version? Just so I understand what we're activating and deactivating.
[EXTERNAL] Derek: Same access, actually. Corporate decided a couple years back that if we're going to have someone for four months, we treat them like they matter for four months. Retention play. So they get the full program, which means the full activate-and-deactivate cycle, which is exactly why the bulk operations matter so much to me.
[INTERNAL] Sam: That's a good policy, and it does mean your bulk-operation reliability is directly tied to how well you can honor it. If deactivate is flaky, you either leave ex-seasonals with lingering access or you spend your January reconciling by hand.
[EXTERNAL] Derek: Both of which are bad. Lingering access is a security-review finding waiting to happen, and hand-reconciliation is my sanity gone. So yeah, the fix isn't a nice-to-have for me, it's the thing that makes the whole seasonal model workable.
[INTERNAL] Sam: I'll make sure that framing is in the write-up too — this isn't a convenience feature, it's what makes your treat-seasonals-like-staff policy operationally sustainable. That elevates it.
[EXTERNAL] Derek: Please. Anything else while I've got you? On your side, I mean.
[INTERNAL] Sam: That was my whole list, actually. Anything else on yours?
[EXTERNAL] Derek: No, that was the meat of it. The dashboard's fine, the seats are predictable, it's really just the bulk operations keeping me up at night.
[INTERNAL] Sam: Then that's where I'll focus. Let me read back the actions so we're aligned: I write up the bulk-deactivate defect with the partial-state and no-report and no-error-reference details plus the January volume context, I confirm whether bulk activation has the same ceiling before November, and I note the PDF-export ask without committing to timing.
[EXTERNAL] Derek: That's all of it. And the October decision point on the deactivate fix — don't let that one slip, that's the one with a real deadline.
[INTERNAL] Sam: October decision point, flagged and underlined. I'll follow up in writing this week. Thanks for laying it out so clearly, Derek — makes my job easy.
[EXTERNAL] Derek: I've filed enough vague tickets in my life to know a good one saves everybody time. Talk soon, Sam.
[INTERNAL] Sam: Talk soon.
