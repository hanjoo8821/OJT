FROM openjdk:latest

WORKDIR /

# ENV id hanjoo
# ENV pw 1010
# ENV sql "SELECT * FROM AB1_2 LEFT JOIN ACCOUNTING ON AB1_2.EMP_NUM = ACCOUNTING.EMP_NUM"
# ENV col1 EMP_NUM
# ENV col2 BIRTH
# ENV col3 SALARY

ADD JdbcAgentEx-ML.jar /JdbcAgentEx-ML.jar
ADD lib/tibero/tibero6jdbc/1.0/tibero6jdbc-1.0.jar /tibero6jdbc-1.0.jar

# ENTRYPOINT java -cp "./JdbcAgentEx-ML.jar:./tibero6jdbc-1.0.jar" local.hanjoo.JdbcAgent
ENTRYPOINT java -cp "./JdbcAgentEx-ML.jar:./tibero6jdbc-1.0.jar" local.hanjoo.JdbcAgent "$id" "$pw" "$sql" "$col1" "$col2" "$col3"
