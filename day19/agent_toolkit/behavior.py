from abc import ABC, abstractmethod
import functools
import time

# observer pattern
class Observer(ABC):
    @abstractmethod
    def update(self, message: str):
        pass

class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer: Observer):
        self._observers.append(observer)

    def notify(self, message: str):
        for observer in self._observers:
            observer.update(message)

# decorator pattern
def log_execution(func):
    """A reusable decorator that logs start/end of agent actions"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Starting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Finished {func.__name__} (Time: {end - start:.4f}s)")
        return result
    return wrapper

