# Streaming

In streaming mode, the `agents` framework emits **events** continuously as the model and tools execute, rather than buffering the entire output and returning it in one go. This allows you to:

- Display partial results (e.g., typing effect in a chat UI)
- Trigger actions as soon as they happen (e.g., log tool calls immediately)
- Reduce perceived latency for end users


## Why Use Streaming?

- **Lower latency**: start showing content instantly.
- **Real-time processing**: handle each event (tool call, text chunk) on the fly.
- **Progressive UIs**: build interfaces that feel responsive and dynamic.


## Setting Up a Streamed Run

Use the `Runner.run_streamed` API instead of `run`:

```python
result = Runner.run_streamed(
    agent,
    input="Please tell me 5 jokes."
)
```

- `agent`: your configured `Agent` instance.
- `input`: the prompt or message to send.
- Returns a `StreamedRunResult` whose `.stream_events()` method yields events.


## Handling Stream Events

Callers can iterate over `result.stream_events()` to receive different event types:

```python
async for event in result.stream_events():
    ...  # Inspect and dispatch on event
```

### Text Delta Events

- **Type**: `raw_response_event`
- **Data**: `ResponseTextDeltaEvent` with `.delta` (text fragment)
- **Use**: print or render each fragment:
  ```python
  if event.type == "raw_response_event":
      print(event.data.delta, end="", flush=True)
  ```

### Agent Update Events

- **Type**: `agent_updated_stream_event`
- **Data**: `.new_agent` (the replacement agent)
- **Use**: log agent switches:
  ```python
  if event.type == "agent_updated_stream_event":
      print(f"Agent updated: {event.new_agent.name}")
  ```

### Run Item Events

- **Type**: `run_item_stream_event`
- **Data**: `.item` with subtype:
  - `tool_call_item`: agent is invoking a tool
  - `tool_call_output_item`: result of the tool call is available
  - `message_output_item`: a complete chat message

Example dispatch:

```python
elif event.type == "run_item_stream_event":
    item = event.item
    if item.type == "tool_call_item":
        print("-- Tool was called")
    elif item.type == "tool_call_output_item":
        print(f"-- Tool output: {item.output}")
    elif item.type == "message_output_item":
        print("-- Message:\n", ItemHelpers.text_message_output(item))
```  


## Example: Printing Jokes as They Arrive

```python
async def main():
    result = Runner.run_streamed(agent, input="Please tell me 5 jokes.")

    async for event in result.stream_events():
        # Skip raw text deltas
        if event.type == "raw_response_event":
            continue

        # Agent updated
        if event.type == "agent_updated_stream_event":
            print(f"Agent updated: {event.new_agent.name}")
            continue

        # Tool and message outputs
        if event.type == "run_item_stream_event":
            item = event.item
            if item.type == "tool_call_item":
                print("-- Tool was called")
            elif item.type == "tool_call_output_item":
                print(f"-- Tool output: {item.output}")
            elif item.type == "message_output_item":
                print("-- Message:\n", ItemHelpers.text_message_output(item))


# Event Loop
asyncio.run(main())
```