# 100 Days of Code - Building AI Agents

![Progress](https://img.shields.io/badge/Progress-21%2F100-brightgreen) ![Python](https://img.shields.io/badge/Python-3.10%2B-blue) ![Focus](https://img.shields.io/badge/Focus-AI%20Agents-orange)

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
| **12** | Singleton | Implement a singleton for config loading | ✅ | [Code](./day12/day12.py) |
| **13** | Observer | Set up observer for state changes | ✅ | [Code](./day13/day13.py) |
| **14** | Decorator | Decorate a function to add timing logs | ✅ | [Code](./day14/day14.py) |
| **15** | Command | Create executable command objects | ✅ | [Code](./day15/day15.py) |
| **16** | Adapter | Adapt a third-party API to agent interface | ✅ | [Code](./day16/day16.py) |
| **17** | Facade | Facade class for multiple service calls | ✅ | [Code](./day17/day17.py) |
| **18** | Apply patterns | Use factory, observer and decorator together | ✅ | [Code](./day18/day18.py) |
| **19** | Pattern toolkit | Build a module with 2-3 patterns | ✅ | [Code](./day19/day19.py) |
| **20** | OAuth integration | Authenticate and call a OAuth-protected endpoint | ✅ | [Code](./day20/day20.py) |
| **21** | Webhooks | Set up a local server to receive webhook | ✅ | [Code](./day21/day21.py) |
| **22** | SQL storage: SQLite | Create table and insert agent states | ⬜ | |
| **23** | MongoDB | Insert and query JSON-like agent logs | ⬜ | |
| **24** | Redis caching | Cache and retrieve a key-value pair | ⬜ | |
| **25** | RabbitMQ queues | Send and receive a message in a queue | ⬜ | |
| **26** | Integrated tool: API + DB combo | Fetch data via API and store in DB | ⬜ | |
| **27** | API chaining | Chain two APIs with error handling | ⬜ | |
| **28** | Input validation | Validate and clean agent inputs | ⬜ | |
| **29** | Structured logging | Log agent events to file | ⬜ | |
| **30** | Metrics tracking | Track and report agent uptime | ⬜ | |

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
* **Day 12 -** Applied the Singleton Pattern to manage shared resources like configuration loaders. Understood that for heavy resources (database pools, global configs), enforcing a single instance prevents memory waste and synchronization errors in a multi-agent system.
* **Day 13 -** Implemented the Observer Pattern to enable real-time event broadcasting. By decoupling the agent (Subject) from its listeners (Loggers, Alerts), established an Event-Driven Architecture where the agent can simply "notify" changes without caring who is listening or how they handle the data.
* **Day 14 -** Mastered the Decorator Pattern to inject "middleware" logic (like timing, logging or retries) into agent functions. This allows for cleaner code by keeping business logic separate from operational concerns and enabling reusable behaviors across different tools.
* **Day 15 -** Implemented the Command Pattern to encapsulate agent actions as objects. This decoupling allows the agent to separate planning (building a queue of commands) from execution, enabling features like task batching, undo capability and clear audit logs for complex reasoning chains.
* **Day 16 -** Applied the Adapter Pattern to bridge the gap between agent's standard interface and incompatible third-party APIs. This allows the agent to utilize a diverse range of external tools (like legacy weather services) without cluttering the core logic with messy translation code.
* **Day 17 -** Implemented the Facade Pattern to simplify complex subsystem interactions. By hiding the intricate details of multiple tools (like initializing databases, authenticating and logging) behind a single front door interface, the agent can focus on high-level goals without getting bogged down in low-level configuration.
* **Day 18 -** Successfully integrated the Factory, Observer and Decorator patterns into a unified sensor monitoring system. This demonstrated the synergy of design patterns - the Factory handled object creation, the Decorator managed logging (cross-cutting concerns) and the Observer handled real-time alerts, resulting in a highly decoupled and scalable architecture.
* **Day 19 -** Transitioned from scripting to library building by creating a reusable Pattern Toolkit. Learned the importance of modularizing code into logical components (Creation vs. Behavior) and using `__init__.py` to manage a clean public API. This shift toward Code as Infrastructure ensures that future agent projects can import robust, pre-tested design patterns rather than reinventing them, mirroring the architecture of major frameworks like LangChain.
* **Day 20 -** Integrated a real-world OAuth 2.0 Client Credentials Flow using the Spotify Web API. Mastered the process of exchanging Base64-encoded credentials for a temporary Bearer Token and implemented a proactive refresh mechanism. This taught me that an agent's autonomy depends heavily on its ability to manage its own authentication lifecycle detecting expiration and handling 401 Unauthorized errors without manual intervention.
* **Day 21 -** Shifted from Polling (Pull) to Webhooks (Push) architecture by building a local HTTP server with Flask. Used Localtunnel to bridge the gap between local machine and the public internet, allowing the agent to receive real-time signals from external sources. I learned that event-driven agents are significantly more resource-efficient, as they remain idle until a specific payload is pushed to their endpoint, a critical design pattern for scaling real-time AI systems like notification bots or automated support agents.

---

## 💻 Tech Stack

* **Languages -** Python
* **Libraries -** `asyncio`, `pandas`, `numpy`, `aiohttp`, `matplotlib`, `beautifulsoup4`, `requests`, `dask`, `pytest`, `python-dotenv` (so far)
* **Frameworks -** Flask, LangChain(Upcoming), AutoGen(Upcoming), LangGraph(Upcoming)

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
    | **12** | [Code](./day12/README.md) |
    | **13** | [Code](./day13/README.md) |
    | **14** | [Code](./day14/README.md) |
    | **15** | [Code](./day15/README.md) |
    | **16** | [Code](./day16/README.md) |
    | **17** | [Code](./day17/README.md) |
    | **18** | [Code](./day18/README.md) |
    | **19** | [Code](./day19/README.md) |
    | **20** | [Code](./day20/README.md) |
    | **21** | [Code](./day21/README.md) |

---
*Connect with me on [LinkedIn](https://www.linkedin.com/in/romen-ranasingha) to follow my daily updates!*
