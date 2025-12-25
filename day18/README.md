# Day 18 - Pattern Integration Challenge

**Phase 2 -** Agent Design Patterns & Integrations

## 📝 The Challenge

**Goal -** Combine the **Factory**, **Observer** and **Decorator** patterns into a single cohesive system.

In professional software architecture, design patterns rarely exist in isolation. They work together to solve different aspects of a problem (Creation, Behavior and Structure).

This challenge involves building a **Sensor Monitoring System** where:
1.**Factory Pattern -** Handles the creation of different sensor types (Temperature, Pressure).
2.**Decorator Pattern -** Wraps the sensor readings to automatically log usage data without cluttering the business logic.
3.**Observer Pattern -** Monitors the sensor values and triggers an **Alarm** if readings exceed a critical threshold.

## 🛠️ Tech Stack

* **Python 3.10+**
* **`abc`** - For defining abstract base classes (`Sensor`, `Observer`).
* **`functools.wraps`** - For creating the logging decorator.

## 📂 Solution Overview

The solution script (`day18.py`) integrates the patterns as follows:

### 1. The Factory (`SensorFactory`)

* **Role -** Centralizes object creation.
* **Why -** The client code doesn't need to know the specific class names (`TemperatureSensor`, `PressureSensor`). It just asks the factory for a temp or pressure sensor.

### 2. The Decorator (`@log_reading`)

* **Role -** Adds logging behavior to the `read_value()` method.
* **Why -** We can add logging to *any* sensor type simply by adding the `@` tag, keeping the sensor's core math logic pure.

### 3. The Observer (`AlarmSystem`)

* **Role -** Watches for state changes.
* **Why -** The sensor doesn't need to know *what* happens when a value is high. It just notifies the observers. This allows us to easily add an `EmailAlertSystem` later without touching the sensor code.

## 🏃‍♂️ How to Run

1. **Run the Script:**

    ```bash
    python day18.py
    ```

2. **Expected Output:**
    You will see the Factory create sensors, the Decorator log the attempt to read data and the Observer trigger an alert if the random value is high.

    ```text
    Initializing System(Factory)
    Running Sensors(Decorator + Observer)
    Reading data from Core Temp...
    Value: 29.96
    Reading data from Hydraulic Press...
    Hydraulic Press is CRITICAL! Value: 80.22
    Value: 80.22
    Reading data from Core Temp...
    Value: 28.87
    Reading data from Hydraulic Press...
    Value: 61.15
    Reading data from Core Temp...
    Value: 31.64
    Reading data from Hydraulic Press...
    Hydraulic Press is CRITICAL! Value: 80.83
    Value: 80.83
    ```

## 🧠 Key Learnings

* **Synergy:** Patterns are more powerful when combined. The **Factory** manages the lifecycle, the **Decorator** manages cross-cutting concerns (logging) and the **Observer** manages event reactions.
* **Scalability:**
* Want a new sensor? Add a class and update the Factory.
* Want to log to a file instead of print? Update the Decorator.
* Want to send SMS alerts? Add a new Observer.
* **Clean Architecture:** Despite having complex behavior (creation, logging, alerting), the main execution block remains incredibly simple and readable.

---
[Back to Main Repo](../README.md)
