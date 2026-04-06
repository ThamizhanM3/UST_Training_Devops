FROM eclipse-temurin:17-jre-alpine

WORKDIR /app

COPY target/app.jar app.jar

EXPOSE 8080

ENV JAVA_OPTS="-Xms256m -Xmx512m"

CMD ["sh", "-c", "java $JAVA_OPTS -jar app.jar"]