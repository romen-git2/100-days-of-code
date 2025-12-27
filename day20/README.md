# Day 20 - Real World OAuth & API Integration

**Phase 2 -** Agent Design Patterns & Integrations

## 📝 The Challenge

**Goal -** Connect an autonomous agent to a live, protected service (Spotify Web API) using the **OAuth 2.0 Client Credentials Flow**.

Real world agents must move beyond mock data. This challenge focuses on teaching an agent to navigate the Protected Web. The agent is responsible for:
1.**Secure Handshake -** Exchanging encrypted credentials for a temporary access token.
2.**State Management -** Tracking the token's lifetime and expiration.
3.**Resiliency -** Automatically refreshing tokens to ensure zero downtime operations.

## 🛠️ Tech Stack

* **Python 3.10+**
* **`requests`** - For handling HTTP/1.1 communication with Spotify's REST API.
* **`base64`** - Used to encode `CLIENT_ID:CLIENT_SECRET` into the required `Basic` Authorization header.
* **Spotify Web API** - Our real world data provider.

## 📂 Solution Overview

The implementation is split into two specialized components:

### 1. The `SpotifyAuthManager` (Provider)

* **Responsibility -** Handles the Secret handshake.
* **Logic -** It encodes credentials and sends a POST request to Spotify’s accounts service.
* **Expiration Handling -** It stores the `token_expires_at` timestamp. Before any API call, it checks `time.time()`. If the current time is within 60 seconds of expiration, it proactively fetches a new token.

### 2. The `MusicAgent` (Consumer)

* **Responsibility -** Executes business logic (searching for artists/music).
* **Logic -** It requests a Bearer Token from the Auth Manager. It focuses entirely on data retrieval and parsing, remaining agnostic of *how* the token was generated.
* **401 Retry Loop -** Includes a safety check-if a request returns a `401 Unauthorized` (even if the local clock says the token is valid), it forces a refresh and retries the request once.

## 🏃‍♂️ How to Run

1. **Create a Spotify Developer App:**
    * Log in to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard).
    * Create a new App.
    * Set the **Redirect URI** to `https://localhost:8888/callback` (Required for setup, though unused by our backend agent).
2. **Configure Credentials:**
    * Copy your **Client ID** and **Client Secret** into the `.env` script(refer `.env.example`).
3. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Execute:**

    ```bash
    python day20.py
    ```

## 🧠 Key Learnings

* **Bearer Authentication -** Authenticated requests are standardized via the `Authorization: Bearer <token>` header.
* **Proactive Refreshing -** Checking token validity *before* the request is far more efficient than waiting for a failure, especially for high frequency agents.
* **Base64 Encoding -** Many OAuth providers require a `Basic` auth header where credentials are joined by a colon and encoded to prevent issues with special characters in the secret.

---
[Back to Main Repo](../README.md)
