# Workshop Strategy: "From Vibecoding to Sustainable Development"

## Pre-Workshop Intelligence Gathering (5-10 min at start)

Start with a **quick interactive assessment** rather than assumptions. Use a casual, non-threatening format:

**Opening Questions (conversational, not quiz-like):**

1. "Show me one of your recent projects - let's look at it together"
2. "When you make changes, how do you share them with teammates?"
3. "What happens when two people work on the same thing?"
4. "Have you ever lost work or had to start over? What happened?"
5. "Do your apps remember data between sessions? How?"

This gives you real context and shows you're there to help, not lecture.

## Proposed Timeline (3 hours)

**Phase 1: Reality Check (30 min)**

- Interactive demo: "Let's break something together"
    - Show what happens when 2 people edit the same file
    - Demonstrate data loss when app restarts without persistence
    - Live example of accidentally committing API keys
- **Goal:** Create "aha moments" about WHY these practices matter

**Phase 2: Git Flow - The Collaborative Safety Net (45 min)**

- **Start with the pain point:** "Remember when you overwrote each other's work?"
- Visual git flow using real example:

```
main (production) ← develop (staging) ← feature/your-name-thing
```

- Hands-on exercise:
    - Everyone creates a feature branch
    - Makes a small change
    - Creates pull request
    - Merge without conflicts
- **Keep it practical:** Use GUI tools (GitHub Desktop, VS Code Git interface) - no CLI unless they want it
- Common scenarios they'll face:
    - Merge conflicts (show, don't scare)
    - How to undo mistakes
    - When to commit vs when to push

**BREAK (10 min)**

**Phase 3: Data Persistence Reality (30 min)**

- "Where does your data go when you close the tab?"
- Show spectrum of solutions:
    - **Browser storage** (localStorage) - quick demos die here
    - **Files** (JSON/CSV) - slightly better
    - **Actual databases** (SQLite → PostgreSQL) - when you're serious
- Live demo: Same app with/without persistence
- **Critical question:** "Is this throwaway or does someone depend on it?"

**Phase 4: Security Essentials (25 min)**

- **Start scary:** Show GitHub secret scanner finding leaked keys
- Practical rules:
    - `.env` files + `.gitignore` (show in their tools)
    - Environment variables in Cursor/Claude
    - Where secrets live in production (env vars, not code)
- Quick demo: Refactoring hardcoded API key to environment variable
- "If it's in git history, it's compromised forever"

**Phase 5: Documentation-First Approach (30 min)**

- Show your workflow:
    - Write `PLAN.md` before coding
    - AI implements from plan
    - Iterate on plan, not random code
- Benefits for their context:
    - Teammates understand what you're building
    - AI agents have clear instructions
    - You can review before wasting time coding wrong thing
- Template they can use:

```markdown
# Feature: [Name]
## Problem
## Solution approach
## Data needed
## Security considerations
## Files to change
```

- Live example: Take one of their projects and write a plan together

**Phase 6: Q\&A + Workflow Design (20 min)**

- "What's your biggest pain point right now?"
- Design their team workflow together on whiteboard:
    - Branching strategy
    - Code review process (even informal)
    - Where secrets live
    - How to share work-in-progress
- Document it as their "team charter"


## Materials to Prepare

**Option A: Minimal Prep (Adaptive approach you prefer)**

- Blank repository ready to demo
- Simple app example they can relate to (PPC dashboard?)
- `.gitignore` template
- `.env.example` template
- One-page git cheatsheet with visuals
- `PLAN.md` template

**Option B: Safety Net Prep**

- Same as above, PLUS:
- 3 pre-built scenarios in separate repos:

1. "Merge conflict disaster"
2. "Lost data nightmare"
3. "Leaked API key"
- Each can be live-demonstrated if questions don't naturally arise


## Cursor/Google AI Studio Crash Course (for you)

**Cursor specifics to mention:**

- Composer mode (multi-file editing) - similar to Claude's approach
- `.cursorrules` file for project context
- Cmd+K inline edits vs Composer for planning
- They likely use Composer - ask them

**Google AI Studio:**

- Primarily prompt playground, not full IDE agent
- Good for testing prompts before integrating
- Less relevant for your workshop unless they use it for actual coding


## Workshop Tone \& Anti-Patterns to Avoid

**DO:**

- Start with empathy: "AI coding tools are amazing but hide complexity"
- Use their vocabulary: "vibe" → "iterate quickly"
- Show consequences, not rules: Demo > Lecture
- Celebrate what they've built: "This works! Now let's make it sustainable"

**DON'T:**

- Use jargon without explaining (no "HEAD", "rebase", "ORM")
- Shame their current approach
- Go deep on database migrations (mention exists, move on)
- Teach CLI Git unless they specifically want it


## Key Frameworks for Decision-Making

Help them develop intuition:

**"Is this a throwaway or real tool?" test:**

- Throwaway → localStorage is fine, no git needed
- Real tool → needs persistence, git, secrets management

**"Bus factor" test:**

- If you get sick, can teammate continue?
- If yes → good documentation/git
- If no → problem

**"Security litmus test":**

- Would you put your credit card in this app?
- If no → probably not secure enough for API keys either


## Deliverable: Their Custom Checklist

End with creating THEIR checklist (collaborative):

```markdown
## Before We Start Coding
- [ ] Write PLAN.md describing what we're building
- [ ] Create feature branch: feature/[your-name]-[thing]
- [ ] Check .env.example for required secrets

## While Coding
- [ ] Commit every logical change (not at end of day)
- [ ] Never commit .env file
- [ ] Test locally before pushing

## When Sharing Work
- [ ] Push feature branch
- [ ] Create PR with description
- [ ] Ask teammate to review (even quick look)
- [ ] Merge to develop, not main

## When Deploying
- [ ] Secrets go in environment variables
- [ ] Test on develop first
- [ ] Document what changed
```


***

## My Recommendation

**Go with minimal prep (Option A) + conversational assessment approach.**

You're experienced enough to adapt, and their questions will naturally guide where depth is needed. The "show don't tell" approach with live demos will resonate better than slides.

**Key success metric:** They leave with:

1. Feature branch created on real project
2. `.gitignore` and `.env` pattern understood
3. One documented plan for next feature
4. Shared understanding of when to ask for help

Would you like me to create any specific materials (templates, cheatsheet, example repo structure) for this workshop?

