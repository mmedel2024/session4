pipeline {
  agent any
  stages {
    stage('Environment') {
      steps {
        sh 'ls -ltr'
        sh 'docker --version'
        sh 'whoami'
        sh 'docker ps'
      }
    }

    stage('Build') {
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
        stage('Test00') {
          steps {
            sh 'python3 ./Scripts_test/00_test_api.py'
          }
        }

        stage('Logs') {
          steps {
            sleep 5
            sh 'docker logs test_api01'
          }
        }

        stage('Test01') {
          steps {
            sh 'python3 ./Scripts_test/01_test_api.py'
          }
        }

        stage('Test02') {
          steps {
            sh 'python3 ./Scripts_test/02_test_api.py'
          }
        }

      }
    }

    stage('Stop') {
      steps {
        sh 'bash Scripts/stop.sh'
      }
    }

    stage('Deploy') {
      steps {
        sh 'cat versionImage | xargs bash Scripts/upload_hub.sh'
      }
    }

  }
}