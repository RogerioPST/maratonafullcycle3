FROM python:3.8.3

RUN apt-get update \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app
#instalando o django
COPY requirements.txt ./
RUN pip install -r requirements.txt
#fim de instalacao django
COPY . .
#lembrar de no docker file, colocar: ENV PYTHONUNBUFFERED=1
#se não, o output do python não aparece quando executa o docker
#ele inicia o server ok, mas não coloca no output as instruções e tal
ENV PYTHONUNBUFFERED=1
EXPOSE 8000
ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]