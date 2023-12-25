import socket
import threading
from tkinter.scrolledtext import ScrolledText
from tkinter import *
from xlutils.copy import copy
from tkinter import messagebox
import pandas
import xlrd


def login():  # 创建弹窗
    username = root_username.get()
    password = root_password.get()
    data = pandas.read_excel('text.xls')
    print(username, password)
    if username != '' and password != '':
        # try:  # 通过异常处理解决对比false报错
        yan = data[data.username == username].password == password  # 和表格中的数据对比
        if yan.any() == True:  # 有一部分相同时就可以
            messagebox.showinfo("登录成功", "登录成功")
            liaotian()
        else:
            messagebox.showinfo("登录失败", '用户名或密码错误')

    else:
        messagebox.showinfo('登录失败', '用户名或密码为空')


def register():
    username = root_username.get()
    password = root_password.get()
    data = pandas.read_excel('text.xls')
    if username != '' and password != '':
        yan = data[data.username == username].password == password
        if yan.any() == True:
            messagebox.showinfo("错误", "用户名和密码以注册")
        else:
            s = [password, username]
            du = xlrd.open_workbook('text.xls')
            d = du.sheet_by_index(0)  # 获取第一个工作表
            all_rows = d.nrows  # 获取表总行数
            wa = copy(du)  # 将xlrd转换为xlwt
            sheet = wa.get_sheet('text')
            sheet.write(all_rows, 0, s[0])
            sheet.write(all_rows, 1, s[1])
            wa.save('text.xls')
            messagebox.showinfo("注册成功", "注册成功")
    else:
        messagebox.showinfo('登录失败', '用户名或密码为空')


def liaotian():
    username = root_username.get()
    print(username)
    root.destroy()  # 关闭之前窗口
    windows = Tk()  # 创建新窗口
    windows.title("欢迎进入聊天室")
    windows.geometry('500x300')
    listbox = ScrolledText(windows)  # 滚动文本框
    listbox.place(x=5, y=0, width=400, height=250)
    Label(windows, text=username + ':').place(x=10, y=270)
    windows_xiaoxi = StringVar()
    Entry(windows, textvariable=windows_xiaoxi, width=40).place(x=90, y=270)
    Button(windows, text='发送', command=lambda: lianjie(windows_xiaoxi, listbox)).place(x=400, y=270)
    windows.mainloop()

def lianjie(xiaoxi, listbox):
    # c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # c.connect(('10.12.220.172', 211))
    xiao = xiaoxi.get()
    xiaoxi.set('')
    print(xiaoxi)
    bangding(xiaoxi)
    # c.send(xiao.encode('utf-8'))
    # x=c.recv(1024).decode('utf-8')
    # print(x)
    listbox.insert('end', "说的是" + xiao + '\n')


root = Tk()
root.title('欢迎登录聊天室')
root.geometry('300x200')  # 宽度和高度
Label(root, text='用户名:').place(x=30, y=30)
Label(root, text='密码:').place(x=30, y=70)
root_username = StringVar()
root_password = StringVar()
Entry(root, textvariable=root_username).place(x=80, y=30)
Entry(root, textvariable=root_password, show='*').place(x=80, y=70)
Button(root, text='登录', command=login).place(x=80, y=110)
Button(root, text='注册', command=register).place(x=180, y=110)
root.mainloop()


def bangding(xiaoxi):
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.connect(('10.12.220.172', 211))
    c.send(xiaoxi.encode('utf-8'))
    print(c.recv(1024).decode('utf-8'))
