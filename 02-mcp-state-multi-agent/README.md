# 02 · MCP, Runtime Context, State & Multi-Agent

Module 2 of the LangChain Academy *LangChain Foundations* course. Module 1 covered a single agent with tools and memory; here the agents get external tools through MCP, share context and state, and are composed into teams of subagents.

## Notebooks

| Notebook | What it covers |
| --- | --- |
| `2.1_mcp.ipynb` | Connecting to a local MCP server (`resources/2.1_mcp_server.py`) and an online MCP server with `langchain-mcp-adapters` |
| `2.1_travel_agent.ipynb` | A travel agent that uses MCP tools |
| `2.2_runtime_context.ipynb` | Passing read-only runtime context to tools |
| `2.2_state.ipynb` | Writing to and reading from custom agent state |
| `2.3_multi_agent.ipynb` | Subagents wrapped as tools and called by a main agent |
| `2.4_wedding_planners.ipynb` | Mini project: a multi-agent wedding planner with a coordinator and specialist subagents |
| `bonus_rag.ipynb` | Semantic search over a PDF handbook and a RAG agent |
| `bonus_sql.ipynb` | A SQL agent over the Chinook sample database |

## Resources

| File | Used by |
| --- | --- |
| `resources/2.1_mcp_server.py` | Local MCP server exposing a Tavily search tool and a GitHub README resource |
| `resources/acmecorp-employee-handbook.pdf` | `bonus_rag.ipynb` |
| `resources/Chinook.db` | `bonus_sql.ipynb` |

## Setup

Requires Python 3.12+ and [uv](https://docs.astral.sh/uv/) (`uvx` is used to launch the MCP server).

```bash
cd 02-mcp-state-multi-agent
cp .env.example .env   # add GOOGLE_API_KEY and TAVILY_API_KEY
uv venv && source .venv/bin/activate
uv pip install langchain langchain-google-genai langgraph langchain-mcp-adapters mcp tavily-python \
  langchain-community langchain-text-splitters pypdf python-dotenv jupyter
jupyter lab
```

Run the notebooks from this folder so the relative `resources/` paths resolve.
