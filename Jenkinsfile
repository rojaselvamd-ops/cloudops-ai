pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh 'docker build -t cloudops-ai .'
      }
    }
    stage('Deploy') {
      steps {
        sh 'docker run -d -p 5000:5000 cloudops-ai'
      }
    }
  }
}
