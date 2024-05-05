import requests
from bs4 import BeautifulSoup

def get_html(url):
    header = {
        'User-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0",
        'Cookie': "SUB=_2AkMRaF5ff8NxqwFRmfsUxW_iZYt_wgzEieKnNK-EJRMxHRl-yT8XqmdZtRB6OuhwsEUDHv3UmOx9Q7NdGxdansTbadkw; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WhNa-NAiNbr7Es7yzju1Hgf; _s_tentry=cn.bing.com; UOR=cn.bing.com,s.weibo.com,cn.bing.com; Apache=5695946124689.933.1714737520463; SINAGLOBAL=5695946124689.933.1714737520463; ULV=1714737520473:1:1:1:5695946124689.933.1714737520463:"
    }
    response = requests.get(url,headers=header)
    return response.text

url = 'https://s.weibo.com/top/summary'
html = get_html(url)
content = BeautifulSoup(html,'lxml')

all_td = content.find_all('td',attrs={'class': "td-02"})

for td in all_td:
    a = td.find('a')
    span = td.find('span')

    print(a.text,end=" ")

    print("分类及热度:",end=" ")
    if span: print(span.string)
    else: print("上升中")