# Day 4 - Web Scraping with BeautifulSoup

**Phase 1 -** Advanced Python & Agent Tools

## 📝 The Challenge

**Goal -** Parse a news article or webpage and extract headlines.

Large Language Models (LLMs) are trained on static datasets, meaning their knowledge is "frozen in time." To build an agent that is truly aware of the world (e.g., a stock market bot or a news summarizer), you need to give it the ability to browse the web. This challenge focuses on **Web Scraping** - programmatically fetching and parsing HTML to extract specific information that an agent can process.

## 🛠️ Tech Stack

* **Python 3.10+**
* **`requests`** - A simple and elegant HTTP library for Python, used to fetch web pages.
* **`beautifulsoup4` (bs4)** - A library for pulling data out of HTML and XML files. It navigates the "soup" of messy HTML tags to find the data you need.

## 📂 Solution Overview

The solution script (`day4.py`) demonstrates how to scrape the **Reddit.com News** section:

1. **Request** - Uses `requests.get()` to download the raw HTML of the page. It includes a `User-Agent` header to mimic a real web browser (avoiding some basic bot blockers).
2. **Parse** - Creates a `BeautifulSoup` object to traverse the HTML Document Object Model (DOM).
3. **Extract** - Uses `.find_all()` to locate specific HTML tags (in this case, `<p>` tags with the class `title`) that contain the headlines.
4. **Clean** - Strips away the HTML tags to output clean, human-readable text.

## 🏃‍♂️ How to Run

1. **Install Dependencies:**

    ```bash
    pip install beautifulsoup4 requests
    ```

2. **Run the Script:**

    ```bash
    python day4.py
    ```

3. **Expected Output:**
    The script will print the number of headlines found followed by the list of titles extracted from the live website.

    ```text
    Fetching posts from https://old.reddit.com/r/news/top/
    Found 8 titles
    1 Rep. Marjorie Taylor Greene announces resignation from Congress
    2 🔒 Lost access to your HPC cluster? Inductiva.AI gets you back up and running OpenFOAM in just 10 lines of Python. Start free.
    3 Superman number one copy found in attic becomes most expensive comic ever sold
    ...
    ```

## 🧠 Key Learnings

* **The DOM -** Understanding HTML structure (tags, classes, IDs) is essential for telling an agent *where* to look for information.
* **Bot Etiquette -** Always use headers (User-Agent) and respect `robots.txt` when possible to avoid getting banned by servers.
* **Live Context -** This is the foundational skill for "Retrieval Augmented Generation" (RAG) workflows where agents fetch live data to answer user queries.

---
[Back to Main Repo](../README.md)
