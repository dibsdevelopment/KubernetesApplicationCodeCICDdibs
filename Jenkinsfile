node {
    def app

    stage('Debug User') {
         sh 'whoami'
         sh 'id'
         sh 'groups'     
    }

    stage('Clone repository') {      

        checkout scm
    }

    stage('Build image') {  
       app = docker.build("dibsiit123/testrepo")
    }

    stage('Test image') {  

        app.inside {
            sh 'echo "Tests passed"'
        }
    }

    stage('Push image') {
        
        docker.withRegistry('https://registry.hub.docker.com', 'DOCKER_HUB_PASSWORD') {
            app.push("${env.BUILD_NUMBER}")
        }
    }
    
    stage('Trigger ManifestUpdate') {
                echo "triggering updatemanifestjob updatemanifest-argocd-pipeline4 "
                build job: 'updatemanifest-argocd-pipeline4', parameters: [string(name: 'DOCKERTAG', value: env.BUILD_NUMBER)]
        }
}

