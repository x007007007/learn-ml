pipeline {
    agent any
    stages {
        stage('Check & install env') {
            steps {
                bat "pip config set global.index-url http://mirrors.aliyun.com/pypi/simple/"
                bat "pip config set global.trusted-host mirrors.aliyun.com"
                bat "python initial-env.py "
            }
        }
        stage('Test') {
            steps {
                //
            }
        }
        stage('Deploy') {
            steps {
                //
            }
        }
    }
}