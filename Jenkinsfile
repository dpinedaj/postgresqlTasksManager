pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        sh '''apt update
apt install -y docker-compose
docker-compose up'''
      }
    }

  }
}