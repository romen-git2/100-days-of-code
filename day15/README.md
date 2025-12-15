# Day 15 - The Command Pattern

**Phase 2 -** Agent Design Patterns & Integrations

## 📝 The Challenge

**Goal -** Create executable command objects that can be queued and executed later.

In sophisticated agentic systems, agents often need to think (plan) before they act. If an agent executes code immediately (e.g., `send_email()`), it becomes difficult to review the plan, batch operations or implement undo functionality.

This challenge uses the **Command Pattern** to encapsulate a request as an object. This allows us to parameterize methods with different requests, queue or log requests and support undoable operations.

## 🛠️ Tech Stack

* **Python 3.10+**
* **`abc` (Abstract Base Classes)** - Used to define a strict interface (`execute()`) that all Command objects must implement.

## 📂 Solution Overview

The solution script (`day15.py`) implements the pattern in three parts:

1. **The Interface (`Command`)** - An abstract base class ensuring every command has an `.execute()` method.
2. **Concrete Commands**:
    * `SaveFileCommand` - Stores filename and content, simulates file I/O when executed.
    * `EmailCommand` - Stores recipient and subject, simulates sending an email when executed.
3. **The Invoker (`AgentExecutor`)**:
    * **Queueing** - Accepts commands via `add_command()` without running them immediately.
    * **Execution** - Iterates through the queue in `execute_pending()`, running each command.
    * **History** - Keeps a log of executed commands for audit purposes.

## 🏃‍♂️ How to Run

1. **Install Dependencies:**
    No external libraries are needed.

2. **Run the Script:**

    ```bash
    python day15.py
    ```

3. **Expected Output:**
    You will see the agent building the plan first (adding to queue) and then executing the plan in a batch.

    ```text
    Agent is thinking and building a plan...
    Added SaveFileCommand to queue.
    Added EmailCommand to queue.
    Added SaveFileCommand to queue.
    Executing Plan (3 steps)
    Saving to 'report.txt': Analysis of financial data......
    Sending email to admin@corp.com. Subject='Report Ready'
    Saving to 'log.txt': Email sent successfully....
    Plan Complete
    Execution History: ['SaveFileCommand', 'EmailCommand', 'SaveFileCommand']
    ```

## 🧠 Key Learnings

* **Decoupling -** The `AgentExecutor` (Invoker) knows nothing about how to send emails or save files. It only knows how to call `.execute()`. This makes the system extensible, you can add a `DatabaseCommand` later without changing the executor.
* **Planning vs. Execution -** This pattern enables agents to generate a full 5-step plan, review it (or have a human review it) and then execute it, rather than acting impulsively step by step.
* **Auditability -** Since every action is an object, it is trivial to store the history of actions (`self._history`) for debugging or compliance logs.

---
[Back to Main Repo](../README.md)
