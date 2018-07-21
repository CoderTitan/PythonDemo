


import pymysql



# 链接数据库
# 参数1：mysql服务所在主机的IP(可以是IP地址, 或者localhost)
# 参数2：用户名
# 参数3：密码
# 参数4：要连接的数据库名
# db = pymysql.connect('localhost', 'root', 'jun.0929', 'titansql')
db = pymysql.connect('192.168.2.12', 'root', 'jun.0929', 'titansql')


# 创建一个cursor对象
cursor = db.cursor()

# 创建sql语句
sql = "select version()"

# 执行sql语句
cursor.execute(sql)

# 获取返回的信息
data = cursor.fetchone()
print(data)

# 断开数据库
cursor.close()

# 关闭数据库
db.close()

