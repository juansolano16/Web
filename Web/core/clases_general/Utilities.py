import threading
import os
from PIL import Image

import random
import string

choiseActivo = [("S", "ACTIVO"),
                ("N", "INACTIVO"),
                (['S', 'N'], "TODOS"),]

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    #print("Random string of length", length, "is:", result_str)
    return result_str


def hiloManager(id_, function_, *args, **kwargs):
    try:
        hilo = threading.Thread(name = id_,
                                target=function_,
                                args=(args,),
                                kwargs=(kwargs),)
        # hilo.setDaemon(True)
        hilo.start()
        # hilo.join()
        return True
    except Exception as e:
        print('Error al iniciar el hilo: ' + str(id_) + ' --- ' + str(e))
        return False


def infoHilo(id_hilo):
    for hilo in threading.enumerate():
        if hilo.getName() == id_hilo:
            return True
    return False


def readDir(dir, file = 1):
    contenido = os.listdir(dir)
    if file == 0: return contenido
    file_ = []
    for fichero in contenido:
        if os.path.isfile(os.path.join(dir, fichero)):
            file_.append(fichero)
    return (file_)


def resize_image(path):
    img = Image.open(path)
    if (img.size[1] > 800):
        basewidth = 800
        wpercent = (basewidth / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        img = img.resize((basewidth, hsize), Image.ANTIALIAS)
        img.save(path)



