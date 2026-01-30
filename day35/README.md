# Day 35 - Custom Tools (Function Calling)

**Phase 3 -** Agent Framework Foundations

## 📝 The Challenge

**Goal -** Give the AI hands by teaching it to execute a specific Python function to solve a problem.

LLMs are brilliant at language but terrible at precise calculation and completely unable to access private data or logic. If you ask a standard model to calculate complex compound interest, it will likely hallucinate a plausible looking but incorrect number.

Today, I built a **Financial Calculator Agent**. Instead of guessing the answer, the AI recognizes it needs help, selects a custom Python tool (`calculate_compound_interest`), calculates the exact result and then uses that result to answer the user.

## 🛠️ Tech Stack

* **Python 3.10+**
* **`langchain-core`** - Using the `@tool` decorator and `ToolMessage`.
* **`langchain-google-genai`** - Powered by **Gemini 2.5 Flash** (Temperature 0.0).
* **`python-dotenv`** - API key management.

## 📂 Solution Overview

The agent loop consists of two passes:

1. **Thinking Phase -** The AI analyzes the user query. If it matches a tool's description, it returns a **Tool Call** (JSON) instead of text.
2. **Action Phase -** We (the code) execute the Python function using the arguments provided by the AI.
3. **Observation Phase -** We feed the function's result back to the AI as a `ToolMessage`.
4. **Response Phase -** The AI incorporates the real data into a natural language response.

### The Tool Definition

The **docstring** is critical. It acts as the instruction manual for the AI.

```python
@tool
def calculate_compound_interest(principal: float, rate: float, years: int) -> float:
    """
    Calculates the future value of an investment using compound interest.
    Formula: A = P(1 + r/100)^t

    Args:
        principal: The initial amount of money (e.g., 1000).
        rate: The annual interest rate in percent (e.g., 5 for 5%).
        years: The number of years the money is invested.
    """
    result = principal * ((1 + (rate / 100)) ** years)
    return round(result, 2)
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
python day35.py
```

### 5. **Sample Interaction**

```text
User: If I invest $5,000 at a 7% interest rate for 10 years, how much will I have?
AI decided to use a tool...
Calling calculate_compound_interest with {'rate': 7, 'principal': 5000, 'years': 10}
Result: 9835.76
AI Final Answer: You will have $9835.76.
```

(Note - The AI didn't do the math, Python did. The AI just orchestrated it.)

## 🧠 Key Learnings

* **Tools are Functions -** A tool in LangChain is just a Python function wrapped with `@tool`. The AI doesn't see the code, it only sees the function signature (inputs/outputs) and the docstring description.
* **The round trip -** I learned that the AI doesn't execute the tool itself. It pauses and says, "Please run this function for me". My code runs it and feeds the answer back. This back-and-forth is the core mechanic of all AI Agents.
* **Docstrings are Prompts -** The description inside the function (`"""..."""`) is actually part of the prompt. Writing clear, descriptive docstrings is essential for the AI to know when and how to use the tool.

---
[Back to Main Repo](../README.md)
