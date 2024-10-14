import tkinter as tk
from tkinter import messagebox
window=tk.Tk()
window.geometry('450x300')
entrysign_1=tk.StringVar()
entrysign_2=tk.StringVar()
entrysign_3=tk.StringVar()
##########################

def def_login():
    login_user=entry_1.get()
    login_password=entry_2.get()
    input_user=f"{login_user} {login_password}"
    with open('user_info.ini','r+',encoding="UTF-8") as user:
        lines=user.readlines()
    for line in lines:
        if input_user==line:
            messagebox.askokcancel(title='登陆成功',message="登陆成功")
    if line!=input_user:
        messagebox.askokcancel(title='警告',message='暂无注册')    
def def_sign(): 
    sign_up_window=tk.Toplevel(window)
    sign_up_window.title("注册用户")
    sign_up_window.geometry("320x200")
    signlabel_1=tk.Label(sign_up_window,text="用户名").place(anchor='nw',y=50,x=70)
    signlabel_2=tk.Label(sign_up_window,text="密码").place(anchor='nw',y=80,x=70)
    signlabel_2=tk.Label(sign_up_window,text="重复密码").place(anchor='nw',y=110,x=70)
    signbutton_1=tk.Button(sign_up_window,text="注册",command=sign_ing).place(x=150,y=140)
    signentry_1=tk.Entry(sign_up_window,textvariable=entrysign_1).place(y=50,x=130)
    signentry_2=tk.Entry(sign_up_window,textvariable=entrysign_2).place(y=80,x=130)
    signentry_3=tk.Entry(sign_up_window,textvariable=entrysign_3).place(y=110,x=130)
def sign_ing():
    ingentry_1=entrysign_1.get()
    ingentry_2=entrysign_2.get()
    ingentry_3=entrysign_3.get()
    if ingentry_2!=ingentry_3:
        messagebox.askokcancel(title='密码不一致',message="密码不一致,请重新输入")
        


###########################
canvas=tk.Canvas(window,height=200,width=500)
welcome_image=tk.PhotoImage(file='welcome.gif')
image=canvas.create_image(0,0,anchor='nw',image=welcome_image)
label_1=tk.Label(window,text='User :')
label_2=tk.Label(window,text='Password :')
button_1=tk.Button(window,text='Login',command=def_login)
button_2=tk.Button(window,text='Sign up',command=def_sign)
entry_1=tk.Entry(window)
entry_2=tk.Entry(window)
###########################
canvas.pack(side='top')
label_1.place(anchor='nw',y=175,x=110)
label_2.place(anchor='nw',y=200,x=110)
entry_1.place(anchor='nw',y=175,x=180)
entry_2.place(anchor='nw',y=200,x=180)
button_1.place(anchor='nw',y=225,x=190)
button_2.place(anchor='nw',y=225,x=245)
window.mainloop()