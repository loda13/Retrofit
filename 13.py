"""
Author: TangYue
"""
'''
题目：（代码上传到文档云，链接在I讯飞群里，命名方式：姓名+域账号+工号）
定义一个父类，父类包含两个参数(param1,param2)，三个子类继承这个父类。要求：
1) 在三个子类中，修改param1的值，同时影响到其他两个子类中param1的值
2) 在三个子类中，修改param2的值，不影响其他两个子类param2的值
3) 使用python3编写代码，程序必须完整且可运行，并且直接在控制台输出明确结果(不要设置交互)
'''
class Father:
    param1 = 1
    param2 = 2

    def __init__(self, param1, param2):
        self.param1 = int(param1)
        self.param2 = int(param2)


class Son1(Father):
    def __init__(self):
        param1 = Son2.param1 + Son3.param1
        param2 = self.param2
        print(f'param1: {param1},param2:{param2}')


class Son2(Father):
    def __init__(self):
        param1 = Son1.param1 + Son3.param1
        param2 = self.param2
        print(f'param1: {param1},param2:{param2}')


class Son3(Father):
    def __init__(self):
        param1 = Son1.param1 + Son2.param1
        param2 = self.param2
        print(f'param1: {param1},param2:{param2}')


if __name__ == '__main__':
    father = Father(1, 2)
    print('初始father的param1=1，son的param1=2，param2=2')
    print('打印son123的param1,param2:')
    son1 = Son1()
    son2 = Son2()
    son3 = Son3()

    print('修改param1=2')
    father2 = Father(2, 2)
    print('打印son123的param1,param2:')
    son4 = Son1()
    son5 = Son2()
    son6 = Son3()

    input("Press <enter>")
