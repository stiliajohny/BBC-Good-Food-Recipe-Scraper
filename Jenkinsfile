pipeline {
   agent any

   stages {
      stage('Get Project') {
         steps {
            git 'https://gitlab.johnstilia.co.uk/jstilia/bbc-good-food-recipe-scraper'
         }
      }
      stage('Execute the Script') {
         steps { Script
            sh label: '', script: 'source ./bin/activate && python ./recipe_scraper.py "https://www.bbcgoodfood.com/recipes/orzo-tomato-soup"'
         }
      }
   }
}