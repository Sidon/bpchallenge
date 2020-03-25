FROM python:3.8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN python -m pip install --upgrade pip

# install nginx
RUN apt-get update && apt-get install nginx vim -y --no-install-recommends
COPY nginx.default /etc/nginx/sites-available/default

#RUN ln -sf /dev/stdout /var/log/nginx/access.log \
#    && ln -sf /dev/stderr /var/log/nginx/error.log

RUN mkdir -p /opt/djangoapp
RUN mkdir -p /var/log/gunicorn
COPY README.rst /opt
WORKDIR  /opt/djangoapp

COPY web/ .
RUN pip install -r base_django/requirements.txt
# RUN ./manage.py collectstatic
# RUN apt install vim

RUN chown -R www-data:www-data /opt/djangoapp

# expose the port 8000
EXPOSE 8030
STOPSIGNAL SIGTERM
CMD ["./start-server.sh"]
# RUN ls -lhat