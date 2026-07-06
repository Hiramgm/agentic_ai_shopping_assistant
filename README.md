# 🛒 Agentic AI Shopping Assistant

A production-inspired, category-agnostic **Agentic AI Shopping Assistant** built to explore and implement modern AI system design patterns, including **Agentic AI**, **Hybrid Retrieval**, **Knowledge Graphs**, **Recommendation Systems**, and **Multi-Agent Orchestration**.

The goal of this project is not to build another chatbot, but to design and implement a scalable shopping intelligence platform similar to next-generation AI shopping assistants.

---

## 🚀 Project Vision

Build an AI shopping agent capable of:

* Understanding natural language shopping queries
* Searching products across multiple categories
* Applying conversational filters
* Performing hybrid retrieval
* Comparing products
* Analyzing customer reviews
* Generating explainable recommendations
* Learning user preferences over time
* Leveraging knowledge graphs for reasoning
* Supporting multiple LLM providers through provider abstraction

### Example

**User:**

> Find a lightweight laptop for machine learning under $1500 with at least 32GB RAM.

**Follow-up:**

> Compare the top two options and explain which one is better for travel.

---

## 🏗️ Architecture Overview

```text
                    Frontend (Next.js)
                            |
                            v
                     FastAPI Backend
                            |
                            v
                    Agent Orchestrator
                            |
        ------------------------------------------------
        |           |          |          |            |
        v           v          v          v            v
     Planner     Search     Review    Compare      Memory
      Agent       Agent      Agent      Agent       Agent
                            |
                            v
        ------------------------------------------------
        | PostgreSQL | Elasticsearch | Pinecone | Neo4j |
        ------------------------------------------------
```

---

## ✨ Core Features

### 🤖 Agentic AI

* Multi-agent orchestration
* Tool calling
* Planning and reasoning
* Explainable responses

### 🔎 Search

* BM25 retrieval
* Semantic retrieval
* Metadata filtering
* Hybrid ranking

### 🕸️ Knowledge Graph

* Product relationships
* Brand relationships
* Similar products
* User preference graph

### 🎯 Recommendation Engine

* Personalized recommendations
* Explainable ranking
* Review-aware recommendations

### 🧠 Memory

* User preferences
* Search history
* Session memory

---

## 🛠️ Technology Stack

| Layer            | Technology             |
| ---------------- | ---------------------- |
| Backend          | FastAPI                |
| Agent Framework  | LangGraph              |
| Database         | PostgreSQL             |
| Search Engine    | Elasticsearch          |
| Vector Database  | Pinecone               |
| Knowledge Graph  | Neo4j                  |
| Cache            | Redis                  |
| Embeddings       | BAAI/bge-large-en-v1.5 |
| Frontend         | Next.js                |
| Observability    | LangSmith              |
| Containerization | Docker                 |

---

## 🔌 Provider Abstraction

The system is designed around provider abstraction, allowing components to be swapped without changing application logic.

### LLM Providers

Planned support:

* Groq
* OpenAI
* Ollama
* OpenRouter
* Local models

Example:

```env
LLM_PROVIDER=groq
LLM_MODEL=llama-3.3-70b-versatile
```

### Embedding Providers

Current implementation:

```env
EMBEDDING_PROVIDER=local
EMBEDDING_MODEL=BAAI/bge-large-en-v1.5
```

### Vector Database

```env
VECTOR_DB=pinecone
```

---

## 📁 Project Structure

```text
agentic-shopping-assistant/

├── backend/
│
│   ├── app/
│   │   ├── agents/
│   │   ├── api/
│   │   ├── core/
│   │   │   ├── config/
│   │   │   ├── logging/
│   │   │   ├── exceptions/
│   │   │   └── constants/
│   │   │
│   │   ├── providers/
│   │   │   ├── llm/
│   │   │   ├── embeddings/
│   │   │   ├── vector_db/
│   │   │   ├── search/
│   │   │   ├── graph/
│   │   │   └── memory/
│   │   │
│   │   ├── database/
│   │   ├── ingestion/
│   │   ├── retrieval/
│   │   ├── ranking/
│   │   ├── schemas/
│   │   ├── services/
│   │   └── utils/
│   │
│   ├── tests/
│   └── docker/
│
├── frontend/
├── docs/
├── data/
└── scripts/
```

---

## ✅ Current Progress

### Foundation Layer

* [x] Repository structure
* [x] FastAPI setup
* [x] Environment configuration
* [x] Settings management
* [x] Structured logging
* [x] Request middleware logging
* [x] Exception handling
* [x] Provider abstraction architecture design

### In Progress

* [ ] Embedding provider factory
* [ ] LLM provider factory
* [ ] Vector DB provider factory
* [ ] Search provider factory
* [ ] Graph provider factory
* [ ] Memory provider factory

---

## 🗺️ Development Roadmap

### Phase 1

* Project setup
* Configuration management
* Provider abstraction layer

### Phase 2

* Database design
* Product schema engine

### Phase 3

* Data ingestion pipeline

### Phase 4

* Elasticsearch integration

### Phase 5

* Pinecone integration

### Phase 6

* Neo4j knowledge graph

### Phase 7

* Hybrid retrieval

### Phase 8

* Agent framework

### Phase 9

* Recommendation engine

### Phase 10

* Frontend

### Phase 11

* Deployment

---

## 🎓 Learning Objectives

This project is designed to provide hands-on experience with:

* Agentic AI
* Multi-agent systems
* Retrieval-Augmented Generation (RAG)
* Hybrid search architectures
* Knowledge graphs
* Recommendation systems
* Vector databases
* Search engineering
* Explainable AI
* Production AI architecture
* Personalization systems

---

## 📌 Project Status

🚧 **Currently under active development.**

The project is being built incrementally using production-inspired software engineering and AI architecture practices.

---

## 📄 License

This project is currently being developed for educational, research, and portfolio purposes.
