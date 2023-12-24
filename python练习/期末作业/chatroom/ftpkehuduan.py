# import socket
import threading
import tkinter
from tkinter import messagebox
import pickle


def login():  # 创建弹窗
    username = root_username.get()
    password = root_password.get()
    if username != '' and password != '':
        messagebox.showinfo("登录成功", "登录成功")
    else:
        messagebox.showinfo('登录失败', '用户名或密码为空')


def register():
    messagebox.showinfo('窗口名称', "注册成功")


root = tkinter.Tk()
root.title('欢迎登录聊天室')
root.geometry('300x200')  # 宽度和高度

tkinter.Label(root, text='用户名:').place(x=30, y=30)
tkinter.Label(root, text='密码:').place(x=30, y=70)

root_username = tkinter.StringVar()
root_password = tkinter.StringVar()
entry_username = tkinter.Entry(root, textvariable=root_username).place(x=80, y=30)  # 创建文本框
entry_password = tkinter.Entry(root, textvariable=root_password, show='*').place(x=80, y=70)

btn_login = tkinter.Button(root, text='登录', command=login).place(x=80, y=110)  # 按钮布局及其绑定方法
btn_register = tkinter.Button(root, text='注册', command=register).place(x=180, y=110)

root.mainloop()

# def handler_jie():
#     while True:
#         s_msg = input("输入" + '\n')
#         c.send(s_msg.encode('utf-8'))
#
#
# def handler_hui():
#     while True:
#         print(c.recv(1024).decode('utf-8'))
#
#
# c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# c.connect(('10.12.220.172', 211))
# tp1 = threading.Thread(target=handler_hui, )
# tp1.start()
# tp = threading.Thread(target=handler_jie, )
# tp.start()
