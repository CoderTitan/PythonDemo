
import urllib.request
import ssl
import re

def jockCrawler(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36"
    }
    reqe = urllib.request.Request(url, headers=headers)
    content = ssl._create_unverified_context()
    response = urllib.request.urlopen(reqe, context=content)

    HTML = response.read().decode('utf-8')


    pat = r'<div class="author clearfix">(.*?)<span class="stats-vote"><i class="number">'
    reJock = re.compile(pat, re.S)
    divList = reJock.findall(HTML)

    # print(divList)

    dic = {}
    for div in divList:
        # 用户名
        name = re.compile(r"<h2>(.*?)</h2>", re.S)
        username = name.findall(div)
        username1 = username[0]

        # 段子
        data = re.compile(r'<div class="content">\n<span>(.*?)</span>', re.S)
        duanzi = data.findall(div)
        duanzi1 = duanzi[0]

        dic[username1] = duanzi1

    return dic



url = "https://www.qiushibaike.com/text/page/1/"
info = jockCrawler(url)

for k, v in info.items():
    print(k + '说: ' + v + '\n\n')

