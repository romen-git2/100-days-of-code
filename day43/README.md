# **Day 43 - Simple Agents & The 3 Evolution Variants**

**Phase 3 -** Agent Framework Foundations

## **📝 The Challenge**

**Goal -** Build and compare three distinct AI Agent architectures using LangChain `create_agent` factory.

1. **Zero-Shot Agent -** A pure LLM with no external tools.  
2. **Tool-Using Agent -** An LLM with hands (Python functions) to fetch live data.  
3. **Memory Agent -** A stateful LLM that tracks conversation history across multiple turns.

## **🛠️ Tech Stack**

* **LangChain** - The `create_agent` factory for production-ready agents.  
* **Gemini 2.5 Flash** - Our engine (Model).  
* **Python Decorators** - @tool used to define the action layer.  

## **🧪 Execution Results**

### **1. Zero-Shot Variant**

* **Query -** "What is the discount code for Gaming Laptop?"  
* **Outcome -** The AI provided general shopping advice (check banners, sign up for newsletters).  
* **Conclusion -** Smart, but lacked specific private data (our internal discount codes).

### **2. Tool-Using Variant**

* **Query -** "Use your tool to find the code for the Gaming Laptop."  
* **Outcome -** The AI identified the intent, executed the `get_discount_code` tool and returned GAMER15.  
* **Conclusion -** 100% accuracy by bridging the gap between reasoning and external data.

### **3. Memory Agent Variant**

* **Turn 1 -** "Hi, I'm Romen. I really want that Gaming Laptop."  
* **Turn 2 -** "What was the discount code for the item I mentioned earlier?"  
* **Outcome -** The AI resolved that "item" referred to the "Gaming Laptop" from Turn 1 and fetched the code correctly.  
* **Conclusion -** Full context-awareness achieved through stateful message history.

## **🏃‍♂️ How to Run**

1. Install dependencies:  

   ```bash
   pip install -r requirements.txt
   ```

2. Run the script:

   ```bash  
   python day43.py
   ```

## **🧠 Reflections**

* **Anaphora Resolution -** Seeing the agent resolve "the item I mentioned earlier" into "Gaming Laptop" without me repeating the product name was the lightbulb moment for how memory actually functions in LLM states.  
* **State vs. Knowledge -** A model doesn't need to *know* everything if it knows *how* to use tools. This reduces hallucinations significantly.

---
[Back to Main Repo](../README.md)
