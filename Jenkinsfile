pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        dockerNode(image: 'ubuntu:18.04') {
          sh 'apt update'
        }

      }
    }

  }
}