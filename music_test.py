import pygame
from pathlib import Path

# Inicializar salida estéreo
pygame.mixer.init(frequency=44100, size=-16, channels=2)

# Permitir hasta 64 sonidos simultáneos
pygame.mixer.set_num_channels(64)

# Carpeta de las notas
RUTA = Path(__file__).parent / "Notas.wav"


def reproducir_nota(nota, lado):

    sonido = pygame.mixer.Sound(str(RUTA / f"{nota}.wav"))

    # Buscar un canal libre
    canal = pygame.mixer.find_channel()

    if canal is None:
        print("No hay canales libres")
        return

    canal.play(sonido)

    # Configurar la salida del sonido
    if lado == "izquierda":
        canal.set_volume(1.0, 0.0)

    elif lado == "derecha":
        canal.set_volume(0.0, 1.0)

    else:
        canal.set_volume(1.0, 1.0)


def reproducir():

    reproducir_nota("La4#", "izquierda")
    reproducir_nota("Re4#", "izquierda")
    pygame.time.wait(500)

    reproducir_nota("Mi5", "derecha")
    reproducir_nota("Fa4#", "derecha")
    # Esperar hasta que terminen todos los sonidos
    while pygame.mixer.get_busy():
        pygame.time.wait(10)


if __name__ == "__main__":
    reproducir()
    pygame.quit()