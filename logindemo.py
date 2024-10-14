
import tkinter as tk
 
def login():
    # 假设用户名和密码正确
    if entry_username.get() == 'user' and entry_password.get() == 'pass':
        top.destroy()  # 关闭登录窗口
        create_main_window()
 
def create_login_window():
    global top
    top = tk.Tk()
    top.title("Login")
 
    label_username = tk.Label(top, text="Username:")
    label_username.pack()
    entry_username = tk.Entry(top)
    entry_username.pack()
 
    label_password = tk.Label(top, text="Password:")
    label_password.pack()
    entry_password = tk.Entry(top, show='*')
    entry_password.pack()
 
    button_login = tk.Button(top, text="Login", command=login)
    button_login.pack()
 
    top.mainloop()
 
def create_main_window():
    main_window = tk.Tk()
    main_window.title("Main Window")
    label_main = tk.Label(main_window, text="Welcome to the main window!")
    label_main.pack()
    main_window.mainloop()
 
create_login_window()