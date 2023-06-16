import pika

# Establish connection to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq', port=5672, credentials=pika.PlainCredentials('your-username', 'your-password')))
channel = connection.channel()

# Declare a queue to publish messages
channel.queue_declare(queue='your-queue-name')

# Publish messages to the queue
messages = ["Message 1", "Message 2", "Message 3"]

for message in messages:
    channel.basic_publish(exchange='', routing_key='your-queue-name', body=message)
    print(f"Published message: {message}")

# Close the connection
connection.close()
