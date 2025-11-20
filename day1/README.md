# Day 1 - Async Python & `asyncio`

**Phase 1 -** Advanced Python & Agent Tools

## 📝 The Challenge

[cite_start]**Goal -** Create an async function to fetch multiple URLs concurrently[cite: 3, 4].

In the world of AI Agents, waiting is the enemy. If an agent waits for one API call to finish before starting the next (synchronous execution), it becomes slow and unresponsive. This challenge focuses on using Python's `asyncio` library to perform non-blocking operations, allowing the agent to "multitask" while waiting for input/output (I/O) operations.

## 🛠️ Tech Stack

* **Python 3.10+**
* **`asyncio`** - The standard library for writing concurrent code using the async/await syntax.
* **`aiohttp`** - An asynchronous HTTP client/server framework (essential for non-blocking web requests).

## 📂 Solution Overview

The solution script (`day1.py`) implements the following:

1. **`fetch_url`** - An asynchronous function that sends a GET request to a specific URL and awaits the response without blocking the main thread.
2. **`main`** - The entry point that orchestrates the creation of multiple tasks (one for each URL).
3. **`asyncio.gather`** - A method to run all fetch tasks concurrently and collect their results once all are finished.

## 🏃‍♂️ How to Run

1. **Install Dependencies:**
    Ensure you have `aiohttp` installed.

    ```bash
    pip install aiohttp
    ```

2. **Run the Script:**

    ```bash
    python day1.py
    ```

3. **Expected Output:**
    You should see logs indicating that fetch requests are starting almost simultaneously, followed by the results as they complete (likely out of order, demonstrating concurrency).

    ```text
    Starting concurrent fetch
    Starting fetch https://python.org
    Starting fetch https://google.com
    Starting fetch https://github.com
    Fetched: https://github.com (Status: 200)
    ...
    ```

## 🧠 Key Learnings

* **Async vs. Sync -** Synchronous code blocks the execution flow until a task finishes. Asynchronous code allows the program to handle other tasks while waiting for long operations (like network requests) to complete.
* **The Event Loop -** `asyncio` relies on an event loop to manage and switch between tasks.
* **Agent Application -** This pattern is crucial for agents that need to query multiple tools, search engines or databases simultaneously to answer a user query quickly.

---
[Back to Main Repo](../README.md)
