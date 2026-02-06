# Implementation Proposals Methodology

This document describes the proposal-first development methodology used in the Kraken API project, proposes improvements, and discusses integration with AI coding agents like Claude Code.

## Table of Contents

- [Overview](#overview)
- [Methodology](#methodology)
  - [Core Principle](#core-principle)
  - [Proposal Lifecycle](#proposal-lifecycle)
  - [Proposal Structure](#proposal-structure)
  - [AI-Generated Proposals: Review Questions](#ai-generated-proposals-review-questions)
  - [Infrastructure](#infrastructure)
- [Usage with AI Coding Agents](#usage-with-ai-coding-agents)
  - [Current Workflow with Claude Code](#current-workflow-with-claude-code)
  - [Comparison with Plan / Execution Modes](#comparison-with-plan--execution-modes)
  - [Recommendations for Agent-Assisted Development](#recommendations-for-agent-assisted-development)

---

## Overview

Kraken API follows a **proposal-first methodology**: every non-trivial feature, architectural change, or infrastructure addition is documented in a structured proposal before any code is written. Proposals live in `docs/proposals/posts/` as markdown files, tracked in a central index (`docs/proposals/index.md`), served as a blog via mkdocs-material, and governed by conventions defined in `CLAUDE.md`.

The system has been used for 7 proposals to date (IP-001 through IP-007), of which 5 are implemented and 2 remain in draft.

## Methodology

### Core Principle

**Think before you build.** Every feature goes through a written design phase that forces the author to articulate the problem, consider alternatives, identify risks, and define success criteria before committing to an implementation path. This applies whether the author is a human developer or an AI agent.

### Proposal Lifecycle

```
Draft  →  Under Review  →  Accepted  →  Implemented
                ↓                            ↓
            Rejected                    Superseded
```

1. **Draft**: Author creates proposal from `.template.md`, fills all sections, updates the proposals index.
2. **Under Review**: Proposal is complete and submitted for team feedback. For AI-generated proposals, Review Questions must be included.
3. **Accepted**: Feedback addressed, questions resolved, approved for implementation.
4. **Implemented**: Code written, deployed, proposal marked complete.
5. **Rejected / Superseded**: Proposal declined or replaced by a newer proposal, with rationale documented.

### Proposal Structure

Every proposal follows a fixed template (`.template.md`) with these sections:

| Section                     | Purpose                                                                                 |
|-----------------------------|-----------------------------------------------------------------------------------------|
| **Frontmatter**             | YAML metadata: date, authors, categories, tags. Controls mkdocs blog rendering.         |
| **Title + Summary**         | `IP-XXX: Title` followed by 2-3 sentence summary and `<!-- more -->` excerpt separator. |
| **Status**                  | Current state, last updated date, implementation progress.                              |
| **Problem Statement**       | What problem exists, who is affected, consequences of inaction.                         |
| **Proposed Solution**       | High-level approach, key components, architecture diagrams (Mermaid).                   |
| **Implementation Plan**     | Phased checklist of tasks. No time estimates.                                           |
| **Technical Details**       | Schema changes, API changes, configuration, code examples.                              |
| **Alternatives Considered** | Other approaches evaluated with pros/cons and rejection rationale.                      |
| **Trade-offs and Risks**    | Design trade-offs with justification; risk table with impact and mitigation.            |
| **Open Questions**          | Unresolved issues (deprecated in favor of Review Questions for AI proposals).           |
| **Success Criteria**        | Measurable checkboxes defining "done".                                                  |
| **Future Considerations**   | Possible extensions deferred to later work.                                             |
| **References**              | Links to code, docs, related proposals, external standards.                             |
| **Discussion**              | Design rationale for non-obvious decisions.                                             |
| **Review Questions**        | (Required for AI-generated proposals) Structured Q&A identifying inconsistencies.       |
| **Changelog**               | Date/Author/Changes table tracking every modification.                                  |

**Key constraints:**

- No time estimates anywhere in proposals.
- Changelog updated on every change, including initial creation.
- Proposals index updated whenever a proposal is created or its status changes.

### AI-Generated Proposals: Review Questions

When an AI agent creates a proposal, it must include a **Review Questions** section. This is the most distinctive aspect of the methodology. The workflow:

1. Agent writes the complete proposal draft.
2. Agent reads back the proposal and identifies inconsistencies, edge cases, contradictions, and ambiguities.
3. Agent adds Review Questions with structured format per question:
   - **Priority**: Critical / Medium / Low
   - **Issue**: What the problem is (with line references)
   - **Context**: Why it matters
   - **Question**: What needs to be decided
   - **Options**: Multiple choice (A/B/C) with recommendations
   - **Answer**: (Human fills in)
   - **Resolution**: (Human describes how to update the proposal)

4. Human reviews, answers all questions, and applies resolutions.
5. Once all questions are resolved, the section is removed and the proposal moves to Accepted.

This mechanism serves as a **structured handoff** between AI and human, ensuring the human validates every significant design decision rather than rubber-stamping an AI-generated document.

### Infrastructure

- **Storage**: Markdown files in `docs/proposals/posts/`, committed to git alongside the codebase.
- **Rendering**: mkdocs-material blog plugin with categories, tags, author tracking, pagination.
- **Index**: `docs/proposals/index.md` serves as the registry with status emoji indicators.
- **Template**: `docs/proposals/.template.md` provides the canonical structure.
- **Governance**: `CLAUDE.md` codifies writing guidelines for both human and AI authors.

---

## Usage with AI Coding Agents

### Current Workflow with Claude Code

The proposal system integrates with Claude Code through `CLAUDE.md`, which acts as the agent's instruction set. The current workflow:

1. **Human requests a proposal**: "Write a proposal for feature X."
2. **Agent explores the codebase**: Reads existing code, related proposals, and patterns.
3. **Agent writes the proposal**: Creates the markdown file following the template.
4. **Agent self-reviews**: Reads back the proposal and generates Review Questions.
5. **Human answers questions**: Fills in Answer and Resolution fields.
6. **Agent applies resolutions**: Updates the proposal based on human decisions.
7. **Human accepts**: Status moves to Accepted.
8. **Agent implements**: Writes code following the accepted proposal as specification.

The Review Questions mechanism is the key innovation here. It addresses the fundamental problem with AI-generated design documents: **the AI doesn't know what it doesn't know**. By systematically reviewing its own output for contradictions and ambiguities, the AI surfaces decisions that require human judgment.

### Comparison with Plan / Execution Modes

Modern AI coding agents (Claude Code, Cursor, Aider, etc.) offer built-in **plan mode** and **execution mode**:

| Aspect              | Plan Mode (Built-in)                               | Proposal System                                      |
|---------------------|----------------------------------------------------|------------------------------------------------------|
| **Trigger**         | Agent enters plan mode automatically or on request | Human explicitly requests a proposal                 |
| **Output**          | Ephemeral plan in conversation context             | Persistent markdown file in git                      |
| **Scope**           | Single coding session                              | Spans multiple sessions and team members             |
| **Review**          | User approves/rejects plan inline                  | Structured Q&A with options and resolutions          |
| **Granularity**     | File-level changes ("I'll edit X, Y, Z")           | System-level design (architecture, schemas, APIs)    |
| **Alternatives**    | Sometimes mentioned                                | Required section with pros/cons                      |
| **Persistence**     | Lost when conversation ends                        | Committed to repo, serves as documentation           |
| **Team visibility** | Only the person in the conversation                | Anyone with repo access                              |
| **Reusability**     | None                                               | Proposals reference each other, build design history |

**Key differences:**

**Plan mode is tactical; proposals are strategic.** Plan mode answers "what files do I change and how?" Proposals answer "what are we building, why, and what did we consider?" They operate at different levels of abstraction and serve different purposes.

**Plan mode is ephemeral; proposals are permanent.** A plan mode session disappears when the conversation ends. A proposal remains in the repository as a design decision record, queryable months later when someone asks "why did we build it this way?"

**Plan mode is single-actor; proposals are collaborative.** Plan mode is a dialogue between one developer and one agent. Proposals (especially with Review Questions) create a structured dialogue that can involve multiple reviewers over time.

**They are complementary, not competing.** The ideal workflow uses proposals for the design phase and plan mode for the implementation phase:

```
Proposal (design, alternatives, decisions)
    ↓
Acceptance
    ↓
Plan Mode (file-by-file implementation strategy)
    ↓
Execution (code changes)
```

### Recommendations for Agent-Assisted Development

#### 1. Use Proposals as Agent Context

When an agent begins implementing an accepted proposal, load the proposal file as context. The proposal contains the specification: what to build, how, which patterns to follow, and what success looks like. This is more reliable than verbal instructions because it has been reviewed and approved.

```
"Implement IP-005. The proposal is at docs/proposals/posts/IP-005-manual-job-trigger-endpoint.md.
Follow it as the specification."
```

#### 2. Let the Agent Update Proposals During Implementation

If the agent discovers during implementation that the proposal needs adjustment (e.g., a schema field type needs to change), it should update the proposal first, note the change in the changelog, then proceed with the updated design. This keeps the proposal as the source of truth.

#### 3. Use Review Questions Beyond AI-Generated Proposals

The Review Questions format is useful even for human-authored proposals. When a human writes a proposal and asks an AI agent to review it, the agent can add Review Questions in the same structured format. This turns the AI into a systematic design reviewer rather than just a document generator.

#### 4. Automate Proposal Scaffolding

An agent can be given a shortcut to scaffold a new proposal: copy the template, assign the next IP number, update the index, and fill in the frontmatter. This reduces friction and ensures conventions are followed from the start.

#### 5. Track Implementation Progress in Proposals

During implementation, the agent should check off items in the Implementation Plan as they're completed and update the changelog. This creates a real-time record of progress that survives across conversation sessions.

#### 6. Plan Mode for Phases, Proposals for Projects

For multi-phase proposals, use plan mode at the start of each phase to break it into concrete file changes, then execute. The proposal stays as the north star; plan mode handles the tactical session-level work.

#### 7. Agent Self-Review Quality

The quality of Review Questions varies. Some are genuinely useful (IP-003 Q3 changed the core algorithm), others are low-value documentation clarifications. Agents should prioritize questions that could affect correctness, data integrity, or user experience over stylistic concerns. The priority system (Critical / Medium / Low) helps, but agents should aim for fewer, higher-impact questions rather than exhaustive coverage.

---

## Summary

The proposal system provides a structured, persistent, reviewable design process that complements the ephemeral plan/execute cycle of AI coding agents. The Review Questions mechanism is particularly effective as a human-AI handoff protocol. The main areas for improvement are operational consistency (status synchronization, category taxonomy) and scaling (lightweight proposals for small changes, dependency tracking).

The system works because it solves a real problem: AI agents can generate plausible-looking designs that contain subtle inconsistencies. By forcing a structured self-review and human sign-off, the proposal system catches these issues before they become code.