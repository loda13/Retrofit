"""
Author: TangYue
"""
'''
学生成绩单程序
成绩录入（多学科）
成绩修改
成绩查询
按学号/姓名查询
班级最高分
班级平均分
学科最高分
学科平均分
学科及格率
要求
使用面向对象式编程
使用MySQL数据库
'''
import pymysql


class Score:
    pass

    def __init__(self):
        self.db = pymysql.connect(
            host='xxxx',
            port=3306,
            user='root',
            passwd='xxxx',
            db='croak',
            charset='utf8',
            autocommit=True)
        self.cur = self.db.cursor()
        self.cursor = self.db.cursor()
        self.cursor.execute("DROP TABLE IF EXISTS Stuscore")
        self.cur.execute("use croak;")
        # 建表
        self.cur.execute("create table Stuscore("
                         "name char(20),"
                         "num int(20),"
                         "chinese char(20),"
                         "english char(20),"
                         "math char(20),"
                         "total char(20)) character set utf8;")

    def appendStudentInfo(self):
        self.db = pymysql.connect(host='xxxx', port=3306, user='root',
                                  passwd='xxxx', db='croak',
                                  charset='utf8', autocommit=True)
        self.cursor = self.db.cursor()  # 利用db方法创建游标对象
        name = input("请输入学生姓名：")
        num = input("请输入学生学号：")
        chinese = input("请输入语文成绩：")
        math = input("请输入数学成绩：")
        english = input("请输入英语成绩：")
        total = int(chinese) + int(math) + int(english)
        sql = """INSERT INTO Stuscore(NAME,NUM,CHINESE,ENGLISH,MATH,
        TOTAL)VALUES (%s,%s,%s,%s,%s,%s)"""
        try:
            self.cursor.execute(sql, (name, num, chinese, english, math, total))
            self.cur.execute("use croak;")
            self.db.commit()
        except:
            self.db.rollback()
        self.db.close()

    def delstudentname(self, delstudentname):
        self.db = pymysql.connect(host='xxxx', port=3306, user='root',
                                  passwd='xxxx', db='croak',
                                  charset='utf8', autocommit=True)
        self.cursor = self.db.cursor()  # 利用db方法创建游标对象
        sql = "DELETE FROM Stuscore WHERE Name='" + delstudentname + "'"

        try:
            self.cursor.execute(sql)
            self.cur.execute("use croak;")
            self.db.commit()
        except:
            self.db.rollback()
        self.db.close()
        print("删除成功")

    def delstudentnum(self, delstudentnum):
        self.db = pymysql.connect(host='xxxx', port=3306, user='root',
                                  passwd='xxxx', db='croak',
                                  charset='utf8', autocommit=True)
        self.cursor = self.db.cursor()  # 利用db方法创建游标对象
        sql = "DELETE FROM Stuscore WHERE NUM='" + delstudentnum + "'"
        querysql = 'select * from Stuscore where NUM="%s"' % delstudentnum
        try:
            self.cursor.execute(sql)
            self.cur.execute("use croak;")
            self.db.commit()
        except:
            self.db.rollback()
        result = self.cursor.execute(querysql)
        print(result)
        self.cur.execute("use croak;")
        if result:
            print("删除失败")
        print("删除成功")

    def querystudentname(self, studentname):
        self.db = pymysql.connect(host='xxxx', port=3306, user='root',
                                  passwd='xxxx', db='croak',
                                  charset='utf8', autocommit=True)
        self.cursor = self.db.cursor()  # 利用db方法创建游标对象

        sql = 'select * from Stuscore where NAME="%s"' % studentname
        try:
            self.cursor.execute(sql)
            self.cur.execute("use croak;")
            results = self.cursor.fetchall()
            print("NAME=%s,NUM=%s,CHINESE=%s,ENGLISH=%s,MATH=%s,TOTAL=%s" % \
                  (results[0][0], results[0][1], results[0][2], results[0][3],
                   results[0][4], results[0][4]))
            return True
        except:
            self.db.rollback()

    def querystudentnum(self, studentnum):
        self.db = pymysql.connect(host='xxxx', port=3306, user='root',
                                  passwd='xxxx', db='croak',
                                  charset='utf8', autocommit=True)
        self.cursor = self.db.cursor()  # 利用db方法创建游标对象

        sql = 'select * from Stuscore where NUM="%s"' % studentnum
        try:
            self.cursor.execute(sql)
            self.cur.execute("use croak;")
            results = self.cursor.fetchall()
            print("NAME=%s,NUM=%s,CHINESE=%s,ENGLISH=%s,MATH=%s,TOTAL=%s" % \
                  (results[0][0], results[0][1], results[0][2], results[0][3],
                   results[0][4], results[0][4]))
            return True
        except:
            self.db.rollback()

    def modifystudentifo(self, Nname, Nchinese, Nenglish, Nmath):
        total = int(Nchinese) + int(Nmath) + int(Nenglish)
        Ntotal = str(total)
        self.db = pymysql.connect(host='xxxx', port=3306, user='root',
                                  passwd='xxxx', db='croak',
                                  charset='utf8', autocommit=True)
        self.cursor = self.db.cursor()  # 利用db方法创建游标对象

        sql = "UPDATE Stuscore SET MATH='%s',CHINESE='%s',ENGLISH='%s',TOTAL='%s' WHERE NAME = '%s'" % (
            Nmath, Nchinese, Nenglish, Ntotal, Nname)

        try:
            self.cursor.execute(sql)
            self.cur.execute("use croak;")
            self.db.commit()
        except:
            self.db.rollback()
            self.db.close()

    def modifystudentifonum(self, Nnum, Nchinese, Nenglish, Nmath):
        total = int(Nchinese) + int(Nmath) + int(Nenglish)
        Ntotal = str(total)
        self.db = pymysql.connect(host='xxxx', port=3306, user='root',
                                  passwd='xxxx', db='croak',
                                  charset='utf8', autocommit=True)
        self.cursor = self.db.cursor()  # 利用db方法创建游标对象

        sql = "UPDATE Stuscore SET MATH='%s',CHINESE='%s',ENGLISH='%s',TOTAL='%s' WHERE NAME = '%s'" % (
            Nmath, Nchinese, Nenglish, Ntotal, Nnum)

        try:
            self.cursor.execute(sql)
            self.cur.execute("use croak;")
            self.db.commit()
        except:
            self.db.rollback()
            self.db.close()

    def allinfo(self):
        self.db = pymysql.connect(host='xxxx', port=3306, user='root',
                                  passwd='xxxx', db='croak',
                                  charset='utf8', autocommit=True)
        self.cursor = self.db.cursor()  # 利用db方法创建游标对象
        sql = "select * from Stuscore"
        self.cursor.execute(sql)
        self.cur.execute("use croak;")
        results = self.cursor.fetchall()
        # print(results)
        dict_num = {}
        i = 0
        print("偏科的有：")
        for row in results:
            NAME = row[0]
            NUM = row[1]
            CHINESE = int(row[2])
            ENGLISH = int(row[3])
            MATH = int(row[4])
            AVE = int(row[5]) / 3
            dict_num[i] = int(row[5])
            i = i + 1
            if abs(int(CHINESE - ENGLISH)) > 20 or abs(
                    int(CHINESE - MATH)) > 20 or abs(int(ENGLISH - MATH)) > 20:
                print("NAME=%s,CHINESE=%s,ENGLISH=%s,MATH=%s,AVE=%s" % (
                    NAME, CHINESE, ENGLISH, MATH, AVE))
        d1 = sorted(dict_num.items(), key=lambda dict_num: dict_num[1],
                    reverse=False)
        print("排序：")
        for row in d1:
            name = results[int(row[0])][0]
            num = int(results[int(row[0])][1])
            chinese = int(results[int(row[0])][2])
            english = int(results[int(row[0])][3])
            math = int(results[int(row[0])][4])
            total = int(results[int(row[0])][5])

            print("NAME=%s,NUM=%s,CHINESE=%s,ENGLISH=%s,MATH=%s,TOTAL=%s" % (
                name, num, chinese, english, math, total))

    def studentMenu(self):
        print("=" * 30)
        print("学生管理系统")
        print("1、添加学生信息")
        print("2、删除学生信息")
        print("3、查询学生信息")
        print("4、修改学生信息")
        print("5、全部学生信息")
        print("6、退出")
        print("=" * 30)


