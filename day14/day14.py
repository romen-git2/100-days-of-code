import time
import functools
import random

# decorator
def measure_performance(func):
    """ A decorator that logs the execution time of the decorated function """
    @functools.wraps(func)  # preserves the metadata(name, docstring) of the original function
    def wrapper(*args, **kwargs):

        print(f"Starting task '{func.__name__}'")
        start_time = time.time()

        result = func(*args, **kwargs)

        end_time = time.time()
        duration = end_time - start_time

        print(f"Finished {func.__name__} in {duration:.4f} seconds")

        return result

    return wrapper

# agent tasks
# apply the decorator using @ symbol
@measure_performance
def run_agent_reasoning(task_name):
    """ Simulates a heavy reasoning step """
    print(f"Agent is thinking about {task_name}")
    process_time = random.uniform(0.5, 2.0)

    time.sleep(process_time)

    return "Analysis complete"


@measure_performance
def quick_memory_lookup(task_name):
    """ Simulates a fast database check """
    print(f"Checking memory for {task_name}")
    time.sleep(0.1)
    return "Found 2 records"


if __name__ == "__main__":

    result1 = run_agent_reasoning("Quantum physics strategy")

    result2 = quick_memory_lookup("Project Alpha")
