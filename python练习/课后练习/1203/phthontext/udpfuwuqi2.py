import socket
import threading


def handler_jieshou(s):
    while True:
        info, addr = s.recvfrom(1024)
        print("客户段发送的是"+info.decode("utf-8"))  # 输出转义


def handler_fashou(addr):
    while True:
        msg = input("输入想要发送的消息")
        s.sendto(msg.encode("utf-8"), addr)


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('10.12.207.67', 211))
info, addr = s.recvfrom(1024)
tp = threading.Thread(target=handler_jieshou, args=(s,))
tp.start()
tp1 = threading.Thread(target=handler_fashou, args=(addr,))
tp1.start()
