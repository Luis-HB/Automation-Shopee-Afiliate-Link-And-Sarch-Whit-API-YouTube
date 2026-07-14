FROM python:3.12-slim-bookworm

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && \
    apt-get install -y gcc curl && \
    pip install --no-cache-dir -r requirements.txt

CMD ["bash"]