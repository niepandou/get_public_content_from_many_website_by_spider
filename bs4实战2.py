import requests
from bs4 import BeautifulSoup

def get_html(url):
    header = {
        "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0",
        "Cookie": "fvlid=1714739872526hed9JXKl1Z; sessionip=113.128.199.194; sessionid=890980F7-69C1-488E-8746-E5553942EFA9%7C%7C2024-05-03+20%3A37%3A54.895%7C%7Ccn.bing.com; autoid=13ee44087ff71c4cec8c1a2773c908fc; sessionvid=066D836C-FCA0-42FC-9771-BE7B4164C156; area=370114; sessionuid=890980F7-69C1-488E-8746-E5553942EFA9%7C%7C2024-05-03+20%3A37%3A54.895%7C%7Ccn.bing.com; __ah_uuid_ng=c_890980F7-69C1-488E-8746-E5553942EFA9; ahpvno=3; v_no=3; visit_info_ad=890980F7-69C1-488E-8746-E5553942EFA9||066D836C-FCA0-42FC-9771-BE7B4164C156||-1||-1||3; ref=cn.bing.com%7C0%7C0%7C0%7C2024-05-03+20%3A40%3A26.889%7C2024-05-03+20%3A37%3A54.895"
    }

    response = requests.get(url,headers=header)
    return response.content

infos = []
for i in range(1,6):
    print("正在爬取第{}页...".format(i))
    url = 'https://www.autohome.com.cn/news/{}/#liststart'.format(i)
    html = get_html(url).decode('GBK')

    content = BeautifulSoup(html,'lxml')
    ul = content.find('ul',attrs={'class': 'article'})

    all_li = ul.find_all('li')
    for li in all_li:
        h3 = li.find('h3')
        span = li.find('span')
        p = li.find('p')

        if ((h3) and (span) and (p)):
            info = {
                "title": h3.text,
                "time": span.text,
                "text": p.text
            }

            infos.append(info)

for info in infos:
    print("标题 " + info["title"])
    print("时间 " + info["time"])
    print("内容 " + info["text"])
    print("---------------------------")