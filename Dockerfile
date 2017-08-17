FROM python:3.6

# Add code
ADD starter /srv/starter
WORKDIR /srv/starter

# Install application requirements
#RUN apt-get update -y && apt-get install -y binutils libproj-dev gdal-bin && apt-get clean
RUN pip3 install uwsgi virtualenv
RUN virtualenv -p python3.6 /venv --no-site-packages
RUN /venv/bin/pip3 install -r /srv/starter/requirements.txt

# uWSGI will listen on this port
#EXPOSE 8000

ENV DJANGO_SETTINGS_MODULE=Runur.settings.dev

# Call collectstatic (customize the following line with the minimal environment variables needed for manage.py to run):
#RUN DATABASE_URL=none /venv/bin/python manage.py collectstatic --noinput
RUN /venv/bin/python manage.py migrate --noinput
RUN /venv/bin/python manage.py collectstatic --noinput

#CMD ["./start.sh"]
CMD ["/usr/local/bin/uwsgi", "--emperor", "/srv/starter/uwsgi_docker.ini"]
#CMD ["/usr/local/bin/uwsgi", "--ini", "/srv/starter/uwsgi_docker.ini"]

# uWSGI configuration (customize as needed):
#ENV UWSGI_VIRTUALENV=/venv UWSGI_WSGI_FILE=Runur/wsgi.py UWSGI_HTTP=:8000 UWSGI_MASTER=1 UWSGI_WORKERS=2 UWSGI_THREADS=8 UWSGI_UID=1000 UWSGI_GID=2000 UWSGI_LAZY_APPS=1 UWSGI_WSGI_ENV_BEHAVIOR=holy
#CMD ["/venv/bin/uwsgi", "--http-auto-chunked", "--http-keepalive"]
