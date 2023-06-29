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
- Container/Dockerfile - Custom Docker container that is leveraged within the sample application to generate messages to the Backend RabbitMQ service
- Container/publisher.py (Python file) - Generates 3 messages, with a timestamp, and sends them to the RabbitMQ queue
- Container/publisher.sh (Script file) - Executes a cronjob inside the container to generate messages every minute

To use the Publisher part of the application, you will need to build the Docker container and upload it. I uploaded my version
of the container into a private Harbor registry that I have running inside my VMware SDDC.

$ docker build -t publisher:latest .
$ docker tag publisher:latest <private-registry>/publisher:latest
$ docker push <private-registry>/publisher:latest

# Requirements:
- Local system should have Docker to build the Publisher container
- Docker repository to push the Publisher container
