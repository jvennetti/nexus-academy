# NEXUS OPEN — Environment Handoff Bible

> **This document is for the Claude Code session that has access to BOTH `jvennetti/nexus-academy` AND `jvennetti/nexus-open`.  
> Read this file at the start of every session. It is the full context for the nexus-open initiative.**

---

## CRITICAL RULE — READ FIRST

**NEVER push to or modify `jvennetti/nexus-academy`. That repo is a completed, private product.**  
All work in this environment goes to `jvennetti/nexus-open` only.  
You may READ nexus-academy freely as a reference. You may NEVER write to it.

---

## 1. What Is Nexus Academy?

`jvennetti/nexus-academy` is a private, static HTML/CSS/JS course site hosted on GitHub Pages. It teaches AI literacy and automation skills. The site has:

- A pre-course intro (animated CIRO boot sequence)
- 6 modules with lessons, intros, and completion pages
- A machine activation sequence (the "finale")
- A bonus vault
- Per-operator progress tracking via localStorage
- Three named operators: Joshua, Allen, Connor — each with their own hub page and locked content
- CIRO: an AI character (SVG robot) who speaks throughout the course

The site is **complete and deployed**. No changes are needed or wanted there.

---

## 2. What Is Nexus Open?

`jvennetti/nexus-open` is a **public** version of the same course, rebuilt for general use — family members and anyone with the link.

Key differences from nexus-academy:
- **Single operator**: no names. All references to Joshua / Allen / Connor → "Operator"
- **One hub page**: `hub-operator.html` (replaces hub-joshua/allen/connor.html)
- **One password**: `76xJFp*w!W3*`
- **Per-device progress**: same localStorage architecture, but with `operator` as the slug instead of a person's name
- **No inside jokes**: "Grace sons" and "Predestined to" and the three-operator lore are removed from CIRO's dialogue
- **Machine activation narrative**: rewritten for a single anonymous operator (not three named ones)
- **Reset button**: hidden by default — reveal via a key combo (not visible on screen)
- **Repo is public**: family members access it via GitHub Pages URL

---

## 3. Repository Layout

In this environment, you have access to two repos. Their expected local paths:

| Repo | Local path | Purpose |
|---|---|---|
| `jvennetti/nexus-academy` | `/home/user/nexus-academy` | Source of truth — READ ONLY |
| `jvennetti/nexus-open` | `/home/user/nexus-open` | All development goes here |

> If the paths differ, adjust accordingly. Never assume — `ls /home/user/` to confirm.

---

## 4. Operator Constants

| | nexus-academy | nexus-open |
|---|---|---|
| Operators | `joshua`, `allen`, `connor` | `operator` |
| Hub pages | `hub-joshua.html`, `hub-allen.html`, `hub-connor.html` | `hub-operator.html` |
| Password | `77POWER`, `11WIND44`, `2FIRE22` | `76xJFp*w!W3*` |
| localStorage key prefix | `nexus_<op>` | `nexus_operator` |
| Intro seen key | `nexus_intro_seen_<op>` | `nexus_intro_seen_operator` |
| Hub visited key | `nexus_hub_visited_<op>` | `nexus_hub_visited_operator` |
| Last page key | `nexus_last_page_<op>` | `nexus_last_page_operator` |
| Current operator key | `nexus_current_operator` | `nexus_current_operator` (value: `'operator'`) |
| Machine activated key | `nexus_machine_activated` | `nexus_machine_activated` (shared, same as nexus-academy) |

In nexus-open JavaScript files, set:
```javascript
const OPERATOR = 'operator';
const OPERATOR_NAME = 'Operator';
const PASSCODE = '76xJFp*w!W3*';
```

---

## 5. File Structure — What to Copy, What to Change

### Copy directly (no changes):
```
audio/                     # All music and SFX — identical
images/                    # All images — identical
nexus-transition.js        # Root-level — identical
pre-course/module-intro.html
all module-*/lesson-*.html   # Lesson content — identical (no CIRO dialogue)
all module-*/challenge.html
all module-*/intermission.html
```

### Copy and adapt (structural changes):
```
hub-joshua.html  →  hub-operator.html      (OPERATOR/NAME/PASSCODE constants, no multiple hubs)
pre-course/ciro-intro.html                 (change CIRO boot dialogue — see §6)
pre-course/complete.html                   (no changes needed — generic)
module-1/intro.html through module-6/intro.html   (CIRO dialogue — see §6)
module-1/complete.html through module-6/complete.html  (CIRO dialogue — see §6)
machine/input.html                         (single operator entry — no name shown)
machine/activated.html                     (boot log + CIRO final speech — see §6)
bonus/vault.html                           (no operator-specific content — copy directly)
404.html                                   (copy directly)
```

### Create new (doesn't exist in nexus-academy):
```
index.html    # Entry point redirect or landing — probably redirect to pre-course/ciro-intro.html?op=operator
```

### Delete / do not create:
```
hub-allen.html   — not needed
hub-connor.html  — not needed
```

---

## 6. CIRO Dialogue — FINAL APPROVED TEXT

**SOURCE OF TRUTH:** `nexus-academy/_dev/ciro-messages-final.md`

Read that file in full. It contains the complete, finalized CIRO dialogue for every page in nexus-open — no edits needed, no decisions to make. Copy the lines into the HTML files exactly as written.

The `[PERSONAL]` and `[LORE]` examples in earlier drafts of this bible are **superseded** by that file. Ignore them and use `ciro-messages-final.md` instead.

### Story arc summary

