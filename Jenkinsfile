pipeline {
  agent {
    docker {
      image 'alpine:3.7'
    }

  }
  stages {
    stage('Build') {
      steps {
        sh 'ls'
        sh 'uname -a'
        sh 'apk add python3'
      }
    }

    stage('error') {
      steps {
        sh '''


python3 -m unittest discover -v'''
      }
    }

  }
}