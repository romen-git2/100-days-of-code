# Day 5 - API Calls with `requests`

**Phase 1 -** Advanced Python & Agent Tools

## 📝 The Challenge

**Goal -** Query a public API (e.g., JSONPlaceholder) and save the response.

While web scraping (Day 4) is great for extracting data from user-facing websites, **APIs (Application Programming Interfaces)** are the primary language of software-to-software communication. For an AI agent to perform useful tasks-like checking the weather, sending emails or retrieving stock prices - it must be able to send structured requests to external servers and interpret the JSON responses. This challenge establishes the foundational skill of integrating external tools into agent's workflow.

## 🛠️ Tech Stack

* **Python 3.10+**
* **`requests`** - The standard library for making HTTP requests in Python. It simplifies sending requests and handling responses compared to the built-in `urllib`.
* **`json`** - Python's built-in library for parsing and generating JSON data.

## 📂 Solution Overview

The solution script (`day5.py`) performs the following actions:

1. **Endpoint Connection** - Defines a target URL (`https://jsonplaceholder.typicode.com/todos`) which serves as a mock REST API for testing.
2. **GET Request** - Uses `requests.get()` to retrieve data.
3. **Safety Check** - Implements `response.raise_for_status()` to immediately catch and report any HTTP errors (like 404 Not Found or 500 Server Error).
4. **Parsing** - Converts the raw response text into a Python list of dictionaries using `.json()`.
5. **Agent Logic** - Filters the data to find specific items (e.g., completed tasks for User ID 1).
6. **Persistence** - Saves the filtered "agent memory" to a local file (`agentTodos.json`) for future use.

## 🏃‍♂️ How to Run

1. **Install Dependencies:**

    ```bash
    pip install requests
    ```

2. **Run the Script:**

    ```bash
    python day5.py
    ```

3. **Expected Output:**
    The script will log its progress and create a JSON file with the results.

    ```text
    Connecting to https://jsonplaceholder.typicode.com/todos...
    Successfully retrieved 200 tasks.
    Found 11 completed tasks for User 1.
    Saved filtered tasks to 'agentTodos.json'
    ```

## 🧠 Key Learnings

* **Structured Data -** Unlike HTML scraping, APIs return **JSON**, which is clean, structured and ready for an agent to use immediately.
* **Error Handling -** Using `raise_for_status()` is crucial. An agent needs to know if a tool failed so it can retry or choose a different strategy, rather than crashing on bad data.
* **Tool Integration -** This pattern (Request -> Parse -> Action) is the exact mechanism used by advanced frameworks like LangChain when an agent calls a "Tool".

---
[Back to Main Repo](../README.md)
