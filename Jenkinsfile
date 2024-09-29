pipeline{
    agent any
    stages {
        stage ('build') {
            steps {
                script {
                    echo 'building phase'
                }
            }
        }
        stage ('test'){
            steps {
                script{
                    echo 'testing phase'
                    bat 'python -m unittest discover'
                }
            }
        }
    }
    post {
        always{
            echo 'cleaning'
        }
        success{
            echo 'success' 
        }
        failure{
            echo 'failed'
        }
    }
}