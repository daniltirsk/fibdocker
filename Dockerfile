#Dockerfile
FROM python:3.8-slim
RUN mkdir /application
WORKDIR "/application"
ADD ./fib.py /application/
ENTRYPOINT [ "python", "/application/fib.py" ]