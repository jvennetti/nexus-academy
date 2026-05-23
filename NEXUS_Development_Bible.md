# 📡 NEXUS ACADEMY — HTML DEVELOPMENT BIBLE
### Version 1.0
### Paste this document at the top of every Claude Code session.

---

## PART 1 — PROJECT OVERVIEW

**School Name:** NEXUS Academy
**Tagline:** *Become the Operator.*
**Hosted at:** `jvennetti.github.io/nexus-academy/`
**Repository:** `jvennetti/nexus-academy`
**Deploy:** GitHub Pages → Settings → Pages → Source: main branch
**Stack:** Native HTML / CSS / JS only. No frameworks. No embedding required.

**Three Operators. Three personal hubs. One shared Machine.**

| Operator | Hub File | Passcode |
|---|---|---|
| Joshua | hub-joshua.html | `77POWER` |
| Connor | hub-connor.html | `2FIRE22` |
| Allen | hub-allen.html | `11WIND44` |

Hub pages are accessed by direct URL — no login. Privacy is honor-system. The only page all three share is `machine.html`.

---

## PART 2 — COLOR PALETTE & VISUAL SYSTEM

### Base Palette

| Role | Hex |
|---|---|
| Body (CIRO / dark backgrounds) | Deep navy |
| Joints / secondary elements | Cool grey |
| Primary accent — electric blue | `#00c8ff` |
| Passcode delivery accent — amber | `#ffaa00` |
| Warning light — yellow | `#ffcc00` |
| Crisis light — red | `#ff4444` |

### CIRO's Light System (Three Chest Dots)

| State | Color | Pulse Speed | When Used |
|---|---|---|---|
| Normal | `#00c8ff` (electric blue) | Slow, calm | Default everywhere throughout the course |
| Warning | `#ffcc00` (yellow) | Medium | Whenever mentioned in CIRO's script |
| Crisis | `#ff4444` (red) | Fast | Whenever mentioned in CIRO's script |
| Passcode | `#ffaa00` (amber) | Steady glow | Module 6 complete.html passcode delivery widget only |

**Rule:** Blue is the default for every widget across the entire course. The only places where yellow or red appear are when specifically mentioned in CIRO's script.

### CIRO's Appearance (SVG)

Compact, angular robot. Transmission panel screen where a face would be. Clean geometric forms. Three chest indicator dots reflect the light system above. Deep navy body, cool grey joints, electric blue accents.

**Lesson pages:** CIRO is text-only on lesson pages — no SVG widget. His transmission header is styled text only.

---

## PART 3 — PAGE TYPES & STRUCTURE

Every module contains exactly these page types:

### 1. `intro.html` — Module Intro Page
- CIRO animated text transmission widget (see ALL CIRO MESSAGES doc for exact text)
- Midjourney art image (module-specific, stored in `assets/images/`)
- Brief CIRO welcome message
- Link/button to the first lesson of the module
- **Module 1 only:** Full CIRO story animation with white → yellow → red → blue light sequence
- **Modules 2–6:** Shorter transmission, blue lights only (Module 4 may include optional yellow flicker per the CIRO Messages doc)

### 2. `lesson-X-X.html` — Individual Lesson Pages (one per video)
- CIRO transmission header — styled text only, no widget
- Lesson context copy (pre-written — paste directly)
- YouTube video embed (iframe)
- **Timestamp Saver widget** — inline, directly below the video — for any lesson with a video over 15 minutes. localStorage-backed, keyed to lesson URL. Clears on module completion.
- Key Takeaways (bullets)
- Prev / Next navigation

### 3. `challenge.html` — Module Challenge Page
- Full-width 4×2 banner image (Midjourney, module-specific, stored in `assets/images/`)
- Challenge copy (pre-written — paste directly)
- "Mark Complete" button → routes to `complete.html`

### 4. `complete.html` — Module Completion Page
- CIRO completion message (from CIRO Messages doc)
- Badge graphic (SVG, stored in `assets/badges/`)
- Badge delivery line (from CIRO Messages doc)
- Routes to next module intro (or hub if end of course)
- **Module 6 only:** After completion message, passcode delivery widget appears in amber transmission style (operator-specific), followed by a button linking to `machine.html`

