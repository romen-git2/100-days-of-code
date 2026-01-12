# Day 29 - Structured Logging(Observability)

**Phase 2 -** Agent Design Patterns & Integrations

## 📝 The Challenge

**Goal -** Replace standard text based logging(`print()`) with production grade **Structured JSON Logging**.

In a production environment with multiple agents running in parallel, simple text logs like `Error: failed to connect` are useless. You cannot query them, you cannot graph them and you cannot easily associate an error with a specific user or request ID.

We built a **Network Monitor Agent** that outputs machine readable JSON. This allows tools like Datadog, Splunk or ELK Stack to ingest the logs and answer questions like *"What was the average latency for the GitHub API over the last hour?"*

## 🛠️ Tech Stack

* **Python 3.10+**
* **`logging` -** Python's standard library(customized).
* **`json` -** For serializing log records.
* **`uuid` -** For generating unique Trace IDs per request.
* **`requests` -** To generate network traffic and errors.

## 📂 Solution Overview

We implemented a **Custom Log Formatter**(`StructuredFormatter`) that intercepts every log call and converts it into a JSON object.

### The Context Injection Pattern

Instead of formatting strings like this:

```python
# Bad: Hard to parse programmatically
logger.info(f"Request to {url} took {duration}ms")
```

We pass raw data in a `context` dictionary:

```python
# Good: Machine readable
logger.info("Request finished", extra={"context": {
    "url": url, 
    "latency_ms": duration, 
    "status": 200
}})
```

The formatter then automatically outputs:

```json
{
  "timestamp": "2023-10-29...", 
  "message": "Request finished", 
  "url": "https://api.github.com", 
  "latency_ms": 120, 
  "status": 200
}
```

## 🏃‍♂️ How to Run

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. **Run the Logger Agent**

```bash
python day29.py
```

### 3. **Observe the Output**

The script will audit 3 URLs(Success, High Latency and Failure). Watch the console for JSON output.

### 4. **Check the Log File**

The agent also writes to `agent_audit.jsonl`. This file acts as a permanent Flight Recorder.

## 🧠 Key Learnings

* **Trace IDs -** Generating a random UUID (`trace_id`) at the start of a task and attaching it to every log allows to filter thousands of logs down to the specific events of *one single request*.
* **Logs vs. Metrics -** Logs shouldn't just be text, they should contain numbers (`latency_ms`, `content_size`). This turns logs into a data source for performance monitoring.
* **Machine Readability -** Debugging is faster when I don't have to read text. I can just filter by `level="ERROR"` or `status_code!=200`.

---
[Back to Main Repo](../README.md)
