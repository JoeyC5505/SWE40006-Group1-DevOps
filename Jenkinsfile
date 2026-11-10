pipeline {
    agent none

    environment {
        IMAGE_NAME = 'student-task-app'
        PROD_USER = 'raqib'
        PROD_HOST = '172.20.10.3'
    }

    stages {
        stage('Clone') {
            agent { label 'vm2-docker' }
            steps {
                git branch: 'feature/docker',
                    credentialsId: 'github-repo-access',
                    url: 'https://github.com/JoeyC5505/SWE40006-Group1-DevOps.git'
            }
        }

        stage('Build') {
            agent { label 'vm2-docker' }
            steps {
                sh 'docker build -t ${IMAGE_NAME}:latest .'
            }
        }

        stage('Test') {
            agent { label 'vm2-docker' }
            steps {
                sh '''
                    docker run --rm -e PYTHONPATH=/app ${IMAGE_NAME}:latest pytest tests/ -v
                '''
            }
        }

        stage('Deploy to Production') {
            agent { label 'built-in' }
            steps {
                sshagent(['prod-server-ssh']) {
                    sh '''
                        ssh -o StrictHostKeyChecking=no ${PROD_USER}@${PROD_HOST} "
                            cd ~/SWE40006-Group1-DevOps &&
                            git fetch origin &&
                            git reset --hard origin/feature/docker &&
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