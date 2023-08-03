pipeline{
    agent any
    environment {

        IMAGE_NAME = "${env.GIT_BRANCH.toLowerCase()}:${env.BUILD_ID}"
    }
    stages{
        stage("Build & Deploy"){
            steps{
                docker.build("${env.IMAGE_NAME}",".")
            }
        }
        stage("Pull & Test"){
             when {
                expression { return params.MANUAL_STAGE == 'Test' || cron('H 17 * * *') }
            }
            steps{
                docker.image("${env.IMAGE_NAME}").run()
            }
        }
    }
    
}