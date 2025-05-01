## Model Configuration Levels

The OpenAI Agents SDK supports model configuration at three different levels, allowing for flexible and layered control over which LLM is used where.

| **Level**       | **What It Is**                                      | **Priority**        | **When to Use**                                            | **Example**                                                                                         |
|-----------------|-----------------------------------------------------|---------------------|------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| **Global**      | Default model/client for **all** Agents and Runners | 🔽 Lowest (fallback) | To apply the same API key or base URL throughout the app   | ```python<br>from agents import set_default_openai_client, AsyncOpenAI<br><br>set_default_openai_client(<br>    AsyncOpenAI(api_key="KEY", base_url="https://api.example.com/v1")<br>)``` |
| **Runner**      | Overrides global for **one run**                    | 🔼 Middle            | To use a different LLM just for one execution              | ```python<br>from agents import Runner, ModelProvider<br><br>provider = ModelProvider.from_config(...)<br>Runner.run(<br>    root_agent,<br>    input="Start task",<br>    model_provider=provider,<br>    max_turns=5<br>)``` |
| **Agent**       | Individual Agent uses its **own** model             | 🔼🔼 Highest           | To let different agents use different LLMs in the same run | ```python<br>from agents import Agent, OpenAIChatCompletionsModel<br><br>expert = Agent(<br>    name="Expert",<br>    instructions="Solve math problems",<br>    model=OpenAIChatCompletionsModel(model="gpt-4o", openai_client=AsyncOpenAI()),<br>    model_settings={"temperature": 0}<br>)``` |

### 📌 Summary
- **Global Level**: Good for setting the same base URL or API key app-wide.
- **Runner Level**: Good for trying a different LLM just for one task.
- **Agent Level**: Best for giving each agent a specialized behavior or model.

> 🔁 Use all three together to build scalable, modular, and powerful agent systems.