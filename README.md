<div align="center">

# Vault of Forbidden Knowledge

<p align="center">
  <img src="assets/gifs/hellmo-forbidden-knowledge.gif" alt="Welcome Banner">
</p>

[![Knowledge Base](https://img.shields.io/badge/Knowledge%20Base-Active-blue.svg)](#)
[![Platform](https://img.shields.io/badge/platform-Cross--Platform-blueviolet.svg)](#)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Stars](https://img.shields.io/github/stars/Huerte/Vault-of-Forbidden-Knowledge?style=flat&color=e3b341)](https://github.com/Huerte/Vault-of-Forbidden-Knowledge/stargazers)
[![Good First Issues](https://img.shields.io/github/issues/Huerte/Vault-of-Forbidden-Knowledge/good%20first%20issue?color=7057ff&label=good%20first%20issues)](https://github.com/Huerte/Vault-of-Forbidden-Knowledge/issues?q=is%3Aopen+label%3A%22good+first+issue%22)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

**Centralized personal knowledge base for IT work, software development, gaming, general tech notes, and random stuff.**

[Good First Issues](https://github.com/Huerte/Vault-of-Forbidden-Knowledge/issues?q=is%3Aopen+label%3A%22good+first+issue%22) · [Request a Guide](https://github.com/Huerte/Vault-of-Forbidden-Knowledge/issues/new/choose) · [Report a Problem](https://github.com/Huerte/Vault-of-Forbidden-Knowledge/issues/new/choose) · [Star this repo](https://github.com/Huerte/Vault-of-Forbidden-Knowledge)

</div>

---

<p align="center">
  Welcome to the Vault of Forbidden Knowledge. This is a single repository serving as the second brain for everything from complex IT troubleshooting to simple commands we keep forgetting.
</p>

---

## New Here? Start With a Good First Issue

You do not need to write code. Pick something small, comment on the issue, and open a pull request.

| Time | What you can do | Where to start |
|---|---|---|
| 2 to 5 min | Fix a typo, share a tip, report a broken link | [time: 5 min](https://github.com/Huerte/Vault-of-Forbidden-Knowledge/issues?q=is%3Aopen+label%3A%22time%3A+5+min%22) |
| 10 to 15 min | Proofread a guide, add a cheatsheet, log an error you fixed | [time: 15 min](https://github.com/Huerte/Vault-of-Forbidden-Knowledge/issues?q=is%3Aopen+label%3A%22time%3A+15+min%22) |
| 20+ min | Write a new guide | [write a guide](https://github.com/Huerte/Vault-of-Forbidden-Knowledge/issues?q=is%3Aopen+label%3A%22write+a+guide%22) |

All beginner-friendly tasks: [good first issues](https://github.com/Huerte/Vault-of-Forbidden-Knowledge/issues?q=is%3Aopen+label%3A%22good+first+issue%22). Never opened a pull request? Try [First Contributions](https://github.com/firstcontributions/first-contributions).

If the vault saves you time, a [star](https://github.com/Huerte/Vault-of-Forbidden-Knowledge) helps other people find it.

---

## Table of Contents

- [New Here?](#new-here-start-with-a-good-first-issue)
- [Navigation](#navigation)
- [Repository Structure](#repository-structure)
- [docs](#docs)
- [cheatsheets](#cheatsheets)
- [logs](#logs)
- [notes](#notes)
- [templates](#templates)
- [Contributing](#contributing)
- [Contributors](#contributors)
- [License](#license)

---

## Navigation

| Section | Description |
|---|---|
| [docs](#docs) | Structured how-to guides and technical write-ups |
| [cheatsheets](#cheatsheets) | One-page quick reference cards |
| [logs](#logs) | Dated troubleshooting and incident entries |
| [notes](#notes) | Random personal tips, tricks, and miscellaneous stuff |
| [templates](#templates) | Standardized templates for creating new guides and entries |
| [Adding screenshots](#adding-screenshots-and-images) | How images are stored for each guide |

---

## Repository Structure

```text
Vault-of-Forbidden-Knowledge/
├── docs/          Step-by-step guides
│   ├── programming-dev/   languages, version-control, databases, frameworks, ci-cd
│   ├── it-fundamentals/   hardware, networking, operating-systems, security-privacy
│   └── games/             game guides and server setups
├── cheatsheets/   One-page quick references
├── logs/          Dated bug and fix entries
├── notes/         Short tips and tricks
├── templates/     Starting points for new files
└── assets/        Images, GIFs, and diagrams used by the docs
```

---

## [docs](docs/)

Pure structured how-to guides and technical documentation. Step-by-step instructions live here.

<details>
<summary><strong><a href="docs/programming-dev/">programming-dev/</a></strong>: Languages, version control, CI/CD, databases, and frameworks</summary>

<br>

<details>
<summary><a href="docs/programming-dev/databases/">databases/</a></summary>

- [Finding PostgreSQL Port](docs/programming-dev/databases/Postgres/port/finding-port.md)
- [Reset PostgreSQL Password (Windows Script)](docs/programming-dev/databases/Postgres/reset-password/reset_pg_pas-windows.bat)
- [Backup and Restore PostgreSQL with pg_dump](docs/programming-dev/databases/Postgres/backup-and-restore/pg-dump-guide.md)

</details>

<details>
<summary><a href="docs/programming-dev/version-control/">version-control/</a></summary>

- [Git Commands Survival Kit](docs/programming-dev/version-control/git-commands-survival-kit.md)
- [Undoing Things in Git (Restore, Reset, Revert)](docs/programming-dev/version-control/undoing-things-in-git.md)

</details>

</details>

<details>
<summary><strong><a href="docs/games/">games/</a></strong>: Game guides, server hosting, modding, and game-specific notes</summary>

<br>

<details>
<summary><a href="docs/games/The%20Forest/">The Forest/</a></summary>

- [Set Up Offline LAN Multiplayer in The Forest](docs/games/The%20Forest/offline-lan-multiplayer-guide.md)

</details>

</details>

<details>
<summary><strong><a href="docs/it-fundamentals/">it-fundamentals/</a></strong>: Hardware, networking, OS, and security</summary>

<br>

<details>
<summary><a href="docs/it-fundamentals/hardware/">hardware/</a></summary>

- [Identifying Real PC Specs (dxdiag & msinfo32)](docs/it-fundamentals/hardware/identifying-real-pc-specs.md)

</details>

<details>
<summary><a href="docs/it-fundamentals/networking/">networking/</a></summary>

- [Diagnosing a No-Internet Connection on Windows](docs/it-fundamentals/networking/diagnosing-no-internet-connection.md)
- [Find Your Local IP Address on Windows](docs/it-fundamentals/networking/find-local-ip-windows.md)
- [Common Network Ports Reference](docs/it-fundamentals/networking/common-ports-reference.md)

</details>

<details>
<summary><a href="docs/it-fundamentals/operating-systems/">operating-systems/</a></summary>

- [Windows Environment Variables: Management and PATH Guide](docs/it-fundamentals/operating-systems/windows-environment-variables.md)
- [Understanding Windows Path Variables and System Directories](docs/it-fundamentals/operating-systems/understanding-windows-paths.md)

</details>

<details>
<summary><a href="docs/it-fundamentals/security-privacy/">security-privacy/</a></summary>

- [SSH Key Pair Generation and Setup on Windows](docs/it-fundamentals/security-privacy/ssh-key-setup-windows.md)
- [Turn On Two-Factor Authentication for GitHub](docs/it-fundamentals/security-privacy/enable-github-2fa.md)

</details>

</details>

---

## [cheatsheets](cheatsheets/)

Single-page quick reference cards for frequently used commands, syntax, and shortcuts.

- [Git Command Cheatsheet](cheatsheets/git-cheatsheet.md)
- [Windows CMD vs PowerShell Cheatsheet](cheatsheets/windows-cmd-powershell.md)

---

## [logs](logs/)

Dated entries for one-off bugs, errors, and incidents.

*No active entries yet.*

---

## [notes](notes/)

Informal personal notes, tips, and tricks that do not fit structured documentation.

*No active entries yet.*

---

## [templates](templates/)

Standardized template Markdown files for adding new content to the repository.

<details>
<summary><strong><a href="templates/">templates/</a></strong>: Templates for guides, tool entries, and troubleshooting</summary>

<br>

- [Guide Template](templates/guide-template.md)
- [Tool Entry Template](templates/tool-entry-template.md)
- [Troubleshooting Template](templates/troubleshooting-template.md)

</details>

---

## Contributing

Contributions are welcome, and you do not need to write code. Browse the [good first issues](https://github.com/Huerte/Vault-of-Forbidden-Knowledge/issues?q=is%3Aopen+label%3A%22good+first+issue%22), read the [Contributing Guide](CONTRIBUTING.md), and be kind ([Code of Conduct](CODE_OF_CONDUCT.md)). Here is how to go from zero to a submitted pull request.

### Getting Started

**Prerequisites:** Git.

**Fork and clone:**

```
# 1. Fork the repo on GitHub, then clone your fork
git clone https://github.com/YOUR_USERNAME/Vault-of-Forbidden-Knowledge.git
cd Vault-of-Forbidden-Knowledge

# 2. Keep your fork in sync with the original
git remote add upstream https://github.com/Huerte/Vault-of-Forbidden-Knowledge.git
```

### Making Changes

**Branch naming:**

```
feat/short-description    # New guides or sections
fix/short-description     # Corrections to existing guides
docs/short-description    # Meta documentation
chore/short-description   # Repository maintenance
```

**Commit messages:** Use plain English. Describe what changed and why:

```
# Good
git commit -m "feat: add guide for finding postgres port"
git commit -m "fix: correct typo in ngrok setup command"
git commit -m "chore: reorganize assets folder"

# Avoid
git commit -m "fix stuff"
git commit -m "update notes"
```

**Content style:**

- Use the provided templates in the `templates/` directory.
- Keep guides concise and straightforward.
- Add screenshots when the process is not immediately obvious.

### Adding Screenshots and Images

Every guide that has screenshots stores its images in `assets/images/` using the same path as the guide itself. The subfolder name matches the guide filename exactly.

```text
Guide:  docs/programming-dev/databases/setup-postgresql.md
Images: assets/images/docs/programming-dev/databases/setup-postgresql/
        ├── 01-dashboard.png
        ├── 02-env-vars.png
        └── 03-success.png
```

### Submitting a Pull Request

1. Push your branch to your fork:
   ```
   git push origin feat/your-feature
   ```

2. Open a Pull Request against `Huerte/Vault-of-Forbidden-Knowledge:main` on GitHub.

3. In the PR description, briefly explain: what you added or changed, and why it's useful.

---

## Contributors

Thanks to everyone who helps this collection grow.

<a href="../../graphs/contributors">
  <img src="https://contrib.rocks/image?repo=Huerte/Vault-of-Forbidden-Knowledge" alt="Contributors">
</a>

Want to see your face here? Pick a [good first issue](https://github.com/Huerte/Vault-of-Forbidden-Knowledge/issues?q=is%3Aopen+label%3A%22good+first+issue%22). If you like the project, a [star](https://github.com/Huerte/Vault-of-Forbidden-Knowledge) is appreciated but never required.

---

## License

Distributed under the **MIT** License. See [`LICENSE`](LICENSE) for details.

---

## To Whoever Inherits This Mess

<div align="center">
  <img src="assets/gifs/una.gif" alt="May odds in your favor">
</div>
