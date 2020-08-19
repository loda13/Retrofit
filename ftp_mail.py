# 建立一个FTP服务器（本机目录）
# 下载FTP目录中一个随机文件
# 然后邮件发送给自己的邮箱（文件以附件的形式发送）
# 接收邮件，将刚才发送的邮件接收（包括附件）下来，邮件内容保存到本地（包括附件）
# Author: TangYue
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

# 实例化DummyAuthorizer来创建ftp用户
authorizer = DummyAuthorizer()
# 参数：用户名，密码，目录，权限
authorizer.add_user('user', '12345', '/Users/yuetang2/Documents/croak', perm='elradfmwMT')
# 匿名登录
# authorizer.add_anonymous('/home/nobody')

handler = FTPHandler
handler.authorizer = authorizer

# 参数：IP，端口，handler
server = FTPServer(('127.0.0.1', 21), handler)
server.serve_forever()

