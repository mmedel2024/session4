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
        sh 'cat versionImage | xargs ./Scripts/build.sh'
      }
    }

  }
}