# Projeto com Minikube e Kubernetes

Este projeto utiliza o [Minikube](https://minikube.sigs.k8s.io/docs/) para simular um cluster Kubernetes local, e implementa um backend em Python e um frontend estático.
Assista esse [vídeo](https://youtu.be/SU-muVhfrGo) para entender o projeto.

## Pré-requisitos

- [Minikube](https://minikube.sigs.k8s.io/docs/start/)
- [Kubectl](https://kubernetes.io/docs/tasks/tools/)
- [Docker](https://docs.docker.com/get-docker/)
- Recomendado: 6 CPUs e 10GB de memória disponíveis

---

## Passo a Passo para executar o projeto

### 1. Clonar o repositório

```bash
git clone <URL_DO_REPOSITORIO>
cd <PASTA_DO_PROJETO>
```

### 2. Escolher o driver de acordo com o seu sistema operacional

```bash


# Funciona para Windows, MacOS e Linux
minikube config set driver docker

# Alternativa para Windows (Hyper-V)
minikube config set driver hyperv
# Alternativa para o MacOS
minikube config set driver hyperkit
# Alternativa para Linux
minikube config set driver kvm2
```

### 3. Iniciar o Minikube com recursos alocados
Dependendo da sua máquina, você pode querer reduzir os recursos alocados. O exemplo abaixo aloca 6 CPUs e 10GB de memória.

```bash
minikube start --cpus 6 --memory 10240
```

### 4. Ativar addons necessários

```bash
minikube addons enable metrics-server
minikube addons enable ingress
```

### 5. Configurar ambiente Docker do Minikube

```bash
eval "$(minikube docker-env --shell bash)"
```

### 6. Construir a imagem do backend

```bash
cd backend
minikube image build -t python-backend:latest .
cd ..
```

### 7. Construir a imagem do frontend

```bash
cd frontend
minikube image build -t static-frontend:latest .
cd ..
```

### 8. Aplicar (ou reaplicar) os manifests Kubernetes

```bash
kubectl delete -f kubernetes/
kubectl apply -f kubernetes/
```

### 9. Acessar serviços

#### Criar túnel para acessar os serviços com IP externo:

```bash
minikube tunnel
```

#### Acessar o dashboard do Kubernetes:

```bash
minikube dashboard
```

### 10. Parar o Minikube (opcional)

```bash
minikube stop
```

---

## Observação

- O túnel (`minikube tunnel`) deve permanecer ativo para acessar serviços como ingress.
