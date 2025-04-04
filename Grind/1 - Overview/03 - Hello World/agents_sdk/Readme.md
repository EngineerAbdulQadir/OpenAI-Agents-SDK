- **Agent:**  
  *Definition:* Represents an AI entity with a defined persona and instructions.  
  *Example:*  
  ```python
  agent = Agent(name="Assistant", instructions="You are a helpful assistant")
  ```

- **Runner:**  
  *Definition:* Manages and executes tasks for an Agent.  
  *Example:*  
  ```python
  result = Runner.run_sync(agent, "Write a haiku about recursion in programming.")
  ```

- **run_sync (part of Runner):**  
  *Definition:* A synchronous function that sends a prompt to the agent and returns the processed output.  
  *Example:*  
  ```python
  output = Runner.run_sync(agent, "Explain recursion in one line.")
  ```