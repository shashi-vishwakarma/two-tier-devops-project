pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                sh 'docker build -t flask-app:${BUILD_NUMBER} .'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker compose down'
                sh 'BUILD_NUMBER=${BUILD_NUMBER} docker compose up -d'
            }
        }
        stage('Health Check') {
            steps {
                sh '''
                sleep 10
                curl -f http://localhost:5000/health
                '''
            }
        }

    }
}
