# **Day 44 - Chain Tracing with LangSmith**

**Phase 3 -** Agent Framework Foundations

## **📝 The Challenge**

**Goal -** Implement observability into an LLM pipeline to solve the Black Box debugging problem.

When building multi-step LLM workflows, if the final output is wrong, it's incredibly difficult to determine *which* step failed just by looking at the terminal. Here, we integrated **LangSmith** to trace a 2-step LCEL chain (Generate a Joke -> Academically Explain the Joke).

## **🛠️ Tech Stack**

* **Python 3.10+**  
* **LangChain Core (langchain_core)** - LCEL pipelines.  
* **LangSmith** - LangChain's observability and evaluation platform.  
* **Google Gemini (gemini-2.5-flash)** - The reasoning engine.

## **📂 Solution Overview**

LangSmith instrumentation requires almost zero code changes. It relies entirely on environment variables:

1. `LANGCHAIN_TRACING_V2="true"` - Flips the global switch to start recording.  
2. `LANGCHAIN_API_KEY` - Authenticates with the LangSmith cloud.  
3. `LANGCHAIN_PROJECT` - Organizes traces into a specific project dashboard.

By running the script, the exact inputs, outputs, system prompts, token consumption and latency for both the Joke LLM call and the Explanation LLM call are visually mapped out in the LangSmith UI.

## **🏃‍♂️ How to Run**

1. Go to [smith.langchain.com](https://smith.langchain.com/) and create a free account.  
2. Generate an API Key and add it to your .env file:  
   `LANGCHAIN_API_KEY="your_api_key_here"`

3. Run the script:  

   ```bash
   python day44.py
   ```

4. Log back into LangSmith and view the `Day44` project to see the visual trace!

## **🧠 Key Learnings & Reflections**

* **Observability is Mandatory -** "Print statement debugging" does not scale for AI agents. Seeing the visual flow of data in LangSmith makes debugging complex LCEL architectures trivial.  
* **Zero-Code Instrumentation -** How elegant LangChain's design is, didn't have to rewrite chains to trace them. The environment variables hook directly into LangChain's core execution engine automatically.  
* **Cost & Latency Tracking -** Tracing isn't just for errors. LangSmith exposes exactly how many tokens were used per step and how long the API took to respond, which is critical for production optimization.

---
[Back to Main Repo](../README.md)
