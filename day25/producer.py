import pika
import json

def send_url_to_queue(url):
    # connect to RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # declare the queue
    channel.queue_declare(queue='scrape queue')

    # send the URL
    message = json.dumps({"url": url})
    channel.basic_publish(exchange='',
                          routing_key='scrape queue',
                          body=message)
    
    print(f"Queued URL: {url}")
    connection.close()

if __name__ == "__main__":
    # list of websites to scrape
    targets = [
        "https://www.google.com",
        "https://www.python.org",
        "https://www.github.com",
        "https://www.wikipedia.org"
    ]

    print("Manager Dispatching Jobs...")
    for target in targets:
        send_url_to_queue(target)
    
    print("All Jobs Dispatched...")