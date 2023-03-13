import tkinter as tk
from datetime import datetime

root = tk.Tk() #Neues Fenster
root.title("Digital Clock") #Titel
root.geometry("800x480")

text1 = tk.Label(
    root,
    font=('Arial', 20, 'bold'),
    bg="white",
    fg="black",
    height="180",
    width="200"
)
text1.config(
    text = "links"
)
text1.pack

text = tk.Label(
    root,
    font=('Arial', 20, 'bold'),
    bg="white",
    fg="black",
    height="180",
    width="400"
)
text.config(
    text = "Wilkommen"
)
text.pack()

text2 = tk.Label(
    root,
    font=('Arial', 20, 'bold'),
    bg="white",
    fg="black",
    height="180",
    width="200"
)
text2.config(
    text = "rechts"
)
text2.pack

uhr = tk.Label(
    root,
    font=('Arial', 80, 'bold'),
    bg='white',
    fg='black',
    height="300",
    width="800"
)
uhr.pack()

def update_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    uhr.config(text=current_time)
    root.after(1000, update_time)

update_time()
root.mainloop()
