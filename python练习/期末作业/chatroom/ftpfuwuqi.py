import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('10.12.220.172', 211))
s.listen(1)
print("等待连接")
while True:
    conn, addr = s.accept()
    print("连接成功")
    bt=conn.recv(1024)
    msg=bt.decode('utf-8')#将接受的消息解码
    print(msg)
    conn.send(msg.encode('utf-8'))#转发并编码
    conn.close()