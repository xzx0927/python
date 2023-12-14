import socket
import threading


def handler(c):
    while True:
        info, addr = c.recvfrom(1024)
        s1 = info.decode('utf-8')
        print(s1)

def handler1(c):
    while True:
        s = input('请输入：')
        y = s.encode('utf-8')
        c.sendto(y, ('192.168.56.1', 211))



c = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
c.bind(('192.168.56.1', 11233))
t = threading.Thread(target=handler, args=(c,))
t.start()
s = input('请输入你的名字：')
y = s.encode('utf-8')
c.sendto(y, ('192.168.56.1', 211))
t = threading.Thread(target=handler1, args=(c,))
t.start()

