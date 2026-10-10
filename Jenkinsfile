pipeline {
    agent any

    environment {
        PYTHON_VERSION = 'python3'
        USERNAME = credentials('ADMIN_USERNAME')
        PASSWORD = credentials('ADMIN_PASSWORD')
    }

    stages {
        stage('download code/ checkout code') {
            steps {
                checkout scm
            }
        }
        stage('show python version') {
            steps {
                sh "$PYTHON_VERSION --version"
            }
        }
        stage('run python program') {
            steps {
                sh """
                    export username=$USERNAME
                    export password=$PASSWORD
                    $PYTHON_VERSION read.py
                """
            }
        }
    }
}