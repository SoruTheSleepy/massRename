import tkinter as tk

window = tk.Tk()
window.minsize(400, 200)

label = tk.Label(text = "Name")
entry = tk.Entry(fg = "#292929", bg = "#fefefe", width = 50)

label.pack()
entry.pack()

entry.delete(0)

name = entry.get()

button = tk.Button(
    text = "Envoyer",
    background = "#fefefe",
    borderwidth = 2
)
button.pack()

window.mainloop()