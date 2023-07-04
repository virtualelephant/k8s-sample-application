# Installation Guide

After downloading the files or cloning the Git repo to the Linux host where you will be deploying the application from, run the following commands:

### Create sample-app namespace and switch context
```
kubectl create namespace sample-app
```
```
kubectl config set-context --current --namespace=sample-app
```

### Create the storage class (assumes the NFS Client Provisioner is already setup)
```
kubectl apply -f storageclass.yaml
```

### Create the RabbitMQ cluster in the sample-app namespace
```
kubectl apply -f rabbitmq-prod.yaml
```