import socket

import threading

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('10.12.207.67', 211))

while True:
    info, addr = s.recvfrom(1024)  # 接受消息
    print(info.decode("utf-8"))  # 输出转义
    #  msg=info.decode("utf-8")[::-1]
    # msg = info.decode("utf-8").lower()#小写
    msg = info.decode("utf-8").upper()  # 大写
    s.sendto(msg.encode("utf-8"), addr)  # 发送消息
