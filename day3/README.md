# Day 3 - Visualization with Matplotlib

**Phase 1 -** Advanced Python & Agent Tools

## 📝 The Challenge

**Goal -** Plot a simple time-series of agent actions.

AI Agents often operate as "black boxes." You give them a task and they execute it - but how do you know if they are improving or stuck in a loop? Visualizing internal states (like reward accumulation, confidence scores or resource usage) is critical for debugging and optimizing agent performance. This challenge uses **Matplotlib** to create a visual log of an agent's learning curve.

## 🛠️ Tech Stack

* **Python 3.10+**
* **`matplotlib`** - The most widely used Python library for creating static, animated and interactive visualizations.

## 📂 Solution Overview

The solution script (`day3.py`) performs the following:

1. **Simulation** - Runs a mock agent for 20 steps. At each step, it assigns a random reward (positive or negative) and logs the action taken ("Explore" vs. "Exploit").
2. **Metric Calculation** - Tracks the **Cumulative Reward** (total score over time), which is a standard metric in Reinforcement Learning to gauge progress.
3. **Visualization**
    * Plots **Step Number (X)** vs. **Cumulative Reward (Y)**.
    * Adds a baseline (y=0) to easily spot when the agent is underperforming.
4. **Export** - Saves the chart as `agent_performance_chart.png`, simulating logging visual artifacts from a headless server.

## 🏃‍♂️ How to Run

1. **Install Dependencies:**

    ```bash
    pip install matplotlib
    ```

2. **Run the Script:**

    ```bash
    python day3.py
    ```

3. **Expected Output:**
    * The script will print - `Chart saved as 'agent_performance_chart.png`.
    * A file named `agent_performance_chart.png` will appear in the directory.
    * If running locally with a display, a window will pop up showing a blue line chart tracking the agent's score over 20 steps.

## 🧠 Key Learnings

* **Visual Debugging -** A downward trend in a reward plot is often the fastest way to spot a bug in an agent's logic.
* **Headless Logging -** Agents often run in cloud containers (Docker/Kubernetes) where there is no screen. Saving plots to disk (`plt.savefig`) allows you to review performance later.
* **Time-Series Data -** Agent behaviors are sequential. Plotting them linearly helps identify patterns like "thrashing" (rapidly switching between actions) or "plateauing" (stop learning).

---
[Back to Main Repo](../README.md)
