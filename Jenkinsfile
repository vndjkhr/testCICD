pipeline {
    agent any

    environment {
        SRC_DIR = "Documents\\local\\TestCICDCode"
        DEPLOY_DIR = "Documents\\Live\\TestCICDCode"
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'master',
                    url: 'https://github.com/vndjkhr/TestCICD.git',
                    credentialsId: 'github-token'
            }
        }

        stage('Prepare Deploy Folder') {
            steps {
                bat '''
                if not exist "%DEPLOY_DIR%" mkdir "%DEPLOY_DIR%"
                '''
            }
        }

        stage('Deploy Code') {
            steps {
                bat '''
                xcopy /E /Y * "%DEPLOY_DIR%"
                '''
            }
        }

        stage('Run Deployment Script') {
            steps {
                dir('Documents\\Live\\TestCICDCode') {
                    bat '''
                    python deploy_marker.py
                    '''
                }
            }
        }
    }

    post {
        success {
            echo "✅ Deployment successful"
        }
        failure {
            echo "❌ Deployment failed"
        }
    }
}
