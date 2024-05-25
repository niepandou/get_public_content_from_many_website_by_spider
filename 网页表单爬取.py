import requests


def get_html(url):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0"
    }
    response = requests.get(url, headers=header)
    return response.text


url = "http://spiderbuf.cn/n06"
html = get_html(url)

print(html)
