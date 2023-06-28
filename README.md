# k8s-sample-application
Sample application for running inside Kubernetes to demonstrate different pieces of technology.

# Application Description:
- Frontend Application: Deploys  NGINX that will output messages placed on a specific RabbitMQ queue
- Backend Application: Deploys RabbitMQ for a messaging queue service
- Publisher Application: Runs a Python script that will generate messages to a specific RabbitMQ queue that it creates

# Backend Application:
- backend-statefulset.yaml: Creates a RabbitMQ stateful set, service accounts, service
- backend-storage.yaml: Creates the persistent volume, via an NFS mount, for RabbitMQ

# Docker container for Publisher
- Custom Docker container that is leveraged within the sample application to generate messages to the Backend RabbitMQ service
- publisher.py (Python file) - Generates 3 messages, with a timestamp, and sends them to the RabbitMQ queue
- publisher.sh (Script file) - Executes a cronjob inside the container to generate messages every minute

# Requirements:
- Local system should have Docker to build the Publisher container
- Docker repository to push the Publisher container
