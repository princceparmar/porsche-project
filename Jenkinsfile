pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out Porsche project from GitHub'
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing dependencies'
                sh 'python3 -m pip install pytest --break-system-packages --quiet'
            }
        }

        stage('Build') {
            steps {
                echo 'Building / Running Porsche application'
                sh 'python3 app.py'
            }
        }

        stage('Test') {
            steps {
                echo 'Running automated tests'
                sh 'pytest test_app.py -v'
            }
        }
    }

    post {
        success {
            echo 'Porsche project build and tests completed successfully.'
        }

        failure {
            echo 'Porsche project build failed - check the console output.'
        }
    }
}
