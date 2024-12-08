import tkinter as tk
from tkinter import *

window = tk.Tk()
window.title("Radio Button")
window.geometry("800x600")
window.configure(bg="azure")

color = StringVar(value="green")

red_radio = tk.Radiobutton(window, text="Red", variable = color, value="red")
red_radio.pack()

green_radio = tk.Radiobutton(window, text="Green", variable = color, value="green")
green_radio.pack()

blue_radio = tk.Radiobutton(window, text="Blue", variable = color, value="blue")
blue_radio.pack()

show_button = tk.Button(window, text="Show", command=lambda: print(color.get()))
show_button.pack(pady=30)

window.mainloop()