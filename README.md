# QA Test for Frontend and Backend Services

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Clone the Repository](#clone-the-repository)
- [Set Up the Environment](#set-up-the-environment)
- [Deploy Services to Minikube](#deploy-services-to-minikube)
- [Run Playwright Tests](#run-playwright-tests)
- [Run the Python script for Health Monitoring](#Run-the-Python-script-for-Health-Monitoring)

## Introduction

This is a test project

## Prerequisites

Make sure you have the following installed on your system:

- [Node.js](https://nodejs.org/) (version 14 or higher)
- [Docker](https://www.docker.com/products/docker-desktop)
- [Minikube](https://minikube.sigs.k8s.io/docs/start/)
- [kubectl](https://kubernetes.io/docs/tasks/tools/)
- [Playwright](https://playwright.dev/docs/intro)

## Clone the Repository

Clone the repository to your local machine using the following command:

```sh
git clone <your-github-repo-url>
cd <repository-name>
```
## Set Up the Environment

Set up the environment to access the frontend URL

## Start Minikube with docker:
```sh
minikube start --driver=docker
```

## Build Docker Images:

```sh
docker build -t vengatesh27/backend:v1 ./backend
docker build -t vengatesh27/frontend:v1 ./frontend
```

## Push Docker Images to a Registry

```sh
docker push vengatesh27/backend:v1
docker push vengatesh27/frontend:v1
```

## Deploy Services to Minikube

```sh
kubectl apply -f ./Deployment/backend-deployment.yml
kubectl apply -f ./Deployment/frontend-deployment.yml
```

## Verify Deployments:

```sh
kubectl get deployments
kubectl get services
```

## Get the Frontend Service URL

```sh
minikube service frontend-service --url
```

## Run Playwright Tests

copy the frontend url from the previous step and replace in the script for frontendUrl variable

```sh
npm install
npx tests/accuknox.spec.js OR
npx playwright test --headed
```

## Playwright report

To get the automation report please use
```sh
  npx playwright show-report
  ```

## Access the Frontend URL

Use the URL obtained from Get the Frontend Service URL step to access the frontend service. Make sure it displays "Hello from the Backend!".


## Run the Python script for Health Monitoring

# Application Health Monitoring Script

This Python script monitors the health of an application and system by checking its HTTP status code for application at regular intervals. It logs the status to a file and prints it to the console.

## Python Prerequisites
- Python 3.x
- requests library (`pip install requests`)
- psutil   library (`pip install psutil`)


## Run the Script:
```sh
python applicationHealthMonitor.py
python systemHealthMonitor.py
```
