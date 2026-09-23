pipeline {
    agent any

    parameters {
    choice(
        name: 'ENVIRONMENT',
        choices: ['DEV', 'UAT', 'PRODUCTION'],
        description: 'Select deployment environment'
    )

    choice(
        name: 'ACTION',
        choices: ['DEPLOY', 'ROLLBACK'],
        description: 'Select deployment action'
    )

    string(
        name: 'VERSION',
        defaultValue: '5.0.1',
        description: 'Docker image version'
    )
}

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
                bat '"C:\\Users\\Vishal Akkam\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" rm -f customer-app-jenkins 2>NUL'
                bat '"C:\\Users\\Vishal Akkam\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" run -d --name customer-app-jenkins -p 8084:8081 customer-app:5.0.1'
            }
        }

        stage('Validate') {
            steps {
                echo 'Validating application'
            }
        }

    }
}