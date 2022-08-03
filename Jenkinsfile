pipeline{ 
    agent any
    options {
        buildDiscarder(logRotator(numToKeepStr: '20', daysToKeepStr: '5'))
    }
    environment {
        CREDS = credentials('project0') /* ..please add to your jenkins new credentials = username: AEfWGNA9zC + password: g0PRYTjC6R, id: project0  .. */
    }
    stages{
        stage('checkout') {
            steps {
                script { 
                    properties([pipelineTriggers([pollSCM('30 * * * *')])])
                }
                git 'https://github.com/AlmogChn/project_second_part.git'
            }
        }
        stage('run backend server') {
            steps{
                script{
                    sh ' nohup python rest_app.py $CREDS_USR $CREDS_PSW &'
                }
            }
        }
        stage('run fronted server') {
            steps {
                script {
                    sh ' nohup python web_app.py $CREDS_USR $CREDS_PSW &'
                }
            }
        }
        stage('backend testing') {
            steps {
                script {
                    sh 'python backend_testing.py $CREDS_USR $CREDS_PSW'
                }
            }
        }
        stage('frontend testing'){
            steps{
                script {
                    sh 'python frontend_testing.py $CREDS_USR $CREDS_PSW'
                }
            }
        }
        stage('combined testing') {
            steps {
                script {
                    sh 'python combined_testing.py $CREDS_USR $CREDS_PSW'
                }
            }
        }    
        stage('clean environment') {
            steps {
                script {
                    sh 'python clean_environment.py'
                }
            }
        }
    }    
    post {
    failure {
        mail to: 'almogchn100@gmail.com',
             subject: "Failed Pipeline: ${currentBuild.fullDisplayName}",
             body: "Something is wrong"
        }
    }
}
