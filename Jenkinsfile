pipeline {
    agent any
    stages {
        stage('Build Image') {
            steps {
                sh 'docker build -t jenkins-flaskapp .'
            }
        }
        stage('Run App') {
            steps {
                sh 'docker-compose up -d'
            }
        }
        stage('Check App') {
            steps {
                sh 'curl -f http://localhost:5000 || exit 1'
            }
        }
    }
}
