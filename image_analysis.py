import cv2
import numpy
import matplotlib.pyplot as plt

def procesar_partitura(partitura_grey):
    #Obtener la imagen binarizada de la imagen en escala de grises permite distinguir claramente entre fondo blanco y tinta negra
    #Las morfológicas de OpenCV funcionan de forma más intuitiva para detectar objetos blancos sobre fondo negro-->THRESH_BINARY_INV
    _,binario = cv2.threshold(partitura_grey,0,255,cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    altura, anchura = binario.shape


    #Sistema de detección de las líneas de la partitura
    #----------------------------------------------------------------------------------
    longitud = anchura//2

    #Se crea un elemento estructurante horizontal(línea horizontal)
    Ejemplo_línea = cv2.getStructuringElement(
        cv2.MORPH_RECT, #Forma rectangular
        (longitud, 1) #dimensión x, y
    )

    #filtra los elementos de la partitura con Ejemplo_línea y se queda con las líneas 
    imagen_lineas = cv2.morphologyEx(binario,
        cv2.MORPH_OPEN,
        Ejemplo_línea
    )

    #Contar cuántas líneas hay y sus posiciones
    num_pentagramas = 0
    num_lineas = 0
    nuevaLinea =True
    filas_vacias = 0

    posicion_lineas=[]

    for i in range(0,altura):#Recorrer los píxeles de arriba a a bajo
        num_pixelesBlancos = numpy.sum(imagen_lineas[i,:] == 255)#Blanco = 255
        if num_pixelesBlancos>=longitud:
            filas_vacias = 0 #Por si hay huecos intermedios en las líneas
            if nuevaLinea == True:
                num_lineas += 1
                nuevaLinea = False #Una línea podría ocupar más de una fila de píxeles
                posicion_inicio = i

        elif nuevaLinea == False:
            filas_vacias += 1
            if filas_vacias == 4:#Si hay varias filas vacías consecutivamente--> la línea terminó
                nuevaLinea =True
                posicion_final = i-4
                #Media entre la posicion vertical de la primera vez que se detecta la línea y la última vez 
                centro_vertical = (posicion_inicio + posicion_final)//2
                posicion_lineas.append(centro_vertical)

    num_pentagramas=int(num_lineas/5)
    #Sistema de detección de Símbolos musicales
    #-------------------------------------------------------------------------------
    imagen_simbolos = cv2.subtract(
        binario,
        imagen_lineas
    )

    imagen_lineas = cv2.bitwise_not(imagen_lineas)
    imagen_simbolos = cv2.bitwise_not(imagen_simbolos)

    return altura, anchura, num_pentagramas, imagen_lineas, imagen_simbolos, posicion_lineas