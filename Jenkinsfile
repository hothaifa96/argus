pipeline{
    agent any
    environment {

        IMAGE_NAME = "${env.GIT_BRANCH.toLowerCase()}:"
        IMAGE_VERSION = "${env.BUILD_ID}"
        AWS_REGION = 'us-east-1' 
        ECR_REGISTRY = '161192472568.dkr.ecr.us-east-1.amazonaws.com/hothaifa'
    
    }
    stages{
        stage("Build & Deploy"){
            steps{
                script {
                    docker.build("${env.IMAGE_NAME}:${IMAGE_VERSION}",".")
                    docker.image("${env.IMAGE_NAME}:${IMAGE_VERSION}").run()
                }
                sh "aws ecr get-login-password --region ${AWS_REGION} | docker login --username AWS --password-stdin ${ECR_REGISTRY}"
                sh "docker tag ${IMAGE_NAME}:${IMAGE_VERSION} ${ECR_REGISTRY}/${IMAGE_NAME}"
                sh "docker push ${ECR_REGISTRY}/${IMAGE_NAME}:${IMAGE_VERSION}"
            }
        }
        stage("Pull & Test"){
             when {
                expression { return params.MANUAL_STAGE == 'Test' || cron('H 17 * * *') }
            }
            steps{
                script {
                    docker.image("${env.IMAGE_NAME}").run()
                }
            }
        }
    }
    
}