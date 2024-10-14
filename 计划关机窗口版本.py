import tkinter as tk
import os
window=tk.Tk()#窗口容器（主要窗口）
window.title('计划关机  作者:wzl')#窗口标题
window.geometry('800x600')#容器大小
window.configure(background='grey')#容器背景
label_top=tk.Label(window,text='键入关机时间单位分钟',bg='green',width=5000)
entry=tk.Entry(window)
text=tk.Text(window,height=2)#heigh决定文本框几行字
var=tk.StringVar()
var.set('确定')
def shutdown():   
    long="shutdown -s -t "
    time=entry.get()
    if time.isnumeric():
        time=int(time)*60
        time=str(time)
        long=f"{long}{time}"
        text.delete(1.0, tk.END)
        text.insert('insert',f" 关机时间为_{int(int(time)/60)}分钟")
        os.system(long)
        var.set('设置成功')
    else:
        var.set('什么玩意')
        text.insert('insert','非法输入,请输入整数数字')
def cancel():
    quxiao='shutdown -a'
    text.delete(1.0, tk.END)
    text.insert('insert',"取消成功")
    os.system(quxiao)
button_1=tk.Button(window,textvariable=var,command=shutdown)
button_2=tk.Button(window,text='取消计划关机',command=cancel)
label_top.pack()
entry.pack()
button_1.pack()
button_2.pack()
text.pack()
window.mainloop()