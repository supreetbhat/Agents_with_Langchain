# 03 · Message Management, Human-in-the-Loop & Dynamic Agents

Module 3 of the LangChain Academy *LangChain Foundations* course. It covers keeping long conversations manageable, putting a human in control of risky tool calls, changing an agent's model, prompt and tools at runtime, and ends with an email agent that combines all of it.

## Notebooks

| Notebook | What it covers |
| --- | --- |
| `3.2_managing_messages.ipynb` | Summarizing, trimming and deleting messages to keep context small |
| `3.3_hitl.ipynb` | Human-in-the-loop middleware: approve, reject or edit tool calls |
| `3.4_dynamic_models.ipynb` | Switching the model per request |
| `3.4_dynamic_prompts.ipynb` | Building the system prompt from runtime context |
| `3.4_dynamic_tools.ipynb` | Exposing different tools depending on state |
| `3.5_email_agent.ipynb` / `.py` | Mini project: an email agent that authenticates the user, then unlocks inbox tools, with approval before sending |

## Other files

| Path | Purpose |
| --- | --- |
| `langgraph.json` | Serves the email agent (`3.5_email_agent.py:agent`) with `langgraph dev` |
| `agent-chat-ui/` | Next.js chat UI (from LangChain) for talking to the LangGraph server, including approving interrupts |
| `resources/Chinook.db` | Sample SQLite database used by the notebooks |

## Setup

Requires Python 3.12+ and [uv](https://docs.astral.sh/uv/).

```bash
cd 03-memory-hitl-dynamic-agents
cp .env.example .env   # add GOOGLE_API_KEY (and optionally LangSmith keys)
uv venv && source .venv/bin/activate
uv pip install langchain langchain-google-genai langgraph "langgraph-cli[inmem]" \
  langchain-community python-dotenv jupyter
jupyter lab
```

### Run the email agent with the chat UI

```bash
# Terminal 1: LangGraph server on http://localhost:2024
uv run langgraph dev

# Terminal 2: chat UI (needs Node.js and pnpm)
cd agent-chat-ui
cp .env.example .env
pnpm install && pnpm dev
```

Or use the hosted UI at [agentchat.vercel.app](https://agentchat.vercel.app) pointed at `http://localhost:2024` with assistant ID `agent`.

The demo login is `julie@example.com` / `password123`.
