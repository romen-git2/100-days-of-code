# Day 11 - The Factory Pattern

**Phase 2 -** Agent Design Patterns & Integrations

## 📝 The Challenge

**Goal -** Write a factory function to instantiate agent types dynamically.

In complex multi-agent systems, a "Manager" or "Orchestrator" agent often needs to spawn specialized sub-agents (e.g., a Researcher, a Coder or a Critic) based on the task at hand. Hardcoding these instantiations (e.g., `if task == 'code': agent = CoderAgent()`) leads to tight coupling and messy code.

This challenge focuses on the **Factory Pattern**, a creational design pattern that provides an interface for creating objects in a superclass but allows subclasses to alter the type of objects that will be created. It centralizes the "birth" of agents, making your system scalable and easier to maintain.

## 🛠️ Tech Stack

* **Python 3.10+**
* **`abc` (Abstract Base Classes)** - Used to enforce a common interface (`BaseAgent`) so that the factory produces interchangeable objects.

## 📂 Solution Overview

The solution script (`day11.py`) implements the pattern in three parts:

1. **The Interface (`BaseAgent`)** - An abstract class that forces every agent to have an `act()` method.
2. **The Concrete Agents**:
    * `ResearchAgent` - Simulates searching for information.
    * `CreativeAgent` - Simulates brainstorming.
    * `CoderAgent` - Simulates writing code.
3. **The Factory (`AgentFactory`)** - A class with a static method `create_agent(type)`. It contains the logic to decide *which* class to instantiate based on a string input.

## 🏃‍♂️ How to Run

1. **Install Dependencies:**
    No external libraries are needed (uses Python Standard Library).

2. **Run the Script:**

    ```bash
    python day11.py
    ```

3. **Expected Output:**
    The script simulates a loop where a client requests different agents by name ("research", "creative", "coding") and receives the correct agent instance to perform a task.

    ```text
    Searching sources for History of AI
    Result: Found 5 relevant sources.
    Brainstorming ideas for Logo design for a startup
    Result: Drafted 3 creative concepts.
    Writing python code for Fibonacci sequence script
    Result: Code for Fibonacci sequence script
    ```

## 🧠 Key Learnings

* **Decoupling -** The code that *uses* the agent (the main loop) doesn't need to know how to *construct* the agent. It just asks the Factory.
* **Scalability -** If you want to add a `WriterAgent`, you only have to modify the Factory and create the new class. The rest of your system (the client code) remains untouched.
* **Dynamic Dispatch -** This pattern is essential for "Agent Swarms" where a router decides which tool or sub-agent to call based on user input at runtime.

---
[Back to Main Repo](../README.md)
