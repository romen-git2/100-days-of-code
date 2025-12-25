from abc import ABC, abstractmethod
import random
import time
import functools

# observer(alert system)
class Observer(ABC):
    @abstractmethod
    def update(self, sensor_name: str, value: float):
        pass

class AlarmSystem(Observer):
    def update(self, sensor_name: str, value: float):
        if value > 80:
            print(f"{sensor_name} is CRITICAL! Value: {value:.2f}")

# decorator(logger)
def log_reading(func):
    """Decorator to log sensor readings automatically"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        sensor_name = args[0].name # args[0] is self
        print(f"Reading data from {sensor_name}...")
        result = func(*args, **kwargs)
        print(f"Value: {result:.2f}")
        return result
    return wrapper

# sensor base class
class Sensor(ABC):
    def __init__(self, name):
        self.name = name
        self._observers = []

    def attach(self, observer: Observer):
        self._observers.append(observer)

    def notify(self, value):
        for observer in self._observers:
            observer.update(self.name, value)

    @abstractmethod
    def read_value(self):
        pass

# factory 
class TemperatureSensor(Sensor):
    @log_reading  # applying decorator
    def read_value(self):
        # simulate temp
        val = random.uniform(20, 100)
        self.notify(val) # notify observers
        return val

class PressureSensor(Sensor):
    @log_reading  # applying decorator
    def read_value(self):
        # simulate pressure
        val = random.uniform(50, 120)
        self.notify(val) # notify observers
        return val

class SensorFactory:
    @staticmethod
    def create_sensor(sensor_type: str, name: str) -> Sensor:
        if sensor_type == "temp":
            return TemperatureSensor(name)
        elif sensor_type == "pressure":
            return PressureSensor(name)
        else:
            raise ValueError("Unknown sensor type")

if __name__ == "__main__":
    print("Initializing System(Factory)")
    factory = SensorFactory()
    
    # create sensors using factory
    t_sensor = factory.create_sensor("temp", "Core Temp")
    p_sensor = factory.create_sensor("pressure", "Hydraulic Press")

    # attach observer(alarm system)
    alarm = AlarmSystem()
    t_sensor.attach(alarm)
    p_sensor.attach(alarm)

    print("Running Sensors(Decorator + Observer)")
    # simulate a few readings
    for _ in range(3):
        t_sensor.read_value()
        time.sleep(0.5)
        
        p_sensor.read_value()
        time.sleep(0.5)