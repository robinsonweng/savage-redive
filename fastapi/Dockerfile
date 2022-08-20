FROM python:3.8-slim-buster

ARG WEBUSER 
ARG WEBGROUP
ARG USER
ARG ENV

WORKDIR /app

COPY . .

ENV VIRTUAL_ENV=$ENV
RUN python3 -m venv $ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip install -r requirements.txt

CMD ["python3", "./savageapi/main.py"]