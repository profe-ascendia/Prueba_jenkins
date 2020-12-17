pipeline {
  agent {
    docker {
      image 'alpine:latest'
    }

  }
  stages {
    stage('Build') {
      steps {
        sh 'npm install'
      }
    }

  }
}