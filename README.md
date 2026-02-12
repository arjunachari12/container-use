
# Self-Debugging, Doc-Indexing AI Stack

## Overview
This project demonstrates:
- Document indexing using embeddings
- Vector storage with Chroma
- Retrieval-Augmented Generation (RAG)
- Self-debugging coding agent
- Containerized execution using Docker

## Prerequisites
- Docker
- Docker Compose
- OpenAI API Key

## Setup

1. Export API key:
   export OPENAI_API_KEY=your_key_here

2. Start services:
   docker compose up --build

## Index Documents
docker compose run indexer

## Run RAG Query
docker compose run rag

## Run Self-Debugging Agent
docker compose run agent

## Architecture
User → Indexer → Vector DB → RAG → Self-Debugging Agent

This is a modular, containerized, production-style AI workflow stack.
