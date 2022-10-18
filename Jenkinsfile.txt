pipeline {
    agent any
    // options {
    //     skipStagesAfterUnstable()
    // }
    environment{
      VERSION = "0.1"
    }
    stages {
         stage('Clone repository') { 
            steps { 
                script{
                checkout scm
		
                }
            }
        }

        
        // stage('Test'){
        

	//     steps {
        //          echo 'Empty'
        //     }
        // }
        stage('Deploy') {
            steps {
                script{
                    docker.withRegistry('https://679089054946.dkr.ecr.ap-south-1.amazonaws.com', 'ecr:ap-south-1:aws_credential') {
                      app.push("${env.VERSION}")
                      app.push("latest")
                    }
                }
            }
        }
    }
}