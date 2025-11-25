# Day 6 - Error Handling & Logging

**Phase 1 -** Advanced Python & Agent Tools

## 📝 The Challenge

**Goal -** Wrap an API call with `try-except` blocks and implement custom logging.

In the real world, APIs fail. Servers go down, rate limits are hit and internet connections drop. An AI agent that crashes at the first sign of trouble is not "autonomous." This challenge focuses on building resilience - teaching the agent to anticipate failure, log exactly what went wrong (for debugging) and attempt to recover (retries) instead of crashing.

## 🛠️ Tech Stack

* **Python 3.10+**
* **`logging`** - Python's standard library for tracking events. It is far superior to `print()` for production systems because it supports log levels (INFO, ERROR, CRITICAL) and file outputs.
* **`random` & `time`** - Used here to simulate an unstable environment and manage retry delays.

## 📂 Solution Overview

The solution script (`day6.py`) simulates a fragile agent environment:

1. **Logging Configuration** - Sets up a logger that writes to both the console and a file named `agentRuntime.log` (for long-term storage).
2. **Custom Exceptions** - Defines specific error types like `AgentRateLimitError`. This allows the agent to react differently to a "wait and try again" problem versus a "fatal crash" problem.
3. **Unstable Simulation** - A mock function `unstableAPICall()` that randomly succeeds, fails or times out.
4. **Robust Wrapper** - A main execution loop that:
    * **Retries** the operation up to 3 times.
    * **Catches** specific errors.
    * **Backs off** (sleeps) if a rate limit is hit.
    * **Escalates** critical errors if retries fail.

## 🏃‍♂️ How to Run

1. **Install Dependencies:**
    No external libraries are needed (uses Python Standard Library).

2. **Run the Script:**

    ```bash
    python day6.py
    ```

3. **Expected Output:**
    Because the API uses `random`, output will vary every time. You might see a success on the first try or a series of retries.

    *Example of a retry scenario:*

    ```text
    2025-11-25 23:14:44,468 - INFO - Agent starting task execution...
    2025-11-25 23:14:44,469 - INFO - Attempt 1/3 Calling API...
    2025-11-25 23:14:44,470 - ERROR - Network issue: Failed to connect to server.. Retrying immediately...
    2025-11-25 23:14:44,470 - INFO - Attempt 2/3 Calling API...
    2025-11-25 23:14:44,471 - ERROR - Network issue: Failed to connect to server.. Retrying immediately...
    2025-11-25 23:14:44,472 - INFO - Attempt 3/3 Calling API...
    2025-11-25 23:14:44,472 - INFO - Success! Result: Agent obtained data!
    ```

4. **Check the Log File:**
    Open `agentRuntime.log` in the same directory to see the permanent record of the agent's attempt.

## 🧠 Key Learnings

* **Logging > Print -** `print` is temporary, logs are permanent. When an agent crashes overnight, the log file is the only evidence you have to figure out why.
* **Granular Handling -** Don't just use `except Exception`. Catching specific errors (like `ConnectionError`) allows the agent to be smart (e.g., "I should retry") rather than just giving up.
* **Graceful Degradation -** Even if the agent fails completely, it should exit cleanly and alert the user, rather than throwing a raw Python stack trace.

---
[Back to Main Repo](../README.md)
