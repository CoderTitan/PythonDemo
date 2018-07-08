import urllib.request


# 向指定的url地址发送请求, 并返回服务器相应的数据(文件对象
response = urllib.request.urlopen("http://www.baidu.com")

# 读取文件的全部内容, 把读取到的数据赋值给一个字符串变量
data = response.read()

'''
# print(data)
print(type(data))


# 读取一行数据
data1 = response.readline()
print(data1)


# 按照每一行读取, 以列表返回
datas = response.readlines()
print(type(datas))
print(datas)


# 把爬取到的网页写入文件

path = r"/Users/quanjunt/Documents/Quanjun/GitHub/PythonDemo/PythonStudy/12-爬虫和json/File/file1.html"
with open(path, 'wb') as f:
    f.write(data)
'''


# response 属性
# 返回当前环境的有关信息
print(response.info())

# 返回状态码
print("-------状态码-------")
code = response.getcode()
print(code)

if code == 200 or code == 304:
    # 请求正常, 数据返回
    print("处理网页信息")

# 返回当前正在爬取的URL地址
print(response.geturl())




# url的编码和解码
# url = r"https://www.titanjun.top/categories/Python基础"
url = r"https://www.titanjun.top/categories/Python%E5%9F%BA%E7%A1%80"
# 解码
newUrl1 = urllib.request.unquote(url)
print(newUrl1)

# 编码
newUrl2 = urllib.request.quote(newUrl1)
print(newUrl2)

# 冒号也会被编码
# newUrl2 = "https%3A//www.titanjun.top/categories/Python%E5%9F%BA%E7%A1%80"
