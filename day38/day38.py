import os
from dotenv import load_dotenv

# LangChain components for RAG Indexing
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS

load_dotenv()
if not os.getenv("GOOGLE_API_KEY"):
    print("Error: GOOGLE_API_KEY not found.")
    exit(1)

# Create a Dummy Knowledge Base
kb_filename = "company_policy.txt"
kb_content = """
Welcome to NexusCorp! Here are our core policies:
1. Remote Work: Employees can work remotely up to 3 days a week. Tuesdays and Thursdays are mandatory in-office days.
2. Vacation Policy: All full-time employees receive 20 days of paid time off (PTO) per year, rolling over a maximum of 5 days to the next year.
3. Equipment: The company provides a MacBook Pro, a $500 home office stipend and covers monthly internet bills up to $50.
4. Security: Never share your VPN credentials. Passwords must be rotated every 90 days.
"""

with open(kb_filename, "w") as f:
    f.write(kb_content)
print(f"Created knowledge base file: {kb_filename}")


def main():

    # Load the Document
    print("Loading document...")
    loader = TextLoader(kb_filename)
    documents = loader.load()
    print(f"Loaded {len(documents)} document(s).")

    # Split into Chunks
    print("Splitting text into chunks...")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=150,  # Size of each piece (small for demo)
        chunk_overlap=20  # Overlap to maintain context between chunks
    )
    chunks = text_splitter.split_documents(documents)
    print(f"Split into {len(chunks)} chunks.")

    print(f"First chunk: '{chunks[0].page_content}'")

    # Generate Embeddings
    print("Generating Embeddings...")
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/gemini-embedding-001")

    # Store in Vector Database
    print("Indexing into Vector Store (FAISS)...")
    vector_db = FAISS.from_documents(chunks, embeddings)

    vector_db.save_local("faiss_index")
    print("Vector Store saved locally to 'faiss_index' folder.")

    print("Testing similarity search (Retrieval)...")
    query = "How much time off do I get?"
    print(f"Query: '{query}'")

    # Find the chunk with the highest mathematical similarity to the question
    docs = vector_db.similarity_search(query, k=1)
    print(f"Retrieval Result: '{docs[0].page_content}'")


if __name__ == "__main__":
    main()
