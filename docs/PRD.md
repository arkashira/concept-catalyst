# Product Requirements Document (PRD)  
**Project:** concept-catalyst  
**Owner:** Senior Product/Engineering Lead – AxentX  
**Date:** 2026‑06‑21  

---  

## 1. Problem Statement  

Indie hackers, solo founders, and creator‑entrepreneurs repeatedly hit an **ideation bottleneck**: they have technical chops but struggle to surface *validated* software ideas that match real market pain and willingness‑to‑pay. Existing tools either provide generic brainstorming prompts or expensive market‑research services, leaving a gap for an **AI‑driven, end‑to‑end solution** that (1) surfaces high‑potential ideas, (2) validates them against live market signals, and (3) packages the output in a ready‑to‑prototype format.  

## 2. Target Users  

| Segment | Primary Persona | Key Pain Points | Desired Outcome |
|---------|----------------|----------------|-----------------|
| **Indie Hackers** | “Alex”, 28, full‑stack dev, builds side‑projects for revenue | No systematic way to discover market‑validated ideas; spends weeks on untested concepts | Quickly generate a shortlist of ideas with clear validation data |
| **Creator‑Entrepreneurs** | “Mia”, 35, designer‑developer hybrid, runs a niche community | Needs ideas that align with community interests and can be monetized | Receive ideas tied to community signals and willingness‑to‑pay estimates |
| **Early‑Stage Solo Founders** | “Ravi”, 32, ex‑consultant, wants to launch a SaaS | Limited time for market research; high risk of building for a non‑existent market | Get a data‑backed “go/no‑go” recommendation within hours |

## 3. Goals & Success Metrics  

| Goal | Success Metric | Target (12 mo) |
|------|----------------|----------------|
| **Validate market need before build** | % of generated ideas that achieve ≥ $500 MRR within 6 mo (post‑validation) | 12 % |
| **Accelerate ideation cycle** | Avg. time from user login → validated idea report | ≤ 15 min |
| **Drive user acquisition & retention** | Monthly Active Users (MAU) | 25 k |
| **Monetize the platform** | Paid conversion rate (free → paid tier) | 8 % |
| **Leverage AxentX data assets** | % of validation signals sourced from internal datasets (auto, instr‑resp, messages, query‑resp) | ≥ 60 % |
| **Maintain high AI quality** | Human‑rated relevance score (1‑5) for generated ideas | ≥ 4.2 |

## 4. Scope  

### In‑Scope (MVP)  

1. **AI‑Powered Idea Generator**  
   - Prompt‑based generation using **vLLM** inference engine.  
   - Ingests live market signals (Google Trends, Reddit, Product Hunt) plus AxentX internal datasets (auto, instr‑resp, messages, query‑resp).  
   - Returns 3‑5 concise idea concepts per request, each with a short “pain statement”, target persona, and high‑level feature sketch.  

2. **Idea Validation Engine**  
   - **Signal Aggregation:** pulls quantitative signals (search volume, mention frequency, competitor count).  
   - **Willingness‑to‑Pay Estimator:** lightweight survey flow (2‑question NPS‑style) + price‑sensitivity model trained on historic AxentX purchase data.  
   - Generates a **Validation Score** (0‑100) and a “Go/No‑Go” recommendation.  

3. **User Dashboard**  
   - List of generated ideas with validation metrics.  
   - Ability to bookmark, annotate, and export (Markdown, CSV, JSON).  
   - Simple UI built with React + Tailwind, hosted on AxentX static CDN.  

4. **Export & Share**  
   - One‑click “Export to Notion/Google Docs” and “Share link (read‑only)”.  

5. **Continuous Learning Loop**  
   - Feedback capture (thumbs up/down, comment) feeds back into the BRAIN (pgvector) to fine‑tune the generation model every 48 h.  

### Out‑of‑Scope (Post‑MVP)  

- Deep financial modeling (e.g., TAM/SAM/SOM calculations).  
- Custom consulting or hands‑on prototyping services.  
- Integration with paid market‑research APIs (e.g., Crunchbase, CB Insights).  
- Multi‑language support (initial release English‑only).  
- Mobile‑native applications (web‑first only).  

## 5. Key Features (Prioritized)  

| Priority | Feature | Description | Acceptance Criteria |
|----------|---------|-------------|---------------------|
| **P1** | **Idea Generation API** | REST endpoint `/generate` that accepts a user prompt and returns 3‑5 idea objects. | • Returns JSON with exactly 3‑5 ideas.<br>• Latency ≤ 2 s (vLLM on 8‑GPU node).<br
