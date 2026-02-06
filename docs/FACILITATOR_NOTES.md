# From Vibecoding to Sustainable Development

***

## High-Level Flow (Proposed Order)

1. Intro \& Information Gathering (questions, reality check)
2. Define the App \& Documentation‑First Plan
3. Tooling \& AI Assistants (Claude/Cursor/Google AI Studio, MCP, llms.txt)
4. Git \& Collaboration (git flow, merge requests, conflicts demo)
5. External Services \& APIs (how they actually plug into tools)
6. Data Persistence (from CSV/Parquet to real databases)
7. Security Basics (secrets, tokens, "don't paste this into ChatGPT")
8. QA \& Wrap‑up (their process going forward)

This order lets you:

- Start from **their current reality**
- Design **a plan for a real app**
- Then layer on **collaboration, APIs, data, and security** in context of that app.

***

## Detailed Timeline (3 Hours)

### 0. Welcome \& Information Gathering (15–20 min)

**Goal:** Understand how they currently vibe code, choose a simple shared app idea, and surface pain points.

**Format:** Interactive discussion, whiteboard / shared doc.

**Steps:**

- Quick intro: "Today is not about turning you into engineers, but about making your AI‑built tools less fragile and more shareable."
- Ask a few focused questions:
    - "Show/tell one internal thing you've built recently."
    - "What hurts the most when multiple people touch the same thing?"
    - "Where does your data usually come from? CSV exports? APIs? Kaggle datasets?"
    - "Have you ever lost work / broken something and had to start over?"
- Jointly pick **one simple app** to use for the whole session, e.g.:
    - "PPC performance dashboard that aggregates from X and Y"
    - "Tool that scores campaigns by efficiency and suggests priorities"
- Write down in 1–2 sentences what this app should do; keep it realistic and small.

Optional Kaggle hook:

- Mention Kaggle as a good source of **practice** datasets for experimenting, but prioritize **their real ad data / real APIs** for motivation.

***

### 1. Documentation‑First Plan for the App (25–30 min)

**Goal:** Show how writing a lightweight plan (in Markdown) before prompting AI massively improves results and collaboration.

**Format:** Live co‑creation of a `PLAN.md` / `IMPLEMENTATION_PROPOSAL.md`.

**Content:**

- Explain idea:
  "Before we throw prompts at Claude/Cursor, we create a small text file that clearly explains what we want. The AI becomes an implementer, not a mind reader."
- Live creation of a plan for the chosen app, e.g.:

```markdown
# Tool: Campaign Performance Helper

## Problem
- We have multiple ad accounts and platforms.
- Reporting is manual and repetitive.

## Goal
- One small tool that:
  - Fetches basic metrics from X and Y
  - Outputs a simple table + maybe some comments

## Data sources
- [List APIs or CSV exports we actually use]

## Rough flow
- Step 1: Get credentials safely (no hardcoding)
- Step 2: Fetch data for a given date range
- Step 3: Store data somewhere (file / db)
- Step 4: Show a summary

## Security notes
- Where API keys live
- What MUST NOT go into git

## Files we expect
- plan/PLAN.md
- src/main_script
- src/api_client
- data/ (for stored outputs)
```

- Show how this plan can be handed to Claude/Cursor:
    - "You are the implementer; here is the plan. Ask me questions if unclear."

This sets the structure that every later topic (git, APIs, security, data) will hook into.

***

### 2. Tooling \& AI Assistants (15–20 min)

**Goal:** Position Claude Code, Cursor, and Google AI Studio as tools in a **structured workflow**, not just "vibes".

**Format:** Short demo + discussion.

**Key points:**

- Show how **you** usually work:
    - Plan in Markdown.
    - Ask AI to propose file structure / implementation steps.
    - Iteratively refine the plan and code.
- Cursor:
    - Mention planning \& implementation phases (Composer, project‑wide edits).
    - Suggest creating a small project config / rules file to give context.
- Claude Code:
    - Good at multi‑file reasoning with `PLAN.md` front and center.
    - Encourage them to paste the plan, not just "build me an app".
- Google AI Studio:
    - More for **prompt experimenting**, not full IDE.
    - Good for testing how a model responds to specific queries / transformations.

**MCP \& llms.txt:**

- Brief conceptual explanation:
    - MCP servers = a way to expose tools/APIs in a structured, discoverable way to AI agents.
    - `llms.txt` = a "robots.txt"‑like file describing how LLMs should treat a site/service.
- Keep it light: "These are standards that help keep your AI tools predictable and aligned, especially as your stack grows. Just know they exist; you don't need to implement them today."

***

### 3. Git \& Collaboration (40–45 min)

**Goal:** Give them a minimal, usable git workflow so they can work together without stepping on each other's toes.

**Format:** Live demo on a simple repo + participants follow along if possible.

**Narrative:**

- Start from their pain:
    - "Right now, when you share code, what happens?"
    - "Who has the 'latest' version?"
- Introduce **minimal git model** visually:

```text
main (production / stable)
  ↑
develop (integration / staging)
  ↑
feature/your-name-thing
```


**Hands‑on flow (ideal case, if they can follow on laptops):**

1. Create or open a repo for the example app.
2. Show:
    - `main` branch (protected in principle).
    - `develop` branch where features are merged and tested.
3. Everyone creates a **feature branch**:
    - Name convention: `feature/name-what-you-are-doing`.
4. Small change: update `PLAN.md` or add a trivial function/text.
5. Commit \& push.
6. Create a **merge request / pull request** into `develop`.
7. Show merge on the hosting platform (GitHub/GitLab).

