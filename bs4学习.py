import requests
from bs4 import BeautifulSoup
#安装c语言库/lxml库来使用lxml解析器,加快bs4解析速度
#Content = BeautifulSoup(html,'lxml')

def get_html(url):
    header = {
        "User-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0"
    }
    response = requests.get(url,headers=header)
    return response.text

url = 'https://www.douban.com/'
html = get_html(url)

soup = BeautifulSoup(html,'lxml')

#获取所有div
all_div = soup.find_all('div')

# print(type(all_div))
# for div in all_div:#type并非列表,只不过可以识别成列表
#     print(div.text)

#获取指定div
# div = all_div[0]
# print(div)

#获取指定属性的标签,不建议直接选,用attrs既可以单个也可以多个,用单属性选择可能出问题找不到
all_a = soup.find_all("a",attrs={"class":"lnk-app"})

for a in all_a:
    print(a.text)

#获取标签属性值
#通过下标方式提取
for a in all_a:
    href = a['href']
    print(href)
#attrs得到
for a in all_a:
    href = a.attrs['href']
    print(href)

#获取所有的信息
all_a = soup.find_all('a',attrs={'class':'rec_topics_name'})

for a in all_a:
    print(a.string)