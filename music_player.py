#Proyecto de Visión por Computadores
import pygame
import numpy as np
import time


pygame.mixer.init(frequency=44100,size=-16,channels=2)

NOTAS = [
    # Octava 4
    ("Do4", 261.63),
    ("Do4#", 277.18),
    ("Re4", 293.66),
    ("Re4#", 311.13),
    ("Mi4", 329.63),
    ("Fa4", 349.23),
    ("Fa4#", 369.99),
    ("Sol4", 392.00),
    ("Sol4#", 415.30),
    ("La4", 440.00),
    ("La4#", 466.16),
    ("Si4", 493.88),
]
NOTAS2 =[
    ("Fa4", 349.23),
    ("Fa4#", 369.99),
    ("Sol4", 392.00),
    ("Sol4#", 415.30),
    ("La4", 440.00),
    ("La4#", 466.16),
    ("Si4", 493.88),
]
def piano(frecuencia, duracion):
    sample_rate = 44100
    n = int(sample_rate * duracion)

    t = np.linspace(0, duracion, n, False)

    # Armónicos para darle un sonido parecido al piano
    onda = (
        1.00 * np.sin(2 * np.pi * frecuencia * t)
        + 0.50 * np.sin(2 * np.pi * frecuencia * 2 * t)
        + 0.25 * np.sin(2 * np.pi * frecuencia * 3 * t)
        + 0.12 * np.sin(2 * np.pi * frecuencia * 4 * t)
        + 0.06 * np.sin(2 * np.pi * frecuencia * 5 * t)
        + 0.03 * np.sin(2 * np.pi * frecuencia * 6 * t)
    )

    # Ataque de la tecla
    ataque = int(0.05 * sample_rate)

    if ataque < n:
        onda[:ataque] *= np.linspace(0, 1, ataque)

    # Decaimiento
    envolvente = np.exp(-3 * t / duracion)
    onda *= envolvente

    # Normalizar
    onda /= np.max(np.abs(onda))

    # Convertir a 16 bits
    onda = (onda * 18000).astype(np.int16)

    # Mono -> estéreo
    onda_estereo = np.column_stack((onda, onda))

    return pygame.sndarray.make_sound(onda_estereo)

def reproducir():
    # Recorrer la lista de notas
    for i in range(max(len(NOTAS), len(NOTAS2))):
        s1 = piano(NOTAS[i][1], 0.75)
        
        s1.play()

        time.sleep(0.35)
