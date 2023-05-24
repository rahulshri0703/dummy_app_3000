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
                sh "pwd"
                sh " echo $BUILD_NUMBER"
            }
        }

          stage('BUILDING DOCKER IMAGE') {
            steps {
                sh "ls"
                sh "docker build -t new999 ."
                sh "docker tag new999 rahulshri0703/new999"
            }
        
        }

        // this project is parameterizer and add Password Parameter username and password
               stage('Login to DOCKER') {
            steps {
                sh "docker login -u $username -p $password"
                sh "docker push rahulshri0703/new999"
            }
        }


    }
    }
    