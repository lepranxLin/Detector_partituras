import pygame

# Inicializar salida estéreo
pygame.mixer.init(frequency=44100, size=-16, channels=2)

# Canales de reproducción
sol = pygame.mixer.Channel(0)
fa = pygame.mixer.Channel(1)

# Cargar notas
do4 = pygame.mixer.Sound("Notas.wav/Do1.wav")
do3 = pygame.mixer.Sound("Notas.wav/Do1.wav")

# Configurar altavoces
sol.set_volume(0.0, 1.0)  # Solo derecha
fa.set_volume(1.0, 0.0)   # Solo izquierda

# Reproducir simultáneamente
sol.play(do4)


input("Pulsa Enter para salir...")