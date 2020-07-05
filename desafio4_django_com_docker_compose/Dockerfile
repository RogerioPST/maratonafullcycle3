FROM python:3

RUN useradd -ms /bin/bash django

USER django

ENV PYTHONUNBUFFERED 1

WORKDIR /home/django/hello_fullcycle

ENV PATH $PATH:/home/django/.local/bin

COPY requirements.txt /home/django/hello_fullcycle

RUN pip install -r requirements.txt

COPY . /home/django/hello_fullcycle

EXPOSE 8000

CMD ["python" ,"manage.py", "runserver", "0.0.0.0:8000"]