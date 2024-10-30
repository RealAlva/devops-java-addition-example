pipeline {
    agent any
    stages {
        stage('Preparar Repositorio') {
            steps {
                dir('/home/daniel/devops-java-addition-example') {
                    sh '''
                    git init
                    git remote remove origin || true
                    git remote add origin /home/daniel/devops-java-addition-example
                    git fetch origin
                    git reset --hard origin/main
                    '''
                }
            }
        }
        stage('Construir con Maven') {
            steps {
                dir('/home/daniel/devops-java-addition-example') {
                    sh 'mvn clean install'
                }
            }
        }
        stage('Instalar dependencias en venv') {
            steps {
                dir('/home/daniel/devops-java-addition-example') {
                    sh '''
                    /bin/bash -c "source venv/bin/activate && pip install -r requirements.txt || pip install selenium"
                    '''
                }
            }
        }
        stage('Pruebas con Selenium') {
            steps {
                dir('/home/daniel/devops-java-addition-example') {
                    sh '''
                    /bin/bash -c "source venv/bin/activate && python3 src/test/python/test_addition.py"
                    '''
                }
            }
        }
        stage('Construir Imagen Docker') {
            steps {
                dir('/home/daniel/devops-java-addition-example') {
                    sh 'docker build -t sumtwonumbers .'
                }
            }
        }
        stage('Desplegar en Docker') {
            steps {
                sh 'docker run -d --name sumtwonumbers -p 8080:8080 sumtwonumbers'
            }
        }
    }
    post {
        success {
            echo 'Integración y Despliegue completados exitosamente.'
        }
        failure {
            echo 'El Pipeline ha fallado.'
        }
    }
}
