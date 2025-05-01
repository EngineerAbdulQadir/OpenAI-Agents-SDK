# Synchronous VS Asynchronous

Choosing between **sync** and **async** affects:
- **Performance**: Can your app block while waiting for an LLM response?
- **Concurrency**: Do you need to handle many LLM calls in parallel?
- **Complexity**: Are you comfortable working with `async/await` and event loops?

---

## Synchronous (Sync)

Your code **blocks** until each Agent or Runner call completes. No other work in that thread can proceed.

### When to Use

- Simple scripts, CLIs, or prototypes  
- Environments without an event loop (no `asyncio`)  
- Low request volume or “one-at-a-time” workflows  

### Code Example

```python
from agents import Runner

# Blocks until the conversation finishes
result = Runner.run(
    root_agent,
    input="Hello, sync world!",
    max_turns=5
)
print(result)
```

### Pros & Cons

| Pros                                | Cons                                            |
|-------------------------------------|-------------------------------------------------|
| Straightforward, linear control     | Cannot overlap I/O with other work              |
| Easy to read and debug              | Poor scalability under concurrent load          |
| No event-loop boilerplate required  | Blocks the entire thread during LLM calls       |

---

## Asynchronous (Async)

Your code returns immediately (a coroutine) and can **await** multiple tasks concurrently within an event loop.

### When to Use

- High-throughput web servers or bots  
- Workloads with many parallel LLM calls  
- Scenarios where overlapping I/O boosts performance  

### Code Example

```python
import asyncio
from agents import AsyncRunner

async def main():
    # Schedule the run and await its result
    result = await AsyncRunner.run(
        root_agent,
        input="Hello, async world!",
        max_turns=5
    )
    print(result)

asyncio.run(main())
```

### Pros & Cons

| Pros                                               | Cons                                          |
|----------------------------------------------------|-----------------------------------------------|
| Supports many concurrent LLM calls in-flight       | Requires `async/await` boilerplate           |
| Better resource utilization for I/O-bound tasks    | Must run inside an event loop (e.g. `asyncio`)|
| Reduced total latency when fan-outing requests     | Slightly more complex control flow           |

---

## Quick Comparison

| Feature                | Sync                            | Async                             |
|------------------------|---------------------------------|-----------------------------------|
| **Blocking**           | Yes                             | No                                |
| **Concurrency**        | One call at a time              | Multiple calls in parallel        |
| **Ease of Use**        | Very simple                     | More boilerplate (`async/await`) |
| **Best Fit**           | CLI tools, simple scripts       | Web backends, bots, heavy I/O     |
| **Requires Event Loop**| No                              | Yes                               |

---