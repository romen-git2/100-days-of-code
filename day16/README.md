# Day 16 - The Adapter Pattern

**Phase 2 -** Agent Design Patterns & Integrations

## 📝 The Challenge

**Goal -** Adapt a third-party API class to match agent's standard tool interface.

In a robust Agent Framework, the agent typically expects all its tools to follow a strict interface (e.g., every tool must have a `.execute(query)` method). However, in the real world, useful libraries and APIs come with their own unique method names and parameters (e.g., `.fetch_data()`, `.get()`, `.connect()`).

This challenge uses the **Adapter Pattern** to build a bridge. We will create a wrapper class that translates the agent's standard calls into the specific calls required by a Legacy or third-party library, allowing the agent to use it without changing its core logic.

## 🛠️ Tech Stack

* **Python 3.10+**
* **`abc` (Abstract Base Classes)** - Used to define the target interface (`AgentTool`) that the adapter must implement.

## 📂 Solution Overview

The solution script (`day16.py`) implements the pattern in three parts:

1. **The Target Interface (`AgentTool`)**:
    * This is the standard interface the agent understands. It enforces a single method - `execute(query: str)`.
2. **The Adaptee (`LegacyWeatherAPI`)**:
    * Simulates a third-party library or old code.
    * Has an incompatible interface - `get_temperature_city(city_name, unit)`.
3. **The Adapter (`WeatherToolAdapter`)**:
    * Implements `AgentTool` (so the agent accepts it).
    * Accepts an instance of `LegacyWeatherAPI` in its constructor.
    * **Translates** the agent's generic `execute("Paris")` call into the specific `get_temperature_city("Paris", unit="C")` call.

## 🏃‍♂️ How to Run

1. **Install Dependencies:**
    No external libraries are needed.

2. **Run the Script:**

    ```bash
    python day16.py
    ```

3. **Expected Output:**
    You will see the Adapter translating the request behind the scenes. The Agent code remains clean and unaware of the legacy API's complexity.

    ```text
    Agent is invoking tool with: Paris
    Translating query 'Paris' to legacy format...
    Connecting to old weather satellite for Paris...
    Result: It is 15.5°C in Paris.
    Agent is invoking tool with: New York
    Translating query 'New York' to legacy format...
    Connecting to old weather satellite for New York...
    Result: It is 22.0°C in New York.
    ```

## 🧠 Key Learnings

* **Interface Consistency -** The Agent execution loop stays simple (`tool.execute()`) regardless of what complex APIs are running in the background.
* **Open/Closed Principle -** You can extend the agent's capabilities (by adding new adapters for new libraries) without modifying the agent's existing source code.
* **Translation Layer -** Adapters don't just pass calls through, they often convert data formats (e.g., string query -> specific arguments) to make the pieces fit together.

---
[Back to Main Repo](../README.md)
