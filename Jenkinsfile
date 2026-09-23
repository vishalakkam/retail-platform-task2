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
                echo 'Building application'
            }
        }

        stage('Test') {
            steps {
                echo 'Running application tests'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application'
            }
        }

        stage('Validate') {
            steps {
                echo 'Validating application'
            }
        }

    }
}