pipeline {
    agent any
    triggers {
        pollSCM('H/5 * * * *')
    }
    stages {
        stage('Check & Install env') {
            steps {
                bat "pip config set global.index-url http://mirrors.aliyun.com/pypi/simple/"
                bat "pip config set global.trusted-host mirrors.aliyun.com"
                bat "python initial-env.py "
            }
            post {
                success {
                  githubNotify description: 'Check & Installed ENV', status: 'SUCCESS', credentialsId: "github-x007007007-token", account: "x007007007", repo: "learn-ml"
                }
                failure {
                  githubNotify description: 'Check & Installed ENV', status: 'FAILURE', credentialsId: "github-x007007007-token", account: "x007007007", repo: "learn-ml"
                }
            }
        }
        stage("Download resource")  {
            steps {
                bat """
                    call pytorch\\venv\\scripts\\activate
                    cd pytorch\\cnn\\data
                    call download.py
                """
            }
            post {
                success {
                  githubNotify description: 'download resource', status: 'SUCCESS', credentialsId: "github-x007007007-token", account: "x007007007", repo: "learn-ml"
                }
                failure {
                  githubNotify description: 'download resource', status: 'FAILURE', credentialsId: "github-x007007007-token", account: "x007007007", repo: "learn-ml"
                }
            }
        }
        stage("run learn")  {
            steps {
                bat """
                    call pytorch\\venv\\scripts\\activate
                    cd pytorch\\cnn
                    call python cnn1.py
                """
            }
            post {
                success {
                  githubNotify description: 'download resource', status: 'SUCCESS', credentialsId: "github-x007007007-token", account: "x007007007", repo: "learn-ml"
                }
                failure {
                  githubNotify description: 'download resource', status: 'FAILURE', credentialsId: "github-x007007007-token", account: "x007007007", repo: "learn-ml"
                }
            }
        }
    }
    post {
        always {
            echo 'One way or another, I have finished'
        }
        success {
            githubNotify status: "SUCCESS", description: "DONE", credentialsId: "github-x007007007-token", account: "x007007007", repo: "learn-ml"
        }
        unstable {
            githubNotify status: "SUCCESS", description: "UNSTABLE", credentialsId: "github-x007007007-token", account: "x007007007", repo: "learn-ml"
        }
        failure {
            githubNotify status: "FAILURE", description: "FAILURE", credentialsId: "github-x007007007-token", account: "x007007007", repo: "learn-ml"
        }
        changed {
            echo 'Things were different before...'
        }
    }
}