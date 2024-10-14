import tkinter as tk
window=tk.Tk()
window.title("一键打包python 作者:wzl")
window.geometry('800x600')
var = tk.IntVar() 
D=0
def funbox_1():
    if var.get():
        D=1
    else:
        D=0

box_1=tk.Checkbutton(window,text='-D',variable=var,command=funbox_1)
print(D)

box_1.pack()
window.mainloop()