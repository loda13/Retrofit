# 建立一个FTP服务器（本机目录）
# 下载FTP目录中一个随机文件
# 然后邮件发送给自己的邮箱（文件以附件的形式发送）
# 接收邮件，将刚才发送的邮件接收（包括附件）下来，邮件内容保存到本地（包括附件）
# Author: TangYue

import ftplib
import os
import random

def connect(client):
    serverIp = "127.0.0.1"
    serverPort = 33
    client.connect(serverIp, serverPort)
    return client


def login(client):
    username = "user"
    password = "123456"
    client.login(username, password)
    return client


def list_file(client):
    client.dir()
    fileList = client.nlst()
    return fileList


def download_file(client, fileList, parentPath=""):
    remotePath = "./ftp/09flaskr.py.txt"
    localPath = "./download"
    if not os.path.exists(localPath):
        os.makedirs(localPath)
    localDir = "%s/ftp/09flaskr.py.txt" % localPath
    fileHandler = open(localDir, "wb")
    cmd = "RETR %s" % remotePath
    print("\n\n")
    print("download %s to %s" % (remotePath, localDir))
    ret = client.retrbinary(cmd, fileHandler.write, 1024)
    print(ret)


def client():
    ftpClient = ftplib.FTP()
    ftpClient = connect(ftpClient)
    ftpClient = login(ftpClient)
    print(ftpClient.welcome)
    fileList = list_file(ftpClient)
    return ftpClient, fileList


if __name__ == "__main__":
    ftpClient, fileList = client()
    download_file(ftpClient, fileList)
