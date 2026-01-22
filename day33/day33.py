from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import datetime

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)
parser = StrOutputParser()

# define the template
# build a structured message
# use {variables} that will be filled in later
email_template = ChatPromptTemplate.from_messages([
    ("system", (
        "You are an expert executive assistant. Write concise, professional emails. "
        "CRITICAL: Do not use placeholders like '[Date]', '[Name]' or '[Recipient]'. "
        "Use ONLY the specific information provided in the variables. "
        "If a piece of information is missing, infer it from the context or leave it out entirely "
        "rather than using a bracketed placeholder."
    )),
    ("user", """
    Today's Date: {date_today}
    Recipient: {recipient}
    Sender: {sender_name}
    Tone: {tone}
    Max Length: {length} words
    
    Context/Reason: {reason}
    
    Write the email now.
    """)
])


# chain
# define the pipe
chain = email_template | model | parser

if __name__ == "__main__":
    
    formatted_date = datetime.date.today().strftime("%B %d, %Y")
    
    # formal request
    print("Generating Formal...")
    response_a = chain.invoke({
        "recipient": "Hiring Manager",
        "reason": "Asking for an update on my application for the Software Engineer role.",
        "tone": "Formal and polite",
        "length": "100",
        "sender_name": "Romen Ranasingha",
        "date_today": formatted_date
    })
    print(f"\n{response_a}")

    # casual check-in
    print("\nGenerating Casual...")
    response_b = chain.invoke({
        "recipient": "Sarah (Project Lead)",
        "reason": "Running late to the standup meeting due to traffic.",
        "tone": "Casual and apologetic",
        "length": "30",
        "sender_name": "Romen Ranasingha",
        "date_today": formatted_date
    })
    print(f"\n{response_b}")