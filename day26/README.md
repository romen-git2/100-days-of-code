# Day 26 - The Full Cycle Tool (API + Database)

**Phase 2 -** Agent Design Patterns & Integrations

## 📝 The Challenge

**Goal -** Build a robust, self-contained Agent Tool that performs a complete data lifecycle - **Fetch(API) -> Process(Logic) -> Store(DB)**.

A production grade agent needs to *remember* what it found. If an agent analyzes a user's GitHub profile today, it should store that snapshot so it can track changes(like follower growth) next week without needing to ask the user again.

We will build a tool that:

1. **Fetches** public profile data from the GitHub API.
2. **Validates** and structures the data using Python `dataclasses`.
3. **Persists** the data into a local SQLite database using an **Upsert** strategy(Insert or Update).

## 🛠️ Tech Stack

* **Python 3.10+**
* **`requests` -** For handling HTTP communication with the GitHub API.
* **`sqlite3` -** Standard library for local persistence(no external server needed).
* **`dataclasses` -** For defining strict data schemas, preventing dictionary spaghetti inside the agent's logic.

## 📂 Solution Overview

We implemented the **Service-Repository Pattern** to decouple concerns:

1. **The Service(`GitHubAPI`) -** Purely responsible for talking to the outside world. It handles URL construction, error checking (404s) and JSON parsing.
2. **The Repository(`DatabaseManager`) -** Purely responsible for talking to the disk. It handles connection pooling, schema creation and SQL queries.
3. **The Coordinator(`AgentTool`) -** The Brain that calls the Service to get data and hands it to the Repository to save it.

### The Upsert Strategy

We used a crucial SQL technique:

```sql
INSERT INTO table ... ON CONFLICT(id) DO UPDATE SET ...
```

This ensures that if the agent runs multiple times for the same user, it doesn't crash or create duplicates. it simply updates the existing record with fresh stats. This is vital for **Idempotency** in autonomous systems.

## 🏃‍♂️ How to Run

### 1. Install Dependencies

This script uses only Python standard libraries and `requests`.

```bash
pip install -r requirements.txt
```

### 2. **Run the Tool**

```bash
python day26.py
```

### 3. **Observe the Output**

You will see the tool:

1. Connect to the API.
2. Fetch data for specific users(e.g., `torvalds`, `defunkt`).
3. Log the save operation to the database.
4. Print a final audit count of records stored.

```text
Fetching data for torvalds...
Found Linus Torvalds | Repos: 9 | Followers: 270611
Saving profile for torvalds...
```

### 4. **Verify the Data(Optional)**

You can inspect the generated `agent_data.db` file using any SQLite viewer or the command line:

```bash
sqlite3 agent_data.db "SELECT * FROM github_profiles;"
```

## 🧠 Key Learnings

* **Separation of Concerns -** Hard coding SQL inside the API fetching function makes code untestable. Separating them into a `DatabaseManager` class makes the system modular.
* **Data Contracts -** Using `@dataclass` acts as a contract between the API and the DB. If the API changes, I only fix the Service layer, the DB layer remains stable.
* **Idempotency -** Agents will often repeat tasks. The database must handle duplicate inputs gracefully(using ON CONFLICT logic) to prevent data corruption.

---
[Back to Main Repo](../README.md)
