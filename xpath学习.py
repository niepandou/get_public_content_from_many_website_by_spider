# //xxx 全局搜索标签 //div,也可以认为是当前目录下的全局 所以有了以下操作
# div > div > div > p 我要筛选p,直接用//div//p即可,而不用复杂的写成//div/div/div/p
# /xxx 在当前标签下搜索某标签 //div/a
# @[xxx] 选取某个带属性的标签 //div[@class="xxx"]
# [x] 选取取得的第几个元素 下标从1开始  //div[1]
# [last()]最后一个标签,[position()<3]前两个标签
# [@*]选择所有拥有属性的节点
# . 当前节点下 ./span
# | 来选择路径 //meta | //a 选取meta或a标签
# xxx/@xxx 可以选择某个标签下某个属性的值 span/@title
# 例如<span title="abc"></span> 得到的就是
import os

# . 用例 //span[./text()="aaa"]/following::text()  寻找span路径下其文本等于aaa的之后的所有文本内容
# 例如
# <span>aaa</span>
# abc
# <div>bcd</bcd>
# 得到的就是[abc,bcd]

import requests
from lxml import etree
import sys
text = \
    """
<tr class = "hots">
    <td class = "1">hot1</td>
    <td class = "2">hot2</td>
    <td class = "3">hot3</td>
    <td class = "4">hot4</td>
    <td class = "5">hot5</td>
</tr>
"""
html = etree.HTML(text)
print(etree.tostring(html, encoding="utf8").decode())  # 打印html内容,且以utf8格式提取,用decode解码
# 得到人性化的结果

print("""
-----------------
""")

# parse对html文件导入并解析
#print(os.getcwd())
html = etree.parse('test.html')
result = etree.tostring(html,encoding='utf8').decode('utf8')
print(result)
print("""
-------------------
""")
#设定格式,自定义解析器
parser = etree.HTMLParser(encoding='utf8')
html = etree.parse('test.html',parser=parser)
result = etree.tostring(html,encoding='utf8').decode('utf8')
print(result)

