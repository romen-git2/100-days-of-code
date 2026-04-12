import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

if not os.getenv("GOOGLE_API_KEY"):
    print("Error: GOOGLE_API_KEY not found in .env")
    exit(1)
if not os.getenv("LANGCHAIN_API_KEY"):
    print("Error: LANGCHAIN_API_KEY not found in .env")
    print("Get one at: https://smith.langchain.com")
    exit(1)

# Enable LangSmith Tracing
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "Day44"

def main():
    print("Tracing is enabled. Executing pipeline...")

    # Initialize the LLM
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)
    parser = StrOutputParser()

    # Joke Generator
    prompt_joke = ChatPromptTemplate.from_template("Tell me a short, clever joke about {topic}.")
    joke_chain = prompt_joke | llm | parser

    # Joke Explainer (Over-analyzer)
    prompt_explain = ChatPromptTemplate.from_template(
        "Analyze this joke and explain exactly why it is funny in a highly academic, serious tone:\n\n{joke}"
    )
    explain_chain = prompt_explain | llm | parser

    # Combine into a Sequential Chain using LCEL
    full_chain = {"joke": joke_chain} | explain_chain

    # Execute the Chain
    topic = "Software Engineers"
    print(f"Topic: {topic}")
    
    # When this runs, LangSmith records the exact inputs, outputs, tokens and latency behind the scenes
    result = full_chain.invoke({"topic": topic})
    
    print("Final Academic Explanation:")
    print(result)
    
    print("Execution Complete")
    print("Go to https://smith.langchain.com to view the exact trace of both LLM calls.")
    
if __name__ == "__main__":
    main()