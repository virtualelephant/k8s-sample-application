# k8s-sample-application

# Application Description:
- Frontend (frontend.yaml): Deploys a Kubernetes Pod running NGINX that will output messages placed on a specific RabbitMQ queue
- Backend (backend.yaml): Deploys a Kubernetes Pod running RabbitMQ
- Publisher (publisher.yaml): Runs a Python script that will generate messages to a specific RabbitMQ queue that it creates

# Docker container for Producer
- Custom Docker container that is leveraged within the sample application to generate messages to the Backend RabbitMQ service
- publisher.py (Python file) - Generates 3 messages, with a timestamp, and sends them to the RabbitMQ queue
- publisher.sh (Script file) - Executes a cronjob inside the container to generate messages every minute

# Requirements:
- Local system should have Docker to build the Publisher container
- Docker repository to push the Publisher container
