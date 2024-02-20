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

    stage('run') {
      steps {
        sh 'cat versionImage | xargs bash Scripts/run.sh'
        sh 'docker log test_api01'
      }
    }

  }
}