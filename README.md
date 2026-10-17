# Agents 🤖

> **I'm learning, and this repo will grow.** It's my personal notebook for building AI agents with [LangChain](https://python.langchain.com) and [LangGraph](https://langchain-ai.github.io/langgraph/). Expect rough edges, experiments, and new folders over time.

Based on the [LangChain Academy – LangChain Foundations](https://github.com/langchain-ai/lca-lc-foundations) course, with my own tweaks and notes.

## Contents

| Folder | Topic | Status |
| --- | --- | --- |
| [01-langchain-foundations](./01-langchain-foundations) | LangChain foundations: models, prompting, tools, web search, memory, multimodal messages, and a personal chef agent | ✅ Done |
| `02-…` (planned) | MCP, runtime context, state, multi-agent | 🚧 Coming soon |
| `03-…` (planned) | Message management, human-in-the-loop, dynamic models/prompts/tools, email agent | 🚧 Coming soon |

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

- [ ] Next up: MCP, runtime context, state, multi-agent
- [ ] After that: human-in-the-loop, dynamic models/prompts/tools, email agent
- [ ] More agent projects of my own

## Credits

Course material by [LangChain](https://github.com/langchain-ai/lca-lc-foundations).
