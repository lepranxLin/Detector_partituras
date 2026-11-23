from ultralytics import YOLO
from collections import Counter

# Cargamos el modelo una sola vez
model = YOLO(
    "runs/detect/runs/music/modelo_partituras/weights/last.pt"
)

def detectar_simbolos(imagen):
    resultados = model.predict(
        source=imagen,
        conf=0.25,
        imgsz=640,
        max_det=500,
        verbose=False
    )

    simbolos = []

    for i in resultados:
        for box in i.boxes:
            clase = int(box.cls[0])
            nombre = model.names[clase]

            simbolos.append(nombre)

    return simbolos


def contar_simbolos(imagen):
    simbolos = detectar_simbolos(imagen)
    return Counter(simbolos)