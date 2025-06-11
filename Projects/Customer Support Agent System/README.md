# Customer Support Agent System

Fresh Fish Assistant is an intelligent multi-agent customer support system built using the OpenAI Agents SDK. It simulates real-time interactions for answering customer questions and handling orders.

## 🧠 Architecture

```
User → Triage Agent ─┬─> Query Agent
                     └─> Order Agent
```

- **Triage Agent**: Classifies user intent.
  - `GREET`: Sends a welcome message.
  - `QUERY`: Handoff to Query Agent.
  - `ORDER`: Handoff to Order Agent.

- **Query Agent**: Answers questions about the company (menu, fish types, freshness, etc.).
- **Order Agent**: Captures and confirms customer orders.

## 🔁 Flow

1. User sends a message.
2. Triage Agent decides which agent should respond.
3. Selected agent processes the message.
4. Response is returned to the user.

## ✅ Features

- Multi-agent routing via OpenAI Agents SDK.
- Order capture and confirmation loop.
- Asynchronous event handling (using asyncio).
- Simple REPL interface for testing.
- Designed for Gemini external client.

---