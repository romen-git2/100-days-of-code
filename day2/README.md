# Day 2 - NumPy & Pandas for Agent Data

**Phase 1 -** Advanced Python & Agent Tools

## 📝 The Challenge

**Goal -** Load and filter a CSV for agent input simulation.

AI Agents constantly receive "observations" from their environment—logs, sensor data, API responses or user interaction histories. This challenge focuses on using **Pandas** to structure raw data and **NumPy** to perform fast numerical analysis, simulating how an agent "remembers" past actions to decide what works best.

## 🛠️ Tech Stack

* **Python 3.10+**
* **`pandas`** - The industry standard for data manipulation and analysis (DataFrames).
* **`numpy`** - The fundamental package for scientific computing (used here for statistical calculations).

## 📂 Solution Overview

The solution script (`day2.py`) performs the following steps:

1. **Data Simulation** - Generates a dummy `agent_logs.csv` file containing mock data (Agent Actions, Reward Scores, Success/Fail Status).
2. **Ingestion** - Uses `pd.read_csv()` to load the raw text log into a structured DataFrame.
3. **Filtration** - Applies Boolean Indexing to filter out data (failed attempts or low-reward actions), isolating high-value memories.
4. **Analysis** - Uses NumPy (`np.mean`) to calculate statistics on the filtered data to inform future agent behavior.

## 🏃‍♂️ How to Run

1. **Install Dependencies:**

    ```bash
    pip install pandas numpy
    ```

2. **Run the Script:**

    ```bash
    python day2.py
    ```

3. **Expected Output:**
    The script will generate a CSV file, print the filtered DataFrame of successful high-reward actions and calculate the average reward score.

    ```text
    agent_logs.csv created

    Loading agent data...

    High value actions(filtered data):
       step_id agent_action  reward_score   status
    2        3        click           0.5  success
    4        5        click           0.6  success
    5        6          buy           5.0  success
    7        8          buy           4.8  success
    8        9        click           0.4  success
    Average reward of high value actions: 2.26
    Most successful action type: click
    ```

## 🧠 Key Learnings

* **Data Cleaning -** Before an agent can learn, it must filter out irrelevant data (e.g., errors or timeouts).
* **Vectorization -** Using Pandas and NumPy is significantly faster and more readable than writing Python `for` loops to process lists of data.

---
[Back to Main Repo](../README.md)
