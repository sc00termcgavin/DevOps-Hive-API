FROM python:latest@sha256:9255d1993f6d28b8a1cd611b108adbdfa38cb7ccc46ddde8ea7d734b6c845e32

WORKDIR /app

# Copy the requirements.txt first to take advantage of Docker's cache
COPY requirements.txt main.py /app/

RUN pip install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 80

CMD ["fastapi", "run", "main.py", "--port", "80"]