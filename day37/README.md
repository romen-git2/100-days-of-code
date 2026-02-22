# **Day 37 - Conversation Memory (Buffer)**

**Phase 3 -** Agent Framework Foundations

## **📝 The Challenge**

**Goal -** Build a chatbot that maintains context across a multi-turn conversation.

LLMs are inherently **stateless**, they treat every query as the first one they've ever seen. If you tell an LLM your name and then ask a follow-up question, a standard LLM call will fail because it doesn't remember the previous interaction.

Today, I implemented **Buffer Memory** using LangChain's modern RunnableWithMessageHistory. This allows the agent to store the conversation history and reference it in future responses, effectively giving the AI short-term memory.

## **🛠️ Tech Stack**

* **Python 3.10+**  
* **langchain_core** - Utilizing RunnableWithMessageHistory and InMemoryChatMessageHistory for state management.  
* **langchain-google-genai** - Powered by **Gemini 2.5 Flash** (Temperature 0.7 for conversational responses).

## **📂 Solution Overview**

The architecture involves wrapping a standard LCEL (LangChain Expression Language) Chain with a History Manager.

1. **The Prompt -** Includes a MessagesPlaceholder variable to act as a slot where previous messages will be injected.  
2. **The Storage -** An in-memory dictionary that maps unique session_ids to their respective chat logs.  
3. **The Wrapper -** RunnableWithMessageHistory automatically intercepts the user's input, fetches the past messages, injects them into the prompt, runs the model and then saves the new AI response back to the storage.

```python
# The Key Component - Wraps the chain to manage state automatically  
chain_with_history = RunnableWithMessageHistory(  
    chain,  
    get_session_history,  # Function to retrieve history dict  
    input_messages_key="input",  
    history_messages_key="chat_history" # Matches the placeholder in the prompt  
)
```

## **🏃‍♂️ How to Run**

1. **Install Dependencies**:

   ```text
   pip install -r requirements.txt
   ```

2. **Add API Key**: Ensure GOOGLE_API_KEY is present in your .env file.  
3. **Run**:

   ```text
   python day37.py
   ```

## **🧠 Key Learnings & Reflections**

* **Memory is Just Context Injection -** AI memory isn't the model actually remembering things, it's simply appending the chat transcript to every new prompt. This means longer conversations cost more tokens.  
* **Session Management -** Using a session_id allows a single backend application to handle thousands of unique users simultaneously without mixing up their conversation histories.  

---
[Back to Main Repo](../README.md)