### 5. `hub-[name].html` — Personal Operator Hub (×3)
- Welcome message from CIRO
- Progress bar
- "Continue" button routing to current position
- Module cards with Midjourney art as card background
- LOCKED overlay on locked modules / UNLOCKED state on completed ones
- Badge display area
- Module locking tracked via browser localStorage (scoped to GitHub Pages domain)
- Progress persists across sessions on same device
- Hub visual language: established in existing `hub-joshua.html`
- MACHINE visual (designed with HTML) is located at the bottom of the page. A large, complex machine. A button says "ACTIVATE" which leads you to 'machine.html' with three passwords and "ACTIVATE" button. Until the Operators get all passwords, they cannot proceed past this page.

### 6. `machine.html` — The Machine (shared)
- Three passcode input fields (one per Operator)
- Passcodes embedded in HTML: Joshua=`77POWER`, Connor=`2FIRE22`, Allen=`11WIND44`
- All three must be entered correctly simultaneously to activate
- Button below the password entries says "ACTIVATE"
- On activation: ending sequence plays (VANTA contact message, then CIRO final transmission), approximately 90 seconds, cannot be skipped
- During CIRO's final transmission: full light cycle active in real time — lights shift as he processes, pause during uncertainty, resolve as each piece lands.
- Full ending text is in the CIRO Messages doc, Part 11

---

## PART 4 — COMPLETE FILE STRUCTURE

```
jvennetti/nexus-academy/
│
├── hub-joshua.html
├── hub-connor.html
├── hub-allen.html
├── machine.html
│
├── pre-course/
│   ├── intro.html          ← Full story animation (white→yellow→red→blue)
│   ├── lesson-0-1.html
│   ├── lesson-0-2.html
│   ├── challenge.html
│   └── complete.html
│
├── module-1/
│   ├── intro.html
│   ├── lesson-1-1.html
│   ├── lesson-1-2.html
│   ├── lesson-1-3.html
│   ├── lesson-1-4.html
│   ├── challenge.html
│   └── complete.html
│
├── module-2/
│   ├── intro.html
│   ├── lesson-2-1.html
│   ├── lesson-2-2.html
│   ├── lesson-2-3.html
│   ├── lesson-2-4.html
│   ├── lesson-2-5.html
│   ├── lesson-2-6.html
│   ├── lesson-2-7.html
│   ├── challenge.html
│   └── complete.html
│
├── module-3/
│   ├── intro.html
│   ├── lesson-3-1.html
│   ├── lesson-3-2.html
│   ├── lesson-3-3.html
│   ├── lesson-3-4.html
│   ├── lesson-3-5.html
│   ├── lesson-3-6.html
│   ├── lesson-3-7.html
│   ├── lesson-3-8.html
│   ├── lesson-3-9.html
│   ├── lesson-3-10.html
│   ├── lesson-3-11.html
│   ├── lesson-3-12.html
│   ├── lesson-3-13.html
│   ├── lesson-3-14.html
│   ├── challenge.html
│   └── complete.html
│
├── module-4/
│   ├── intro.html
│   ├── lesson-4-1.html
│   ├── lesson-4-2.html
│   ├── lesson-4-3.html
│   ├── lesson-4-4.html
│   ├── lesson-4-5.html
│   ├── lesson-4-6.html
│   ├── lesson-4-7.html
│   ├── lesson-4-8.html
│   ├── challenge.html
│   └── complete.html
│
├── module-5/
│   ├── intro.html
│   ├── lesson-5-1.html
│   ├── lesson-5-2.html
│   ├── lesson-5-3.html
│   ├── lesson-5-4.html
│   ├── lesson-5-5.html
│   ├── lesson-5-6.html
│   ├── lesson-5-7.html
│   ├── challenge.html
│   └── complete.html
│
├── module-6/
│   ├── intro.html
│   ├── lesson-6-1.html
│   ├── lesson-6-2.html
│   ├── lesson-6-3.html
│   ├── lesson-6-4.html
│   ├── challenge.html
│   └── complete.html       ← Passcode delivery (amber) + link to machine.html
│
└── assets/
    ├── images/             ← Midjourney module art (one per module + 4×1 challenge banners)
    ├── badges/             ← SVG badge files
    └── css/                ← Shared stylesheets (if used)
```

