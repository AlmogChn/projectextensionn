pipeline{ 
    agent any
    options {
        buildDiscarder(logRotator(numToKeepStr: '20', daysToKeepStr: '5'))
    }
    environment {
        registry = "almogchn/project_extension3"
        registryCredential = 'docker_hub'
        dockerImage = ''
    }
    stages{
        stage('Cloning Git') {
            steps {
                script { 
                    properties([pipelineTriggers([pollSCM('30 * * * *')])])
                }
                git branch: 'main', url: 'https://github.com/AlmogChn/projectextension.git'
            }
        }
        stage('run backend server') {
            steps{
                script{
                    sh ' nohup python rest_app.py &'
                }
            }
        }
        stage('backend testing') {
            steps {
                script {
                    sh 'python backend_testing.py'
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
        stage ('build image'){
            steps {
                script {
                    dockerImage = docker.build registry + ":$BUILD_NUMBER"
                }
            }
        }
        stage('push image') {
            steps {
                script {
                    docker.withRegistry('', registryCredential) {
                        dockerImage.push()
                    }
                }
            }
        }
         stage('set version') {
            steps {
                sh "echo IMAGE_TAG=${BUILD_NUMBER} > .env"
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
        always {
            sh "docker rmi $registry:$BUILD_NUMBER"
        }
     }
}
