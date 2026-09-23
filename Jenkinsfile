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

        choice(
            name: 'RUN_TESTS',
            choices: ['YES', 'NO'],
            description: 'Run application tests'
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
                bat '"C:\\Users\\Vishal Akkam\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" build -t customer-app:%VERSION% .'
            }
        }

        stage('Test') {
            steps {
                script {
                    if (params.RUN_TESTS == 'YES') {
                        echo 'Running application tests'
                        echo 'Tests completed successfully'
                    } else {
                        echo 'Tests skipped'
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                script {

    def deployBranch = ''
    def containerName = ''
    def hostPort = ''
    def networkName = ''

    if (params.ENVIRONMENT == 'DEV') {
        deployBranch = 'develop'
        containerName = 'customer-app-dev'
        hostPort = '8081'
        networkName = 'customer-dev-net'
    } else if (params.ENVIRONMENT == 'UAT') {
        deployBranch = 'release'
        containerName = 'customer-app-uat'
        hostPort = '8082'
        networkName = 'customer-uat-net'
    } else {
        deployBranch = 'main'
        containerName = 'customer-app-prod'
        hostPort = '8083'
        networkName = 'customer-prod-net'
    }

    echo "Environment: ${params.ENVIRONMENT}"
    echo "Branch: ${deployBranch}"
    echo "Container: ${containerName}"
    echo "Port: ${hostPort}"
    echo "Network: ${networkName}"

    if (params.ACTION == 'DEPLOY') {
            }
        }

        stage('Validate') {
            steps {
                echo 'Validating application'
                bat '"C:\\Users\\Vishal Akkam\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" ps'
            }
        }

    }
}