The whole story spine is three beats around the word "Nexus":
1. Intro: CIRO finds the embedded word "Nexus" — doesn't know what it means
2. Recovered message: The contact embedded it as permission; they don't know what it means either
3. Final transmission: A nexus is a binding point between two things that couldn't reach each other alone — the operator and the system

That's the whole story. Single operator. No three-operator framing. No antagonist named. Clean and self-contained.

---

## 7. Reset Button — Key Combo

In nexus-academy, the reset button is visible but low-opacity. In nexus-open, hide it entirely and reveal only on a key combo.

Suggested implementation — in `hub-operator.html`:
```javascript
// Hidden reset — reveal on Shift+Alt+R (or choose another combo)
document.addEventListener('keydown', function(e) {
  if (e.shiftKey && e.altKey && e.key === 'R') {
    var btn = document.querySelector('.reset-btn');
    if (btn) btn.style.display = btn.style.display === 'block' ? 'none' : 'block';
  }
});
```

And in CSS, set `.reset-btn { display: none; }` instead of visible.

The reset modal text should NOT say "start over" — use phrasing like "clear your progress" or "reset your session."

---

## 8. Hub Music — Random Start Point

Implemented in nexus-academy and should be copied exactly to nexus-open.  
The `hub-theme.mp3` track is ~3m 56s at 320kbps.  
Three modes (random each page load):
- Mode 0: 0:00 — plays immediately at full volume, no fade
- Mode 1: 1:45 (105s, hardcoded) — 3-second fade-in
- Mode 2: ~2:37 (157s) — 3-second fade-in

The JS block for this is in the hub files (and vault/activated) — copy it directly.

---

## 9. Key Technical Conventions (copy from nexus-academy)

- All progress stored in localStorage, namespaced per operator:
  `nexus_intro_seen_operator`, `nexus_hub_visited_operator`, `nexus_last_page_operator`
- `nexus_current_operator` = `'operator'` (always)
- `nexus_machine_activated` — shared device-level key (same as nexus-academy behavior)
- Timestamps tracked as `nexus_ts_operator<pathname>`
- Pages in subdirectories use `../` to reference root assets
- Hub page and root files reference assets without `../`
- All nav links to hub resolve via `localStorage.getItem('nexus_current_operator')` → `hub-operator.html`
- `DEV_UNLOCK` must always remain `false`
- nexus-transition.js stays at root — uses `currentScript.src` for audio paths (do not move it)

---

## 10. Audio Files

All audio in nexus-academy carries over unchanged to nexus-open:

```
audio/music/hub-theme.mp3          # Hub background music (random start — see §8)
audio/music/ciro-intro.mp3         # CIRO intro sequence music
audio/music/machine-ambient.wav    # Machine section ambient (Web Audio API loop)
audio/sfx/password-confirm.mp3     # UI confirmation sound
audio/sfx/power-on-1/2/3.mp3      # Power-on SFX (picked randomly)
audio/sfx/transition-1/2/3.wav    # Page transition SFX
audio/sfx/decrypting-noise.wav    # Machine input page ambient (5% vol, 5–9s first, then 20–50s)
audio/sfx/short-success.wav       # Module/badge success
```

---

## 11. Development Workflow

```bash
# Always confirm you're working in nexus-open:
cd /home/user/nexus-open

# Development branch (create if it doesn't exist):
git checkout -b claude/<branch-name>

# After changes:
git add <files>
git commit -m "description"
git push -u origin claude/<branch-name>

# Create PR → squash merge to main (auto-authorized)
# Never push to nexus-academy
```

Merge policy: after every push to the dev branch, create a PR and squash merge to `main` immediately. Same as nexus-academy workflow.

---

## 12. What's Already Done (in nexus-academy, for reference)

These features exist in nexus-academy and should be copied into nexus-open:

- ✅ CIRO head tilt idle animations (SVG `<g id="ciro-head">`, CSS transform, JS IIFE)
- ✅ CIRO idle status messages — 3 rotating options, cycle starts at 1m/5m/7m then every 10m
- ✅ Reset confirmation modal (styled, replaces browser confirm())
- ✅ Sound design on reset modal (password-confirm on open/cancel, power_on on confirm)
- ✅ Machine ambient ↔ hub music coexistence (machine amb at 0.126 vol, hub stays at full)
- ✅ Decrypting noise on machine/input.html (5% vol, first at 5–9s, then 20–50s recurring)
- ✅ Hub music random start (3 modes, 3s fade on modes 1 and 2)
- ✅ Red loading screen on RESTORE click (machineRestoreTransit — instant overlay, no blue bleed)
- ✅ nexus-transition.js shared across all pages (black overlay, progress bar, sounds)
- ✅ Passcode section: "⚡ Passcode Transmission — Amber Channel"

---

## 13. Pending / Still To Do for nexus-open

- [x] CIRO dialogue finalized (see `_dev/ciro-messages-final.md`)
- [ ] Set up nexus-open repo structure (copy files from nexus-academy)
- [ ] Create `hub-operator.html` from `hub-joshua.html` (swap OPERATOR constants, hide reset btn)
- [ ] Apply CIRO dialogue from `ciro-messages-final.md` to all relevant pages
- [ ] Apply rewritten boot log, recovered message, and CIRO final transmission to `machine/activated.html`
- [ ] Add Shift+Alt+R key-combo reveal for reset button
- [ ] Create `index.html` entry point (likely a redirect to `pre-course/ciro-intro.html?op=operator`)
- [ ] Test full flow: ciro-intro → hub → pre-course → modules → machine → vault
- [ ] Confirm no "Operator Operator" double-naming anywhere

---

*This file lives at `nexus-academy/_dev/nexus-open-bible.md`.  
The new Claude Code environment can read it from the nexus-academy repo.*
