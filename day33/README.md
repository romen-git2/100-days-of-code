# Day 33 - Prompt Templating (Variables)

**Phase 3 -** Agent Framework Foundations

## 📝 The Challenge

**Goal -** Create a reusable prompt template that accepts multiple user input variables and eliminates manual placeholders.

As agents become more complex, hard coding strings becomes impossible to manage. Today, I moved from Magic Strings to **Structured Templates** using LangChain's `ChatPromptTemplate`. This allows the agent to be dynamic, context aware and production-ready by injecting data (like the current date) programmatically.

## 🛠️ Tech Stack

* **Python 3.10+**
* **`langchain-core`** - Using `ChatPromptTemplate` for orchestration.
* **`langchain-google-genai`** - Powered by **Gemini 2.5 Flash** for high speed, intelligent text generation.
* **`python-dotenv`** - For secure API key management.

## 📂 Solution Overview

I built a **Context-Aware Email Generator** that accepts 6 dynamic variables. Crucially, I integrated Python's `datetime` module to ensure the AI never generates manual placeholders like `[Date]`.

### The Template Logic

We define a System role for persona and a User role for the task. The `{variables}` act as slots that are filled only at the moment of execution.

```python
# Variables used: recipient, date_today, reason, tone, length, sender_name
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert executive assistant..."),
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
python day33.py
```

### 5. **Sample Interaction**

```text
Generating Formal...

Subject: Software Engineer Application Status - Romen Ranasingha

Dear Hiring Manager,

I am writing to respectfully inquire about the status of my application for the Software Engineer position. I submitted my application previously and remain very interested in this opportunity.

Please let me know if there is any update you can share regarding the hiring process. Thank you for your time and consideration.

Sincerely,

Romen Ranasingha
```

## 🧠 Key Learnings

* **Instruction Adherence -** By using `from_messages` (System/User/Human), I learned how to provide the LLM with a clear North Star instruction that it follows more strictly than a single block of text.
* **Context Injection -** I realized that if you don't provide the data (like a date or a specific ID), the LLM will hallucinate a bracketed placeholder. The solution is to fetch that data programmatically in Python and pass it as a variable.
* **Scalability -** I can now use this one single Chain to handle thousands of different email scenarios just by changing the input dictionary. This is the foundation of building a scalable Agent Service.

---
[Back to Main Repo](../README.md)
