

import urllib.request
import os
import re
import ssl
from collections import deque


# path = r"/Users/quanjunt/Documents/Quanjun/GitHub/PythonDemo/PythonStudy/12-爬虫和json/File/file2.html"


# 将网页信息写入文件
def writeFileBytes(htmlByte, toPath):
    with open(toPath, 'wb') as file:
        file.write(htmlByte)


# 将网页爬取的数据信息写如文件
def writeDatatoFile(htmlData, toPath):
    with open(toPath, 'w') as file:
        file.write(htmlData)



# 获取网页信息
def getHTMLInfo(url):

    req = urllib.request.Request(url)
    content = ssl._create_unverified_context()
    response = urllib.request.urlopen(req, context=content)

    return response.read()


# 获取QQ
def getQQNumber(url, toPath):
    htmlByte = getHTMLInfo(url)
    htmlStr = str(htmlByte)

    # 写入文件
    path = r"/Users/quanjunt/Documents/Quanjun/GitHub/PythonDemo/PythonStudy/12-爬虫和json/File/qq1.html"
    writeFileBytes(htmlByte, path)


    pat = r'(((http|ftp|https)://)(([a-zA-Z0-9\._-]+\.[a-zA-Z]{2,6})|([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}))(:[0-9]{1,4})*(/[a-zA-Z0-9\&%_\./-~-]*)?)'
    reUrl = re.compile(pat)
    urlList = reUrl.findall(htmlStr)

    # 去重, 转为list即可
    urlsLists = list(set(urlList))
    pat = r"[1-9]\d{4,9}"
    reQQ = re.compile(pat)
    qqList = reQQ.findall(htmlStr)

    # 去重, 转为list即可
    qqLists = list(set(qqList))
    file = open(toPath, 'a')
    for qqStr in qqLists:
        file.write(qqStr + "\n")
    file.close()

    return urlsLists


def center(url, toPath):
    que = deque()
    que.append(url)

    while len(que) != 0:
        targetUrl = que.popleft()
        urlList = getQQNumber(targetUrl, toPath)
        for item in urlList:
            tempUrl = item[0]
            que.append(tempUrl)


url = "https://www.douban.com/group/topic/41011762/?start=1100"
path = r"/Users/quanjunt/Documents/Quanjun/GitHub/PythonDemo/PythonStudy/12-爬虫和json/File/qq2.txt"
center(url, path)
