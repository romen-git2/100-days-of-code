# **Day 39 - Retrieval Query (RAG Execution)**

**Phase 3 -** Agent Framework Foundations

## **📝 The Challenge**

**Goal -** Query the Vector Database created on Day 38 and use an LLM to generate a factual answer based solely on that retrieved context.

We built the Memory (Vector DB). Here, we build the Bridge (Retriever) and the Reasoning Engine (Generator). This implementation demonstrates how to prevent LLM hallucinations by grounding the AI's response in verified data.

## **🛠️ Tech Stack**

* **Python 3.10+**  
* **langchain** - Using the modern `create_retrieval_chain` LCEL constructors.  
* **faiss-cpu** - Our local vector engine.  
* **langchain-google-genai** - Utilizing Gemini 2.5 Flash.

## **📂 Solution Overview**

The script performs the following flow:

1. **Load Index** - Loads the FAISS vector store from disk.  
2. **Retrieve** - Converts the user query into a vector and finds the top 2 matching document chunks.  
3. **Stuffing** - Takes those chunks and stuffs them into the {context} variable of a system prompt.  
4. **Augmented Generation** - The LLM reads the context and the question together to produce a grounded response.

## **🏃‍♂️ How to Run**

1. Ensure the `faiss_index` folder exists in your current directory.  
2. Install the necessary packages:  

   ```bash
   pip install -r requirements.txt
   ```

3. Run the script:  

   ```bash
   python day39.py
   ```

## **🧠 Key Learnings & Reflections**

* **Hallucination Control** - By setting temperature=0 and using a strict system prompt, we force the LLM to admit ignorance ("I don't know") if the answer isn't in the provided chunks.  
* **Semantic Retrieval** - The agent successfully mapped the query "What kind of laptop..." to the chunk containing "MacBook Pro" without needing an exact keyword match.  

---
[Back to Main Repo](../README.md)
