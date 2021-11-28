FROM python:latest
RUN mkdir /code
RUN apt-get update  \
    && apt-get install -y postgresql-client
COPY requirements.txt /code
RUN pip install --upgrade pip
RUN pip install -r /code/requirements.txt
COPY . /code/
WORKDIR /code/Bus_booking_system
CMD python manage.py migratedocker-compose exec [containerID] ./app/console migrations:migrate --no-interaction
CMD python manage.py runserver 0.0.0.0:8000