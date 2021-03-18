# REST API using Django Rest Framework

## Description

- The context of this project is to provide a simple web service for storing and retrieving mountain peaks.
 

## Running project without docker

### Install the dependencies

    pip install -r requirements.txt

### Launch api
    postgresql database should be installed.
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
    

## Launch with docker

- To Run the docker containers

     docker-compose up

- To migrate use the following command

    docker exec -it project_meteo_web_1 python manage.py migrate --noinput