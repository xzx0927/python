from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
user=DummyAuthorizer()
user.add_user('admin','123',r'D:\垃圾',perm='elradfmwMT')
handler=FTPHandler
handler.authorizer=user
server=FTPServer(('169.254.212.4',21),handler=handler)
server.serve_forever()
# ftp.quit()