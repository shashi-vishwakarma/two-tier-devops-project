# Two-Tier Web Application Deployment using Docker & Jenkins
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Jenkins](https://img.shields.io/badge/Jenkins-D24939?style=for-the-badge&logo=jenkins&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazonaws&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)


## Project Overview

This project demonstrates a complete CI/CD pipeline for deploying a two-tier web application using Docker, Docker Compose, Jenkins, GitHub Webhooks, and AWS EC2.

The application consists of a Flask web application and a MySQL database running inside Docker containers. Jenkins automatically builds and deploys the application whenever new code is pushed to GitHub.

---

## 📐 Architecture

```text
                    +----------------------+
                    |      Developer       |
                    +----------+-----------+
                               |
                          git push
                               |
                               ▼
                    +----------------------+
                    |       GitHub         |
                    +----------+-----------+
                               |
                      GitHub Webhook
                               |
                               ▼
                    +----------------------+
                    |      Jenkins         |
                    |  CI/CD Pipeline      |
                    +----------+-----------+
                               |
                  Build Docker Image
                  flask-app:${BUILD_NUMBER}
                               |
                               ▼
                    +----------------------+
                    |   Docker Compose     |
                    +----------+-----------+
                               |
                 +-------------+-------------+
                 |                           |
                 ▼                           ▼
      +------------------+        +------------------+
      | Flask Container  | <----> | MySQL Container  |
      | employee-app     |        | mysql-container  |
      +------------------+        +------------------+
                 |
                 ▼
          Browser :5000
```
---

## Tech Stack

- Linux (Ubuntu)
- Git
- GitHub
- Docker
- Docker Compose
- Jenkins
- AWS EC2
- Flask
- MySQL

---

## Features

- Dockerized Flask Application
- MySQL Database Container
- Docker Compose Deployment
- Jenkins CI/CD Pipeline
- Automatic Deployment using GitHub Webhook
- Health Check Endpoint
- Dynamic Docker Image Tagging
- Automatic Database Initialization
- Production-style Deployment Workflow

---

## Jenkins Pipeline

1. Checkout Source Code
2. Build Docker Image
3. Test Stage
4. Deploy Containers
5. Health Check

---

## Project Structure

```text
two-tier-devops-project/
│
├── app/
│   ├── app.py
│   └── requirements.txt
│
├── screenshots/
├── Dockerfile
├── docker-compose.yml
├── Jenkinsfile
├── init.sql
└── README.md
```

---
## 🚀 Installation
### Clone the Repository

```bash
git clone git@github.com:shashi-vishwakarma/two-tier-devops-project.git
```

### Navigate to the Project Directory

```bash
cd two-tier-devops-project
```

### Start the Application

```bash
docker compose up -d
```

### Verify Running Containers

```bash
docker ps
```

### Access the Application

```text
http://<EC2-Public-IP>:5000
```

## Health Check

```
GET /health
```

Returns

```json
{
  "status":"healthy"
}
```

---

## CI/CD Flow

Git Push

↓

GitHub Webhook

↓

Jenkins Pipeline

↓

Docker Image Build

↓

Docker Compose Deployment

↓

Health Check

↓

Application Live

---
## 🔧 Challenges & Solutions

### 1. MySQL Initialization Issue

**Problem**

The `employees` table was not created because the existing Docker volume prevented `init.sql` from running.

**Solution**

Removed the old Docker volume and recreated the containers so MySQL executed the initialization script.

---

### 2. Exit Code 137

**Problem**

The application container stopped with Exit Code 137 due to insufficient memory on the EC2 instance.

**Solution**

Added swap memory and restarted the deployment.

---

### 3. Jenkins Authentication Issue

**Problem**

Jenkins was unable to clone the GitHub repository.

**Solution**

Configured SSH keys and added the GitHub credentials in Jenkins.

---

### 4. GitHub Webhook

**Problem**

The pipeline had to be started manually after every code change.

**Solution**

Configured a GitHub Webhook to automatically trigger the Jenkins pipeline on every push.

---

### 5. Dynamic Docker Image Tagging

**Problem**

Every build overwrote the same Docker image (`flask-app:v1`).

**Solution**

Configured Jenkins to create uniquely tagged Docker images using the build number and deployed those images through Docker Compose.

## 📚 Skills Learned

- Linux Administration
- Git & GitHub
- Docker
- Docker Compose
- Jenkins CI/CD
- AWS EC2
- GitHub Webhooks
- Flask Deployment
- MySQL Integration
- Docker Networking
- Health Checks
- Dynamic Docker Image Tagging
- CI/CD Pipeline Automation
- Docker Troubleshooting
- Jenkins Troubleshooting


## Future Improvements

- Terraform
- Kubernetes
- Monitoring
- Grafana
- Prometheus

---

## Author

Shashi Vishwakarma
