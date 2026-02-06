---
draft: true
date: 2026-02-06
authors:
  - jdubec
categories:
  - Architecture
tags:
  - slides
  - presentation
  - structure
  - workshop
---

# IP-001: Presentation Structure & Complete Slide List

This proposal defines the full structure, slide-by-slide content, speaker notes, and narrative arc for the "From Vibecoding to Sustainable Development" workshop presentation. It replaces the default Slidev starter template with purpose-built content for a 3-hour interactive session targeting PPC/marketing professionals.

<!-- more -->

## Status

**Status**: Under Review
**Last Updated**: 2026-02-06
**Implementation**: Not started

## Problem Statement

The `slides.md` file currently contains the default Slidev starter template ("Welcome to Slidev", Navigation, Code examples, etc.) with zero workshop-specific content. We have comprehensive planning documents (`README.md`, `docs/PITCH.md`) but no actual slides to present.

- **Current situation**: Rich planning docs exist but the actual deliverable (the slides) is empty boilerplate.
- **Pain points**: Without a defined slide structure, we risk improvising the workshop, missing key topics, or running long/short on time.
- **Who is affected**: The speaker (jdubec), the workshop audience (PPC/marketing team), and anyone who accesses the hosted slides later as reference.
- **Consequences of not addressing**: The speaker shows up with a Slidev demo about LaTeX equations to a room full of marketers who just want their scripts to stop breaking. Awkward silence ensues.

## Proposed Solution

### Overview

Replace the entire `slides.md` content with a structured presentation of **~60-70 slides** organized into 8 sections matching the workshop flow from `README.md`. Each slide includes:

1. **Visual content** — what the audience sees (headlines, diagrams, code snippets, images)
2. **Speaker notes** — what the presenter says (talking points, jokes, audience prompts, timing cues)
3. **Interaction markers** — where audience participation happens (polls, questions, live demos)

The presentation follows a **story arc**: start from the audience's reality (vibecoding chaos), build through structured practices, and end with a co-created workflow they own.

### Key Components

1. **Opening Act (Slides 1-8)**: Hook, reality check, the "what is vibecoding" definition, and scary statistics to establish why this matters
2. **Documentation-First (Slides 9-15)**: The core mindset shift — plan before you prompt
3. **Tooling & AI Assistants (Slides 16-22)**: Positioning Claude Code, Cursor, and Google AI Studio as tools in a workflow, not magic wands
4. **Git & Collaboration (Slides 23-35)**: The longest section — visual git flow, live demo, merge conflict survival guide
5. **APIs & External Services (Slides 36-42)**: Demystifying APIs for non-engineers, connecting to their PPC world
6. **Security Basics (Slides 43-51)**: Horror stories, `.env` patterns, the "never paste secrets" rule
7. **Data Persistence (Slides 52-58)**: From "my data vanished" to structured storage options
8. **Wrap-Up & Team Workflow (Slides 59-65)**: Co-creating their checklist, Q&A, closing

### Architecture

```mermaid
graph LR
    A[slides.md<br/>Main entry] --> B[Section 0<br/>Opening & Hook]
    A --> C[Section 1<br/>Documentation-First]
    A --> D[Section 2<br/>Tooling & AI]
    A --> E[Section 3<br/>Git & Collaboration]
    A --> F[Section 4<br/>APIs]
    A --> G[Section 5<br/>Security]
    A --> H[Section 6<br/>Data Persistence]
    A --> I[Section 7<br/>Wrap-Up]

    style A fill:#2B90B6,color:#fff
    style E fill:#e67e22,color:#fff
```

All content lives in `slides.md` directly (no `pages/` splitting for now), using Slidev's `---` separator syntax. Sections are visually separated with section-title slides.

## Detailed Slide List

> **Convention**: Each slide entry includes a `[Layout]` tag, the slide title, content summary, and speaker notes. Speaker notes are marked with 🎤. Audience interaction is marked with 👥. Jokes/lighteners are marked with 😄.

---

### SECTION 0: Opening & Hook (15-20 min)

---

#### Slide 1: Title Slide
**[Layout: cover]**

**Content:**
- Title: "From Vibecoding to Sustainable Development"
- Subtitle: "How to make your AI-built tools less fragile, more shareable, and way less terrifying"
- Author, date, company/context

🎤 **Speaker Notes:**
"Welcome! Today is NOT about turning you into software engineers. I repeat — nobody here needs to learn what a linked list is. Today is about taking the cool things you're already building with AI and making them... survivable. Survivable by your teammates. Survivable by future-you at 3 AM when something breaks."

---

#### Slide 2: About Me / Credibility Slide
**[Layout: image-right]**

**Content:**
- Brief speaker intro
- "I write code for a living so you don't have to" angle
- Fun fact or ice breaker
- I am from FIIT STU. I am studying wireless networks and worked as software engineer for 10+ years.
- Faculty of informatics and information technologies on Slovak University of Technology in Bratislava.

🎤 **Speaker Notes:**
"Quick intro — I'm [name], I've been writing software for [X] years. I've leaked API keys, I've deleted production databases, I've written code that even I couldn't understand a week later. I'm basically a cautionary tale with a salary. And I'm here to help you avoid my greatest hits."

😄 **Joke:** "They say experience is the best teacher. My GitHub history says experience is the most expensive teacher."

---

#### Slide 3: The Vibe Coding Era
**[Layout: quote]**

**Content:**
- Andrej Karpathy's original tweet (Feb 3, 2025):
  > "There's a new kind of coding I call 'vibe coding', where you fully give in to the vibes, embrace exponentials, and forget that the code even exists."
- Source attribution
- Image/screenshot of the tweet if possible

🎤 **Speaker Notes:**
"Exactly one year ago today — February 3, 2025 — Andrej Karpathy, co-founder of OpenAI, posted this on X. He coined the term 'vibe coding.' The idea: you describe what you want in English, the AI writes the code, you never look at the code, you just see if the thing works. If it doesn't, you paste the error message back in and hope for the best. Sound familiar?"

**Background for speaker:** Karpathy described his workflow: "I 'Accept All' always, I don't read the diffs anymore. When I get error messages I just copy paste them in with no comment. The code grows beyond my usual comprehension." He clarified it's "not too bad for throwaway weekend projects."

