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
EXPOSE 8000

ENV DJANGO_SETTINGS_MODULE=Runur.settings

# Call collectstatic (customize the following line with the minimal environment variables needed for manage.py to run):
#RUN DATABASE_URL=none /venv/bin/python manage.py collectstatic --noinput

#CMD ["./start.sh"]
CMD ["/usr/local/bin/uwsgi", "--emperor", "/srv/starter/uwsgi_docker.ini"]
