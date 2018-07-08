

'''
import urllib.request


# 把怕渠道的数据直接写入文件中
path = r"/Users/quanjunt/Documents/Quanjun/GitHub/PythonDemo/PythonStudy/12-爬虫和json/File/file2.html"
urllib.request.urlretrieve("http://www.baidu.com", filename=path)

# urlretrieve在执行过程中, 会产生一些缓存
# 清楚缓存
urllib.request.urlcleanup()

'''



# 模拟浏览器
import urllib.request
import random



url = 'http://www.baidu.com'

'''
# 模拟请求头
headers = {
    "Accept" : "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With" : "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
    "Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8"
}

# 设置一个请求体
req = urllib.request.Request(url, headers=headers)
# 发起请求
response = urllib.request.urlopen(req)
data = response.read()
print(data)
'''



agentsList = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0"
]

agentStr = random.choice(agentStr)
req = urllib.request.Request(url)

# 想请求体里添加User-Agent
req.add_header('User-Agent', agentStr)
response = urllib.request.urlopen(req)
data = response.read().decode('utf-8')
print(data)




