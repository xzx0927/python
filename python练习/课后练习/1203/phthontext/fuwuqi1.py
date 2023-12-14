import socket
import threading


# def handler_jiesho(conn):
#     while True:
#         bt = conn.recv(1024)
#         msg = bt.decode('utf-8')
#         print("客户端回复的是" + conn.getpeername()[0] + msg)
#         # _conn.getpeername()返回的是addr（IP和端口）
#         for _conn in connList:
#             if conn != _conn:
#                 _conn.send(
#                     ('ip:' + conn.getpeername()[0] + "端口:" + str(conn.getpeername()[1]) + '内容是:' + msg).encode(
#                         'utf-8'))
#         if msg == ".":
#             break
#
#
# def handler_huifu(conn):
#     while True:
#         s_msg = input('请输入' + '\n')
#         # conn.send(s_msg.encode('utf-8'))
#         for _conn in connList:
#             _conn.send(s_msg.encode("utf-8"))
#         if s_msg == ".":
#             break


def handler_bangding(conn):
    tishi = "输入自己的用户名"  # 用户名唯一
    conn.send(tishi.encode("utf-8"))
    bt = conn.recv(1024)
    n_name = bt.decode("utf-8")
    if kehu.get(n_name) is None:
        print("用户"+n_name+"绑定成功,ip是"+conn.getpeername()[0]+"端口号是"+str(conn.getpeername()[1]))
        kehu.setdefault(n_name, conn)
        tp = threading.Thread(target=handler_zhuanfa, args=(conn, n_name))
        tp.start()

    else:
        t = "用户名已存在"
        conn.send(t.encode("utf-8"))
        tp = threading.Thread(target=handler_bangding, args=(conn,))
        tp.start()


def handler_zhuanfa(conn, name):
    tishi = "输入想要发送给的用户名"  # 用户名唯一
    conn.send(tishi.encode("utf-8"))
    bt = conn.recv(1024)
    n_name = bt.decode("utf-8")
    if kehu.get(n_name) is not None:
        print("与" + name + "连接成功")
        speak = "输入发送的内容"
        conn.send(speak.encode("utf-8"))
        while True:
            bt1 = conn.recv(1024)
            neirong = bt1.decode("utf-8")
            print(name+"发送给"+n_name+"的内容是"+neirong)
            _conn = kehu.get(n_name)
            _conn.send((name + "发送的" + neirong).encode("utf-8"))
            if neirong == "..":
                tp = threading.Thread(target=handler_bangding, args=(conn,))
                tp.start()#要在发送一次消息才会跳出?需要再次循环???未break出去
                break
            elif neirong == ".":
                tp = threading.Thread(target=handler_zhuanfa, args=(conn, name))
                tp.start()#要在发送一次消息才会跳出
                break
    else:
        t = "用户不存在"
        conn.send(t.encode("utf-8"))
        tp = threading.Thread(target=handler_zhuanfa, args=(conn, name))
        tp.start()


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('192.168.219.215', 211))
s.listen(1)
print("等待连接")
global connList, kehu
kehu = {}
connList = []
if __name__ == "__main__":
    while True:
        conn, addr = s.accept()
        connList.append(conn)
        print("用户连接服务器成功")
        tp = threading.Thread(target=handler_bangding, args=(conn,))  # 用户只能建立一次连接
        tp.start()
        kehu.clear()
