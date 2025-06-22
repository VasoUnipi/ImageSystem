// Ορίζεται ένα declarative pipeline
pipeline {
    // Εκτέλεση του pipeline σε οποιοδήποτε διαθέσιμο Jenkins agent
    agent any
    // Παράλειψη του default checkout (το οποίο επιχειρεί να κάνει αυτόματα checkout από το repo)
    options {
        skipDefaultCheckout(true)
    }
     // Ορισμός των σταδίων του pipeline
    stages {
        // 1ο Στάδιο: Δημιουργία Docker image για το Flask app
        stage('Build Image') {
            steps {
                // Εκτέλεση εντολής build του Dockerfile με όνομα image: jenkins-flaskapp
                sh 'docker build -f Dockerfile -t jenkins-flaskapp .'
            }
        }
        // 2ο Στάδιο: Εκτέλεση του container με το Flask app
        stage('Run Flaskapp') {
            steps {
                // Αν υπάρχει ήδη container με το όνομα flaskapp_test, τον αφαιρεί
                sh 'docker rm -f flaskapp_test || true'
                // Εκκινεί νέο κοντέινερ από το image jenkins-flaskapp
                // Ο container συνδέεται στο Docker network με όνομα imagesystem_default
                // Εκθέτει τη θύρα 5000 του app στη 5001 του host για δοκιμή
                sh 'docker run -d --rm --name flaskapp_test --network=imagesystem_default -p 5001:5000 jenkins-flaskapp'
            }
        }
        // 3ο Στάδιο: Έλεγχος διαθεσιμότητας της εφαρμογής (health check)
        stage('Health Check') {
            steps {
                // Αναμονή 5 δευτερολέπτων για να ξεκινήσει η εφαρμογή
                sh 'sleep 5'
                // Αποστολή HTTP request προς το container – αν αποτύχει, το build αποτυγχάνει
                sh 'curl -f http://flaskapp_test:5000'
            }
        }
    }
}
