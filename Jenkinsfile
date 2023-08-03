pipeline{
    agent any

    environment {
        IMAGE_NAME = "${env.GIT_BRANCH.toLowerCase()}"
        IMAGE_VERSION = "${env.BUILD_ID}"
        AWS_REGION = 'us-east-1' 
        ECR_REGISTRY = '161192472568.dkr.ecr.us-east-1.amazonaws.com/hothaifa'
        BUCKET_NAME = 'hothaifa'

    
    }
    stages{
        stage("Build & Deploy"){
            steps{
                script {
                    docker.build("${env.IMAGE_NAME}:${IMAGE_VERSION}",".")
                    docker.image("${env.IMAGE_NAME}:${IMAGE_VERSION}").run('--name container1')
                    sh 'docker cp container1:/app/artifact.txt .'
                }
                
                withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', credentialsId: 'jenkins-aws-cli']]) {
                    sh "aws ecr get-login-password --region ${AWS_REGION} | docker login --username AWS --password-stdin ${ECR_REGISTRY}"
                    sh "docker tag ${IMAGE_NAME}:${IMAGE_VERSION} ${ECR_REGISTRY}"
                    sh "docker push ${ECR_REGISTRY}:latest"
                    sh "aws s3 cp artifact.txt s3://${BUCKET_NAME}"
                }
            
            }
        }
        stage("Pull & Test"){
          
             when {
                expression { return params.MANUAL_STAGE == 'Test' || cron('H 17 * * *') }
            }
            steps{
                
                script{
                    sh 'docker cp container1:/app/artifact.txt .'
                    sh 'aws s3 cp s3://${BUCKET_NAME}/artifact.txt file.txt'
                    sh "[ -s 'file.txt' ] && cat 'file.txt'"
                }
            }
            
        }
    }  
}