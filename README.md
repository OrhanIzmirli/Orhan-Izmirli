# Thought-to-Task Agent

This project is an agent-based system that converts unstructured human thoughts into structured, prioritized tasks and a daily execution plan.

The goal of the project is to demonstrate how an agent can reason over messy human input and transform it into actionable steps using a clean and extensible architecture.

---

## Overview

Users can freely write unstructured, messy thoughts such as goals, reminders, or intentions.  
The agent processes this input and produces:

- Prioritized tasks
- Task categories
- Time estimates
- Execution tips
- A summarized daily plan

---

## Architecture

**Backend**
- FastAPI
- REST-based API interface

**Agent Layer**
- Custom planning logic
- Task structuring and prioritization
- Execution flow management

**Frontend**
- Lightweight HTML-based UI
- Communicates with the agent via REST API

**LLM Support**
- Designed to be fully LLM-agnostic
- Gemini integration implemented
- Currently running in demo fallback mode due to free-tier quota limits
- Can be switched to Gemini, Groq, or local models without changing the API or frontend

---

## How It Works

1. User submits an unstructured thought
2. The agent analyzes intent and extracts tasks
3. Tasks are categorized and prioritized
4. Time estimates and execution tips are generated
5. A daily execution plan is created

---

## How to Run

```bash
python -m uvicorn src.api:app --reload
