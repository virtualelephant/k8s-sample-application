import pika
import time

# Establish connection to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq', port=5672, credentials=pika.PlainCredentials('your-username', 'your-password')))
channel = connection.channel()

# Declare a queue to publish messages
channel.queue_declare(queue='your-queue-name')

# Publish messages to the queue
messages = ["Message 1", "Message 2", "Message 3"]

for message in messages:
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    body = f"{timestamp} - {message}"
    channel.basic_publish(exchange='', routing_key='your-queue-name', body=body)
    print(f"Published message: {body}")

# Close the connection
connection.close()
