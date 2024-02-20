pipeline {
  agent any
  stages {
    stage('env') {
      steps {
        sh 'docker --version'
      }
    }

    stage('build') {
      steps {
        sh 'cat version_image | xargs ./Scripts/build.sh'
      }
    }

  }
}