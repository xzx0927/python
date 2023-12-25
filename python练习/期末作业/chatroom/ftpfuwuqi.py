import socket
import threading

import xlwt


def handler_jiesho(conn):
    while True:
        bt = conn.recv(1024)
        msg = bt.decode('utf-8')
        print("客户端IP：" + conn.getpeername()[0] + "端口：" + str(conn.getpeername()[1]) + "发送的是" + msg)
        # _conn.getpeername()返回的是addr（IP和端口）
        for _conn in connList:
            if conn != _conn:
                _conn.send(
                    ('ip:' + conn.getpeername()[0] + "端口:" + str(conn.getpeername()[1]) + '内容是:' + msg).encode(
                        'utf-8'))
        if msg == ".":
            break

def chushihuan():
    wb = xlwt.Workbook()
    sh = wb.add_sheet("text")
    sh.write(0, 0, 'username')
    sh.write(0, 1, 'password')
    sh.write(1, 0, 'admin')
    sh.write(1, 1, 'admin')
    wb.save('text.xls')
    print("初始化用户成功")


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('10.12.220.172', 211))
print("等待连接")
chushihuan()
s.listen(5)
global connList
connList = []
conn, addr = s.accept()
list.append(conn)
print("连接成功")
bt = conn.recv(1024)
tp = threading.Thread(target=handler_jiesho, args=(conn,))
tp.start()
# msg = bt.decode('utf-8')  # 将接受的消息解码
# print(msg)
# conn.send(msg.encode('utf-8'))  # 转发并编码
