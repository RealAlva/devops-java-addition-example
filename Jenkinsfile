pipeline {
    agent any
    environment {
        PATH = "${env.PATH}:/usr/local/bin:/usr/lib/chromedriver"
    }
    stages {
        stage('Clonar Repositorio') {
            steps {
                git branch: 'main', url: 'file:///home/daniel/devops-java-addition-example' // Asegúrate que sea la ruta correcta del repositorio local
            }
        }
        stage('Construir con Maven') {
            steps {
                sh 'mvn clean install'
            }
        }
        stage('Configurar Entorno Python para Pruebas Selenium') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }
        stage('Pruebas con Selenium') {
            steps {
                sh '''
                    . venv/bin/activate
                    python3 src/test/python/test_addition.py
                '''
            }
        }
        stage('Construir Imagen Docker') {
            steps {
                sh 'docker build -t sumtwonumbers .'
            }
        }
        stage('Desplegar en Docker') {
            steps {
            // Eliminar el contenedor existente si está en ejecución
                sh 'docker rm -f sumtwonumbers || true'
        
            // Iniciar el contenedor en el puerto 8081
                sh 'docker run -d --name sumtwonumbers -p 8081:8080 sumtwonumbers'
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
