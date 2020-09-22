FROM openjdk:latest

WORKDIR /

# ENV id hanjoo
# ENV pw 1010

ADD JdbcAgentEx-null.jar /JdbcAgentEx-null.jar
ADD lib/tibero/tibero6jdbc/1.0/tibero6jdbc-1.0.jar /tibero6jdbc-1.0.jar

# ENTRYPOINT java -cp "./JdbcAgentEx-null.jar:./tibero6jdbc-1.0.jar" local.hanjoo.JdbcAgent
# ENTRYPOINT java -cp "./JdbcAgentEx-null.jar:./tibero6jdbc-1.0.jar" local.hanjoo.JdbcAgent "$id" "$pw"
