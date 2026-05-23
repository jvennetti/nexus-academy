# ⚡ MODULE 3 — THE AUTOMATION LAYER
### *From chatting to doing. Claude gets hands.*

---

## What This Module Is

This module is about moving from Claude as a conversation partner to Claude as an operator — a tool that  can plans tasks, execute workflows, and work your tools while you focus on larger-scale decisions.

By the end you'll have Cowork configured, connectors live, scheduled tasks running, and a working understanding of the automation layer that ties this new world together.

---

## Lesson 12 — Introducing Cowork
**Anthropic | ~1 min**

▶ [Watch Now](https://www.youtube.com/watch?v=UAmKyyZ-b9E)

This is the orientation that reframes what Claude actually is. A coworker that you can delegate real work to.

**Key takeaways:**
- Cowork lives in the Claude desktop app as its own tab, separate from the chat interface
- Requires a paid Claude account (Pro or Max) — not available on the free plan
- The mental shift starting here: you're not just prompting anymore, you're delegating

---

## Lesson 13 — Let Claude Handle Work in Your Browser
**Anthropic | ~1.5 min**

▶ [Watch Now](https://www.youtube.com/watch?v=rBJnWMD0Pho)

Three real workflows in 90 seconds. Claude for Chrome extends Cowork into your browser.

**Key takeaways:**
- Claude for Chrome is a separate extension that connects browser activity to Cowork
- Install Claude for Chrome now. You'll need it for lesson 18

---

## Lesson 14 — Claude Now Controls Your Entire Computer
**Paul Lipsky | ~7 min**

▶ [Watch Now](https://www.youtube.com/watch?v=dwYfNQzHQuY)

Paul Lipsky tests computer use on a live machine and shows where it works well and where it currently hits friction.

**Key takeaways:**
- Computer use is enabled under Claude settings → Computer Use — requires accessibility and screen recording permissions on Mac
- Claude takes screenshots and moves the mouse and keyboard on your behalf. Some actions cannot be undone so enable this deliberately
- When a connector exists for an app (Notion, Gmail), Claude uses the connector. Computer use kicks in for apps with no native connector
- Standout use case from the video: screenshot an idea on your phone → text it to your Mac → Cowork reads it and logs it to your database. Zero manual entry.

---

## Lesson 15 — Getting Started with Connectors
**Anthropic | ~3.5 min**

▶ [Watch Now](https://www.youtube.com/watch?v=_jjSS0qGFbI)

Claude gets dramatically more useful the moment it can talk to the tools you already use. Connectors give Claude access to Gmail, Google Calendar, Notion, and more. This is your first hands-on configuration step in the module.

**Key takeaways:**
- Connectors are found under Claude settings → Customize → Connectors
- You choose which connectors are active per task — scope is always your call
- Start with the tools you use every day before exploring anything more advanced

> **Do this now.** Connect at least two tools you use daily before continuing to Lesson 16.

---

## Lesson 16 — What is MCP?
**~10 min**

▶ [Watch Now](https://www.youtube.com/watch?v=AdODsQdGHz0)

Before you go deeper into automation, you need to understand the standard that makes all of it possible. MCP (Model Context Protocol) is the universal layer that lets AI agents connect to external tools without every integration being custom-built from scratch.

It is now the infrastructure standard for the AI agent ecosystem.

**Key takeaways:**
- Before MCP, connecting to external tools with AI required custom code for every single integration. 3 AI platforms × 3 tools = 9 separate builds. MCP reduces that to 6 total connections and eliminates redundant work
- MCP standardizes how context (tools, data, and prompt templates) moves between AI applications and external services
- One MCP server per service works with every MCP-compatible AI client. Build it once; it's compatible everywhere
- MCP doesn't enable new capabilities — it makes existing capabilities dramatically easier, compressing hours of setup into minutes
- Anything with a REST API can have an MCP server. Hundreds already exist.

---

## Lesson 17 — The Model Context Protocol (Deep Dive)
**Anthropic | ~30 min**

▶ [Watch Now](https://www.youtube.com/watch?v=CQywdSdi5iA)

This is the Anthropic team — the people who actually built MCP — talking about it from the inside. Dense, but worth it.

The podcast covers MCP's origin, why it went open source, what adoption looks like across the industry, and what's coming next. Treat it like a long-form briefing. First pass: listen while doing something else. Come back to the parts that are directly relevant to whatever you're building.

**Key takeaways:**
- MCP exposes three things to AI clients: **tools** (actions the model can take in the world), **resources** (data and files it can ingest), and **prompts** (slash-command-triggered prompt templates)
- MCP launched as open source deliberately — closed ecosystems create friction for integration builders; open standards lower the barrier for everyone and let the community maintain it
- At Anthropic's internal hackathon, with no mandate to use MCP, every single team gravitated toward building an MCP server. That organic signal confirmed the direction
- Current state: 10,000+ MCP servers in existence; major AI clients and model providers have adopted the standard; remote MCP (cloud-hosted) is now expanding beyond local-only setups through Claude.ai integrations
- What's coming: a **registry API** letting models search for and pull in new MCP servers on demand; better infrastructure for **long-running tasks**; and **elicitation** — a server's ability to ask the user for more information mid-task

---

## Lesson 18 — Full Claude Cowork Tutorial
**Futurepedia | ~15 min**

▶ [Watch Now](https://www.youtube.com/watch?v=7e3JovO8ngI)

The practical walkthrough. Watch this before the setup deep dive in the next lesson — this gives you the mental model first. Lesson 19 gives you the full configuration.

The key reframe this lesson makes: you stop writing prompts and start writing task briefs.

**Key takeaways:**
- Three tabs in the Claude desktop app: Chat, Cowork, Code. This module is about Cowork
- A task in Cowork is a multi-step instruction Claude executes end-to-end, not a single conversational exchange
- **Skills** are reusable instruction sets — the equivalent of SOPs for an employee. Claude draws on them automatically without you re-explaining context each time
- The more business context lives in your Skills, the less you have to include in each individual task prompt
- Cowork is not a replacement for Claude chat — it's a separate mode built for execution instead of conversation

---

## Lesson 19 — Set Up Cowork Better Than 99% of People
**BetterCreating | ~47 min**

▶ [Watch Now](https://www.youtube.com/watch?v=pl90LATQlHI)

Split this into two viewing blocks. This is the lesson that makes Cowork really work.

Most people spend 10 minutes on setup and wonder why results feel generic. The reason is always the same: they skipped the configuration. The setup is the leverage — everything that follows depends on what you build here.

**Key takeaways:**
- Skills are the core differentiator. Write them like you'd onboard a new hire: who are you, what's the business, what's the voice, what does a good output look like
- Permission management matters — configure exactly what Cowork can execute autonomously versus what requires your approval
- A well-built Skill runs better with less input. Time invested here compounds across every task you run going forward
- Don't rush this one. The 47 minutes is an investment in every hour of work that follows.

> **Before moving to Lesson 20:** Write at least one Skill for your own context — your name, your business or work situation, your communication style, and one recurring task you want Cowork to handle without re-explaining it each time.

---

## Lesson 20 — Scheduled Tasks: Working While You Sleep
**Brock Mesarich | ~13 min**

▶ [Watch Now](https://www.youtube.com/watch?v=Namp-sV0UEw)

The most overlooked feature in Cowork. Most people never configure it, but it's very important.

**Key takeaways:**
- Scheduled tasks run on a defined cadence — daily, weekly, or custom — without any manual trigger
- Regular Claude starts from zero every conversation. While Cowork with Skills starts by knowing your business, your context, and your tone
- Task quality depends directly on the Skill behind it. A vague Skill produces vague output on a schedule
- Use "Always Allow" on permissions you trust — every manual approval you remove is recurring automation for the AI

---

## Lesson 21 — Automate 90% of Your Social Media with Cowork
**~15 min**

▶ [Watch Now](https://www.youtube.com/watch?v=oFTA27l_TO4)

A live pipeline from someone who's actually running it. This is what Lessons 18–20 look like wired together.

The stack: competitor research → content ideation → draft generation → scheduled publishing. Modular Skills. Running on a schedule. Output produced without operator input.

**Key takeaways:**
- The system starts with competitor and market research, which feeds the strategy. Claude isn't just automating the writing — it's also automating the thinking behind what to write
- Each stage of the content pipeline is its own skill — modular, adjustable, replaceable without breaking other skills that are working well
- Skills make this architecture portable: the same structure works for any niche, business, or content format
- This is what a solo content operation looks like at scale — no team required

---

## Lesson 22 — Zapier MCP: The Unlock
**Paul Lipsky | ~11 min**

▶ [Watch Now](https://www.youtube.com/watch?v=nxAU266r2co)

Claude's built-in connectors are a great starting point, but Zapier MCP is where Cowork becomes genuinely autonomous.

This lesson solves one particular constraint: native Claude connectors often require approval before acting. Drafting an email is fine; sending it requires confirmation. Zapier MCP gives Claude broader permissions and unlocks 8,000+ apps that aren't available through native connectors.

**Key takeaways:**
- Native Gmail connector drafts emails but won't send without approval. Zapier MCP drafts and sends
- Zapier MCP is a bridge — it extends Claude's connectors with broader permissions, not a replacement for them
- Setup: go to zapier.com/mcp → create a Claude MCP server → add tools → connect inside Claude under Connectors → Zapier Custom
- Free plan: 100 tasks/month. Paid plans available when volume requires it
- Recommended tools to connect first: Gmail, Google Sheets, Asana, Notion
- If a tool has both a native connector and Zapier MCP available, Zapier MCP typically has broader permissions — use that
- Use "Always Allow" only deliberately. Each permission granted removes one approval step from every future scheduled task

> **Do this now:** Set up your Zapier MCP server and connect at least one tool you already use via the native connector. Run the same task both ways and observe the difference.

---

## Lesson 23 — What Is n8n?
**Zero Code Devs | ~3 min**

▶ [Watch Now](https://www.youtube.com/watch?v=DRqvtMFq0y8)

n8n is an automation platform — like Zapier, but built differently.

**Key takeaways:**
- n8n is open-source and self-hostable; Zapier is cloud-based with a free tier and paid scale
- Both connect apps and automate workflows — the difference is where the logic lives and who controls the infrastructure

---

## Lesson 24 — n8n vs Zapier: Pick Your Tool
**~12 min**

▶ [Watch Now](https://www.youtube.com/watch?v=ZqoXUJPFmBA)

The decision lesson. You will leave with a clear answer on which automation tool belongs in your stack — and the framework to explain that choice to a client.

Neither tool is universally better. The right answer depends on how you work, how technical you want to get, and whether you prioritize speed to deployment or infrastructure control. (Note from Joshua: I feel like Zapier is the best option for us but I haven't watched this video. Let's decide on this together so we can learn using the same tools)

**Key takeaways:**
- **Zapier:** faster setup, cloud-native, 8,000+ integrations, lower technical barrier — best when you need to move quickly and don't require infrastructure control
- **n8n:** more powerful for complex logic, lower cost at scale, more configuration required — best when you need full control, custom workflows, or white-labeled solutions for clients
- Both are used professionally. This isn't a beginner vs. advanced split.
- If you're unsure: start with Zapier. You can migrate logic to n8n when your needs grow and the tradeoffs become real

---

## Lesson 25 — Zapier AI Agents: Step-by-Step
**Kevin Stratvert | ~12.5 min**

▶ [Watch Now](https://www.youtube.com/watch?v=avQMU1yJkyY)

Hands-on from start to finish: a Zapier Agent built from scratch (trigger, tools, instructions, test, deploy.

The walkthrough constructs a complete invoice follow-up agent: reads a Google Sheet, identifies overdue invoices, emails the customer, logs the update, and runs daily at 8 AM — no manual input after setup.

**Key takeaways:**
- A Zapier Agent = a trigger + connected tools + plain-English instructions + AI. Clear, specific instructions are the variable that separates an agent that runs cleanly from one that asks too many clarifying questions
- Tools give the agent the ability to act — without them, it can reason through steps but can't touch your apps
- Test before going live. The test run in this video catches a missing detail (the sheet name) that would have broken the live run
- Free tier: 400 activities/month. Pro: 1,500/month. An activity is any single action the agent takes — a lookup, an email send, a record update
- Once live and toggled on, Zapier agents run without approvals — fully autonomous on the schedule you define

---

## Module 3 Challenge

**The Real-World Scenario:**

You've just taken on a new client — a local home services company (HVAC, landscaping, cleaning) that handles all follow-up manually. They're losing jobs to faster-responding competitors. The owner estimates they miss 20–30% of leads simply because follow-up arrives too late or not at all. They've asked you to build the first piece of their automation stack before your next meeting.

Before you build, set up your environment:

Open Claude chat and prompt it to build everything you need to run this system. Ask it to generate: a complete lead tracking sheet (10 fictional leads with names, service type, contact info, inquiry date, and follow-up status — a mix of fresh leads and ones overdue for contact), a Skill document that defines Ridgeline's business context, voice, services, and what a good follow-up message looks like, and a sample follow-up message for one of the overdue leads so you know what the output should look like before you automate it. Copy the lead data into a Google Sheet. Save the Skill document. You now have a real environment to build against.

Your challenge:

1. Load the Skill you generated into Cowork so it knows who Ridgeline is
2. Set up a scheduled task that runs daily: check the lead sheet, identify anyone not followed up with in 48+ hours, and draft a personalized outreach message for each
3. Use Zapier MCP to wire at least one action the native connectors can't handle — ideally sending the message or logging the outreach back into the sheet

**Your deliverable:** A running scheduled task that produces at least one real output against your lead sheet — with no manual input from you to trigger it.

**Advanced extension:** Add a second scheduled task that runs Monday mornings and delivers a weekly summary to your inbox: leads contacted, responses received, calls booked, and follow-ups still pending.

> **Integration note:** This is the automation pattern that appears across almost every services business — home services, consulting, real estate, agency work. The system you're building here is the same architecture you'd package and sell to a client. Build it like it's going to a real paying customer, because it is.
