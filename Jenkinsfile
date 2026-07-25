pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'git@github.com:shashi-vishwakarma/two-tier-devops-project.git'
            }
        }
    }
}
