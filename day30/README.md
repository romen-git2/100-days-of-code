# Day 30 - Metrics Tracking & Health Monitoring(The Pulse)

**Phase 2 Completion -** Agent Design Patterns & Integrations

## 📝 The Challenge

**Goal -** Implement a self monitoring system that tracks an agent's performance trends, uptime and success rates in real-time.

While **Logging(Day 29)** tells us *what* happened in the past, **Metrics** tell us the *current health* of the system. In production, an agent might still be running(not crashing) but could be performing poorly due to high network latency or a 50% failure rate. Without a metrics layer, these silent degradations go unnoticed.

We built a **Live Watchdog Agent**. It pings real-world services to calculate moving averages, jitter and availability, allowing the agent to self diagnose its status as `HEALTHY`, `DEGRADED`, or `CRITICAL`.

## 🛠️ Tech Stack

* **Python 3.10+**
* **`requests` -** To generate network traffic.
* **`dataclasses` -** For structured, memory efficient metrics storage.
* **`statistics` -** To calculate averages and performance trends.

## 📂 Solution Overview

We implemented a **Heartbeat Mechanism** that separates data collection from data interpretation:

1. **Metric Aggregation -** Instead of looking at a single request, the agent stores a window of recent latencies.
2. **Derived Statistics -** We calculate the **Success Rate** and **Average Latency** dynamically.
3. **Threshold Logic -** The agent uses Health Rules. For example, if the average latency exceeds 300ms, the agent flags itself as Degraded, even if no hard errors have occurred yet.

## 🏃‍♂️ How to Run

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. **Run the Health Monitor**

```bash
python day30.py
```

### 3. **Observe the Dashboard**

The agent will perform 5 real pings to Google and then output a final Health Report.

```text
Starting Monitor on https://www.google.com...
[1/5] Ping: 200 | Latency: 553.7ms
[2/5] Ping: 200 | Latency: 92.4ms
[3/5] Ping: 200 | Latency: 250.0ms
[4/5] Ping: 200 | Latency: 248.9ms
[5/5] Ping: 200 | Latency: 97.0ms
Target:       https://www.google.com
Status:       HEALTHY
Total Pings:  5
Success Rate: 100.0%
Latency:      Avg: 248.4ms | Max: 553.65ms
Time Elapsed: 3.75s
```

## 🧠 Key Learnings

* **Metrics vs. Logs -** Logs are for debugging specific events, metrics are for understanding system capacity and stability over time.
* **The Keep-Alive Insight -** By monitoring pings, observed how latency drops after the first request due to TCP connection reuse, a detail only visible through structured metrics.
* **Automated Alerting -** Learned how to turn raw numbers into Actionable Intelligence. By setting thresholds on `success_rate`, the agent can now trigger its own recovery protocols.

---
[Back to Main Repo](../README.md)
