pipeline {
    agent any
    stages {
        stage('Check & install env') {
            githubNotify status: "PENDING", credentialsId: "github-x007007007-token", account: "x007007007", repo: "learn-ml"

            steps {
                bat "pip config set global.index-url http://mirrors.aliyun.com/pypi/simple/"
                bat "pip config set global.trusted-host mirrors.aliyun.com"
                bat "python initial-env.py "
            }
        }
    }
    post {
        always {
            echo 'One way or another, I have finished'
        }
        success {
            githubNotify status: "SUCCESS", credentialsId: "github-x007007007-token", account: "x007007007", repo: "learn-ml"
        }
        unstable {
            githubNotify status: "ERROR", credentialsId: "github-x007007007-token", account: "x007007007", repo: "learn-ml"
        }
        failure {
            githubNotify status: "FAILURE", credentialsId: "github-x007007007-token", account: "x007007007", repo: "learn-ml"
        }
        changed {
            echo 'Things were different before...'
        }
    }
}