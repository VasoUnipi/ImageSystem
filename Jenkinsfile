pipeline {
    agent any
    stages {
        stage('Build Image') {
            steps {
                sh 'docker build -f Dockerfile -t jenkins-flaskapp .'
            }
        }
        stage('Run Flaskapp') {
            steps {
                sh 'docker run -d --name flaskapp_test --network=imagesystem_default -p 5001:5000 jenkins-flaskapp'
            }
        }
        stage('Health Check') {
            steps {
                sh 'sleep 5'
                sh 'curl -f http://localhost:5001'
            }
        }
    }
}
