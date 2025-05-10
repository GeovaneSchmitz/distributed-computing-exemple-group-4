#!/bin/bash

cd $(dirname "$0") || exit 1

eval "$(minicube docker-env)"
cd backend

docker build -t python-backend:latest .
cd ../frontend

docker build -t static-frontend:latest .

cd ..
# re deploy the images to kubernetes
kubectl delete -f kubernetes/
kubectl apply -f kubernetes/
