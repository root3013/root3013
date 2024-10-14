import tkinter as tk
 
def on_checkbutton_clicked():
    if var.get():
        print("Checkbutton is selected")
        buttontext_1.insert('insert',1)
    else:
        print("Checkbutton is not selected")
 
root = tk.Tk()
root.title("Checkbutton Example")
buttontext_1=tk.Text(root)
 
var = tk.IntVar()  # 用于跟踪Checkbutton状态的变量
 
# 创建Checkbutton
checkbutton = tk.Checkbutton(root, text="选项", variable=var, command=on_checkbutton_clicked)
print(checkbutton)
checkbutton.pack()
buttontext_1.pack()
root.mainloop()