if __name__ == '__main__':
    test = Score()
    while True:
        test.studentMenu()
        menuindex = input("请输入选项序号：")
        while not menuindex.isdigit():
            menuindex = input("输入错误，请重新输入：")
        if int(menuindex) == 1:
            test.appendStudentInfo()
        elif int(menuindex) == 2:
            print("1、输入学生姓名")
            print("2、输入学生学号")
            menuindexson = input("请输入选项序号：")

            if int(menuindexson) == 1:
                delstudentname = input("请输入要删除的学生姓名：")
                test.delstudentname(delstudentname)
            elif int(menuindexson) == 2:
                delstudentnum = input("请输入要删除的学生学号：")
                test.delstudentnum(delstudentnum)
        elif int(menuindex) == 3:
            print("1、输入学生姓名")
            print("2、输入学生学号")
            menuindexson = input("请输入选项序号：")

            if int(menuindexson) == 1:
                studentname = input("请输入要查询的学生名字：")
                test.querystudentname(studentname)
            elif int(menuindexson) == 2:
                studentnum = input("请输入要查询的学生学号：")
                test.querystudentnum(studentnum)
        elif int(menuindex) == 4:
            print("1、输入学生姓名")
            print("2、输入学生学号")
            menuindexson = input("请输入选项序号：")

            if int(menuindexson) == 1:
                Nname = input("要修改成绩的学生姓名：")
                Nchinese = input("请重新输入语文成绩：")
                Nmath = input("请重新输入数学成绩：")
                Nenglish = input("请重新输入英语成绩：")
                test.modifystudentifo(Nname, Nchinese, Nenglish, Nmath)
            elif int(menuindexson) == 2:
                Nnum = input("要修改成绩的学生学号：")
                Nchinese = input("请重新输入语文成绩：")
                Nmath = input("请重新输入数学成绩：")
                Nenglish = input("请重新输入英语成绩：")
                test.modifystudentifonum(Nnum, Nchinese, Nenglish, Nmath)
        elif int(menuindex) == 5:
            test.allinfo()
        elif int(menuindex) == 6:
            break
        else:
            print("输入序号无效")
