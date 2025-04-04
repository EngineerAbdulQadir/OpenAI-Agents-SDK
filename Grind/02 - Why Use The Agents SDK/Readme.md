# 02 - Why Use the Agents SDK

The Agents SDK is built on two fundamental design principles:

- **Balanced Simplicity and Functionality:**  
  It provides enough features to be truly useful while keeping the number of primitives minimal, ensuring a fast and smooth learning curve.

- **Out-of-the-Box Excellence with Customizability:**  
  It works seamlessly from the start, yet offers the flexibility to customize exactly how your agents operate.

---

## Key Features

- **Agent Loop:**  
  A built-in agent loop manages the process of calling tools, transmitting results back to the LLM, and iterating until the LLM completes its tasks.

- **Python-First:**  
  Utilize native Python features to orchestrate and chain agents without having to adopt entirely new abstractions.

- **Handoffs:**  
  Empower your application with the ability to coordinate and delegate tasks among multiple agents effortlessly.

- **Guardrails:**  
  Execute input validations and checks in parallel with your agents, ensuring that any errors are caught early and handled gracefully.

- **Function Tools:**  
  Convert any Python function into a tool, complete with automatic schema generation and robust Pydantic-powered validation.

- **Tracing:**  
  Built-in tracing capabilities allow you to visualize, debug, and monitor your workflows, alongside leveraging the OpenAI suite for evaluation, fine-tuning, and distillation.

---