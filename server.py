# 使用socket模块，建立一个聊天工具
# 功能与qq聊天相同，有两个窗口，可以输入，可以退出
# 要求使用面向对象编程
# Author:TangYue
import socket


class Server:
    HOST = '127.0.0.1'
    PORT = 3333
    # buffSize = 1024
    sc = socket.socket()
    # sc.settimeout(5)
    sc.bind((HOST, PORT))
    sc.listen(1)

    def __init__(self):
        print(f'the server is listening at {Server.HOST}:{Server.PORT}')
        print('waiting for conntection...')
        conn, addr = Server.sc.accept()
        print(f'connect success addr={addr}')
        print('connect successfully'+'\n'+'wait for server'+'\n'+'press Enter with noting input to quit')
        while True:
            msg = conn.recv(1024)
            print('from client:', msg.decode())
            response = input('text: ')
            if len(response) > 0:
                conn.send(response.encode())
                print('sent')
            else:
                print('now quit')
                self.sc.close()
                break



if __name__ == '__main__':
    run = Server()
    run