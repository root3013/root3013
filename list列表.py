import tkinter as tk
from tkinter import messagebox
window=tk.Tk()
window.geometry("400x500")
window.title("list BY:wzl geometry: 400x500")
list_var=tk.StringVar()
label_var=tk.StringVar()
ra_1=tk.IntVar()
ra_2=tk.IntVar()
ra_1.set(0)
ra_2.set(0)
flag_1=0
#######################################函数区域
def def_button1():
    lb_var=entry.get()
    lb.insert('end',lb_var)
def def_button2():
    if flag_1:
        lb_size=lb.size()
        for index in range(0,lb_size):
            lb.delete(0)
    else:
        del_index=lb.curselection()
        lb.delete(del_index)

def def_radiobutton1():
    global flag_1
    flag_1=1
def def_radiobutton2():
    global flag_1
    flag_1=0
def def_quit():
    if messagebox.askokcancel(title='退出程序',message="退出程序"):
        exit()
#######################################
def def_button3():
    lb_size=lb.size()
    for index in range(0,lb_size):
        tk.Radiobutton(window,text=lb.get(index),variable=ra_2,value=index).pack(anchor="w")
#######################################控件区域
button_1=tk.Button(window,text="插入",command=def_button1)
button_2=tk.Button(window,text='删除',command=def_button2)
button_3=tk.Button(window,text='刷新',command=def_button3)
radiobutton_1=tk.Radiobutton(window,text='全部删除',variable=ra_1,value=0,command=def_radiobutton1)
radiobutton_2=tk.Radiobutton(window,text='删除单个',variable=ra_1,value=1,command=def_radiobutton2)
lb=tk.Listbox(window,listvariable=list_var)
label_1=tk.Label(window,textvariable=label_var)
entry=tk.Entry(window)
menubar=tk.Menu()
quitfile=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label='退出',menu=quitfile)
quitfile.add_command(label='退出',command=def_quit)
#######################################位置区域
lb.pack()
entry.pack()
label_4=tk.Label(window).pack()
label_5=tk.Label(window).pack()
button_1.place(x=160,y=205)
button_2.place(x=205,y=205)
radiobutton_1.pack()
radiobutton_2.pack()
label_1.pack()
button_3.pack()
window.config(menu=menubar)
window.mainloop()