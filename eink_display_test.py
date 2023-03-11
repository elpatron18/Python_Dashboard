import pygame

# Bildgröße einstellen (entspricht der Größe des E-Ink-Displays)
WIDTH, HEIGHT = 640, 384

# Pygame initialisieren
pygame.init()

# Fenster erstellen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Raspberry Pi Dashboard")

# Schriftart und Text definieren
font = pygame.font.SysFont("arial", 50)
text = "Hello, Raspberry Pi Dashboard!"

# Text als Bild rendern
text_surface = font.render(text, True, (0, 0, 0))

# Text auf das Display zeichnen
screen.blit(text_surface, ((WIDTH - text_surface.get_width()) // 2, (HEIGHT - text_surface.get_height()) // 2))

# Display aktualisieren
pygame.display.flip()

# Schleife für das Fenster-Rendering
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Pygame beenden
pygame.quit()
