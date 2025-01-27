FROM python:3.9-slim
WORKDIR /app

COPY .env .
COPY index.html .
COPY script.py .

RUN pip install fastapi uvicorn python-dotenv openai

CMD ["uvicorn", "script:app", "--host", "0.0.0.0", "--port", "8080"]