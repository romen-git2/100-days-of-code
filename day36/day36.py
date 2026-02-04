import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
from langchain.agents import create_agent 

load_dotenv()
if not os.getenv("GOOGLE_API_KEY"):
    print("Error: GOOGLE_API_KEY not found.")
    exit(1)

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.0)

# define tools
@tool
def get_word_length(word: str) -> int:
    """Returns the exact character count of a word. Use this for word length tasks."""
    length = len(word)
    print(f"'{word}' has {length} letters.")
    return length

@tool
def power_calculator(base: int, exponent: int) -> int:
    """Calculates base raised to the power of exponent (base^exponent)."""
    result = base ** exponent
    print(f"{base}^{exponent} = {result}")
    return result

tools = [get_word_length, power_calculator]

agent_executor = create_agent(
    model=llm, 
    tools=tools,
    system_prompt="You are a helpful assistant that uses tools for math and word lengths."
)

if __name__ == "__main__":

    query = (
        "Find the length of the word 'pneumonoultramicroscopicsilicovolcanoconiosis', "
        "subtract the length of 'pseudopseudohypoparathyroidism' "
        "and raise the result to the power of 3."
    )
    
    print(f"Query: {query}")
    
    inputs = {"messages": [("user", query)]}
    
    # stream values to see the state update after every step
    for step in agent_executor.stream(inputs, stream_mode="values"):
        message = step["messages"][-1]
        
        # thought (AI decides to call a tool)
        if hasattr(message, 'tool_calls') and message.tool_calls:
            for tc in message.tool_calls:
                print(f"Thought: Calling {tc['name']} with {tc['args']}...")
        
        # observation (tool returns data)
        elif message.type == "tool":
            print(f"Observation: {message.content}")
            
        # final Answer (AI speaks)
        elif message.type == "ai":
            print(f"AI: {message.content}")