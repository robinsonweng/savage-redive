FROM python:3.8-slim-buster

WORKDIR /app

COPY . .

RUN pip install virtualenv

ENV VIRTUAL_ENV=venv

RUN virtualenv ${VIRTUAL_ENV}

ENV PATH="${VIRTUAL_ENV}/bin:$PATH"

RUN pip install -r requirements.txt

# CMD ["uvicorn", "main:app", "--reload"] 