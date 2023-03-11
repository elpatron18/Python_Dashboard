from PIL import Image, ImageDraw, ImageFont

# Bildgröße und Schriftart einstellen
WIDTH, HEIGHT = 640, 384
FONT_SIZE = 30
font = ImageFont.truetype("arial.ttf", FONT_SIZE)

# Bild erstellen und mit weiß füllen
image = Image.new("1", (WIDTH, HEIGHT), 255)
draw = ImageDraw.Draw(image)

# Text auf das Bild schreiben
text = "Hello, Raspberry Pi Dashboard!"
text_width, text_height = draw.textsize(text, font)
x = (WIDTH - text_width) // 2
y = (HEIGHT - text_height) // 2
draw.text((x, y), text, font=font, fill=0)

# Bild auf das E-Ink-Display übertragen
# Hier muss der Code ergänzt werden, um das E-Ink-Display anzusteuern

# Bild speichern und anzeigen
image.save("dashboard.png")
image.show()