---

## PART 5 — BADGE SYSTEM

| Badge Name | File | Trigger |
|---|---|---|
| SYSTEM ONLINE | `system-online.svg` | Complete Pre-Course |
| BOOT SEQUENCE COMPLETE | `boot-sequence-complete.svg` | Complete Module 1 |
| SIGNAL STEADY | `signal-steady.svg` | Complete Module 2 |
| COMMANDER | `commander.svg` | Complete Module 3 |
| ARCHITECT | `architect.svg` | Complete Module 4 |
| PIPELINE INVENTOR | `pipeline-inventor.svg` | Complete Module 5 |
| OPERATOR | `operator.svg` | Complete Module 6 |
| NEXUS *(grand badge — larger than all others)* | `nexus.svg` | Machine activated (all 3 codes + ending viewed) |

Badge delivery lines are in the CIRO Messages doc, Part 10.

---

## PART 6 — FUNCTIONAL REQUIREMENTS

### localStorage Keys (hub progress tracking)
- Module completion stored in localStorage, scoped to GitHub Pages domain
- Keys should be consistent and predictable (e.g., `nexus_module_precourse_complete`, `nexus_module_1_complete`, etc.)
- Hub reads these keys on load to render LOCKED / UNLOCKED states and progress bar
- Timestamp Saver keys scoped to lesson URL — cleared when module is marked complete

### Timestamp Saver Widget (inline, on lessons >15 min)
- Single text input (placeholder: e.g., "15:42 — where I stopped")
- Save button
- Display area showing last saved timestamp
- localStorage key: lesson URL or unique lesson ID
- Cleared when Operator marks module complete

### Machine Activation Logic
- Three input fields, one per Operator, labeled by name
- On submit: check all three codes simultaneously
- Correct: trigger ending sequence
- Incorrect: show error state, allow retry
- Ending sequence: cannot be skipped, ~90 seconds, animated line-by-line text delivery

### Module 6 Passcode Delivery
- Triggered when Operator clicks "Mark Complete" on Module 6 challenge
- Passcode widget appears in amber transmission style
- Each hub page has its own operator-specific passcode pre-built in the HTML
- After passcode, a button links to `machine.html`

---

## PART 7 — BUILD ORDER FOR CLAUDE CODE

Build in this sequence. Scope each session to one module.

1. Master lesson page template (from Claude Chat — design first, then hand off)
2. Master module intro template
3. Master challenge page template
4. Master complete page template
5. Generate all lesson HTML files from templates + lesson markdown content
6. Build `machine.html`
7. Clone `hub-joshua.html` → build `hub-connor.html` and `hub-allen.html`
8. Add badge SVGs to `assets/badges/`
9. Add Midjourney module art to `assets/images/`
10. Full navigation audit — verify every prev/next link
11. Deploy and test all three Operator URLs

**Start every Claude Code session by pasting this Bible.**
**Show one file before batch-generating the rest.**
**Claude Code can run `git add`, `git commit`, `git push` to deploy directly.**

---

## PART 8 — OPEN ITEMS

- [ ] GitHub Pages activated in repo settings (Settings → Pages → main branch)
- [ ] Master lesson page template built in Claude Chat
- [ ] Master module intro template built in Claude Chat
- [ ] Master challenge page template built in Claude Chat
- [ ] Master complete page template built in Claude Chat
- [ ] All lesson HTML files generated via Claude Code
- [ ] `hub-connor.html` and `hub-allen.html` built (clone Joshua's, update name + passcode)
- [ ] Badge SVGs designed and added to `assets/badges/`
- [ ] Midjourney module art added to `assets/images/`
- [ ] `machine.html` built and tested with all three codes
- [ ] Full navigation audit completed
- [ ] Confirm Pre-Course `complete.html` behavior — does it auto-unlock Module 1, or is Module 1 open by default?

---

*End of HTML Development Bible — Version 1.0*
