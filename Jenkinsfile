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
            defaultValue: '5.0.2',
            description: 'Docker image version to deploy or rollback to'
        )

        choice(
            name: 'RUN_TESTS',
            choices: ['YES', 'NO'],
            description: 'Run application tests'
        )
    }

    stages {

        stage('Select Environment') {
            steps {
                script {

                    if (params.ENVIRONMENT == 'DEV') {

                        env.DEPLOY_BRANCH = 'develop'
                        env.CONTAINER_NAME = 'customer-app-dev'
                        env.HOST_PORT = '8081'
                        env.NETWORK_NAME = 'customer-dev-net'
                        env.DB_CONTAINER = 'customer-db-dev'
                        env.DB_PASSWORD = 'customer123'

                    } else if (params.ENVIRONMENT == 'UAT') {

                        env.DEPLOY_BRANCH = 'release'
                        env.CONTAINER_NAME = 'customer-app-uat'
                        env.HOST_PORT = '8082'
                        env.NETWORK_NAME = 'customer-uat-net'
                        env.DB_CONTAINER = 'customer-db-uat'
                        env.DB_PASSWORD = 'uatcustomer123'

                    } else {

                        env.DEPLOY_BRANCH = 'main'
                        env.CONTAINER_NAME = 'customer-app-prod'
                        env.HOST_PORT = '8083'
                        env.NETWORK_NAME = 'customer-prod-net'
                        env.DB_CONTAINER = 'customer-db-prod'
                        env.DB_PASSWORD = 'prodcustomer123'
                    }

                    echo "Environment: ${params.ENVIRONMENT}"
                    echo "Branch: ${env.DEPLOY_BRANCH}"
                    echo "Container: ${env.CONTAINER_NAME}"
                    echo "Port: ${env.HOST_PORT}"
                    echo "Network: ${env.NETWORK_NAME}"
                    echo "Database: ${env.DB_CONTAINER}"
                }
            }
        }


        stage('Checkout') {
            steps {
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: "*/${env.DEPLOY_BRANCH}"]],
                    userRemoteConfigs: [[
                        url: 'https://github.com/vishalakkam/retail-platform-task2.git'
                    ]]
                ])
            }
        }


        stage('Build') {
            when {
                expression {
                    params.ACTION == 'DEPLOY'
                }
            }

            steps {
                echo "Building Docker image version ${params.VERSION}..."

                bat '"C:\\Users\\Vishal Akkam\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" build -t customer-app:%VERSION% .'
            }
        }


        stage('Test') {
            when {
                expression {
                    params.RUN_TESTS == 'YES'
                }
            }

            steps {
                echo 'Running application tests inside Docker...'

                bat '"C:\\Users\\Vishal Akkam\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" run --rm customer-app:%VERSION% python -m compileall /app'

                echo 'Tests completed successfully'
            }
        }


        stage('Production Confirmation') {
            when {
                expression {
                    params.ENVIRONMENT == 'PRODUCTION' &&
                    params.ACTION == 'DEPLOY'
                }
            }

            steps {
                input(
                    message: 'Confirm PRODUCTION deployment?',
                    ok: 'Deploy to Production'
                )
            }
        }


        stage('Deploy / Rollback') {
            steps {
                script {

                    if (params.ACTION == 'DEPLOY') {

                        echo "Starting deployment..."
                        echo "Environment: ${params.ENVIRONMENT}"
                        echo "Version: ${params.VERSION}"

                        bat """
"C:\\Users\\Vishal Akkam\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" network inspect ${env.NETWORK_NAME} >NUL 2>&1
if errorlevel 1 (
    "C:\\Users\\Vishal Akkam\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" network create ${env.NETWORK_NAME}
)
"""

                        bat """
"C:\\Users\\Vishal Akkam\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" rm -f ${env.CONTAINER_NAME} 2>NUL
"""

                        bat """
"C:\\Users\\Vishal Akkam\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" run -d --name ${env.CONTAINER_NAME} --network ${env.NETWORK_NAME} -p ${env.HOST_PORT}:8081 -e DB_HOST=${env.DB_CONTAINER} -e DB_USER=customeruser -e DB_PASSWORD=${env.DB_PASSWORD} -e DB_NAME=customerdb customer-app:%VERSION%
"""

                        echo 'Deployment completed successfully'

                    } else {

                        echo "Starting rollback..."
                        echo "Environment: ${params.ENVIRONMENT}"
                        echo "Rollback version: ${params.VERSION}"

                        bat """
"C:\\Users\\Vishal Akkam\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" rm -f ${env.CONTAINER_NAME} 2>NUL
"""

                        bat """
"C:\\Users\\Vishal Akkam\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" run -d --name ${env.CONTAINER_NAME} --network ${env.NETWORK_NAME} -p ${env.HOST_PORT}:8081 -e DB_HOST=${env.DB_CONTAINER} -e DB_USER=customeruser -e DB_PASSWORD=${env.DB_PASSWORD} -e DB_NAME=customerdb customer-app:%VERSION%
"""

                        echo 'Rollback completed successfully'
                    }
                }
            }
        }


        stage('Validate') {
            steps {

                echo "Validating ${params.ENVIRONMENT} environment..."

                bat """
"C:\\Users\\Vishal Akkam\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" ps --filter "name=${env.CONTAINER_NAME}"
"""

                bat """
powershell -Command "(Invoke-WebRequest -UseBasicParsing http://localhost:${env.HOST_PORT}/health).Content"
"""

                bat """
powershell -Command "(Invoke-WebRequest -UseBasicParsing http://localhost:${env.HOST_PORT}/db-test).Content"
"""

                echo 'Application and database validation completed successfully'
            }
        }
    }


    post {

        success {
            echo 'CI/CD Pipeline completed successfully.'
        }

        failure {
            echo 'CI/CD Pipeline failed. Check the Console Output.'
        }
    }
}