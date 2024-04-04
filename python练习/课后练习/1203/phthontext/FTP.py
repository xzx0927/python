#FTP服务器搭建
# from pyftpdlib.authorizers import DummyAuthorizer
# from pyftpdlib.handlers import FTPHandler
# from pyftpdlib.servers import FTPServer
# user=DummyAuthorizer()
# user.add_user('admin','123',r'D:\新建文件夹',perm='elradfmwMT')
# handler=FTPHandler
# handler.authorizer=user
# server=FTPServer(('172.23.20.67',21),handler=handler)
# server.serve_forever()
from ftplib import FTP
ftp=FTP()
ftp.connect('169.254.212.4',21)
ftp.login('admin','123')
# print(ftp.getwelcome())
# for f in ftp.nlst():
#     print(f.encode('iso-8859-1').decode('gbk'))
# ftp.quit()

#下载
with open('ok.txt','wb') as f:
    ftp.retrbinary('RETR 11.txt',f.write)

# 上传
# with open('ok.txt','rb') as f:
#     ftp.storbinary('STOR 12.txt',f)
# ftp.quit()