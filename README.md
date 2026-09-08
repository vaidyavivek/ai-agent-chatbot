# AI Agent Chatbot 🤖

A conversational AI agent built with **Python**, **LangChain**, and **LangGraph**.
Unlike a regular chatbot that only generates text, this agent reasons, selects 
tools, and acts — deciding when to answer directly vs. when to use a tool.

## What Makes This an Agent?

- Understands when to use tools vs. when to respond directly
- Maintains conversation state across multiple turns using LangGraph
- Executes custom tools based on user intent
- Reasons through problems before responding

## Features

- 🧠 Stateful multi-turn conversations via LangGraph's state machine
- 🔧 Custom tool-calling — agent decides when and how to use tools
- 🧮 Built-in calculator tool for math queries
- 💬 Powered by OpenAI's GPT model

## Sample Conversation

You: What is 1234 multiplied by 567?
Agent: [Calling calculator tool...]
Agent: 1234 × 567 = 699,678

You: Now divide that by 3
Agent: [Calling calculator tool...]
Agent: 699,678 ÷ 3 = 233,226

You: What else can you help with?
Agent: I can answer questions, help with calculations, and reason
through multi-step problems. Just ask!

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core language |
| LangChain | LLM orchestration and tool integration |
| LangGraph | Stateful agent workflow management |
| OpenAI API | GPT model for reasoning |
| uv | Fast Python package management |

## Prerequisites

- Python 3.11+
- OpenAI API key

## How to Run

1. Clone the repo
```bash
git clone https://github.com/vaidyavivek/ai-agent-chatbot.git
cd ai-agent-chatbot
```

2. Create a `.env` file with your OpenAI API key:
```
OPENAI_API_KEY=your_key_here
```

3. Install and run
```bash
uv run src/project1/main.py
```

## Project Structure
```
ai-agent-chatbot/
├── src/
│   └── project1/
│       └── main.py
├── .env
├── pyproject.toml
└── README.md
```
