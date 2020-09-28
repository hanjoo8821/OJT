FROM continuumio/anaconda3:latest

WORKDIR /

# ENV col2 BIRTH
# ENV col3 SALARY

ADD regression.py /regression.py

ENTRYPOINT python /regression.py "$col2" "$col3"
