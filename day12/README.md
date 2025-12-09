# Day 12 - The Singleton Pattern

**Phase 2 -** Agent Design Patterns & Integrations

## 📝 The Challenge

**Goal -** Implement a Singleton class for loading agent configuration.

In large-scale agent systems, certain resources like configuration loaders, database connection pools or logger instances should be shared globally rather than recreated every time they are needed. Creating 50 separate objects to read the same `config.json` file is inefficient and can lead to synchronization errors.

This challenge uses the **Singleton Pattern** to ensure that a class has only **one instance** and provides a global point of access to it.

## 🛠️ Tech Stack

* **Python 3.10+**
* **`__new__` Method** - We override Python's object creation method to intercept the instantiation process and return an existing instance if one is already available.

## 📂 Solution Overview

The solution script (`day12.py`) demonstrates the pattern:

1. **The Class (`ConfigurationManager`)**:
    * Uses a class variable `_instance` to track if the object already exists.
    * Overrides `__new__` to control creation. If `_instance` is `None`, it creates the object, otherwise, it returns the existing one.
2. **Simulation**:
    * Simulates loading configuration settings (API keys, model versions) only once.
3. **Proof**:
    * The script attempts to create two separate variables (`config1` and `config2`).
    * It prints their memory IDs (`id(obj)`) to prove that both variables actually point to the exact same object in memory.

## 🏃‍♂️ How to Run

1. **Install Dependencies:**
    No external libraries are needed.

2. **Run the Script:**

    ```bash
    python day12.py
    ```

3. **Expected Output:**
    You will see that the "Loading settings" log only appears once and both objects share the same ID.

    ```text
    Creating the FIRST and ONLY instance...
    Loading settings from disk (simulated)...
    Config 1 Model: gpt-4
    Config 1 ID: 1565086280272
    Instance already exists. Returning existing one.
    Config 2 Model: gpt-4
    Config 2 ID: 1565086280272
    Config1 and config2 are the same object.
    ```

## 🧠 Key Learnings

* **`__new__` vs. `__init__`** - `__init__` initializes an object, but `__new__` creates it. To implement a true Singleton in Python, you must control `__new__`.
* **Resource Optimization** - This pattern is essential for expensive operations (like connecting to a remote Secret Manager or Database) that should only happen once during the agent's lifecycle.
* **Global State** - While powerful, Singletons act as global state. They should be used sparingly (e.g., for Config or Logging) to avoid making the system difficult to test.

---
[Back to Main Repo](../README.md)
