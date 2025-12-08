# 100 Days of Code - Building AI Agents

![Progress](https://img.shields.io/badge/Progress-11%2F100-brightgreen) ![Python](https://img.shields.io/badge/Python-3.10%2B-blue) ![Focus](https://img.shields.io/badge/Focus-AI%20Agents-orange)

This repository documents my journey through the **100 Days of Code** challenge, specifically focused on **Advanced Python, Agentic AI and Large Language Model (LLM) Orchestration**.

The curriculum follows a specialized roadmap covering everything from async Python basics to deploying multi-agent swarms on Kubernetes.

## 📚 Curriculum Overview

The challenge is divided into 7 key phases:

* **Phase 1 -** Advanced Python & Agent Tools (Days 1-10)
* **Phase 2 -** Agent Design Patterns & Integrations (Days 11-30)
* **Phase 3 -** Agent Framework Foundations (LangChain, AutoGen) (Days 31-50)
* **Phase 4 -** Advanced Frameworks & Multi-Agent Systems (Days 51-70)
* **Phase 5 -** MLOps & Deployment for Agents (Days 71-85)
* **Phase 6 -** Advanced Agentic Systems (Memory, Ethics, Planning) (Days 86-95)
* **Phase 7 -** Capstone & Optimization (Days 96-100)

---

## 🛠️ Daily Log

### Phase 1 - Advanced Python & Agent Tools

| Day | Topic | Challenge | Status | Links |
| :--- | :--- | :--- | :--- | :--- |
| **01** | Async Python | Async URL Fetcher with `asyncio` | ✅ | [Code](./day1/day1.py) |
| **02** | NumPy & Pandas | Agent Observation Data Processing | ✅ | [Code](./day2/day2.py) |
| **03** | Visualization | Matplotlib for Agent State Logging | ✅ | [Code](./day3/day3.py) |
| **04** | Web Scraping | Extracting Data with BeautifulSoup | ✅ | [Code](./day4/day4.py) |
| **05** | API Calls | Tool Integration via `requests` | ✅ | [Code](./day5/day5.py) |
| **06** | Error Handling | Custom Exceptions & Logging | ✅ | [Code](./day6/day6.py) |
| **07** | Parallel Processing | Dask for Agent Simulations | ✅ | [Code](./day7/day7.py) |
| **08** | OOP Patterns | Strategy Pattern for Decisions | ✅ | [Code](./day8/day8.py) |
| **09** | Data Pipeline | ETL with Pandas | ✅ | [Code](./day9/day9.py) |
| **10** | Unit Testing | Pytest for Agent Components | ✅ | [Code](./day10/test_agent.py) |

### Phase 2 - Agent Design Patterns & Integrations

| Day | Topic | Challenge | Status | Links |
| :--- | :--- | :--- | :--- | :--- |
| **11** | Factory Pattern | Factory function to instantiate agent types | ✅ | [Code](./day11/day11.py) |
| **12** | Singleton | Implement a singleton for config loading | ⬜ |  |
| **13** | Observer | Set up observer for state changes | ⬜ |  |
| **14** | Decorator | Decorate a function to add timing logs | ⬜ |  |
| **15** | Command | Create executable command objects | ⬜ |  |
| **16** | Adapter | Adapt a third-party API to agent interface | ⬜ |  |
| **17** | Facade | Facade class for multiple service calls | ⬜ |  |
| **18** | Apply patterns | Use factory, observer and decorator together | ⬜ |  |
| **19** | Pattern toolkit | Build a module with 2-3 patterns | ⬜ |  |
| **20** | OAuth integration | Authenticate and call a OAuth-protected endpoint | ⬜ |  |
| **21** | Webhooks | Set up a local server to receive webhook | ⬜ |  |
| **22** | SQL storage: SQLite | Create table and insert agent states | ⬜ |  |
| **23** | MongoDB | Insert and query JSON-like agent logs | ⬜ |  |
| **24** | Redis caching | Cache and retrieve a key-value pair | ⬜ |  |
| **25** | RabbitMQ queues | Send and receive a message in a queue | ⬜ |  |
| **26** | Integrated tool: API + DB combo | Fetch data via API and store in DB | ⬜ |  |
| **27** | API chaining | Chain two APIs with error handling | ⬜ |  |
| **28** | Input validation | Validate and clean agent inputs | ⬜ |  |
| **29** | Structured logging | Log agent events to file | ⬜ |  |
| **30** | Metrics tracking | Track and report agent uptime | ⬜ |  |

---

## 🧠 Key Learnings & Reflections

* **Day 1 -** Learned that `asyncio` is critical for agents to perform non-blocking operations (like waiting for LLM tokens or API responses).
* **Day 2 -** Realized that filtering data effectively before an agent can make decisions based on history.
* **Day 3 -** Discovered that visualizing agent states (via Matplotlib) is essential for debugging "black box" behavior, allowing for quick identification of learning plateaus or erratic actions.
* **Day 4 -** Understood that LLMs are "frozen in time," so mastering web scraping (BeautifulSoup) is crucial for giving agents real-time context and access to live data sources.
* **Day 5 -** Learned that unlike scraping, APIs provide structured JSON data that is safer and more reliable for agents to parse and act upon.
* **Day 6 -** Recognized that robust agents require custom exception handling (try-except blocks) and structured logging to survive API failures and recover without crashing.
* **Day 7 -** Distinguished between concurrency (waiting) and parallelism (doing). Learned that parallel processing is essential for scaling agent simulations and running efficient batch evaluations across multiple CPU cores.
* **Day 8 -** Implemented the Strategy Pattern to decouple decision logic, allowing agents to dynamically switch between different problem-solving methods (like "fast keyword search" vs. "complex reasoning") at runtime.
* **Day 9 -** Built an ETL pipeline (Extract, Transform, Load) to sanitize messy input logs. Realized that agents need clean, structured data (like JSON records) to function reliably, reinforcing the "Garbage In, Garbage Out" principle.
* **Day 10 -** Validated that while LLM outputs vary, the underlying tool logic must be deterministic. Unit testing (Pytest) prevents regressions, ensuring that changes to the agent's code don't silently break its ability to parse commands or calculate results.
* **Day 11 -** Implemented the Factory Pattern to centralize the creation of specialized agents. Realized this pattern is crucial for multi-agent swarms, allowing a Manager agent to spawn specific sub-agents (Coder, Researcher) dynamically without knowing the complex construction details, ensuring high decoupling and scalability.

---

## 💻 Tech Stack

* **Languages -** Python
* **Libraries -** `asyncio`, `pandas`, `numpy`, `aiohttp`, `matplotlib`, `beautifulsoup4`, `requests`, `dask`, `pytest` (so far)
* **Frameworks (Upcoming) -** LangChain, AutoGen, LangGraph

## 🏃‍♂️ How to Run

1. Clone the repo:

    ```bash
    git clone https://github.com/romen-git2/100-days-of-code.git
    ```

2. Locate README.md of specific day for instructions:

    | Day | README.md links |
    | :--- | :--- |
    | **01** | [Code](./day1/README.md) |
    | **02** | [Code](./day2/README.md) |
    | **03** | [Code](./day3/README.md) |
    | **04** | [Code](./day4/README.md) |
    | **05** | [Code](./day5/README.md) |
    | **06** | [Code](./day6/README.md) |
    | **07** | [Code](./day7/README.md) |
    | **08** | [Code](./day8/README.md) |
    | **09** | [Code](./day9/README.md) |
    | **10** | [Code](./day10/README.md) |
    | **11** | [Code](./day11/README.md) |

---
*Connect with me on [LinkedIn](https://www.linkedin.com/in/romen-ranasingha) to follow my daily updates!*
