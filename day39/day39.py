import os
from dotenv import load_dotenv

# LangChain Components for RAG Execution
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_classic.chains import create_retrieval_chain

load_dotenv()
if not os.getenv("GOOGLE_API_KEY"):
    print("Error: GOOGLE_API_KEY not found.")
    exit(1)

def main():

    # Initialize the Models
    print("Initializing LLM and Embedding Model...")
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0) 
    embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")

    # Load the Vector Database
    print("Loading local FAISS database...")
    try:
        vector_db = FAISS.load_local(
            "faiss_index", 
            embeddings, 
            allow_dangerous_deserialization=True 
        )
    except Exception as e:
        print(f"Failed to load FAISS index: {e}")
        return

    # Create the Retriever
    # This turns the database into a tool that fetches the top 2 most relevant chunks
    retriever = vector_db.as_retriever(search_kwargs={"k": 2})

    # Define the RAG Prompt
    # Explicitly tell the AI to ONLY use the provided context.
    system_prompt = (
        "You are an assistant for question-answering tasks. "
        "Use the following pieces of retrieved context to answer the question. "
        "If you don't know the answer based on the context, say that you don't know. "
        "Keep the answer concise.\n\n"
        "Context: {context}"
    )
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{input}"),
    ])

    # Build the RAG Chain
    question_answer_chain = create_stuff_documents_chain(llm, prompt)
    
    # Links the retriever (to fetch docs) with the QA chain (to answer)
    rag_chain = create_retrieval_chain(retriever, question_answer_chain)

    # Execute the Query
    user_query = "What kind of laptop and stipend will I get?"
    print(f"Executing Query: '{user_query}'")
    
    # Invoke the chain
    response = rag_chain.invoke({"input": user_query})

    print("AI Answer:")
    print(response["answer"])

    print("Sources Retrieved:")
    for i, doc in enumerate(response["context"]):
        print(f"Chunk {i+1}: {doc.page_content.strip()}")

if __name__ == "__main__":
    main()