FROM python:3.8-slim-buster

ARG WEBUSER 
ARG WEBGROUP
ARG USER
ARG ENV

# if group not exist, create one
RUN if ! [ $(getent group "${WEBGROUP}") ] ; then groupadd "$WEBGROUP"; fi

# if user not exist, create one
RUN if ! [ $(id -u "${WEBUSER}") ] ; then useradd -ms /bin/bash "${WEBUSER}"; fi
RUN if ! [ $(id -u "${USER}") ] ; then useradd -ms /bin/bash "${USER}"; fi

USER ${USER}

WORKDIR /home/${USER}

COPY . .

ENV VIRTUAL_ENV=${ENV}
RUN python3 -m venv ${ENV}
ENV PATH="${VIRTUAL_ENV}/bin:${PATH}"

RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "5000"]