import requests
from lxml import etree
from time import time
def get_html(url):
    header = {
        "user-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0"
    }
    response = requests.get(url,headers=header)
    return response.text

start = time()
print(start)
pages = []
inner_url = []
#得到每一页的链接
for i in range(0,5,1):
    i = i * 20
    url = "https://movie.douban.com/review/best/?start={}".format(i)#用format替换{}
    pages.append(url)
#得到每一页下的每一个影评链接
for page in pages:
    html = get_html(page)
    content = etree.HTML(html)
    all_a = content.xpath('//a[@class="subject-img"]/@href')
    for a in all_a:
        inner_url.append(a)

#对每个影评操作,在之前进行utf8仅用于调试,没必要,在此刻需要得到结果在转不迟
movies = []
i = 1
for url in inner_url:
    html = get_html(url)
    content = etree.HTML(html)
    #print(etree.tostring(content,encoding='utf8').decode())

    #电影名
    name = content.xpath('//div[@id="content"]/h1/span[1]/text()')
    #电影时间
    movie_time = content.xpath('//div[@id="content"]/h1/span[2]/text()')

    #获得剧情简介
    tmp_content = content.xpath('//span[@property="v:summary"]/text()')[0]
    short_content = ""
    for word in tmp_content.split(' '):
        short_content += word

    #得到评论人和评分
    comment_item = content.xpath('//div[@id="hot-comments"]/div[@class="comment-item "]')
    commenter = []
    rank = []
    for item in comment_item:
        tmp_commenter = item.xpath('.//span[@class="comment-info"]/a/text()')
        tmp_rank = item.xpath('.//span[@class="comment-info"]/span[2]/@title')
        commenter.append(tmp_commenter[0])
        rank.append(tmp_rank[0])

    #集合数据
    movie = {
        "title":name,
        "time":movie_time,
        "short-content":short_content,
        "commenter":commenter,
        "rank":rank
    }
    movies.append(movie)
    print("已爬取第{}条电影".format(i))
    i = i + 1

for movie in movies:
    title = movie["title"]
    movie_time = movie["time"]
    short_content = movie["short-content"]
    commenter = movie["commenter"]
    rank = movie["rank"]

    #打印所有结果
    print("电影名: " + title[0])
    print("上映时间: " + movie_time[0] + '\n')
    print("内容简介: " + short_content)
    print("短评信息:")
    for i in range(len(commenter)):
        print("评论人: " + commenter[i] + ", 评分: " + rank[i])
    print("-------分割线-------")

end = time()
print(start)
print(end)
print((end - start) / 60)

