FROM python:3.10-alpine3.18

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /amonic
COPY . .

RUN pip install --upgrade pip

#RUN apk add libffi-dev openssl-dev cargo
RUN pip install -r requirements.txt

EXPOSE 8000

RUN apk add postgresql-client build-base postgresql-dev

RUN adduser --disabled-password artem

USER artem