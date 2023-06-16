# k8s-sample-application

# Application Description:
- Frontend (frontend.yaml): Deploys a Kubernetes Pod running NGINX that will output messages placed on a specific RabbitMQ queue
- Backend (backend.yaml): Deploys a Kubernetes Pod running RabbitMQ
- Producer (producer.py): Runs a Python script that will generate messages to a specific RabbitMQ queue that it creates

# Requirements:
- Local system where the Producer is excuted needs to have the Pika Python module installed
