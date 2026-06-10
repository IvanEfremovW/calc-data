FROM python:3.14-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . .

RUN pip install uv --no-cache-dir
RUN uv pip install --system --no-cache-dir . 

ENTRYPOINT ["python3", "calc_data.py"]