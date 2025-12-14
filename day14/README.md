# Day 14 - The Decorator Pattern

**Phase 2 -** Agent Design Patterns & Integrations

## 📝 The Challenge

**Goal -** Decorate a function to add timing logs.

As you build complex agents, you often need to add "middleware" functionality like logging, retrying failed API calls or measuring performance to multiple different tools. Writing this logic inside every single function leads to repetitive, messy code.

This challenge uses the **Decorator Pattern** to "wrap" agent functions with dynamic behavior. By placing a simple tag (like `@timer`) above a function, we can inject logic before and after its execution without modifying the function's actual code.

## 🛠️ Tech Stack

* **Python 3.10+**
* **`functools.wraps`** - A helper that preserves the metadata (name, docstring) of the original function so debugging remains easy.
* **`time`** - Used to calculate the execution duration.

## 📂 Solution Overview

The solution script (`day14.py`) demonstrates how to wrap agent tasks:

1. **The Decorator (`measure_performance`)**:
    * Accepts a function `func` as input.
    * Defines a `wrapper` that records the `start_time`, runs the function and then calculates the `duration`.
    * Uses `*args` and `**kwargs` to ensure it works with *any* function signature.
2. **The Application**:
    * We apply `@measure_performance` to a slow task (`run_agent_reasoning`) and a fast task (`quick_memory_lookup`).
    * The core logic of those functions remains clean, they know nothing about timers.

## 🏃‍♂️ How to Run

1. **Install Dependencies:**
    No external libraries are needed.

2. **Run the Script:**

    ```bash
    python day14.py
    ```

3. **Expected Output:**
    You will see the decorator intercepting the calls, printing the start/end logs and measuring the time taken.

    ```text
    Starting task 'run_agent_reasoning'
    Agent is thinking about Quantum physics strategy
    Finished run_agent_reasoning in 1.5345 seconds
    Starting task 'quick_memory_lookup'
    Checking memory for Project Alpha
    Finished quick_memory_lookup in 0.1008 seconds
    ```

## 🧠 Key Learnings

* **Separation of Concerns -** The business logic (reasoning) is separated from the operational logic (timing/logging). This makes your code cleaner and easier to read.
* **Reusability -** You write the timing logic once and can apply it to hundreds of agent tools simply by adding the `@` line.
* **`functools.wraps` -** Essential for production decorators. Without it, your decorated functions lose their identity (name and docstrings), making debugging a nightmare.

---
[Back to Main Repo](../README.md)
