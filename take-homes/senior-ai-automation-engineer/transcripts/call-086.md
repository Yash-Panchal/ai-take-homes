# Call — Halcyon Robotics × BetterUp · QBR
Date: 2026-06-16 · Call ID: call-086
Participants: [EXTERNAL] Dr. Elaine Voss, VP People Analytics (Halcyon Robotics) · [EXTERNAL] Tobias Renn, HR Systems Analyst (Halcyon Robotics) · [INTERNAL] Sam Oduya, CSM

[INTERNAL] Sam: Hey both, thanks for making the QBR. Elaine, Tobias, good to have you. I know robotics people are busy building the machines that replace the rest of us.
[EXTERNAL] Elaine: We prefer "augment." Marketing insisted.
[INTERNAL] Sam: Ha, noted, augment. How's the quarter treating you?
[EXTERNAL] Elaine: Busy. We closed a Series D, so we've roughly doubled headcount plans for the year. Which is partly why I wanted Tobias on this one, he lives in the systems and reporting side.
[INTERNAL] Sam: Perfect, welcome Tobias. Let me share my screen and we'll walk the quarter, then I want to leave plenty of room for whatever's on your list.
[EXTERNAL] Tobias: Sounds good.
[INTERNAL] Sam: Okay. So this quarter you added 140 members, you're now at 620 active. Utilization is 78 percent which for a hypergrowth org is honestly excellent, a lot of fast-growing companies see utilization crater as they scale.
[EXTERNAL] Elaine: That's a relief. My board deck needs it to not crater.
[INTERNAL] Sam: It's holding. Session satisfaction is 4.6 out of 5, essentially flat quarter over quarter. Coach match acceptance is 88 percent on first suggestion.
[EXTERNAL] Tobias: What's the denominator on satisfaction, is that every session or a sample?
[INTERNAL] Sam: Post-session survey, so it's whoever responds, which is about 40 percent of sessions. I can get you the response rate breakdown if you want it for the deck.
[EXTERNAL] Tobias: Please, yeah. Elaine's going to get asked.
[INTERNAL] Sam: I'll send it after. Engagement by function, your engineering org is your heaviest user, then product, then G and A trailing a bit.
[EXTERNAL] Elaine: G and A always trails. They think they're too busy to develop. It's a whole thing.
[INTERNAL] Sam: The eternal struggle. Anything you want to dig into on the usage side, or should I keep moving?
[EXTERNAL] Elaine: Keep moving, the numbers are good, the numbers aren't why I'm worried.
[INTERNAL] Sam: Okay, ominous. What's the worry?
[EXTERNAL] Elaine: Not a worry exactly. More that I'm getting pressure from above to prove out the coaching investment in the language finance speaks, and right now the way I do that is clunky.
[INTERNAL] Sam: Say more about clunky.
[EXTERNAL] Elaine: So every month I go into the dashboards, I look at the engagement numbers, the utilization, the wellbeing trend, and I basically screenshot them into a slide deck. Tobias, how many screenshots was the last board pack?
[EXTERNAL] Tobias: For the coaching section? Eleven. I counted because it was miserable.
[INTERNAL] Sam: Eleven screenshots. Okay.
[EXTERNAL] Elaine: And here's the thing. Our whole analytics function runs on a proper BI stack. Everything else the board sees is a live dashboard I built. Attrition, comp bands, DEI metrics, hiring funnel, all of it flows into our BI tool and updates automatically.
[EXTERNAL] Tobias: We're a Tableau shop primarily, some Power BI in finance.
[INTERNAL] Sam: So coaching is the one island that doesn't flow in.
[EXTERNAL] Elaine: Exactly. It's the one data source I have to hand-carry. And it looks bad, frankly, in a company full of engineers, that the coaching metrics are the ones where the VP is manually screenshotting a web page like it's 2011.
[INTERNAL] Sam: I hear that. So what you'd want is a way to pull the engagement metrics programmatically, into Tableau, so they refresh alongside everything else.
[EXTERNAL] Elaine: Yes. An API, or a data connector, whatever the right word is. Tobias would know better than me what shape it needs to be.
[EXTERNAL] Tobias: Ideally a REST endpoint we can hit on a schedule, or a native connector. We can work with either. What we can't work with is a human clicking export buttons. That doesn't scale and it breaks the second I'm on vacation.
[INTERNAL] Sam: That's very clear. Let me ask a couple clarifying questions so I write this up right. Which metrics specifically, is it the engagement and utilization stuff, or do you need the individual-level detail?
[EXTERNAL] Elaine: Aggregate only. Please, God, not individual. We are extremely careful about the privacy line on coaching, individual coaching data never leaves the vendor by design and I want to keep it that way. It's the org-level and team-level engagement rollups I need.
[INTERNAL] Sam: Good, that actually makes it cleaner. Aggregate engagement and utilization metrics, exposed via API so you can pull them into Tableau on a schedule.
[EXTERNAL] Tobias: And ideally the historical series, not just current snapshot, so we can trend it. But even current snapshot on a schedule would let us build the trend ourselves.
[INTERNAL] Sam: Understood. And the pain today is real manual toil, eleven screenshots a month, plus the optics of it being the one manual data source in an automated shop.
[EXTERNAL] Elaine: You've got it exactly.
[INTERNAL] Sam: I want to be straight with you, we don't have a self-serve metrics API generally available today. What we have is the dashboards and the CSV exports. So this is a real product ask, not a "flip a switch" thing.
[EXTERNAL] Elaine: I figured. I'd rather know the honest state than get a runaround.
[INTERNAL] Sam: I appreciate that. Here's what I'll do. I'm going to write this up as a product request, API access to aggregate engagement metrics for BI ingestion, Tableau and Power BI named, aggregate only, historical series preferred. And I'll attach the business context, that it's a board-reporting requirement for a fast-scaling account.
[EXTERNAL] Elaine: The board-reporting framing will help. This isn't a nice-to-have for me, it's becoming a credibility issue.
[INTERNAL] Sam: I'll make that loud in the writeup. Can I quote the eleven screenshots? Product people respond to concrete toil.
[EXTERNAL] Elaine: Quote it. Quote Tobias's misery.
[EXTERNAL] Tobias: Please do, maybe someone will pity me.
[INTERNAL] Sam: Consider it quoted. Now realistically, I can't promise a date on a feature like this and I won't pretend to. What I can do is get it in front of product with a strong customer case and get you into any beta if one exists. If there's an early-access program forming for a metrics API you'd be a natural design partner given your BI maturity.
[EXTERNAL] Elaine: We'd absolutely be a design partner. Tobias would love that, he gets to complain directly to the people who can fix it.
[EXTERNAL] Tobias: My dream.
[INTERNAL] Sam: I'll flag you both as willing design partners in the writeup. In the meantime, is the CSV export getting you anything usable, or is it too manual too?
[EXTERNAL] Tobias: The CSV is better than screenshots but it's still me logging in and clicking, so it has the same "breaks when I'm out" problem. If I could at least automate the download that'd help but I don't think I can.
[INTERNAL] Sam: Not today, no scheduled or programmatic export currently. I won't sell you a workaround that doesn't exist. Let me get the real ask in front of product.
[EXTERNAL] Elaine: That's the right move. Thank you for not blowing smoke.
[INTERNAL] Sam: Never my style. Okay, shifting gears, anything else for the quarter? You mentioned the Series D, does that change your seat trajectory for next year?
[EXTERNAL] Elaine: Significantly up. We're modeling another 300 heads over 18 months. So expansion conversation is coming, probably Q3.
[INTERNAL] Sam: I'll get ahead of that. Are the new hires concentrated anywhere, engineering again?
[EXTERNAL] Elaine: Engineering and a big go-to-market build-out. We're finally commercializing the warehouse automation line.
[INTERNAL] Sam: Congratulations, that's a big step. GTM teams tend to adopt coaching fast when there's a performance-pressure element, so I'd expect your utilization to hold as you grow.
[EXTERNAL] Elaine: From your lips. Alright, I think that's my list. The metrics API was the big one.
[INTERNAL] Sam: Then let me recap. I'm sending you the survey response-rate breakdown for the deck, I'm filing the aggregate-metrics API request with the board-reporting business case and both of you as willing design partners, and I'll flag you for any beta. And I'll open the expansion conversation in Q3 around your growth plan.
[EXTERNAL] Tobias: That's all of it.
[INTERNAL] Sam: Elaine, Tobias, appreciate you both. I'll get that email over today.
[EXTERNAL] Elaine: Thanks Sam. Go tell product about my eleven screenshots.
[INTERNAL] Sam: They will hear about the screenshots. Take care both.
