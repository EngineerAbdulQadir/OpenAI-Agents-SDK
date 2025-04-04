from agents import Agent, Runner

agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant",
    
    # You Can Also Pass The Selected Model Of OpenAI
    # model="gpt-3.5-turbo",
)

result = Runner.run_sync(agent, "Write a haiku about recursion in programming.")
print(result.final_output)