# 金额转换程序
# 输入一个字符串，可以自动转换为金额格式输出(人民币)
# 可以将人民币按照汇率转换成其他货币，例如美金、英镑等
# 可以设置汇率
# 可以实现非人民币货币的互相转换，例如xx美金=xx英镑
# 按天设置汇率(7天)，预测从当天开始到一周后人民币兑换外汇的收益(注意区间在7天内可以随意更改) ，显示格式不限
# 要求
# 使用面向对象式编程
# 一个父类和两个或多个子类，父类中包含一些基本信息，子类包含金额转换方法
# Author: TangYue

class Transformation(object):
    """所有金额基类"""

    num = 0
    company = 0
    yields = 0
    wealth = 0

    def __init__(self, num, company, yields, wealth):
        # self.result = result
        # self.convert = convert
        self.num = float(num)
        self.company = float(company)
        self.yields = yields
        self.wealth = float(wealth)
        # self.num = num
        # self.company = company
        # self.result= self.num * self.company
        # self.convert = format(self.num, ',')

    def count(self):
        self.wealth = self.num * self.company

    def result(self):
        self.count()
        print(self.wealth)

    def convert(self, symbols_):
        print("结果：" + symbols_ + str(format(self.num, ',')))

    def diy(self):
        # print("自定义汇率：" + '£' + str(self.wealth))
        self.result()

    def exchange(self):
        print('$' + str(self.convert()))
        # self.num = self.num * 0.89
        # self.convert = format(self.num, ',')
        print("美元转欧元汇率0.89,转换后：" + '£' + str(self.result()))

    def earnings(self):
        global i
        self.yields = self.yields.split(",")
        # print(self.yields)
        # self.wealth = self.yields[0] * int(self.num)
        # self.num = int(self.num)
        for i in range(0, 7):
            # print(i)
            # print(self.num)
            # print(self.yields[i])
            self.wealth = self.num * float(self.yields[i]) + self.wealth
        print("七天后收益：" + str(self.wealth - self.num * 7))


class smalldollars(Transformation):
    """子类美元"""

    def pounds(self):
        self.company = 0.89
        self.result()
        self.num = self.wealth
        self.convert('£')
        # print("美元：" + '$' + self.convert)


class smallrmb(Transformation):
    """子类欧元"""

    def dollars(self):
        self.company = 0.14
        self.result()
        self.num = self.wealth
        self.convert('$')

    def pounds(self):
        self.company = 0.13
        self.result()
        self.num = self.wealth
        self.convert('£')


# print("人民币：" + '￥' + self.convert)


class smallpounds(Transformation):
    """子类欧元"""

    def rmb(self):
        self.company = 7.93
        self.result()
        self.num = self.wealth
        self.convert('￥')


print("目前支持转换："
      "1、数字转人民币"
      "2、人民币转美元"
      "3、人民币转欧元"
      "4、自定义汇率转换"
      "5、美元转欧元"
      "6、欧元转人民币"
      "7、按天设置汇率，并计算收益")
option = int(input("请输入你的选择："))
if option == 1:
    test1 = Transformation(input("请输入金额："), 0, 0, 0)
    test1.convert('￥')
elif option == 2:
    test1 = smallrmb(input("请输入金额："), 0, 0, 0)
    test1.dollars()
elif option == 3:
    test1 = smallrmb(input("请输入金额："), 0, 0, 0)
    print(test1.pounds())
elif option == 4:
    test1 = Transformation(input("请输入金额："), input("请输入汇率："), 0, 0)
    test1.result()
elif option == 5:
    test1 = smalldollars(input("请输入金额："), 0, 0, 0)
    test1.pounds()
elif option == 6:
    test1 = smallpounds(input("请输入金额："), 0, 0, 0)
    test1.rmb()
elif option == 7:
    test1 = Transformation(input("请输入本金："), 0, input("请输入7天汇率，用‘，’隔开："), 0)
    print(test1.earnings())
else:
    print("您的输入有误，程序结束")

# test1 = Transformation(input("请输入金额："), input("请输入汇率："))
# print(test1.rmb())
# print(test1.dollars())
# print(test1.pounds())
# print(test1.diy())
# print(test1.exchange())

# test1 = Transformation(100, 0, '1,1,1,1,2,2,2', 0)
# print(test1.earnings())

# test1 = Transformation(input("请输入金额："), 0, 0, 0)
# test1.convert('￥')
# test1 = smallrmb(input("请输入金额："), 0, 0, 0)
# test1.dollars()
# test1 = Transformation(input("请输入金额："), input("请输入汇率："), 0, 0)
# test1.result()
# test1 = smalldollars(input("请输入金额："), 0, 0, 0)
# test1.pounds()
# test1 = smallpounds(input("请输入金额："), 0, 0, 0)
# test1.rmb()
# exit()
input("Press <enter>")
