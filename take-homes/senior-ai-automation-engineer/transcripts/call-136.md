# Call — Portman Grand Hotels × BetterUp · Admin Sync
Date: 2026-06-29 · Call ID: call-136
Participants: [EXTERNAL] Renata Kohl, HR Systems Administrator (Portman Grand Hotels) · [INTERNAL] Lena Kowalski, Implementation

[INTERNAL] Lena: Renata, hi — thanks for grabbing time. You mentioned in your note you'd hit a wall with the roster imports. Let's sort it out.
[EXTERNAL] Renata: Yes, please. I've been banging my head on this for two days and I'm about ready to blame gremlins.
[INTERNAL] Lena: Let's exorcise the gremlins together. But first, two days of head-banging deserves a coffee — how are you holding up otherwise? Hospitality in summer is no joke.
[EXTERNAL] Renata: Ha, I'm running on cold brew and spite at this point. Summer's our peak — every property's near capacity, which means near-full staffing, which means I'm provisioning people constantly.
[INTERNAL] Lena: The summer surge. Are you staffing up seasonally, or is this permanent headcount?
[EXTERNAL] Renata: Mix. We bring on a wave of seasonal staff for the summer — front desk, housekeeping, F&B — and then a chunk of them we keep if they're good. So there's a big provisioning spike in May and June and then a smaller trickle as we decide who stays.
[INTERNAL] Lena: That's a lot of roster churn in a short window. Which is exactly why the import matters so much for you.
[EXTERNAL] Renata: Exactly. If imports break during the summer spike, I'm dead in the water. Which is what happened, hence the panic email.
[INTERNAL] Lena: Understood — bad timing for it to break. Before we dig into the failure — how's the rollout across the properties going otherwise?
[EXTERNAL] Renata: Good, mostly. We're up to fourteen properties on the platform now. Each hotel's GM runs their own team, and I do the central admin work — provisioning, roster management, all the plumbing.
[INTERNAL] Lena: Fourteen properties from a central seat — that's a lot of plumbing for one person. Do the GMs do any of their own admin, or is it all funneled through you?
[EXTERNAL] Renata: It all funnels through me, by design. The GMs are great at running hotels and terrible at data hygiene, so I don't let them touch the roster. Learned that the hard way when a GM once uploaded a spreadsheet with everyone's names in the wrong columns.
[INTERNAL] Lena: Ha — centralizing it was the right call. One trained admin beats fourteen well-meaning GMs every time.
[EXTERNAL] Renata: That's my whole philosophy. I'm a control freak about the data because the data is the one thing that has to be right. Which is why this import failure has been driving me up a wall — I do everything correctly and it still broke.
[INTERNAL] Lena: So you're the one keeping the whole hospitality machine fed with clean data. Which is exactly why the import matters.
[EXTERNAL] Renata: Right. And with fourteen properties and turnover being what it is in hospitality — which is brutal, people come and go constantly — I'm doing roster imports all the time. New hires in, departures out. It's a weekly job at minimum.
[INTERNAL] Lena: Understood. So walk me through the import that's failing. What exactly are you doing and what happens?
[EXTERNAL] Renata: Okay. So I build a CSV — I've done this dozens of times, I know the format. Columns for name, email, employee ID, property, the whole thing. I go to the admin panel, Members, the bulk import, I upload the file, and it just... rejects the whole thing. The entire file. It doesn't import a single row.
[INTERNAL] Lena: The whole file rejected, no partial import. And what does it tell you when it rejects?
[EXTERNAL] Renata: That's the maddening part. It gives me the most useless error I have ever seen. It says — let me read it exactly — "An unknown error occurred. Please try again." That's it. That's the whole message. No line number, no field, no hint about what's wrong.
[INTERNAL] Lena: An opaque "unknown error occurred," no detail about what or where. And "try again" doesn't help because —
[EXTERNAL] Renata: Because trying again does nothing! It's not a fluke, it's the same file failing the same way every time. I tried again probably fifteen times out of pure stubbornness. Same error every time. It is not a "try again" situation.
[INTERNAL] Lena: I believe you. Let me help narrow it down, because "unknown error" is useless to both of us and I want to find the real cause. First — have you successfully imported before with this same process?
[EXTERNAL] Renata: Yes! That's why it's driving me crazy. I've done this exact workflow probably fifty times. Same panel, same kind of file. It's always worked. Now suddenly this batch won't go.
[INTERNAL] Lena: So something about this particular file differs from the ones that worked. Is there anything different about how you built it this time?
[EXTERNAL] Renata: Not that I can think of. I built it the same way I always do. Well — actually, this time I exported the starting template from a different system. Our new HRIS. We migrated HRIS platforms last month, and I pulled the roster out of the new one instead of the old one. But the columns look identical, I checked.
[INTERNAL] Lena: That's a useful clue. Different source system can introduce subtle formatting differences even when the columns look the same to the eye. Can I ask you to do something? Open the CSV in a plain text editor, not a spreadsheet — something like Notepad or TextEdit — so we can see the raw characters.
[EXTERNAL] Renata: Okay, hold on... opening it in Notepad now. Ugh, it's all commas and no formatting, but okay, it's open.
[INTERNAL] Lena: Perfect. Now look at the very first line — the header row with your column names. Read it to me exactly, character by character, especially at the very end of that line.
[EXTERNAL] Renata: The first line is: name comma email comma employee_id comma property comma start_date... and then... hm. There's a space after "start_date" before the line ends. There's like a trailing space at the end of the header row. Is that — that can't be it, can it?
[INTERNAL] Lena: That very well might be it. Trailing whitespace on the header row is exactly the kind of thing that a source-system export sneaks in and that the eye never catches in a spreadsheet, because spreadsheets hide it. And a strict importer can choke on it — the last column header reads as "start_date " with a space instead of "start_date", it doesn't match the expected field, and the whole parse fails.
[EXTERNAL] Renata: Are you serious. Two days over a space.
[INTERNAL] Lena: Let's confirm it's the cause before we celebrate. Delete that trailing space at the end of the header row — just the header row for now — save the file, and try the import again.
[EXTERNAL] Renata: Okay... deleting the space... saving... going back to the admin panel... uploading... and — it's importing! It's actually importing! All two hundred and thirty rows went through. You have got to be kidding me.
[INTERNAL] Lena: There we go. It was the trailing whitespace on the header. Your new HRIS export tacked a space onto the end of that header line, and the importer rejected the entire file over it.
[EXTERNAL] Renata: I am equal parts relieved and furious. Relieved it works, furious it was a space, and furious the error message told me absolutely nothing. If it had said "there's a problem with your header row" I'd have found it in five minutes instead of two days.
[INTERNAL] Lena: And that's the part I want to flag as a real problem — not your file, the error handling. You did nothing wrong; your file had a stray space that any normal export can produce, and the system's response was to reject the whole thing with a message that gives you zero information to fix it. That's a genuine product defect, and I'm going to write it up.
[EXTERNAL] Renata: Please do. Because I'm not the only admin who imports rosters, and the next person who hits this is going to lose two days like I did.
[INTERNAL] Lena: Exactly my thinking. Let me capture it precisely so it's actionable. The issue is twofold: first, the CSV importer rejects the entire file when the header row has trailing whitespace, rather than trimming it or importing anyway; and second, when it rejects, it returns an opaque "an unknown error occurred, please try again" with no indication of what or where the problem is. Does that match what you experienced?
[EXTERNAL] Renata: That matches exactly. And I'd add — "try again" is actively misleading, because trying again with the same file will never work. It made me waste time re-uploading instead of investigating.
[INTERNAL] Lena: That's a great detail, I'll include it — the guidance itself sends people down the wrong path. The ideal fix would be for the importer to tolerate trailing whitespace in headers, or at minimum to return a specific error like "unexpected header field" pointing at the row. Either would have saved you two days.
[EXTERNAL] Renata: Tolerating the whitespace would be best, honestly. Because I guarantee our HRIS is going to keep producing that space on every export, and I don't want to remember to hand-clean it every single week.
[INTERNAL] Lena: That's an important point for the write-up — this isn't a one-time fluke, your source system reproduces the trailing space on every export, so without a fix you're facing this weekly. I'll note that the trigger is reliably reproducible, which strengthens the case.
[EXTERNAL] Renata: Good. And in the meantime, I know to strip the space. But I'll be grumbling about it every week until it's fixed.
[INTERNAL] Lena: Grumble away — and yes, for now, opening the file in a plain text editor and clearing any trailing space on the header row is your reliable workaround. It's annoying but it works. I'd rather you have a working workaround than be blocked.
[EXTERNAL] Renata: While we're at it — is there any way to validate a file before I commit the import? Like a dry-run that tells me it's clean without actually creating anyone?
[INTERNAL] Lena: There isn't a formal dry-run mode today, no. The best current practice is to test with a small file — two or three rows — before you run the full batch, so if there's a formatting problem you catch it on three rows instead of two hundred.
[EXTERNAL] Renata: Huh. That's a decent habit. I'll start doing a three-row canary import first.
[INTERNAL] Lena: The canary import is exactly the right instinct — it would have caught this header issue immediately, on three rows, in ten seconds. I'll add "customer would value a dry-run/validation mode" as a note when I file the defect, since it's related, but the canary trick works today.
[EXTERNAL] Renata: Perfect. Belt and suspenders — canary import plus stripping the header space. I'll do both religiously now.
[INTERNAL] Lena: Belt and suspenders is the admin's way. I'll take it. At least now you know the trick.
[EXTERNAL] Renata: At least now I know the trick. Two days ago I was ready to file a support ticket titled "your import is possessed."
[INTERNAL] Lena: Ha. "Possessed" would've been a more accurate error message than "unknown error occurred." Let me read back the write-up: admin bulk CSV import rejects the entire file when the header row contains trailing whitespace, importing zero rows, and returns an opaque "an unknown error occurred, please try again" with no field or line detail — misleading because retrying the same file always fails. Reliably reproducible; the customer's HRIS export produces the trailing space on every export. Requested fix: tolerate header whitespace, or at minimum give a specific, actionable error. Got it all?
[EXTERNAL] Renata: You got all of it, including my emotional damage.
[INTERNAL] Lena: The emotional damage I'll leave out of the official ticket. Everything else goes in with your account attached. Anything else on your plate while I have you?
[EXTERNAL] Renata: No, that was the big one. Now that imports work again I can actually get my week back on track.
[INTERNAL] Lena: Glad we cracked it. To recap: import unblocked via the whitespace workaround, and I'm filing the importer defect and the error-message issue with your account and the weekly-reproducibility note attached. I'll keep you posted as it moves.
[EXTERNAL] Renata: Perfect. Thank you, Lena. You just saved my sanity.
[INTERNAL] Lena: Anytime. And genuinely, if you hit anything else during the summer spike, ping me directly rather than waiting for a scheduled call — provisioning delays during your peak are exactly when I want to be fast.
[EXTERNAL] Renata: I appreciate that. I'll take you up on it if the gremlins come back.
[INTERNAL] Lena: Please do. Go enjoy your working import. Talk soon.
