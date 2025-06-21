pipeline {
    agent any
    stages {
        stage('Build Image') {
            steps {
                 {
                   sh 'docker build -f Docker/Dockerfile.app -t jenkins-flaskapp .'
                }
            }
        }
        stage('Run App') {
            steps {
                sh 'docker-compose up -d'
            }
        }
        stage('Check App') {
            steps {
                sh 'sleep 5 && curl -f http://localhost:5000 || exit 1'
            }
        }
    }
}
