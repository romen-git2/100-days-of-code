from abc import ABC, abstractmethod
import time

# strategy interface
class ProcessingStrategy(ABC):
    """
    The interface that all strategies must follow.
    This ensures every strategy has a 'processQuery' method.
    """
    @abstractmethod
    def processQuery(self, query: str) -> str:
        pass

# concrete strategies
class KeywordSearchStrategy(ProcessingStrategy):
    """Strategy A - Fast, simple keyword matching."""
    def processQuery(self, query: str) -> str:
        print("Using fast Keyword Search...")
        # simulate simple logic
        if "weather" in query.lower():
            return "It is sunny today."
        elif "price" in query.lower():
            return "$100."
        else:
            return "No keywords found."

class LLMReasoningStrategy(ProcessingStrategy):
    """Strategy B - Slow, complex reasoning (simulated)."""
    def processQuery(self, query: str) -> str:
        print("Using advanced LLM Reasoning...")
        # simulate latency (thinking time)
        time.sleep(1)
        return f"Based on the context of '{query}', I deduce the answer is complex."

class Agent:
    def __init__(self, name: str, strategy: ProcessingStrategy):
        self.name = name
        self.strategy = strategy

    def setStrategy(self, strategy: ProcessingStrategy):
        """Allows switching the 'brain' of the agent dynamically."""
        print(
            f"Switching {self.name}'s strategy to {strategy.__class__.__name__}")
        self.strategy = strategy

    def answer(self, query: str):
        print(f"{self.name} received query: '{query}'")
        # delegate the work to the strategy object
        result = self.strategy.processQuery(query)
        print(result)

if __name__ == "__main__":
    # "Fast" strategy
    agent = Agent(name="bot", strategy=KeywordSearchStrategy())

    agent.answer("What is the weather?")
    agent.answer("What is the meaning of life?")  # fails (no keyword)

    # switch to the "Smart" strategy dynamically
    # this is useful if the first attempt failed or if the user asks a hard question
    agent.setStrategy(LLMReasoningStrategy())

    agent.answer("What is the meaning of life?")
