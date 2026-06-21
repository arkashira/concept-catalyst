# TECH_SPEC.md – Concept‑Catalyst  

**Version:** 1.0.0  
**Last Updated:** 2026‑06‑21  
**Owner:** Product & Engineering Lead – AxentX  

---  

## 1. Overview  

Concept‑Catalyst is an AI‑powered SaaS that helps indie hackers and creators overcome the ideation bottleneck by **generating software product ideas** and **validating market demand** in a single workflow.  

* **Idea Generation** – Structured LLM prompts produce concise, novel concepts (problem statement, target persona, core feature set).  
* **Idea Validation** – A lightweight market‑fit model scores each concept on pain‑level, willingness‑to‑pay (WTP), and competitive landscape using curated public datasets and AxentX’s proprietary “pair” data.  

The service is built as a **cloud‑native micro‑service stack** with a React front‑end, FastAPI back‑end, and GPU‑accelerated inference using **vLLM** and **SGLang**. All embeddings are stored in PostgreSQL with the **pgvector** extension, enabling fast similarity search for idea de‑duplication and recommendation.

---  

## 2. Architecture Diagram  

```
+-------------------+        +-------------------+        +-------------------+
|   Front‑End (SPA) | <----> |   API Gateway     | <----> |   Auth Provider   |
|  React + TS + UI |        |   FastAPI (uvicorn)      (Auth0 / OIDC)   |
+-------------------+        +-------------------+        +-------------------+
                                   |   ^   |
            +----------------------+   |   +----------------------+
            |                          |                          |
   +--------v--------+        +--------v--------+        +--------v--------+
   | Idea Generator  |        | Idea Validator  |        |   Data Service   |
   | (vLLM + SGLang) |        | (ML scoring)    |        | (Postgres + pgvector) |
   +-----------------+        +-----------------+        +-----------------+
            |                          |                          |
            |   +----------------------+----------------------+   |
            |   |                     Message Queue (Kafka)   |   |
            |   +----------------------------------------------+   |
            |                                                  |
   +--------v--------+                                 +-------v-------+
   |  Cache (Redis)  |                                 |  Metrics (Prometheus) |
   +-----------------+                                 +-----------------------+
```

---  

## 3. Core Components  

| Component | Responsibility | Tech / Libraries | Runtime |
|-----------|----------------|------------------|---------|
| **Front‑End** | SPA for idea creation, review, feedback | React 18, TypeScript, Vite, TailwindCSS, React‑Query | Browser |
| **API Gateway** | HTTP/HTTPS entry point, request validation, auth, rate‑limiting | FastAPI, Pydantic, uvicorn, Starlette middleware | Python 3.11 |
| **Idea Generator** | Structured generation of product concepts | vLLM (GPU‑accelerated inference), SGLang for schema‑guided output, custom prompt templates | Python, GPU (NVIDIA A100+) |
| **Idea Validator** | Market‑fit scoring (pain, WTP, competition) | LightGBM + CatBoost ensemble, embeddings similarity via pgvector, feature extraction from `auto`, `instr‑resp`, `messages`, `query‑resp` datasets | Python, CPU (optional GPU for embedding inference) |
| **Data Service** | Persistent storage of users, ideas, validation results, feedback | PostgreSQL 15 + pgvector, SQLAlchemy 2.0, Alembic migrations | PostgreSQL |
| **Cache** | Low‑latency storage for recent embeddings & validation scores | Redis 7 (cluster mode) | In‑memory |
| **Message Queue** | Async processing of heavy tasks (embedding generation, batch validation) | Apache Kafka (3‑node cluster) | JVM |
| **Auth** | OAuth2/OIDC, token validation, user management | Auth0 (or self‑hosted OIDC), FastAPI Security utilities | External |
| **Observability** | Metrics, logs, tracing | Prometheus, Grafana, Loki, OpenTelemetry (Python SDK) | Sidecar/daemonset |
| **CI/CD** | Automated build, test, container image push, Helm release | GitHub Actions, Docker, Helm, ArgoCD (optional) | Cloud |

---  

## 4. Data Model  

### 4.1 Entity Diagram  

```
User
 └─ id (PK)
 └─ email (unique)
 └─ name
 └─ created_at
 └─ last_login

Idea
 └─ id (PK)
 └─ user_id (FK → User.id)
 └─ title
 └─ description
 └─ persona
