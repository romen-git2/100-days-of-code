# Day 34 - Output Parsing (JSON & Pydantic)

**Phase 3 -** Agent Framework Foundations

## 📝 The Challenge

**Goal -** Force the LLM to return structured JSON data instead of conversational text.

In software engineering, LLMs speak in strings, but our applications speak in **Objects**. To make an agent truly useful for a database or a UI, we must ensure its output is predictable and machine readable. Today, I implemented a **Product Info Extractor** that transforms messy, unstructured marketing copy into a strict Python dictionary using **Pydantic** and **LangChain’s `JsonOutputParser`**.

## 🛠️ Tech Stack

* **Python 3.10+**
* **`pydantic`** - For defining the data contract (schema) and validation.
* **`langchain-core`** - Utilizing `JsonOutputParser` and `PromptTemplate`.
* **`langchain-google-genai`** - Powered by **Gemini 2.5 Flash** (Temperature 0.0 for deterministic results).
* **`python-dotenv`** - For API key management.

## 📂 Solution Overview

The workflow follows a 3-step synchronization:

1. **Define the Schema -** Using Pydantic to specify fields (e.g., `price` must be a float, `colors` must be a list).
2. **Inject Instructions -** The parser automatically generates the complex prompt needed to tell the AI *how* to format the JSON.
3. **Automatic Type Casting -** The chain converts the AI's string response into a real Python dictionary.

### The Parsing Logic

```python
# The parser uses the Pydantic class to create instructions
parser = JsonOutputParser(pydantic_object=ProductSchema)

prompt = PromptTemplate(
    template="Extract details from: {text}\n{format_instructions}",
    input_variables=["text"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)
```

## 🏃‍♂️ How to Run

### 1. Get a Google API Key

* Visit [Google AI Studio](https://aistudio.google.com/) and create a API key.

### 2. Configure Environment

Create a `.env` file:

```text
GOOGLE_API_KEY=google_api_key
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. **Execute**

```bash
python day34.py
```

### 5. **Sample Transformation**

```text
Raw Input: 
    I just saw the new Lego Smart Play Star Wars set! It's the talk of CES 2026.
    The starter kit is $89.99 and features the new Smart Bricks that light up.
    It comes in Classic Gray, Starship Silver and Rebel Orange.
    It's currently available for pre-order, so yes, it's in stock for now!
    The ultimate interactive building experience.

Parsing...
Extracted Data (Type: <class 'dict'>):
Name:   Lego Smart Play Star Wars set
Price:  $89.99
Colors: ['Classic Gray', 'Starship Silver', 'Rebel Orange']
Stock:  In Stock
```

## 🧠 Key Learnings

* **Schema-First Design -** I learned that defining a Pydantic model acts as a Contract. If the AI fails to meet this contract, the parser will raise an error, preventing corrupt data from entering the database.
* **Deterministic Configuration -** By setting `temperature=0.0`, I minimized the creative tendencies of the model, ensuring it focuses strictly on extraction logic rather than conversational filler.
* **The Bridge to Integration -** This is the most critical step for AI agents. With structured output, the agent is no longer just a chatbot, it is now a functional backend service capable of driving real-world software logic.

---
[Back to Main Repo](../README.md)
