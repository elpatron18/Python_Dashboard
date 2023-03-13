# Python Display Cheatsheet
## Essentials
### 1. Pygame instaliieren und Display initialisieren
```commandline
import pygame
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
```
### Hintergrundfarbe
```commandline
background_color = (255, 255, 255) # Weiß
```

### 2. Display immer wieder aktualisieren
```commandline
pygame.display.flip()
```
### 3. Schleife zum Schließen des Displays
```commandline
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
```
## Objekte zum Einfügen
### Rechteck
```commandline
rect = pygame.Rect(100, 100, 50, 50) # x-Position, y-Position, Breite, Höhe
color = (255, 0, 0) # Rot
pygame.draw.rect(screen, color, rect)
```
### Bild
```commandline
rect = pygame.Rect(100, 100, 50, 50) # x-Position, y-Position, Breite, Höhe
color = (255, 0, 0) # Rot
pygame.draw.rect(screen, color, rect)
```
### Text
```commandline
font = pygame.font.Font(None, 36)
text = font.render("Hello World", True, (0, 0, 0)) # Text, Anti-Aliasing, Farbe (Schwarz)
x, y = 300, 300 # x-Position, y-Position
screen.blit(text, (x, y))
```
## Positionierung
### generell mit:
```commandline
x, y = 300, 300 # x-Position, y-Position
screen.blit(__NameDerVariable__, (x, y))
```
### Zentrieren
```commandline
x = display_width - object_width
y = some_y_coordinate 

screen.blit(object_surface, (x, y))
```
### Rechtsbündig
```commandline
x = (display_width - object_width) / 2
y = some_y_coordinate 

screen.blit(object_surface, (x, y))
```
## [Pillow](https://pillow.readthedocs.io/en/stable/)
### Bild erstellen und speichern
```commandline
from PIL import Image

# Größe des Bildes
width, height = 800, 600

# Erstelle neues Bild
img = Image.new('RGB', (width, height), (255, 255, 255)) # Weiß

# Speichere Bild
img.save('neues_bild.png')
```
### Bild auf virtuellem Screen anzeigen
```commandline
# Konvertiere Bild in Surface-Objekt
surface = pygame.surfarray.make_surface(np.array(img))

# Blit Surface-Objekt auf virtuellen Screen
x, y = 0, 0
screen.blit(surface, (x, y))
```
### Größe ändern
```commandline
from PIL import Image
# Öffne das Bild
image = Image.open("example.jpg")

# Ändere die Größe des Bildes auf 50x50 Pixel
resized_image = image.resize((50, 50))

# Speichere das veränderte Bild
resized_image.save("resized_example.jpg")
```
### Drehen
```commandline
# Drehe das Bild um 90 Grad im Uhrzeigersinn
rotated_image = image.rotate(-90)

# Speichere das veränderte Bild
rotated_image.save("rotated_example.jpg")
```
### Ausschnitt (Crop)
```commandline
# Öffne das Bild
image = Image.open("example.jpg")

# Schneide das Bild auf den Bereich zwischen 100x100 Pixel und 200x200 Pixel
cropped_image = image.crop((100, 100, 200, 200))

# Speichere das veränderte Bild
cropped_image.save("cropped_example.jpg")
```
## Tkinter Cheatsheet
### Import und Initialisierung
```commandline
import tkinter as tk
root = tk.Tk()
```
### Titel und Größe des Fensters setzen
```commandline
root.title("My Window")
root.geometry("800x600")
```
### Widgets erstellen
```commandline
label = tk.Label(root, text="Hello World")
button = tk.Button(root, text="Click me!", command=my_function)
entry = tk.Entry(root)
canvas = tk.Canvas(root, width=200, height=200)
```
### Widgets platzieren
```commandline
label.pack()
button.pack()
entry.pack()
canvas.pack()
```
### Ereignisse behandeln
```commandline
def my_function():
    print("Button clicked!")

button = tk.Button(root, text="Click me!", command=my_function)
```
### Starten des Hauptloops
```commandline
root.mainloop()
```