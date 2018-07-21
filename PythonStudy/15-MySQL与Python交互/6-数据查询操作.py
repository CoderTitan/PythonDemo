
'''
fetchone()
功能：获取下一个查询结果集，结果集是一个对象

fetchall()
功能：接收全部的返回的行

rowcount:是一个只读属性，返回execute()方法影响的行数

'''


import pymysql

db = pymysql.connect('localhost', 'root', 'jun.0929', 'titansql')

# 创建cursor对象
cursor = db.cursor()

sql = 'select * from userinfo where age>16'

try:
    cursor.execute(sql)

    print(cursor.fetchone())
    print('查询到-%d-条数据' % cursor.rowcount)

    result = cursor.fetchall()
    for row in result:
        print('%d--%d' % (row[0], row[1]))

    print('数据查询成功')

except:
    print('数据查询失败')

cursor.close()
db.close()
