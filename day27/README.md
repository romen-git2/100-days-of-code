# Day 27 - API Chaining & Data Enrichment

**Phase 2 -** Agent Design Patterns & Integrations

## 📝 The Challenge

**Goal -** Create an agent workflow where the **Output** of one tool becomes the **Input** of another.

Single step agents are limited. Real world problem solving often requires investigation. For example, if you ask an agent "Is it raining where User X lives?", the agent cannot answer that with one query. It needs to:

1. **Look up** User X to find their location (City/Coordinates).
2. **Pass** those coordinates to a Weather Service.
3. **Synthesize** the answer.

This is called **API Chaining** and it is the fundamental logic behind Reasoning agents.

## 🛠️ Tech Stack

* **Python 3.10+**
* **`requests` -** For HTTP calls.
* **`dataclasses` -** To enforce type safety when passing data between steps.
* **API 1(Source) -** `JSONPlaceholder` (Mock User Data).
* **API 2(Enrichment) -** `Open-Meteo` (Real-time Weather Data).

## 📂 Solution Overview

We implemented a **Sequential Enrichment Chain**:

1. **Step 1(Source) -** The agent queries `jsonplaceholder.typicode.com` to get a user profile. It parses the JSON to find the nested `geo` coordinates.
2. **Transformation -** The agent converts string coordinates (e.g., `"-31.8"`) into floating point numbers required by the next API.
3. **Step 2(Enrichment) -** The agent queries `api.open-meteo.com` using those specific coordinates to get the current temperature and wind speed.
4. **Synthesis -** The agent combines the Name (from API 1) and the Weather (from API 2) into a single report.

## 🏃‍♂️ How to Run

### 1. No API Keys Needed

We specifically chose open APIs that do not require authentication tokens for this exercise.

### 2. Install Dependencies

```bash
pip install requests
```

### 3. **Run the Script**

```bash
python day27.py
```

### 4. **Observe the Workflow**

You will see the agent perform the handover of data between the two services:

```text
Starting Context Chain(Target: User 5)
Fetching profile for User ID: 5...
Found: Chelsey Dietrich living in Roscoeview(-31.8129, 62.5342)
Checking weather at -31.8129, 62.5342...
User: Chelsey Dietrich
Location: Roscoeview
Status: Currently experiencing 21.6°C with wind speeds of 24.3 km/h
```

## 🧠 Key Learnings

* **Dependency Chains -** Step 2 is strictly dependent on the success of Step 1. If the User API fails(404), the Weather API must never be called. This requires robust Fail-Fast error handling.
* **Data Transformation -** APIs rarely speak the same language. API 1 gave coordinates as Strings inside a nested JSON object, API 2 expected Floats as query parameters. The Agent's job is to act as the Adapter between these distinct interfaces.
* **Value Creation -** The final report contains information that didn't exist in either source alone.

---
[Back to Main Repo](../README.md)
