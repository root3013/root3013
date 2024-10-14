import tkinter as tk
window=tk.Tk()
window.title("are you hit")
window.geometry('800x600')
entry_1=tk.Entry(window,show='None')#可改为字符'*'
def insert_point():
    var=entry_1.get()
    text.insert('insert',var)
def insert_end():
    var=entry_1.get()
    text.insert('end',var)
Button_1=tk.Button(window,text='Insert me point',bg='green',command=insert_point)
Button_2=tk.Button(window,text='Insert me end',bg='green',command=insert_end)
text=tk.Text(window,height=2)#heigh决定文本框几行字
entry_1.pack()
Button_1.pack()
Button_2.pack()
text.pack()
window.mainloop()#刷新窗口