import socket
import threading


def handler_jiesho(conn):
    while True:
        bt = conn.recv(1024)
        msg = bt.decode('utf-8')
        print("客户端IP：" + conn.getpeername()[0]+"端口："+str(conn.getpeername()[1]) +"发送的是"+ msg)
        # _conn.getpeername()返回的是addr（IP和端口）
        for _conn in connList:
            if conn != _conn:
                _conn.send(
                    ('ip:' + conn.getpeername()[0] + "端口:" + str(conn.getpeername()[1]) + '内容是:' + msg).encode(
                        'utf-8'))
        if msg == ".":
            break


def handler_huifu(conn):
    while True:
        s_msg = input('请输入' + '\n')
        # conn.send(s_msg.encode('utf-8'))
        for _conn in connList:
            _conn.send(("服务器回复的是"+s_msg).encode("utf-8"))
        if s_msg == ".":
            break


def handler_bangding(conn):
    tishi = "输入自己的用户名"  # 用户名唯一
    conn.send(tishi.encode("utf-8"))
    bt = conn.recv(1024)
    n_name = bt.decode("utf-8")
    if kehu.get(n_name) is None:
        print("用户"+n_name+"绑定成功,ip是"+conn.getpeername()[0]+"端口号是"+str(conn.getpeername()[1]))
        kehu.setdefault(n_name, conn)
        tp = threading.Thread(target=handler_jiesho, args=(conn,))
        tp.start()
        tp1 = threading.Thread(target=handler_huifu, args=(conn,))
        tp1.start()
    else:
        t = "用户名已存在"
        conn.send(t.encode("utf-8"))
        tp = threading.Thread(target=handler_bangding, args=(conn,))
        tp.start()


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('192.168.219.215', 211))
s.listen(1)
if __name__ == "__main__":
    print("等待连接")
    global connList,kehu
    connList = []
    kehu={}
    while True:
        conn, addr = s.accept()
        connList.append(conn)
        print("连接成功")
        tp=threading.Thread(target=handler_bangding, args=(conn,))
        tp.start()
        # tp = threading.Thread(target=handler_jiesho, args=(conn,))
        # tp.start()
        # tp1 = threading.Thread(target=handler_huifu, args=(conn,))
        # tp1.start()
