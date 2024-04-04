import socket

import threading


def handler_jie(c):
    while True:
        msg = input("输入")
        c.sendto(msg.encode("utf-8"), ('192.168.78.215', 211))


def handler_hui(c):
    while True:
        info, addr = c.recvfrom(1024)
        print(info.decode('utf-8'))  # str(addr)从哪发送过来


c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
c.bind(("",43932))

tp = threading.Thread(target=handler_jie, args=(c,))
tp.start()
tp1 = threading.Thread(target=handler_hui, args=(c,))
tp1.start()