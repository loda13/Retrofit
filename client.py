# 使用socket模块，建立一个聊天工具
# 功能与qq聊天相同，有两个窗口，可以输入，可以退出
# 要求使用面向对象编程
# Author:TangYue
import socket
import sys

from click._compat import raw_input


class Client:
    host, port = input('please enter host address like host:port: ').split(':')
    sc = socket.create_connection((host, int(port)))

    def verify(self):
        try:
            host, port = self.host, self.port
        except ValueError:
            print('the address is wrong')
            sys.exit(-1)
        if len(host) == 0 or len(port) == 0:
            print('the address is wrong')
            sys.exit(-1)
        else:
            self.sc
        print(
            'connect successfully' + '\n' + 'wait for server' + '\n' + 'press Enter with noting input to quit')
        self.sc.send(b'hello server.')

    def message(self):
        while True:
            response = self.sc.recv(1024)
            print('from server:', response.decode())
            msg = input('text: ')
            if len(msg) > 0:
                self.sc.send(msg.encode())
                print('sent')
            else:
                print('now quit')
                self.sc.close()
                break


if __name__ == '__main__':
    run = Client()
    run.verify()
    run.message()
