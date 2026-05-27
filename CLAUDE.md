# NEXUS Academy — Claude Instructions

## Standing Permissions

- **Always merge after pushing.** After every push to the development branch, create a PR (if one doesn't exist) and immediately merge it to `main` via squash merge. Never wait for explicit merge approval — it is pre-authorized for all work in this repo.
- **Development branch:** `claude/modest-rubin-nzUzA`. Never push to a different branch without explicit instruction.
- **`DEV_UNLOCK` must always remain `false`.** Never change it to `true` under any circumstances.

## Repo Structure

```
nexus-academy/
├── hub-joshua.html         # Operator hub pages (source of truth: hub-joshua)
├── hub-allen.html
├── hub-connor.html
├── pre-course/             # Pre-course intro, module intro, lessons, complete
├── module-1/ … module-6/  # Lessons, challenge, intermission, intro, complete
├── machine/                # machine/input.html, machine/activated.html
├── bonus/                  # bonus/vault.html
├── audio/
│   ├── music/              # hub-theme.mp3, ciro-intro.mp3, machine-ambient.wav, etc.
│   └── sfx/                # power-on-1/2/3.mp3, short-success.wav, etc.
├── images/
├── nexus-transition.js     # Stays at root — uses currentScript.src for audio paths
├── 404.html
└── _dev/                   # Templates, docs, migration scripts (not deployed)
```

## Operators

| Operator | Password  | Hub page          |
|----------|-----------|-------------------|
| Joshua   | `77POWER` | `hub-joshua.html` |
| Allen    | `11WIND44`| `hub-allen.html`  |
| Connor   | `2FIRE22` | `hub-connor.html` |

Entry point for each: `pre-course/ciro-intro.html?op=<name>` (one-time animated intro, sets `nexus_intro_seen_<op>` in localStorage).

## Key Conventions

- All progress/state is namespaced per operator in localStorage: `nexus_intro_seen_<op>`, `nexus_hub_visited_<op>`, `nexus_last_page_<op>`.
- `nexus_current_operator` holds the active operator name (`joshua`/`allen`/`connor`).
- `nexus_machine_activated` is shared across operators (intentional).
- Pages in subdirectories (modules, machine/, bonus/, pre-course/) use `../` to reference root-level assets.
- Hub pages are at root and reference assets without `../`.
- All nav links to the hub are dynamic: resolve from `localStorage.getItem('nexus_current_operator')`.
- `hub-allen.html` and `hub-connor.html` are generated from `hub-joshua.html` — only operator constants differ. Keep all three in sync.
