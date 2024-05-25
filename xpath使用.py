from lxml import etree
import requests

def get_html(url):
    response = requests.get(url)
    return response.text

url = 'https://www.acwing.com/activity/'
html = get_html(url)

content = etree.HTML(html)

#获取所有的div标签
# all_div = content.xpath("//div")
# for div in all_div:
#     print(etree.tostring(div,encoding='utf8').decode('utf8'))

#获取指定的div标签
# all_div = content.xpath('//div[@class="activity-index-block"]')
# for div in all_div:
#     print(etree.tostring(div,encoding='utf8').decode('utf8'))

#获取div中所有的课程标题
#只需获取找到的div中的第一个span即是我要找的
all_div = content.xpath('//div[@class="col-xs-8 col-sm-8"]')
for div in all_div:
    span = div.xpath('./span/text()')[0]
    print(span)

