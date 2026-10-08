
from pydantic_ai import Agent 
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.ollama import OllamaProvider 

from tools.file_tools import read_file, write_file

model = OpenAIChatModel(
    "qwen3:latest",
    provider=OllamaProvider(
        base_url="http://localhost:11434/v1"
    )
)

berry = Agent(
    model,
    system_prompt="""
    You are BERRY, a personal AI assistant.
    You can read and write files when necessary.
    """
)

@berry.tool
def read_file_tool(ctx, filename: str) -> str:
    return read_file(filename)


@berry.tool
def write_file_tool(ctx, filename: str, content: str) -> str:
    return write_file(filename, content)


result = berry.run_sync("Hello Berry!")
print(result.output)


history=[]
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Berry: Bye bye! 🫐")
        break
    result=berry.run_sync(user_input,message_history=history)
    history=result.all_messages()

    # result = berry.run_sync(user_input)
    print(f"Berry: {result.output}")
