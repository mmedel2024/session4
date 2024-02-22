pipeline {
  agent any
  stages {
    stage('Environment') {
      steps {
        sh 'docker --version'
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
        stage('Test') {
          steps {
            sh 'python3 ./Scripts_test/00_test_api.py'
          }
        }

        stage('Logs') {
          steps {
            sleep 20
            sh 'docker logs test_api01'
          }
        }

        stage('TestConversor') {
          steps {
            sh 'python3 ./Scripts_test/01_test_api.py'
          }
        }

      }
    }

    stage('Stop') {
      steps {
        sh 'bash Scripts/stop.sh'
      }
    }

    stage('upload_imagen') {
      steps {
        sh 'cat versionImage | xargs bash Scripts/upload_hub.sh'
      }
    }

  }
}