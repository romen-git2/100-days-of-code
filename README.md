# 100 Days of Code - Building AI Agents

![Progress](https://img.shields.io/badge/Progress-45%2F100-brightgreen) ![Python](https://img.shields.io/badge/Python-3.10%2B-blue) ![Focus](https://img.shields.io/badge/Focus-AI%20Agents-orange)

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
| **22** | SQL storage: SQLite | Create table and insert agent states | ✅ | [Code](./day22/day22.py) |
| **23** | MongoDB | Insert and query JSON-like agent logs | ✅ | [Code](./day23/day23.py) |
| **24** | Redis caching | Cache and retrieve a key-value pair | ✅ | [Code](./day24/day24.py) |
| **25** | RabbitMQ queues | Send and receive a message in a queue | ✅ | [Code](./day25/producer.py) |
| **26** | Integrated tool: API + DB combo | Fetch data via API and store in DB | ✅ | [Code](./day26/day26.py) |
| **27** | API chaining | Chain two APIs with error handling | ✅ | [Code](./day27/day27.py) |
| **28** | Input validation | Validate and clean agent inputs | ✅ | [Code](./day28/day28.py) |
| **29** | Structured logging | Log agent events to file | ✅ | [Code](./day29/day29.py) |
| **30** | Metrics tracking | Track and report agent uptime | ✅ | [Code](./day30/day30.py) |

### Phase 3 - Agent Frameworks Foundations

| Day | Topic | Challenge | Status | Links |
| :--- | :--- | :--- | :--- | :--- |
| **31** | LangChain Components | Set up a basic LLM call with LCEL | ✅ | [Code](./day31/day31.py) |
| **32** | Simple Chains | Chain two prompts for Q&A (Prompt Chaining) | ✅ | [Code](./day32/day32.py) |
| **33** | Prompt Templating | Create a template with user input variables | ✅ | [Code](./day33/day33.py) |
| **34** | Output Parsing | Parse JSON from LLM output into Python objects | ✅ | [Code](./day34/day34.py) |
| **35** | Custom Tools | Define a calculator tool as a custom function | ✅ | [Code](./day35/day35.py) |
| **36** | ReAct Agent | Build an agent that answers using a tool (Reasoning + Action) | ✅ | [Code](./day36/day36.py) |
| **37** | Conversation Memory | Maintain a 3-turn chat history using Buffer Memory | ✅ | [Code](./day37/day37.py) |
| **38** | RAG Setup | Index a text file into a Vector Store (Document Indexing) | ✅ | [Code](./day38/day38.py) |
| **39** | Retrieval Query | Perform a similarity search on indexed docs | ✅ | [Code](./day39/day39.py) |
| **40** | Embeddings | Embed and compare two texts using pre-built models | ✅ | [Code](./day40/day40.py) |
| **41** | Prompt Tuning | Improve output using Few-Shot examples | ✅ | [Code](./day41/day41.py) |
| **42** | Sequential Workflows | Build a 3-step runnable workflow using LCEL | ✅ | [Code](./day42/day42.py) |
| **43** | Simple Agents | Build 3 variants: Zero-shot, Tool-using, and Memory agent | ✅ | [Code](./day43/day43.py) |
| **44** | Chain Tracing | Trace a chain execution using LangSmith basics | ✅ | [Code](./day44/day44.py) |
| **45** | Basic Assistant | Deploy a local Q&A assistant script | ✅ | [Code](./day45/day45.py) |
| **46** | AutoGen Agents | Create a single agent using AutoGen basic setup | ⬜ | |
| **47** | Multi-turn Convo | Simulate a back-and-forth dialogue in AutoGen | ⬜ | |
| **48** | Group Chat | Coordinate a simple task between 2 agents | ⬜ | |
| **49** | Role Definition | Assign custom personas/roles to agents | ⬜ | |
| **50** | API in AutoGen | Agent calls an external API within the AutoGen framework | ⬜ | |

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
* **Day 22 -** Implemented Persistent Memory for the agent using SQLite. Moved from storing state in volatile RAM (variables) to a file based database on disk. This allows the agent to survive restarts and crashes without losing its history. Learned to design a schema for Agent Activity Logs (timestamp, action, result) and reinforced the importance of ACID compliance for data integrity in long running autonomous systems.
* **Day 23 -** Integrated NoSQL storage with MongoDB to handle unstructured agent data. Unlike SQLite's rigid tables, MongoDB's flexible Document Store model is perfect for saving messy, nested JSON outputs typical of LLMs (like reasoning chains or multi-step plans). This Schema-less approach allows the agent's memory to evolve dynamically without needing complex database migrations every time adding a new data field.
* **Day 24 -** Implemented high speed caching using Redis to optimize agent performance. By storing expensive API responses in RAM, reducing data retrieval time from seconds(network latency) to microseconds. Learned the Cache-Aside Pattern and the importance of TTL (Time-To-Live) to ensure the agent doesn't act on stale data, significantly cutting down on redundant API costs and wait times.
* **Day 25 -** Mastered Asynchronous Messaging by implementing a distributed task queue with RabbitMQ. I transitioned from a monolithic script to a Producer-Consumer architecture, allowing a Manager agent to dispatch heavy web scraping jobs without blocking its own execution. Learned the importance of Message Acknowledgments(ACK) for fault tolerance and realized how queues enable horizontal scaling allowing multiple worker agents to pull from the same queue to process tasks in parallel.
* **Day 26 -** Built a Full Cycle Agent Tool that integrates API fetching, data processing and database persistence into a single workflow. I implemented the Service-Repository Pattern to cleanly separate network logic(Service) from storage logic(Repository). A critical takeaway was using the Upsert Strategy(ON CONFLICT DO UPDATE) in SQL, ensuring the agent can run repeatedly without crashing or corrupting data, a fundamental requirement for autonomous systems.
* **Day 27 -** Moving from isolated tool use to sequential workflow orchestration. By linking the output of a User Profile API(source) to a Real-time Weather API(enrichment), I implemented a deterministic handover process. This taught me the importance of Data Transformation—acting as the middleman to convert incompatible data types (like string coordinates to floats)—and Fail-Fast Error Handling, ensuring the chain terminates safely if a primary dependency is missing. This architecture is the backbone of Reasoning agents that must investigate and synthesize information from multiple sources to solve a single query.
* **Day 28 -** Implemented a strict Data Validation and Sanitization layer using Pydantic V2. By creating a Data Guardian for real-time API feeds, I moved from fragile dictionary parsing to a robust Schema-First approach. Leveraged Type Coercion(auto-converting strings to floats) and Custom Field Validators to sanitize messy external data such as automatically prepending protocols to URLs. In agentic systems, Fail-Fast validation is the ultimate defense against "Garbage In, Garbage Out" ensuring that downstream logic only ever interacts with clean, verified and physically logical data.
* **Day 29 -** Transitioned to Structured JSON Logging, establishing production grade observability for agentic workflows. By implementing a custom JSONFormatter and a trace_id system using UUIDs, I enabled the ability to track an agent's Flight Path across multiple distributed events. Logging should not just be text but Data capturing real-time metrics like latency_ms and status_codes in a machine readable format. This shift is critical for debugging complex multi-agent systems, allowing logs to be ingested by aggregators(like ELK or Datadog) to create performance dashboards and trigger automated alerts based on structured failure patterns.
* **Day 30 -** Mastered Metrics Tracking and Health Monitoring, the final pillar of agent reliability. While logging(Day 29) captures discrete events, metrics are essential for identifying silent degradations, where an agent is running but performing poorly. I built a live Watchdog agent that calculates real-time SRE Golden Signals(Latency, Success Rate and Jitter) from network pings. By implementing automated threshold logic, I enabled the agent to self diagnose its own state (Healthy vs. Degraded), allowing for proactive alerting. This concludes Phase 2, moving from isolated tools to a fully observable, self-aware agent architecture.
* **Day 31 -** Entered the LangChain era by building LCEL (LangChain Expression Language) pipeline. By abstracting "Prompt -> Model -> Parser" flow into a declarative chain (chain = prompt | model | parser), we can build AI applications that are modular and model-agnostic.
* **Day 32 -** Mastered Sequential Prompt Chaining by building a multi-step pipeline where the output of one LLM call serves as the input for the next. I discovered that decomposing complex tasks such as technical research followed by persona based simplification leads to significantly higher accuracy and better tone control compared to a single mega prompt. By using the Gemini 2.5 Flash model, I implemented a high speed workflow optimized for the reasoning and thinking required in agentic use cases.
* **Day 33 -** Mastered Dynamic Prompt Templating. I transitioned from brittle string concatenation to LangChain's ChatPromptTemplate, building a reusable, context aware email generator. A major takeaway was learning to separate Instructions (System Message) from Data (User Input). By programmatically injecting variables like datetime.date.today(), I ensured the agent produces production-ready output without manual placeholders like [Date], a critical step for building autonomous, end-to-end workflows.
* **Day 34 -** Solved the "Text vs. Data" conflict by implementing Structured Output Parsing. By utilizing JsonOutputParser and Pydantic schemas, I forced the LLM to return valid JSON objects instead of conversational prose. I learned that defining a schema acts as a Contract for the agent, by setting `temperature=0.0`, the model shifts from creative generation to deterministic extraction. This is the fundamental bridge that allows AI agents to communicate with databases, external APIs and frontend UIs reliably.
* **Day 35 -** Transitioned from "AI that talks" to "**AI that acts**" by implementing **Custom Tools (Function Calling)**. I learned that a Tool is essentially a Python function wrapped in a `@tool` decorator, where the docstring serves as the instruction manual for the LLM. I mastered the **Execution Round-Trip** - The AI identifies a need, generates a structured tool call, the system executes the Python logic and the result is fed back via a `ToolMessage`. This architecture allows the agent to delegate precise tasks to deterministic code, eliminating LLM hallucinations in technical domains.
* **Day 36 -** Built an autonomous **ReAct Agent**. I transitioned from manual orchestration (where the developer writes the if/else logic for tool calls) to autonomous reasoning, where the LLM determines the execution path based on a provided toolkit. I learned how to implement a stateful **Reason -> Act -> Observe** loop, enabling the agent to solve multi-step problems (like calculating character counts and performing sequential math) by maintaining a scratchpad of its own thoughts and tool observations.
* **Day 37 -** Implemented **Conversation Memory** using LangChain's modern RunnableWithMessageHistory. LLMs are inherently stateless and that AI memory is actually achieved by dynamically injecting previous interaction history into the prompt's context window. By leveraging `InMemoryChatMessageHistory` and `session_id` management, unlocked capability of recalling user details across multiple turns, officially transitioning from single-shot tasks to stateful, continuous dialogues.
* **Day 38 -** Built a complete Document Indexing pipeline. LLMs can’t efficiently process massive files in a single prompt, so implemented an ETL workflow to Load raw text, Split it into semantic chunks using `RecursiveCharacterTextSplitter`, and transform those chunks into high-dimensional mathematical vectors (Embeddings) using Google's `gemini-embedding-001`. By storing these in a local FAISS Vector Database, enabled the agent to perform Semantic Search, retrieving information based on meaning rather than just keyword matching.
* **Day 39 -** Completed the **Retrieval-Augmented Generation (RAG)** loop by implementing the Execution phase. Learned how to ground an LLM in a custom knowledge base by performing a similarity search on a local FAISS index and injecting the retrieved chunks into a restricted system prompt. The key takeaway was realizing how `temperature=0` and explicit context instructions act as a primary defense against AI hallucinations in production-grade RAG systems.
* **Day 40 -** Demystified the black box of Vector Databases by manually working with **Embeddings and Cosine Similarity**. Embedding models convert text into massive, high-dimensional float arrays (specifically, 3072 dimensions), mapping concepts into a geometric space. By using `numpy` to manually calculate the angle between vectors, semantically identical sentences with zero keyword overlap (e.g., "reset password" vs. "recover credentials") score a high `0.71` similarity, compared to `0.51` for unrelated text. This geometric relationship is the absolute mathematical foundation of semantic search and RAG.
* **Day 41 -** Used **Few-Shot Prompting** to dynamically control LLM output formatting. Used the "Show, Don't Tell" principle of Prompt Engineering. Instead of writing overly complex System Prompts (Zero-Shot) hoping the model formats data correctly, used LangChain's `FewShotChatMessagePromptTemplate` to inject 3 examples of optimal input/output pairs directly into the prompt as simulated chat history. This leverages In-Context Learning, forcing the AI to perfectly mimic a desired tone and structure (like explaining tech concepts using analogies) without the need for expensive model fine-tuning.
* **Day 42 -** Built a 3-step Sequential Workflow (Topic -> Title -> Outline -> Tweet) using LangChain Expression Language (LCEL) and `RunnablePassthrough.assign()`. When chaining LLMs, Strict Prompting (e.g., "Return exactly one item. No conversational filler.") is mandatory to keep data clean as it moves down the assembly line.
* **Day 43 -** Built 3 Agent variants (Zero-shot, Tool-using and Memory) using LangChain `create_agent` factory. By defining external capabilities as `@tool` functions, the agent transitions from an isolated brain to a stateful system capable of **Anaphora Resolution** (resolving "the item I mentioned earlier" into "Gaming Laptop" by tracking message history).
* **Day 44 -** Solved the LLM Black Box problem by implementing **Observability with LangSmith**. Debugging multi-step AI pipelines with `print()` statements is unscalable. By enabling `LANGCHAIN_TRACING_V2`, automatically captured the exact inputs, outputs, token consumption and latency of a multi-step LCEL workflow. This visual tracing is a mandatory architectural component for moving AI agents from experimental scripts to production-grade, debuggable software.
* **Day 45 -** Built **ContractGuard Pro**, a Streamlit application utilizing a **Hybrid Edge-Cloud AI Architecture**. Implemented a Privacy Shield using `LangChain Ollama` (`gemma3:270m` and `moondream`) to scrub Personally Identifiable Information (PII) from PDFs and images entirely locally. Once anonymized, the sanitized text is sent to the Cloud (`gemini`) for complex legal reasoning. Solidified understanding of routing workloads between Edge AI (for privacy) and Cloud AI (for intelligence).

---

## 💻 Tech Stack

* **Languages -** Python
* **Libraries -** `asyncio`, `pandas`, `numpy`, `aiohttp`, `matplotlib`, `beautifulsoup4`, `requests`, `dask`, `pytest`, `python-dotenv`, `pymongo`, `redis`, `pika`, `pydantic`, `langchain-google-genai`, `langchain-community`, `langchain-text-splitters`, `faiss-cpu`, `langchain-core`, `streamlit`, `langchain-ollama`, `Pillow`, `pypdf`, `python-docx`, `fpdf2`, `pdf2image`(so far)
* **Frameworks -** Flask, LangChain, AutoGen(Upcoming), LangGraph(Upcoming)

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
    | **22** | [Code](./day22/README.md) |
    | **23** | [Code](./day23/README.md) |
    | **24** | [Code](./day24/README.md) |
    | **25** | [Code](./day25/README.md) |
    | **26** | [Code](./day26/README.md) |
    | **27** | [Code](./day27/README.md) |
    | **28** | [Code](./day28/README.md) |
    | **29** | [Code](./day29/README.md) |
    | **30** | [Code](./day30/README.md) |
    | **31** | [Code](./day31/README.md) |
    | **32** | [Code](./day32/README.md) |
    | **33** | [Code](./day33/README.md) |
    | **34** | [Code](./day34/README.md) |
    | **35** | [Code](./day35/README.md) |
    | **36** | [Code](./day36/README.md) |
    | **37** | [Code](./day37/README.md) |
    | **38** | [Code](./day38/README.md) |
    | **39** | [Code](./day39/README.md) |
    | **40** | [Code](./day40/README.md) |
    | **41** | [Code](./day41/README.md) |
    | **42** | [Code](./day42/README.md) |
    | **43** | [Code](./day43/README.md) |
    | **44** | [Code](./day44/README.md) |
    | **45** | [Code](./day45/README.md) |

---
*Connect with me on [LinkedIn](https://www.linkedin.com/in/romen-ranasingha) to follow my daily updates!*
