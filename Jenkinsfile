pipeline{
    agent any
    stages{
        stage("Build & Deploy"){
            steps{
                echo "========executing A========"
                sh "docker build -t demo ."
            }
        }
        stage("Pull & Test"){
             when {
                expression { return params.MANUAL_STAGE == 'Test' || cron('H 17 * * *') }
            }
            steps{
                echo "========executing A========"
                sh "docker iamges"
                sh "docker start this:latest"
                sh "ls"
            }
        }
    }
    
}