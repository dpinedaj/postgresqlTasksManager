pipeline {
  agent {
    node {
      label 'build'
    }

  }
  stages {
    stage('build') {
      steps {
        sh 'docker-compose up'
      }
    }

  }
}