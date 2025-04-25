FROM python:3.9-slim

WORKDIR /app

COPY app.py /app/
COPY templates /app/templates
COPY static /app/static

RUN pip install --no-cache-dir flask requests
EXPOSE 8080

CMD ["python", "app.py"]

