##

```jenkinsfile
pipeline {
  agent {
    docker { image 'python:3.11-slim' }
  }
  parameters{
    string(name: 'NOMBRE', defaultValue: 'Mundo', description: '¿A quién saludamos?')
  }
  environment {
    SALUDO = "Hola, ${params.NOMBRE}!"
    VARIABLE_DE_EJEMPLO = "Valor de ejemplo"
    VARIABLE_DE_JENKINS = "${env.BUILD_NUMBER}"
  }
  stages {
    stage('Hola (Docker)') {
      steps {
        echo "${env.SALUDO}"
        echo "Variable de ejemplo: ${env.VARIABLE_DE_EJEMPLO}"
        echo "Número de build de Jenkins: ${env.VARIABLE_DE_JENKINS}"
    }
      steps {
        sh 'python --version'        // esto corre dentro del contenedor
        sh 'echo "Trabajo en: $(pwd)"'
      }
    }
  }

  post {
    always { echo 'El contenedor se elimina al terminar.' }
    success { echo 'Listo' }
    failure { echo 'Falló' }
  }
}
```