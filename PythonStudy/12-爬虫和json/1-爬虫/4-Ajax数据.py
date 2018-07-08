
import urllib.request
import ssl
import json

def ajaxCrawler(url):

    req = urllib.request.Request(url)

    # 使用ssl创建未验证的上下文
    content = ssl._create_unverified_context()
    response = urllib.request.urlopen(req, context=content)

    jsonStr = response.read().decode('utf-8')
    jsonData = json.loads(jsonStr)

    return jsonData



url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=20&limit=20"
info = ajaxCrawler(url)
print(len(info))


print('---------上拉加载------')

for i in (1, 10):
    url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=" + str(i * 20) + "&limit=20"
    info1 = ajaxCrawler(url)
    print(len(info1))