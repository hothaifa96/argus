FROM python:3.11.4-alpine3.18
WORKDIR /app
COPY main.py .
CMD python main.py
