FROM python:3.10-slim
WORKDIR /app
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt
COPY requirements.txt .
COPY . .
COPY templates ./templates
CMD ["python", "app.py"]
