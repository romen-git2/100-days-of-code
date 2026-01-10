# Day 28 - Input Validation & Data Sanitization

**Phase 2 -** Agent Design Patterns & Integrations

## 📝 The Challenge

**Goal -** Implement a strict validation layer using **Pydantic** to protect the agent from "Garbage In, Garbage Out"(GIGO).

In a production environment, agents interact with unpredictable inputs, whether from messy public APIs, LLM hallucinations or user typos. If an agent expects a floating point coordinate but receives a string like `"unknown"`, the system crashes.

Today, we built a **Data Guardian**. We fetch user data from an external API and use Pydantic to **Parse, Clean and Validate** it before it ever reaches our business logic.

## 🛠️ Tech Stack

* **Python 3.10+**
* **`Pydantic V2` -** The industry standard for data validation and settings management.
* **`requests` -** For fetching real-world external data.
* **`email-validator` -** (Optional dependency for Pydantic) to ensure email strings are RFC compliant.

## 📂 Solution Overview

We implemented a **Schema-First** approach to data handling:

1. **Type Coercion -** The API returns coordinates as strings (e.g., `"lat": "-37.3159"`). Pydantic automatically casts these into Python `float` types.
2. **Custom Sanitization -** We used `@field_validator` to intercept messy data. For example, if an API returns a website without a protocol (`hildegard.org`), validator automatically prepends `http://`.
3. **Boundary Checks -** We enforced physical constraints(e.g., Latitude must be between -90 and 90) to ensure the data is geographically logical.
4. **Nested Modeling -** Created a complex schema where a `UserProfile` model contains a nested `GeoCoordinates` model, mirroring real-world JSON structures.

## 🏃‍♂️ How to Run

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. **Run the Guardian**

```bash
python day28.py
```

### 3. **Observe the Validation**

The script will fetch 10 users. For each user, you will see the Bouncer in action:

* **Validating** types.
* **Cleaning** URL formats.
* **Rejecting** any malformed records.

```text
Fetching data from https://jsonplaceholder.typicode.com/users...
Received 10 raw records.
Starting Validation Layer...
Valid: Leanne Graham        | Web: http://hildegard.org | Lat: -37.3159
Valid: Ervin Howell         | Web: http://anastasia.net | Lat: -43.9509
Valid: Clementine Bauch     | Web: http://ramiro.info | Lat: -68.6102
Valid: Patricia Lebsack     | Web: http://kale.biz | Lat: 29.4572
Valid: Chelsey Dietrich     | Web: http://demarco.info | Lat: -31.8129
Valid: Mrs. Dennis Schulist | Web: http://ola.org | Lat: -71.4197
Valid: Kurtis Weissnat      | Web: http://elvis.io | Lat: 24.8918
Valid: Nicholas Runolfsdottir V | Web: http://jacynthe.com | Lat: -14.399
Valid: Glenna Reichert      | Web: http://conrad.com | Lat: 24.6463
Valid: Clementina DuBuque   | Web: http://ambrose.net | Lat: -38.2386
Success. 10/10 records cleaned and imported.
```

## 🧠 Key Learnings

* **Fail-Fast Architecture -** It is significantly cheaper to reject bad data at the entry point than to debug a Silent Failure deep inside a database or LLM chain.
* **Declarative vs. Imperative -** Instead of writing dozens of if/else statements to check data types, defined a Model. This makes the code self-documenting and much easier to maintain.
* **Data Sanitization -** Validation isn't just about saying "No". It's about fixing what is fixable(like adding missing http:// prefixes) to make the agent more resilient to minor external errors.

---
[Back to Main Repo](../README.md)
