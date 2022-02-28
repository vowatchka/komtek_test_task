FROM python:3-alpine
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
# fix for install psycopg2
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
WORKDIR /terms_srv
COPY requirements.txt .
RUN python -m pip install --upgrade pip && pip install -r requirements.txt
COPY terms_srv/ .
COPY test_data/ .
