FROM python:3.10-slim
WORKDIR /app
COPY app/requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt
COPY app/ .
COPY app/templates ./templates
CMD ["python", "app.py"]
