import tkinter as tk
from tkinter import messagebox
import os
from tkinter import filedialog
window=tk.Tk()
window.geometry('800x600')
window.configure(background='green')
window.title('Py一键打包 by:wzl')
##################################
global var1
global var2
global var3
flag1=0
flag2=0
flag3=0
flag4=0
var1=tk.IntVar()
var2=tk.IntVar()
var3=tk.IntVar()
##################################
def def_ico_button():
    global flag3
    global ico_path
    flag3=1
    ico_path = filedialog.askopenfilename()
    label_3.config(text=f"已包含图标:{ico_path}")
def def_file_button():
    global file_path
    global flag4
    flag4=1
    file_path = filedialog.askopenfilename()
    label_4.config(text=f"py地址:  {file_path}")
def def_button_1():
    global juzi
    juzi='pyinstaller '
    if flag1:
            juzi=f"{juzi} -F"
    if flag2:
            juzi=f"{juzi} -w"
    if flag3:
            juzi=f"{juzi} -i {ico_path}"
    if flag4:
        label_2.config(text="")
        juzi=f"{juzi} {file_path}"
        print(juzi)
        os.system(juzi)
        label_2.config(text='恭喜您制作完成,前往软件目录dist文件夹查看')
    else:
         label_2.config(text="请拖入py文件!!")  
def box1():
    global flag1
    if var1.get():
        flag1=1
    else:
        flag1=0
def box2():
    global flag2
    if var2.get():
        flag2=1
    else:
        flag2=0
def box3():
    global flag3
    if var3.get():
        flag3=1
    else:
        flag3=0
def quit():
     if messagebox.askokcancel(title='退出',message='退出'):
        exit()
##################################
check_1=tk.Checkbutton(window,text='-F 单个文件',bg='green',variable=var1,command=box1)
check_2=tk.Checkbutton(window,text='-w 隐藏命令行',bg='green',variable=var2,command=box2)
#check_3=tk.Checkbutton(window,text='-i',variable=var3,command=box3)
button_1=tk.Button(window,text='打包',bg='grey',command=def_button_1)
ico_button=tk.Button(window,text='拖入图标文件',bg='green',command=def_ico_button)
file_button=tk.Button(window,text='拖入.py文件',bg='green',command=def_file_button)
label_1=tk.Label(window,text='本程序由pyinstaller实现，请确保已安装pyinstaller',bg='green',width=200)
label_2=tk.Label(window,text='',bg='green',width=200)
label_3=tk.Label(window,text='当前为默认图标',bg='green',width=200)
label_4=tk.Label(window,text='请输入py地址',bg='green',width=200)
##################################菜单文件
menubar=tk.Menu(window)
openfile=tk.Menu(menubar,tearoff=0)
quitfile=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label='打开',menu=openfile)
menubar.add_cascade(label='退出',menu=quitfile)
openfile.add_command(label='打开文件',command=def_file_button)
openfile.add_command(label='打开图片',command=def_ico_button)
quitfile.add_command(label='退出',command=quit)
##################################
label_1.pack()
ico_button.pack()
file_button.pack()
check_1.pack()
check_2.pack()
button_1.pack()
label_2.pack()
label_3.pack()
label_4.pack()
window.config(menu=menubar)
window.mainloop()