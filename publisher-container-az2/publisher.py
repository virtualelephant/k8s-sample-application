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
messages = ["INFO: [AZ2] Successfully initialized Sample Application version 1.0 ", "INFO: [AZ2] Download Sample Application via Git from https://github.com/virtualelephant/k8s-sample-application.git", "INFO: [AZ2] Sample Application Log Message #1", "INFO: [AZ2] Sample Application Log Message #2", "INFO: [AZ2] Sample Application Log Message #3"]

for message in messages:
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    body = f"{timestamp} - {message}"
    channel.basic_publish(exchange='', routing_key='log-messages', body=body)
    print(f"Published message: {body}")

# Close the connection
connection.close()