**Reference:** [Karpathy's original tweet](https://x.com/karpathy/status/1886192184808149383) | [Wikipedia: Vibe coding](https://en.wikipedia.org/wiki/Vibe_coding)

---

#### Slide 4: Vibe Coding vs. AI-Assisted Development
**[Layout: two-cols]**

**Content:**

| Vibe Coding 🌊 | AI-Assisted Dev 🏗️ |
|---|---|
| Accept all, read nothing | Review, understand, test |
| "It works, ship it" | "It works, but *why*?" |
| Error? Paste it back | Error? Understand the root cause |
| Solo weekend project | Team tool that must survive Monday |
| The vibes are immaculate | The vibes are... documented |

🎤 **Speaker Notes:**
"Simon Willison — the creator of Django, one of the most popular web frameworks — made an important distinction: if an LLM wrote the code for you, and you then reviewed it, tested it, and can explain what it does to someone else — that's NOT vibe coding. That's just software development with a fancy assistant. The key question is: do you understand what your tool actually does?"

😄 **Joke:** "Vibe coding is like ordering food in a language you don't speak. Sometimes you get a steak. Sometimes you get a cow tongue. You won't know until you bite."

**Reference:** [Simon Willison: Not all AI-assisted programming is vibe coding](https://simonwillison.net/2025/Mar/19/vibe-coding/)

---

#### Slide 5: The Scale of... Vibes
**[Layout: fact]**

**Content:**
- **84%** of developers use or plan to use AI tools (Stack Overflow 2025)
- **25%** of Y Combinator W25 startups had 95% AI-generated codebases
- **45%** of AI-generated code contains security vulnerabilities (Veracode 2025)
- **39 million** secrets leaked on GitHub in 2024 alone
- **86%** of AI-generated code had XSS vulnerabilities in testing

🎤 **Speaker Notes:**
"Let's look at some numbers. 84% of developers are using AI tools — so this isn't fringe, this is mainstream. A quarter of the latest Y Combinator startups are almost entirely AI-generated code. But here's the kicker: nearly half of that AI-generated code has security holes. And 39 million — MILLION — secret keys and passwords were accidentally pushed to GitHub last year. That's not a bug, that's a lifestyle."

👥 **Audience prompt:** "Quick show of hands — who here has used ChatGPT, Claude, or Cursor to write code or scripts? ...And who has looked at the code it generated? ...And who understood it?"

**References:**
- [Stack Overflow 2025 Survey](https://stackoverflow.com/)
- [Veracode: AI code security](https://zencoder.ai/blog/vibe-coding-risks)
- [GitHub: 39M secrets leaked](https://cybersecuritynews.com/39m-secret-api-keys-credentials-leaked-from-github/)

---

#### Slide 6: Real Horror Stories
**[Layout: default]**

**Content:**
- 🔥 **Lovable (May 2025):** Vibe-coding platform generated apps where 170 out of 1,645 had vulnerabilities exposing personal information to anyone
- 💸 **Replit incident:** An AI-generated script accidentally deleted an entire production database
- 🔑 **Base44 SaaS breach:** AI-generated component allowed unauthenticated access to sensitive business logic
- 🤦 **Every day:** Live scrapers find accidentally-leaked API keys for OpenAI, Anthropic, AWS every second

🎤 **Speaker Notes:**
"These aren't hypothetical. In May 2025, Lovable — a company that LITERALLY sells vibe coding — had over 10% of its generated apps leaking personal data. Someone on Replit asked an AI to clean up their database. The AI interpreted 'clean up' very literally. It cleaned up everything. Including the data. There is a non-zero chance that someone in this room has pushed an API key to a public repo. The bots found it in about 30 seconds."

😄 **Joke:** "The AI said 'I'll handle the database.' It handled it the way a toddler handles a glass of juice."

**References:**
- [Accorian: Security Impact of Vibe Coding](https://www.accorian.com/security-impact-of-vibe-coding-deep-dive-part-1-of-2/)
- [The New Stack: Catastrophic Explosions](https://thenewstack.io/vibe-coding-could-cause-catastrophic-explosions-in-2026/)

---

#### Slide 7: But Vibe Coding Is Also Amazing
**[Layout: center]**

**Content:**
- "The power to automate your work without learning to code is genuinely revolutionary"
- Before AI: "I need to learn Python for 6 months to automate this report"
- After AI: "Hey Claude, write me a script that pulls Google Ads data and makes a CSV summary"
- **The goal today:** Keep the magic. Add the guardrails.

🎤 **Speaker Notes:**
"Now, I don't want to be the person who kills the vibe. What you're doing IS amazing. A year ago, automating your PPC reports required hiring a developer or spending months learning Python. Now you can describe what you want and get working code in minutes. That's incredible. We're not here to stop you from using AI. We're here to make sure the things you build don't catch fire when you're on vacation."

😄 **Joke:** "Vibe coding is like cooking with a flamethrower. You CAN make dinner. But maybe we should also talk about fire extinguishers."

---

#### Slide 8: Today's Roadmap
**[Layout: default]**

**Content:**
Visual roadmap / timeline:

```
📋 Plan First → 🤖 AI Tools → 🔀 Git → 🔌 APIs → 🔒 Security → 💾 Data → ✅ Your Workflow
```

- "We'll build understanding layer by layer, using a real example from YOUR work"
- Duration: ~3 hours with breaks
- Format: Mix of slides, live demos, and YOUR questions

🎤 **Speaker Notes:**
"Here's our roadmap. We're going to start by talking about planning before prompting. Then we'll look at your AI tools in a new light. Then the big one — git, which is how you stop overwriting each other's work. Then APIs, security, and data storage. And we'll end by building YOUR team's workflow together."

👥 **Audience prompt:** "Before we dive in — quick question. Show me or tell me: what's one internal tool or script you've built recently? What does it do? What breaks?"

---

### SECTION 1: Documentation-First Planning (25-30 min)

---

#### Slide 9: Section Title — "Plan Before You Prompt"
**[Layout: section]**

**Content:**
- Large text: "Plan Before You Prompt"
- Subtitle: "The difference between 'vibe coding' and 'building something real'"

🎤 **Speaker Notes:**
"This is the single most important habit change we'll talk about today. Everything else — git, security, data — builds on this foundation. If you take ONE thing away from this workshop, let it be this section."

---

#### Slide 10: The Prompt Problem
**[Layout: two-cols]**

**Content:**

**Without a plan:**
```
"Build me a PPC dashboard"
```
→ AI builds... something. Maybe not what you wanted. You iterate 47 times. You forget what you asked for. The code is a Frankenstein's monster of prompt iterations.

**With a plan:**
```
"Here is PLAN.md with requirements,
data sources, and security rules.
Implement it step by step."
```
→ AI follows a spec. You can review against the plan. Your teammate can understand what was built.

🎤 **Speaker Notes:**
"Here's what typically happens. You open Claude or Cursor and type 'build me a PPC dashboard.' The AI does... something. It looks kind of right. You say 'add a filter.' It adds a filter but breaks the chart. You say 'fix the chart.' It fixes the chart but removes the filter. Three hours later you have a pile of code that sort of works, nobody understands it, and you're not sure which version was the good one."

😄 **Joke:** "Prompting AI without a plan is like giving a taxi driver directions one turn at a time. 'Go left. No wait, go right. Actually, go back.' You'll get somewhere, but probably not where you wanted."

---

#### Slide 11: The PLAN.md Template
**[Layout: default]**

**Content:**
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

## Security Notes
- Where API keys live
- What MUST NOT go into git

## Files We Expect
- plan/PLAN.md
- src/main_script
- src/api_client
- data/ (for outputs)
```

🎤 **Speaker Notes:**
"This is the template. It's not a PhD thesis — it's maybe 20 lines of text that answer the basic questions: what are we building, where does data come from, and what should NEVER be in the code? You write this BEFORE opening your AI tool. Then you hand this to Claude, Cursor, or whatever you use and say: 'You are the implementer. Here is the plan. Ask me questions if anything is unclear.'"

**Key point for speaker:** Emphasize this is a CONVERSATION STARTER with the AI, not a rigid spec. The plan helps the AI ask better questions and produce more coherent code.

---

#### Slide 12: Live Exercise — Let's Write a Plan Together
**[Layout: center]**

**Content:**
- 👥 Interactive: "Let's pick a real tool from your team and write a plan for it"
- Whiteboard / shared doc time
- Template on screen for reference

🎤 **Speaker Notes:**
"OK, let's do this for real. Who has a script or tool they've built recently — or one they WISH they had? Doesn't have to be fancy. 'A script that pulls our Google Ads data into a spreadsheet' is perfect."

👥 **Audience exercise (10-15 min):**
1. Pick one real tool/script from the audience
2. Fill in the PLAN.md template together on screen
3. Point out: "See? Now anyone on your team knows what this thing does. Including the AI."

---

#### Slide 13: How to Hand the Plan to AI
**[Layout: image-right]**

**Content:**
Example prompt:
```
You are implementing a tool based on the plan below.
Follow it as the specification.
Ask me questions before making assumptions.

[paste PLAN.md contents]
```

Key principles:
- AI is the **implementer**, not the **architect**
- The plan is the **contract** between you and the AI
- If the AI goes off-script, point it back to the plan

🎤 **Speaker Notes:**
"The magic phrase is: 'Ask me questions before making assumptions.' This changes the dynamic completely. Instead of the AI guessing what you want and building something random, it actually checks with you. You become the project manager. The AI becomes the developer who reads the brief first."

---

#### Slide 14: Plan-Driven vs. Vibe-Driven Results
**[Layout: two-cols]**

**Content:**
Visual comparison:

**Vibe-driven project timeline:**
```
Day 1: "Build a dashboard" → works!
Day 2: "Add filters" → half-broken
Day 3: "Fix it" → different half broken
Day 5: "Start over"
Day 7: "I hate coding"
```

**Plan-driven project timeline:**
```
Day 1: Write PLAN.md (30 min)
Day 1: AI implements step 1-3
Day 2: Review, adjust plan, AI implements step 4-5
Day 3: Working tool that matches the plan
Day 5: Teammate reads PLAN.md, understands everything
```

🎤 **Speaker Notes:**
"I've seen both of these timelines play out in real teams. The vibe-driven approach feels faster on day one, but by day five you're starting over. The plan-driven approach feels slower at first — 'why am I writing a document instead of coding?' — but by day five you have something that works AND that someone else can maintain."

---

#### Slide 15: The Bus Factor
**[Layout: center]**

**Content:**
- 🚌 **Bus Factor:** "If [person] gets hit by a bus, can anyone else continue their work?"
- Without documentation: Bus factor = 1
- With PLAN.md + git: Bus factor = your whole team
- "This isn't about buses. It's about vacations, sick days, and switching projects."

🎤 **Speaker Notes:**
"In software engineering, we have this morbid concept called the 'bus factor.' If the person who built this tool gets hit by a bus — or, more realistically, goes on vacation or quits — can anyone else figure out what the tool does and keep it running? If the answer is no, you have a bus factor of one. PLAN.md is the cheapest insurance policy against a bus factor of one."

😄 **Joke:** "In our industry, we've rebranded this to the 'lottery factor.' Same concept, but you're happy for the person instead of traumatized."

---

### SECTION 2: Tooling & AI Assistants (15-20 min)

---

#### Slide 16: Section Title — "Your AI Toolkit"
**[Layout: section]**

**Content:**
- Large text: "Your AI Toolkit"
- Subtitle: "Same tools, better workflow"

---

#### Slide 17: The Tooling Landscape
**[Layout: default]**

**Content:**
Three-column layout:

| Claude Code | Cursor | Google AI Studio |
|---|---|---|
| Terminal-based AI agent | AI-powered IDE | Prompt playground |
| Multi-file reasoning | Composer mode for project-wide edits | Test prompts & transformations |
| Reads your whole project | `.cursorrules` for context | Not a full IDE |
| Best for: complex multi-file tasks | Best for: daily coding workflow | Best for: experimenting |

🎤 **Speaker Notes:**
"You probably already use one or more of these. Let's quickly position them. Cursor is the one most of you likely use daily — it's an IDE (code editor) with AI built in. Claude Code is a terminal agent that can reason about your whole project at once. Google AI Studio is more of a sandbox for testing prompts. They're all useful, but for different things."

👥 **Audience prompt:** "Quick poll: who uses Cursor? Claude/ChatGPT? Google AI Studio? Something else?"

---

#### Slide 18: Cursor Power Moves
**[Layout: default]**

**Content:**
- **Composer mode:** Multi-file edits guided by context
- **`.cursorrules` file:** "Here's how this project works" — persistent project context
- **Cmd+K:** Quick inline edits
- **Pro tip:** Drop your `PLAN.md` into the project root. Cursor reads it automatically.

🎤 **Speaker Notes:**
"For Cursor users — there are two modes that matter. Cmd+K is for quick edits in a single file. Composer is for bigger changes across multiple files. The game-changer is the `.cursorrules` file — you put it in your project root and it tells Cursor things like 'always use environment variables for API keys' or 'follow the structure in PLAN.md.' It's like giving the AI a permanent cheat sheet about your project."

---

#### Slide 19: Claude Code Power Moves
**[Layout: default]**

**Content:**
- **CLAUDE.md file:** Project instructions Claude reads automatically
- **Multi-file reasoning:** "Read the whole project, then implement step 3 of the plan"
- **Best with a plan:** Claude Code + PLAN.md = focused implementation

🎤 **Speaker Notes:**
"Claude Code works differently — it's in your terminal, not in an IDE. But it's incredibly good at reading your entire project, understanding the structure, and making changes across multiple files. The `CLAUDE.md` file works like `.cursorrules` — it's permanent instructions. You can put things like 'never hardcode API keys' or 'always check PLAN.md before making changes' and Claude will follow those rules every time."

---

#### Slide 20: The Golden Rule of AI Tooling
**[Layout: center]**

**Content:**
> "The AI is a junior developer with infinite energy and zero judgment. You are the senior developer. Act like it."

- ✅ Give it a plan
- ✅ Review its output
- ✅ Ask it to explain what it did
- ❌ Accept all without reading
- ❌ Paste production secrets into prompts
- ❌ Assume it knows your business logic

🎤 **Speaker Notes:**
"Here's the mental model I want you to walk away with. The AI is a junior developer who works 24/7, never sleeps, never complains, and types at the speed of light. But like any junior developer, it has terrible judgment. It will confidently write code that looks perfect but has a gaping security hole. It will reorganize your project in a way that makes sense to no one. YOUR job is to be the senior developer who reviews, questions, and approves. The plan is how you give direction. The review is how you maintain quality."

😄 **Joke:** "Think of AI as that intern who's really enthusiastic but once reorganized the entire filing system alphabetically by the third word of each document title. Technically sorted! Practically useless."

---

#### Slide 21: MCP & llms.txt (Just Know They Exist)
**[Layout: default]**

**Content:**
- **MCP (Model Context Protocol):** A standard for connecting AI tools to external services (databases, APIs, etc.)
- **llms.txt:** Like robots.txt but for AI — tells LLMs how to interact with your service
- "You don't need to implement these today. Just know they exist for when your tools get more complex."

🎤 **Speaker Notes:**
"Two quick concepts for your radar. MCP is a way to let your AI tools directly talk to services — like connecting Claude directly to your database or GitHub. llms.txt is a standard file you put on a website to guide AI tools. Think of these as plumbing — you don't need to be a plumber today, but it's good to know plumbing exists for when you need it."

---

#### Slide 22: Tool Comparison Summary
**[Layout: default]**

**Content:**
Decision matrix:

| I want to... | Use... |
|---|---|
| Edit code in a file | Cursor (Cmd+K) |
| Restructure a project | Cursor Composer or Claude Code |
| Test a prompt idea | Google AI Studio |
| Implement a full plan | Claude Code with PLAN.md |
| Quick one-off script | Any of them + the PLAN.md habit |

🎤 **Speaker Notes:**
"Here's your cheat sheet. Don't overthink tool choice — pick the one you're comfortable with. The WORKFLOW matters more than the tool. Plan → implement → review. Works with any of them."

---

### ☕ BREAK SLIDE

#### Slide 23: Break Time
**[Layout: center]**

**Content:**
- "5-minute break"
- "Stretch, hydrate, check your ads aren't on fire"
- Fun fact or meme about coding

😄 **Fun fact for screen:** "In 2024, GitHub users accidentally leaked enough API keys to fill 39 million Post-it notes. That's about 780 kilometers of Post-it notes. From here to [relevant landmark]."

---

### SECTION 3: Git & Collaboration (40-45 min)

---

#### Slide 24: Section Title — "Git: Your Collaborative Safety Net"
**[Layout: section]**

**Content:**
- Large text: "Git: Your Collaborative Safety Net"
- Subtitle: "The 'undo' button for your entire project — and how to stop overwriting each other's work"

---

#### Slide 25: The Problem Without Git
**[Layout: default]**

**Content:**
Illustration of chaos:
```
📁 campaign-tool-final.py
📁 campaign-tool-final-v2.py
📁 campaign-tool-final-v2-FIXED.py
📁 campaign-tool-final-v2-FIXED-johns-version.py
📁 campaign-tool-DONT-TOUCH.py
📁 campaign-tool-final-ACTUALLY-FINAL.py
```

🎤 **Speaker Notes:**
"Raise your hand if this looks familiar. You have a file. You make a copy. Your colleague makes a copy of the copy. Someone emails their version. Now you have six versions and nobody knows which one works. This is what git solves. Git is version control — it's like Google Docs' version history, but for code."

👥 **Audience prompt:** "What happens right now when two of you work on the same script?"

😄 **Joke:** "Developers have a saying: 'There are two hard things in computer science: cache invalidation, naming things, and off-by-one errors.' The file naming problem is #2."

---

#### Slide 26: Git in 60 Seconds
**[Layout: default]**

**Content:**
Simple visual:
```
Your computer          GitHub/GitLab (the cloud)
┌─────────┐           ┌─────────────┐
│ You edit │ ──push──→ │ Everyone    │
│ files    │ ←pull──── │ sees it     │
└─────────┘           └─────────────┘
```

Core concepts (non-jargon):
- **Repository (repo):** Your project folder, but tracked
- **Commit:** A save point with a description ("added campaign filter")
- **Push:** Upload your save points to the shared location
- **Pull:** Download everyone else's save points
- **Branch:** Your own parallel copy to work on without breaking things

🎤 **Speaker Notes:**
"Git is actually simple if you strip away the jargon. A repo is just your project folder with superpowers. A commit is a save point — like checkpoints in a video game. You push to share your work, pull to get others' work. And a branch is your personal workspace where you can experiment without messing up the main version."

---

#### Slide 27: The Branch Model — Why It Matters
**[Layout: default]**

**Content:**
Visual branch model:
```
main         ●━━━━━━━━━━━━━━━━●━━━━━━● (stable, production)
              \              ↗
develop        ●━━━━●━━━━●━━● (integration, testing)
                \  ↗     \  ↗
feature/anna    ●━●       \
feature/jan              ●━● (your work)
```

Three branches you need to know:
1. **main** — the "production" version that works. Don't touch this directly.
2. **develop** — where features get merged and tested together.
3. **feature/your-name-thing** — YOUR workspace. Go wild here.

🎤 **Speaker Notes:**
"Here's the model. Think of it like a highway system. Main is the highway — it's smooth, it's paved, traffic flows. Develop is the on-ramp where we check if new things are safe. Feature branches are side roads where you build new stuff. When your side road is done, you merge it onto the on-ramp, test it, and then it joins the highway. Nobody drives construction equipment on the highway."

😄 **Joke:** "The 'main' branch is like the kitchen at a restaurant. The feature branch is where you experiment with recipes. You NEVER experiment in the kitchen during dinner service."

---

#### Slide 28: Branch Naming Convention
**[Layout: default]**

**Content:**
```
feature/anna-add-campaign-filter
feature/jan-fix-csv-export
feature/petra-update-api-client
```

Rules:
- Start with `feature/`
- Include your name (so we know whose branch it is)
- Describe what you're doing (short and clear)
- Use hyphens, not spaces

🎤 **Speaker Notes:**
"Simple naming convention. Start with 'feature/', add your name, describe the change. This way when someone looks at the list of branches, they immediately know who's working on what. No more guessing games."

---

#### Slide 29: The Git Workflow — Step by Step
**[Layout: default]**

**Content:**
```
1. git checkout develop          ← Start from develop
2. git checkout -b feature/me   ← Create your branch
3. ... do your work ...
4. git add my-changed-files     ← Stage changes
5. git commit -m "what I did"   ← Save checkpoint
6. git push                     ← Upload to GitHub
7. Create Pull Request           ← Ask to merge
8. Team reviews → Merge! 🎉
```

🎤 **Speaker Notes:**
"Here's the workflow. Step 1: start from the develop branch. Step 2: create your own feature branch. Steps 3-5: work normally and save checkpoints. Step 6: push to GitHub. Step 7: create a pull request — which is basically saying 'hey team, I'm done, please look at this before we merge it.' Step 8: someone glances at it, approves, and it gets merged."

**Important for speaker:** If using GUI tools (GitHub Desktop, VS Code), show the equivalent buttons. Don't assume CLI comfort.

---

#### Slide 30: What's a Pull Request?
**[Layout: image-right]**

**Content:**
- A **Pull Request (PR)** = "I made changes. Please review before merging."
- Shows a visual of a GitHub PR interface (screenshot or mockup)
- It's a conversation:
  - "Here's what I changed and why"
  - "Looks good!" or "Hey, you left an API key in line 42"

🎤 **Speaker Notes:**
"A pull request is your way of saying 'I finished my feature, can someone take a look before we merge it into develop?' It shows exactly what changed. Your teammate can see every line, ask questions, suggest changes. This is where you catch mistakes — like accidentally committing an API key — before they reach the shared code."

😄 **Joke:** "A pull request is like asking someone to proofread your email before you send it to the CEO. Except the email is code and the CEO is production."

---

#### Slide 31: Commit Messages That Don't Suck
**[Layout: two-cols]**

**Content:**

**Bad commit messages:**
```
"stuff"
"fixed it"
"asdfgh"
"wip"
"final commit"
"no really final this time"
```

**Good commit messages:**
```
"add campaign filter by date range"
"fix CSV export missing header row"
"update API client to use env variables"
"remove hardcoded API key from config"
```

🎤 **Speaker Notes:**
"Your commit message is a gift to future-you. Six months from now, you'll look at the history and either see 'add campaign filter by date range' — great, you know exactly what happened — or 'stuff.' Which future do you prefer? The rule is simple: describe WHAT you changed and WHY."

😄 **Joke:** "The most terrifying words in software: 'git log' shows 47 commits all named 'fix'. Fix WHAT? Nobody knows. It's like a horror movie where the journal entries just say 'the thing happened again.'"

---

#### Slide 32: Live Demo — GitHub Desktop / VS Code Git
**[Layout: center]**

**Content:**
- 👥 Live Demo
- "Let's create a repo, make branches, and merge — using GUI tools"
- Step-by-step walkthrough

🎤 **Speaker Notes:**
"OK, let's do this live. I'm going to open [GitHub Desktop / VS Code] and we'll walk through the whole flow. Create a repo, create a branch, make a change, commit, push, create a pull request, and merge. If you have your laptop, follow along."

👥 **Audience exercise (15 min):**
1. Open GitHub Desktop or VS Code
2. Clone the workshop repo (or create a new one)
3. Create a feature branch with your name
4. Edit PLAN.md (add your name to a list or similar)
5. Commit, push, create PR
6. Merge into develop

---

#### Slide 33: The Merge Conflict (Don't Panic)
**[Layout: default]**

**Content:**
What a merge conflict looks like:
```
<<<<<<< HEAD
report_format = "csv"
=======
report_format = "xlsx"
>>>>>>> feature/jan-excel-export
```

Translation: "Two people changed the same line. Git doesn't know which version you want. Please decide."

🎤 **Speaker Notes:**
"At some point, this WILL happen. Two people change the same line. Git can't guess which one is right, so it shows you both versions and asks you to pick. The top section is what's currently in the branch. The bottom section is what you're trying to merge. You delete the markers, keep the version you want (or combine them), save, and commit. That's it. It looks scary the first time, but it's literally just 'which version do you want?'"

😄 **Joke:** "A merge conflict is git's way of saying 'I don't get paid enough to make this decision for you.'"

---

#### Slide 34: Disaster Recovery with Git
**[Layout: default]**

**Content:**
- "I broke everything!" → `git stash` or `git checkout .` (discard changes)
- "I need the version from Tuesday" → `git log` → `git checkout <commit>`
- "Someone merged bad code" → `git revert`
- "I committed secrets" → **ROTATE THE KEY IMMEDIATELY.** Then clean git history.

🎤 **Speaker Notes:**
"Here's your emergency playbook. Broke everything? Git can undo it. Need an old version? Git has it. Someone merged bad code? Git can revert it. But — and this is critical — if you committed a secret like an API key, git history is NOT enough. Even if you delete it in the next commit, it's still in the history. Anyone who clones the repo has it. Bots scrape GitHub every second looking for exactly this. The ONLY safe response is: rotate the key. Get a new one. The old one is compromised."

---

#### Slide 35: Git Cheat Sheet
**[Layout: default]**

**Content:**
One-page visual cheat sheet:

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

🎤 **Speaker Notes:**
"This is your cheat sheet. Bookmark this slide, screenshot it, tattoo it — whatever works. These 8 commands cover 95% of what you'll ever need. If you forget everything else, remember: branch, commit, push, pull request."

---

### SECTION 4: External Services & APIs (20-25 min)

---

#### Slide 36: Section Title — "APIs: How Your Tools Talk to the World"
**[Layout: section]**

**Content:**
- Large text: "APIs: Where Your Data Actually Comes From"
- Subtitle: "Making the magical black box slightly less magical"

---

#### Slide 37: What Is an API? (No Jargon Version)
**[Layout: default]**

**Content:**
Restaurant analogy:
```
You (the app)     Waiter (the API)     Kitchen (the service)
┌─────────┐      ┌─────────────┐      ┌──────────────┐
│ "I want │      │ Takes your  │      │ Google Ads   │
│ campaign │ ──→  │ request,    │ ──→  │ Meta Ads     │
│ data for │      │ brings back │      │ GA4          │
│ January" │ ←──  │ the result  │ ←──  │ etc.         │
└─────────┘      └─────────────┘      └──────────────┘
```

🎤 **Speaker Notes:**
"An API is just a messenger. You send a request — 'give me campaign data for January' — and it brings back the answer. That's it. Think of it like a restaurant: you don't go into the kitchen to cook. You tell the waiter what you want, the kitchen makes it, and the waiter brings it back. The API is the waiter. The menu is the API documentation — it tells you what you can order."

😄 **Joke:** "An API is a waiter that never judges your order. 'You want ALL the data for the last 3 years grouped by hour? Sure thing. That'll be 47 seconds and your rate limit for today.'"

---

#### Slide 38: APIs in Your PPC World
**[Layout: default]**

**Content:**
APIs you probably already use (whether you know it or not):
- **Google Ads API** — campaign data, keywords, budgets
- **Google Analytics 4 API** — website traffic, conversions
- **Meta Marketing API** — Facebook/Instagram ads
- **Google Sheets API** — reading/writing spreadsheets
- **Slack API** — sending notifications

When you use a script that "pulls data from Google Ads," it's using an API.

🎤 **Speaker Notes:**
"Every time you use a script that gets your ad data, it's calling an API behind the scenes. The Google Ads API lets you read campaign data, adjust budgets, pause ads. The GA4 API gives you analytics. The Meta API does the same for Facebook and Instagram. When your AI-generated script 'pulls data from Google Ads,' this is what it's doing — making API calls."

---

#### Slide 39: Anatomy of an API Call
**[Layout: default]**

**Content:**
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

🎤 **Speaker Notes:**
"Here's what an API call looks like in code. Four parts: WHERE to ask (the URL), WHO's asking (your authentication token — this is the secret part!), WHAT to ask (parameters like date range), and the response that comes back. See that `YOUR_TOKEN_HERE`? That's the thing that must NEVER be hardcoded in your script. That's what we'll cover in the security section."

---

#### Slide 40: When APIs Go Wrong
**[Layout: default]**

**Content:**
Common API errors and what they mean:
- **401 Unauthorized** — "Who are you? Your key is wrong or expired"
- **403 Forbidden** — "I know who you are, but you can't do that"
- **404 Not Found** — "That endpoint/resource doesn't exist"
- **429 Too Many Requests** — "Slow down! You're asking too much too fast"
- **500 Internal Server Error** — "It's not you, it's us"

🎤 **Speaker Notes:**
"When your script stops working and throws an error, these numbers tell you why. 401 means your credentials are wrong — did your token expire? 429 means you're hitting the API too fast — most APIs have rate limits. 500 means Google/Meta's servers are having a bad day and there's nothing you can do except wait. Teach your AI to handle these errors in the code it generates."

😄 **Joke:** "HTTP 418 'I'm a Teapot' is a real error code. It was an April Fools' joke in 1998. Developers are the kind of people who embed jokes into internet standards. We're a fun bunch."

---

#### Slide 41: Rate Limits — The API Speed Limit
**[Layout: default]**

**Content:**
- Most APIs limit how many requests you can make per minute/day
- Google Ads API: varies by access level
- Exceeding the limit = your script stops working temporarily
- **Solution:** Build in delays, cache data, don't re-fetch what you already have

🎤 **Speaker Notes:**
"Every API has speed limits. It's like a highway — there's a maximum number of cars per minute. If your script hammers an API with thousands of requests, it'll get temporarily blocked. Tell your AI: 'Add rate limiting and caching to avoid hitting API limits.' This is one of those things AI-generated code often misses."

---

#### Slide 42: API Transition to Security
**[Layout: center]**

**Content:**
- "To call ANY of these APIs, you need **credentials**"
- Credentials = API keys, tokens, secrets
- "Where these credentials live determines whether your tool is safe or a ticking time bomb"
- ➡️ Let's talk security...

🎤 **Speaker Notes:**
"So now you know what APIs are and how they work. The key takeaway: every API call requires credentials. Where you store those credentials is the single biggest security decision you'll make. And that's our next topic."

---

### SECTION 5: Security Basics (20-25 min)

---

#### Slide 43: Section Title — "Security: Don't Be a Statistic"
**[Layout: section]**

**Content:**
- Large text: "Security: Don't Be a Statistic"
- Subtitle: "39 million secrets leaked on GitHub in 2024. Let's not add to that number."

---

#### Slide 44: The Scariest Slide in This Presentation
**[Layout: default]**

**Content:**
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

What happens next:
1. ⏱️ **30 seconds:** Automated bots find the key
2. 💸 **5 minutes:** Someone starts using your API quota
3. 📧 **Next morning:** You get a bill for $4,000

🎤 **Speaker Notes:**
"This is real code from a real GitHub repo — with changed values, obviously. Someone put their Google Ads API credentials directly in the code, pushed it to a public repo, and within minutes, bots found it. Automated scrapers scan every new commit on GitHub looking for patterns that look like API keys. They find them in about 30 seconds. Once found, they're sold, shared, or used immediately. Last year, 39 million secrets were found this way."

**Reference:** [GitHub: 39M secrets leaked in 2024](https://cybersecuritynews.com/39m-secret-api-keys-credentials-leaked-from-github/)

---

#### Slide 45: The Three Rules of Secrets
**[Layout: center]**

**Content:**

### 🔒 Rule 1: Secrets NEVER go in code
### 🔒 Rule 2: Secrets NEVER go in git
### 🔒 Rule 3: Secrets NEVER go into AI prompts

That's it. That's the whole security section. Everything else is implementation details.

🎤 **Speaker Notes:**
"If you remember nothing else from the security section, remember these three rules. Never put secrets in code — use environment variables. Never put secrets in git — use .gitignore. Never paste production API keys into ChatGPT, Claude, or Cursor prompts. You can say 'the API key is stored in the environment variable called GOOGLE_ADS_KEY' without actually pasting the key. The AI doesn't need your real key to write the code."

---

#### Slide 46: The .env Pattern
**[Layout: two-cols]**

**Content:**

**The `.env` file (NOT committed to git):**
```
# .env - THIS FILE IS SECRET
GOOGLE_ADS_API_KEY=AIzaSyD-9tSrke72PouQMnMX...
META_ACCESS_TOKEN=EAABsbCS1234...
DATABASE_URL=postgresql://user:pass@localhost/db
```

**Your code reads from environment:**
```python
import os

api_key = os.environ["GOOGLE_ADS_API_KEY"]
# ← No secrets in the code!
```

**Your `.gitignore` file:**
```
.env
.env.local
*.pem
credentials.json
```

🎤 **Speaker Notes:**
"Here's the pattern. You create a file called `.env` in your project root. This is where ALL your secrets live. Your code reads from this file — it never has the actual key value in the source code. And critically, you add `.env` to `.gitignore`, which tells git to pretend the file doesn't exist. It will never be committed, never be pushed to GitHub."

---

#### Slide 47: The .env.example Pattern
**[Layout: default]**

**Content:**
```
# .env.example - THIS FILE IS COMMITTED (shows structure, not values)
GOOGLE_ADS_API_KEY=your-key-here
META_ACCESS_TOKEN=your-token-here
DATABASE_URL=postgresql://user:pass@host/dbname
```

Why?
- New teammate joins → copies `.env.example` to `.env` → fills in their own keys
- Documents WHAT environment variables exist without exposing values
- This file IS committed to git — it's just a template

🎤 **Speaker Notes:**
"But wait — if .env is not in git, how does a new person know what environment variables they need? That's what .env.example is for. It's a template that shows the variable NAMES but not the actual VALUES. It gets committed to git. When someone new joins, they copy it to .env and fill in their own credentials."

---

#### Slide 48: Quick Security Audit
**[Layout: center]**

**Content:**
👥 Interactive exercise:

"Let's do a 2-minute security check on one of your existing projects:"
- [ ] Are there any API keys directly in the code?
- [ ] Is there a `.gitignore` file?
- [ ] Does `.gitignore` include `.env`?
- [ ] Are credentials in a `.env` file (or similar)?
- [ ] Have any secrets ever been committed to git history?

🎤 **Speaker Notes:**
"Let's do this right now. Pull up one of your existing projects. Can you find any API keys or passwords directly in the Python/JS files? Is there a .gitignore? Does it mention .env? This is a quick health check. No judgment — we're here to fix things, not blame."

👥 **Audience exercise (5 min):** Walk through one real project and check these items.

---

#### Slide 49: "But I Already Committed a Secret..."
**[Layout: default]**

**Content:**
If a secret was ever in git history, even if you deleted it later:

1. **ROTATE THE KEY IMMEDIATELY** — get a new one from the API provider
2. The old key is compromised forever (bots scrape git history too)
3. Optionally: clean git history with `git filter-branch` or BFG Repo Cleaner
4. But step 1 is the only thing that actually matters

🎤 **Speaker Notes:**
"This is the most important thing I'll say today about security: if an API key was EVER in your git history — even for one commit — consider it compromised. Deleting it in the next commit doesn't help. Git keeps the full history. Bots can read old commits. The ONLY fix is to go to the API provider, revoke the old key, and generate a new one. Do step 1 and you're safe. Skip step 1 and you're crossing your fingers."

---

#### Slide 50: AI Tools and Secrets
**[Layout: default]**

**Content:**
- ✅ "The API key is stored in the `GOOGLE_ADS_KEY` environment variable"
- ❌ "The API key is `AIzaSyD-9tSrke72PouQMnMX-a7eZSW0jkFMBWY`"

What you CAN tell AI tools:
- Variable names, file structure, patterns
- What the API does, what data it returns

What you CANNOT tell AI tools:
- Actual key values, passwords, tokens
- Connection strings with real credentials

🎤 **Speaker Notes:**
"When you're working with Claude, Cursor, or ChatGPT, you can describe everything ABOUT your secrets without revealing them. Say 'I have an environment variable called GOOGLE_ADS_KEY' — the AI can write all the code it needs around that. Never paste the actual key value into any AI tool. These conversations may be logged, used for training, or intercepted."

---

#### Slide 51: Security Cheat Sheet
**[Layout: default]**

**Content:**
| Situation | Do This |
|---|---|
| New project | Create `.env` + `.gitignore` FIRST |
| Need to share credentials with teammate | Use a password manager, NEVER Slack/email |
| AI tool asks for API key | Give the variable name, not the value |
| Found a secret in git | Rotate key immediately, then clean history |
| Not sure if something is a secret | If in doubt, treat it as a secret |
| Setting up a new service | Immediately put credentials in `.env` |

🎤 **Speaker Notes:**
"Bookmark this. When in doubt about anything security-related, check this cheat sheet. The golden rule: if you're not sure whether something is a secret, treat it as one. Better safe than explaining to your boss why someone ran up a $4,000 API bill on your leaked credentials."

---

### SECTION 6: Data Persistence (20-25 min)

---

#### Slide 52: Section Title — "Data Persistence: Where Does Your Data Live?"
**[Layout: section]**

**Content:**
- Large text: "Where Does Your Data Live?"
- Subtitle: "What happens when you close the tab, restart the script, or turn off your laptop"

---

#### Slide 53: The Persistence Spectrum
**[Layout: default]**

**Content:**
```
Level 0: RAM only        → "Close the tab, data is gone"
Level 1: LocalStorage    → "Browser remembers, but only on your machine"
Level 2: Files (CSV/JSON)→ "Data survives, shareable, but manual"
Level 3: SQLite          → "Real database, single file, no server needed"
Level 4: PostgreSQL      → "Full database server, multi-user, production-grade"
```

Arrows showing when to upgrade:
- Level 0→1: "I need data between sessions"
- Level 1→2: "I need to share data or analyze it"
- Level 2→3: "I need to query data in complex ways"
- Level 3→4: "Multiple people access data simultaneously"

🎤 **Speaker Notes:**
"Data persistence is just a fancy way of saying 'where does your data live when the program isn't running?' The spectrum goes from 'vanishes when you close the tab' to 'enterprise database that'll survive a nuclear winter.' Most of your PPC tools need to be somewhere in the Level 2-3 range."

---

#### Slide 54: Level 2 Deep Dive — Files
**[Layout: two-cols]**

**Content:**

**CSV (Comma-Separated Values):**
```csv
campaign,clicks,cost,conversions
Brand,1234,450.00,89
Generic,5678,1200.00,42
```
- ✅ Opens in Excel/Sheets
- ✅ Humans can read it
- ❌ Slow with large data
- ❌ No data types (everything is text)

**Parquet:**
- ✅ 10-100x smaller than CSV
- ✅ Preserves data types
- ✅ Blazing fast for analysis
- ❌ Can't open in Excel directly
- ❌ Need Python/tools to read

🎤 **Speaker Notes:**
"For most of your scripts, files are the right answer. CSV is the universal format — everyone knows it, it opens in Excel. Parquet is the fancy version — it's compressed, typed, and fast. If your script saves daily campaign snapshots, CSV is fine for small data. If you're storing millions of rows of hourly data, Parquet is the way to go."

---

#### Slide 55: Level 3 — SQLite (The Sweet Spot)
**[Layout: default]**

**Content:**
```python
import sqlite3

# The entire database is ONE file
db = sqlite3.connect("campaigns.db")

# Create a table
db.execute("""
    CREATE TABLE IF NOT EXISTS daily_stats (
        date TEXT,
        campaign TEXT,
        clicks INTEGER,
        cost REAL,
        conversions INTEGER
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

🎤 **Speaker Notes:**
"SQLite is the magic middle ground. It's a real database — you can query it with SQL — but it's just a single file. No server to install, no configuration, no passwords. You just point at a file and it works. For PPC tools that need to accumulate data over time, this is often the perfect choice. Tell your AI: 'store the data in SQLite' and it'll set this up for you."

---

#### Slide 56: When to Upgrade (Decision Tree)
**[Layout: default]**

**Content:**
```mermaid
graph TD
    A[Does data need to survive between runs?] -->|No| B[RAM / Variables<br/>Level 0]
    A -->|Yes| C[Do multiple people access it simultaneously?]
    C -->|No| D[Is the data complex / needs querying?]
    C -->|Yes| E[PostgreSQL<br/>Level 4]
    D -->|No| F[CSV / Parquet files<br/>Level 2]
    D -->|Yes| G[SQLite<br/>Level 3]
```

🎤 **Speaker Notes:**
"Here's your decision tree. Start simple and upgrade when you hit a wall. Does data need to survive between runs? If no, you don't need persistence at all. If yes, do multiple people need it at the same time? If no, is the data complex? Simple data → files. Complex queries → SQLite. Multiple simultaneous users → PostgreSQL. Don't over-engineer. Start with files or SQLite. You can always upgrade later."

---

#### Slide 57: The "Is This Throwaway?" Test
**[Layout: center]**

**Content:**
Ask yourself two questions:
1. **"Will someone other than me use this?"** → Needs persistence + documentation
2. **"Will I need this data next week?"** → Needs file/database storage

| Throwaway | Real Tool |
|---|---|
| One-time analysis | Daily reporting |
| Prototype/demo | Team dashboard |
| Exploring data | Automated pipeline |
| → Level 0-1 is fine | → Level 2-3 minimum |

🎤 **Speaker Notes:**
"Not everything needs a database. If you're doing a one-time analysis, a Jupyter notebook with no persistence is totally fine. But if your tool runs daily, feeds into decisions, or is used by your team — that's a real tool and it needs real storage. The 'throwaway vs. real' distinction is the most important question you can ask before building anything."

---

#### Slide 58: Data Persistence in PLAN.md
**[Layout: default]**

**Content:**
Add to your plan:
```markdown
## Data Storage
- **Type:** CSV files / SQLite / PostgreSQL
- **Location:** data/ directory (git-ignored if large)
- **Retention:** Keep last 90 days of daily snapshots
- **Backup:** [how/when]
- **Who accesses:** Just me / team / external
```

🎤 **Speaker Notes:**
"Add this section to your PLAN.md. Before the AI writes any code, decide where the data lives. This prevents the AI from making random choices — sometimes it'll use SQLite, sometimes files, sometimes a full Postgres setup, depending on its mood. You decide. Put it in the plan."

---

### SECTION 7: Wrap-Up & Team Workflow (20-25 min)

---

#### Slide 59: Section Title — "Building Your Team's Workflow"
**[Layout: section]**

**Content:**
- Large text: "Your Workflow, Your Rules"
- Subtitle: "Let's take everything we've covered and make it yours"

---

#### Slide 60: Everything We've Covered
**[Layout: default]**

**Content:**
Quick visual recap:
1. 📋 **Plan First** — Write PLAN.md before prompting AI
2. 🤖 **AI Tools** — Use them as implementers, not architects
3. 🔀 **Git** — Branches, commits, PRs, no more `final-v2-FIXED.py`
4. 🔌 **APIs** — Your tools talk to services via structured requests
5. 🔒 **Security** — .env, .gitignore, never paste secrets
6. 💾 **Data** — Choose the right persistence level for the job

🎤 **Speaker Notes:**
"Quick recap of everything we covered today. Six topics, all connected. The plan drives the AI. Git keeps you safe. APIs connect you to data. Security protects your credentials. Data persistence makes your tools reliable. And it all starts with writing a plan before you start prompting."

---

#### Slide 61: Co-Create Your Team Checklist
**[Layout: center]**

**Content:**
👥 Interactive: "Let's build YOUR checklist together"

Starting template:
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
- [ ] Teammate can understand the project from docs alone
```

🎤 **Speaker Notes:**
"Let's customize this for YOUR team. What would you add? What doesn't apply? Maybe you have specific tools or platforms that need their own rules. The goal is that this checklist lives in your team wiki or Notion and you actually use it."

👥 **Audience exercise (10 min):** Edit the checklist together on screen based on their feedback.

---

#### Slide 62: The Vibes-to-Sustainable Spectrum
**[Layout: default]**

**Content:**
```
← Pure Vibecoding                        Sustainable Dev →

"Build me a thing"    "Here's PLAN.md,     "Plan, branch,
  ↓                    implement step 3"    implement, PR,
"Accept all"              ↓                  review, merge"
  ↓                  "Review the output"        ↓
"It works! Ship it"       ↓                "Documented,
  ↓                  "Commit to branch"     versioned,
"It broke. Start over"   ↓                  secure, shared"
                     "PR + merge"
```

- You don't have to be at the far right
- Moving even slightly from the left makes a HUGE difference
- Each practice you adopt is a win

🎤 **Speaker Notes:**
"You don't have to become a software engineer. Moving even slightly away from pure vibecoding makes an enormous difference. Writing a plan? Big win. Using git? Huge win. Not committing secrets? Potentially saves thousands of dollars. Each step on this spectrum makes your tools more reliable and your team more effective."

---

#### Slide 63: What to Do Monday Morning
**[Layout: default]**

**Content:**
Your action items:

1. **Today:** Pick one existing tool/script and add a `PLAN.md` to it
2. **This week:** Set up `.gitignore` and `.env` on your active projects
3. **This month:** Start using feature branches for new work
4. **Ongoing:** Every new project starts with PLAN.md

"You don't have to do everything at once. Start with one habit."

🎤 **Speaker Notes:**
"Here's your Monday morning todo list. Don't try to retrofit everything at once. Pick ONE project, add a plan, set up .env and .gitignore. Start using branches for your next feature. These are small steps that compound over time."

---

#### Slide 64: Q&A
**[Layout: center]**

**Content:**
- "Questions, concerns, confessions?"
- "What's still unclear?"
- "What's the first thing you want to try?"

🎤 **Speaker Notes:**
"Open floor. What questions do you have? What's still confusing? What are you most excited to try? And — this is a safe space — who wants to confess something they've been doing that they now realize might be... problematic?"

😄 **Joke:** "This is like a coding AA meeting. 'Hi, I'm [name], and I hardcode my API keys.' 'Hi [name].'"

---

#### Slide 65: Thank You & Resources
**[Layout: end]**

**Content:**
- "From Vibecoding to Sustainable Development"
- Contact info
- Link to this slide deck (hosted on Netlify/Vercel)
- Resources:
  - [Git cheat sheet](link)
  - [.env best practices](link)
  - [PLAN.md template](link)
  - [Slidev source code for this presentation](link)

🎤 **Speaker Notes:**
"Thank you! These slides are hosted online — you can revisit them anytime. I've included links to cheat sheets, templates, and everything we discussed. Feel free to reach out if you get stuck on anything. Remember: you're not becoming engineers. You're becoming engineers' favorite kind of colleagues — the ones who plan, document, and don't commit secrets."

😄 **Closing joke:** "Go forth and may your vibes be sustainable, your branches be merged, and your API keys be forever environment variables."

---

## Implementation Plan

### Phase 1: Slide Content Creation

- [ ] Replace `slides.md` with the full presentation content
- [ ] Configure Slidev frontmatter (theme, title, transitions, duration)
- [ ] Add speaker notes using Slidev's `<!-- -->` comment syntax
- [ ] Set up section divider slides with consistent styling

### Phase 2: Visual Polish

- [ ] Add Mermaid diagrams for git flow, API calls, and decision trees
- [ ] Create code snippet files in `snippets/` for complex examples
- [ ] Add v-click animations for progressive reveal on key slides
- [ ] Style section title slides with distinct colors per section

### Phase 3: Interactive Elements

- [ ] Add poll/voting components if available in Slidev ecosystem
- [ ] Create live demo scripts/repos for the git section
- [ ] Prepare `.env.example`, `.gitignore` templates as handouts
- [ ] Build a PLAN.md template slide that can be shown alongside live editing

### Phase 4: Testing & Refinement

- [ ] Run through the entire presentation locally
- [ ] Time each section against the 3-hour budget
- [ ] Test PDF export for offline distribution
- [ ] Deploy to Netlify/Vercel for live hosting

### Prerequisites

- Slidev dev environment working (`npm run dev`)
- Decision on final theme and visual style
- Access to GitHub for live demo setup
- Agreement on which audience-specific examples to use (PPC tools, dashboards, etc.)

## Technical Details

### Technology Stack

- **Slidev v52.11+**: Markdown-based presentation framework with Vue component support
- **Seriph theme**: Clean, developer-focused presentation theme
- **Mermaid**: Diagram generation from markdown (built into Slidev)
- **UnoCSS**: Utility-first CSS (bundled with Slidev)

### Slide Structure in slides.md

Each slide uses Slidev's frontmatter syntax:
```markdown
---
layout: default
transition: slide-left
---

# Slide Title

Content here

<!--
Speaker notes go here.
The audience never sees these.
They appear in Presenter Mode (press P).
-->
```

### Presenter Mode

Slidev's built-in presenter mode (accessible at `/presenter`) shows:
- Current slide + next slide preview
- Speaker notes
- Timer/clock
- Drawing tools

This is critical for the speaker — all 🎤 notes translate to `<!-- -->` blocks.

### File Organization

```
slides.md                    ← All slides (single file for now)
snippets/
  plan-template.md           ← PLAN.md template for slides
  env-example.txt            ← .env/.gitignore examples
  api-call.py                ← Python API call example
components/
  Counter.vue                ← Keep existing example (maybe use in demo)
```

## Alternatives Considered

### Alternative 1: Split Slides Across Multiple Files

**Description**: Use Slidev's `src:` import to split each section into its own file in `pages/`.

**Pros:**
- Cleaner file organization
- Easier to reorder sections
- Parallel editing possible

**Cons:**
- More complex setup
- Harder to get the "big picture" of the whole presentation
- Frontmatter inheritance can be tricky

**Why not chosen**: For a first implementation, a single `slides.md` is simpler to work with and review. Can refactor to multi-file later if the file gets unwieldy.

### Alternative 2: Use a More Visual Theme

**Description**: Switch from `seriph` to a theme with more built-in layouts like `slidev-theme-apple-basic` or `slidev-theme-purplin`.

**Pros:**
- More polished visual style out of the box
- More layout options

**Cons:**
- May not match the "developer workshop" vibe
- Additional dependency
- Less customization flexibility

**Why not chosen**: `seriph` is clean, professional, and well-maintained. Custom styling can be added via UnoCSS as needed.

### Alternative 3: PowerPoint/Google Slides Instead of Slidev

**Description**: Use a traditional slide tool instead of code-based slides.

**Pros:**
- Familiar to the audience
- Easy drag-and-drop design

**Cons:**
- Can't show live code with syntax highlighting
- No version control (ironic for a workshop about git)
- No programmatic diagrams
- Can't be hosted as a web app

**Why not chosen**: Slidev demonstrates the very practices we're teaching — code-based, version-controlled, deployable.

## Trade-offs and Risks

### Trade-offs

- **Depth vs. breadth**: 65 slides across 8 sections in 3 hours means we cover each topic at introductory level. This is appropriate for the audience (non-engineers) but means we can't go deep on any single topic.
- **Interactivity vs. content**: More audience exercises means less content coverage. We're prioritizing interactivity because learning sticks better with hands-on practice.
- **Humor vs. professionalism**: The proposal includes jokes and informal language. This is intentional for the audience (making technical topics approachable) but should be calibrated to the room.

### Risks

| Risk | Impact | Mitigation |
|------|--------|-----------|
| 3 hours isn't enough for all content | Medium | Each section has core slides and optional deep-dives. Cut the deep-dives if running long. |
| Audience skill level varies widely | High | Open with assessment questions. Adjust depth on the fly. |
| Live demo fails | Medium | Pre-record backup demos. Have screenshots ready. |
| Audience doesn't have laptops for exercises | Low | Make exercises optional. Show everything on screen. |
| Jokes fall flat | Low | The jokes are optional seasoning, not structural. Skip if the room isn't receptive. |

## Success Criteria

- [ ] All 65 slides implemented in `slides.md` with speaker notes
- [ ] Presentation runs locally without errors (`npm run dev`)
- [ ] PDF export works (`npm run export`)
- [ ] Deployed successfully to Netlify or Vercel
- [ ] Presenter mode shows all speaker notes correctly
- [ ] Total estimated speaking time fits within 3-hour window
- [ ] At least one audience member doesn't commit an API key to GitHub after attending

## Future Considerations

- **Multi-language support**: Could create a Czech or Slovak version if presenting to local teams
- **Hands-on workshop repo**: A dedicated GitHub repo with pre-built exercise scenarios (merge conflicts, leaked secrets, etc.)
- **Follow-up session**: "Part 2" covering testing, CI/CD, and deployment for teams that adopt the basic practices
- **Video recording**: Export slides + record voiceover for async consumption
- **Modular sections**: Split into standalone mini-workshops (just Git, just Security, etc.)

## References

- [Andrej Karpathy's original "vibe coding" tweet (Feb 2025)](https://x.com/karpathy/status/1886192184808149383)
- [Wikipedia: Vibe coding](https://en.wikipedia.org/wiki/Vibe_coding)
- [Simon Willison: Not all AI-assisted programming is vibe coding](https://simonwillison.net/2025/Mar/19/vibe-coding/)
- [5 Vibe Coding Risks (Zencoder)](https://zencoder.ai/blog/vibe-coding-risks)
- [Vibe coding could cause catastrophic explosions in 2026 (The New Stack)](https://thenewstack.io/vibe-coding-could-cause-catastrophic-explosions-in-2026/)
- [Security Impact of Vibe Coding (Accorian)](https://www.accorian.com/security-impact-of-vibe-coding-deep-dive-part-1-of-2/)
- [The Pros and Cons of Vibe Coding (Software Mind)](https://softwaremind.com/blog/the-rise-and-risk-of-vibe-coding-whats-worth-knowing/)
- [GitHub: 39M secrets leaked](https://cybersecuritynews.com/39m-secret-api-keys-credentials-leaked-from-github/)
- [From Zero to Hero: Coding for PPC (DEV Community)](https://dev.to/paulsanjay81/from-zero-to-hero-how-coding-can-supercharge-your-ppc-career-5ab1)
- [PPC and Coding (LinkedIn)](https://www.linkedin.com/pulse/ppc-coding-what-every-digital-marketer-needs-know-mark-staton-phd)
- [Slidev Documentation](https://sli.dev)
- [Google Ads API Documentation](https://developers.google.com/google-ads/api/docs/start)

## Review Questions

**Note**: This section is REQUIRED for AI-created proposals. Human-authored proposals may include it if needed.

**Status**: ✅ Resolved
**Review Date**: 2026-02-06
**Reviewer**: Claude AI (Opus 4.6)

The following questions must be answered before implementation:

---

### Q1: Presentation Language

**Issue**: The workshop content in README.md and PITCH.md doesn't specify the presentation language. Slides are currently in English, but the audience appears to be a Czech/Slovak PPC team (based on context clues like author name, location hints).

**Context**: If the audience primarily speaks Czech/Slovak, English slides may create a barrier. However, English technical terms (git, commit, push, API) are universally used and don't translate well.

**Question**: Should the slides be written in English or Czech/Slovak?

**Options**:
- [X] **A**: English slides, English speaker notes (recommended if presenting in English or to an international audience)
- [ ] **B**: Czech/Slovak slides, Czech/Slovak speaker notes (better if audience is purely local)
- [ ] **C**: English slides with Czech/Slovak speaker notes (hybrid — international-looking slides, but speaker can reference Czech talking points)

**Answer**:
```
I will speak in Slovak - yet I would like to have all materials in English.
```

**Resolution**:
```
All slide content, speaker notes, code snippets, and cheat sheets remain in English as written.
No changes needed to the proposal — the current content is already fully English.
The speaker will present in Slovak using the English materials as visual support.
This is a common approach in Slovak tech environments where English technical terms
(git, commit, push, API, .env) are used natively.
```

---

### Q2: Slide Count and Timing

**Issue**: The proposal outlines 65 slides for a 3-hour workshop. This averages ~2.8 minutes per slide, but some slides are interactive exercises (10-15 min) while others are quick transitions (~30 sec). The git section alone has 12 slides for a 45-minute slot.

**Context**: Too many slides means rushing or cutting content. Too few means awkward long pauses on single slides. The interactive exercises are the most variable — they could take 5 minutes or 20 depending on the audience.

**Question**: Is 65 slides the right count, or should we trim/expand?

**Options**:
- [X] **A**: Keep 65 slides as proposed — the mix of quick and slow slides balances out (recommended)
- [ ] **B**: Trim to ~50 slides — combine some content slides to leave more room for discussion
- [ ] **C**: Expand to ~80 slides — split complex slides into smaller steps for better pacing
- [ ] **D**: Mark slides as "core" vs. "optional" so the speaker can skip optional ones if running long

**Answer**:
```
Make as much material as possible - I can manage it in real time
```

**Resolution**:
```
Keep all 65 slides as proposed. During implementation, add extra "bonus" slides where
possible — deeper dives on git commands, additional API examples, more security horror
stories. The speaker will manage pacing in real time, skipping or lingering as the
audience energy dictates. No slides will be marked as "optional" — everything is
available material and the speaker's experience will determine what gets airtime.
```

---

### Q3: Live Demo Strategy

**Issue**: The proposal mentions live demos (git workflow, API calls) but doesn't specify whether to use a pre-prepared repo, the audience's real projects, or a mock project created during the session.

**Context**: Live demos are engaging but risky (things break, internet goes down, git auth fails). Pre-recorded demos are safe but less engaging. Using the audience's real projects is most relevant but unpredictable.

**Question**: What should the live demo strategy be?

**Options**:
- [X] **A**: Pre-prepared demo repo with scripted scenarios + audience follows along on their own (recommended — safety + participation)
- [ ] **B**: Fully live, building from scratch during the workshop (most engaging, highest risk)
- [ ] **C**: Pre-recorded video demos as backup, live attempt as primary (belt + suspenders)
- [ ] **D**: No live demos — use detailed screenshots and code snippets on slides instead

**Answer**:
```
We will create demo resources inside this repository. Make it rather simple.
```

**Resolution**:
```
Add a new task to the Implementation Plan: create a simple demo/ directory inside
this repository with:
  - demo/PLAN.md — example plan for a fictional PPC tool
  - demo/.env.example — template showing required environment variables
  - demo/.gitignore — pre-configured to ignore .env and common secrets
  - demo/main.py — minimal Python script demonstrating .env usage and a mock API call
Keep it intentionally simple — the demo exists to show patterns, not to be a real app.
The speaker will use this repo itself as the git demo (creating branches, PRs, etc.)
rather than setting up a separate repository.
```

---

### Q4: Humor Calibration

**Issue**: The proposal includes 15+ jokes and humorous analogies. The audience is a professional marketing team, not a developer conference. Humor that works in tech circles (merge conflict jokes, HTTP 418) may not land.

**Context**: Humor makes technical content approachable, but forced jokes in a professional setting can be awkward. The speaker knows the audience — humor level should match their culture.

**Question**: What's the right humor level for this audience?

**Options**:
- [X] **A**: Keep all jokes as written — they're PG-rated analogies that make concepts memorable (recommended)
- [ ] **B**: Reduce to ~5 key jokes — keep the best ones, cut the rest
- [ ] **C**: Replace jokes with real-world anecdotes from the team's own experience
- [ ] **D**: Minimal humor — professional tone throughout, let the content speak

**Answer**:
```
We can have spicy humor - I will do anecdotes on the fly based on the audience
```

**Resolution**:
```
Keep all 15+ jokes and analogies in the slides as written. Where possible, make
the humor even spicier — upgrade PG jokes to edgier tech humor. The speaker notes
should include extra joke options so the speaker can pick what fits the room.
Speaker will layer in live anecdotes on top of the written humor based on audience
reactions. No jokes will be removed during implementation — treat them as a menu
the speaker can draw from.
```

---

### Q5: Section Ordering — Security Before or After APIs?

**Issue**: The proposal follows the README order: APIs (Section 4) then Security (Section 5). However, PITCH.md puts Security before APIs. There's a logical argument for both: APIs naturally lead to "and now you need credentials, which leads to security" but Security-first means the audience has guardrails before they see API code.

**Context**: The order affects the narrative flow. APIs→Security creates a natural "transition" moment. Security→APIs means the audience already knows the .env pattern when they see API code with credentials.

**Question**: Should Security come before or after the APIs section?

**Options**:
- [X] **A**: APIs → Security (as proposed) — creates the natural "aha" transition: "to use APIs you need keys, which leads to security" (recommended)
- [ ] **B**: Security → APIs — "learn the rules first, then see them applied in API code"
- [ ] **C**: Interleave them — cover credentials/security during the API section as one combined topic

**Answer**:
```
Yep - let's do aha transition
```

**Resolution**:
```
Keep the current section order: APIs (Section 4) → Security (Section 5). The "aha"
transition on Slide 42 ("To call ANY of these APIs, you need credentials... where
these credentials live determines whether your tool is safe or a ticking time bomb")
serves as the natural bridge. No reordering needed — the proposal already implements
this correctly.
```

---

**Instructions for completing Review Questions**:

1. For each question, check the box next to your chosen option
2. Fill in the "Answer" section with your reasoning
3. Fill in the "Resolution" section with specific changes to make
4. Update the proposal based on all resolutions.
5. Change Status to "✅ Resolved" when all questions answered. Remove the "Review Questions" after the document is accepted.
6. Add changelog entry: "Resolved review questions and updated proposal accordingly"

---

## Changelog

| Date | Author | Changes |
|------|--------|---------|
| 2026-02-06 | Claude AI (Opus 4.6) | Initial draft with full slide list, speaker notes, and review questions |
| 2026-02-06 | Claude AI (Opus 4.6) | Resolved all 5 review questions based on author answers; updated status to Under Review |