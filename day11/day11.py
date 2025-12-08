from abc import ABC, abstractmethod

# agent interface
class BaseAgent(ABC):

    @abstractmethod
    def act(self, task: str):
        pass

# concrete agent types
class ResearchAgent(BaseAgent):

    def act(self, task: str):
        print(f"Searching sources for {task}")
        return "Found 5 relevant sources."

class CreativeAgent(BaseAgent):

    def act(self, task: str):
        print(f"Brainstorming ideas for {task}")
        return "Drafted 3 creative concepts."

class CoderAgent(BaseAgent):

    def act(self, task: str):
        print(f"Writing python code for {task}")
        return print(f"Code for {task}")

# agent factory
class AgentFactory():

    @staticmethod
    def create_agent(agent_type: str) -> BaseAgent:

        agent_type = agent_type.lower()

        if agent_type == "research":
            return ResearchAgent()
        elif agent_type == "creative":
            return CreativeAgent()
        elif agent_type == "coding":
            return CoderAgent()
        else:
            raise ValueError(f"Unknown agent type: {agent_type}")


# client code (simulation)
if __name__ == "__main__":

    tasks = [
        ("research", "History of AI"),
        ("creative", "Logo design for a startup"),
        ("coding", "Fibonacci sequence script"),
        # ("writer", "Write a book") # this trigger the error
    ]

    for type_name, task in tasks:
        try:
            agent = AgentFactory.create_agent(type_name)
            result = agent.act(task)
            print(f"Result: {result}")
        except ValueError as e:
            print(f"Error: {e}")
