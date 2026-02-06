---
theme: seriph
background: https://cover.sli.dev
title: From Vibecoding to Sustainable Development
info: |
  ## From Vibecoding to Sustainable Development
  Workshop for PPC/marketing teams on making AI-built tools less fragile, more shareable, and way less terrifying.
  Much less terrifying

  By Jakub Dubec — FIIT STU Bratislava
class: text-center
drawings:
  persist: false
transition: slide-left
mdc: true
duration: 180min
---

# From Vibecoding to Sustainable Development

How to make your AI-built tools less fragile, more shareable, and way less terrifying

<div class="abs-bl m-6">
  Jakub Dubec · FIIT STU Bratislava
</div>

<div class="abs-br m-6">
  <img src="/images/fiit-logo.svg" class="h-12" alt="FIIT STU" />
</div>

<!--
Welcome! Today is NOT about turning you into software engineers. I repeat — nobody here needs to learn what a linked list is. Today is about taking the cool things you're already building with AI and making them... survivable. Survivable by your teammates. Survivable by future-you at 3 AM when something breaks.
-->

---
layout: image-right
image: https://github.com/Sibyx.png
---

# About Me

**Jakub Dubec** <span class="opacity-60">@Sibyx</span>

- Cloud Engineer & PhD student
- 10+ years as a software engineer
- FIIT STU — Slovak University of Technology in Bratislava
- Python, Django, cloud infrastructure, API design

<div class="mt-4 text-sm opacity-75">

jakubdubec.me · github.com/Sibyx

</div>

<!--
Quick intro — I'm Jakub, I've been writing software for over 10 years and I'm currently doing a PhD at FIIT STU in Bratislava, researching wireless networks. By day I'm a cloud engineer, by night I maintain open-source libraries that apparently 163 people on GitHub depend on — which terrifies me. I've leaked API keys, I've deleted production databases, I've written code that even I couldn't understand a week later. I'm basically a cautionary tale with a salary. And I'm here to help you avoid my greatest hits.

They say experience is the best teacher. My GitHub history says experience is the most expensive teacher. I once accidentally pushed AWS credentials to a public repo. The bots found them before my CI pipeline even finished running.
-->

---
layout: center
class: text-center
---

# Quick Workflow Survey

<div class="text-xl mt-4 mb-8 opacity-80">

I want to learn about **YOUR** workflow — help me calibrate this workshop to you.

</div>

<div class="grid grid-cols-2 gap-12 items-center">
<div>

<div class="text-4xl font-bold mb-4">menti.com</div>

