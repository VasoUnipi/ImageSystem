pipeline {
    agent any
    stages {
        stage('Build Image') {
            steps {
                sh 'docker build -f Dockerfile -t jenkins-flaskapp .'
            }
        }
        stage('Run System') {
            steps {
                sh 'docker-compose up -d'
            }
        }
        stage('Health Check') {
            steps {
                sh 'sleep 5'
                sh 'docker-compose exec -T flaskapp curl -f http://localhost:5000'
            }
        }
    }
}
