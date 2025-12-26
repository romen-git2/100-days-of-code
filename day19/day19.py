from agent_toolkit import SingletonMeta, Subject, Observer, log_execution
import time

# using singleton for global configuration
class GameConfig(metaclass=SingletonMeta):
    def __init__(self):
        self.difficulty = "Hard"
        print("Config Loaded")

# using observer for event system
class GameEventSystem(Subject):
    def trigger_event(self, event_name):
        print(f"Triggering Event: {event_name}")
        self.notify(event_name)

class PlayerUI(Observer):
    def update(self, message: str):
        print(f"Displaying notification: {message}")

class SoundEngine(Observer):
    def update(self, message: str):
        print(f"Playing sound effect for {message}")

# using decorator for logging
class PlayerAction:
    @log_execution
    def attack(self):
        print("Player swings sword")
        time.sleep(0.2)

if __name__ == "__main__":
    # singleton
    cfg1 = GameConfig()
    cfg2 = GameConfig()
    print(f"Are configs the same object? {cfg1 is cfg2}")

    # observer
    events = GameEventSystem()
    ui = PlayerUI()
    audio = SoundEngine()
    
    events.attach(ui)
    events.attach(audio)
    
    events.trigger_event("Boss Spawn")

    # decorator
    p = PlayerAction()
    p.attack()