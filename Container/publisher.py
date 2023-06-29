import pika
import time

# Establish connection to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq', port=5672, credentials=pika.PlainCredentials('rbqadmin', 'VMware123!')))
channel = connection.channel()

# Declare a queue to publish messages
channel.queue_declare(queue='sample-application')

# Publish messages to the queue
messages = ["INFO: Successfully initialized sample pplication version 0.1 ", "WARNING: Connection timeout issue while attempting to connect to sample application", "DEBUG: Executing background task: Cleaning up temp files"]

for message in messages:
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    body = f"{timestamp} - {message}"
    channel.basic_publish(exchange='', routing_key='sample-application', body=body)
    print(f"Published message: {body}")

# Close the connection
connection.close()
