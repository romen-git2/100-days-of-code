# Day 10 - Unit Testing with Pytest

**Phase 1 -** Advanced Python & Agent Tools

## 📝 The Challenge

**Goal -** Write tests for a simple agent action function.

AI Agents are complex systems composed of many moving parts - prompt parsers, tool selectors and API handlers. If you change a single line of code to improve one feature, you risk breaking another. This challenge focuses on **Unit Testing**, a critical practice for ensuring that the deterministic parts of your agent (like parsing a command string: `Action: Search("query")`) work reliably and don't suffer from regressions as your codebase grows.

## 🛠️ Tech Stack

* **Python 3.10+**
* **`pytest`** - The industry-standard testing framework for Python. It is favored for its simple syntax (`assert result == expected`) and powerful features like fixtures and parametrization.

## 📂 Solution Overview

The solution consists of two files separating the code from the tests:

1. **`agent_logic.py`** (The Component):
    * Contains a function `parse_llm_action` that uses regex to extract tool names and arguments from a raw text string.
    * Contains a helper `calculate_confidence` to average probability scores.
2. **`test_agent.py`** (The Test Suite):
    * **test_parse_valid_action()** - Verifies that valid inputs return the correct dictionary structure.
    * **test_parse_action_with_spaces()** - Tests how the parser handles extra whitespace or empty lists.
    * **test_parse_invalid_format_raises_error()** - Uses `pytest.raises` to ensure the function explicitly throws a `ValueError` when given malformed input (crucial for robust agents).

## 🏃‍♂️ How to Run

1. **Install Dependencies:**

    ```bash
    pip install pytest
    ```

2. **Run the Tests:**
    Navigate to the directory and run the `pytest` command. It will automatically discover and run the test file.

    ```bash
    pytest
    ```

3. **Expected Output:**
    You should see green text indicating that all tests passed.

    ```text
    test_agent.py .....                                                      [100%]

    ============================== 5 passed in 0.47s ==============================
    ```

## 🧠 Key Learnings

* **Determinism -** While you can't always predict what an LLM *writes*, you MUST be able to predict how your code *handles* it. Unit tests ensure your parsers are bulletproof.
* **Regression Prevention -** Writing tests now saves you hours of debugging later. If a future update breaks your parser, `pytest` will alert you immediately.
* **Testing Failure -** It is just as important to test that your code fails correctly (raises the right errors) on bad input as it is to test that it succeeds on good input.

---
[Back to Main Repo](../README.md)
