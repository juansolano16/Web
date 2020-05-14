#!/bin/bash

#SQLITE PYTHON 3.2
export LD_LIBRARY_PATH="/usr/local/lib"

NAME="Web" # Nombre de la aplicación
DJANGODIR=/home/Web/ #Ruta de la carpeta de la aplicación
SOCKFILE=/home/Web/run/gunicorn.sock #Ruta donde se creará el archivo de socket unix para comunicarnos
LOGDIR=${DJANGODIR}logs/gunicorn.log #Carpeta donde estara los logs del gunicorn
USER=juansolano #Usuario con el que vamos a correr el sitio web
GROUP=jair #Grupo con el que vamos a correr el sitio web
NUM_WORKERS=3 #Número de procesos que se van a utilizar para correr la aplicación
DJANGO_SETTINGS_MODULE=Web.settings #Ruta de los settings
DJANGO_WSGI_MODULE=Web.wsgi #Nombre del módulo wsgi


# Activar el entorno virtual
cd $DJANGODIR
source ./env/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Crear la carpeta run si no existe para guardar el socket linux
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Iniciar la aplicación django por medio de gunicorn
#exec gunicorn Web.wsgi:application --bind 0.0.0.0:8000
exec gunicorn ${DJANGO_WSGI_MODULE}:application \
--bind=unix:$SOCKFILE \
--name $NAME \
--workers $NUM_WORKERS \
#--user=$USER --group=$GROUP \
--log-level=debug \
--log-file=-
