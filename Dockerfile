FROM continuumio/miniconda3 AS build


# Copying the environment files
COPY env.yml env.yml
RUN conda env create --file env.yml

# Installing conda-pack
RUN conda install -c conda-forge conda-pack


# Using conda pack to create an archived environment
RUN /bin/bash -c "conda-pack -n flask_env -o /tmp/flask_env.tar && mkdir /venv && cd /venv && tar xf /tmp/flask_env.tar && rm /tmp/flask_env.tar"

RUN /venv/bin/conda-unpack

FROM debian:buster AS runtime

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8 APP_USER=app APP_HOME=/home/app

RUN useradd --no-log-init -r -m -U "$APP_USER"

COPY --from=build --chown="$APP_USER":"$APP_USER" venv "$APP_HOME"/flask_env
COPY --chown="$APP_USER":"$APP_USER" ./ "$APP_HOME"/app

USER "$APP_USER"
WORKDIR "$APP_HOME"/app

ENV PATH="$APP_HOME/ml-ops.env/bin:$PATH"

EXPOSE 5000
ENTRYPOINT ["python", "main.py"]
