pipeline {
    agent any

    environment {
        DEPLOY_DIR = "C:\\Users\\vinod_jakhar\\Documents\\codebases\\live\\TestCICDCode"
    }

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'master',
                    url: 'https://github.com/vndjkhr/TestCICD.git',
                    credentialsId: 'github-token'
            }
        }

        stage('Prepare Deployment Folder') {
            steps {
                bat """
                if not exist "%DEPLOY_DIR%" (
                    mkdir "%DEPLOY_DIR%"
                )
                """
            }
        }

        stage('Deploy Code to Live Folder') {
            steps {
                bat """
                xcopy /E /Y /I * "%DEPLOY_DIR%"
                """
            }
        }

        stage('Run Deployment Marker') {
            steps {
                dir('C:\\Users\\vinod_jakhar\\Documents\\codebases\\live\\TestCICDCode') {
                    bat """
                    python deploy_marker.py
                    """
                }
            }
        }
    }

    post {
        success {
            echo "✅ CI/CD Demo Deployment Successful"
        }
        failure {
            echo "❌ CI/CD Demo Deployment Failed"
        }
    }
}
