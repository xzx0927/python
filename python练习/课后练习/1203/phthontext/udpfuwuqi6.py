import socket



global addrList
addrList = []
global kehu
kehu = {}
global kehu2
kehu2 = {}
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('192.168.78.215', 211))
while True:
    info, addr = s.recvfrom(1024)
    msg = info.decode('utf-8')
    temp = msg.split('#')#第一次为自己用户名，第二次消息格式为用户名#消息
    print(temp)
    print(type(temp))
    print(temp[0])
    if len(addrList) != 0:
        ss2 = kehu2.get(temp[0])
        for i in addrList:
            if addr != i:
                kehu.setdefault(addr, msg)
                kehu2.setdefault(msg, addr)
                addrList.append(addr)
                addrList = list(set(addrList))
                a = list(set(addrList))
                if ss2 == i:
                    s2 = kehu.get(addr)
                    s3 = s2 + '说：'
                    s.sendto((s3+temp[1]).encode('utf-8'), i)
                    print('---------------------')
    else:
        kehu.setdefault(addr, msg)
        kehu2.setdefault(msg, addr)
        addrList.append(addr)
