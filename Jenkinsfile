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
        stage ('docker compose'){
            steps{
                sh 'docker-compose up -d'
            }
        }
       stage ('docker backend testing'){
            steps{
                 sh 'python docker_backend_testing.py'
            }
        }
       stage('clean environment again'){
            steps{
                 sh 'python clean_environment.py'
            }
        }      
    }   
    post {
        always {
            sh "docker rmi $registry:$BUILD_NUMBER"
        }
    }
    
}
