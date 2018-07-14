

import urllib.request
import re
import os

def imageCache(url, toPath):

    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    htmlStr = response.read()

    # path = r"/Users/quanjunt/Documents/Quanjun/GitHub/PythonDemo/PythonStudy/12-爬虫和json/File/picture.html"
    # with open(path, 'wb') as file:
    #     file.write(htmlStr)


    pat = r'<img style="width:230px;height:322px" src="//(.*?)"/>'

    reImage = re.compile(pat, re.S)
    imageList = reImage.findall(htmlStr)
    num = 1
    for imaUrl in imageList:
        path = os.path.join(toPath, str(num)+ ".jpg")
        num += 1

        # 图片下载到本地存储
        urllib.request.urlretrieve("http://" + imaUrl, filename=path)



url = "http://list.yhd.com/c28115-0-90896/?tc=0.0.16.CatMenu_Search_100000040_154700.128&tp=1.1.3433.7.2.LrEpYl6-10-9JhO4&ti=TG6299"
# url = "http://www.baidu.com"
topath = r"/Users/quanjunt/Documents/Quanjun/GitHub/PythonDemo/PythonStudy/12-爬虫和json/image"

imageCache(url, topath)


