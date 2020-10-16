# 题目：（代码上传到文档云，链接在I讯飞群里，命名方式：姓名+域账号+工号）
# 现在有一个json:
# {'city':'合肥','area':'蜀山','street':'望江西路','name':'科大讯飞','detail':{'Buildings':[{'A1':{'floor':[{'f1':'大厅'}]}},{'A2':{'floor':[{'f2':'餐厅'}]}},{'A4':{'floor':[{'f1':'小吃'},{'f2':'餐厅'}]}},{'A3':{}},{'A5':{'floor':[]}}],'Parkings':['p1','p2','p3']}}
# 请将此json的所有路径依次输出(每条路径都走到最里层)，例如：
# city:合肥
# area:蜀山
# detail:Buildings:@list0@:A1:floor:@list0@:f1:大厅
# ......
# 注意：list的顺序也要在路径中表示出来
# Author: TangYue

import json

str = {'city': '合肥',
       'area': '蜀山',
       'street': '望江西路',
       'name': '科大讯飞',
       'detail': {
           'Buildings': [{'A1': {'floor': [{'f1': '大厅'}]}}, {'A2': {'floor': [{
               'f2': '餐厅'}]}}, {'A4': {'floor': [{'f1': '小吃'}, {'f2': '餐厅'}]}},
                         {'A3': {}}, {'A5': {'floor': []}}],
           'Parkings': ['p1', 'p2', 'p3']}}
d = json.dumps(str)
l = json.loads(d)
print(d)
print(l)
# print(l['city'])
for i in l:
    print(l[i])
j = l['detail']
for i in j:
    print(i)
    k = i
    print(j[i])

    for i in j[k]:
        print(i)
        # print(j[k][i])

input("Press <enter>")
