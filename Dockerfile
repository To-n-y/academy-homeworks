FROM python:3.10-alpine
ENV PYTHONUNBUFFERED 1
EXPOSE 8000
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]