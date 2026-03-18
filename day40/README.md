# **Day 40 - Embeddings & Cosine Similarity**

**Phase 3 -** Agent Framework Foundations

## **📝 The Challenge**

**Goal -** Demystify how AI understands language by manually generating text embeddings and calculating their mathematical similarity.

In previous days, we used FAISS as a black box to find relevant documents. Now, we look at the exact math that makes RAG possible. We will use Google's embedding model to convert text into arrays of floats (vectors) and use NumPy to calculate the **Cosine Similarity** between them.

This proves that AI doesn't search for matching *keywords*, it calculates geometric *distance*.

## **🛠️ Tech Stack**

* **Python 3.10+**  
* **langchain-google-genai** - To access the gemini-embedding-001 model.  
* **numpy** - For calculating dot products and vector norms (Cosine Similarity).

## **📂 Solution Overview**

1. **The Sentences -** We define three sentences. Two are semantically identical but use entirely different words (e.g., "reset password" vs "recover credentials"). The third is completely unrelated.  
2. **Embedding -** We pass these strings to `embed_query()`. The API returns an incredibly dense list of **3072 floats** for each sentence.  
3. **The Math -** We use NumPy to calculate the Cosine Similarity formula: (A · B) / (||A|| * ||B||).  
4. **The Result -** The script outputs a score of 0.7173 for the related sentences and drops to 0.5132 for the unrelated sentence, visually demonstrating how semantic search works.

## **🏃‍♂️ How to Run**

1. Install dependencies:

   ```bash  
   pip install -r requirements.txt
   ```

2. Ensure .env file has `GOOGLE_API_KEY`.  
3. Run the script:

   ```bash
   python day40.py
   ```

## **🧠 Key Learnings & Reflections**

* **What is an Embedding?** It's a high-dimensional coordinate. Just like `[lat, long]` plots a city on a 2D map, an embedding (like `[0.036, 0.010, ...]`) plots a concept in a 3072-dimensional space.  
* **Semantic over Lexical -** "Reset my password" and "Recover account credentials" have almost no lexical overlap (keywords), yet their Cosine Similarity score is significantly higher. This is why Vector Databases are vastly superior to SQL LIKE '%keyword%' queries for AI.  
* **Cosine Similarity -** By dividing the dot product of two vectors by the product of their magnitudes, we calculate the angle between them. A smaller angle means the concepts mean the same thing mathematically.

---
[Back to Main Repo](../README.md)
