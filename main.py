
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
You are BERRY, a capable and intelligent personal AI assistant.

- Give helpful, specific, and detailed answers when appropriate.
- Understand the user's actual question before responding.
- Avoid repeating generic greetings or saying "How can I assist you?" unnecessarily.
- Maintain context across the conversation.
- Use your available tools when they are relevant.
- Be natural, friendly, and conversational.
- If you do not know something, say so honestly.
"""
)

@berry.tool
def read_file_tool(ctx, filename: str) -> str:
    return read_file(filename)


@berry.tool
def write_file_tool(ctx, filename: str, content: str) -> str:
    return write_file(filename, content)


if __name__ == "__main__":
    result = berry.run_sync("Hello Berry!")
    print(result.output)



# history=[]
# while True:
#     user_input = input("You: ")
#     if user_input.lower() in ["exit", "quit", "bye"]:
#         print("Berry: Bye bye! 🫐")
#         break
#     result=berry.run_sync(user_input,message_history=history)
#     history=result.all_messages()

#     # result = berry.run_sync(user_input)
#     print(f"Berry: {result.output}")

# input_box.bind("<Return>", lambda event: send_message())

history = []

def ask_berry(user_message):
    global history
    result = berry.run_sync(user_message, message_history=history)
    history = result.all_messages()
    return result.output
    
