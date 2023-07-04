# k8s-sample-application
Sample application for running inside Kubernetes to demonstrate different pieces of technology.

# Application Description:
- Frontend Application: Deploys  NGINX that will output messages placed on a specific RabbitMQ queue
- Backend Application: Deploys RabbitMQ for a messaging queue service
- Publisher Application: Runs a Python script that will generate messages to a specific RabbitMQ queue that it creates

# Frontend (NGINX) Application:
- frontend-httpproxy.yaml - Frontend access through NSX ALB using the httpproxy object inside Kubernetes
- frontend-storage.yaml - PersistentVolume and PersistentVolumeClaim that is shared by both the frontend (nginx) Deployment and the frontend-reader (Python script) Deployment to store the index.html file
- frontend.yaml - NGINX Deployment and service
- frontend-reader.yaml - Python container running the reader.py script through cron that pulls the messages off the RabbitMQ queue
- html-configmap.yaml - File shared by both the frontend services

# Backend (RabbitMQ) Application:
I used the built in RabbitMQ cluster operator functionality that is available here and modified the 'production-ready' YAML
https://www.rabbitmq.com/kubernetes/operator/quickstart-operator.html

- rabbitmq-prod.yaml: Creates a RabbitMQ stateful set, service accounts, service
- rabbitmq-httpproxy.yaml: Creates the HTTPProxy for RabbitMQ

# Docker container for RabbitMQ Reader
- reader-container/Dockerfile - Customer Docker container that has a Python script running in cron that reads the messages written to the RabbitMQ queue 'log-messages'
- reader-container/reader.py (Python file) - Reads messagess off of the RabbitMQ queue
- reader-container/requirements.txt - Extra packages that are needed inside the Docker container

To use the Reader part of the application, you will need to build the Docker container and upload it to a repo.
$ docker build -t reader:latest .
$ docker tag reader:latest <private-registry>/reader:latest
$ docker push <private-registry>/reader:latest

# Docker container for NGINX
- nginx-container/Dockerfile - Simple nginx container

To use the NGINX part of the application, you will need to build the Docker container and upload it to a repo.
$ docker build -t frontend-nginx:latest .
$ docker tag frontend-nginx:latest <private-registry>/frontend-nginx:latest
$ docker push <private-registry>/frontend-nginx:latest

# Docker container for RabbitMQ Publisher
- publisher-ontainer/Dockerfile - Custom Docker container that is leveraged within the sample application to generate messages to the Backend RabbitMQ service
- publisher-container/publisher.py (Python file) - Generates 3 messages, with a timestamp, and sends them to the RabbitMQ queue
- publisher-container/requirements.txt - Extra packages that need to be installed inside the Docker container

To use the Publisher part of the application, you will need to build the Docker container and upload it to a repo.

$ docker build -t publisher:latest .
$ docker tag publisher:latest <private-registry>/publisher:latest
$ docker push <private-registry>/publisher:latest

# Requirements:
- Local system should have Docker to build the Publisher container
- Container repository to push the Publisher container
- RabbitMQ Cluster Operator
- NFS Client Provisioner for Kubernetes

# Installing RabbitMQ Cluster Operator

https://www.rabbitmq.com/kubernetes/operator/quickstart-operator.html

$ kubectl apply -f "https://github.com/rabbitmq/cluster-operator/releases/latest/download/cluster-operator.yml"

# Installing NFS Client Provisioner
https://github.com/kubernetes-sigs/nfs-subdir-external-provisioner

$ helm repo add nfs-subdir-external-provisioner https://kubernetes-sigs.github.io/nfs-subdir-external-provisioner/
$ helm install nfs-subdir-external-provisioner nfs-subdir-external-provisioner/nfs-subdir-external-provisioner \
    --set nfs.server=x.x.x.x \
    --set nfs.path=/exported/path
