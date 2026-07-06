# Agentic AI Shopping Assistant - Master Project Plan

**Goal:** Build a production-inspired, category-agnostic AI shopping
agent demonstrating Agentic AI, RAG, hybrid retrieval, knowledge graphs,
recommendations, memory, and explainability.

------------------------------------------------------------------------

# 0. Product Vision

User can: - Search products using natural language - Filter using
conversational follow-ups - Compare products - Analyze reviews - Receive
personalized recommendations - Ask "why" questions - Search across
multiple categories - Benefit from persistent preferences

Example: \> Find lightweight machine learning laptops under \$1500. \>
\> Show only 32GB RAM options. \> \> Compare the top two. \> \> Which
would you personally recommend?

------------------------------------------------------------------------

# 1. Architecture Decisions

## Backend

-   FastAPI

## Frontend

-   Next.js

## Agent Framework

-   LangGraph

## Databases

-   PostgreSQL
-   Elasticsearch
-   Pinecone
-   Neo4j
-   Redis

## Observability

-   LangSmith

## Background Processing

-   Celery + Redis

## Containerization

-   Docker + docker-compose

------------------------------------------------------------------------

# 2. Provider Abstraction Layer

## Environment Variables

``` env
LLM_PROVIDER=groq
LLM_MODEL=llama-3.3-70b-versatile

EMBEDDING_PROVIDER=voyage
EMBEDDING_MODEL=voyage-large-2

VECTOR_DB=pinecone
SEARCH_ENGINE=elasticsearch
GRAPH_DB=neo4j
CACHE_PROVIDER=redis
```

## Factories

-   LLMFactory
-   EmbeddingFactory
-   VectorDBFactory
-   SearchFactory
-   GraphFactory
-   MemoryFactory

Supported providers: - OpenAI - Groq - Ollama - OpenRouter - Local
models

------------------------------------------------------------------------

# Phase 1 --- Project Setup

## Tasks

-   Create repository
-   Setup poetry/uv
-   Setup pre-commit
-   Setup linting
-   Setup formatting
-   Setup Docker
-   Setup environment management
-   Setup logging
-   Setup configuration loader
-   Setup CI/CD

## Deliverables

-   Running project skeleton
-   Docker environment
-   Config management

------------------------------------------------------------------------

# Phase 2 --- Database Design

## PostgreSQL Tables

### Products

-   product_id
-   title
-   description
-   brand
-   category
-   subcategory
-   price
-   currency
-   rating
-   review_count
-   availability
-   images
-   tags

### Product Attributes

-   product_id
-   attribute_name
-   attribute_value

### Categories

### Brands

### Reviews

### User Preferences

### Search History

### Sessions

## Tasks

-   ERD
-   Alembic migrations
-   Indexing strategy

------------------------------------------------------------------------

# Phase 3 --- Product Schema Engine

## Universal Schema

``` json
{
  "product_id":"",
  "title":"",
  "brand":"",
  "category":"",
  "subcategory":"",
  "price":"",
  "rating":"",
  "description":"",
  "attributes":{}
}
```

## Category Schemas

### Laptop

-   cpu
-   gpu
-   ram
-   storage
-   battery
-   weight

### Shoes

-   sport
-   size
-   gender
-   material
-   foot_type
-   waterproof

### Smartphones

-   processor
-   storage
-   camera
-   battery
-   display

## Tasks

-   Dynamic schema loader
-   Attribute validation
-   Metadata normalizer

------------------------------------------------------------------------

# Phase 4 --- Data Ingestion Pipeline

## Sources

-   CSV
-   XLSX
-   JSON
-   APIs

## Pipeline

1.  Load
2.  Validate
3.  Clean
4.  Normalize
5.  Extract metadata
6.  Generate embeddings
7.  Build KG
8.  Persist

## Tasks

-   CSV parser
-   Excel parser
-   Validation rules
-   Missing value handling
-   Duplicate detection
-   Attribute extraction
-   Unit normalization

------------------------------------------------------------------------

# Phase 5 --- Elasticsearch

## Features

-   BM25 search
-   Faceted search
-   Filters
-   Sorting

## Filters

