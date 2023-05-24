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
            }
        }

          stage('BUILDING DOCKER IMAGE') {
            steps {
                sh "ls"
                sh "docker build -t rahulshri0703/dummy_3000:$BUILD_NUMBER -t rahulshri0703/dummy_3000:latest ."
                // sh "docker tag new999:$BUILD_NUMBER rahulshri0703/new999:$BUILD_NUMBER"
            }
        
        }

        // this project is parameterizer and add Password Parameter username and password
               stage('Login to DOCKER') {
            steps {
                // login to docker
                sh "docker login -u $username -p $password"
                // push 
                sh "docker push rahulshri0703/dummy_3000:$BUILD_NUMBER"
                sh "docker push rahulshri0703/dummy_3000:latest"
                //delete the images
                sh " docker rmi rahulshri0703/dummy_3000:$BUILD_NUMBER"
                sh " docker rmi rahulshri0703/dummy_3000:latest"
            }
        }

        stage("ANSIBLE PING TO VMS") {
            steps {
                sh "ansible -i inventory ping all"
            }
        }

     stage("ANSIBLE deploy container") {
            steps {
                sh "docker rm app"
                // deploy
                sh "ansible-playbook -i inventory ansible_command.yml"
            }
        }
         

    }
    }
    