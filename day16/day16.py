from abc import ABC, abstractmethod

# agent expects all tools to look like this
class AgentTool(ABC):
    @abstractmethod
    def execute(self, query: str) -> str:
        pass

# this class has a useful feature but the interface is incompatible
# it uses 'get_temperature_city' instead of 'execute'
class LegacyWeatherAPI:
    def get_temperature_city(self, city_name: str, unit: str = "C") -> float:
        print(f"Connecting to old weather satellite for {city_name}...")
        # simulate fetching data
        if city_name.lower() == "paris":
            return 15.5
        elif city_name.lower() == "new york":
            return 22.0
        return 0.0

# adapter
# this wraps the Legacy API to look like an AgentTool
class WeatherToolAdapter(AgentTool):
    def __init__(self, legacy_api: LegacyWeatherAPI):
        self.legacy_api = legacy_api

    def execute(self, query: str) -> str:
        """
        Translates the generic 'query' (e.g., 'Paris') 
        into the specific method call required by the legacy API
        """
        print(f"Translating query '{query}' to legacy format...")
        
        # adapter handles the complexity of the specific method call
        temp = self.legacy_api.get_temperature_city(query, unit="C")
        
        return f"It is {temp}°C in {query}."

# agent
def agent_runner(tool: AgentTool, query: str):
    """
    The agent code only knows how to call .execute()
    It doesn't know or care that it's actually calling a legacy API
    """
    print(f"Agent is invoking tool with: {query}")
    result = tool.execute(query)
    print(f"Result: {result}")

if __name__ == "__main__":
    # create the incompatible service
    old_service = LegacyWeatherAPI()

    # wrap it with the adapter
    weather_tool = WeatherToolAdapter(old_service)

    # agent uses it just like any other standard tool
    agent_runner(weather_tool, "Paris")
    agent_runner(weather_tool, "New York")