pipeline {
    agent any
    stages {
        stage('Build Image') {
            steps {
                sh 'docker build -f Docker/Dockerfile.app -t jenkins-flaskapp .'
            }
        }
        stage('Run System') {
            steps {
                sh 'docker-compose up -d'
            }
        }
        stage('Health Check') {
            steps {
                sh 'sleep 5 && curl -f http://localhost:5000 || exit 1'
            }
        }
    }
}
