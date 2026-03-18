import os
import numpy as np
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()
if not os.getenv("GOOGLE_API_KEY"):
    print("Error: GOOGLE_API_KEY not found.")
    exit(1)

def cosine_similarity(vec1: list[float], vec2: list[float]) -> float:
    """
    Calculates the cosine similarity between two vectors.
    Returns a value between -1 and 1. 
    1 means perfectly identical direction (semantic meaning).
    """
    a = np.array(vec1)
    b = np.array(vec2)
    
    dot_product = np.dot(a, b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    
    return dot_product / (norm_a * norm_b)

def main():
    # Initialize the Embedding Model
    print("Loading Embedding Model...")
    embeddings_model = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")

    # Define test sentences
    # Sentences A and B mean the same thing, but share almost no keywords
    # Sentence C is completely unrelated
    sentence_a = "I need to reset my password."
    sentence_b = "How do I recover my account credentials?"
    sentence_c = "The recipe calls for two cups of flour and three eggs."

    print("Sentences:")
    print(f"A: '{sentence_a}'")
    print(f"B: '{sentence_b}'")
    print(f"C: '{sentence_c}'")

    # Generate Embeddings (Convert Text to Math)
    print("Generating Embeddings (converting text to high-dimensional vectors)...")
    vec_a = embeddings_model.embed_query(sentence_a)
    vec_b = embeddings_model.embed_query(sentence_b)
    vec_c = embeddings_model.embed_query(sentence_c)

    print(f"Vector A's first 5 dimensions: {vec_a[:5]}")
    print(f"Total dimensions in this model: {len(vec_a)}")

    #Calculate Mathematical Similarity
    print("Calculating Cosine Similarity...")
    
    sim_a_b = cosine_similarity(vec_a, vec_b)
    sim_a_c = cosine_similarity(vec_a, vec_c)
    
    print(f"Similarity between A & B (Related):   {sim_a_b:.4f}")
    print(f"Similarity between A & C (Unrelated): {sim_a_c:.4f}")

if __name__ == "__main__":
    main()