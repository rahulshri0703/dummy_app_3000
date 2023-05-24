pipeline {
    
    agent any

      environment {
        docker_cred = credentials('docker_credential')
    
    }

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

        // create a docker_credentials in Dashboard>Manage Jenkins>Credentials>System>Global credentials (unrestricted)

               stage('Login to DOCKER') {
            steps {
                // login to docker
                 sh "docker login -u $docker_cred_USR -p $docker_cred_PSW"
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
                // sudo apt update 
                // sudo apt install iputils-ping -y
                //sh "export ANSIBLE_HOST_KEY_CHECKING=False"
                sh "chmod 400 aws_key_pair.cer"
                sh "ansible -i inventory -m ping all --ssh-common-args='-o StrictHostKeyChecking=no'"
            }
        }

     stage("ANSIBLE deploy container") {
            steps {
                // deploy
                sh "ansible-playbook -i inventory ansible_command.yml"
            }
        }
         

    }
    }
    