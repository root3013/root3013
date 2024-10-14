import tkinter as tk
import os
from tkinter import filedialog
window=tk.Tk()
window.title('pyinstaller by:wzl')
window.geometry('800x600')
window.configure(background='yellow')#容器背景
var1=tk.IntVar()
var2=tk.IntVar()
var3=tk.IntVar()
var_button=tk.IntVar()
var_button.set('目录确定')
check_box_D=''
check_box_w=''
all_text=''
###########################################################################
def def_check_box1():
    if var1.get():
        global check_box_D
        check_box_D='-F'
    else :
        check_box_D=''
    if var2.get():
        text.delete(1.0, tk.END)
        text.insert('insert',f"pyinstaller {check_box_D} {check_box_w} ")
    else:
        text.delete(1.0, tk.END)
        text.insert('insert',f"pyinstaller {check_box_D} ")
##########################################################################
print(check_box_D)
check_box_w=0
def def_check_box2():
    if var2.get():
        global check_box_w
        check_box_w='-w'
    else :
        check_box_w=''
    if var1.get():
        text.delete(1.0, tk.END)
        text.insert('insert',f"pyinstaller {check_box_D} {check_box_w} ")
    else:
        text.delete(1.0, tk.END)
        text.insert('insert',f"pyinstaller {check_box_w} ")
###########################################################################
def def_button():
    global all_text
    all_text = text.get('1.0', 'end-1c')
    print(all_text)
###########################################################################
def def_file_button():
    file_path = filedialog.askopenfilename()
    text.insert('insert',f'"{file_path}"')
###########################################################################
def def_ico_button():
    global ico_path
    ico_path = filedialog.askopenfile()
    ico_text.insert('insert',ico_path)
###########################################################################
text=tk.Text(window,height=1)
text.insert('insert','pyinstaller ')
ico_text=tk.Text(window,height=1)
button=tk.Button(window,textvariable=var_button,command=def_button)
file_button=tk.Button(window,text='拖入文件',command=def_file_button)
check_box_1=tk.Checkbutton(window,text='单个文件',bg="yellow",variable=var1,command=def_check_box1)
check_box_2=tk.Checkbutton(window,text='隐藏控制台',bg="yellow",variable=var2,command=def_check_box2)
label_1=tk.Label(window,text='本程序由pyinstaller实现，请确保已安装pyinstaller',bg='green',width=200)
ico_button=tk.Button(window,text='拖入ico文件',command=def_ico_button)
#############################################################################
label_1.pack()
check_box_1.pack()
check_box_2.pack()
ico_button.pack()
ico_text.pack()
file_button.pack()
text.pack()
button.pack()
#label_1.grid(row=0, column=0, columnspan=2, pady=10)
#check_box_1.grid(row=1, column=0, padx=5, pady=5)
#check_box_2.grid(row=1, column=1, padx=5, pady=5)
#file_button.grid(row=2, column=0, columnspan=2, pady=10)
#text.grid(row=3, column=0, columnspan=2, pady=10)
#button.grid(row=4, column=0, columnspan=2, pady=10)
window.mainloop()