web: /usr/local/bin/gunicorn config.wsgi --bind 0.0.0.0:5000 --chdir=/app
worker: /usr/bin/supervisord -n -c /app/config/workers.conf
