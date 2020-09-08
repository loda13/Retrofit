# 建立一个FTP服务器（本机目录）
# 下载FTP目录中一个随机文件
# 然后邮件发送给自己的邮箱（文件以附件的形式发送）
# 接收邮件，将刚才发送的邮件接收（包括附件）下来，邮件内容保存到本地（包括附件）
# Author: TangYue

import smtplib
import poplib
import base64
import sys

from email.mime.text import MIMEText
from email.header import Header
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr


def send_email(msg):
    args = sys.argv[1:]
    sender = "yuetang2@iflytek.com"
    receivers = ["yuetang2@iflytek.com"]
    user = args[0]
    password64 = args[1].encode("utf-8")
    password = args[1]

    smtpObj = smtplib.SMTP("mail.iflytek.com")

    smtpObj.login(user, password)

    errs = smtpObj.sendmail(sender, receivers, msg.as_string())
    print(errs)


def recevice_email():
    args = sys.argv[1:]
    user = args[0]
    password64 = args[1].encode("utf-8")
    # base64.decodebytes(password64).decode("utf-8")
    password = args[1]
    server = "mail.iflytek.com"

    pop3Obj = poplib.POP3(server)
    print(pop3Obj.welcome.decode("utf-8"))
    pop3Obj.user(user)
    pop3Obj.pass_(password)
    pop3Obj.set_debuglevel(1)  # 打开调试信息

    email_num, email_size = pop3Obj.stat()
    print(email_num, email_size)

    rsp, msg_list, rsp_siz = pop3Obj.list()
    print(msg_list)

    rsp, msglines, msgsiz = pop3Obj.retr(len(msg_list))
    content = b'\r\n'.join(msglines).decode('utf-8')
    msg = Parser().parsestr(text=content)

    __get_address(msg)
    __get_subject(msg)
    __get_content(msg)


def __get_subject(msg):
    subject = msg['Subject']
    value, charset = decode_header(subject)[0]
    print(value.decode(charset))


def __get_address(msg):
    fromAddr = msg["From"]
    head, addr = parseaddr(fromAddr)
    value, charset = decode_header(head)[0]
    print(value, addr)

    toAddr = msg["to"]
    for li in toAddr.split(","):
        print(li.strip())


def __get_content(msg):
    content = msg.get_payload()
    if type(content) == list:
        for sContent in content:
            __get_content(sContent)
    else:
        contentType = msg["Content-Type"]
        charset = msg["charset"] if msg["charset"] else "gbk"
        transfer = msg['Content-Transfer-Encoding']
        if "text/plain" in contentType:
            if transfer == "base64":
                contentStr = base64.decodebytes(content.encode(charset))
                contentStr = contentStr.decode(charset)
                print(contentStr)
        elif "text/html" in contentType:
            print(content)
        else:
            fileName64 = msg.get_filename().split("?")[3]
            fileName = base64.decodebytes(fileName64.encode(charset))
            fileName = fileName.decode(charset)
            print(fileName)


def create_email():
    send_file = open(r"./download/test.txt", 'rb').read()
    msg = MIMEText(send_file, 'base64', _charset="utf-8")


    msg["From"] = Header("yuetang2")

    msg["to"] = Header("yuetang2")

    msg["Subject"] = Header("yuetang2 09flaskr.py.txt", 'utf-8')
    return msg


if __name__ == "__main__":
    msg = create_email()
    send_email(msg)
    recevice_email()
