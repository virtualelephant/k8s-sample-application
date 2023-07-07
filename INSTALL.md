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

Wait until the StatefulSet for RabbitMQ is online. From there you can get the default username and password.

```
username="$(kubectl get secret rabbitmq-default-user -o jsonpath='{.data.username}' | base64 --decode)"
echo "username: $username"
password="$(kubectl get secret rabbitmq-default-user -o jsonpath='{.data.password}' | base64 --decode)"
echo "password: $password"
```

If the application is being run inside a Tanzu Kubernetes Grid cluster with NSX ALB, the following HTTPProxy object can be leveraged to expose the RabbitMQ UI.

```
kubectl apply -f rabbitmq-httpproxy.yaml
```

If you have an Ingress controller installed, such as HAProxy, the following Ingress object can be leveraged to expose the RabbitMQ UI.

```
kubectl apply -f rabbitmq-ingress.yaml
```

### Create the Publisher Deployment to generate messages into RabbitMQ
```
kubectl apply -f publisher.yaml
```

### Create the Frontend Deployments to read the messages and display them in a webpage
```
kubectl apply -f frontend-storage.yaml
kubectl apply -f html-configmap.yaml
kubectl apply -f frontend-reader.yaml
kubectl apply -f frontend.yaml
```

Again, if the environment is leveraging NSX ALB, create the HTTPProxy to expose NGINX.
```
kubectl apply -f frontend-httpproxy.yaml
```

Otherwise, leverage the Ingress object to expose NGINX.
```
kubectl apply -f frontend-ingress.yaml
```