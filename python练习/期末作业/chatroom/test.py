import datetime

import socket
import threading
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
from xlutils.copy import copy
import pandas
import xlrd

ISOTIMEFORMAT = '%H:%M:%S'  # 定义时间格式
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def liaotian():
    def jieshou(c):
        user_list = []
        while True:
            content = c.recv(1024).decode('utf-8')  # 接受服务器发来的消息
            print(content)
            if content.endswith('~'):
                user_list.append(content.strip('~'))  # 接受用户名
                user_list = list(set(user_list))
                try:
                    list_onlineuser.delete('1.0', 'end')  # 清空滚动文本框
                    for name in user_list:
                        list_onlineuser.insert('end', name + '\n')
                        list_onlineuser.update()
                    list_user.delete('1.0', 'end')  # 清空已注册列表
                    data = pandas.read_excel('text.xls')  # 打开文件
                    user = data['username']
                    for name in user:
                        list_user.insert('end', name + '\n')
                        list_user.update()
                except:
                    print('1')
            else:
                curtime = datetime.datetime.now().strftime(ISOTIMEFORMAT)
                listbox.insert(tkinter.END, curtime + content + '\n')  # 将消息写入最后
                listbox.update()  # 更新聊天信息

    def fashou():  # 将消息发送到服务器
        msg= windows_xiaoxi.get()
        print(msg)
        c.send(msg.encode('utf-8'))
        windows_xiaoxi.set('')

    windows = Tk()  # 创建新窗口
    windows.title("欢迎进入聊天室")
    windows.geometry('500x300')
    listbox = ScrolledText(windows)  # 滚动文本框聊天窗口信息
    listbox.place(x=5, y=0, width=400, height=250)
    Label(windows, text='已注册人数').place(x=410, y=0)
    list_user = ScrolledText(windows)
    list_user.place(x=410, y=20, width=90, height=100)
    Label(windows, text='在线人数').place(x=410, y=120)
    list_onlineuser = ScrolledText(windows)
    list_onlineuser.place(x=410, y=140, width=90, height=100)
    # Button(windows, text='更新', command=gengxin).place(x=410, y=240)

    Label(windows, text='我:').place(x=10, y=270)
    windows_xiaoxi = StringVar()  # 聊天输入口
    windows_xiaoxi.set('')
    entryinput = Entry(windows, textvariable=windows_xiaoxi, width=40)
    entryinput.place(x=90, y=270)
    Button(windows, text='发送', command=fashou).place(x=400, y=270)
    threading.Thread(target=jieshou, args=(c,)).start()  # 启动线程服务（接受消息）
    windows.mainloop()


def lonig_run():  # 创建登录窗口
    def login():  # 创建弹窗
        username = root_username.get()
        password = root_password.get()
        data = pandas.read_excel('text.xls')
        if username != '' and password != '':
            try:  # 通过异常处理解决对比false报错
                yan = data[data.username == username].password == password  # 和表格中的数据对比
                print(yan)
                if yan.any() == True:  # 有完全相同时才可以
                    messagebox.showinfo("登录成功", "登录成功")
                    root.destroy()
                    c.connect(('10.12.220.172', 211))  # 创建连接
                    c.send(username.encode('utf-8'))  # 传输用户名
                    liaotian()  # 打开聊天窗口
                else:
                    messagebox.showinfo("登录失败", '用户名或密码错误')
            except:
                messagebox.showinfo("警告", '警告')

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


lonig_run()
