FROM openjdk:16-jdk

WORKDIR /

# ENV id hanjoo
# ENV pw 1010

ADD JdbcAgentEx-basic.jar /JdbcAgentEx-basic.jar
ADD lib/tibero/tibero6jdbc/1.0/tibero6jdbc-1.0.jar /tibero6jdbc-1.0.jar

# ENTRYPOINT java -cp "./JdbcAgentEx-basic.jar:./tibero6jdbc-1.0.jar" local.hanjoo.JdbcAgent
ENTRYPOINT java -cp "./JdbcAgentEx-basic.jar:./tibero6jdbc-1.0.jar" local.hanjoo.JdbcAgent "$id" "$pw" | tee /tmp/result.txt
