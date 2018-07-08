
'''
# 设置超时
import urllib.request

# 如果网页时间长时间未响应, 系统判断超时, 无法爬取
for i in range(1, 100):
    try:
        response = urllib.request.urlopen('http://www.baidu.com', timeout=0.5)
        data = response.read().decode('utf-8')
        print(len(data))
    except:
        print('请求超时, 稍后再试')

'''

'''
使用场景：进行客户端与服务端之间的消息传递时使用

GET: 通过URL网址传递信息，可以直接在URL网址上添加要传递的信息
POST: 可以向服务器提交数据，是一种比较流行的比较安全的数据传递方式
PUT: 请求服务器存储一个资源，通常要指定存储的位置
DELETE: 请求服务器删除一个资源
HEAD: 请求获取对应的HTTP报头信息
OPTIONS:可以获取当前UTL所支持的请求类型

'''

print('------get请求--------')
'''
特点：把数据拼接到请求路径的后面传递给服务器

有点：速度快

缺点：承载的数据量小，不安全
'''

'''
url = 'http://www.baidu.com'
response = urllib.request.urlopen(url)
data = response.read().decode('utf-8')
print(data)
print(type(data))
'''


print('--------post请求-----------')

'''
特点：把参数进行打包，单独传输

优点：数量大，安全(当对服务器数据进行修改时建议使用post)

缺点：速度慢
'''

'''
import urllib.parse
data1 = {
    'username': 'titan',
    'password': 'jun'
}
# 对要发送的数据进行打包
postData = urllib.parse.urlencode(data1).encode('utf-8')
# 请求体
req = urllib.request.Request(url, postData)
# 请求
header = "User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36"
req.add_header(header)
response1 = urllib.request.urlopen(req)

data2 = response.read().decode('utf-8')
print(data2)

'''


print('-----json数据------')

# json数据解析
import json
jsonStr = '{"name":"titan", "age":18, "hobby":["money","power","english"], "parames":{"a":1,"b":2}}'
# 将json数据转成python类型的数据
jsonData = json.loads(jsonStr)
print(type(jsonData))
print(jsonData)
print(jsonData['parames'])


# 将python类型的数据转成json格式的字符串
jsonStr2 = json.dumps(jsonData)
print(type(jsonStr2))
print(jsonStr2)



# 读取本地的json文件
path = r"/Users/quanjunt/Documents/Quanjun/GitHub/PythonDemo/PythonStudy/12-爬虫和json/File/menuList.json"
with open(path, 'rb') as file:
    jsonData3 = json.load(file)
    print(jsonData3)



# 把数据写入json文件
path2 = r"/Users/quanjunt/Documents/Quanjun/GitHub/PythonDemo/PythonStudy/12-爬虫和json/File/write.json"
with open(path2, 'w') as file:
    json.dump(jsonData3, file)