**[https://www.menti.com/al2u77w4v54j](https://www.menti.com/al2u77w4v54j)**

</div>
<div>

<img src="/images/mentimeter_qr_code.png" class="h-48 mx-auto rounded" alt="Scan to join" />

</div>
</div>

<div class="mt-6 text-sm opacity-60">

10 questions. No wrong answers. Just tell me how you work.

</div>

<!--
Pull out your phones — yes, really, I'm giving you permission to use your phone during a presentation. Go to menti.com or scan the QR code. This is NOT a test — there are literally no wrong answers. I want to learn about how you work: what tools you use, where your data lives, how you manage versions. This helps me calibrate the rest of the workshop to YOUR team specifically. Pick whatever honestly describes your workflow. There's also a funny option on each question — I won't judge you if you pick it. Actually, I might.

Fallback if Wi-Fi fails: read each question aloud, ask for a show of hands per option, mentally note the distribution. The 10 questions cover: AI tools used, what they build, data storage, services/APIs, project duration, planning habits, version control, hosting, security practices, and self-assessment on the vibes spectrum.
-->

---

# The Vibe Coding Era

> "There's a new kind of coding I call 'vibe coding', where you fully give in to the vibes, embrace exponentials, and forget that the code even exists."

**— Andrej Karpathy**, co-founder of OpenAI, February 3, 2025

<!--
February 3, 2025 — Andrej Karpathy, co-founder of OpenAI, posted this on X. He coined the term 'vibe coding.' The idea: you describe what you want in English, the AI writes the code, you never look at the code, you just see if the thing works. If it doesn't, you paste the error message back in and hope for the best. Sound familiar?

Background: Karpathy described his workflow: "I 'Accept All' always, I don't read the diffs anymore. When I get error messages I just copy paste them in with no comment. The code grows beyond my usual comprehension." He clarified it's "not too bad for throwaway weekend projects."
-->

---
layout: two-cols
layoutClass: gap-16
---

# Vibe Coding vs. AI-Assisted Dev

| Vibe Coding 🌊           | AI-Assisted Dev 🏗️            |
|--------------------------|--------------------------------|
| Accept all, read nothing | Review, understand, test       |
| "It works, ship it"      | "It works, but *why*?"         |
| Error? Paste it back     | Error? Understand root cause   |
| Solo weekend project     | Team tool that survives Monday |
| The vibes are immaculate | The vibes are... documented    |

::right::

<div class="mt-12">

### The Key Distinction

If an LLM wrote the code for you, and you then **reviewed it**, **tested it**, and can **explain** what it does — that's NOT vibe coding.

That's just **software development** with a fancy assistant.

<div class="text-sm opacity-60 mt-4">
— Simon Willison, creator of Django
</div>

</div>

<!--
Simon Willison — the creator of Django, one of the most popular web frameworks — made an important distinction: if an LLM wrote the code for you, and you then reviewed it, tested it, and can explain what it does to someone else — that's NOT vibe coding. That's just software development with a fancy assistant. The key question is: do you understand what your tool actually does?

Vibe coding is like ordering food in a language you don't speak. Sometimes you get a steak. Sometimes you get a cow tongue. You won't know until you bite.
-->

---

# The Scale of... Vibes

<div class="grid grid-cols-2 gap-8 mt-8">
<div>

### The Good

- **84%** of developers use or plan to use AI tools <span class="text-sm opacity-60">(Stack Overflow 2025)</span>
- **25%** of Y Combinator W25 startups had 95% AI-generated codebases

</div>
<div>

### The Terrifying

- **45%** of AI-generated code contains security vulnerabilities <span class="text-sm opacity-60">(Veracode 2025)</span>
- **39 million** secrets leaked on GitHub in 2024
- **86%** of AI-generated code had XSS vulnerabilities in testing

</div>
</div>

<div v-click class="mt-8 text-center text-xl font-bold text-red-400">
That's not a bug, that's a lifestyle.
</div>

<!--
Let's look at some numbers. 84% of developers are using AI tools — so this isn't fringe, this is mainstream. A quarter of the latest Y Combinator startups are almost entirely AI-generated code. But here's the kicker: nearly half of that AI-generated code has security holes. And 39 million — MILLION — secret keys and passwords were accidentally pushed to GitHub last year.

Remember the survey results? Most of you are already using AI tools to write code and scripts. But how many of you actually look at what it generates? And how many understand it?
-->

---

# Real Horror Stories

<v-clicks>

- 🔥 **Lovable (May 2025)** — Vibe-coding platform generated apps where 170 out of 1,645 had vulnerabilities exposing personal information to anyone

- 💸 **Replit incident** — An AI-generated script accidentally deleted an entire production database

- 🔑 **Base44 SaaS breach** — AI-generated component allowed unauthenticated access to sensitive business logic

- 🤦 **Every single day** — Live scrapers find accidentally-leaked API keys for OpenAI, Anthropic, AWS every second

</v-clicks>

<!--
These aren't hypothetical. In May 2025, Lovable — a company that LITERALLY sells vibe coding — had over 10% of its generated apps leaking personal data. Someone on Replit asked an AI to clean up their database. The AI interpreted 'clean up' very literally. It cleaned up everything. Including the data. There is a non-zero chance that someone in this room has pushed an API key to a public repo. The bots found it in about 30 seconds.

The AI said 'I'll handle the database.' It handled it the way a toddler handles a glass of juice.
-->

---
layout: center
class: text-center
---

# But Vibe Coding Is Also Amazing

<div class="text-xl mt-8">

**Before AI:** "I need to learn Python for 6 months to automate this report"

<div v-click class="mt-4">

**After AI:** "Hey Claude, write me a script that pulls Google Ads data and makes a CSV summary"

</div>

</div>

<div v-click class="mt-12 text-2xl font-bold">
The goal today: Keep the magic. Add the guardrails.
</div>

<!--
Now, I don't want to be the person who kills the vibe. What you're doing IS amazing. A year ago, automating your PPC reports required hiring a developer or spending months learning Python. Now you can describe what you want and get working code in minutes. That's incredible. We're not here to stop you from using AI. We're here to make sure the things you build don't catch fire when you're on vacation.

Vibe coding is like cooking with a flamethrower. You CAN make dinner. But maybe we should also talk about fire extinguishers.
-->

---

# Today's Roadmap

<div class="mt-8 text-lg">

```
📋 Plan First → 🤖 AI Tools → 🔀 Git → 🔌 APIs → 🔒 Security → 💾 Data → ✅ Your Workflow
```

</div>

<v-clicks class="mt-8">

- We'll build understanding **layer by layer**
- Using a **real example** from YOUR work
- Duration: **~3 hours** with breaks
- Format: Mix of **slides, live demos, and YOUR questions**

</v-clicks>

<!--
Here's our roadmap. We're going to start by talking about planning before prompting. Then we'll look at your AI tools in a new light. Then the big one — git, which is how you stop overwriting each other's work. Then APIs, security, and data storage. And we'll end by building YOUR team's workflow together.

Before we dive in — quick question. Show me or tell me: what's one internal tool or script you've built recently? What does it do? What breaks?
-->

---
layout: section
---

# Plan Before You Prompt

The difference between "vibe coding" and "building something real"

<!--
This is the single most important habit change we'll talk about today. Everything else — git, security, data — builds on this foundation. If you take ONE thing away from this workshop, let it be this section.
-->

---
layout: two-cols
layoutClass: gap-8
---

# The Prompt Problem

### Without a plan

```
"Build me a PPC dashboard"
```

<div class="mt-2 text-sm">

→ AI builds... something. Maybe not what you wanted.
You iterate 47 times. You forget what you asked for.
The code is a Frankenstein's monster of prompt iterations.

</div>

::right::

### With a plan

```
"Here is PLAN.md with requirements,
data sources, and security rules.
Implement it step by step."
```

<div class="mt-2 text-sm">

→ AI follows a spec. You can review against the plan.
Your teammate can understand what was built.

</div>

<!--
Here's what typically happens. You open Claude or Cursor and type 'build me a PPC dashboard.' The AI does... something. It looks kind of right. You say 'add a filter.' It adds a filter but breaks the chart. You say 'fix the chart.' It fixes the chart but removes the filter. Three hours later you have a pile of code that sort of works, nobody understands it, and you're not sure which version was the good one.

Prompting AI without a plan is like giving a taxi driver directions one turn at a time. 'Go left. No wait, go right. Actually, go back.' You'll get somewhere, but probably not where you wanted.
-->

---

# The PLAN.md Template

```markdown
# Tool: [Name of what you're building]

## Problem
- What pain point does this solve?
- Who needs it?

## Goal
- One clear sentence of what success looks like

## Data Sources
- Where does the data come from? (APIs, CSVs, databases)

## Rough Flow
1. Get credentials safely (no hardcoding!)
2. Fetch/load data
3. Process/transform
4. Store results
5. Display or export

## Files We Expect
- plan/PLAN.md, src/main_script, src/api_client, data/
```

<!--
This is the template. It's not a PhD thesis — it's maybe 20 lines of text that answer the basic questions: what are we building, where does data come from, and what should NEVER be in the code? You write this BEFORE opening your AI tool. Then you hand this to Claude, Cursor, or whatever you use and say: 'You are the implementer. Here is the plan. Ask me questions if anything is unclear.'

Emphasize: this is a CONVERSATION STARTER with the AI, not a rigid spec. The plan helps the AI ask better questions and produce more coherent code.
-->

---
layout: center
class: text-center
---

# Let's Write a Plan Together

<div class="text-xl mt-8">

👥 Interactive Exercise

</div>

"Let's pick a **real tool** from your team and write a plan for it"

<div class="mt-8 text-sm opacity-75">

Template is on the previous slide for reference.

Who has a script or tool they've built recently — or one they WISH they had?

</div>

<!--
OK, let's do this for real. Who has a script or tool they've built recently — or one they WISH they had? Doesn't have to be fancy. 'A script that pulls our Google Ads data into a spreadsheet' is perfect.

Exercise (10-15 min):
1. Pick one real tool/script from the audience
2. Fill in the PLAN.md template together on screen
3. Point out: "See? Now anyone on your team knows what this thing does. Including the AI."
-->

---

# How to Hand the Plan to AI

<div class="grid grid-cols-2 gap-8">
<div>

### The Prompt

```
You are implementing a tool based on
the plan below.
Follow it as the specification.
Ask me questions before making
assumptions.

[paste PLAN.md contents]
```

</div>
<div>

### Key Principles

<v-clicks>

- AI is the **implementer**, not the **architect**
- The plan is the **contract** between you and the AI
- If the AI goes off-script, point it back to the plan
- The magic phrase: **"Ask me questions before making assumptions"**

</v-clicks>

</div>
</div>

<!--
The magic phrase is: 'Ask me questions before making assumptions.' This changes the dynamic completely. Instead of the AI guessing what you want and building something random, it actually checks with you. You become the project manager. The AI becomes the developer who reads the brief first.
-->

---

# PLAN.md Is a Living Document

<div class="text-xl mt-4 mb-6 font-bold opacity-80">

PLAN.md isn't a tombstone — it's a journal.

</div>

```
BEFORE building          DURING building           AFTER building
┌──────────────┐        ┌──────────────┐         ┌──────────────┐
│ Write the    │        │ Update when  │         │ Record what  │
│ plan         │  ──→   │ reality      │  ──→    │ was actually │
│              │        │ diverges     │         │ built        │
└──────────────┘        └──────────────┘         └──────────────┘
```

<v-clicks class="mt-6">

- The AI discovered the API returns data in a different format? **Update the plan.**
- You decided to skip a feature? **Note it in the plan.**
- The finished tool works differently than planned? **The plan reflects reality, not fantasy.**

</v-clicks>

<!--
Now that you know how to write a plan and hand it to AI, let me tell you the one thing most teams get wrong — they never update the plan. They write it, hand it to Claude, and never look at it again. Then six months later someone reads PLAN.md and it describes a completely different tool than what exists. The plan is only useful if it stays true. When reality changes — and it ALWAYS changes — update the plan. Think of PLAN.md as a journal, not a contract. It evolves with your project. And this idea — keeping the document alive, updating it as you go — becomes even more important when your projects get bigger. Which brings me to something I want to show you...
-->

---

# The Planning Spectrum

<div class="mt-6">

```
← Quick & Light                                     Structured & Thorough →

 No Plan         PLAN.md          Implementation        Full RFC / ADR
                                  Proposals
    ↓                ↓                  ↓                      ↓
 "Just vibe"    "20 lines of      "Structured doc        "Enterprise-grade
                what, why, how"    with lifecycle,        design records"
                                   alternatives,
                                   review questions"

     🏠               🏡                 🏢                     🏗️
 Weekend hack    Team script       Multi-phase            Production
                                   project                system
```

</div>

<div v-click class="mt-6 text-center text-xl font-bold">

You don't jump from no plan to enterprise RFC. You grow into it.

</div>

<!--
Planning isn't binary — it's a spectrum. For a quick script, PLAN.md is perfect. Twenty lines, five minutes, done. But what happens when your tool grows? When it has multiple phases, multiple contributors, and decisions that affect the whole team? That's when you need something more structured. I want to show you what that looks like — not because you need it today, but because you'll recognize the moment when you do.
-->

---
layout: two-cols
layoutClass: gap-8
---

# Implementation Proposals

### PLAN.md <span class="opacity-60">(you know this)</span>

```
Quick, informal, 20 lines
One person writes it
Lives in project root
Great for: scripts, small tools
```

::right::

### Implementation Proposal <span class="opacity-60">(the next level)</span>

```
Same idea — think before you build
But with more structure:

✓ Problem: what are we solving?
✓ Solution: how?
✓ Alternatives: what else did we consider?
✓ Trade-offs: what could go wrong?
```

<div class="mt-4">

```
Draft → Review → Accepted → Implemented
           ↓
       Rejected
```

</div>

<!--
An Implementation Proposal is PLAN.md's big sibling. Same core idea — think before you build — but with more structure. Instead of 20 freeform lines, you have defined sections that force you to think about alternatives and risks. And it has a lifecycle — the proposal goes through review before anyone writes code. You don't need to memorize these sections. I want to show you what this actually looks like in practice.

[Speaker: switch to live screen share. Open a real Implementation Proposal from your own project. Walk through the sections briefly — 60-90 seconds. Point out: 'See? Problem, Solution, Alternatives, Trade-offs. That's it. The AI wrote this draft, I reviewed it.' Then switch back to slides.]
-->

---

# Review Questions — The AI Handoff

<div class="mt-2 mb-4">

The key innovation: **AI writes the proposal, then reviews its own work.**

</div>

<div class="grid grid-cols-2 gap-6">
<div>

```
Step 1: You say
  "Write a proposal for feature X"

Step 2: AI writes the full proposal

Step 3: AI re-reads its own proposal
  and finds contradictions...
```

</div>
<div>

<div class="border border-gray-400 rounded p-4 text-sm">

**Q1: Data Storage Choice**

**Issue**: Proposal says "store in CSV" but also mentions "complex queries needed"

**Question**: Should we use SQLite instead?

**Options**:
- A) CSV files (simple, portable)
- B) SQLite (queryable, single file)
- C) PostgreSQL (if team access needed)

