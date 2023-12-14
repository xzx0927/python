import socket
import threading


def handler_jieshou(info, addr,):
    print(info.decode("utf-8"))  # 输出转义
    # msg = info.decode("utf-8")
    # msg = info.decode("utf-8").lower()#小写
    a=list(set(addrList))#去重
    for _addr in a:
        print(_addr)
        if addr != _addr:
            msg = info.decode("utf-8")  # 消息
            s.sendto(msg.encode("utf-8"), _addr)  # 发送消息


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('10.12.207.67', 211))
global addrList
addrList = []
while True:
    print("进")
    info, addr = s.recvfrom(1024)
    addrList.append(addr)
    tp = threading.Thread(target=handler_jieshou, args=(info, addr))
    tp.start()
