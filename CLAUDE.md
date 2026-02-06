# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **Slidev presentation** for a workshop titled "From Vibecoding to Sustainable Development." It teaches non-engineers (PPC/marketing professionals) how to move from ad-hoc AI-assisted coding to structured development practices (git flow, documentation-first planning, security basics, data persistence).

The repository serves dual purposes:
1. **The slides themselves** (`slides.md`) — a Slidev deck presented to the audience
2. **Workshop reference docs** (`docs/`) — planning materials, proposal methodology documentation, and templates used during the workshop

## Commands

- `npm run dev` — Start Slidev dev server with hot reload (opens browser)
- `npm run build` — Build static SPA to `dist/`
- `npm run export` — Export slides to PDF

## Architecture

**Slidev framework** (sli.dev) — presentations are written in Markdown with Vue component support.

- `slides.md` — Main presentation entry point. Uses `seriph` theme. Slides are separated by `---`. Frontmatter per slide controls layout, transitions, and classes.
- `pages/` — Additional slide files imported via `src:` attribute in `slides.md`
- `components/` — Vue SFC components usable directly in slides (e.g., `<Counter />`)
- `snippets/` — TypeScript code snippets embedded in slides via `<<< @/snippets/external.ts#snippet`
- `docs/` — Workshop planning and methodology docs (not part of the slide deck itself)

### Proposal System (from `docs/`)

The `docs/` directory contains a **proposal-first methodology** adapted from a separate project (Kraken API). Key pieces:

- `docs/proposals/.template.md` — Canonical proposal template with required sections (Problem, Solution, Implementation Plan, Alternatives, Trade-offs, Review Questions, Changelog)
- `docs/proposals/index.md` — Registry of all proposals with status tracking
- `docs/proposals/posts/` — Individual proposal files named `ip-XXX-title.md`
- `docs/IMPLEMENTATION_PROPOSALS.md` — Full methodology description including AI-agent workflow and Review Questions protocol

**Review Questions protocol**: When an AI agent creates a proposal, it must self-review and generate structured questions (Priority/Issue/Context/Question/Options) for human sign-off before implementation.

### Deployment

Configured for both **Netlify** (`netlify.toml`) and **Vercel** (`vercel.json`). Both build with `npm run build` and serve from `dist/`. Node 20 required.

## Proposal Writing Rules

- No time estimates in proposals
- Always update the changelog on every change
- Always update `docs/proposals/index.md` when creating or changing proposal status
- AI-generated proposals must include the Review Questions section
- Use status emoji in the index: Draft, Under Review, Accepted, Implemented, Rejected, Superseded