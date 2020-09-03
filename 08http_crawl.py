# 获取https://www.w3school.com.cn/导航，以及每个导航下左边的课程表和右边的侧边栏 \
# (包括工具栏箱和赞助商图片)，结果保存到一个json中，并格式化打印。
# Author: TangYue

import requests
from bs4 import BeautifulSoup
import json
import re


class W3school:
    pass

    def __init__(self):
        self.url = 'https://www.w3school.com.cn'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/84.0.4147.89 Safari/537.36 '
        }

    def _soup(self, url):
        r = requests.get(url, headers=self.headers)
        r.encoding = 'GBK'
        soup = BeautifulSoup(r.text, "lxml")
        return soup

    def _build(self):
        wrap = {}
        name = []
        soup = self._soup(self.urls)
        course = soup.select("#course")
        for i in course[0].find_all("a"):
            name.append(i.string)
        wrap["课程表"] = name
        tools = soup.select("#tools")

        if len(tools) > 0:
            Tool = {}
            for i in tools[0].find_all("h2"):
                tool = []
                name = i.string
                j = i.find_next_siblings("ul")
                for k in j[0].find_all("li"):
                    tool.append(k.string)
                Tool[name] = tool
            wrap["工具箱"] = Tool
        sidebars = soup.select("#sp_sidebar")

        if len(sidebars) > 0:
            sidebar = {}
            for k in sidebars[0].find_all("a"):
                sidebar['图片跳转链接地址'] = k["href"]
            wrap["赞助商连接"] = sidebar
        return wrap

    def run(self):
        wrap = {}
        soup = self._soup(self.url)
        menu = soup.select("#menu")
        for i in menu[0].find_all("a"):
            name = i.string
            self.urls = self.url + i["href"]
            info = self._build()
            wrap[name] = info

        wrap = json.dumps(wrap, ensure_ascii=False, sort_keys=False, indent=4,
                          separators=(',', ': '))
        f = open('structure.json', "w", encoding="utf-8")
        f.write(str(wrap))
        f.close()


if __name__ == "__main__":
    f = W3school()
    f.run()
