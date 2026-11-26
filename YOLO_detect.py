from pathlib import Path
from ultralytics import YOLO
from collections import Counter

# Ruta del modelo entrenado
PROYECTO = Path(__file__).parent
MODELO = PROYECTO / "runs" / "music" / "modelo_entrenamiento" / "weights" / "last.pt"

# Cargar el modelo entrenado
model = YOLO(str(MODELO))


def detectar_simbolos(imagen):

    # Detectar los símbolos de la partitura
    resultados = model.predict(
        source=imagen,
        conf=0.5,
        imgsz=640,
        device="cpu",
        max_det=2000,
        verbose=False
    )

    simbolos = []

    for resultado in resultados:
        for box in resultado.boxes:

            clase = int(box.cls.item())
            nombre = model.names[clase]
            confianza = float(box.conf.item())

            # Coordenadas del rectángulo detectado
            x1, y1, x2, y2 = box.xyxy[0].tolist()

            # Guardar información del símbolo
            simbolos.append({
                "nombre": nombre,
                "clase": clase,
                "confianza": confianza,
                "x": (x1 + x2) / 2,
                "y": (y1 + y2) / 2,
                "x1": x1,
                "y1": y1,
                "x2": x2,
                "y2": y2
            })

    return simbolos


def contar_simbolos(simbolos):

    conteo = Counter()

    for simbolo in simbolos:
        conteo[simbolo["nombre"]] += 1

    return conteo