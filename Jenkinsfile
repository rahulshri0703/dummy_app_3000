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
            step {
                sh "echo GOOD"
            }
        }
    }
    }
    