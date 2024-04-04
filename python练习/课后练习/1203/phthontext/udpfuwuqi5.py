import socket
import threading

global addrList
addrList = []
global kehu
kehu = {}
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('192.168.78.215', 211))
while True:
    info, addr = s.recvfrom(1024)
    msg = info.decode('utf-8')
    print(len(addrList))
    print(kehu)
    if len(addrList) != 0:
        for _addr in addrList:
            if addr != _addr:
                kehu.setdefault(addr, msg)
                addrList.append(addr)
                addrList = list(set(addrList))
                a = list(set(addrList))
                s2 = kehu.get(addr)
                s3 = s2 + '说：'
                s.sendto((s3+msg).encode('utf-8'), _addr)
                print('_____')
    else:
        kehu.setdefault(addr, msg)
        addrList.append(addr)
