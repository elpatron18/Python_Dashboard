import pygame
import numpy as np

# Erstelle ein Array mit Pixeln (hier: 32x32 Pixel)
pixels = np.zeros((32, 32, 3), dtype=np.uint8)

# Fülle das Array mit Farben (hier: alle Pixel rot)
pixels[:,:,0] = 255

# Erstelle eine Surface aus dem Array
surface = pygame.surfarray.make_surface(pixels)

# Initialisiere Pygame
pygame.init()

# Erstelle ein Fenster
screen = pygame.display.set_mode((400, 400))

# Zeige die Surface im Fenster an
screen.blit(surface, (0, 0))

# Aktualisiere das Fenster
pygame.display.flip()

# Schleife, um das Fenster offen zu halten
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
