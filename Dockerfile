ARG BASE_IMAGE=python:2.7-slim
FROM ${BASE_IMAGE}

LABEL maintainer="Peter Karacsonyi <peter.karacsonyi@msci.com>"

RUN mkdir -p /var/log/containers/ && chmod 777 -R /var/log/containers/ 

COPY source/* /home/*


EXPOSE  5001

#ENTRYPOINT ["/home/webhook-shims/runserver.py"]
