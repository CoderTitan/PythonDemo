import pymysql

db = pymysql.connect('localhost', 'root', 'jun.0929', 'titansql')

# 创建cursor对象
cursor = db.cursor()

sql = 'delete from userinfo where age=16'

try:
    cursor.execute(sql)
    db.commit()
    print('数据删除成功')
except:
    db.rollback()
    print('数据删除失败')

cursor.close()
db.close()