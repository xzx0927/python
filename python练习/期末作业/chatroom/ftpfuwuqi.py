import socket
import threading

import xlwt

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('10.12.220.172', 211))
s.listen(1)
print("等待连接")
wb = xlwt.Workbook()
sh = wb.add_sheet("text")
sh.write(0, 0, 'username')
sh.write(0, 1, 'password')
sh.write(1, 0, 'admin')
sh.write(1, 1, 'admin')
wb.save('text.xls')
while True:
    conn, addr = s.accept()

    print("连接成功")
    bt = conn.recv(1024)
    msg = bt.decode('utf-8')  # 将接受的消息解码
    print(msg)
    conn.send(msg.encode('utf-8'))  # 转发并编码
    conn.close()
