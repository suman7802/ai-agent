# AI Agent (Python)

A modular Python-based AI agent designed with best practices in mind.  
The project supports structured configuration, tool-based execution (e.g. weather, time, real-time utilities), and OpenAI-compatible Gemini models.

---

## Features

- OpenAI-compatible Gemini integration
- Modular agent and tool architecture
- Pydantic-based models for validation
- External tool support (weather, time, etc.)
- Config-driven setup
- Clean project structure suitable for extension

---

## Setup Instructions

### 1. Create and Activate Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Create Configuration File

```bash
cp config.example.ini config.ini
```

Edit `config.ini` and add your API key.

> ⚠️ Do not commit `config.ini` to GitHub.

---

### 4. Run the Application

```bash
python -m app.main
```

---
