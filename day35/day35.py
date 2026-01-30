from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, ToolMessage

load_dotenv()
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.0)

@tool
def calculate_compound_interest(principal: float, rate: float, years: int) -> float:
    """
    Calculates the future value of an investment using compound interest.
    Formula: A = P(1 + r/100)^t

    Args:
        principal: The initial amount of money (e.g., 1000).
        rate: The annual interest rate in percent (e.g., 5 for 5%).
        years: The number of years the money is invested.
    """
    result = principal * ((1 + (rate / 100)) ** years)
    return round(result, 2)

@tool
def heavy_multiplication(a: int, b: int) -> int:
    """Useful for multiplying two integers."""
    return a * b

# bind tools
# give the AI a toolbox with multiple options
tools = [calculate_compound_interest, heavy_multiplication]
tools_map = {t.name: t for t in tools}

llm_with_tools = llm.bind_tools(tools)

def run_agent_turn(user_query):
    print(f"User: {user_query}")
    messages = [HumanMessage(content=user_query)]

    # first pass - AI thinks
    ai_msg = llm_with_tools.invoke(messages)
    messages.append(ai_msg)

    if ai_msg.tool_calls:
        print("AI decided to use a tool...")

        for tool_call in ai_msg.tool_calls:
            tool_name = tool_call["name"]
            tool_args = tool_call["args"]
            tool_id = tool_call["id"]

            print(f"Calling {tool_name} with {tool_args}")

            # execute
            selected_tool = tools_map[tool_name]
            tool_result = selected_tool.invoke(tool_args)
            print(f"Result: {tool_result}")

            messages.append(ToolMessage(
                content=str(tool_result),
                tool_call_id=tool_id
            ))

        # second pass - AI answers
        final_response = llm_with_tools.invoke(messages)
        print(f"AI Final Answer: {final_response.content}")
    else:
        print(f"AI Answer: {ai_msg.content}")

if __name__ == "__main__":
    # query that requires the specific financial formula
    run_agent_turn(
        "If I invest $5,000 at a 7% interest rate for 10 years, how much will I have?")
