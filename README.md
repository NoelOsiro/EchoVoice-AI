# PersonalizeAI (EchoVoice-AI workspace)

This repository contains a scaffold for "PersonalizeAI" — a Multi-Agent AI Personalization Platform (orchestrator + agents + frontend stub).

Quick start (backend):

1. Copy `.env.template` to `.env` and fill API keys.
2. Create a Python virtualenv and install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

3. Run the backend orchestrator (development):

```bash
cd backend
# Install dependencies first (see requirements.txt)
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

Then POST an event to `http://127.0.0.1:8000/orchestrate` with JSON payload to simulate the pipeline.

Repository layout (scaffold):

```
PersonalizeAI/
├── README.md
├── requirements.txt
├── package.json
├── .env.template
├── data/
├── frontend/
└── backend/
```

This is an initial scaffold with simple, mock implementations for each agent to help you prototype the orchestration flow.
#Microsoft Innovation Challenge November 2025# AI-powered multi-agent system for safe, on-brand customer personalization with segmentation, content retrieval, message generation, and A/B/n experimentation.
