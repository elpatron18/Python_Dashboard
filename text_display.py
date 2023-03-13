import sys

import pygame
import numpy as np

# Erstelle ein Array mit Pixeln (hier: 32x32 Pixel)
pixels = np.zeros((32, 32, 3), dtype=np.uint8)

# Fülle das Array mit Farben (hier: alle Pixel rot)
pixels.fill(128)

# Erstelle eine Surface aus dem Array
surface = pygame.surfarray.make_surface(pixels)

from PIL import Image, ImageDraw, ImageFont

# Erstelle ein leeres Bild
img = Image.new('L', (200, 200), 255)

# Erstelle ein ImageDraw-Objekt
draw = ImageDraw.Draw(img)

# Definiere den Text und die Schriftart
text = 'Hello, world!'
font = ImageFont.truetype('fonts/NunitoSans.ttf', 20)

# Berechne die Größe des Textes
text_width, text_height = draw.textsize(text, font)

# Berechne die Position des Textes in der Mitte des Bildes
x = (img.width - text_width) // 2
y = (img.height - text_height) // 2

# Füge den Text in das Bild ein
draw.text((x, y), text, font=font, fill=0)

# Zeige das Bild an
img.show()


# Initialisiere Pygame
pygame.init()

# Erstelle ein Fenster
screen = pygame.display.set_mode((800, 600))

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
