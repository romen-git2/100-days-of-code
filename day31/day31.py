import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

if not os.getenv("GOOGLE_API_KEY"):
    print("Error: GOOGLE_API_KEY not found in .env file")
    exit(1)

# model(Gemini Wrapper)
model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.7
)

# prompt(template)
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a tech consultant. Answer concisely."),
    ("user", "Explain what {topic} is in one sentence.")
])

# output parser
parser = StrOutputParser()

# chain(LCEL)
# Input -> Prompt -> Gemini -> Parser -> Output
chain = prompt | model | parser

if __name__ == "__main__":
    
    topic = input("Enter a tech topic: ")
    
    print(f"Asking Gemini about {topic}...")
    
    try:
        response = chain.invoke({"topic": topic})
        print(f"Answer: {response}")
    except Exception as e:
        print(f"Error: {e}")