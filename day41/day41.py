import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import (
    ChatPromptTemplate,
    FewShotChatMessagePromptTemplate,
)
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
if not os.getenv("GOOGLE_API_KEY"):
    print("Error: GOOGLE_API_KEY not found.")
    exit(1)


def main():

    # 1. Initialize the LLM
    print("Initializing LLM...")
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)

    # Define Examples
    examples = [
        {
            "input": "API",
            "output": """Think of an API as a waiter in a restaurant. You (the app) tell the waiter your order, they take it to the kitchen 
            (the server) and bring your food (the data) back to you."""
        },
        {
            "input": "Firewall",
            "output": """Think of a firewall as a bouncer at a nightclub. It checks the IDs of everyone trying to get in (network traffic) and 
            blocks anyone who isn't on the guest list (malicious data)."""
        },
        {
            "input": "Cache",
            "output": """Think of a cache as your pockets. Instead of walking all the way to your closet (main memory) every time you need your 
            keys, you keep them in your pocket (cache) for instant access."""
        }
    ]

    # Create the Example Template
    # This defines how each example is formatted as a mock chat history
    example_prompt = ChatPromptTemplate.from_messages([
        ("human", "{input}"),
        ("ai", "{output}"),
    ])

    # 4. Create the Few-Shot Prompt Template
    print("Assembling Few-Shot Prompt Template...")
    few_shot_prompt = FewShotChatMessagePromptTemplate(
        example_prompt=example_prompt,
        examples=examples,
    )

    # Assemble the Final Prompt
    # Combine a System Message, Few-Shot Examples and the actual User Input
    final_prompt = ChatPromptTemplate.from_messages([
        ("system", """You are an expert technical communicator. Explain IT concepts to beginners using everyday analogies. Follow the exact format 
         shown in the examples."""),
        few_shot_prompt,
        ("human", "{input}"),
    ])

    # Build the LCEL Chain
    chain = final_prompt | llm | StrOutputParser()

    # Test the Chain with a novel concept
    test_concepts = ["Load Balancer", "Vector Database"]

    print("Executing Chain with new concepts...")
    for concept in test_concepts:
        print(f"Concept: {concept}")

        response = chain.invoke({"input": concept})

        print(f"Output: {response}")


if __name__ == "__main__":
    main()
