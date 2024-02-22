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

    stage('Run') {
      steps {
        sh 'cat versionImage | xargs bash Scripts/run.sh'
        sh 'docker logs test_api01'
      }
    }

    stage('Test') {
      parallel {
        stage('Test') {
          steps {
            sh 'python3 ./Scripts_test/00_test_api.py'
          }
        }

        stage('Logs') {
          steps {
            sleep 10
            sh 'docker logs test_app01'
          }
        }

        stage('TestConversor') {
          steps {
            sh 'python3 ./Scripts_test/01_test_api.py'
          }
        }

      }
    }

  }
}