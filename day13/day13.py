from abc import ABC, abstractmethod

# observer interface
class Observer(ABC):
    """
    The interface that all subscribers must implement
    """
    @abstractmethod
    def update(self, agent_name: str, status: str):
        pass

class Agent:
    def __init__(self, name: str):
        self.name = name
        self._observers = []  # list to hold subscribers
        self._status = "Idle"

    def attach(self, observer: Observer):
        """Add a new listener"""
        self._observers.append(observer)
        print(f"{observer.__class__.__name__} is now watching {self.name}.")

    def detach(self, observer: Observer):
        """Remove a listener"""
        self._observers.remove(observer)

    def notify(self):
        """Notify all listeners of the current state"""
        print(f"{self.name} notifying observers...")
        for observer in self._observers:
            observer.update(self.name, self._status)

    def set_status(self, new_status: str):
        """Change state and trigger notification"""
        print(f"{self.name} is changing status to {new_status}")
        self._status = new_status
        self.notify()

# concrete observers
class LoggerObserver(Observer):
    def update(self, agent_name: str, status: str):
        print(f"Agent '{agent_name}' changed state to '{status}'.")

class AlertSystemObserver(Observer):
    def update(self, agent_name: str, status: str):
        if status == "Error":
            print(f"CRITICAL ISSUE DETECTED WITH {agent_name}")
        elif status == "Complete":
            print(f"User notified: Task finished by {agent_name}.")

if __name__ == "__main__":
    # create the subject
    agent = Agent("Agent-001")

    # create observers
    logger = LoggerObserver()
    alerts = AlertSystemObserver()

    # attach observers
    agent.attach(logger)
    agent.attach(alerts)

    # simulate state changes
    agent.set_status("Working")   # both log it
    agent.set_status("Complete")  # alert system sends a success notification
    agent.set_status("Error")     # alert system triggers a critical alert
