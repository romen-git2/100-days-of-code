# Day 31 - Introduction to LangChain (LLM Wrappers)

**Phase 3 -** Agent Framework Foundations

## 📝 The Challenge

**Goal -** Build a basic Chain using **LangChain** and **Google Gemini** to abstract away raw API calls.

For the first 30 days, we manually handled HTTP requests, JSON parsing and API errors. While educational, this doesn't scale. Today, we switch to **LangChain**, a framework that treats AI components (Models, Prompts, Parsers) as modular Legos that can be piped together.

We implemented a **Tech Consultant** that demonstrates the **LCEL (LangChain Expression Language)** syntax - `Prompt | Model | Parser`.

## 🛠️ Tech Stack

* **Python 3.10+**
* **`langchain` -** The orchestration framework.
* **`langchain-google-genai` -** The integration package for Google's Gemini models.
* **`python-dotenv` -** For managing API keys securely.
* **Google Gemini -** The LLM backend.

## 📂 Solution Overview

### The Pipe Syntax (LCEL)

Instead of writing imperative code (e.g., `response = call_api(prompt)`), we define a declarative chain:

```python
# The Recipe for the AI interaction
chain = prompt | model | parser
```

1. **Prompt (`ChatPromptTemplate`) -** Handles the "System" vs "User" role formatting automatically.
2. **Model (`ChatGoogleGenerativeAI`) -** Connects to Gemini, handling retries and connection errors.
3. **Parser (`StrOutputParser`) -** Cleans the messy JSON response into a simple string.

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

### 4. **Run the Chain**

```bash
python day31.py
```

### 5. **Sample Interaction**

```text
Enter a tech topic: Agentic AI
Asking Gemini about Agentic AI...
Answer: Agentic AI refers to AI systems that can autonomously perceive, reason, plan, and act in an environment to achieve specific goals.
```

## 🧠 Key Learnings

* **Model Agnosticism -** Using LangChain's `ChatPromptTemplate`, we can switch the underlying model (e.g., from OpenAI to Gemini) by changing **one line of code**. The rest of the application logic remains untouched.
* **LCEL (LangChain Expression Language) -** The pipe syntax (`|`) makes the flow of data intuitive. It forces a clean separation of concerns, constructing the prompt is separate from executing the model, which is separate from parsing the output.
* **Wrappers -** No longer need to check if `response.status_code == 200`. The LangChain wrapper handles the network layer, letting us focus purely on the application logic.

---
[Back to Main Repo](../README.md)
