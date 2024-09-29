pipline{
    agent any
    stages {
        stage ('build') {
            echo 'building phase'
        }
        stage ('Testing') {
            echo 'Testing phase'
            bat 'python -m unittest discover'
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