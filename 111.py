#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'ylxiao'

import requests
from bs4 import BeautifulSoup
import json
import re
import os

'''
【朴实无华的作业】
1、获取https://www.w3school.com.cn/导航
2、以及每个导航下左边的课程表和右边的侧边栏(包括工具栏箱和赞助商图片)，
3、结果保存到一个json中，并格式化打印。
'''

class REQ():
    def __init__(self):
        # 定义变量
        self.url = 'https://www.w3school.com.cn'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Mobile Safari/537.36'
        }
        self.savepath = BASE_DIR + "\\ret.json"

    def run(self):
        ret = {}
        soup = self.req(self.url)

        # 获取css文件路径
        pic_css = soup.find('link')
        self.css = self.url + pic_css["href"]

        # 获取导航
        navigation = soup.select("#navfirst")

        # 解析导航
        for i in navigation[0].find_all("a"):
            # 获取导航名称
            name = i.string

            # 获取对应导航链接
            url = self.url + i["href"]
            #ret[name] = url
            #print(url)

            # 获取对应导航下课程、工具与图片信息
            info = self.parse(url)
            ret[name] = info

        ret = json.dumps(ret, ensure_ascii=False, indent=4)
        print(ret)
        print("开始将结果保存文件中：")
        f = open(self.savepath, "w", encoding="utf-8")
        f.write(str(ret))
        f.close()
        print("写入文件完成。文件为：%s"%(self.savepath))

    # 功能方法
    def req(self, url):
        try:
            r = requests.get(url, headers=self.headers)
            r.encoding = 'GBK'
            #print(r.encoding)

            if r.status_code == 200:
                #print("请求成功。")
                soup = BeautifulSoup(r.text, "lxml")
                return soup
            else:
                print("请求失败。")
        except Exception as e:
            print(e)

    def parse(self, url):
        ret = {}
        name = []
        soup = self.req(url)
        # 解析课程表
        courses = soup.select("div #navsecond")
        for i in courses[0].find_all("a"):
            # 获取课程名称
            name.append(i.string)
        ret["course"] = name

        # 解析工具栏箱
        tools = soup.select("div #tools")
        if len(tools) > 0:
            Tool = {}
            # 工具名
            for i in tools[0].find_all("h2"):
                tool = []
                #print("i:%s"%(i))
                name = i.string
                #print("工具栏：%s"%(name))
                #for j in i.find_next_siblings("ul"):
                j = i.find_next_siblings("ul")

                #print("j:%s"%(j))
                # 工具名
                for k in j[0].find_all("li"):
                    #print("k:%s"%(k))
                    #print(k.string)
                    tool.append(k.string)
                #print(tool)
                Tool[name] = tool
            ret["tool"] = Tool

        # 解析赞助商图片
        sidebars = soup.select("div #sp_sidebar")

        if len(sidebars) > 0:
            # 赞助商图片
            sidebar = {}
            for k in sidebars[0].find_all("a"):
                # 图片跳转链接地址
                sidebar['图片跳转链接地址'] = k["href"]
                # 图片下载地址
                path = self.search()
                pic_url = self.url + path[0]
                sidebar['图片下载地址'] = pic_url
            ret["sidebar"] = sidebar
        return ret

    def search(self):
        pic_info = self.req(self.css)
        data = pic_info.select("p")
        pat1 = re.compile("div#sps_1 a#sps_1_link" + '(.*?)' + '}', re.S)
        data1 = pat1.findall(str(data))
        pat2 = re.compile("transparent url\(\"" + '(.*?)' + '\"\)', re.S)
        path = pat2.findall(str(data1[0]))
        return path

if __name__ == "__main__":
    try:
        # 获取当前路径
        BASE_DIR = os.getcwd()

        # 爬取并解析
        f = REQ()
        f.run()
        os.system("pause")
    except Exception as e:
        print(e)