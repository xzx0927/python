# import socket
# import threading
# import Chatroom
#
# de = Chatroom
# de.Chatroom()
import tkinter

username="xie"
__windows = tkinter.Tk()  # 创建新窗口
__windows.title("欢迎进入聊天室")
__windows.geometry('500x300')
tkinter.Label(__windows, text=username+":").place(x=10, y=270)
__windows_dialog=tkinter.StringVar()
tkinter.Entry(__windows, textvariable=__windows_dialog,width='50').place(x=40, y=270)
tkinter.Button(__windows, text='发送',).place(x=400, y=270)
__windows.mainloop()

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
