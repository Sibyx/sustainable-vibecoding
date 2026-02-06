---
draft: false
date: 2026-02-06
authors:
  - jdubec
categories:
  - Infrastructure
tags:
  - cleanup
  - ci-cd
  - github-actions
  - publish
  - readme
  - license
---

# IP-004: Final Publish Preparation

This proposal addresses accumulated inconsistencies from rapid IP-001 through IP-003 development and prepares the repository for public publishing on GitHub Pages. It covers dead file cleanup, proposal status reconciliation, GitHub Actions CI/CD, and public-facing polish (README, LICENSE, deploy config).

<!-- more -->

## Status

**Status**: Implemented
**Last Updated**: 2026-02-06
**Implementation**: Complete

## Problem Statement

The repository has been developed rapidly through three implementation proposals (IP-001 slide structure, IP-002 PLAN.md methodology slides, IP-003 Mentimeter survey). This pace left several inconsistencies and gaps that need resolving before the repository is suitable as a public GitHub project hosting the workshop slides.

**Specific issues:**

1. **Dead files in root `images/` directory**: Contains `mentimeter_qr_code.png` (duplicate of `public/images/mentimeter_qr_code.png` which is the one actually used by slides) and `logo.png` (unused by any slide or component). The root `images/` dir serves no runtime purpose.

2. **Starter template artifacts**: Three files from the Slidev starter template remain in the repo but are not referenced by any slide:
   - `pages/imported-slides.md` — unused imported slides page
   - `components/Counter.vue` — example counter component
   - `snippets/external.ts` — example code snippet

3. **Redundant deployment configurations**: Both `netlify.toml` and `vercel.json` exist, but the target deployment platform is GitHub Pages. These configs are misleading for contributors.

4. **Proposal status mismatches**:
   - **IP-003**: Index says "Accepted" but the proposal body says "Implemented" with `draft: false`. The index is stale.
   - **IP-002**: Has `draft: true` in frontmatter and "Under Review" status, but all 3 review questions are resolved (status: Resolved) and the slides have already been implemented. The proposal should be "Implemented".

5. **No CI/CD**: No GitHub Actions workflows exist. There's no automated build check on PRs and no automated deployment to GitHub Pages.

6. **No LICENSE file**: The repository has no license, which means it's technically "all rights reserved" — inappropriate for a public workshop resource.

7. **README.md is facilitator planning notes**: The current README contains a detailed workshop timeline, teaching notes, and planning structure. This is valuable for the facilitator but confusing for a public visitor who lands on the GitHub repo expecting a project description.

8. **Minor slide issue**: Line ~183 of `slides.md` still contains a "show of hands" prompt in the speaker notes (`Quick show of hands — who here has used ChatGPT, Claude, or Cursor to write code or scripts?`) which should reference the Mentimeter survey results instead, since IP-003 replaced informal polls with the survey.

**Who is affected**: Anyone visiting the public GitHub repository, contributors, and the speaker using the slides.

**Consequences of not addressing**: The repository looks unfinished and inconsistent. Missing CI/CD means broken builds go undetected. Missing license discourages reuse. Stale proposal statuses undermine the proposal methodology the workshop itself teaches.

## Proposed Solution

### Overview

Five phases of cleanup and polish, executed sequentially. Each phase is independent enough to be committed separately, enabling clean git history.

### Key Components

1. **File Cleanup** — Remove dead files that serve no runtime or documentation purpose
2. **Proposal Reconciliation** — Fix proposal statuses to match reality
3. **GitHub Actions CI/CD** — Automated build checks on PRs and deployment to GitHub Pages on push to master
4. **Public Polish** — README rewrite, LICENSE file, slide URL update
5. **Deploy Config Cleanup** — Remove platform-specific configs that don't match the deployment target

## Implementation Plan

### Phase 1: File Cleanup

