import requests
import json

def fetchAgentTasks():
    # fetching a list of todos from the mock API
    url = "https://jsonplaceholder.typicode.com/todos"

    print(f"Connecting to {url}...")

    try:
        response = requests.get(url)

        response.raise_for_status()  # raises an error for 4xx or 5xx codes

        # parse the JSON response
        tasks = response.json()

        print(f"Successfully retrieved {len(tasks)} tasks.")

        # filter Data (Agent Logic)
        completedTasks = [
            t for t in tasks
            if t['completed'] is True and t['userId'] == 1
        ]

        print(f"Found {len(completedTasks)} completed tasks for User 1.")

        # save the result
        outputFile = "agentTodos.json"
        with open(outputFile, "w") as f:
            json.dump(completedTasks, f, indent=4)

        print(f"Saved filtered tasks to '{outputFile}'")

    except requests.exceptions.RequestException as e:
        print(f"API Request failed: {e}")


if __name__ == "__main__":
    fetchAgentTasks()
    
    
    
    
