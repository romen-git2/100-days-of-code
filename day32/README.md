# Day 32 - Simple Chains (Prompt Chaining)

**Phase 3 -** Agent Framework Foundations

## 📝 The Challenge

**Goal -** Chain two prompts for a Q&A workflow.

While Day 31 focused on a single LLM call, Day 32 is about **Sequential Processing**. Instead of asking an LLM to perform multiple complex tasks in one go, we break the logic into a pipeline where the output of the first prompt serves as the input for the second. This prevents task confusion and significantly improves the quality of the final output.

## 🛠️ Tech Stack

* **Python 3.10+**
* **`langchain`** - For orchestration using LCEL (LangChain Expression Language).
* **`langchain-google-genai`** - Utilizing the **Gemini 2.5 Flash** model, which is optimized for low latency and agentic use cases.
* **`python-dotenv`** - For secure API key management.

## 📂 Solution Overview

We implemented a two-step "Expert-to-Beginner" pipeline:

1. **The Expert Chain -** Takes a topic and generates a high fidelity, technical explanation.
2. **The Communicator Chain -** Takes that technical output and translates it into a simple, one-sentence summary for a beginner.

### The Pipeline Logic (LCEL)

```python
# The output of chain_expert is mapped to tech_info for the next step
full_chain = (
    {"tech_info": chain_expert} 
    | chain_simplify
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

### 4. **Run the Script**

```bash
python day32.py
```

### 5. **Sample Interaction**

```text
Enter a topic: AI agents
Consulting the expert...
Simplifying the response...
Summary: An AI agent is a smart computer program that independently senses its environment, makes decisions, acts, and learns to achieve specific goals.
```

## 🧠 Key Learnings

* **Task Decomposition -** Splitting reasoning from formatting significantly improves output quality. By isolating the technical research step from the simplification step, the model performs better at both.
* **Dynamic Mapping -** Using dictionary mapping within an LCEL chain allows for seamless data handovers between incompatible prompt variables.

---
[Back to Main Repo](../README.md)
