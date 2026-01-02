import os
from pymongo import MongoClient
from dotenv import load_dotenv
import datetime

# setup connection
load_dotenv()
uri = os.getenv("MONGO_URI")

try:
    client = MongoClient(uri)
    # ping to check if connection is successful
    client.admin.command('ping')
    print("Successfully connected to MongoDB")
except Exception as e:
    print(f"Connection failed: {e}")
    exit()

# select database & collection
db = client["agent"]
memories = db["logs"]

# storing complex data(write)
def log_agent_thought_process():
    # data structure is deeply nested and messy
    complex_memory = {
        "session_id": "sess_998877",
        "agent_type": "Researcher",
        "timestamp": datetime.datetime.now(datetime.timezone.utc),
        "task": "Analyze market trends for EV cars",
        "thought_chain": [
            {"step": 1, "thought": "Searching Google for 'EV sales 2025'",
                "tool": "GoogleSearch"},
            {"step": 2, "thought": "Found 15 articles. Filtering for relevance.",
                "tool": "DataFilter"},
            {"step": 3, "thought": "Summarizing top 3 trends.",
                "tool": "LLM_Summarizer"}
        ],
        "final_output": {
            "trend_1": "Battery costs dropping",
            "trend_2": "infrastructure expanding",
            "confidence_score": 0.89
        }
    }

    result = memories.insert_one(complex_memory)
    print(f"Document saved with ID {result.inserted_id}")

# retrieving data(read)
def find_relevant_memories(agent_type):
    print(f"Searching for memories from {agent_type}...")

    query = {"agent_type": agent_type}
    results = memories.find(query)

    for doc in results:
        print(f"Found Session: {doc['session_id']}")
        print(f"Last Thought: {doc['thought_chain'][-1]['thought']}")
        print(f"Confidence: {doc['final_output']['confidence_score']}")

if __name__ == "__main__":
    log_agent_thought_process()
    find_relevant_memories("Researcher")
