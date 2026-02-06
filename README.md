# From Vibecoding to Sustainable Development

[![CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

A 3-hour workshop that teaches non-engineers how to move from ad-hoc AI-assisted coding ("vibecoding") to structured, sustainable development practices.

**Live slides**: [sibyx.github.io/sustainable-vibecoding](https://sibyx.github.io/sustainable-vibecoding/)

## What the Workshop Covers

1. **Plan Before You Prompt** — PLAN.md, Implementation Proposals, Review Questions
2. **AI Toolkit** — Claude Code, Cursor, Google AI Studio, MCP
3. **Git & Collaboration** — Branching, pull requests, merge conflicts
4. **APIs & External Services** — How tools connect to the real world
5. **Security Basics** — .env files, secret management, what never goes in git
6. **Data Persistence** — From CSV files to databases

## Running Locally

```bash
npm install
npm run dev
```

## Building

```bash
npm run build    # Static SPA → dist/
npm run export   # PDF export
```

## Project Structure

- `slides.md` — Main presentation ([Slidev](https://sli.dev) framework)
- `docs/proposals/` — Implementation Proposals that designed these slides
- `docs/FACILITATOR_NOTES.md` — Detailed facilitator planning notes and timeline
- `docs/IMPLEMENTATION_PROPOSALS.md` — Full proposal methodology documentation

## License

This work is licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).

**Author**: Jakub Dubec ([@Sibyx](https://github.com/Sibyx))