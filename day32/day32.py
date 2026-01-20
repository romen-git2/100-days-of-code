from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# using gemini-2.5-flash model for performance and reliability
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash", 
    temperature=0.7
)
parser = StrOutputParser()

# expert chain
# focuses on technical accuracy
prompt_expert = ChatPromptTemplate.from_template(
    "You are a technical expert. Provide a detailed 2-sentence explanation of: {topic}"
)
chain_expert = prompt_expert | model | parser

# communicator chain
# focuses on simplification
prompt_simplify = ChatPromptTemplate.from_template(
    "Rewrite this technical explanation so a beginner can understand it in one sentence:\n\n{tech_info}"
)
chain_simplify = prompt_simplify | model | parser

# map the output of the first chain to the input variable "tech_info"
full_chain = (
    {"tech_info": chain_expert} 
    | chain_simplify
)

if __name__ == "__main__":
    topic = input("Enter a topic: ")
    
    print(f"Consulting the expert...")
    print(f"Simplifying the response...")
    
    try:
        # running the full pipeline
        final_answer = full_chain.invoke({"topic": topic})
        print(f"Summary: {final_answer}")
    except Exception as e:
        print(f"Error: {e}")