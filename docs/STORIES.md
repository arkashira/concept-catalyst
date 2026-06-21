# STORIES.md – concept‑catalyst  

## Overview  
**concept‑catalyst** is an AI‑powered SaaS that helps indie hackers and creators break through the ideation bottleneck by **generating** software ideas and **validating** them against real‑world market signals. The backlog below is organized into Epics, each containing concrete, shippable story cards written in the *“As a <role>, I want <goal>, so that <benefit>”* format with clear Acceptance Criteria. Stories are ordered to reflect the Minimum Viable Product (MVP) rollout, followed by incremental enhancements.

---  

## EPIC 1 – User Onboarding & Account Management  

| # | Story | Acceptance Criteria |
|---|-------|----------------------|
| **1.1** | **As a prospective user, I want to create an account with email/password, so that I can securely access my personal idea workspace.** | - Given the Sign‑Up page, when I submit a valid email and password, then an account is created, a verification email is sent, and I am redirected to the onboarding wizard.<br>- Invalid email formats or weak passwords display inline error messages.<br>- Passwords are stored hashed (bcrypt) and never logged. |
| **1.2** | **As a returning user, I want to log in with my credentials, so that I can resume my work.** | - Given the Login page, when I enter correct credentials, then I am authenticated, a JWT is issued, and I am taken to the Dashboard.<br>- Failed login attempts show a generic “Invalid credentials” message and are rate‑limited (max 5 attempts/15 min). |
| **1.3** | **As a user, I want to reset my password, so that I can regain access if I forget it.** | - Given the “Forgot password?” link, when I submit my registered email, then I receive a time‑limited reset link.<br>- The link leads to a page where I can set a new password that meets the strength policy. |
| **1.4** | **As a user, I want to delete my account, so that I can remove my data from the platform.** | - Given the Account Settings page, when I confirm deletion, then all personal data, saved ideas, and validation reports are permanently removed, and I receive a confirmation email. |

---  

## EPIC 2 – Idea Generation Engine  

| # | Story | Acceptance Criteria |
|---|-------|----------------------|
| **2.1** | **As an indie hacker, I want to input my constraints (domain, tech stack, target audience, budget), so that the AI can tailor idea suggestions to my context.** | - The “New Idea” form accepts free‑text and selectable fields for domain, tech stack, audience persona, and budget range.<br>- All fields are optional; missing fields default to “broad”. |
| **2.2** | **As a creator, I want to receive a list of 5‑10 AI‑generated software ideas, so that I can quickly explore viable concepts.** | - When I submit the constraints, the backend calls the **vLLM** inference service and returns a ranked list of ideas within 5 seconds.<br>- Each idea includes a title, one‑sentence description, estimated TAM (Total Addressable Market), and suggested tech stack. |
| **2.3** | **As a user, I want to filter and sort generated ideas (by relevance, TAM, tech stack), so that I can focus on the most promising concepts.** | - UI provides dropdown filters for tech stack and audience, and sorting options for TAM and relevance score.<br>- Applying a filter updates the list instantly without a full page reload. |
| **2.4** | **As a user, I want to request a deeper “concept brief” for any idea, so that I can see a fleshed‑out product outline.** | - When I click “Generate Brief”, the system produces a 300‑word outline covering problem statement, core features, user journey, and monetization model.<br>- The brief is displayed in a modal and saved to the user’s workspace. |

---  

## EPIC 3 – Market Validation Layer  

| # | Story | Acceptance Criteria |
|---|-------|----------------------|
| **3.1** | **As a user, I want the AI to estimate market demand for an idea, so that I can gauge its commercial potential.** | - The validation service queries the **query‑resp** dataset and external public APIs (e.g., Google Trends, Crunchbase) to compute a Demand Score (0‑100).<br>- The score is displayed alongside the idea with a color‑coded badge (green ≥ 70, yellow 50‑69, red < 50). |
| **3.2** | **As a user, I want to see a “Willingness‑to‑Pay” (WTP) estimate, so that I can decide on pricing strategy.** | - The system aggregates historical pricing data from the **instr‑resp** dataset for similar products and outputs a suggested price range (e.g., $9‑$29/mo).<br>- The WTP estimate includes a confidence interval and a short rationale. |
