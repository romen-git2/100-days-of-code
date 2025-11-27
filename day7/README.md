# Day 7 - Parallel Processing with Dask

**Phase 1 -** Advanced Python & Agent Tools

## 📝 The Challenge

**Goal -** Parallelize a loop over 100 mock agent tasks.

As moving from building a single agent to "Multi-Agent Systems" or "Swarm Intelligence", performance becomes a bottleneck. If requirement is to test an agent's decision-making on 100 different scenarios, running them one by one (serially) is incredibly slow. This challenge uses **Dask** to perform **Parallel Processing**, allowing to utilize every core of CPU to run multiple agent simulations simultaneously.

## 🛠️ Tech Stack

* **Python 3.10+**
* **`dask`** - A flexible library for parallel computing in Python. It mimics the Pandas/NumPy API but extends it to work across multiple cores or even clusters.

## 📂 Solution Overview

The solution script (`day7.py`) demonstrates the difference between Serial vs. Parallel execution:

1. **Mock Task** - Defines a function `runAgentSimulation` that sleeps for a random time (0.5 - 1.5s) to simulate an agent "thinking" or processing data.
2. **Lazy Evaluation** - Uses `dask.delayed` to wrap the function calls. This doesn't run them immediately, instead it builds a "Task Graph" of work to be done.
3. **Parallel Execution** - Uses `dask.compute()` to trigger the execution. Dask automatically assigns the tasks to available CPU cores.
4. **Performance Check** - Calculates the speedup factor (Time Serial / Time Parallel) to prove the efficiency gain.

## 🏃‍♂️ How to Run

1. **Install Dependencies:**

    ```bash
    pip install "dask[complete]"
    ```

2. **Run the Script:**

    ```bash
    python day7.py
    ```

3. **Expected Output:**
    You will see a comparison showing how much faster the parallel execution is.

    ```text
    Starting simulation for 100 agents
    Tasks scheduled. computing now...
    Simulation complete
    Total time taken: 19.61 seconds
    Time if run serially: 100.05 seconds
    Speedup: 5.1x
    ```

    *(Note - Exact speedup depends on the number of cores in CPU.)*

## 🧠 Key Learnings

* **Parallelism vs. Concurrency -** * **Day 1 (Asyncio)** was about *Concurrency* (waiting efficiently for I/O like APIs). **Day 7 (Dask)** is about *Parallelism* (using extra CPU muscle to do heavy calculations or simulations faster).
* **Scaling -** This pattern is essential when you need to run "Evals" (evaluations) on your agents-testing them against hundreds of test cases to ensure they are working correctly.
* **Lazy Evaluation -** Dask doesn't work until you tell it to (`compute()`). This allows it to optimize the workflow before executing.

---
[Back to Main Repo](../README.md)
