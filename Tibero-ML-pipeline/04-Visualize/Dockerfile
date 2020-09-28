FROM continuumio/anaconda3:latest

WORKDIR /

# ENV col2 BIRTH
# ENV col3 SALARY

ADD graph_out.py /graph_out.py

ENTRYPOINT python /graph_out.py "$col2" "$col3"
