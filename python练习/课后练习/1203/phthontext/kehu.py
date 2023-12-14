import socket

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(('10.12.207.67', 250))

while True:
    s_msg = input("请输入要发送的消息:")
    c.send(s_msg.encode('utf-8'))
    print(c.recv(1024).decode('utf-8'))

# c.close()
