FROM python:3.8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN python -m pip install --upgrade pip

RUN mkdir -p /opt/djangoapp
RUN mkdir -p /var/log/gunicorn
COPY README.rst /opt
WORKDIR  /opt/djangoapp

COPY web/ .
RUN pip install -r base_django/requirements.txt
# RUN ./manage.py collectstatic
# RUN apt install vim

# expose the port 8000
EXPOSE 8000

# CMD ["ls"]


# define the default command to run when starting the container
CMD ["gunicorn", "--bind", ":8000", "--error-logfile", "/var/log/gunicorn/errors", "base_django.wsgi:application"]