**Answer**: _________ <span class="text-yellow-400">← YOU decide</span>

</div>

</div>
</div>

<div v-click class="mt-4 text-center font-bold text-lg">

The AI doesn't know what it doesn't know. But it CAN find its own contradictions.

</div>

<!--
This is my favorite part of the whole methodology. After the AI writes a proposal, it reads it back and generates questions — structured questions with options — about things that don't quite add up. The AI found a contradiction? It asks you. The AI isn't sure about a design choice? It gives you options. You — the human — make the final call. This is the handoff. The AI does the heavy lifting, but YOU make the decisions. It's like having a junior architect who drafts the blueprints and then says 'hey boss, I noticed three things that don't quite work — which way should we go?'
-->

---
layout: center
---

# These Slides Were Planned This Way

<div class="text-lg mt-8">

The slides you're watching **right now** were designed using this exact system.

</div>

<v-clicks class="mt-6">

- **IP-001** proposed the full slide structure, speaker notes, and section order
- AI (Claude) wrote the first draft
- AI generated **5 Review Questions** (language, slide count, demo strategy, humor, section order)
- I answered each question
- AI applied the resolutions and built the slides

</v-clicks>

<div v-click class="mt-8 text-xl font-bold">

I used this system to build what you're watching. It works.

</div>

<!--
By the way — this presentation was designed using the exact methodology I just showed you. I didn't just open Claude and say 'make me slides.' I wrote a proposal — IP-001 — that defined every section, every slide, every speaker note. The AI drafted it, then generated five review questions: should the slides be in English or Slovak? How many slides? What's the demo strategy? I answered each one, the AI updated the proposal, and then implemented it. The result is what you're looking at. Let me show you the actual document.

