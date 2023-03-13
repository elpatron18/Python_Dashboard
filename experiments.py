import pygame
from PIL import Image
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    background_color = (255, 255, 255)  # Weiß
    screen.fill(background_color)

    img_width, img_height = 800, 600
    img = Image.new('RGB', (width, height), (255, 255, 255))

    pygame.display.flip()

pygame.quit()
