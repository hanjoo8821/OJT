FROM openjdk:8-jre-alpine

WORKDIR /

# ENV id hanjoo
# ENV pw 1010

ADD JdbcAgentEx-1.0.jar /JdbcAgentEx-1.0.jar
ADD lib/tibero/tibero6jdbc/1.0/tibero6jdbc-1.0.jar /tibero6jdbc-1.0.jar

# ENTRYPOINT java -cp "./JdbcAgentEx-1.0.jar:./tibero6jdbc-1.0.jar" local.hanjoo.JdbcAgent
ENTRYPOINT java -cp "./JdbcAgentEx-1.0.jar:./tibero6jdbc-1.0.jar" local.hanjoo.JdbcAgent "$id" "$pw"
