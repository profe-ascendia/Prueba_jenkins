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
        sh 'python3 -m unittest dicover -v'
      }
    }

  }
}