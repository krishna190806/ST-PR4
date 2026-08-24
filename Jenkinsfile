pipeline {
   agent any

   stages {
       stage('Clone') {
           steps {
               echo 'Cloning repository...'
               checkout scm
           }
       }

       stage('Build') {
           steps {
               echo 'Installing dependencies...'
               sh 'pip3 install --break-system-packages -r requirements.txt'
           }
       }

       stage('Test') {
           steps {
               echo 'Running test cases...'
               sh 'python3 -m pytest test_app.py -v'
           }
       }
   }

   post {
       success {
           echo 'Pipeline finished successfully!'
       }
       failure {
           echo 'Pipeline failed. Check console output above.'
       }
   }
}
