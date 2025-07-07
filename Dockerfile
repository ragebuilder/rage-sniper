# Dockerfile for rage-sniper on Fly.io
FROM python:3.10-slim

# Create working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy app code
COPY . .

# Run bot
CMD ["python", "main.py"]
