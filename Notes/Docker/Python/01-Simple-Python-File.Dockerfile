FROM python:3.12

WORKDIR /app

COPY script.py .

CMD ["python", "script.py"]