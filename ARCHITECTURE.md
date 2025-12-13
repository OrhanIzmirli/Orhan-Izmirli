# Architecture Overview

This project follows a modular agent-based architecture designed to transform unstructured human thoughts into structured, actionable task plans.

## High-Level Flow

User Input
→ Agent API (FastAPI)
→ Planner
→ (Optional) Memory
→ Executor (LLM / Demo Mode)
→ Structured Tasks + Daily Plan

## Components

### 1. API Layer (FastAPI)
- Entry point for user requests
- Exposes REST endpoints for agent execution
- Handles request/response lifecycle

### 2. Planner
- Breaks down unstructured user input into clear sub-tasks
- Assigns priorities, categories, and time estimates
- Produces an execution-ready task structure

### 3. Memory
- Stores previous inputs and outputs
- Enables future extensibility for long-term context or personalization
- Currently used for logging and traceability

### 4. Executor
- Responsible for calling the LLM (Gemini API or demo fallback)
- Handles tool execution and response formatting
- Abstracted to support multiple LLM providers

## LLM Integration

- Google Gemini API is integrated as the primary LLM
- A demo fallback mode is used when free-tier quota is unavailable
- The system is LLM-agnostic and can switch providers without API changes

## Observability & Logging

- Requests and responses are logged for transparency
- Memory history enables inspection of agent decisions
