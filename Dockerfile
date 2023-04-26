FROM python:3.8

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 8080

ENTRYPOINT ["uvicorn", "main:app", "--reload", "--port", "8080"]
