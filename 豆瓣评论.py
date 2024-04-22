import requests
from bs4 import BeautifulSoup

def get_html(url):
    header = {
        "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0'
    }
    response = requests.get(url,headers=header)
    #print(response)
    return response.text
def get_userName(comment):
    comment_info = comment.find("span",class_="comment-info")
    user_name = comment_info.find("a").text
    return user_name
def get_userComment(comment):
    comment_content = comment.find("p",class_="comment-content")
    user_comment = comment_content.find("span",class_="short").text
    return user_comment

url = 'https://movie.douban.com/subject/26925611/comments?sort=new_score&status=P'
html = get_html(url)
soup = BeautifulSoup(html,"html.parser")

#进入comment标签,该标签是保存每个用户信息和评论的标签
all_comment = soup.find_all("div",class_="comment")

#我们仅需得到用户名和其评论内容即可
for comment in all_comment:
    #用户标签在comment-info里面的a标签中
    user_name = get_userName(comment)
    user_comment = get_userComment(comment)
    #因为有的评论里面可能包含了换行符,所以需要特殊处理comment
    print(user_name + ":",end="")
    for content in user_comment:
        print(content,end="")
    print()
