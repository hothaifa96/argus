pipeline{
    agent any
    stages{
        stage("Build & Deploy"){
            steps{
                echo "========executing A========"
                sh "docker build -t this ."
            }
        }
        stage("Pull & Test"){
             when {
                expression { return params.MANUAL_STAGE == 'Test' || cron('H 17 * * *') }
            }
            steps{
                echo "========executing A========"
                sh "docker start this"
                sh "ls"
            }
        }
    }
    
}