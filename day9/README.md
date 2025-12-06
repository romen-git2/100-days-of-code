# Day 9 - Data Pipelines (ETL) with Pandas

**Phase 1 -** Advanced Python & Agent Tools

## 📝 The Challenge

**Goal -** Ingest, transform and output agent data to JSON.

AI Agents are sensitive to the quality of the data they consume ("Garbage In, Garbage Out"). If you feed an agent raw logs containing missing timestamps, failed requests or unstructured text, it will struggle to perform accurately. This challenge focuses on building an **ETL (Extract, Transform, Load)** pipeline, the backbone of any production data system to automate the cleaning and structuring of data before it reaches the agent.

## 🛠️ Tech Stack

* **Python 3.10+**
* **`pandas`** - The primary tool for data manipulation. It handles the "Transform" phase by filtering, sorting and cleaning the raw input.
* **`json`** - Used for the "Load" phase to save the cleaned data in a format that LLMs and web APIs can easily digest.

## 📂 Solution Overview

The solution script (`day9.py`) implements a functional pipeline:

1. **Extract** - Reads raw simulation data from a CSV file (`raw_agent_logs.csv`).
2. **Transform**:
    * **Data Cleaning** - Removes rows with missing timestamps using `dropna`.
    * **Quality Filter** - Discards failed sessions (`status != 'complete'`) and low-quality responses (`score < 0.5`).
    * **Normalization** - Converts string timestamps into proper Python `datetime` objects.
3. **Load** - Exports the refined dataset to `clean_agent_context.json` using the `orient='records'` format, which produces a clean list of JSON objects ideal for agent context windows.

## 🏃‍♂️ How to Run

1. **Install Dependencies:**

    ```bash
    pip install pandas
    ```

2. **Run the Script:**

    ```bash
    python day9.py
    ```

3. **Expected Output:**
    The script will log each step of the pipeline and generate a JSON file.

    ```text
    Created source file raw_agent_logs.csv
    Loading data from raw_agent_logs.csv...
    Loaded 5 rows.
    Cleaning data...
    Dropped 1 rows with missing timestamps.
    Filtered down to 3 high quality interactions.
    Saving to clean_agent_context.json...
    Data pipeline completed.
    ```

## 🧠 Key Learnings

* **Garbage In, Garbage Out -** A simple drop of bad data (like failed API calls) can significantly improve an agent's success rate compared to trying to "reason" through the errors.
* **Modular Design -** Separating `extract()`, `transform()` and `load()` functions makes the code testable and easy to maintain.
* **LLM-Ready Formats -** Saving data as a list of JSON records (`[{"key": "value"}, ...]`) is the standard format for constructing few-shot examples or context for Large Language Models.

---
[Back to Main Repo](../README.md)
