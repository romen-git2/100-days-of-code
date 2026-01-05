import redis
import requests
import time
import hashlib
import json

# connect to redis
cache = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

def fetch_real_data_from_slow_api(query):
    """
    Makes a request to httpbin.org
    The '/delay/2' endpoint forces the server to wait 2 seconds before responding
    This mimics the latency
    """
    print(f"Making HTTP request for: {query}...")
    
    # this acts like LLM API endpoint
    url = f"https://httpbin.org/delay/2" 
    
    response = requests.post(url, json={"query": query})
    
    return response.json()

def get_agent_response(query):
    # create a unique cache key based on the query
    query_hash = hashlib.md5(query.encode()).hexdigest()
    cache_key = f"agent_response:{query_hash}"

    # check cache(read)
    cached_data = cache.get(cache_key)
    
    if cached_data:
        print(f"Found result in Redis.")
        return json.loads(cached_data)

    # cache miss -> make network call
    print(f"Data not in memory. Calling remote server...")
    data = fetch_real_data_from_slow_api(query)
    
    result = {
        "reply": f"Processed '{query}'",
        "server_origin": data.get("origin"), 
        "timestamp": time.time()
    }

    # save to cache(write). 
    # expires in 60 seconds
    cache.set(cache_key, json.dumps(result), ex=60)
    
    return result

if __name__ == "__main__":
    # ensure redis is running
    try:
        cache.ping()
    except redis.ConnectionError:
        print("Redis is not running. Run: docker run -d -p 6379:6379 redis")
        exit()

    user_query = "Explain Quantum Physics"

    print(f"Attempt 1(Network Call)")
    start = time.time()
    response = get_agent_response(user_query)
    print(f"Result: {response['reply']} (Server IP: {response['server_origin']})")
    print(f"Total Time: {time.time() - start:.2f}s")

    print(f"Attempt 2(Redis Cache)")
    start = time.time()
    response = get_agent_response(user_query)
    print(f"Result: {response['reply']} (Server IP: {response['server_origin']})")
    print(f"Total Time: {time.time() - start:.2f}s")