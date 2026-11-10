pipeline {
    agent any

    environment {
        IMAGE_NAME = 'student-task-app'
        PROD_USER = 'raqib'
        PROD_HOST = '172.20.10.3'
    }

    stages {
        stage('Clone') {
            steps {
                git branch: 'feature/docker',
                    credentialsId: 'github-repo-access',
                    url: 'https://github.com/JoeyC5505/SWE40006-Group1-DevOps.git'
            }
        }

        stage('Build') {
            steps {
                sh 'docker build -t ${IMAGE_NAME}:latest .'
            }
        }

        stage('Test') {
    steps {
        sh '''
            docker run --rm -e PYTHONPATH=/app student-task-app:latest pytest tests/ -v
        '''
    }
}

        stage('Deploy to Production') {
            steps {
                sshagent(['prod-server-ssh']) {
                    sh '''
                        ssh -o StrictHostKeyChecking=no ${PROD_USER}@${PROD_HOST} "
                            cd ~/SWE40006-Group1-DevOps &&
                            git pull origin main &&
                            docker compose down &&
                            docker compose up -d --build
                        "
                    '''
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline complete - deployed to production successfully.'
        }
        failure {
            echo 'Pipeline failed - production deployment skipped.'
        }
    }
}