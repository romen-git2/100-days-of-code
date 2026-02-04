# **Day 36 - The ReAct Agent (Reasoning + Acting)**

**Phase 3 -** Agent Framework Foundations

## **The Challenge**

**Goal -** Build an autonomous agent that can solve multi-step logic puzzles by looping through thoughts and actions.

In Day 35, we manually wrote the logic to execute tool calls. This is known as hard-coded orchestration. Today, I implemented the **ReAct (Reason + Act)** pattern. Instead of the developer defining the steps, the **Agent** defines the steps.

By providing a set of tools and a goal, the agent enters a loop:

1. **Thought -** Analyzes the current state and decides what to do next.  
2. **Action -** Calls a specific tool (e.g., a calculator).  
3. **Observation -** Learns from the tool's result.  
4. **Repeat -** Continues until it reaches the final answer.

## **🛠️ Tech Stack**

* **Python 3.10+**  
* **langchain** - Utilizing the unified create_agent factory.  
* **langgraph**: The underlying engine handling the stateful loop.  
* **langchain-google-genai** - Powered by **Gemini 2.5 Flash**.

## **📂 Solution Overview**

The agent is tasked with a sequential calculation that an LLM cannot solve accurately on its own:

"Find the length of Word A, subtract the length of Word B and raise the result to the power of 3."

We use the modern create_agent abstraction.

```python
from langchain.agents import create_agent

# The agent is defined by its model and its toolkit  
agent_executor = create_agent(  
    model=llm,   
    tools=tools,  
    system_prompt="You are a helpful assistant that uses tools for math and word lengths."  
)
```

### **The Tools**

1. get_word_length - A deterministic Python function to count characters (LLMs notoriously struggle with counting).  
2. power_calculator - A math tool for precise exponentiation.

## **🏃‍♂️ How to Run**

### **1. Setup Environment**

Ensure your .env file is ready with your API key.

Install the latest packages:

```text
pip install -r requirements.txt
```

### **2. Execute the Agent**

```text
python day36.py
```

### **3. Sample Interaction**

```text
Query: Find the length of the word 'pneumonoultramicroscopicsilicovolcanoconiosis', subtract the length of 'pseudopseudohypoparathyroidism' and raise the result to the power of 3.
Thought: Calling get_word_length with {'word': 'pneumonoultramicroscopicsilicovolcanoconiosis'}...
'pneumonoultramicroscopicsilicovolcanoconiosis' has 45 letters.
Observation: 45
Thought: Calling get_word_length with {'word': 'pseudopseudohypoparathyroidism'}...
'pseudopseudohypoparathyroidism' has 30 letters.
Observation: 30
Thought: Calling power_calculator with {'exponent': 3, 'base': 15}...
15^3 = 3375
Observation: 3375
AI: [{'type': 'text', 'text': 'The result is 3375.', 'extras': {'signature': 'CrwCAb4+9vvqBF9XG8LTl4iSGJ6uxM8NVy9xhw0XM24R9f/0g5ktACSlX761DrZKxTKAUA6XUlFF65jdojpqRWfnXSuyK+jqj1LTJX8oG6HRqTAgh9aUZVD7LlMaAV76qVe3q+Sq8Zna3Ww64eNXA2nmT3e8/bxlhh52d8lH2btvoxI510DiOLyFEPqNuXgHT/F+LPhrBC1W2BUL42Z4PTiDK+33g7tFtx7uOdSMDdWL8dS235saq56W09/lBPvmHnblNVpBDiJhg0A8TUomf6gEKeAPY6R1OahxAUIjiVojh/yvRMV6Vq6TP8iW3/7WiYEqywF8wyDOtgoq98tCHVF76accA72HMaipHTrg+aT8FToMzpRnJ1Y4KGiBQx32CojuyQGD/Iq7auX7ms50XFlnXyTDcTKP55uBtjLSqg=='}}]
```

## **🧠 Key Learnings**

* **Deterministic vs. Probabilistic -** By giving the LLM tools, we move from black box guessing to reliable automation.  
* **State Management -** Maintain a Scratchpad, a memory of what it has already done so it doesn't repeat steps.  
* **The Reasoning Tax -** While more powerful, ReAct agents take longer and use more tokens because they think out loud. For simple tasks, a standard chain is better, for complex, unknown paths, the ReAct agent is essential.

---
[Back to Main Repo](../README.md)
