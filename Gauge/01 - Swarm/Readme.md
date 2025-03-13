# 01 - Swarm: OpenAI’s Experimental Multi-Agent Framework

Swarm was OpenAI’s early, experimental framework for orchestrating multi-agent workflows. It introduced a minimalistic design built on two key abstractions:

- **Agents:** Lightweight units that encapsulate specific instructions and tool functions. Each agent functions as an independent “LLM with a purpose.”
- **Handoffs:** A simple mechanism to transfer control between agents, enabling a network of specialized agents to collaboratively tackle complex tasks.

---

## Overview

Swarm was designed as a client-side, stateless wrapper around the Chat Completions API. It provided an accessible way for developers to learn about multi-agent orchestration without the overhead of production-ready systems. Although Swarm is intended primarily for educational and demo purposes, its core concepts have paved the way for more robust solutions.

Recognizing the need for real-world applications, OpenAI has evolved Swarm into the **OpenAI Agents SDK**. The new SDK builds on these foundational ideas and offers enhanced safety features, observability tools, and production-grade stability.

---

## Features

- **Minimalistic Design:** Focuses on essential multi-agent orchestration concepts without unnecessary complexity.
- **Agent Abstraction:** Define agents with clear instructions and tool functions.
- **Simple Handoffs:** Easily transfer control between agents to manage complex workflows.
- **Educational Value:** Ideal for demos, proof-of-concepts, and learning experiments.
- **Foundation for Production:** Inspires the more advanced OpenAI Agents SDK for robust, real-world applications.

---

## Installation

Swarm is available as an open-source Python package. To install Swarm, run:

```bash
pip install git+https://github.com/openai/swarm.git
```

> **Note:** For any production use cases, please migrate to the [OpenAI Agents SDK](#).

---

## Usage

Below is a simple example demonstrating how to create an agent and run a conversation using Swarm:

```python
from swarm import Swarm, Agent

# Initialize the Swarm client
client = Swarm()

# Create an agent with specific instructions
agent = Agent(
    name="Example Agent",
    instructions="You are a helpful agent."
)

# Run the agent with an initial user message
response = client.run(
    agent=agent,
    messages=[{"role": "user", "content": "Hello, Agent!"}]
)

# Print the agent's final response
print(response.messages[-1]["content"])
```

---

## Transition to OpenAI Agents SDK

OpenAI has since transitioned from Swarm to the [OpenAI Agents SDK](#), which offers:
- Enhanced safety and observability features
- Improved control flow and orchestration for multi-agent workflows
- Production-grade stability and support

Developers are encouraged to adopt the Agents SDK for any serious or production use.

---

## Acknowledgements

Swarm was developed by the OpenAI Solutions team as an experimental framework to explore the fundamentals of multi-agent orchestration. For more detailed information and updates on production-ready solutions, please visit the [OpenAI website](https://openai.com).

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---