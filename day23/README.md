# Day 23 - Flexible Memory with MongoDB (NoSQL)

**Phase 2 -** Agent Design Patterns & Integrations

## 📝 The Challenge

**Goal -** Implement a Flexible Memory system for the agent using **MongoDB** to store complex, unstructured data like reasoning chains and nested JSON outputs.

While **SQLite** (Day 22) is perfect for structured logs (rows and columns), AI agents often produce messy data. An LLM's thought process, a conversation history with varying attributes or a scrape of a dynamic website doesn't fit neatly into a rigid SQL table.

We need a **NoSQL** database that acts like a Document Store allowing us to dump complex JSON objects directly into storage without defining a schema first.

## 🛠️ Tech Stack

* **Python 3.10+**
* **MongoDB -** A NoSQL database that stores data in flexible, JSON-like documents.
* **`pymongo` -** The standard Python driver for MongoDB.
* **`python-dotenv` -** To securely manage database credentials (connection strings).

## 📂 Solution Overview

### 1. The Connection

We connect to a MongoDB instance (a cloud Cluster via MongoDB Atlas) using a **Connection URI**.

### 2. The Data Structure (The "Document")

Unlike SQL, we don't create a table. We simply insert a dictionary. This allows us to store nested lists and sub dictionaries, which is perfect for representing an Agent's Chain of Thought:

```json
{
  "agent": "Researcher",
  "task": "Market Analysis",
  "thought_chain": [
    {"step": 1, "tool": "Google Search"},
    {"step": 2, "tool": "Summarizer"}
  ],
  "result": {
    "confidence": 0.9,
    "summary": "..."
  }
}
```

### 3. The Operations

* **Insert (Write) -** using `insert_one()` to save the complex dictionary.
* **Find (Read) -** using `find()` to retrieve documents based on specific fields (e.g., `{"agent": "Researcher"}`).

## 🏃‍♂️ How to Run

1. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

2. **Setup MongoDB:**
    * **Option A (Cloud) -** Create a free cluster on [MongoDB Atlas](https://www.mongodb.com/cloud/atlas). Get your connection string.
    * **Option B (Local) -** Use Docker - `docker run -d -p 27017:27017 mongo`.

3. **Configure Environment (Create a .env file in the same folder):**

    ```Ini, TOML
    MONGO_URI="mongodb+srv://YOUR_USER:YOUR_PASS@cluster.mongodb.net/..."
    # Or for local - MONGO_URI="mongodb://localhost:27017/"
    ```

4. **Run the Script:**

    ```bash
    python day23.py
    ```

## 🧠 Key Learnings

* **SQL vs. NoSQL -** Learned that SQL (SQLite) is best for rigid, structured data (like transaction ledgers), while NoSQL (MongoDB) is superior for flexible, hierarchical data (like AI thought traces).
* **Schemaless Design -** Discovered the power of not having to pre-define table columns. If an agent gains a new attribute tomorrow, we can start saving it immediately without migrating the database.
* **JSON Compatibility -** Realized that since LLMs and APIs speak JSON and MongoDB stores JSON (BSON), they are a natural fit for the AI tech stack.

---
[Back to Main Repo](../README.md)
