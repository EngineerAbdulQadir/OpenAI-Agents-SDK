# OpenAI Agents SDK: Structured Output

The **OpenAI Agents SDK** is a powerful toolkit for building AI agents that can perform tasks and interact with users across various applications. A key feature, **Structured Output**, allows agents to generate responses in predefined, machine-readable formats like JSON, enabling seamless integration with other systems.

---

## Table of Contents

1. [Introduction](#introduction)
2. [What is Structured Output?](#what-is-structured-output)
3. [How Structured Output Works](#how-structured-output-works)
4. [Implementing Structured Output](#implementing-structured-output)
5. [Customizing Structured Output](#customizing-structured-output)
6. [Use Case Examples](#use-case-examples)
7. [Best Practices](#best-practices)
8. [Conclusion](#conclusion)

---

## Introduction

The OpenAI Agents SDK empowers developers to create AI agents for tasks like customer support, data processing, and more. **Structured Output** ensures that agent responses are delivered in a consistent, predefined format, such as JSON, making them ideal for applications requiring parseable data.

---

## What is Structured Output?

**Structured Output** is a feature that constrains an AI agent’s responses to a specific schema, typically JSON. This ensures predictable, machine-readable outputs for use in APIs, databases, or other systems. For example, instead of freeform text, an agent might return:

```json
{
  "name": "John",
  "age": 30
}
```

---

## How Structured Output Works

Structured Output relies on the SDK’s integration with language models that support schema-constrained generation. The process includes:

1. **Schema Definition**: Developers specify a schema (e.g., JSON schema) for the output format.
2. **Agent Configuration**: The agent is set to enforce the schema via SDK parameters.
3. **Processing**: The LLM generates a response adhering to the schema.
4. **Validation**: The SDK ensures the output matches the schema, raising errors if necessary.

---

## Implementing Structured Output

To use Structured Output, define a schema and configure the agent accordingly.

### Basic Example

```python
from agents import Agent

# Define a JSON schema
schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "integer"}
    },
    "required": ["name", "age"]
}

# Configure the agent
agent = Agent(
    name="User Info Agent",
    instructions="Extract user information from input.",
    response_format=schema
)

# Run the agent
response = agent.run("John is 30 years old.")
print(response)
# Output: {"name": "John", "age": 30}
```

---

## Customizing Structured Output

Structured Output can be tailored to specific needs:

- **Complex Schemas**: Support nested objects, arrays, or optional fields.
- **Error Handling**: Configure retries or fallback responses for invalid outputs.
- **Validation Rules**: Enforce constraints like minimum/maximum values or patterns.

### Example with Complex Schema

```python
schema = {
    "type": "object",
    "properties": {
        "user": {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "age": {"type": "integer", "minimum": 18}
            },
            "required": ["name", "age"]
        },
        "orders": {
            "type": "array",
            "items": {"type": "string"}
        }
    },
    "required": ["user"]
}

agent = Agent(
    name="Order Agent",
    instructions="Extract user and order data.",
    response_format=schema
)

response = agent.run("John, 30, ordered books and shoes.")
print(response)
# Output: {"user": {"name": "John", "age": 30}, "orders": ["books", "shoes"]}
```

---

## Use Case Examples

### API Integration

- **Scenario**: An agent processes user queries for a REST API.
- **Structured Output**: Returns JSON data like `{"status": "success", "result": {...}}`.

### Database Ingestion

- **Scenario**: An agent extracts customer data for a CRM.
- **Structured Output**: Formats data as `{"customer_id": 123, "name": "John"}`.

---

## Best Practices

- **Keep Schemas Simple**: Avoid overly complex schemas to ensure LLM compliance.
- **Validate Outputs**: Test outputs to confirm schema adherence.
- **Handle Errors**: Implement fallback logic for cases where the LLM fails to produce valid output.
- **Monitor Performance**: Assess any latency introduced by structured generation.

---

## Conclusion

Structured Output in the OpenAI Agents SDK enables developers to build AI agents that produce consistent, machine-readable responses. By enforcing predefined schemas, it simplifies integration and enhances reliability, making it a vital tool for production-ready AI applications.