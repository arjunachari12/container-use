
FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir openai
CMD ["python", "self_debug.py"]
