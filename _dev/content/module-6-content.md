# 🏆 MODULE 6 — CLIENT READY
### *Close deals, deliver well, build a real business.*

---

## What This Module Is

This module is about what you do with the skills you've learned. Plus some more. Get ready for vision casting plus some more information. Go at the speed of rest!

---

## Lesson 41 — How to Build a $10M Solo AI Business (Zero Code)
**Dan Martell | ~14 min**

▶ [Watch Now](https://youtu.be/w-XPlC3a2oI)

Before you look at what to charge or how to close, you need a clear picture of what you're actually building toward. This is that video. Watch it first.

**Key takeaways:**
- Your job isn't to do the work — it's to design the system that does the work
- Start with the problem, not the tool. Fall in love with what the customer is trying to solve
- Solve the problem manually before you automate them
- Scale by reducing your involvement, not adding people

---

## Lesson 42 — Claude Skills: SOPs For Agents
**~15 min**

▶ [Watch Now](https://www.youtube.com/watch?v=fvUGQFtJaT4)

You've used Skills throughout this course. This video explains the architecture behind them and why they matter beyond just your own builds — they're the delivery mechanism for client work.

**Key takeaways:**
- The quality of an agent's output is a direct function of the context it's given. Better Skills, more consistent results
- Skills are composable and portable — build once, use across Cowork, Claude Code, and the API
- Writing a Skill is like onboarding someone: what's the business, what's the task, what does good look like, what do you do when something's unclear
- What you hand a client isn't the automation. It's the system that runs without them

---

## Lesson 43 — How I Sold These 4 AI Agents for $23,000 (as a Beginner)
**Nate Herk | ~14 min**

▶ [Watch Now](https://www.youtube.com/watch?v=HNKlFTd1maM)

Watch what this guy gets wrong and what he gets right. Real deals, real numbers, real mistakes. 

**Key takeaways:**
- Price on ROI, not effort — calculate what the problem costs the client, then price as a fraction of what solving it saves them
- Lead with the cost of the problem, not what you can build
- Underpricing, under-scoping, and chasing small retainers too early are the three things that quietly kill this business

---

## Lesson 44 — What I'd Learn Instead of Automation in 2026
**Nick Saraev | ~13 min**

▶ [Watch Now](https://www.youtube.com/watch?v=YIl-awY250k)

Nick runs a $400K/month automation agency and is pivoting away from automation as a primary skill. His perspective is important.

**Key takeaways:**
- Technical execution skills get invalidated by every major wave of technology. Automation is next
- What replaces it: knowing what a business actually needs and communicating it precisely enough for AI to execute reliably
- The shape of a service business — marketing, sales, onboarding, delivery, reactivation — is the same regardless of what you're selling
- Learn the shape because the tools will continue changing

---

## Module 6 Challenge — The Final Task

**The Scenario:**

Meridian Missions is a non-profit with 12 field teams operating across 4 countries. Every week, each team submits a field report. Every week, someone on staff manually reads those reports, pulls out the highlights, writes donor update emails, compiles a prayer bulletin, and flags anything urgent to leadership.

It takes the better part of two days. Most of it is pattern work — the same structure, the same extraction logic, the same destinations — repeated across 12 reports every single week.

Your job is to build the system that does it.

This is the only challenge in the course where multiple agents work together as a coordinated system. Each one does a different job. They run off the same input. They produce different outputs for different people. This is what systems thinking looks like when it's built.

---

**Step 1 — Generate your environment**

Before you build anything, you need data to build against. Open Claude and paste this prompt exactly:

> *"I'm building a multi-agent system for a non-profit called Meridian Missions. Generate the following five documents. Format each as a clearly labeled, separate section I can save individually.*
>
> *Document 1 — Org Brief: Meridian Missions' mission statement, the three regions they operate in (South Asia, East Africa, South America), their three donor segments (Standard, Partner, Major Donor), their communication tone, and what they care most about in how they present their work publicly.*
>
> *Document 2 — Six Field Reports: Two reports from each region (six total). Each report should include: team name, region, a 2–3 paragraph program update, two or three prayer requests, and exactly one item explicitly flagged as urgent. Make the urgent items varied — a medical situation, a funding gap, a security concern.*
>
> *Document 3 — Donor Contact List: 12 fictional donors. Four per segment (Standard, Partner, Major). Each entry needs: full name, email address, giving level, and which region they're most personally connected to.*
>
> *Document 4 — Donor Email Samples: One example donor update email for each segment. Standard gets a warm general update. Partner gets program specifics and impact numbers. Major Donor gets a personal note written as if it's from the executive director.*
>
> *Document 5 — Prayer Bulletin Sample: A complete example weekly prayer bulletin — what it includes, how it's structured, and how it reads when it's done well."*

When Claude delivers the five documents, do the following before you build anything:

- Save each document somewhere you can reference it — a Google Doc, a Notion page, or a folder of text files
- Copy Document 3 (the donor contact list) into a Google Sheet with columns for: Name, Email, Giving Level, Region
- Read through the six field reports and make sure each one has a clear urgent flag — if any are vague, ask Claude to sharpen them
- Read the email samples and the bulletin. These are your quality bar. Every agent you build should produce output that clears this standard

You now have a real environment.

---

**Step 2 — Build the four agents**

Each agent takes the weekly field reports as its primary input and produces a specific output. Build them in order — each one feeds the next.

---

**Agent 1 — The Field Summarizer**

**Job:** Read each field report and extract three things: a concise program progress summary, the prayer requests, and any urgent needs. Output one structured section per team, in a consistent format.

**Build it:** Start in Claude chat. Write a prompt that processes a single report into the right structure. Test it against two or three of your sample reports until the output is clean and consistent. Then decide where this agent lives:

- If you want it triggered manually or on a schedule: build it as a Cowork task with a Skill that defines Meridian's context and the expected output format
- If you want it triggered automatically when a new report arrives: build it as an n8n or Zapier workflow

The output of this agent is the input to every other agent. Get it right before moving on.

---

**Agent 2 — The Donor Communicator**

**Job:** Take the summaries from Agent 1 and generate personalized donor update emails — one per donor, matched to their giving level and regional connection. Standard donors get the general program update for their region. Partners get program detail and impact specifics. Major Donors get a message that reads like it came directly from the executive director.

**Build it:** Load your donor contact sheet and your Document 4 samples as context. Write a prompt that takes one summary + one donor record and produces a correctly segmented email. Run it against all 12 donors. The output should be staged as drafts in Gmail (via Zapier MCP) or written into a new tab in your Google Sheet — one row per donor, one column for the drafted email.

---

**Agent 3 — The Prayer Bulletin**

**Job:** Pull all the prayer requests from Agent 1's summaries and compile them into a single weekly bulletin — organized by region, formatted for email distribution, and clean enough to send without editing.

**Build it:** This is the simplest agent. Write a prompt that takes the prayer request sections from your six summaries and produces a complete bulletin matching your Document 5 sample. Run it, review the output against your sample, and adjust until it's clean. Output can be a formatted document, a Google Doc, or plain text — whatever format Meridian would actually use.

---

**Agent 4 — The Needs Router**

**Job:** Scan Agent 1's summaries for anything flagged as urgent. For each urgent item: draft a short priority alert email to the regional director and log the need in a tracking spreadsheet.

**Build it:** This agent needs to actually write to somewhere — not just draft. Wire it through Zapier MCP or n8n so the log entry happens without you doing it manually. The tracking spreadsheet should capture: team name, region, date flagged, and a one-line description of the need. The alert email should be short, clear, and read like it came from a staff member, not a robot.

This is the agent that tests whether your system can take action, not just produce text.

---

**Step 3 — Run a full cycle**

With all four agents built, run the system against your six sample reports as if it's Monday morning and the reports just came in.

- Agent 1 processes all six reports into structured summaries
- Agent 2 generates donor emails for all 12 contacts
- Agent 3 produces a complete prayer bulletin
- Agent 4 identifies the urgent flags, drafts the alerts, and logs them

Your deliverable is the real output of that cycle — the six summaries, the 12 donor emails, the bulletin, and the needs log — produced with as little manual work from you as possible. If you had to manually trigger each agent, that's fine. If you wired them to run sequentially, even better.

---

**What you just built**

Every organization running field operations, donor communications, or distributed teams has this problem. Information comes in from multiple places. It needs to go out to multiple audiences in multiple formats. Someone is doing it by hand.

The four-agent structure you built here — ingest, communicate, distribute, escalate — is not specific to non-profits. It's the same pattern inside a real estate agency processing weekly market reports, a consulting firm managing client updates, or a franchise operation running location check-ins.

You now know how to build it.

---

> **Self-verify when complete.** All four agents built. Full cycle run against your sample data. Real output produced for every agent. When it's done, mark complete.
