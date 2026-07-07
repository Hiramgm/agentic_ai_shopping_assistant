# 🛒 Agentic AI Shopping Assistant

A production-inspired, category-agnostic **Agentic AI Shopping
Assistant** that demonstrates how modern e-commerce AI systems can be
designed using **Agentic AI, Hybrid Search, Knowledge Graphs,
Recommendation Systems, and Provider Abstraction**.

> **Goal:** Build a portfolio-quality project that mirrors the
> architecture used by large-scale commerce platforms rather than a
> simple chatbot.

------------------------------------------------------------------------

# ✨ Features

-   Natural language product search
-   Multi-agent orchestration
-   Hybrid retrieval (BM25 + Semantic Search)
-   Product comparison
-   Explainable recommendations
-   Conversational shopping assistant
-   User preference memory
-   Knowledge graph reasoning
-   Swappable AI providers (LLMs, Embeddings, Vector DBs)

------------------------------------------------------------------------

# 🏗 High-Level Architecture

``` text
                CSV / Excel / Supplier APIs
                         │
                         ▼
                Data Ingestion Pipeline
                         │
                         ▼
          Validation & Normalization Layer
                         │
                         ▼
             PostgreSQL (Source of Truth)
                         │
      ┌──────────────────┼──────────────────┐
      ▼                  ▼                  ▼
 Elasticsearch        Pinecone           Neo4j
 Keyword Search    Semantic Search   Knowledge Graph
      └──────────────────┼──────────────────┘
                         ▼
               Hybrid Retrieval Engine
                         ▼
                 Agent Orchestrator
       ┌─────────┬──────────┬──────────┬─────────┐
       ▼         ▼          ▼          ▼
    Planner   Search     Compare    Memory
                         ▼
                  Final AI Response
```

------------------------------------------------------------------------

# 🔄 End-to-End Data Flow

``` text
CSV / Excel / API
      │
      ▼
Load Data
      │
      ▼
Validate Schema
      │
      ▼
Normalize Products
      │
      ▼
Store in PostgreSQL
      │
      ├── Build Search Document
      ├── Build Metadata
      ├── Generate Embeddings
      ├── Index into Elasticsearch
      ├── Store Vectors in Pinecone
      └── Create Relationships in Neo4j
```

------------------------------------------------------------------------

# 🔍 Search Flow

``` text
User Query
      │
      ▼
Planner Agent
      │
      ▼
Hybrid Retrieval
 ├───────────────┐
 ▼               ▼
BM25         Semantic Search
 ▼               ▼
Elastic      Pinecone
      │
      ▼
Result Fusion
      │
      ▼
Metadata Filtering
      │
      ▼
LLM Ranking
      │
      ▼
Response Generation
```

------------------------------------------------------------------------

# 🗄 Data Architecture

PostgreSQL acts as the **source of truth**.

``` text
Brand
 │
Category
 │
Product
 ├── ProductAttribute
 ├── ProductImage
 ├── ProductVariant
 └── ProductReview
```

Specialized systems:

-   PostgreSQL → transactional data
-   Elasticsearch → keyword search
-   Pinecone → semantic retrieval
-   Neo4j → relationship reasoning

------------------------------------------------------------------------

# 🔌 Provider Abstraction

Everything is configurable through environment variables.

``` env
LLM_PROVIDER=groq
LLM_MODEL=llama-3.3-70b-versatile

EMBEDDING_PROVIDER=jina
EMBEDDING_MODEL=jina-embeddings-v3

VECTOR_DB=pinecone
SEARCH_ENGINE=elasticsearch
GRAPH_DB=neo4j
```

Planned providers

### LLM

-   Groq
-   OpenAI
-   Ollama
-   OpenRouter

### Embeddings

-   Jina AI ✅
-   OpenAI
-   Voyage AI

### Vector DB

-   Pinecone

------------------------------------------------------------------------

# 🛠 Technology Stack

  Layer              Technology
  ------------------ ----------------
  Backend            FastAPI
  ORM                SQLAlchemy 2.x
  Database           PostgreSQL
  Migrations         Alembic
  Search             Elasticsearch
  Vector DB          Pinecone
  Knowledge Graph    Neo4j
  Cache              Redis
  Embeddings         Jina AI
  LLM                Groq
  Agent Framework    LangGraph
  Frontend           Next.js
  Observability      LangSmith
  Containerization   Docker

------------------------------------------------------------------------

# 📁 Project Structure

``` text
backend/
└── app/
    ├── agents/
    ├── api/
    ├── core/
    │   ├── config/
    │   ├── exceptions/
    │   └── logging/
    ├── db/
    ├── ingestion/
    ├── providers/
    │   ├── embeddings/
    │   ├── llm/
    │   ├── vector_db/
    │   ├── search/
    │   └── graph/
    ├── schemas/
    └── services/
```

------------------------------------------------------------------------

# 🚀 Development Roadmap

## Phase 1 --- Foundation

-   [x] FastAPI
-   [x] Configuration management
-   [x] Structured logging
-   [x] Request middleware
-   [x] Exception handling
-   [x] API router architecture
-   [x] Provider abstraction
-   [x] Embedding provider architecture
-   [x] Jina embedding provider

## Phase 2 --- Data Layer

-   [ ] PostgreSQL
-   [ ] SQLAlchemy models
-   [ ] Alembic
-   [ ] Product schema
-   [ ] Brand schema
-   [ ] Category schema
-   [ ] Product attributes
-   [ ] Product variants

## Phase 3 --- Ingestion

-   [ ] CSV loader
-   [ ] Excel loader
-   [ ] Validation
-   [ ] Normalization
-   [ ] Search document builder
-   [ ] Metadata builder
-   [ ] Embedding pipeline

## Phase 4 --- Retrieval

-   [ ] Elasticsearch
-   [ ] Pinecone
-   [ ] Hybrid retrieval
-   [ ] Ranking

## Phase 5 --- Knowledge Graph

-   [ ] Neo4j
-   [ ] Product relationships
-   [ ] Recommendation graph

## Phase 6 --- Agentic AI

-   [ ] Planner Agent
-   [ ] Search Agent
-   [ ] Compare Agent
-   [ ] Review Agent
-   [ ] Memory Agent
-   [ ] Agent Orchestrator

## Phase 7 --- Frontend & Deployment

-   [ ] Next.js
-   [ ] Docker
-   [ ] CI/CD
-   [ ] Monitoring

------------------------------------------------------------------------

# 📈 Current Progress

## Completed

-   FastAPI backend
-   Environment configuration
-   Structured logging
-   Global exception handling
-   API router architecture
-   Embedding abstraction
-   Registry pattern
-   Factory pattern
-   Config-driven providers
-   Jina embedding integration

## Next

-   PostgreSQL integration
-   Product schema
-   Ingestion pipeline
-   Pinecone
-   Elasticsearch
-   Neo4j

------------------------------------------------------------------------

# 🎓 Learning Objectives

This project provides hands-on experience with:

-   Agentic AI
-   Multi-agent systems
-   Production RAG
-   Hybrid search
-   Semantic retrieval
-   Knowledge graphs
-   Recommendation systems
-   PostgreSQL
-   Elasticsearch
-   Pinecone
-   Neo4j
-   AI system architecture
-   Production backend engineering

------------------------------------------------------------------------

# 📄 License

Educational, research, and portfolio project.
