FROM python:3.7.2-slim-stretch

ENV DEBIAN_FRONTEND noninteractive
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8
ENV PYTHONUNBUFFERED 1

# -- Install system dependencies:
RUN apt-get update && apt-get upgrade -y && apt-get install -yqq apt-transport-https curl gnupg2
RUN echo "deb https://deb.nodesource.com/node_10.x stretch main" > /etc/apt/sources.list.d/nodesource.list
RUN curl -fsSL https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add -
RUN apt-get update && \
  apt-get install -yqq nodejs gnupg2 && \
  pip install -U pip && pip install pipenv && \
  rm -rf /var/lib/apt/lists/*

# -- Adding Pipfiles and package.json
COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock
COPY package.json package.json
COPY package-lock.json package-lock.json

# -- Install project dependencies:
RUN set -ex && pipenv install --deploy --system && npm i -g npm@^6

# -- Create Django user:
RUN addgroup --system django && adduser --system --ingroup django django

RUN set -ex && mkdir /app
COPY . /app
WORKDIR /app

# -- Install Application into container:
COPY ./compose/production/django/entrypoint entrypoint
RUN sed -i 's/\r//' entrypoint
RUN chmod +x entrypoint
RUN chown django entrypoint

COPY ./compose/production/django/start start
RUN sed -i 's/\r//' start
RUN chmod +x start
RUN chown django start

RUN chown -R django /app

USER django

ENTRYPOINT ["./entrypoint"]
