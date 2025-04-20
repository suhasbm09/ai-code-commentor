pipeline{
    agent any

    stages{
        stage('clone Repo'){
            steps{
                git 'git@github.com:suhasbm09/ai-code-commentor.git'
            }
        }

        stage('Build Docker Image'){
            steps{
                script{
                    dockerImage= docker.build("ai-code-commentor:latest")
                }
            }
        }
        stage('Run Container'){
            steps{
                sh 'docker run -d -p 5000:5000 ai-code-commentor:latest'
            }
        }
    }
}