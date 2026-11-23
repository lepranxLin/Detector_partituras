from ultralytics import YOLO
'''
# 1. Cargamos el modelo preentrenado YOLO26
model = YOLO("yolo26n.pt")

# 2. Entrenamos con nuestro dataset de partituras
model.train(
    data="dataset/data.yaml",
    epochs=100,
    imgsz=640,
    batch=8,
    device="cpu",
    project="runs/music",
    name="modelo_partituras"
)

print("Entrenamiento finalizado")
'''
def main():
    # Cargar el último entrenamiento guardado
    model = YOLO(
        "runs/detect/runs/music/modelo_partituras/weights/last.pt"
    )

    # Reanudar desde la última época guardada
    model.train(resume=True)

if __name__ == "__main__":
    main()