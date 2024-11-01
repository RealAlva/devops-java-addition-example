# Usar una imagen base de Java
FROM openjdk:11-jre-slim

# Copiar el archivo JAR generado al contenedor
COPY target/SumTwoNumbers-1.0-SNAPSHOT.jar app.jar

# Ejecutar la aplicación
ENTRYPOINT ["java", "-jar", "/app.jar"]