[Speaker: switch to live screen share. Open docs/proposals/posts/ip-001-presentation-structure-and-slide-list.md. Scroll through it briefly — show the Problem Statement, the Detailed Slide List, the Review Questions with filled-in answers. Point out: 'See Q1? I said English slides, Slovak speaking. Q4? I said keep all the jokes. These decisions shaped what you're watching right now.' Keep it to 60-90 seconds. Switch back to slides.]
-->

---
layout: two-cols
layoutClass: gap-8
---

# Plan-Driven vs. Vibe-Driven

### Vibe-driven timeline

```
Day 1: "Build a dashboard" → works!
Day 2: "Add filters" → half-broken
Day 3: "Fix it" → different half broken
Day 5: "Start over"
Day 7: "I hate coding"
```

::right::

### Plan-driven timeline

```
Day 1: Write PLAN.md (30 min)
Day 1: AI implements step 1-3
Day 2: Review, adjust plan,
        AI implements step 4-5
Day 3: Working tool that matches plan
Day 5: Teammate reads PLAN.md,
        understands everything
```

<!--
I've seen both of these timelines play out in real teams. The vibe-driven approach feels faster on day one, but by day five you're starting over. The plan-driven approach feels slower at first — 'why am I writing a document instead of coding?' — but by day five you have something that works AND that someone else can maintain.
-->

---
layout: center
---

# The Bus Factor 🚌

<div class="text-xl mt-8">

**"If [person] gets hit by a bus, can anyone else continue their work?"**

</div>

<div class="grid grid-cols-2 gap-8 mt-8">
<div class="text-center">

### Without documentation

Bus factor = **1** 😬

</div>
<div class="text-center">

### With PLAN.md + git

Bus factor = **your whole team** 🎉

</div>
</div>

<div v-click class="mt-8 text-center opacity-75">

This isn't about buses. It's about vacations, sick days, and switching projects.

</div>

<!--
In software engineering, we have this morbid concept called the 'bus factor.' If the person who built this tool gets hit by a bus — or, more realistically, goes on vacation or quits — can anyone else figure out what the tool does and keep it running? If the answer is no, you have a bus factor of one. PLAN.md is the cheapest insurance policy against a bus factor of one.

In our industry, we've rebranded this to the 'lottery factor.' Same concept, but you're happy for the person instead of traumatized.
-->

---
layout: section
---

# Your AI Toolkit

Same tools, better workflow

---

# The Tooling Landscape

<div class="grid grid-cols-3 gap-6 mt-4">
<div class="border border-gray-500 rounded p-4">

### Claude Code

- Terminal-based AI agent
- Multi-file reasoning
- Reads your whole project
- **Best for:** complex multi-file tasks
- Uses `CLAUDE.md` for context

</div>
<div class="border border-gray-500 rounded p-4">

### Cursor

- AI-powered IDE
- Composer mode for project-wide edits
- `.cursorrules` for context
- **Best for:** daily coding workflow
- Cmd+K for inline edits

</div>
<div class="border border-gray-500 rounded p-4">

### Google AI Studio

- Prompt playground
- Test prompts & transformations
- Not a full IDE
- **Best for:** experimenting
- Great for prototyping ideas

</div>
</div>

<!--
You probably already use one or more of these. Let's quickly position them. Cursor is the one most of you likely use daily — it's an IDE with AI built in. Claude Code is a terminal agent that can reason about your whole project at once. Google AI Studio is more of a sandbox for testing prompts. They're all useful, but for different things.

Quick poll: who uses Cursor? Claude/ChatGPT? Google AI Studio? Something else?
-->

---

# Cursor Power Moves

<v-clicks>

- **Composer mode** — Multi-file edits guided by context
- **`.cursorrules` file** — "Here's how this project works" — persistent project context
- **Cmd+K** — Quick inline edits on a single file
- **Pro tip:** Drop your `PLAN.md` into the project root. Cursor reads it automatically.

</v-clicks>

<!--
For Cursor users — there are two modes that matter. Cmd+K is for quick edits in a single file. Composer is for bigger changes across multiple files. The game-changer is the .cursorrules file — you put it in your project root and it tells Cursor things like 'always use environment variables for API keys' or 'follow the structure in PLAN.md.' It's like giving the AI a permanent cheat sheet about your project.
-->

---

# Claude Code Power Moves

<v-clicks>

- **`CLAUDE.md` file** — Project instructions Claude reads automatically
- **Multi-file reasoning** — "Read the whole project, then implement step 3 of the plan"
- **Best with a plan** — Claude Code + PLAN.md = focused implementation

</v-clicks>

<!--
Claude Code works differently — it's in your terminal, not in an IDE. But it's incredibly good at reading your entire project, understanding the structure, and making changes across multiple files. The CLAUDE.md file works like .cursorrules — it's permanent instructions. You can put things like 'never hardcode API keys' or 'always check PLAN.md before making changes' and Claude will follow those rules every time.
-->

---
layout: center
---

# The Golden Rule of AI Tooling

<div class="text-2xl mt-4 mb-8 font-bold">

> "The AI is a junior developer with infinite energy and zero judgment.<br>You are the senior developer. Act like it."

</div>

<div class="grid grid-cols-2 gap-8">
<div>

- ✅ Give it a plan
- ✅ Review its output
- ✅ Ask it to explain what it did

</div>
<div>

- ❌ Accept all without reading
- ❌ Paste production secrets into prompts
- ❌ Assume it knows your business logic

</div>
</div>

<!--
Here's the mental model I want you to walk away with. The AI is a junior developer who works 24/7, never sleeps, never complains, and types at the speed of light. But like any junior developer, it has terrible judgment. It will confidently write code that looks perfect but has a gaping security hole. YOUR job is to be the senior developer who reviews, questions, and approves.

Think of AI as that intern who's really enthusiastic but once reorganized the entire filing system alphabetically by the third word of each document title. Technically sorted! Practically useless.
-->

---

# MCP & llms.txt — Just Know They Exist

<div class="grid grid-cols-2 gap-8 mt-8">
<div>

### MCP (Model Context Protocol)

A standard for connecting AI tools to external services (databases, APIs, GitHub, etc.)

Think: letting Claude directly talk to your database

</div>
<div>

### llms.txt

Like `robots.txt` but for AI — tells LLMs how to interact with your service

Think: instructions for AI visitors to your website

</div>
</div>

<div class="mt-8 text-center opacity-75">

You don't need these today. Just know they exist for when your tools get more complex.

</div>

<!--
Two quick concepts for your radar. MCP is a way to let your AI tools directly talk to services — like connecting Claude directly to your database or GitHub. llms.txt is a standard file you put on a website to guide AI tools. Think of these as plumbing — you don't need to be a plumber today, but it's good to know plumbing exists for when you need it.
-->

---

# Tool Decision Matrix

| I want to... | Use... |
|---|---|
| Edit code in a file | Cursor (Cmd+K) |
| Restructure a project | Cursor Composer or Claude Code |
| Test a prompt idea | Google AI Studio |
| Implement a full plan | Claude Code with PLAN.md |
| Quick one-off script | Any of them + the PLAN.md habit |

<div class="mt-8 text-center font-bold text-xl">

The **WORKFLOW** matters more than the tool.

Plan → Implement → Review.

</div>

<!--
Here's your cheat sheet. Don't overthink tool choice — pick the one you're comfortable with. The WORKFLOW matters more than the tool. Plan, implement, review. Works with any of them.
-->

---
layout: section
---

# Git: Your Collaborative Safety Net

The "undo" button for your entire project — and how to stop overwriting each other's work

---

# The Problem Without Git

<div class="mt-8 font-mono text-lg">

```
📁 campaign-tool-final.py
📁 campaign-tool-final-v2.py
📁 campaign-tool-final-v2-FIXED.py
📁 campaign-tool-final-v2-FIXED-johns-version.py
📁 campaign-tool-DONT-TOUCH.py
📁 campaign-tool-final-ACTUALLY-FINAL.py
```

</div>

<div v-click class="mt-8 text-center text-xl">

🙋 Raise your hand if this looks familiar.

</div>

<!--
Raise your hand if this looks familiar. You have a file. You make a copy. Your colleague makes a copy of the copy. Someone emails their version. Now you have six versions and nobody knows which one works. This is what git solves. Git is version control — it's like Google Docs' version history, but for code.

What happens right now when two of you work on the same script?

Developers have a saying: 'There are two hard things in computer science: cache invalidation, naming things, and off-by-one errors.' The file naming problem is #2.
-->

---

# Git in 60 Seconds

```
Your computer              GitHub/GitLab (the cloud)
┌──────────────┐          ┌──────────────────┐
│  You edit     │ ──push─→ │  Everyone sees   │
│  files        │ ←─pull── │  the changes     │
└──────────────┘          └──────────────────┘
```

<div class="grid grid-cols-2 gap-8 mt-8">
<div>

### Core Concepts (no jargon)

- **Repository (repo)** — Your project folder, but tracked
- **Commit** — A save point with a description
- **Push** — Upload your save points to the cloud

</div>
<div>

<div class="mt-0">

- **Pull** — Download everyone else's save points
- **Branch** — Your own parallel copy to work on

</div>

</div>
</div>

<!--
Git is actually simple if you strip away the jargon. A repo is just your project folder with superpowers. A commit is a save point — like checkpoints in a video game. You push to share your work, pull to get others' work. And a branch is your personal workspace where you can experiment without messing up the main version.
-->

---

# The Branch Model

```
main       ●━━━━━━━━━━━━━━━━━━━━●━━━━━━━●  (stable, production)
            \                  ↗
develop      ●━━━━━●━━━━━●━━━●  (integration, testing)
              \   ↗      \  ↗
feature/anna   ●━●        \
feature/jan               ●━●  (your work)
```

<v-clicks>

1. **main** — the "production" version that works. Don't touch directly.
2. **develop** — where features get merged and tested together.
3. **feature/your-name-thing** — YOUR workspace. Go wild here.

</v-clicks>

<!--
Here's the model. Think of it like a highway system. Main is the highway — it's smooth, it's paved, traffic flows. Develop is the on-ramp where we check if new things are safe. Feature branches are side roads where you build new stuff. When your side road is done, you merge it onto the on-ramp, test it, and then it joins the highway. Nobody drives construction equipment on the highway.

The 'main' branch is like the kitchen at a restaurant. The feature branch is where you experiment with recipes. You NEVER experiment in the kitchen during dinner service.
-->

---

# Branch Naming Convention

```
feature/anna-add-campaign-filter
feature/jan-fix-csv-export
feature/petra-update-api-client
```

<div class="mt-8">

### Rules

<v-clicks>

- Start with `feature/`
- Include **your name** (so we know whose branch it is)
- **Describe** what you're doing (short and clear)
- Use **hyphens**, not spaces

</v-clicks>

</div>

<!--
Simple naming convention. Start with 'feature/', add your name, describe the change. This way when someone looks at the list of branches, they immediately know who's working on what. No more guessing games.
-->

---

# The Git Workflow — Step by Step

```
1. git checkout develop            ← Start from develop
2. git checkout -b feature/me     ← Create your branch
3. ... do your work ...
4. git add my-changed-files       ← Stage changes
5. git commit -m "what I did"     ← Save checkpoint
6. git push                       ← Upload to GitHub
7. Create Pull Request             ← Ask to merge
8. Team reviews → Merge! 🎉
```

<div v-click class="mt-4 text-sm opacity-75">

💡 If using GUI tools (GitHub Desktop, VS Code), each step has a button — no typing needed.

</div>

<!--
Here's the workflow. Step 1: start from the develop branch. Step 2: create your own feature branch. Steps 3-5: work normally and save checkpoints. Step 6: push to GitHub. Step 7: create a pull request — which is basically saying 'hey team, I'm done, please look at this before we merge it.' Step 8: someone glances at it, approves, and it gets merged.

If using GUI tools — GitHub Desktop, VS Code — show the equivalent buttons. Don't assume CLI comfort.
-->

---

# What's a Pull Request?

A **Pull Request (PR)** = "I made changes. Please review before merging."

<div class="grid grid-cols-2 gap-8 mt-8">
<div>

### It's a conversation

- "Here's what I changed and why"
- "Looks good! ✅"
- "Hey, you left an API key in line 42 🚨"

</div>
<div>

### Why it matters

- Catches mistakes **before** they reach shared code
- Creates a **history** of decisions
- Even a **quick glance** from a teammate helps

</div>
</div>

<!--
A pull request is your way of saying 'I finished my feature, can someone take a look before we merge it into develop?' It shows exactly what changed. Your teammate can see every line, ask questions, suggest changes. This is where you catch mistakes — like accidentally committing an API key — before they reach the shared code.

A pull request is like asking someone to proofread your email before you send it to the CEO. Except the email is code and the CEO is production.
-->

---
layout: two-cols
layoutClass: gap-8
---

# Commit Messages That Don't Suck

### ❌ Bad

```
"stuff"
"fixed it"
"asdfgh"
"wip"
"final commit"
"no really final this time"
```

::right::

### ✅ Good

```
"add campaign filter by date range"
"fix CSV export missing header row"
"update API client to use env variables"
"remove hardcoded API key from config"
```

<div class="mt-4 text-sm">

**Rule:** Describe WHAT you changed and WHY.

Your commit message is a gift to future-you.

</div>

<!--
Your commit message is a gift to future-you. Six months from now, you'll look at the history and either see 'add campaign filter by date range' — great, you know exactly what happened — or 'stuff.' Which future do you prefer?

The most terrifying words in software: 'git log' shows 47 commits all named 'fix'. Fix WHAT? Nobody knows. It's like a horror movie where the journal entries just say 'the thing happened again.'
-->

---
layout: center
class: text-center
---

# 👥 Live Demo

Let's create a repo, make branches, and merge — using GUI tools

<div class="mt-8 text-sm opacity-75">

If you have your laptop, follow along!

1. Clone the workshop repo
2. Create a feature branch with your name
3. Make a small change
4. Commit, push, create PR
5. Merge into develop

</div>

<!--
OK, let's do this live. I'm going to open GitHub Desktop / VS Code and we'll walk through the whole flow. Create a repo, create a branch, make a change, commit, push, create a pull request, and merge. If you have your laptop, follow along.
-->

---

# Disaster Recovery with Git

<v-clicks>

- **"I broke everything!"** → `git stash` or `git checkout .` — discard changes
- **"I need Tuesday's version"** → `git log` → `git checkout <commit>`
- **"Someone merged bad code"** → `git revert`
- **"I committed secrets"** → **ROTATE THE KEY IMMEDIATELY.** Then clean git history.

</v-clicks>

<div v-click class="mt-8 p-4 border border-red-400 rounded text-center">

⚠️ If a secret was ever in git history — even for one commit — the old key is compromised.<br>
Bots scrape GitHub every second. The ONLY fix is: <strong>rotate the key</strong>.

</div>

<!--
Here's your emergency playbook. Broke everything? Git can undo it. Need an old version? Git has it. Someone merged bad code? Git can revert it. But — and this is critical — if you committed a secret like an API key, git history is NOT enough. Even if you delete it in the next commit, it's still in the history. The ONLY safe response is: rotate the key.
-->

---

# Git Cheat Sheet

| I want to... | Command / Action |
|---|---|
| Start fresh from develop | `git checkout develop && git pull` |
| Create my branch | `git checkout -b feature/name-thing` |
| Save my work | `git add . && git commit -m "message"` |
| Share my work | `git push` |
| Get latest changes | `git pull` |
| See what changed | `git status` / `git diff` |
| Undo my local changes | `git checkout .` |
| See history | `git log --oneline` |

<div class="mt-4 text-center text-sm opacity-75">

These 8 commands cover 95% of what you'll ever need. Screenshot this slide.

</div>

<!--
This is your cheat sheet. Bookmark this slide, screenshot it, tattoo it — whatever works. These 8 commands cover 95% of what you'll ever need. If you forget everything else, remember: branch, commit, push, pull request.
-->

---
layout: section
---

# APIs: Where Your Data Actually Comes From

Making the magical black box slightly less magical

---

# What Is an API? (No Jargon Version)

```
You (the app)     Waiter (the API)     Kitchen (the service)
┌─────────┐      ┌──────────────┐     ┌──────────────┐
│ "I want │      │ Takes your   │     │ Google Ads   │
│ campaign │ ──→  │ request,     │ ──→ │ Meta Ads     │
│ data for │      │ brings back  │     │ GA4          │
│ January" │ ←──  │ the result   │ ←── │ etc.         │
└─────────┘      └──────────────┘     └──────────────┘
```

<div v-click class="mt-8 text-xl text-center">

The API is the **waiter**. The API documentation is the **menu**.

</div>

<!--
An API is just a messenger. You send a request — 'give me campaign data for January' — and it brings back the answer. Think of it like a restaurant: you don't go into the kitchen to cook. You tell the waiter what you want, the kitchen makes it, and the waiter brings it back.

An API is a waiter that never judges your order. 'You want ALL the data for the last 3 years grouped by hour? Sure thing. That'll be 47 seconds and your rate limit for today.'
-->

---

# APIs in Your PPC World

APIs you probably already use (whether you know it or not):

<v-clicks>

- **Google Ads API** — campaign data, keywords, budgets
- **Google Analytics 4 API** — website traffic, conversions
- **Meta Marketing API** — Facebook/Instagram ads
- **Google Sheets API** — reading/writing spreadsheets
- **Slack API** — sending notifications

</v-clicks>

<div v-click class="mt-8 font-bold">

When your script "pulls data from Google Ads" — it's making API calls.

</div>

<!--
Every time you use a script that gets your ad data, it's calling an API behind the scenes. The Google Ads API lets you read campaign data, adjust budgets, pause ads. The GA4 API gives you analytics. When your AI-generated script 'pulls data from Google Ads,' this is what it's doing — making API calls.
-->

---

# Anatomy of an API Call

```python
# This is what happens behind the scenes:

# 1. Where to ask (URL/endpoint)
url = "https://googleads.googleapis.com/v17/customers/123/campaigns"

# 2. Who's asking (authentication)
headers = {"Authorization": "Bearer YOUR_TOKEN_HERE"}  # ← THIS is the secret!

# 3. What to ask (parameters)
params = {"date_range": "last_30_days"}

# 4. Send the request → Get the response
response = requests.get(url, headers=headers, params=params)
data = response.json()  # ← Your campaign data!
```

<div v-click class="mt-4 text-center text-red-400 font-bold">

See that YOUR_TOKEN_HERE? That MUST NEVER be hardcoded. Stay tuned...

</div>

<!--
Here's what an API call looks like in code. Four parts: WHERE to ask (the URL), WHO's asking (your authentication token — this is the secret part!), WHAT to ask (parameters like date range), and the response. See that YOUR_TOKEN_HERE? That's the thing that must NEVER be hardcoded in your script.
-->

---

# When APIs Go Wrong

<v-clicks>

- **401 Unauthorized** — "Who are you? Your key is wrong or expired"
- **403 Forbidden** — "I know who you are, but you can't do that"
- **404 Not Found** — "That endpoint/resource doesn't exist"
- **429 Too Many Requests** — "Slow down! You're asking too much too fast"
- **500 Internal Server Error** — "It's not you, it's us"

</v-clicks>

<div v-click class="mt-4 text-sm opacity-60 text-center">

HTTP 418 "I'm a Teapot" is a real error code. It was an April Fools' joke in 1998. Developers are the kind of people who embed jokes into internet standards.

</div>

<!--
When your script stops working and throws an error, these numbers tell you why. 401 means your credentials are wrong — did your token expire? 429 means you're hitting the API too fast. 500 means Google's servers are having a bad day. Teach your AI to handle these errors in the code it generates.
-->

---

# Rate Limits — The API Speed Limit

<v-clicks>

- Most APIs limit how many requests you can make per minute/day
- Google Ads API: varies by access level
- Exceeding the limit = your script **stops working temporarily**
- **Solution:** Build in delays, cache data, don't re-fetch what you already have

</v-clicks>

<div v-click class="mt-8">

💡 Tell your AI: *"Add rate limiting and caching to avoid hitting API limits."*

This is one of those things AI-generated code often misses.

</div>

<!--
Every API has speed limits. If your script hammers an API with thousands of requests, it'll get temporarily blocked. Tell your AI: 'Add rate limiting and caching to avoid hitting API limits.' This is one of those things AI-generated code often misses.
-->

---
layout: center
class: text-center
---

# The Bridge to Security

<div class="text-2xl mt-8">

To call **ANY** of these APIs, you need **credentials**.

</div>

<div v-click class="text-xl mt-4">

API keys, tokens, secrets.

</div>

<div v-click class="text-2xl mt-8 font-bold text-red-400">

Where these credentials live determines whether your tool is safe or a ticking time bomb.

</div>

<!--
So now you know what APIs are and how they work. The key takeaway: every API call requires credentials. Where you store those credentials is the single biggest security decision you'll make. And that's our next topic.
-->

---
layout: section
---

# Security: Don't Be a Statistic

39 million secrets leaked on GitHub in 2024. Let's not add to that number.

---

# The Scariest Slide in This Presentation

```python
# ❌ THIS IS IN SOMEONE'S PUBLIC GITHUB RIGHT NOW
import google.ads

API_KEY = "AIzaSyD-9tSrke72PouQMnMX-a7eZSW0jkFMBWY"
CLIENT_SECRET = "GOCSPX-rTb3kN7dEvGl2YsCFapM5YnBhRZ"
REFRESH_TOKEN = "1//04MuU7VqGhASMCgYIARAAGAQSNwF..."

client = google.ads.GoogleAdsClient(
    developer_token=API_KEY,
    client_secret=CLIENT_SECRET,
)
```

<v-clicks>

1. ⏱️ **30 seconds** — Automated bots find the key
2. 💸 **5 minutes** — Someone starts using your API quota
3. 📧 **Next morning** — You get a bill for $4,000

</v-clicks>

<!--
This is real code from a real GitHub repo — with changed values, obviously. Someone put their Google Ads API credentials directly in the code, pushed it to a public repo, and within minutes, bots found it. Automated scrapers scan every new commit on GitHub looking for patterns that look like API keys. They find them in about 30 seconds.
-->

---
layout: center
---

# The Three Rules of Secrets

<div class="text-3xl mt-8 space-y-6">

<v-clicks>

<div>🔒 Rule 1: Secrets <span class="text-red-400 font-bold">NEVER</span> go in code</div>

<div>🔒 Rule 2: Secrets <span class="text-red-400 font-bold">NEVER</span> go in git</div>

<div>🔒 Rule 3: Secrets <span class="text-red-400 font-bold">NEVER</span> go into AI prompts</div>

</v-clicks>

</div>

<div v-click class="mt-12 text-center opacity-75">

That's it. That's the whole security section. Everything else is implementation details.

</div>

<!--
If you remember nothing else from the security section, remember these three rules. Never put secrets in code — use environment variables. Never put secrets in git — use .gitignore. Never paste production API keys into ChatGPT, Claude, or Cursor prompts. The AI doesn't need your real key to write the code.
-->

---
layout: two-cols
layoutClass: gap-8
---

# The .env Pattern

### The `.env` file <span class="text-red-400">(NOT in git)</span>

```
# .env - THIS FILE IS SECRET
GOOGLE_ADS_API_KEY=AIzaSyD-9tSr...
META_ACCESS_TOKEN=EAABsbCS1234...
DATABASE_URL=postgresql://user:pass@host/db
```

### Your code reads from environment

```python
import os

api_key = os.environ["GOOGLE_ADS_API_KEY"]
# ← No secrets in the code!
```

::right::

### Your `.gitignore` file

```
.env
.env.local
*.pem
credentials.json
```

<div class="mt-8">

### How it works

1. Secrets live in `.env`
2. Code reads from environment
3. `.gitignore` tells git to ignore `.env`
4. Secret never touches git history

</div>

<!--
Here's the pattern. You create a file called .env in your project root. This is where ALL your secrets live. Your code reads from this file. And critically, you add .env to .gitignore, which tells git to pretend the file doesn't exist. It will never be committed, never be pushed to GitHub.
-->

---

# The .env.example Pattern

```
# .env.example - THIS FILE IS COMMITTED (shows structure, not values)
GOOGLE_ADS_API_KEY=your-key-here
META_ACCESS_TOKEN=your-token-here
DATABASE_URL=postgresql://user:pass@host/dbname
```

<div class="mt-8">

### Why?

<v-clicks>

- New teammate joins → copies `.env.example` to `.env` → fills in their own keys
- Documents **WHAT** environment variables exist without exposing values
- This file **IS** committed to git — it's just a template

</v-clicks>

</div>

<!--
But wait — if .env is not in git, how does a new person know what environment variables they need? That's what .env.example is for. It's a template that shows the variable NAMES but not the actual VALUES. It gets committed to git. When someone new joins, they copy it to .env and fill in their own credentials.
-->

---
layout: center
class: text-center
---

# 👥 Quick Security Audit

<div class="mt-8 text-left inline-block">

Let's do a 2-minute security check on one of your existing projects:

- [ ] Are there any API keys directly in the code?
- [ ] Is there a `.gitignore` file?
- [ ] Does `.gitignore` include `.env`?
- [ ] Are credentials in a `.env` file (or similar)?
- [ ] Have any secrets ever been committed to git history?

</div>

<div class="mt-8 text-sm opacity-75">

No judgment — we're here to fix things, not blame.

</div>

<!--
Let's do this right now. Pull up one of your existing projects. Can you find any API keys or passwords directly in the Python/JS files? Is there a .gitignore? Does it mention .env? This is a quick health check.
-->

---

# "But I Already Committed a Secret..."

If a secret was **ever** in git history, even if you deleted it later:

<v-clicks>

1. **ROTATE THE KEY IMMEDIATELY** — get a new one from the API provider
2. The old key is **compromised forever** (bots scrape git history too)
3. Optionally: clean git history with BFG Repo Cleaner
4. But **step 1 is the only thing that actually matters**

</v-clicks>

<div v-click class="mt-8 p-4 border border-red-400 rounded text-center">

Deleting a secret in the next commit does NOT help.<br>
Git keeps full history. Bots read old commits. <strong>Rotate the key.</strong>

</div>

<!--
This is the most important thing I'll say today about security: if an API key was EVER in your git history — even for one commit — consider it compromised. The ONLY fix is to go to the API provider, revoke the old key, and generate a new one.
-->

---

# AI Tools and Secrets

<div class="grid grid-cols-2 gap-8 mt-8">
<div>

### ✅ What you CAN tell AI

- Variable names and file structure
- "The API key is stored in the `GOOGLE_ADS_KEY` environment variable"
- What the API does, what data it returns

</div>
<div>

### ❌ What you CANNOT tell AI

- Actual key values, passwords, tokens
- "The API key is `AIzaSyD-9tSr...`"
- Connection strings with real credentials

</div>
</div>

<!--
When you're working with Claude, Cursor, or ChatGPT, you can describe everything ABOUT your secrets without revealing them. Say 'I have an environment variable called GOOGLE_ADS_KEY' — the AI can write all the code it needs. Never paste the actual key value into any AI tool.
-->

---

# Security Cheat Sheet

| Situation | Do This |
|---|---|
| New project | Create `.env` + `.gitignore` FIRST |
| Share credentials with teammate | Use a password manager, NEVER Slack/email |
| AI tool asks for API key | Give the variable name, not the value |
| Found a secret in git | Rotate key immediately, then clean history |
| Not sure if something is a secret | If in doubt, treat it as a secret |
| Setting up a new service | Immediately put credentials in `.env` |

<!--
Bookmark this. When in doubt about anything security-related, check this cheat sheet. The golden rule: if you're not sure whether something is a secret, treat it as one. Better safe than explaining to your boss why someone ran up a $4,000 API bill on your leaked credentials.
-->

---
layout: section
---

# Where Does Your Data Live?

What happens when you close the tab, restart the script, or turn off your laptop

---

# The Persistence Spectrum

```
Level 0: RAM only        →  "Close the tab, data is gone"
Level 1: LocalStorage    →  "Browser remembers, but only on your machine"
Level 2: Files (CSV/JSON)→  "Data survives, shareable, but manual"
Level 3: SQLite          →  "Real database, single file, no server needed"
Level 4: PostgreSQL      →  "Full database server, multi-user, production-grade"
```

<div class="mt-8">

### When to upgrade

<v-clicks>

- Level 0 → 1: "I need data **between sessions**"
- Level 1 → 2: "I need to **share** data or analyze it"
- Level 2 → 3: "I need to **query** data in complex ways"
- Level 3 → 4: "**Multiple people** access data simultaneously"

</v-clicks>

</div>

<!--
Data persistence is just a fancy way of saying 'where does your data live when the program isn't running?' Most of your PPC tools need to be somewhere in the Level 2-3 range.
-->

---
layout: two-cols
layoutClass: gap-8
---

# Level 2: Files

### CSV

```csv
campaign,clicks,cost,conversions
Brand,1234,450.00,89
Generic,5678,1200.00,42
```

- ✅ Opens in Excel/Sheets
- ✅ Humans can read it
- ❌ Slow with large data
- ❌ No data types

::right::

### Parquet

<div class="mt-12">

- ✅ 10-100x smaller than CSV
- ✅ Preserves data types
- ✅ Blazing fast for analysis
- ❌ Can't open in Excel directly
- ❌ Need Python/tools to read

</div>

<!--
For most of your scripts, files are the right answer. CSV is the universal format — everyone knows it, it opens in Excel. Parquet is the fancy version — it's compressed, typed, and fast. If your script saves daily campaign snapshots, CSV is fine for small data. Millions of rows? Parquet.
-->

---

# Level 3: SQLite — The Sweet Spot

```python
import sqlite3

# The entire database is ONE file
db = sqlite3.connect("campaigns.db")

# Create a table
db.execute("""
    CREATE TABLE IF NOT EXISTS daily_stats (
        date TEXT, campaign TEXT,
        clicks INTEGER, cost REAL, conversions INTEGER
    )
""")

# Query with SQL
results = db.execute("""
    SELECT campaign, SUM(cost), SUM(conversions)
    FROM daily_stats
    WHERE date >= '2026-01-01'
    GROUP BY campaign
    ORDER BY SUM(conversions) DESC
""")
```

<div class="mt-2 text-center text-sm opacity-75">

Real database. Single file. No server. No configuration. No passwords. Just works.

</div>

<!--
SQLite is the magic middle ground. It's a real database — you can query it with SQL — but it's just a single file. No server to install, no configuration, no passwords. Tell your AI: 'store the data in SQLite' and it'll set this up for you.
-->

---

# The "Is This Throwaway?" Test

<div class="grid grid-cols-2 gap-8 mt-8">
<div class="text-center">

### Throwaway

One-time analysis<br>
Prototype / demo<br>
Exploring data

**→ Level 0-1 is fine**

</div>
<div class="text-center">

### Real Tool

Daily reporting<br>
Team dashboard<br>
Automated pipeline

**→ Level 1-3 minimum**

</div>
</div>

<div v-click class="mt-8 text-center text-xl font-bold">

Ask: "Will someone other than me use this?" and "Will I need this data next week?"

</div>

<!--
Not everything needs a database. If you're doing a one-time analysis, a Jupyter notebook with no persistence is totally fine. But if your tool runs daily, feeds into decisions, or is used by your team — that needs real storage.
-->

---

# Data Persistence in PLAN.md

Add this section to your plans:

```markdown
## Data Storage
- **Type:** CSV files / SQLite / PostgreSQL
- **Location:** data/ directory (git-ignored if large)
- **Retention:** Keep last 90 days of daily snapshots
- **Backup:** [how/when]
- **Who accesses:** Just me / team / external
```

<div class="mt-8">

**Why?** This prevents the AI from making random choices — sometimes it'll use SQLite, sometimes files, sometimes Postgres, depending on its mood.

**You** decide. Put it in the plan.

</div>

<!--
Add this section to your PLAN.md. Before the AI writes any code, decide where the data lives. This prevents the AI from making random choices. You decide. Put it in the plan.
-->

---
layout: section
---

# Your Workflow, Your Rules

Let's take everything we've covered and make it yours

---

# Everything We've Covered

<div class="mt-8 text-lg">

<v-clicks>

1. 📋 **Plan First** — Write PLAN.md before prompting AI
2. 🤖 **AI Tools** — Use them as implementers, not architects
3. 🔀 **Git** — Branches, commits, PRs, no more `final-v2-FIXED.py`
4. 🔌 **APIs** — Your tools talk to services via structured requests
5. 🔒 **Security** — `.env`, `.gitignore`, never paste secrets
6. 💾 **Data** — Choose the right persistence level for the job

</v-clicks>

</div>

<!--
Quick recap of everything we covered today. Six topics, all connected. The plan drives the AI. Git keeps you safe. APIs connect you to data. Security protects your credentials. Data persistence makes your tools reliable.
-->

---

# 👥 Let's Build Your Team Checklist

```markdown
## Before We Start Building
- [ ] Write PLAN.md describing what we're building
- [ ] Create feature branch: feature/[name]-[thing]
- [ ] Check .env.example for required secrets

## While Building
- [ ] Use AI with PLAN.md as context
- [ ] Commit every logical change with clear message
- [ ] Never commit .env or credentials
- [ ] Test locally before pushing

## When Sharing Work
- [ ] Push feature branch
- [ ] Create PR with description of changes
- [ ] Ask teammate to review (even a quick look)
- [ ] Merge to develop, not main

## When It's "Done"
- [ ] Secrets in environment variables
- [ ] Data storage decided and documented
- [ ] PLAN.md updated with what was actually built
```

<!--
Let's customize this for YOUR team. What would you add? What doesn't apply? Maybe you have specific tools or platforms that need their own rules. The goal is that this checklist lives in your team wiki or Notion and you actually use it.
-->

---

# The Vibes-to-Sustainable Spectrum

```
← Pure Vibecoding                              Sustainable Dev →

"Build me a thing"    "Here's PLAN.md,       "Plan, branch,
  ↓                    implement step 3"      implement, PR,
"Accept all"              ↓                    review, merge"
  ↓                  "Review the output"           ↓
"It works! Ship it"       ↓                  "Documented,
  ↓                  "Commit to branch"       versioned,
"It broke."               ↓                   secure, shared"
                     "PR + merge"
```

<div v-click class="mt-4 text-center text-xl">

You don't have to be at the far right.<br>
**Moving even slightly from the left makes a HUGE difference.**

</div>

<!--
You don't have to become a software engineer. Moving even slightly away from pure vibecoding makes an enormous difference. Writing a plan? Big win. Using git? Huge win. Not committing secrets? Potentially saves thousands of dollars.
-->

---

# What to Do Monday Morning

<v-clicks>

1. **Today:** Pick one existing tool/script and add a `PLAN.md` to it
2. **This week:** Set up `.gitignore` and `.env` on your active projects
3. **This month:** Start using feature branches for new work
4. **Ongoing:** Every new project starts with PLAN.md

</v-clicks>

<div v-click class="mt-8 text-center text-xl font-bold">

You don't have to do everything at once. Start with one habit.

</div>

<!--
Here's your Monday morning todo list. Don't try to retrofit everything at once. Pick ONE project, add a plan, set up .env and .gitignore. Start using branches for your next feature. These are small steps that compound over time.
-->

---
layout: center
class: text-center
---

# Questions, Concerns, Confessions?

<div class="text-xl mt-8">

What's still unclear?

What's the first thing you want to try?

</div>

<div v-click class="mt-12 text-sm opacity-60">

This is like a coding AA meeting. "Hi, I'm Jakub, and I hardcode my API keys." "Hi Jakub."

</div>

<!--
Open floor. What questions do you have? What's still confusing? What are you most excited to try? And — this is a safe space — who wants to confess something they've been doing that they now realize might be... problematic?
-->

---
layout: center
class: text-center
---

# Thank You!

**From Vibecoding to Sustainable Development**

<div class="mt-8">

**Jakub Dubec** · jakubdubec.me · github.com/Sibyx

</div>

<div class="mt-8 text-sm opacity-75">

Slides & resources: [sibyx.github.io/sustainable-vibecoding](https://sibyx.github.io/sustainable-vibecoding/)

PLAN.md template · .env patterns · Git cheat sheet (Slide 35)

</div>

<div class="mt-8 text-lg font-bold">

Go forth and may your vibes be sustainable, your branches be merged,<br>and your API keys be forever environment variables.

</div>

<div class="mt-4 text-xs opacity-40">

CC BY 4.0 · Jakub Dubec

</div>

<!--
Thank you! These slides are hosted online — you can revisit them anytime. The demo resources, templates, and cheat sheets are all in the repository. Find me on GitHub as @Sibyx or at jakubdubec.me.

Remember: you're not becoming engineers. You're becoming engineers' favorite kind of colleagues — the ones who plan, document, and don't commit secrets.
-->