FROM openjdk:latest

WORKDIR /

# ENV id hanjoo
# ENV pw 1010
# ENV tab AB1_2
# ENV id1 EMP_NUM
# ENV id2 NAME
# ENV id3 EMAIL

ADD JdbcAgentEx-ML.jar /JdbcAgentEx-ML.jar
ADD lib/tibero/tibero6jdbc/1.0/tibero6jdbc-1.0.jar /tibero6jdbc-1.0.jar

# ENTRYPOINT java -cp "./JdbcAgentEx-ML.jar:./tibero6jdbc-1.0.jar" local.hanjoo.JdbcAgent
ENTRYPOINT java -cp "./JdbcAgentEx-ML.jar:./tibero6jdbc-1.0.jar" local.hanjoo.JdbcAgent "$id" "$pw" "$tab" "$id1" "$id2" "$id3"
