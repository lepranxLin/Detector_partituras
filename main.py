# Proyecto de Visión por Computadores: Detector_partituras
import argparse
import cv2
holaaaaaaaaaaaa
import matplotlib.pyplot as pyplot
import pygame

# importar scripts de las funciones
import image_analysis
import music_player

# script de YOLO
from YOLO_detect import detectar_simbolos, contar_simbolos


class Data:

    def __init__(self):
        self.num_lineas = 0
        self.num_pentagramas = 0
        self.matriz_lineas = ([])  # Contiene la posición vertical de cada línea agrupada por pentragramas
        self.espaciados = []


parser = argparse.ArgumentParser(
    description="Programa para cargar una partitura e interpretarla"
)
parser.add_argument("--imagen", "-i", type=str, default="sencillo.png")
args = parser.parse_args()

print("_______________Detector de Partituras__________________\n")
# Cargamos la imagen indicada por el usuario
partitura = cv2.imread(args.imagen)

if partitura is None:
    print("Error: no se pudo cargar la imagen.")
    exit()
else:
    print("Imagen cargada correctamente.")




# Transformar a escala de grises para desacerse del RGB
partitura_grey = cv2.cvtColor(partitura, cv2.COLOR_BGR2GRAY)

# Obtener información de la partitura
# ---------------------------------------------------------------------------
data = Data()
(
    altura,
    anchura,
    data.num_pentagramas,
    imagen_lineas,
    imagen_simbolos,
    posiciones_lineas,
) = image_analysis.procesar_partitura(partitura_grey)

data.num_lineas = len(posiciones_lineas)
print(f"Altura: {altura}; anchura: {anchura}; nº pentagramas: {data.num_pentagramas}\n")

# Guardar en una matriz de tamaño nº pentagramas * 5 (cada columna es la posición vertical de una línea)
for i in range(0, data.num_lineas, 5):
    pentagrama = posiciones_lineas[i : i + 5]  # Coge un grupo de 5 líneas
    data.matriz_lineas.append(pentagrama)  # Añade la fila a la matriz

# Mostrar las posiciones de las líneas
for i in range(0, data.num_pentagramas):
    #print(f"Pentagrama {i+1}\n")
    for j in range(0, 5):
        #print(f"Linea {j+1} : {data.matriz_lineas[i][j]}")

        if j < 4:
            espacio = data.matriz_lineas[i][j + 1] - data.matriz_lineas[i][j]
            data.espaciados.append(espacio)
            #print(f"Espacio {j+1} : {espacio}")

    #print()  # Salto de línea entre pentagramas distintos


# Imagen con los pentagramas
#pyplot.figure()
#pyplot.imshow(imagen_lineas, cmap="gray")
#pyplot.title("Filtros de pentagramas")


# Imagen con los símbolos
#pyplot.figure()
#pyplot.imshow(imagen_simbolos, cmap="gray")
#pyplot.title("Filtro de simbolos")

#pyplot.show(block=False)
#pyplot.pause(0.1)

# Detectar símbolos
simbolos=detectar_simbolos(partitura)
print(f"Total: {len(simbolos)}")

conteo = contar_simbolos(partitura)
for nombre, cantidad in conteo.most_common():
    print(f"{nombre}: {cantidad}")
# Reproducir las notas:
# -------------------------------------------------------------------------
start = input("¿Reproducir?(s/n): ")
if start == "s":
    music_player.reproducir()

pygame.quit()
