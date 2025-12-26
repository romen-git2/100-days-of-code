# Day 19 - The Pattern Toolkit

**Phase 2 -** Agent Design Patterns & Integrations

## 📝 The Challenge

**Goal -** Refactor previously learned patterns into a clean, reusable Python package (`agent_toolkit`).

In software engineering, you don't want to rewrite the **Singleton** or **Observer** logic for every new agent you build. You want a Toolbox that you can carry with you.

This challenge involves moving from *scripting* to *library building*. We will create a modular Python package containing:
1.**Creation Module -** Holds `SingletonMeta` and `AgentFactory`.
2.**Behavior Module -** Holds `Observer`, `Subject` and `Decorators`.
3.**Client Script -** A separate `day19.py` that imports tools from this package to build a game/agent simulation.

## 🛠️ Tech Stack

* **Python 3.10+**
* **Modules/Packages -** Understanding `__init__.py` and relative imports.

## 📂 Folder Structure

The structure is critical for this challenge. It simulates a real-world library layout:

```text
Day19_PatternToolkit/
│
├── agent_toolkit/          <-- 📦 Reusable Package
│   ├── __init__.py         <-- Exposes the classes
│   ├── creation.py         <-- Creation Patterns (Singleton, Factory)
│   └── behavior.py         <-- Behavior Patterns (Observer, Decorator)
│
└── day19.py                 <-- 🏃 Client Code (The User of the library)
```

## 📂 Solution Overview

### 1. `creation.py`

* Contains the **Singleton Metaclass** (for global configs) and a generic **AgentFactory**. These deal with *how objects are born*.

### 2. `behavior.py`

* Contains the **Observer/Subject** classes (for event handling) and the **@log_execution** decorator. These deal with *how objects act*.

### 3. `__init__.py`

* This file imports the classes from the sub-modules and exposes them at the package level. This allows the user to write: `from agent_toolkit import SingletonMeta` instead of `from agent_toolkit.creation import SingletonMeta`.

## 🏃‍♂️ How to Run

1. **Run the Script:**
   Because `day19.py` is next to the `agent_toolkit` folder, Python will recognize it as a package.

    ```bash
    python day19.py
    ```

2. **Expected Output:**
    You will see the `day19.py` utilizing tools it didn't define itself.

    ```text
    Config Loaded
    Are configs the same object? True
    Triggering Event: Boss Spawn
    Displaying notification: Boss Spawn
    Playing sound effect for Boss Spawn
    Starting attack...
    Player swings sword
    Finished attack (Time: 0.2006s)
    ```

## 🧠 Key Learnings

* **Packaging -** Code becomes Infrastructure when it's packaged. You stop thinking about *how* to write an Observer and start thinking about *where* to import it from.
* **Separation of Concerns -** Splitting code into `creation` and `behavior` files makes the library easier to navigate and maintain.
* **Namespace Management -** Using `__init__.py` to control what users see creates a clean Public API for your library, hiding the internal file structure.

---
[Back to Main Repo](../README.md)
