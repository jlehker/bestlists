FROM python:3.8.0-slim-buster

ENV DEBIAN_FRONTEND noninteractive
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8
ENV PYTHONUNBUFFERED 1

# -- Install system dependencies:
RUN apt-get update -yqq && apt-get upgrade -yqq && apt-get install -yqq apt-transport-https curl gnupg2 supervisor
RUN pip -qq install -U pip && pip -qq install pipenv

# -- Adding Pipfiles and package.json
COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

# -- Install project dependencies:
RUN set -ex && pipenv install --deploy --system

# RUN set -ex && pipenv lock --requirements > /tmp/requirements.txt
# RUN pip install -r /tmp/requirements.txt

# -- Create Django user:
RUN addgroup --system django && adduser --system --ingroup django django

# -- Install Application into container:
COPY ./compose/production/django/entrypoint entrypoint
RUN sed -i 's/\r//' entrypoint
RUN chmod +x entrypoint
RUN chown django entrypoint

# -- Create app directory:
RUN set -ex && mkdir /app
COPY . /app
RUN chown -R django /app
WORKDIR /app

USER django

ENTRYPOINT ["/entrypoint"]
