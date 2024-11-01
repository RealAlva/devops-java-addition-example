pipeline {
    agent any
    environment {
        PATH = "${env.PATH}:/usr/local/bin:/usr/lib/chromedriver"
    }
    stages {
        stage('Clonar Repositorio') {
            steps {
                git branch: 'main', url: 'https://github.com/RealAlva/devops-java-addition-example.git'
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
        // Verificar y eliminar el contenedor existente si está en ejecución
        sh '''
        if [ "$(docker ps -aq -f name=sumtwonumbers)" ]; then
            docker rm -f sumtwonumbers || true
        fi
        '''

        // Iniciar el contenedor en el puerto 8081 para evitar conflictos
        sh 'docker run -d --name sumtwonumbers_new -p 8081:8080 sumtwonumbers'
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
