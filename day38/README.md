# **Day 38 - RAG Setup (Document Indexing)**

**Phase 3 -** Agent Framework Foundations

## **📝 The Challenge**

**Goal -** Convert a raw text file into a searchable format that an AI Agent can use.

Up until now, our agents have relied purely on their training weights and short-term memory (chat history). Today, we implement **Retrieval-Augmented Generation (RAG)**.

To give our AI a Long-Term Knowledge Base, we cannot simply paste a 100 page PDF into the prompt (it's too expensive and exceeds the context window limits). Instead, we must perform **Document Indexing** - loading the text, splitting it into small chunks, converting those chunks into numbers (embeddings) and saving them into a Vector Database.

## **🛠️ Tech Stack**

* **Python 3.10+**  
* **langchain / langchain_community** - Used for TextLoader and RecursiveCharacterTextSplitter.  
* **faiss-cpu** - Facebook AI Similarity Search (Our local vector database).  
* **langchain-google-genai** - Powered by **Google's gemini-embedding-001** model to convert text to vectors.

## **📂 Solution Overview**

The architecture is a classic ETL (Extract, Transform, Load) pipeline for RAG:

1. **Extract -** TextLoader reads a local .txt file into LangChain Document objects.  
2. **Transform -** RecursiveCharacterTextSplitter breaks the large document into smaller 150 character chunks with a 20 character overlap (to preserve context across chunk boundaries).  
3. **Embed -** The GoogleGenerativeAIEmbeddings model converts the human text into high dimensional mathematical vectors.  
4. **Load -** FAISS.from_documents loads these vectors into a local database and saves them to disk (faiss_index) for future retrieval.

## **🏃‍♂️ How to Run**

1. **Install Dependencies**:

   ```text
   pip install -r requirements.txt
   ```

2. **Add API Key** - Ensure GOOGLE_API_KEY is present in your .env file.  
3. **Run the script**:  

   ```text
   python day38.py
   ```

## **🧠 Key Learnings & Reflections**

* **Embeddings vs. Keywords -** LLMs don't search for exact keywords like standard SQL databases. They convert text into mathematical arrays (vectors) where semantically similar concepts (e.g., "vacation" and "time off") are mathematically close to each other.  
* **Chunking Strategy -** You can't embed an entire book at once. The RecursiveCharacterTextSplitter is critical because it breaks text down while trying to keep paragraphs and sentences intact, preventing the AI from getting cut-off context.  
* **Vector Stores (FAISS) -** Instead of storing strings in tables, vector databases store arrays of floats. By saving the index locally (save_local), we avoid paying the API cost to re-embed the same document every time the agent runs.

---
[Back to Main Repo](../README.md)