- [ ] Delete `images/mentimeter_qr_code.png` (duplicate; `public/images/mentimeter_qr_code.png` is the one used by slides at `/images/mentimeter_qr_code.png`)
- [ ] Delete `images/logo.png` (unused by any file)
- [ ] Delete root `images/` directory (empty after above)
- [ ] Delete `pages/imported-slides.md` (Slidev starter template artifact, unreferenced)
- [ ] Delete `components/Counter.vue` (Slidev starter template artifact, unreferenced)
- [ ] Delete `snippets/external.ts` (Slidev starter template artifact, unreferenced)
- [ ] Remove empty directories (`pages/`, `snippets/`) if they become empty after deletions

### Phase 2: Proposal Reconciliation

- [ ] **IP-002** (`docs/proposals/posts/ip-002-plan-md-and-proposal-methodology-slides.md`):
  - Change frontmatter `draft: true` to `draft: false`
  - Change Status from "Under Review" to "Implemented"
  - Change Implementation from "Not started" to "Complete"
  - Add changelog entry
- [ ] **IP-003**: Update `docs/proposals/index.md` row from "Accepted" to "Implemented" (body already says Implemented)
- [ ] **IP-002**: Update `docs/proposals/index.md` row from "Under Review" to "Implemented"

### Phase 3: GitHub Actions

- [ ] Create `.github/workflows/deploy.yml` — Deploy to GitHub Pages on push to `master`
  - Trigger: `push` to `master`
  - Steps: checkout → setup Node 20 → `npm ci` → `npm run build` → upload pages artifact → deploy pages
  - Uses `actions/upload-pages-artifact@v4` and `actions/deploy-pages@v4`
  - Permissions: `pages: write`, `id-token: write`
  - Concurrency group to prevent overlapping deployments

- [ ] Create `.github/workflows/ci.yml` — Build check on pull requests
  - Trigger: `pull_request` to `master` and `develop`
  - Steps: checkout → setup Node 20 → `npm ci` → `npm run build`
  - Status check only — no deployment

### Phase 4: Public Polish

- [ ] Rewrite `README.md` for public visitors:
  - Project title and one-line description
  - What the workshop covers (brief)
  - How to run locally (`npm install`, `npm run dev`)
  - How to build (`npm run build`)
  - Link to live slides (GitHub Pages URL)
  - Link to proposal methodology docs
  - License badge
  - Move current facilitator notes to `docs/FACILITATOR_NOTES.md` (preserve the content)

- [ ] Add `LICENSE` file with CC BY 4.0 legal text

- [ ] Update closing slide in `slides.md` with the live GitHub Pages URL (once known)

- [ ] Add CC BY 4.0 license note to the closing/final slide (visible to audience and hosted slide viewers)

- [ ] Fix speaker notes at line ~183: replace "Quick show of hands" prompt with a reference to Mentimeter survey results

### Phase 5: Deploy Config Cleanup

- [ ] Remove `netlify.toml`
- [ ] Remove `vercel.json`

### Prerequisites

- IP-001, IP-002, and IP-003 implementation complete (they are)
- GitHub repository settings: Pages enabled, source set to GitHub Actions

## Technical Details

### GitHub Actions: `deploy.yml`

```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches: [master]

permissions:
  pages: write
  id-token: write

concurrency:
  group: pages
  cancel-in-progress: false

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: npm
      - run: npm ci
      - run: npm run build
      - uses: actions/upload-pages-artifact@v4
        with:
          path: dist

  deploy:
    needs: build
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - id: deployment
        uses: actions/deploy-pages@v4
```

### GitHub Actions: `ci.yml`

```yaml
name: CI

on:
  pull_request:
    branches: [master, develop]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: npm
      - run: npm ci
      - run: npm run build
```

### Slide Fix (Line ~183)

Current speaker notes contain:
```
Quick show of hands — who here has used ChatGPT, Claude, or Cursor to write code or scripts? ...And who has looked at the code it generated? ...And who understood it?
```

