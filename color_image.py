# Clase creada por Juan Pablo Guerrero para la clase de Procesamiento de imágenes y visión
# Pontificia Universidad Javeriana

import numpy as np
import cv2
import os

class color_image:

    def __init__(self, path, image_name): # constructor, recibe la ruta de la imagen y el nombre
        self.path = path
        self.image_name = image_name
        self.total_path = os.path.join(path, image_name) # junta ambos strings
        self.saved_image = cv2.imread(self.total_path) # accede a la imagen y la guarda en el atributo

    def display_image(self): # metodo para mostrar la imagen original
        return cv2.imshow(self.image_name , self.saved_image)

    def dispplay_properties(self): # metodo para mostrar las propiedades de la imagen
        self.width, self.height, self.channels = self.saved_image.shape # se guardan los valores de tamaño de la imagen
        return print('image "{}" properties:'.format(self.image_name), 'width:', self.width, 'height', self.height) # se muestran en el print

    def make_gray(self): # muestra la imagen en escala de grises
        self.image_gray = cv2.cvtColor(self.saved_image, cv2.COLOR_BGR2GRAY) # se convierte el espacio de BGR a Grises
        return cv2.imshow('Gray scale of {}'.format(self.image_name), self.image_gray) #se muestra la imagen gris

    def colorized_rgb(self,color): # muestra la imagen en un solo canal de color, como entrada se solicita cual color se quiere mostrar
        self.colorized_image = self.saved_image.copy() # se realiza una copia de la imagen en un nuevo atributo

        if color == 'red': # si se solicita la imagen en rojo
            self.colorized_image[:, :, (0, 1)] = 0  # color rojo
        if color == 'blue': # si se solicita la imagen en azul
            self.colorized_image[:, :, (1, 2)] = 0  # color azul
        if color == 'green': # si se solicita la imagen en verde
            self.colorized_image[:, :, (0, 2)] = 0  # color green

        cv2.imshow('{} in {}'.format(self.image_name,color), self.colorized_image) # se muestra la imagen colorizada
    def make_hue(self): # se muestra la imagen con el tono resaltado
        self.image_HSV = cv2.cvtColor(self.saved_image, cv2.COLOR_BGR2HSV) # se convierte el espacio de BGR a HSV
        self.image_HSV[:, :, (1, 2)]= 255 # se modifican los canales S(saturation) y V(value) al maximo sin modificar el H(Hue)
        self.image_HUE = cv2.cvtColor(self.image_HSV, cv2.COLOR_HSV2BGR) # se convierte el espacio de HSV a BGR

        cv2.imshow('{} make hue'.format(self.image_name),self.image_HUE) # se muestra la nueva imagen