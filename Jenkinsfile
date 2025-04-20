pipeline{
    agent any

    environment{
        DOCKER_IMAGE='suhasbm09/ai-code-commentor'
    }
    triggers{
        githubPush()
    }

    stages{
        stage('clone Repo'){
            steps{
                git branch:'master',
                url:'git@github.com:suhasbm09/ai-code-commentor.git'
            }
        }

        stage('Build Docker Image'){
            steps{
                script{
                    sh 'docker build -t $DOCKER_IMAGE:latest .'
                }
            }
        }
        stage('Push to DockerHub'){
            steps{
                withCredentials([usernamePassword(credentialsId:'dockerhub-creds',usernameVariable:'DOCKER_USER',passwordVariable:'DOCKER_PASS')]){
                    sh '''
                    echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                    docker push $DOCKER_IMAGE:latest
                    '''
                }
            }
        }
    }
}