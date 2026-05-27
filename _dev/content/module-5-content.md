# 🎯 MODULE 5 — LEAD GENERATION MACHINE
### *Build the pipeline that fills your calendar.*

---

## What This Module Is

By the end of this module you'll have a working lead generation pipeline — from research to enrichment to personalized outreach — running with minimal manual input. You'll know how the tools talk to each other, why each one exists in the stack, and how to deploy this for yourself and for a client.

---

## Lesson 34 — Getting Started with Research in Claude.ai
**Anthropic | ~2.5 min**

▶ [Watch Now](https://www.youtube.com/watch?v=R-KJgjIrh24)

A quick orientation to Claude's Research mode — your prospecting engine for this module.

**Key takeaways:**

- Enable Research from the bottom-left of the chat window. It runs in the background (5–45 min) and returns a cited, multi-source report — not a search result
- Detail your prompt. Vague prompts trigger follow-up questions before Research starts. Specific prompts produce usable output the first time

---

## Lesson 35 — Getting Started with Projects in Claude.ai
**Anthropic | ~7 min**

▶ [Watch Now](https://www.youtube.com/watch?v=GJ5jTgcbRHA)

Projects give Claude consistent and reliable context. Every prospect and client gets their own project: its own knowledge base, instructions, and chat history.

**Key takeaways:**

- Anything uploaded to a project's knowledge base is automatically loaded into every chat inside it. Avoid re-explaining
- Project instructions set Claude's behavior for every conversation in that project: tone, role, output format, and what it's trying to help you accomplish
- One-off context (a prospect's annual report, a single contract) should be directly uploaded into a chat without adding it to the knowledge base permanently
- On team plans, projects are shareable with view or edit permissions — one person builds the framework, the team inherits it

---

## Lesson 36 — What Is Clay?
**~5 min**

▶ [Watch Now](https://www.youtube.com/watch?v=v31hKg-WSCc)

Clay is the enrichment layer that sits between your lead source and your sequencer. You'll see it directly referenced in the next two lessons - this is your orientation.

**Key takeaways:**
- Clay has a four-step framework: Find the people you want to reach, Enrich them with data, Transform that data into something useful (like a personalized email), then Export it to wherever you send from
- Instead of being locked into one data source, Clay checks multiple sources back to back and only charges you when it actually finds something; so you get better coverage without paying for misses
- Clay has a built-in AI agent that can browse the web on your behalf — useful for finding signals that no database would have, like whether a company just hired a new sales director or recently rebranded

---

## Lesson 37 — How to Use Apollo.io — Full Tutorial
**Matt Lucero | ~20 min**

▶ [Watch Now](https://www.youtube.com/watch?v=n_lRMtWDU40)

Apollo is one of the best lead sources. 220+ million contacts with verified emails, direct dials, and firmographic filters that let you build a precisely targeted list.

**Key takeaways:**
- Apollo's primary value is its database and the ability to filter it with precision: job title, seniority, company size, industry, revenue, buying intent signals, tech stack, location, and more
- Filter for **Verified** and **Guessed** to maximize deliverability
- When building a list: start in the **Companies** tab to identify target accounts by firmographic criteria, then switch to the **People** tab to find decision makers inside those companies. Working top-down produces higher-quality lists than building from people alone
- Export to a Google Sheet and clean it up before it goes anywhere else
- Apollo → Clay is a natural handoff: export from Apollo, import to Clay for enrichment, personalization, and transformation

---

## Lesson 38 — AI Sales Automation with Claude: Full Lead Gen System (No Code)
**Marc | ~18 min**

▶ [Watch Now](https://www.youtube.com/watch?v=TWAnPWOzUnE)

This is a full Lead Generation workflow: Claude Cowork as the orchestration layer, Apollo or Clay for contact enrichment, Lemlist as the sending infrastructure. No code required. The whole system can be scheduled to run on repeat.

**Key takeaways:**
- The full workflow runs inside Cowork: find the companies, find the contacts, write the emails, push to Lemlist — all in one task
- If you don't have a target company list yet, that step can be part of the workflow — Claude can research and generate the account list
- You need Lemlist (or a similar tool) for sending at volume. One inbox can't handle it, and 1,000+ emails sent in a day will get flagged
- Load your outreach playbook into a Cowork Skill so Claude writes in your voice, not a generic one
- To put this on autopilot: end the session by asking Claude to schedule the task (e.g., every Monday at 9 AM). It asks for approval once, then runs without you! (Note from Joshua: I added an exclamation point because this is awesome)

---

## Lesson 39 — Claude Cowork Just Changed Sales Forever
**Ben AI | ~15 min**

▶ [Watch Now](https://www.youtube.com/watch?v=EqJoui72QrU)

This lesson shows Cowork operating across the full sales cycle — prospecting, qualification, call prep, pipeline review, and win/loss analysis. Enjoy!

**Key takeaways:**
- There's a ready-made **Sales Plugin** inside Cowork under Browse Plugins — install it and customize from there
- The connectors that matter most for sales: Apify, Apollo, Clay, Lemlist or Instantly, and your CRM
- Scheduled call prep and win/loss analysis are the two highest-value Skills shown — both worth building early
- The fastest way to build a new Skill: do the workflow manually with Claude once, then ask it to save that process as a Skill at the end of the session

---

## Lesson 40 — Claude Code Just Changed Lead Generation Forever
**Eric Nowoslawski | ~20 min**

▶ [Watch Now](https://www.youtube.com/watch?v=RLHzU2_Xl5g)

Think of Cowork as the tool that handles tasks on a schedule — Claude Code goes further, running full campaigns at scale, doing the filtering and research for you, and actually getting better over time without you touching it.


**Key takeaways:**

- Skills in Claude Code work the same way as in Cowork — but with direct access to your computer and other tools
- You can have Claude Code automatically filter your lead list by visiting each company's website and deciding if they're a fit
- The most important concept in this video is **Auto Research** — Claude Code runs your campaigns, checks what's working, makes changes, and repeats. It learns over time without you doing anything

---

## Module 5 Challenge

**The Real-World Scenario:**

Summit Properties is a boutique real estate agency. They work with investor clients — people looking for rental properties, fix-and-flips, and commercial deals — but everything they do to find new clients is manual. Their best salesperson spends 6 hours a week just researching prospects, tracking down email addresses, and writing first messages to people they found on LinkedIn or through referrals. They've never had a real outbound system. You've been brought in to build one.

Before you build, set up your environment:

Open Claude and ask it to produce all of the following for Summit Properties:

- **ICP brief** — a description of their ideal client: what kind of investor they are, what their job title typically is, what size company they work at, where they're based, and three problems they have that Summit can solve
- **Prospect list** — 15 fictional people who match that description, with name, title, company, and LinkedIn URL
- **One sample outreach email** — written in Summit's voice, so you know what good looks like before you automate it
- **Cowork Skill document** — a document that tells Cowork who Summit is, what they do, who they sell to, how they like to sound, and what a good cold email from them looks like. Save this as a Skill in Cowork
- **Claude Project** — Create a new project in Claude called "Summit Properties." Paste the ICP brief into the project instructions. Upload the sample email and Skill document into the project knowledge. Run every conversation for this challenge inside this project — that way Claude always knows the context and you never have to re-explain it

You now have a real environment.

**Your challenge:**

1. **Research brief** — Use Claude's Research mode to build a clear picture of Summit's ideal client: who they are, what would tell you they're actively looking for deals right now, what they care about, and how you'd find them on Apollo or LinkedIn
2. **Lead list** — Using Apollo (the free plan works), build a filtered list of people who match that profile. Export it to a Google Sheet with at minimum: name, title, company, email, LinkedIn URL, and company size. Clean up any blank rows or extra columns before moving on
3. **Outreach campaign** — Load your Skill into Cowork and run the sequence: have it go through the lead list, write a personalized first email for each person using Summit's voice and their specific details, then push everything into Lemlist as a campaign. If you haven't set up Lemlist yet, save the emails into a Google Sheet instead
4. **Schedule it** — Set the pipeline to run automatically. Either weekly (every Monday, pull 10 new leads from Apollo and draft outreach) or triggered when a new row is added to the lead sheet

**Your deliverable:** A working outbound pipeline — a research brief, a clean lead list, drafted outreach emails, and at least one step running on its own without you triggering it. Aim for under 45 minutes of active work once the environment is set up.

**Advanced extension:** Build a call prep Skill for Summit. When someone books a meeting, the Skill looks up their LinkedIn profile, their company website, and any recent news about them — then puts together a one-page summary with a company overview, what problems they likely have, questions to ask on the call, and which part of Summit's offer to lead with. Set it to run automatically each morning based on that day's calendar.

> **Integration note:** The pipeline you're building here — find the right people, reach out, follow up, is exactly what every successful agency, brokerage, and service business runs on. The person who can build this for a client in an afternoon isn't just good with AI. They're solving a real revenue problem. That's the business.
