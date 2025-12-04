# Day 8 - OOP Design Patterns (The Strategy Pattern)

**Phase 1 -** Advanced Python & Agent Tools

## 📝 The Challenge

**Goal -** Define two distinct strategies and switch between them dynamically.

AI Agents are not static entities, they need to adapt to different situations. Sometimes an agent needs to be "fast and cheap" (e.g., a simple keyword search), while other times it needs to be "slow and smart" (e.g., deep reasoning with an LLM). Hardcoding this logic into one giant `if-else` block makes code messy and hard to maintain.

This challenge focuses on the **Strategy Pattern**, an Object-Oriented Programming (OOP) design that encapsulates algorithms into separate classes, allowing the agent to swap its "brain" at runtime.

## 🛠️ Tech Stack

* **Python 3.10+**
* **`abc` (Abstract Base Classes)** - Python's built-in module for defining interfaces. It ensures that every strategy adheres to a specific structure (e.g., they all must have a `processQuery` method).

## 📂 Solution Overview

The solution script (`day8.py`) implements a modular agent architecture:

1. **Interface (`ProcessingStrategy`)** - An abstract base class that defines the contract. Any new strategy *must* implement the `processQuery` method.
2. **Strategy A (`KeywordSearchStrategy`)** - A fast, deterministic algorithm that checks for specific keywords (simulating a database lookup).
3. **Strategy B (`LLMReasoningStrategy`)** - A slower, more complex algorithm that simulates "thinking" (using `time.sleep`) to represent calling an LLM.
4. **Context (`Agent`)** - The main class that utilizes the strategies. It has a `setStrategy()` method, allowing it to switch behaviors on the fly without changing its internal code.

## 🏃‍♂️ How to Run

1. **Install Dependencies:**
    No external libraries are needed (uses Python Standard Library).

2. **Run the Script:**

    ```bash
    python day8.py
    ```

3. **Expected Output:**
    You will see the agent answer a simple question, fail a hard question, switch strategies and then successfully answer the hard question.

    ```text
    bot received query: 'What is the weather?'
    Using fast Keyword Search...
    It is sunny today.
    bot received query: 'What is the meaning of life?'
    Using fast Keyword Search...
    No keywords found.
    Switching bot's strategy to LLMReasoningStrategy
    bot received query: 'What is the meaning of life?'
    Using advanced LLM Reasoning...
    Based on the context of 'What is the meaning of life?', I deduce the answer is complex.
    ```

## 🧠 Key Learnings

* **Composition over Inheritance -** The Agent *has a* Strategy, it doesn't inherit from it. This allows for dynamic switching (changing the "brain" while the program is running).
* **Separation of Concerns -** The agent doesn't need to know *how* to solve the problem, only that the strategy object *can* solve it. This makes adding new tools (like a Google Search strategy) easy.
* **Resilience -** This pattern is the foundation for "fallback" mechanisms (e.g., if the LLM API is down, automatically switch to the Keyword Strategy).

---
[Back to Main Repo](../README.md)
