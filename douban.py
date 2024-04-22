import requests
from bs4 import BeautifulSoup
def get_html(url):
    header = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0'
    }
    response = requests.get(url,headers=header)
    #print(response)
    return response.text

url = 'https://movie.douban.com/chart'
html = get_html(url)
soup = BeautifulSoup(html,'html.parser')
#得到所有带pl2类的div标签
all_div = soup.find_all("div",attrs={"class": "pl2"})

titles = []
#标题内容就在a标签内,介于a标签和他的子标签之间,因为标题不长所以只读取第一行
#或者说,以他翻译的分隔符/作为分割,得到仅国语标题
for div in all_div:
    title = div.find("a").text.strip()
    title = title.split("/")[0].strip()
    titles.append(title)

for title in titles:
    print(title)




