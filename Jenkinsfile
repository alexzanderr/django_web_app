CODE_CHANGES = getGitChanges()
pipeline {
	agent any

	// these variables have global scope in the pipeline
	environment {
		NEW_VERSION = '1.3.0'
	}

	stages {

		stage("build") {
			steps {
				echo 'build stage'
				// sh 'pip install -r requirements.txt'
				echo "building version ${NEW_VERSION}"
			}
		}

		stage("test") {
			when {
				expression {
					BRANCH_NAME == 'dev' || BRANCH_NAME == 'main' && CODE_CHANGES == true
				}
			}
			steps {
				echo 'test state'
			}
		}

		stage("deploy") {
			steps {
				echo 'deploy stage'
			}
		}
	}

	post {
		always {
			echo 'always'
		}
		failure {
			echo 'your code is crap'
		}
	}
}


