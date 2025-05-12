#!/bin/bash

cd $(dirname "$0") || exit 1
# for linux
#minikube config set driver kvm2
# for windows 
#minikube config set driver docker
# for mac
# minikube config set driver hyperkit
#minikube start
sleep 5
minikube start --cpus 6 --memory 10240

minikube addons enable metrics-server
minikube addons enable ingress
eval "$(minikube docker-env --shell bash)"
cd backend

minikube image build -t python-backend:latest .
cd ../frontend

minikube image build -t static-frontend:latest .

cd ..
# re deploy the images to kubernetes
kubectl delete -f kubernetes/
kubectl apply -f kubernetes/
