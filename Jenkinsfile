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
        bat '"C:\\Users\\Vishal Akkam\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" build -t customer-app:5.0.1 .'
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