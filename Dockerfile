FROM python:3.9-slim

WORKDIR .

COPY requirements.txt .
RUN pip3 install -r requirements.txt --no-cache-dir
COPY ./app /app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
