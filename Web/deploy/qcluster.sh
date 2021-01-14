#!/bin/bash

#SQLITE PYTHON 3.2
export LD_LIBRARY_PATH="/usr/local/lib"

NAME="Web" # Nombre de la aplicación
DJANGODIR=/home/Web/ #Ruta de la carpeta de la aplicación
SOCKFILE=/home/Web/run/gunicorn.sock #Ruta donde se creará el archivo de socket unix para comunicarnos
LOGDIR=${DJANGODIR}logs/gunicorn.log #Carpeta donde estara los logs del gunicorn
USER=juansolano #Usuario con el que vamos a correr el sitio web
GROUP=root #Grupo con el que vamos a correr el sitio web
NUM_WORKERS=3 #Número de procesos que se van a utilizar para correr la aplicación
DJANGO_SETTINGS_MODULE=config.settings #Ruta de los settings
DJANGO_WSGI_MODULE=config.wsgi #Nombre del módulo wsgi

# Activar el entorno virtual
cd $DJANGODIR
source ./env/bin/activate
#export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
#export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Activa qcluster
exec python manage.py qcluster
