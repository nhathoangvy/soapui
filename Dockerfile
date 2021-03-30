
FROM python:3
FROM java:openjdk-8-jdk

WORKDIR /automation_test

COPY src/ ./src
COPY manage.py .

RUN echo "deb [check-valid-until=no] http://archive.debian.org/debian jessie-backports main" > /etc/apt/sources.list.d/jessie-backports.list

RUN sed -i '/deb http:\/\/deb.debian.org\/debian jessie-updates main/d' /etc/apt/sources.list

RUN apt-get -o Acquire::Check-Valid-Until=false update
RUN apt install ansible -y
RUN apt install ant -y
RUN apt install python-setuptools python-dev python -y
RUN apt install python3-pip -y

RUN pip3 install prometheus_client && pip3 install requests 

ENTRYPOINT python3 ./manage.py