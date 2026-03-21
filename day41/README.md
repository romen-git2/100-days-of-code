# **Day 41 - Prompt Tuning (Few-Shot Prompting)**

**Phase 3 -** Agent Framework Foundations

## **📝 The Challenge**

**Goal -** Force an LLM to output a highly specific format and tone without relying solely on long, complex system instructions.

When building AI Agents, you often need the output to follow a strict pattern (e.g., returning data in a specific shape or writing in a distinct voice). **Zero-Shot prompting** (just giving instructions) is often fragile. Here, we implement **Few-Shot Prompting** - providing the LLM with 2-3 examples of the desired input/output pairs to teach it the pattern.

## **🛠️ Tech Stack**

* **Python 3.10+**  
* **LangChain Core (`langchain_core.prompts`)** - Utilizing FewShotChatMessagePromptTemplate and ChatPromptTemplate.  
* **Google Gemini (gemini-2.5-flash)** - The LLM engine.

## **📂 Solution Overview**

We built a Tech-to-Layman Translator that uses analogies.

1. **The Examples -** We created a list of dictionaries containing input (a tech term) and output (the analogy).  
2. **The Example Prompt -** We mapped these dictionaries to a conversational flow (Human asks, AI answers).  
3. **The Few-Shot Template -** LangChain dynamically injects these examples into the prompt as a simulated chat history.  
4. **The Final Chain -** The LLM reads the system instructions, reviews the simulated history (our examples) to learn the pattern and then processes the actual user input.

## **🏃‍♂️ How to Run**

1. Install dependencies:  

   ```bash
   pip install -r requiremnets.txt
   ```

2. Ensure your .env file has your `GOOGLE_API_KEY`.  
3. Run the script:  

   ```bash
   python day41.py
   ```

## **🧠 Key Learnings & Reflections**

* **"Show, Don't Tell" -** Instead of writing a paragraph in the system prompt begging the AI to format things a certain way, giving it just 3 examples is vastly more effective and uses fewer tokens.  
* **In-Context Learning -** By simulating a chat history where the AI *already answered* correctly 3 times, it naturally continues the pattern for the 4th turn. This is the core mechanism of few-shot prompting in modern chat models.  
* **LangChain's Abstractions -** The FewShotChatMessagePromptTemplate makes it incredibly clean to manage these examples in code rather than dealing with messy string concatenations.

---
[Back to Main Repo](../README.md)
