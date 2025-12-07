import pytest
from agent_logic import parse_llm_action, calculate_confidence


def test_parse_valid_action():
    input_text = 'Action: Search("Python Agents")'
    expected = {
        "tool": "Search",
        "args": "Python Agents"
    }

    result = parse_llm_action(input_text)

    assert result == expected


def test_parse_action_with_spaces():
    input_text = 'Action:   Email("romenranasingha@gmail.com")'
    result = parse_llm_action(input_text)
    assert result["tool"] == "Email"
    assert result["args"] == "romenranasingha@gmail.com"


def test_parse_invalid_format_raises_error():
    bad_input = "I think I shoould search for Python"

    with pytest.raises(ValueError) as excinfo:
        parse_llm_action(bad_input)

    assert "Invalid action format." in str(excinfo.value)


def test_confidence_calculation():
    probs = [0.9, 0.8, 1.0]
    assert calculate_confidence(probs) == 0.9


def test_confidence_empty_list():
    assert calculate_confidence([]) == 0.0
