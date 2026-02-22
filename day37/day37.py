import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

load_dotenv()
if not os.getenv("GOOGLE_API_KEY"):
    print("Error: GOOGLE_API_KEY not found.")
    exit(1)

# Initialize Model
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)

# Prompt with History Slot
# Reserve a placeholder for the conversation history to be injected
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a friendly AI companion. You remember details about the user."),
    MessagesPlaceholder(variable_name="chat_history"), # Memory Slot
    ("user", "{input}")
])

# Core Chain
# This is a standard LCEL chain (Prompt -> Model -> String Parser)
chain = prompt | model | StrOutputParser()

# Memory Management
# In production - Redis/Postgres 
# For learning - Python dictionary.
store = {}

def get_session_history(session_id: str):
    """Returns the history object for a specific session ID."""
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]

# Stateful Wrapper
# This wraps the chain and handles reading/writing history automatically
chain_with_history = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="chat_history"
)

if __name__ == "__main__":
    
    # Define a session ID. This allows to have multiple separate users.
    session_id = "user_123"
    config = {"configurable": {"session_id": session_id}}

    print(f"[Session ID: {session_id}]")

    # Introduction
    user_input_1 = "Hi! My name is Romen and I am a software engineer."
    print(f"User: {user_input_1}")
    response1 = chain_with_history.invoke({"input": user_input_1}, config=config)
    print(f"AI: {response1}")

    # Distraction
    # Ask a random question to flush the immediate context.
    user_input_2 = "What is 25 * 4?"
    print(f"User: {user_input_2}")
    response2 = chain_with_history.invoke({"input": user_input_2}, config=config)
    print(f"AI: {response2}")

    # Memory Test
    # Ask the AI to recall information
    user_input_3 = "Do you remember my name and profession?"
    print(f"User: {user_input_3}")
    response3 = chain_with_history.invoke({"input": user_input_3}, config=config)
    print(f"AI: {response3}")