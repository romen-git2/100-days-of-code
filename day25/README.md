# Day 25 - Distributed Task Queues with RabbitMQ

**Phase 2 -** Agent Design Patterns & Integrations

## 📝 The Challenge

**Goal -** Implement an **Asynchronous Message Queue** system to decouple the Task Assigner from the Task Executor.

In a scalable AI system, you cannot have the main application block(freeze) while waiting for heavy tasks(like scraping a website, generating an image or processing a large file) to complete.

* **Synchronous -** User waits 10s for the scraper.
* **Asynchronous -** User gets an Accepted message instantly, the scraper runs in the background.

We use **RabbitMQ** as the message broker to handle this communication safely and reliably.

## 🛠️ Tech Stack

* **Python 3.10+**
* **RabbitMQ -** A robust, open-source message broker.
* **`pika` -** The Python client library for RabbitMQ.
* **`requests` -** Used by the worker to perform **network operations**.

## 📂 Solution Overview

We built a **Producer-Consumer Architecture**:

1. **The Producer (`producer.py`) -** Acts as the Manager. It takes a list of URLs and pushes them into a named queue (`scrape queue`). It does not wait for the work to finish.
2. **The Queue -** A buffer inside RabbitMQ that holds the messages safely.
3. **The Consumer (`consumer.py`) -** Acts as the Worker. It listens to the queue, picks up a URL, performs a **HTTP request** to download the page and prints the result.
4. **Acknowledgment(ACK) -** The worker explicitly tells RabbitMQ "I am done" only after the job is finished. If the worker crashes mid-job, the message is saved and re-delivered to another worker.

## 🏃‍♂️ How to Run

### 1. Prerequisites(Start RabbitMQ)

You need a running RabbitMQ instance.

* **Using Docker(Recommended):**

    ```bash
    docker run -d --hostname day25-rabbit --name some-rabbit -p 5672:5672 -p 15672:15672 rabbitmq:3-management
    ```

    *(Note - You can visit `http://localhost:15672` (login - `guest`/`guest`) to see the dashboard.)*

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. **Run the Distributed System**

You need two separate terminal windows to see the magic.

**Terminal 1(The Worker) -** Start the consumer. It will sit idle, waiting for work.

```bash
python consumer.py
```

**Terminal 2(The Manager) -** Run the producer to dispatch jobs.

```bash
python producer.py
```

### 4. **Observe**

* **Terminal 2** will instantly run and exit.
* **Terminal 1** will wake up, pick up the URLs one by one, scrape the websites(you will see network pauses) and print the file sizes.

## 🧠 Key Learnings

* **Decoupling -** The Producer doesn't know who the consumer is or if they are even online. This allows you to restart the worker without breaking the manager.
* **Asynchronous Processing -** Heavy tasks(like network requests) are moved out of the main flow, preventing bottlenecks.
* **Durability -** RabbitMQ keeps messages safe in the queue until they are explicitly Acknowledged(ACK).
* **Scaling -** Could simply run python consumer.py in five different terminals and RabbitMQ would automatically distribute the work among them(Round Robin).

---
[Back to Main Repo](../README.md)
