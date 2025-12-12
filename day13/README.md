# Day 13 - The Observer Pattern

**Phase 2 -** Agent Design Patterns & Integrations

## 📝 The Challenge

**Goal -** Set up an observer mechanism to track agent state changes.

AI Agents operate asynchronously and often unpredictably. When an agent completes a task, encounters a critical error or moves to a new reasoning step, it needs to "broadcast" this event to various systems (like a User Interface, a Database logger or an Alert system).

Hardcoding these calls (e.g., `agent.log_to_db()`, `agent.send_email()`) creates tight coupling and messy code. This challenge uses the **Observer Pattern** to decouple the agent (the **Subject**) from the systems listening to it (the **Observers**), enabling a clean Event-Driven Architecture.

## 🛠️ Tech Stack

* **Python 3.10+**
* **`abc` (Abstract Base Classes)** - Used to define a strict interface that all Observers must adhere to, ensuring the Agent can notify them uniformly.

## 📂 Solution Overview

The solution script (`day13.py`) implements the pattern in three parts:

1. **The Interface (`Observer`)** - An abstract class defining the `update()` method.
2. **The Subject (`Agent`)**:
    * Maintains a private list of subscribers (`_observers`).
    * Provides `attach()` and `detach()` methods to manage listeners.
    * Calls `notify()` whenever its internal state changes.
3. **Concrete Observers**:
    * `LoggerObserver` - Simply prints status changes to the console (simulating a log file).
    * `AlertSystemObserver` - Reacts intelligently sending a "CRITICAL ALERT" only if the status is "Error" and a success message if "Complete".

## 🏃‍♂️ How to Run

1. **Install Dependencies:**
    No external libraries are needed.

2. **Run the Script:**

    ```bash
    python day13.py
    ```

3. **Expected Output:**
    You will see the Agent "pushing" updates to the observers. Notice how the Alert System reacts differently depending on the specific status provided.

    ```text
    LoggerObserver is now watching Agent-001.
    AlertSystemObserver is now watching Agent-001.
    Agent-001 is changing status to Working
    Agent-001 notifying observers...
    Agent 'Agent-001' changed state to 'Working'.
    Agent-001 is changing status to Complete
    Agent-001 notifying observers...
    Agent 'Agent-001' changed state to 'Complete'.
    User notified: Task finished by Agent-001.
    Agent-001 is changing status to Error
    Agent-001 notifying observers...
    Agent 'Agent-001' changed state to 'Error'.
    CRITICAL ISSUE DETECTED WITH Agent-001
    ```

## 🧠 Key Learnings

* **Decoupling -** The `Agent` class knows nothing about logging or alerts. It simply iterates through a list and calls `.update()`. This allows you to add a new "SlackNotifier" without ever touching the Agent's code.
* **One-to-Many -** A single event (Status Change) can trigger multiple independent actions (Log to file, Update UI, Send Email).
* **Event-Driven -** This pattern is the backbone of robust agent systems, allowing them to stream tokens or report progress in real-time without blocking the main execution loop.

---
[Back to Main Repo](../README.md)
