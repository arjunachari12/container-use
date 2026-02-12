
FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir langchain chromadb openai pypdf
CMD ["python", "index.py"]
