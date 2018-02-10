FROM python:3.6

RUN pip install flask-ask && \
    mkdir /app

WORKDIR /app

COPY src/* .

ENTRYPOINT ["python", "app.py"]