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
      }
    }

    stage('') {
      steps {
        sh 'apk install python3'
      }
    }

  }
}