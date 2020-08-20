# 建立一个FTP服务器（本机目录）
# 下载FTP目录中一个随机文件
# 然后邮件发送给自己的邮箱（文件以附件的形式发送）
# 接收邮件，将刚才发送的邮件接收（包括附件）下来，邮件内容保存到本地（包括附件）
# Author: TangYue

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


def user():
    author = DummyAuthorizer()
    return author


def add_anonymous(author):
    homedir = "./ftp/"
    author.add_anonymous(homedir)
    return author


def add_user(author):
    name = "user"
    password = "123456"
    homedir = "./ftp/"
    perm = 'elradfmwMT'
    author.add_user(name, password, homedir, perm)
    return author


def server_n():
    author = user()
    author = add_anonymous(author)
    handler = FTPHandler
    handler.authorizer = author
    server = FTPServer(("127.0.0.1", 33), handler)
    server.serve_forever()


def server_u():
    author = user()
    author = add_user(author)
    handler = FTPHandler
    handler.authorizer = author
    server = FTPServer(("127.0.0.1", 33), handler)
    server.serve_forever()


if __name__ == "__main__":
    # server_n()
    server_u()
