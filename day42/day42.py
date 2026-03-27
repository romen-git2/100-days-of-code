import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

load_dotenv()
if not os.getenv("GOOGLE_API_KEY"):
    print("Error: GOOGLE_API_KEY not found.")
    exit(1)

def main():

    # Initialize the LLM
    print("Initializing LLM...")
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)
    parser = StrOutputParser()

    # Step 1: Title Generator
    prompt1 = ChatPromptTemplate.from_template(
        "Generate exactly ONE catchy, click-worthy blog post title about {topic}. "
        "Return ONLY the title. Do not include any quotes, numbers, or conversational text like 'Here is a title'."
    )
    title_chain = prompt1 | llm | parser

    # Step 2: Outline Generator
    prompt2 = ChatPromptTemplate.from_template(
        "Write a brief, 3-point outline for a blog post titled: '{title}'. "
        "Return ONLY the outline. Do not include introductory or concluding remarks."
    )
    outline_chain = prompt2 | llm | parser

    # Step 3: Tweet Generator
    prompt3 = ChatPromptTemplate.from_template(
        "Write exactly ONE short, engaging tweet promoting a blog post with this outline:\n{outline}\n\n"
        "Include engaging emojis and hashtags. Return ONLY the tweet itself. Do not give me multiple options."
    )
    tweet_chain = prompt3 | llm | parser

    # Build the Sequential Workflow
    # RunnablePassthrough.assign() - add new keys to dictionary 
    # while keeping the old ones intact for the next steps
    print("Assembling the Pipeline...")
    
    overall_workflow = (
        {"topic": RunnablePassthrough()} 
        | RunnablePassthrough.assign(title=title_chain)
        | RunnablePassthrough.assign(outline=outline_chain)
        | RunnablePassthrough.assign(tweet=tweet_chain)
    )

    # Execute the Workflow
    topic = "The future of AI in software engineering"
    print(f"Executing Workflow for topic: '{topic}'...")
    
    result = overall_workflow.invoke(topic)

    print(f"Generated Title: {result['title']}")
    print(f"Generated Outline: {result['outline']}")
    print(f"Generated Tweet: {result['tweet']}")

if __name__ == "__main__":
    main()