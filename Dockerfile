FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install --break-system-packages -r requirements.txt
CMD ["python3", "app.py"]
