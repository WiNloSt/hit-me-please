FROM python:3.7-alpine

COPY requirements.txt /app/
WORKDIR /app/
RUN pip3 install -r requirements.txt

COPY . /app/

ENTRYPOINT [ "sh", "-c", "cd hit_me_please && python manage.py migrate && python manage.py runserver 0.0.0.0:8000" ]
