FROM python:3.7.2-slim-stretch

ENV DEBIAN_FRONTEND noninteractive
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8
ENV PYTHONUNBUFFERED 1

# -- Install system dependencies:
RUN apt-get update && apt-get upgrade -y && apt-get install curl -y

# -- Install Pipenv:
RUN pip3 install --upgrade pip
RUN pip3 install pipenv

# -- Create Django user:
RUN addgroup --system django && adduser --system --ingroup django django

# -- Install Application into container:
COPY ./compose/production/django/entrypoint /entrypoint
RUN sed -i 's/\r//' /entrypoint
RUN chmod +x /entrypoint
RUN chown django /entrypoint

COPY ./compose/production/django/start /start
RUN sed -i 's/\r//' /start
RUN chmod +x /start
RUN chown django /start

RUN set -ex && mkdir /app

COPY . /app

RUN chown -R django /app

USER django

WORKDIR /app

# -- Adding Pipfiles
ONBUILD COPY Pipfile Pipfile
ONBUILD COPY Pipfile.lock Pipfile.lock

# -- Install dependencies:
ONBUILD RUN set -ex && pipenv install --deploy --system

ENTRYPOINT ["/entrypoint"]