Replace with:
```
Remember the survey results? Most of you are already using AI tools to write code and scripts. But how many of you actually look at what it generates? And how many understand it?
```

This aligns with IP-003's replacement of informal show-of-hands prompts with the Mentimeter survey.

## Alternatives Considered

### Alternative 1: Skip CI/CD — Deploy Manually

**Description**: Don't add GitHub Actions. Build locally with `npm run build` and push `dist/` to a `gh-pages` branch manually.

**Pros:**
- No workflow files to maintain
- Works immediately without GitHub Pages settings

**Cons:**
- Manual deployment is error-prone and easy to forget
- No automated build check on PRs — broken builds merge undetected
- Contradicts the workshop's own message about sustainable development practices

**Why not chosen**: A workshop about sustainable development should practice what it preaches. Automated CI/CD is a basic hygiene practice.

### Alternative 2: Keep All Deploy Configs

**Description**: Keep `netlify.toml`, `vercel.json`, and add GitHub Actions. Support all three platforms.

**Pros:**
- Maximum flexibility — anyone can deploy anywhere
- No information lost

**Cons:**
- Confusing for contributors ("which platform is this deployed to?")
- Configs may drift out of sync
- Signals indecision rather than intentionality

**Why not chosen**: Pick one platform and commit to it. GitHub Pages is free, integrates with the existing GitHub workflow, and requires zero additional accounts.

### Alternative 3: Keep README as Facilitator Notes

**Description**: Don't rewrite README. The audience is the facilitator, not random GitHub visitors.

**Pros:**
- No content reorganization needed
- Facilitator notes stay front and center

**Cons:**
- Public visitors see planning notes instead of a project description
- Doesn't follow GitHub conventions (README = project overview)
- Facilitator notes are better served by a dedicated doc

**Why not chosen**: Move facilitator notes to `docs/FACILITATOR_NOTES.md` and give README its conventional role. Both audiences are served.

## Trade-offs and Risks

### Trade-offs

- **Deleting starter template files**: Removes reference examples, but they're available in the Slidev documentation and serve no purpose in a published workshop repo
- **README rewrite**: Facilitator loses the top-level planning doc, but gains a dedicated `docs/FACILITATOR_NOTES.md` which is arguably better organized
- **Single deploy target**: Commits to GitHub Pages, dropping Netlify/Vercel flexibility. Acceptable since the repo is already on GitHub and Pages is free

### Risks

| Risk | Impact | Mitigation |
|------|--------|------------|
| GitHub Pages deployment fails | Medium | CI workflow catches build errors before they reach master. Manual `npm run build` always available as fallback. |
| Facilitator notes lost in reorganization | Low | Content is moved, not deleted. Git history preserves the original README. |
| License choice restricts reuse | Low | CC BY 4.0 is standard for educational content and requires only attribution. Permissive enough for workshop material. |
| Removing deploy configs breaks someone's fork | Low | Forks can re-add configs. The files are trivial. |

## Success Criteria

- [ ] No dead files remain (root `images/`, starter template artifacts)
- [ ] All proposal statuses in `index.md` match their respective proposal bodies
- [ ] GitHub Actions: PRs to master/develop trigger build checks
- [ ] GitHub Actions: Push to master deploys to GitHub Pages
- [ ] README describes the project for a public audience
- [ ] LICENSE file exists with CC BY 4.0 text
- [ ] Speaker notes at line ~183 reference Mentimeter instead of show-of-hands
- [ ] `netlify.toml` and `vercel.json` removed
- [ ] CC BY 4.0 license note visible on closing slide

## Future Considerations

- **Custom domain**: If the workshop gets its own domain, update the GitHub Pages settings and README accordingly
- **Slide versioning**: Tag releases before each workshop delivery to preserve slide state per event
- **Contributor guidelines**: If others contribute, add a `CONTRIBUTING.md` with the proposal workflow
- **Automated PDF export**: Add a GitHub Action that runs `npm run export` and attaches the PDF to releases

## References

- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [GitHub Actions: deploy-pages](https://github.com/actions/deploy-pages)
- [Slidev Deployment Guide](https://sli.dev/guide/hosting)
- [IP-001: Presentation Structure](ip-001-presentation-structure-and-slide-list.md)
- [IP-002: PLAN.md & Proposal Methodology Slides](ip-002-plan-md-and-proposal-methodology-slides.md)
- [IP-003: Audience Workflow Survey via Mentimeter](ip-003-audience-knowledge-kahoot-quiz.md)

## Review Questions

**Note**: This section is REQUIRED for AI-created proposals. Human-authored proposals may include it if needed.

**Status**: Resolved
**Review Date**: 2026-02-06
**Reviewer**: Claude AI (Opus 4.6)

The following questions must be answered before implementation:

---

### Q1: Deployment Target

**Issue**: The repository currently has `netlify.toml` and `vercel.json` but no GitHub Actions workflows. The plan assumes GitHub Pages as the sole deployment target.

**Context**: Keeping multiple deploy configs adds flexibility but creates confusion about which platform is actually used. Removing them is a one-way door — forks that rely on them would need to re-add. However, the configs are trivial (< 20 lines each) and easily recreated.

**Question**: Should we commit to GitHub Pages only and remove Netlify/Vercel configs?

**Options**:
- [X] **A**: GitHub Pages only — remove `netlify.toml` and `vercel.json` (recommended — clean, intentional, matches the GitHub-native workflow)
- [ ] **B**: Keep all three — add GitHub Actions but also keep Netlify/Vercel configs as deployment alternatives
- [ ] **C**: Keep configs but add a comment at the top of each noting they're unused and preserved for reference only

**Answer**:
```
Relly only on GitHub Actions for deployment and GitHub Pages for hosting.
```

**Resolution**:
```
Delete netlify.toml and vercel.json in Phase 5. GitHub Pages via GitHub Actions is the
sole deployment target. Phase 3 workflows are confirmed as the only deploy mechanism.
No changes needed to the proposal — Phase 5 already describes this as the default path.
```

---

### Q2: Starter File Cleanup

**Issue**: Three files from the Slidev starter template remain: `pages/imported-slides.md`, `components/Counter.vue`, `snippets/external.ts`. None are referenced by any slide. They exist because `npm create slidev` generates them as examples.

**Context**: These files are noise in a published repo — they suggest the project is still a template. However, someone learning Slidev from this repo might find them useful as reference. The Slidev docs cover all of this, so the reference value is minimal.

**Question**: Should we remove all three unused starter template files?

**Options**:
- [X] **A**: Remove all three — they're template noise in a published project (recommended)
- [ ] **B**: Keep them — they serve as Slidev reference for anyone who clones the repo
- [ ] **C**: Remove `Counter.vue` and `external.ts` but keep `imported-slides.md` as it demonstrates Slidev's multi-file feature

**Answer**:
```
Get rid of the bullshit
```

**Resolution**:
```
Delete all three files in Phase 1: pages/imported-slides.md, components/Counter.vue,
snippets/external.ts. No changes needed to the proposal — Phase 1 already lists all
three for deletion. If the pages/ or snippets/ directories become empty after deletion,
remove the empty directories as well.
```

---

### Q3: README Audience

**Issue**: The current `README.md` contains detailed facilitator planning notes (workshop timeline, teaching format, step-by-step instructions). This is valuable content but unconventional for a GitHub README, which typically describes the project for visitors.

**Context**: Moving facilitator notes to `docs/FACILITATOR_NOTES.md` preserves the content while giving README its conventional role. The trade-off is that the facilitator needs to know to look in `docs/` instead of the root. Git history preserves the original.

**Question**: Should we rewrite README for public visitors and move facilitator notes to docs?

**Options**:
- [X] **A**: Rewrite README for public visitors, move facilitator notes to `docs/FACILITATOR_NOTES.md` (recommended — serves both audiences)
- [ ] **B**: Keep README as facilitator notes — the primary audience is the speaker, not GitHub visitors
- [ ] **C**: Create a separate `docs/PUBLIC_README.md` and keep root README as facilitator notes (unconventional but preserves facilitator workflow)

**Answer**:
```
Yep, make sense of it
```

**Resolution**:
```
Move current README.md content to docs/FACILITATOR_NOTES.md. Rewrite README.md as a
public-facing project description: title, one-line summary, workshop topics, local dev
instructions (npm install / npm run dev / npm run build), link to live GitHub Pages URL,
link to docs/ for methodology, and CC BY 4.0 license badge. Phase 4 already describes
this — no structural changes needed.
```

---

### Q4: License Choice

**Issue**: The repository has no LICENSE file. For a public workshop resource containing slides, documentation, and code (Slidev/Vue), the license choice affects how others can reuse the material.

**Context**: MIT is standard for code repos and maximally permissive. Creative Commons licenses (CC BY, CC BY-SA) are more common for educational/presentation content. A dual license (MIT for code, CC for content) is possible but adds complexity. No license means "all rights reserved" by default.

**Question**: Which license should we use?

**Options**:
- [ ] **A**: MIT License (recommended — simple, permissive, covers both code and content, widely understood)
- [X] **B**: CC BY 4.0 (Creative Commons Attribution — standard for educational content, requires attribution)
- [ ] **C**: CC BY-SA 4.0 (Creative Commons Attribution-ShareAlike — requires attribution and derivative works use the same license)
- [ ] **D**: No license — keep "all rights reserved" and let people ask permission

**Answer**:
```
CC BY 4.0 works fine for me. Add also license to presentation slide somewhere reasonable.
```

**Resolution**:
```
Use CC BY 4.0 license. Create a LICENSE file with the full CC BY 4.0 legal text. In
Phase 4, add a CC BY 4.0 badge to the new README.md. Additionally, add a license
reference to the presentation slides — add a small "CC BY 4.0" note to the closing/final
slide so the audience and anyone viewing the hosted slides sees the license.
Update Phase 4 tasks to include the slide license addition.
```

---

**Instructions for completing Review Questions**:

1. For each question, check the box next to your chosen option
2. Fill in the "Answer" section with your reasoning
3. Fill in the "Resolution" section with specific changes to make
4. Update the proposal based on all resolutions.
5. Change Status to "Resolved" when all questions answered. Remove the "Review Questions" after the document is accepted.
6. Add changelog entry: "Resolved review questions and updated proposal accordingly"

---

## Changelog

| Date | Author               | Changes |
|------|----------------------|---------|
| 2026-02-06 | jdubec               | Initial draft: 5-phase cleanup plan, GitHub Actions CI/CD design, 4 review questions covering deployment target, starter files, README audience, and license choice |
| 2026-02-06 | Claude AI (Opus 4.6) | Resolved review questions: Q1 GitHub Pages only (remove netlify/vercel), Q2 delete all starter template files, Q3 rewrite README for public + move facilitator notes to docs, Q4 CC BY 4.0 license with badge in README and reference on closing slide |
| 2026-02-06 | Claude AI (Opus 4.6) | Applied resolutions to proposal body: removed conditional/pending language from Phases 4-5 and Success Criteria, specified CC BY 4.0 throughout, added slide license task to Phase 4, added empty directory cleanup to Phase 1, updated risks table. Status → Under Review |
| 2026-02-06 | Claude AI (Opus 4.6) | Implementation complete. All 5 phases executed: deleted dead files and starter artifacts (Phase 1), reconciled IP-002 status (Phase 2), created deploy.yml and ci.yml workflows (Phase 3), rewrote README, moved facilitator notes, added CC BY 4.0 LICENSE, updated closing slide with URL and license, fixed show-of-hands speaker notes (Phase 4), removed netlify.toml and vercel.json (Phase 5). Status → Implemented |