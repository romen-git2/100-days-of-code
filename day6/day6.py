import logging
import random
import time

# setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("agentRuntime.log"), 
        logging.StreamHandler()                 
    ]
)

# define custom exceptions
class AgentToolError(Exception):
    """raised when an external tool fails irrevocably"""
    pass

class AgentRateLimitError(Exception):
    """raised when the agent sends too many requests"""
    pass

def unstableAPICall():
    """simulates an API that succeeds, fails or times out randomly"""
    outcome = random.random()
    
    if outcome < 0.3:
        return {"status": "success", "data": "Agent obtained data!"}
    elif outcome < 0.6:
        raise ConnectionError("Failed to connect to server.")
    elif outcome < 0.8:
        raise AgentRateLimitError("Rate limit exceeded. Try again later.")
    else:
        raise ValueError("Invalid JSON response received.")

def runAgentTask():
    logging.info("Agent starting task execution...")
    
    maxRetries = 3
    for attempt in range(1, maxRetries + 1):
        try:
            logging.info(f"Attempt {attempt}/{maxRetries} Calling API...")
            result = unstableAPICall()
            
            logging.info(f"Success! Result: {result['data']}")
            return result
            
        except AgentRateLimitError as e:
            logging.warning(f"Rate limit hit: {e}. Waiting 2 seconds...")
            time.sleep(2)
            
        except ConnectionError as e:
            logging.error(f"Network issue: {e}. Retrying immediately...")
            
        except Exception as e:
            logging.critical(f"Critical/Unexpected Error: {type(e).__name__}: {e}")
            raise AgentToolError("Agent crashed due to unexpected API failure.") from e
    
    logging.error("All retries exhausted. Task failed.")
    return None

if __name__ == "__main__":
    try:
        runAgentTask()
    except AgentToolError:
        print("Main System: The agent failed and alerted the user.")