import pika
import time

host = 'rabbitmq.sample-app.svc.cluster.local'
port = 5672
credentials = pika.PlainCredentials('deploy', 'VMware123!', 'external')
# Establish connection to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(host=host, port=port, credentials=credentials))
channel = connection.channel()

# Declare a queue to publish messages
channel.queue_declare(queue='log-messages')

# Publish messages to the queue
messages = ["INFO: Successfully initialized sample application version 0.1 ", "WARNING: Connection timeout issue while attempting to connect to sample application", "DEBUG: Executing background task: Cleaning up temp files"]

for message in messages:
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    body = f"{timestamp} - {message}"
    channel.basic_publish(exchange='', routing_key='log-messages', body=body)
    print(f"Published message: {body}")

# Close the connection
connection.close()
