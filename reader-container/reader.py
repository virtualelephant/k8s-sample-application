import pika
import os

host = 'rabbitmq.sample-app.svc.cluster.local'
port = 5672
credentials = pika.PlainCredentials('deploy', 'VMware123!', 'external')
# Establish connection to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(host=host,port=port,credentials=credentials))

channel = connection.channel()
channel.queue_declare(queue='log-messages')

def callback(ch, method, properties, body):
    message = body.decode()
    with open('/usr/share/nginx/html/index.html', 'a') as file:
        file.write(f'<p>{message}</p>\n')

channel.basic_consume(queue='log-messages', on_message_callback=callback, auto_ack=True)
channel.start_consuming()