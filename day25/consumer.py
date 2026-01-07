import pika
import json
import requests
import time

def scrape_website(ch, method, properties, body):
    """Callback function that performs the work"""
    data = json.loads(body)
    url = data['url']
    
    print(f"Worker picked up {url}")
    
    try:
        # perform a HTTP request
        start_time = time.time()
        response = requests.get(url, timeout=10)
        duration = time.time() - start_time
        
        # analyze the data
        page_size = len(response.content)
        status = response.status_code
        
        print(f"Status: {status} | Size: {page_size/1024:.2f} KB | Time: {duration:.2f}s")

    except Exception as e:
        print(f"Failed to scrape {url}: {e}")

    # acknowledge the message(tell RabbitMQ, so it can delete the task)
    ch.basic_ack(delivery_tag=method.delivery_tag)

def start_worker():
    # connect
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # declare queue
    channel.queue_declare(queue='scrape queue')
    
    # only allow 1 unacknowledged message at a time
    # this prevents one worker from getting swamped if tasks vary in size
    channel.basic_qos(prefetch_count=1)

    # listen
    channel.basic_consume(queue='scrape queue', on_message_callback=scrape_website)

    print('Worker Agent Online. Waiting for URLs...')
    channel.start_consuming()

if __name__ == "__main__":
    try:
        start_worker()
    except KeyboardInterrupt:
        print("Worker stopping...")