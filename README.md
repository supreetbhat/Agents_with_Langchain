# Agents 

> **I'm learning, and this repo will grow.** It's my personal notebook for building AI agents with [LangChain](https://python.langchain.com) and [LangGraph](https://langchain-ai.github.io/langgraph/). Expect rough edges, experiments, and new folders over time.

Based on the [LangChain Academy – LangChain Foundations](https://github.com/langchain-ai/lca-lc-foundations) course, with my own tweaks and notes.

## Contents

| Folder | Topic | Status |
| --- | --- | --- |
| [01-langchain-foundations](./01-langchain-foundations) | LangChain foundations: models, prompting, tools, web search, memory, multimodal messages, and a personal chef agent | ✅ Done |
| [02-mcp-state-multi-agent](./02-mcp-state-multi-agent) | MCP, runtime context, state, multi-agent systems, plus RAG and SQL bonus labs | ✅ Done |
| [03-memory-hitl-dynamic-agents](./03-memory-hitl-dynamic-agents) | Message management, human-in-the-loop, dynamic models/prompts/tools, and an email agent | ✅ Done |

## 01-langchain-foundations

| Notebook | What it covers |
| --- | --- |
| `1.1_foundational_models.ipynb` | Calling chat models and creating a basic agent |
| `1.1_prompting.ipynb` | System prompts and structured output |
| `1.2_tools.ipynb` | Defining and using custom tools |
| `1.2_web_search.ipynb` | Giving an agent web search with Tavily |
| `1.3_memory.ipynb` | Short-term memory with checkpointers |
| `1.4_multimodal_messages.ipynb` | Sending images to the model |
| `1.5_personal_chef.ipynb` / `.py` | Mini project: a chef agent that searches the web for recipes |

## 02-mcp-state-multi-agent

| Notebook | What it covers |
| --- | --- |
| `2.1_mcp.ipynb` / `2.1_travel_agent.ipynb` | Using local and online MCP servers as agent tools |
| `2.2_runtime_context.ipynb` | Passing runtime context to tools |
| `2.2_state.ipynb` | Reading and writing custom agent state |
| `2.3_multi_agent.ipynb` | Subagents called as tools |
| `2.4_wedding_planners.ipynb` | Mini project: multi-agent wedding planner |
| `bonus_rag.ipynb` / `bonus_sql.ipynb` | RAG over a PDF and a SQL agent on Chinook |

See the [module README](./02-mcp-state-multi-agent/README.md) for details.

## 03-memory-hitl-dynamic-agents

| Notebook | What it covers |
| --- | --- |
| `3.2_managing_messages.ipynb` | Summarizing and trimming messages |
| `3.3_hitl.ipynb` | Approving, rejecting and editing tool calls |
| `3.4_dynamic_models.ipynb` / `_prompts` / `_tools` | Changing model, prompt and tools at runtime |
| `3.5_email_agent.ipynb` / `.py` | Mini project: email agent with login, dynamic tools and approval; served with `langgraph dev` and `agent-chat-ui/` |

See the [module README](./03-memory-hitl-dynamic-agents/README.md) for details.

## Setup

Requires Python 3.11+ and [uv](https://docs.astral.sh/uv/).

```bash
git clone https://github.com/supreetbhat/Agents.git
cd Agents/01-langchain-foundations

uv venv && source .venv/bin/activate
uv pip install langchain langchain-google-genai langgraph "langgraph-cli[inmem]" tavily-python python-dotenv jupyter

cp .env.example .env   # then add your API keys
```

You need a [Google AI Studio](https://aistudio.google.com/apikey) key and a [Tavily](https://tavily.com) key.

### Run the personal chef agent in LangGraph Studio

```bash
cd 01-langchain-foundations
uv run langgraph dev
```

## Roadmap

- [x] MCP, runtime context, state, multi-agent
- [x] Message management, human-in-the-loop, dynamic models/prompts/tools, email agent
- [ ] More agent projects of my own

## Credits

Course material by [LangChain](https://github.com/langchain-ai/lca-lc-foundations).
