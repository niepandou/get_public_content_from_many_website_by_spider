import re
import requests

# 爬取微博热搜

def get_html(url):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
        'Cookie': 'UOR=cn.bing.com,s.weibo.com,cn.bing.com; SINAGLOBAL=5695946124689.933.1714737520463; login_sid_t=f8da769deae97927de6f37661396f7f0; cross_origin_proto=SSL; XSRF-TOKEN=HgwntpmflOMSCxfNvuaBJoea; _s_tentry=cn.bing.com; Apache=9752368286029.688.1716557543110; ULV=1716557543112:2:2:1:9752368286029.688.1716557543110:1714737520473; wb_view_log=1707*9601.3499999046325684; PC_TOKEN=8c3d1bb049; SUB=_2A25LVOksDeRhGeFI6VAQ9yzEzD2IHXVoKGTkrDV8PUNbmtANLRnjkW9NfVB42GnoDBOTONtFQ6GioFVJDhci1nrM; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFNhEBMkFSvs5GUjyhJUAmq5JpX5KzhUgL.FoMceozpS0zRS022dJLoIp.LxKBLBonL12BLxKMLBK5LBox-wPWQdcvV; ALF=02_1719150204; WBPSESS=bkbRYFu8uQjz_ghrfg9fvGhWoDGIDtNeeX_qNcIZNBgOIJC8YrvWPLWlz4lK8SheCW7ctDGOuMsVg81d7YQSTQj__qciJ4YNTRYkDiqhB3v509Gvx81pHbzoqC2JoXaBcQ2PwqWZ4A3YCzLeANrtaw==',
    }
    response = requests.get(url,headers=header)
    return response.content
url = 'https://s.weibo.com/top/summary'
content = get_html(url).decode('utf8')

text = re.findall('<td class="td-02">([\\d\\D]*?)</td>',content)

for intext in text:
    title = re.search('<a.*?>(.*?)</a>',intext)
    num = re.search('<span>(.*?)</span>',intext)
    print('标题: ',title.group(1))
    #特判一下置顶热搜(无热度)
    if num:
        print('热度:',num.group(1))
    else:
        print('热度: 置顶')
# print(content)