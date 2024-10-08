pipeline {
    agent {
        docker {
            image 'python:3.9-slim'
        }
    }
    stages {
        stage('Clone Repository') {
            steps {
                script {
                    git branch: 'main', url: 'https://github.com/ShijithDG/myAddBuild.git'
                }
            }
        }
        stage('Build') {
            steps {
                script {
                    echo 'Building phase'
                    // Replace with actual build commands if needed
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    echo 'Testing phase'
                    // Use python3 explicitly
                    sh 'python3 -m unittest discover'
                }
            }
        }
    }
    post {
        always {
            echo 'Cleaning up...'
            cleanWs()
        }
    }
}
