FROM python:3
ENV PYTHONUNBUFFERED 1
RUN python -m pip install --upgrade pip
RUN mkdir /docker-django
WORKDIR /docker-django
COPY base_django/requirements.txt ./
RUN pip install -r requirements.txt

COPY . .


