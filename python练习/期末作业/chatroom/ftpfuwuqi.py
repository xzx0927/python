import socket
import threading
import time

import xlwt

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('10.12.220.172', 211))
print("等待连接")

s.listen()
user_list = []
socket_list = []  # 用于储存ip和其他信息


def donglutishi(s, username):
    # try:
    print(s.recv(1024).decode('utf-8'))
    return s.recv(1024).decode('utf-8')
    # except:
    #     for _conn in socket_list:
    #         _conn.send(('系统消息' + username + '离开了聊天室').encode('utf-8'))
    #         user_list.remove(username)
    #         s.close()


def he(s, username):  # 接受消息并转发
    if username.endswith('~'):  # 判断是否为用户名
        kehuduan = socket_list.copy()
        for _conn in kehuduan:
            for _user in user_list:
                _conn.send(_user.encode('utf-8'))
    while True:
        xiaoxi = s.recv(1024).decode('utf-8')
        print(xiaoxi)
        if xiaoxi == '':
            break
        else:
            print(socket_list)
            for _conn in socket_list:
                _conn.send(('用户' + username + '说:' + xiaoxi).encode('utf-8'))


def chushihuan():
    wb = xlwt.Workbook()
    sh = wb.add_sheet("text")
    sh.write(0, 0, 'username')
    sh.write(0, 1, 'password')
    sh.write(1, 0, 'admin')
    sh.write(1, 1, 'admin')
    wb.save('text.xls')
    print("初始化用户成功")


chushihuan()  # 初始化用户信息
while True:
    conn, addr = s.accept()
    socket_list.append(conn)
    print("连接成功")
    bt = conn.recv(1024).decode('utf-8')  # 接受用户名
    bt = bt + '~'
    user_list.append(bt)
    user_list = list(set(user_list))  # 去重
    for _conn in socket_list:
        x = str(bt).strip('~')
        _conn.send(('系统消息:' + x + '进入聊天室').encode('utf-8'))
    print(user_list)
    time.sleep(1)
    tp = threading.Thread(target=he, args=(conn, bt,))
    tp.start()
