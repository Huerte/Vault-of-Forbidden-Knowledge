# IT & Games Knowledge Hub

Centralized personal knowledge base for IT work, software development, gaming, apps, and general tech notes.

## Directory Structure

```text
/
├── docs/               <- Structured how-to guides and technical write-ups
│   ├── it-fundamentals/
│   │   ├── networking/
│   │   ├── operating-systems/
│   │   ├── hardware/
│   │   └── security-privacy/
│   ├── programming-dev/
│   │   ├── languages/
│   │   ├── version-control/
│   │   ├── ci-cd/
│   │   ├── databases/
│   │   └── frameworks/
│   └── games/
│       ├── server-hosting/
│       ├── modding/
│       ├── emulation/
│       ├── troubleshooting/
│       └── dev-tools/
│
├── apps/               <- Notes and guides for specific applications and tools
│   ├── cli/
│   ├── gui/
│   ├── developer/
│   ├── it/
│   ├── engineering/
│   ├── office/
│   ├── gaming/
│   ├── productivity/
│   ├── browser-extensions/
│   └── misc/
│
├── cheatsheets/        <- One-page quick reference cards
│
├── logs/               <- Dated troubleshooting and incident entries
│
├── notes/              <- Random personal tips, tricks, and miscellaneous stuff
│   ├── phone-tips/
│   ├── app-tricks/
│   ├── file-conversion/
│   ├── browser-tricks/
│   ├── subscriptions/
│   ├── media-apps/
│   ├── productivity-hacks/
│   └── random-howtos/
│
├── assets/
│   ├── images/         <- Mirrors the above structure exactly
│   ├── diagrams/
│   └── gifs/
│
├── templates/
├── README.md
├── CONTRIBUTING.md
└── .gitignore
```

## Section Breakdown

### [docs](docs/)
Pure structured how-to guides and technical documentation. If you're writing step-by-step instructions, it goes here.

- **it-fundamentals/**: Networking, OS setup, hardware, security, and privacy basics.
- **programming-dev/**: Languages, version control, CI/CD, databases, and frameworks.
- **games/**: Dedicated server hosting, modding, emulation, troubleshooting, and game dev tools.

### [apps](apps/)
Notes and configuration guides tied to a specific application or tool. Not a general how-to but rather setup, config, and usage notes for individual software.

- **cli/**: Command line utilities.
- **gui/**: Desktop GUI applications.
- **developer/**: IDEs, code editors, API clients, and programming utilities.
- **it/**: Network scanners, VM managers, terminal emulators, and sysadmin software.
- **engineering/**: CAD, circuit design, simulation, and other engineering software.
- **office/**: Word processors, spreadsheets, and presentation software.
- **gaming/**: Game launchers, mod managers, and game-specific client utilities.
- **productivity/**: Note-taking apps, task trackers, and desktop automation tools.
- **browser-extensions/**: Browser extension setups and configurations.
- **misc/**: Anything that does not fit the above categories.

### [cheatsheets](cheatsheets/)
Single-page quick reference cards for frequently used commands, syntax, and shortcuts. No prose, just reference.

Examples: Git commands, Linux CLI, Docker, Regex, keyboard shortcuts.

### [logs](logs/)
Dated entries for one-off bugs, errors, and incidents. Written after the fact once the issue is resolved. Format: `YYYY-MM-DD-short-description.md`.

### [notes](notes/)
Informal personal notes, tips, and tricks that do not fit structured documentation.

- **phone-tips/**: Android and iOS tricks, storage cleanup, battery tips.
- **app-tricks/**: Hidden features and useful settings in apps.
- **file-conversion/**: Format conversion tools, compression, batch renaming.
- **browser-tricks/**: Browser configs, tab management, dev tools shortcuts.
- **subscriptions/**: Free tier tracking, trial dates, account hygiene.
- **media-apps/**: Download quality settings, offline mode, region tips.
- **productivity-hacks/**: Workflow shortcuts, keyboard remaps, automation scripts.
- **random-howtos/**: Catch-all for anything else.

## Assets and Images

Every guide that has screenshots stores its images in `assets/images/` using the same path as the guide itself. The subfolder name matches the guide filename exactly.

```text
Guide:  docs/programming-dev/databases/setup-postgresql.md
Images: assets/images/docs/programming-dev/databases/setup-postgresql/
        ├── 01-dashboard.png
        ├── 02-env-vars.png
        └── 03-success.png
```
