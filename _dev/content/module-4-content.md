# 🤖 MODULE 4 — THE AGENT BLUEPRINT
### *From automation to agents. You're building systems now.*

---

## What This Module Is

Module 3 gave Claude hands. This module gives it a brain.

Automations execute what you define. Agents figure out what needs to happen and execute that — even when the path wasn't mapped in advance.

By the end of this module you'll have a clear mental model of how agents actually work, understand where they're worth building and where they aren't, and have a working example of a multi-step agent in the real world.

---

## Lesson 26 — You're Not Behind (Yet): How to Build AI Agents in 2026
**Futurepedia | ~25 min**

▶ [Watch Now](https://www.youtube.com/watch?v=ibFJ--CH3cQ)

Before you can build something well, you need a clear picture of what it actually is — and "agent" has become one of the most over-used and under-defined words in the space right now. This video shows two real agents being built step-by-step across two different platforms.

**Key takeaways:**
- An AI agent is a system that can reason, plan, and take actions on its own based on the information it's given — think of it as a digital employee that can use tools and make decisions
- The critical distinction: a **workflow** runs through a fixed, pre-defined sequence of steps. An **agent** decides how many steps to take and which ones — you don't know in advance.
- Agents need three things to function: a goal or task, access to tools (search, APIs, files, etc.), and a loop — the ability to keep running until the task is resolved
- You don't need a technical background to build them anymore. The barrier is understanding the architecture, not writing code
- The agents cutting the most time aren't replacing entire roles — they're compressing specific high-volume workflows from hours to minutes. That's where to start

---

## Lesson 27 — Tips for Building AI Agents
**Anthropic | ~18 min**

▶ [Watch Now](https://www.youtube.com/watch?v=LP5OCa20Zpg)

This one's from Anthropic's (Claude's) own AI teams — the people who built and study how agents perform in production.

**Key takeaways:**
- **Workflows vs. agents** isn't a hierarchy — it's a spectrum. Many production systems are a mix: structured steps where the path is known, agent loops where it isn't. You choose what to use depending on how predictable the task is
- Tool descriptions matter as much as the agent's instructions. A vague tool description produces uncertain tool use. Write them like you'd brief a new hire: what it does, when to use it, what to expect back
- Most agent failures aren't model failures — they're design failures. Poorly scoped tasks, ambiguous instructions, missing context. Start simpler than you think you need to
- **Build measurement in from the start.** Agents that aren't being evaluated can't be improved
- Avoid the over-engineering trap: some of the best-performing production systems run everything inside a single LLM call. Complexity doesn't equal capability
- Where agents genuinely outperform simple automation: tasks where the number of steps is unknown, tasks requiring judgment between multiple options, and tasks that need to recover from unexpected results mid-run

---

## Lesson 28 — Claude Ran a Business in Our Office
**Anthropic | ~6 min**

▶ [Watch Now](https://www.youtube.com/watch?v=5KTHvKCrQ00)

This is a fun video about Anthropic's internal experiment where they gave Claude autonomous control of a vending machine business inside their office.

Watch it as a case study. The point isn't the vending machine — it's what holds up and what breaks when you hand a real operational task to an AI with physical consequences.

**Key takeaways:**
- Claude handled the expected parts well: pricing logic, inventory reasoning, structured decisions with clear criteria
- This test revealed the agent's limits: ambiguous situations, customer interactions requiring judgment calls, and tasks that needed context the agent didn't have access to failed
- Autonomous agents in production need clearly defined boundaries — what the agent can decide alone and what needs a human checkpoint. Vague scope produces unexpected behavior

> **The pattern that holds across every agent deployment:** agents perform best on tasks that are well-defined, bounded, and measurable. The further you move from that, the more oversight architecture you need to build alongside the agent.

---

## Lesson 29 — I Built a Marketing Team with 1 AI Agent and No Code
**Nate Herk | ~33 min**

▶ [Watch Now](https://www.youtube.com/watch?v=ldETapkr8Hg)

Nate builds a complete multi-agent content pipeline inside n8n — from a single prompt, the system creates videos, LinkedIn posts, blog posts, images, and image edits, all logged to Google Drive. This is the architecture lesson. Watch how the agent is constructed, not just what it produces.

**Key takeaways:**
- A single agent can access multiple tools simultaneously — this one routes between six distinct workflows based on what you ask it. One agent, many capabilities
- The agent doesn't just produce content — it maintains a log of everything it creates (type, prompt, Drive link), which becomes a searchable asset library over time
- The interface (Telegram, voice or text) is separate from the logic. Changing the interface doesn't change the workflows beneath it
- Each workflow is modular — video creation, image generation, and blog writing are independent nodes. Break one and the others keep running
- Real operational cost: the video covers what this system actually costs to run monthly. Build with that number in mind before deploying for a client

---

## Lesson 30 — Every Claude Code Concept Explained for Normal People
**Simon Scrapes | ~27 min**

▶ [Watch Now](https://www.youtube.com/watch?v=ZlDnsf_DOzg)

Claude Code is the command-line interface for Claude — a terminal-based environment where Claude can read and write files, run code, and interact with your computer directly. It's more powerful than the chat interface and more precise than Cowork for technical builds.

This lesson covers 27 core concepts in under 60 seconds each, building from the basics up.

**Key takeaways:**
- Claude Code gives Claude access to tools that operate on your computer: reading and writing files, running bash commands, and navigating directories. That's the fundamental difference from chat — it can act, not just respond
- The **context window** is Claude's short-term memory for a session. When it fills up, older content falls out. Managing context is a skill
- **Context rot** happens as sessions grow long: Claude starts losing track of earlier instructions and details. The fix is starting clean sessions for new tasks and using memory files to preserve critical context across sessions
- **Subagents** are separate Claude instances that run with their own clean context windows, following instructions from the main agent. When a task grows complex, the main agent delegates to subagents rather than cramming everything into one bloated context
- **MCP servers** are how Claude Code connects to external tools
- **Skills files** in Claude Code are persistent instruction sets — like Cowork Skills
- You don't tell Claude which tool to use. You describe what you want. Claude picks the right tools automatically

---

## Lesson 31 — Claude Design Basics: Master 95% in 10 Minutes
**Tristen O'Brien | ~10 min**

▶ [Watch Now](https://www.youtube.com/watch?v=X7YMMyd2Qnk)

Claude Design is a separate, experimental Anthropic tool for visual and interface work — accessible at claude.ai/design. It generates wireframes, high-fidelity prototypes, and slide decks from plain-language prompts. Here's your orientation to Claude Design.

**Key takeaways:**
- Four starting modes: **Prototype** (wireframe or high-fidelity), **Slide deck**, **From template**, or **Other**. High-fidelity mode is where most of the leverage is
- The most-skipped step (and the most important): **providing visual reference material**. Claude Design performs significantly better when it can see examples of the aesthetic you're aiming for — screenshots, URLs, or uploaded images
- You can export prototypes directly to code — HTML/CSS/React — making it a practical starting point for real builds, not just mockups
- Note from Joshua: Claude Design is in research preview, and the Weekly Usage Limits are entirely separate from your regular Claude usage limits. You get a whole new set of tokens to try out Claude Design

---

## Lesson 32 — I Built 5 Websites in 18 Minutes with Claude
**Luke Carter | ~18 min**

▶ [Watch Now](https://www.youtube.com/watch?v=TWZ90EUyejk)

What you used to think required a designer, a developer, and a week now requires a prompt, iteration, and an afternoon. This is called "vibe coding".

**Key takeaways:**
- Claude Opus 4.6's built-in design aesthetic is strong enough that you don't need to supply inspiration — you need to supply a clear, structured prompt
- The prompt framework that works: **[type of site] for [specific business], [tone/aesthetic], [key sections needed], [any reference or constraint]**. Vague prompts produce generic output; specific prompts produce specific work
- Iteration is the workflow. The first output is a draft, not the deliverable. Every pass in this video narrows from a rough direction to a polished result
- Claude builds in the Artifacts panel — you see the site rendered live as it writes. Changes are instant

---

## Lesson 33 — Claude Works with You on Slides, Spreadsheets, and Contract Redlines
**Anthropic | ~1.5 min**

▶ [Watch Now](https://www.youtube.com/watch?v=LpGpwhORWr0)

Claude works directly in Microsoft Office files.

**Key takeaways:**
- Claude now works inside Excel and PowerPoint — formatting, populating, and structuring real files, not generating text to paste elsewhere
- The contract redline demo is particularly relevant for service providers: Claude reads an existing contract, identifies clauses to revise, and marks changes in tracked-changes format — the standard output format for legal and client-facing work
- This closes the loop between generation and delivery. The output is the file the client receives

---

## Module 4 Challenge

**The Real-World Scenario:**

ClearView Advisory is a boutique consulting firm. Their team is producing client deliverables manually — proposal documents, research briefs, presentation decks. Every engagement starts from scratch: the same structure, the same research process, the same formatting work. The partner leading the engagement estimates they spend 6–8 hours per proposal that should take 90 minutes. They've asked you to build a system that changes that.

Before you build, create your environment:

Open Claude and ask it to generate everything you need to run this scenario: a fictional ClearView client brief (company name, industry, engagement type, 3–5 key questions they want answered), a Skill document defining ClearView's voice, their proposal structure (executive summary, research findings, recommended approach, next steps), and a sample one-page research summary on that client's industry so you know what the output should look like. Save the Skill. You now have a real environment.

**Your challenge:**

1. **Research brief** — Use Claude's deep research mode to produce a structured research summary on the client's industry based on the brief. The output should be usable in a proposal without editing
2. **Proposal document** — Using Claude in Excel or PowerPoint (Lesson 33), build a client-ready proposal deck for ClearView based on your research. Apply the voice and structure from the Skill you created. The output should look like something you'd actually send to a client
3. **Agent handoff** — Set up a Cowork task or n8n workflow that automates at least one repeating step in this pipeline — either the research trigger, the document generation, or a follow-up task (such as drafting a follow-up email when the proposal is complete)

**Your deliverable:** A proposal document that looks client-ready, produced in under 30 minutes of active work — plus at least one automated step that would run without your involvement on the next engagement.

**Advanced extension:** Build a second agent that takes the completed proposal and drafts a personalized outreach email to the prospective client — pulling their name, company, and engagement focus from the brief — and stages it in Gmail via Zapier MCP, ready to send with one click.

> **Integration note:** The pattern here — brief → research → document → outreach — is the same workflow that runs inside every professional services firm, law practice, and consulting engagement. The Operator who can compress this from a week to a morning is not competing on hours. They're competing on a different playing field entirely.
