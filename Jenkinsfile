pipeline {
    
    agent any
    stages {
        stage('fetch_code') {
            steps {
                git branch : 'main',url : "https://github.com/rahulshri0703/dummy_app_3000.git"
            }
        post {
            success {
                echo "pulled succesful"
                archiveArtifacts  artifacts: "**/*.py"  
              
            }
        }
        }

        stage('echo') {
            steps {
                sh "echo GOOD"
            }
        }

          stage('BUILDING DOCKER IMAGE') {
            steps {
                sh "docker build -t rahulshri0703/new99:$BUILD_NUMBER ."
            }
        }

         stage('Login to DOCKER') {
            steps {
                sh "docker login -u rahulshri0703 -p d8982667712!"
            }
        }

        {
            stage ('PUSH TO DOCKER') {
                steps {
                    sh "docker push rahulshri0703/new99:$BUILD_NUMBER"
                }
            }
        }
    }
    }
    