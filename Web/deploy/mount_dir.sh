#!/bin/bash

if mountpoint -q /home/Web/imagenes/ 
then
   echo "imagenes ya mounted"
else
   mount -t cifs //10.10.10.66/imagenes /home/Web/imagenes/ -o credentials=/home/Web/credfile
   echo "imagenes mounted ok"
fi

if mountpoint -q /home/Web/vbodegas 
then
   echo "vbodegas ya mounted"
else
   mount -t cifs //10.10.10.66/BodegaProveedores /home/Web/vbodegas -o credentials=/home/Web/credfile
   echo "vbodegas mounted ok"
fi

if mountpoint -q /home/Web/ComprobantesElectronicos 
then
   echo "ComprobantesElectronicos ya mounted"
else
   mount -t cifs //10.10.10.63/comprobantes /home/Web/ComprobantesElectronicos -o credentials=/home/Web/credfile
   echo "ComprobantesElectronicos mounted ok"
fi

#mount -t cifs //10.10.10.66/imagenes /home/Web/imagenes/ -o credentials=/home/Web/credfile
#mount -t cifs //10.10.10.66/BodegaProveedores /home/Web/vbodegas -o credentials=/home/Web/credfile
#mount -t cifs //10.10.10.63/comprobantes /home/Web/ComprobantesElectronicos -o credentials=/home/Web/credfile
