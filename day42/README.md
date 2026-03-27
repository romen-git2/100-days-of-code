# **Day 42 - Sequential Workflows & Cascading Failures**

**Phase 3 -** Agent Framework Foundations

## **📝 The Challenge**

**Goal -** Build a multi-step execution pipeline (Topic -> Title -> Outline -> Tweet) and solve the problem of Cascading Failures using strict prompt engineering.

Single prompts are great, but complex tasks require breaking problems down into smaller, sequential steps. Here, we built an "AI Assembly Line" using LangChain's LCEL. However, encountered a classic AI engineering problem: if step 1 is too chatty (e.g., returning 20 titles instead of 1), step 2 ingests all that garbage, completely ruining the downstream outputs.

## **🛠️ Tech Stack**

* **Python 3.10+**  
* **LangChain Core (`langchain_core.runnables`)** - Specifically leveraging RunnablePassthrough and LCEL pipe operators (|).  
* **Google Gemini (gemini-2.5-flash)** - The reasoning engine for all three steps.

## **📂 Solution Overview**

We created three distinct chains (`title_chain`, `outline_chain`, `tweet_chain`) and wired them together using RunnablePassthrough.assign(). This LCEL method acts like a conveyor belt, carrying a dictionary forward and appending the result of each step to it.

**The Fix -** We had to aggressively update our prompts. Instead of "Write a title," we must use Strict Prompting: *"Write exactly ONE title. Return ONLY the title. Do not include conversational filler."*

## **🏃‍♂️ How to Run**

1. Install dependencies:  

   ```bash
   pip install -r requirements.txt
   ```

2. Run the script:

   ```bash  
   python day42.py
   ```

## **🧠 Key Learnings & Reflections**

* **Cascading Failures -** In an AI pipeline, the output of Model A is the exact input of Model B. If Model A includes conversational filler ("Sure, here are some titles!"), Model B will treat that filler as part of the data.  
* **Strict Prompting is Mandatory for Chains -** When chaining LLMs, you must forbid them from being polite. Phrases like "Return ONLY the data" and "Do not include introductory text" are essential.  
* **The Magic of RunnablePassthrough.assign -** This allows step 3 to access data from step 1 (like the original topic or title) without having to manually carry variables over in Python.

---
[Back to Main Repo](../README.md)