-   category
-   brand
-   price
-   rating
-   availability
-   category attributes

## Tasks

-   Index design
-   Mapping design
-   Synonym dictionaries
-   Query templates

------------------------------------------------------------------------

# Phase 6 --- Pinecone

## Embedding Documents

Include: - Title - Description - Category - Brand - Attributes - Use
cases - Pros/cons - Price

## Metadata

-   product_id
-   category
-   brand
-   price
-   rating
-   attributes

## Tasks

-   Namespace strategy
-   Metadata filtering
-   Upsert pipeline
-   Batch processing

------------------------------------------------------------------------

# Phase 7 --- Neo4j Knowledge Graph

## Nodes

-   Product
-   Category
-   Brand
-   Attribute
-   User
-   Review
-   UseCase

## Relationships

-   BELONGS_TO
-   MADE_BY
-   HAS_ATTRIBUTE
-   USED_FOR
-   SIMILAR_TO
-   BOUGHT_WITH
-   PREFERS
-   VIEWED

## Tasks

-   Graph schema
-   Similarity edges
-   Recommendation edges

------------------------------------------------------------------------

# Phase 8 --- Agent Architecture

## Planner Agent

Responsibilities: - Intent detection - Category detection - Constraint
extraction - Tool routing

## Search Agent

Uses: - Elasticsearch - Pinecone - Neo4j

## Filter Agent

Applies: - Metadata constraints - Dynamic category filters

## Review Agent

Produces: - Sentiment - Pros - Cons - Complaints

## Recommendation Agent

Ranking: - Semantic score - BM25 score - Metadata score - Review score -
KG score - Personalization score

## Compare Agent

Produces structured comparisons.

## Explain Agent

Produces explainable recommendations.

## Memory Agent

Maintains: - Preferences - History - Sessions

------------------------------------------------------------------------

# Phase 9 --- Hybrid Retrieval

Formula:

Final Score = - 30% semantic - 25% BM25 - 20% metadata - 15% KG - 10%
personalization

Pipeline: 1. Retrieve BM25 2. Retrieve semantic 3. Retrieve KG 4. Merge
5. Rerank 6. Recommend

------------------------------------------------------------------------

# Phase 10 --- Reviews

Features: - Sentiment analysis - Aspect extraction - Pros/cons -
Summarization - Complaint mining

Tasks: - Chunk reviews - Embed reviews - Aggregate sentiment

------------------------------------------------------------------------

# Phase 11 --- Personalization

Store: - Preferred brands - Avoided brands - Budget - Favorite
categories - Previous interactions

Features: - Preference learning - Recommendation tuning

------------------------------------------------------------------------

# Phase 12 --- API Layer

Endpoints: - /search - /compare - /recommend - /explain - /memory -
/reviews - /products - /admin

Tasks: - Pydantic schemas - Validation - Error handling

------------------------------------------------------------------------

# Phase 13 --- Frontend

Pages: - Search - Product details - Compare - Recommendations - Profile

Components: - Chat interface - Filters - Cards - Comparison tables

------------------------------------------------------------------------

# Phase 14 --- Observability

Implement: - LangSmith tracing - Structured logging - Metrics - Latency
monitoring - Failure monitoring

------------------------------------------------------------------------

# Phase 15 --- Testing

Types: - Unit - Integration - Agent tests - Retrieval tests - API
tests - End-to-end tests

------------------------------------------------------------------------

# Phase 16 --- Deployment

Services: - FastAPI - PostgreSQL - Elasticsearch - Redis - Neo4j

Tasks: - Dockerfiles - Compose - Environment configs

------------------------------------------------------------------------

# Phase 17 --- Stretch Goals

-   Image similarity search
-   Visual shopping
-   Web fallback search
-   Price tracking
-   Multi-agent debate
-   Bundle recommendation
-   Shopping cart agent
-   Trend prediction
-   Purchase prediction

------------------------------------------------------------------------

# Success Criteria

The project demonstrates: - Agentic AI - Multi-agent systems - RAG -
Hybrid retrieval - Knowledge graphs - Recommendation systems - Search
engineering - Vector databases - Explainable AI - Personalization -
Production architecture
