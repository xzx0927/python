import socket

import threading


def handler_jie():
    while True:
        s_msg = input("输入"+'\n')
        c.send(s_msg.encode('utf-8'))


def handler_hui():
    while True:
        print(c.recv(1024).decode('utf-8'))



c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(('192.168.219.215', 211))

tp = threading.Thread(target=handler_jie,)
tp.start()
tp1 = threading.Thread(target=handler_hui,)
tp1.start()

