import tkinter as tk
window=tk.Tk()
window.title("are you hit")
window.geometry('800x600')
label_1=tk.Label(window,text='OMG!',bg='green',font=('Ariak',12),width=15,height=2)
label_1.pack()#窗口位置
var=tk.StringVar()
on_hit=False

def hit_me():
    global on_hit
    if on_hit==False:
        on_hit = True
        var.set('you hit me')
    else:
        on_hit=False
        var.set('')

button_1=tk.Button(window,textvariable=var,bg='grey',width=15,height=2,command=hit_me)
button_1.pack()
window.mainloop()