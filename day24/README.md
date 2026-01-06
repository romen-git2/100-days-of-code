# Day 24 - High Speed Caching with Redis

**Phase 2 -** Agent Design Patterns & Integrations

## 📝 The Challenge

**Goal -** Implement a high performance **Caching Layer** to optimize agent response times and reduce API costs.

In a production environment, AI agents often face two major bottlenecks:

1. **Latency -** Calls to LLMs (like GPT-4) or external APIs take time (often 1-5 seconds) to traverse the network and process.
2. **Cost -** Every API call costs money. Asking the exact same question twice shouldn't cost double.

To solve this, we use **Redis** (Remote Dictionary Server), an in-memory data store that acts as a short term Brain RAM for the agent.

## 🛠️ Tech Stack

* **Python 3.10+**
* **Redis -** An open-source, in-memory key-value store.
* **`redis` -** The Python client for interacting with Redis.
* **`requests` -** Used to make *real* network calls to demonstrate actual latency reduction.

## 📂 Solution Overview

We implemented the **Cache-Aside Pattern**:

1. **Check Cache -** Before doing any work, the agent checks Redis using a unique key (hashed prompt).
2. **Cache Hit -** If data exists, return it instantly (Speed - approx. 0.003s).
3. **Cache Miss -** If data is missing, make the slow network call (Speed - approx. 2.00s +).
4. **Write Back -** Save the fresh result to Redis with a **TTL (Time To Live)** so it expires automatically after a set time (e.g., 60 seconds).

### The Test Subject

We query a real remote endpoint - `https://httpbin.org/delay/2`. This server forces a 2-second wait, simulating the actual processing time of a complex LLM query.

## 🏃‍♂️ How to Run

### 1. Prerequisites(Start Redis)

You need a running Redis instance.

* **Using Docker(Recommended):**

    ```bash
    docker run -d -p 6379:6379 redis
    ```

* **macOS (Homebrew):** `brew install redis && brew services start redis`
* **Windows:** Use WSL2 or the Docker method.

### 2. Install Dependencies

```bash
pip install redis requests
```

### 3. **Run the Script:**

```bash
python day24.py
```

### 4. **Observe the Results**

* **First Run(Cold) -** The script will hang for approx. 2.5 seconds while it fetches data from the internet.
* **Second Run(Warm) -** The result will appear instantly.
* **Third Run(After 60s) -** The cache expires and it fetches from the internet again.

## 🧠 Key Learnings

* **In-Memory Speed -** Accessing RAM (Redis) is orders of magnitude faster than accessing the Network (API).
* **TTL(Time-To-Live) -** Understood the importance of expiring old data. For an agent, Stock Prices should have a short TTL(seconds), while History Facts can have a long TTL(days).
* **Serialization -** Redis stores strings/bytes. Serialization Python Dictionaries to JSON strings before saving (json.dumps) and deserialization them when reading (json.loads).

---
[Back to Main Repo](../README.md)
