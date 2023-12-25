import tkinter
from xlutils.copy import copy
from tkinter import messagebox
import pandas
import xlrd


class Chatroom:
    __root_username = None
    __root_password = None

    def __init__(self):
        self.__root = tkinter.Tk()
        self.__root.title('欢迎登录聊天室')
        self.__root.geometry('300x200')  # 宽度和高度
        tkinter.Label(self.__root, text='用户名:').place(x=30, y=30)
        tkinter.Label(self.__root, text='密码:').place(x=30, y=70)
        self.__root_username = tkinter.StringVar()
        self.__root_password = tkinter.StringVar()
        tkinter.Entry(self.__root, textvariable=self.__root_username).place(x=80, y=30)
        tkinter.Entry(self.__root, textvariable=self.__root_password, show='*').place(x=80, y=70)
        tkinter.Button(self.__root, text='登录', command=Chatroom.login).place(x=80, y=110)
        tkinter.Button(self.__root, text='注册', command=Chatroom.register).place(x=180, y=110)
        self.__root.mainloop()

    def login(self):  # 创建弹窗
        username = self.__root_username.get()
        password = self.__root_password.get()
        data = pandas.read_excel('text.xls')
        print(username, password)
        if username != '' and password != '':
            try:  # 通过异常处理解决对比false报错
                yan = data[data.username == username].password == password  # 和表格中的数据对比
                if yan.any() == True:  # 有一部分相同时就可以
                    messagebox.showinfo("登录成功", "登录成功")
                else:
                    messagebox.showinfo("登录失败", '用户名或密码错误')
            except:
                messagebox.showinfo("登录失败", '用户名或密码错误')

        else:
            messagebox.showinfo('登录失败', '用户名或密码为空')

    def register(self):
        username = self.__root_username.get()
        password = self.__root_password.get()
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

    def liaotian(self):
        username = self.__root_username.get()
        self.__root.destroy()  # 关闭之前窗口
        self.__windows = tkinter.Tk()  # 创建新窗口
        self.__windows.title("欢迎"+username+"进入聊天室")
        self.__root.geometry('300x200')


