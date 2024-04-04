import socket

import threading



s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('172.23.20.21', 211))
while True:
    info,addr=s.recvfrom(1024)#接受消息
    print(info.decode("utf-8"))#输出转义
    msg=info.decode("utf-8")
    s.sendto(msg.encode("utf-8"),addr)#发送消息

