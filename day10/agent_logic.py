import re


def parse_llm_action(text: str) -> dict:
    """ 
    parses string like 'Action: Search("query")' into a dictionary.
    expected format - Action: ToolName("Args")    
    """
    pattern = r"Action:\s*(\w+)\((.*)\)"
    match = re.search(pattern, text)

    if not match:
        raise ValueError(
            "Invalid action format. Expected: 'Action: ToolName(Args)'")

    tool_name = match.group(1)
    arguments = match.group(2).replace('"', '').strip()

    return {
        "tool": tool_name,
        "args": arguments
    }


def calculate_confidence(probs: list) -> float:
    """ calculate average confidence from a list token probabilities """
    if not probs:
        return 0.0

    return sum(probs) / len(probs)
