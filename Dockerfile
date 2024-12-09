FROM python:latest

WORKDIR /app

COPY main.py /app

CMD ["python", "main.py"]