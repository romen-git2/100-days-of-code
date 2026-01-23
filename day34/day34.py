from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, Field
from typing import List

load_dotenv()

# low temp helps structure
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.0)

# schema
# use pydantic to tell the AI exactly what fields need
class ProductSchema(BaseModel):
    name: str = Field(description="The marketing name of the product")
    price_usd: float = Field(description="Price in USD (number only)")
    colors: List[str] = Field(description="List of available color options")
    is_available: bool = Field(description="True if the product is in stock")
    summary: str = Field(description="A short 5-word summary")

# parser
# this tool automatically generates the instruction - "Output must be valid JSON..."
parser = JsonOutputParser(pydantic_object=ProductSchema)

# prompt
# {format_instructions} is where LangChain injects the JSON schema.
prompt = PromptTemplate(
    template="""
    You are a data extraction bot. Extract product details from the text below.
    
    User Text: {text}
    
    {format_instructions}
    """,
    input_variables=["text"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

# chain
chain = prompt | model | parser

if __name__ == "__main__":
    
    # messy input text representing real-world user data
    raw_input = """
    I just saw the new Lego Smart Play Star Wars set! It's the talk of CES 2026. 
    The starter kit is $89.99 and features the new Smart Bricks that light up. 
    It comes in Classic Gray, Starship Silver and Rebel Orange. 
    It's currently available for pre-order, so yes, it's in stock for now! 
    The ultimate interactive building experience.
    """
    
    print(f"Raw Input: {raw_input}")
    print("Parsing...")
    
    try:
        # result will be a pure python dictionary
        result = chain.invoke({"text": raw_input})
        
        print(f"Extracted Data (Type: {type(result)}):")
        print(f"Name:   {result['name']}")
        print(f"Price:  ${result['price_usd']}")
        print(f"Colors: {result['colors']}")
        print(f"Stock:  {'In Stock' if result['is_available'] else 'Out of Stock'}")
        
    except Exception as e:
        print(f"Error: {e}")