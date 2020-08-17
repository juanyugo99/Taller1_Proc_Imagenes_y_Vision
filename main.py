# Taller 1 de la clase de Procesamiento de imágenes y visión
# Realizado por Juan Pablo Guerrero
# Pontificia Universidad Javeriana

import numpy as np
import cv2
import os

from color_image import *   # importa la clase desde el archivo color_image.py (deben estar en la misma carpeta)

if __name__ == '__main__':

    ruta = input('Cual es la ruta de la imagen?: ')     # ruta de la imagen

    nombre = input('cual es el nombre de la imagen?: ')     # nombre del archivo de la imagen

    imagen = color_image(ruta, nombre)      # crea el objeto "Imagen"

    imagen.display_image()      # muestra la imagen sin modificaciones

    imagen.dispplay_properties()        # muestra el tamaño de la imagen

    imagen.make_gray()      # muestra la imagen en escala de grises

    imagen.colorized_rgb('red')     # muestra la imagen en el canal de color deseado, en este caso en rojo(red)

    imagen.make_hue()       # muestra la imagen con tono resaltado

    cv2.waitKey(0)      # espera


