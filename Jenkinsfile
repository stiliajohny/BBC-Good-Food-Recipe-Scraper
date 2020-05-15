pipeline {
  agent any

  stages {
    stage('Git checkout') {
      steps {
        git url: 'https://gitlab.johnstilia.co.uk/jstilia/bbc-good-food-recipe-scraper.git'
      }
    }
    stage('Execute Script') {
      steps {
        Script {
          sh "echo hello"

        }
      }
    }
  }
}