**Disaster demo:**

- Show a prepared scenario with a simple merge conflict:
    - Two people change the same line in `PLAN.md` or `config`.
    - Show the conflict markers and resolve it live.
- Messaging:
    - "This looks scary at first, but it's basically git saying: 'I don't know which version you want; please decide.'"

Emphasize:

- Commit often with meaningful messages.
- Never commit secrets or `.env` files.
- The main win: **everyone can always go back** and see who changed what and why.

***

### 4. External Services \& APIs (20–25 min)

**Goal:** Make APIs less magical and connect them to the example app + security.

**Format:** Conceptual with a small live call if feasible.

**Key points (tie to their PPC world):**

- Most of the useful stuff (Google Ads, GA4, Meta Ads, etc.) is accessed via **APIs**.
- Basic mental model:
    - "The tool sends a request to URL X with your credentials and parameters; it returns JSON with data."
- Show a simple example:
    - Pseudocode or minimal Python/JS snippet calling a fake or public API.
    - Show response structure.
- Link to plan:
    - "In our `PLAN.md`, Step 2 was: fetch data for a date range. This is where APIs come in."

Transition:

- "To call APIs, we need **keys/tokens**. That leads directly to security…"

***

### 5. Security Basics (20–25 min)

**Goal:** Burn into their brain that secrets are never hardcoded or committed, and that AI tools are not a safe place for credentials.

**Format:** Short scary stories + practical patterns.

**Content:**

- Show a hypothetical mistake:
    - API key directly in code: `API_KEY = "sk-..."`.
    - Pushed to GitHub.
- Explain:
    - Once a secret is in git history, treat it as compromised.
- Show the correct pattern:
    - `.env` file with `API_KEY=...`
    - Code reads from environment variable.
    - `.gitignore` contains `.env`.
- For AI tools:
    - "You can describe what the environment variable is called (`API_KEY`), but don't paste production credentials into prompts."
- Simple rule set:
    - Never commit `.env` or credentials.
    - Prefer environment variables or managed secret stores when things get serious.
    - Rotate keys if in doubt.

Tie back to external APIs:

- "Every time you see the word `token` or `key` in docs, think: this belongs in a secret, not in code, not in git, not in Slack."

***

### 6. Data Persistence (20–25 min)

**Goal:** Show options for "where data lives" and when it's worth moving from quick hacks to real storage.

**Format:** Whiteboard + tiny demo.

**Levels of persistence:**

1. **No persistence** – data disappears when you close the app / browser.
2. **Files** (CSV, Parquet, JSON):
    - Great for experiments, quick reporting, columnar analytics (Parquet).
    - Easy to version in git (minus big files).
3. **Databases** (SQLite, Postgres, etc.):
    - Needed when multiple users, larger data, or complex queries.
    - Mention migrations exist, but don't go deep—just explain that schema changes must be tracked.

Tie it to their app:

- Decide for the example:
    - "For this PPC helper, what is enough?"
        - MVP: write daily snapshot to a Parquet or CSV file.
        - Future: push into a database if needed.
- Show one mini example:
    - Read some input (mock or real).
    - Save to a small Parquet or CSV file.
    - Read it back.
- Talk about **reproducibility**:
    - "Tomorrow you can re‑run the analysis because the data is actually stored somewhere stable."

***

### 7. QA \& Process Wrap‑Up (20–25 min)

**Goal:** Turn everything into a minimal repeatable process they can follow when "vibecoding" the next tool.

**Format:** Open Q\&A + co‑creating a checklist / mini process on screen.

**Steps:**

- Ask:
    - "After today, what part feels most useful?"
    - "Where do you still feel lost?"
- Co‑create a **simple workflow** for them, for example:

```markdown
## Before Building a New Tool
- [ ] Write PLAN.md using the template
- [ ] Decide: is this throwaway or production-ish?
- [ ] Create a feature branch for this work

## While Building
- [ ] Use AI coding assistant with PLAN.md as context
- [ ] Never paste secrets into prompts
- [ ] Store API keys in .env (ignored by git)
- [ ] Save data (CSV/Parquet) if it needs to be reused

## Collaborating
- [ ] Commit and push regularly
- [ ] Open a merge request into develop
- [ ] Ask at least one teammate to glance at the changes

## Before Using in Real Life
- [ ] Do a basic manual test
- [ ] Check that no secrets are in git
- [ ] Update PLAN.md / README with what the tool actually does
```

- Encourage them to adapt this checklist to their reality and share it in whatever internal space they use (Notion, Confluence, Google Docs, etc.).

***

## Optional Add‑Ons (If Time / Interest)

- **Kaggle mini‑digression:**
    - Show one dataset that's similar to their PPC work.
    - Mention using it to prototype models or visualizations before connecting to real APIs.
- **Cursor/Claude advanced tricks:**
    - Show how to ask the model to generate tests or sanity checks.
    - Show how to ask the model to refactor for better structure based on `PLAN.md`.

***

This structure gives a clear story arc:

1. Start with **their reality** and pick a concrete app.
2. Introduce **documentation‑first** as the central habit.
3. Wrap their existing AI tools into a **structured workflow**.
4. Add collaboration (git), connectivity (APIs), persistence (data), and guardrails (security).
5. End by co‑designing a **minimal process** they can actually follow.

If helpful, the next step can be: drafting a concrete `PLAN.md` template and a one‑pager git/branching cheat sheet tailored to this team.