# Day 22 - Persistent Memory with SQLite

**Phase 2 -** Agent Design Patterns & Integrations

## 📝 The Challenge

**Goal -** Give the agent Long-Term Memory by implementing a persistent storage layer using **SQLite**.

Up until now, our agents have suffered from Amnesia. If the script crashed or the computer restarted, all data (webhook logs, API results, conversation history) was lost because it lived in **RAM (Volatile Memory)**.

To build robust, production-ready agents, we must store critical state data on **Disk (Persistent Storage)**.

## 🛠️ Tech Stack

* **Python 3.10+**
* **`sqlite3`** - A serverless, self-contained SQL database engine included with Python. No installation required.
* **`datetime`** - For timestamping agent activities.

## 📂 Solution Overview

We implemented a `AgentMemory` class that handles all database interactions. This adheres to the **Single Responsibility Principle**, the agent doesn't need to know SQL, it just asks the memory manager to save or recall.

### 1. The Schema (The Brain Structure)

We created a table called `agent_logs` with the following columns:

* `id` - A unique identifier for every action.
* `timestamp` - When it happened.
* `agent_name` - Who did it (e.g., Spotify Bot vs. Manager Bot).
* `task` - What they tried to do.
* `result` - The outcome (Success/Failure).

### 2. The Operations

* **Initialization -** automatically creates the `.db` file if it doesn't exist.
* **Commit (Write) -** Uses `INSERT` to safely store data.
* **Recall (Read) -** Uses `SELECT` to retrieve history, allowing the agent to learn from past actions.

## 🏃‍♂️ How to Run

1. **Run the Script:**

    ```bash
    python day22.py
    ```

    *Output - You will see logs confirming that actions were saved.*

2. **Verify Persistence:**
    * Run the script once.
    * Stop it.
    * Run it again.
    * **Observe -** The Recall step will show records from *both* runs. The agent remembers!

3. **Check the File:**
    You will see a new file named `agent_memory.db` in your directory. You can open this with any SQLite viewer (like *DB Browser for SQLite*) to inspect the raw data.

## 🧠 Key Learnings

* **Volatile vs. Persistent -** Understood the critical difference between storing state in variables (lost on exit) vs. a database (saved on disk).
* **ACID Properties -** Learned that SQLite ensures data integrity, if the agent crashes halfway through saving a log, the database file won't be corrupted.
* **Schema Design -** Designed a flexible table structure that can track the history of multiple different agents in a swarm.

---
[Back to Main Repo](../README.md)
