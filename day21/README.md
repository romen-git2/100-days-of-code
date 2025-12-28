# Day 21 - Webhooks & Event-Driven Architecture

**Phase 2 -** Agent Design Patterns & Integrations

## 📝 The Challenge

**Goal -** Transform the agent from a Pull-based system (polling) to a Push-based system (Webhooks). Build a local HTTP server that can receive real-time data from the internet.

Most modern agents shouldn't waste resources asking "Is there new data?" every few seconds. Instead, they should act like a service that stays idle until an external event (a GitHub push, a Discord message or a Stripe payment) triggers them.

## 🛠️ Tech Stack

* **Python 3.10+**
* **Flask -** To create the web server and the `/webhook` endpoint.
* **Localtunnel (npx) -** To create a secure bridge between the public internet and `localhost:5000`.
* **Postman -** To simulate an external service sending a JSON payload.

## 📂 Solution Overview

### 1. The Webhook Listener (`day21.py`)

Using **Flask**, we opened a specific gate (the `/webhook` route) that only accepts `POST` requests.

* **Validation -** The agent first checks if the incoming data is valid JSON.
* **Routing -** Based on the `action` field in the payload (e.g., alert or greet), the agent executes a specific internal function.

### 2. The Public Tunnel

Since `localhost` is invisible to the outside world, we used `npx localtunnel` to generate a temporary public URL. This allows any service on the internet to send data directly to our Python script.

## 🏃‍♂️ How to Run

1. **Start the Server:**

    ```bash
    python day21.py
    ```

    *The agent is now listening on port 5000.*

2. **Expose the Server:**
    In a separate terminal, run:

    ```bash
    npx localtunnel --port 5000
    ```

    *Copy the URL provided (e.g., `https://seven-banks-invite.loca.lt`).*

3. **Trigger the Agent:**
    Open **Postman**, set the method to **POST**, enter your localtunnel URL + `/webhook` and send a JSON body:

    ```json
    {
      "sender": "RemoteServer USA",
      "action": "alert"
    }
    ```

## 🧠 Key Learnings

* **Asynchronous Triggers -** Learned how to build an agent that reacts instantly to external events rather than relying on a `while True` loop.
* **Infrastructure Tunneling -** Understood how to safely bridge local development with the public web for testing third-party integrations.
* **Payload Parsing -** Practiced extracting intent from a JSON Webhook Payload, which is the standard way modern apps (Slack, GitHub, Twilio) communicate.

---
[Back to Main Repo](../README.md)
