from pathlib import Path
from ultralytics import YOLO

PROYECTO = Path(r"C:\Users\lepra\Documents\Universidad\VisionComputadores")
RUNS = PROYECTO / "runs" / "music"
NOMBRE = "modelo_entrenamiento"
LAST = RUNS / NOMBRE / "weights" / "last.pt"

def main():
    if LAST.exists():
        # Reanudar desde la última época guardada
        model = YOLO(str(LAST))
        model.train(resume=True)
    else:
        # No hay checkpoint: entrenar desde cero
        print(f"No existe {LAST}, se inicia un entrenamiento nuevo")
        model = YOLO("yolo26n.pt")
        model.train(
            data=str(PROYECTO / "music_dataset" / "data.yaml"),
            epochs=100,
            imgsz=640,
            batch=8,
            device="cpu",
            project=str(RUNS),
            name=NOMBRE,
        )
        print("Entrenamiento finalizado")

if __name__ == "__main__":
    main()