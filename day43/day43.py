from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, BaseMessage

load_dotenv()
model_name = "gemini-2.5-flash"
llm = ChatGoogleGenerativeAI(model=model_name, temperature=0)

# Tool
@tool
def get_discount_code(product_name: str) -> str:
    """Fetches the current active discount code for a specific product."""
    db = {
        "wireless_headphones": "AUDIO20",
        "smart_watch": "TIME10",
        "gaming_laptop": "GAMER15",
        "mechanical_keyboard": "CLICKY5"
    }
    key = product_name.lower().replace(" ", "_")
    return f"Code: {db.get(key, 'NO_DISCOUNT')}"

def clean_output(message: BaseMessage) -> str:
    """Extracts clean text from complex message structure."""
    if isinstance(message.content, str): return message.content
    if isinstance(message.content, list):
        return " ".join([p['text'] for p in message.content if 'text' in p])
    return str(message.content)

# Zero-Shot (No Tools)
# Use create_agent with no tools. It behaves like a standard chain.
zero_shot_agent = create_agent(model=llm, tools=[])

# Tool Using Agent
# The agent now has access to the discount database tool.
tool_agent = create_agent(model=llm, tools=[get_discount_code])

# Memory Agent (Stateful)
# Agent handles message history in state automatically.
memory_agent = create_agent(
    model=llm, 
    tools=[get_discount_code],
    system_prompt="You are a helpful assistant. Remember the user's name and their interests."
)

def main():
    product = "Gaming Laptop"

    # Zero-Shot
    print("ZERO-SHOT")
    res1 = zero_shot_agent.invoke({"messages": [HumanMessage(content=f"What is the discount code for {product}?")]})
    print(f"AI: {clean_output(res1['messages'][-1])}")
    print("Analysis: It either hallucinates or says it doesn't know.")

    # Tool-Using
    print("TOOL USING (Connecting to DB)")
    res2 = tool_agent.invoke({"messages": [HumanMessage(content=f"Use your tool to find the code for {product}")]})
    print(f"AI: {clean_output(res2['messages'][-1])}")
    print("Analysis: It calls the Python tool and gets 'GAMER15' accurately.")

    # Memory Agent
    print("MEMORY AGENT (Multi-turn Context)")
    # Give it context
    print("User: Hi, I'm Romen. I really want that Gaming Laptop.")
    turn1 = memory_agent.invoke({"messages": [HumanMessage(content="Hi, I'm Romen. I really want that Gaming Laptop.")]})
    
    # Test if it remembers the name and the product
    # Pass the history back in
    print("User: What was the discount code for the item I mentioned earlier?")
    history = turn1["messages"] + [HumanMessage(content="What was the discount code for the item I mentioned earlier?")]
    turn2 = memory_agent.invoke({"messages": history})
    
    print(f"AI: {clean_output(turn2['messages'][-1])}")
    print("Analysis: Success! It remembered 'Romen' and 'Gaming Laptop' to call the tool.")

if __name__ == "__main__":
    main()