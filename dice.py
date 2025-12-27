import tkinter as tk
import random

def roll():
    number = random.randint(1, 6)
    label.config(text=str(number))

root = tk.Tk()
root.title("Dice Roller")
root.geometry("200x200")

label = tk.Label(root, text="?", font=("Arial", 50))
label.pack(pady=20)

button = tk.Button(root, text="Roll Dice", command=roll)
button.pack()

root.mainloop()
