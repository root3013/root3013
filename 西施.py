import tkinter as tk

master = tk.Tk()

GIRLS = [
    ("西施", 1),
    ("王昭君", 2),
    ("貂蝉", 3),
    ("杨玉环", 4)]

v = tk.IntVar()

for girl, num in GIRLS:
    b = tk.Radiobutton(master, text=girl, variable=v, value=num)
    b.pack(anchor="w")

master.mainloop()
