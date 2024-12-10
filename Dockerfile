FROM python:latest

WORKDIR /app

# Copy the requirements.txt first to take advantage of Docker's cache
COPY requirements.txt main.py /app/

RUN pip install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 80

CMD ["fastapi", "run", "main.py", "--port", "80"]