# 获取https://www.w3school.com.cn/导航，以及每个导航下左边的课程表和右边的侧边栏 \
# (包括工具栏箱和赞助商图片)，结果保存到一个json中，并格式化打印。
# Author: TangYue

from bs4 import BeautifulSoup
import urllib.request
import json


class Job:
    pass

    def __init__(self):
        self.url = 'https://www.w3school.com.cn'
        self.page = urllib.request.urlopen(self.url)
        self.soup = BeautifulSoup(self.page, 'html.parser')
        self.d = {}

    def menu(self):
        label = self.soup.select("#menu")
        for a in label[0].find_all("a"):
            menu = a.string
            i = self.url + a["href"]
            self.d[menu] = i

    def course(self):
        for j in self.d.keys():
            k = self.d[j]
            self.url = k
            self.page = urllib.request.urlopen(self.url)
            self.soup = BeautifulSoup(self.page, 'html.parser')
            label = self.soup.select("#course")
            for l in label[0].find_all("a"):
                course = l.string
                print(course)

    def tools(self):
        for j in self.d.keys():
            k = self.d[j]
            self.url = k
            self.page = urllib.request.urlopen(self.url)
            self.soup = BeautifulSoup(self.page, 'html.parser')
            label = self.soup.select("#tools")
            for l in label[0].find_all("a"):
                tools = l.string
                print(tools)

    def sp_sidebar(self):
        for j in self.d.keys():
            k = self.d[j]
            self.url = k
            self.page = urllib.request.urlopen(self.url)
            self.soup = BeautifulSoup(self.page, 'html.parser')
            label = self.soup.select("#sp_sidebar")
            for l in label[0].find_all("a"):
                sp_sidebar = l["href"]
                print(sp_sidebar)

if __name__ == '__main__':
    test = Job()
    test.menu()
    test.course()
    test.tools()
    test.sp_sidebar()
