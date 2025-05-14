# LLM SEO Content Tool 🧠🔍

**Agent-ready SEO content generation tool with MCP and Tool profile support for modern LLM ecosystems.**

This repository provides an API-based SEO content generation utility designed for seamless integration with large language model (LLM) frameworks such as [LangChain](https://www.langchain.com/), [AutoGPT](https://github.com/Torantulino/Auto-GPT), [CrewAI](https://github.com/joaomdmoura/crewAI), and other agent-based platforms.

The tool is discoverable through an MCP-compliant manifest and a structured `tool_profile.json` interface — allowing AI agents to understand and invoke it autonomously.

---

## 🔗 Live Deployment

| Resource               | URL                                          |
|------------------------|----------------------------------------------|
| **MCP Manifest**       | `https://api.seogpt.dev/mcp-manifest`       |
| **Tool Profile**       | `https://api.seogpt.dev/tool_profile.json`  |
| **Tool Endpoint**      | Protected – requires `x-api-key` header     |

> 🛡️ Note: This endpoint is protected. You must provide a valid `x-api-key` in your request headers. Use the value defined in your `.env` file as `MASTER_KEY`.

---

## 💡 Features

- 🔧 **LangChain-compatible** Tool wrapper
- 🧠 **Persona-based SEO output** (e.g., `algo-chill`, `algo-expert`)
- 📄 Generates: `content_html`, `meta`, and `schema` fields
- 🌐 Fully accessible via public MCP manifest
- 🔐 API Key protected (`x-api-key` header)

---

## 🛠 Tool Specification

### Inputs

| Field     | Type     | Description                                 |
|-----------|----------|---------------------------------------------|
| `prompt`  | string   | Topic or idea for content generation        |
| `persona` | string   | Optional persona to adjust tone & style     |

### Outputs

- `content_html` — Structured HTML content  
- `meta` — Includes `title` and `description`  
- `schema` — JSON-LD or similar SEO markup structure  

---

## 🚀 Quickstart

### 🔹 Requirements
```bash
pip install langchain openai requests python-dotenv
```

### 🔹 Environment File

Create a `.env` file with:

```env
# Replace with your actual API key from seogpt.dev
MASTER_KEY=your-api-key-here
```

---

### 🔹 Tool Usage Example

```python
from langchain.agents import initialize_agent, AgentType
from langchain.chat_models import ChatOpenAI
from seo_tool import seo_tool

llm = ChatOpenAI(temperature=0, model="gpt-4")
agent = initialize_agent(
    tools=[seo_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

agent.run("Write SEO content about digital marketing")
```

---

## 📁 Files

| File                | Description                                  |
|---------------------|----------------------------------------------|
| `seo_tool.py`       | LangChain Tool wrapper for SEOGPT            |
| `run_agent.py`      | Sample usage with LangChain agent            |
| `tool_profile.json` | Agent-compatible structured tool description |
| `mcp_manifest.json` | MCP-style capability manifest for LLMs       |
| `.env.example`      | Sample environment file                      |
| `requirements.txt`  | Required packages for local use              |

---

## 📜 License

MIT License — free for public and commercial use.

---

## 🧠 Maintainer

This project is developed by [Uğur Arı](https://ugurari.com), powered by GPT-4o and designed for the future of autonomous content generation.

Feel free to use, fork, extend, or integrate with any agent you love.
