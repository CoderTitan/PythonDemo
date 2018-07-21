

import pymysql

db = pymysql.connect('localhost', 'root', 'jun.0929', 'titansql')

# 创建cursor对象
cursor = db.cursor()

# 建表
# 在建表之前要检查表是否存在, 如果存在则删除
cursor.execute("drop table if exists userinfo")

# 创建表
try:
    sql = "create table userinfo(id int auto_increment primary key, age int not null)"
    cursor.execute(sql)
    print('创建成功')
except:
    print('创建表失败')


cursor.close()
db.close()



