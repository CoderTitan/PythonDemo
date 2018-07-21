

import pymysql

db = pymysql.connect('localhost', 'root', 'jun.0929', 'titansql')

# 创建cursor对象
cursor = db.cursor()


sql = 'update userinfo set age=30 where id=4'
try:
    cursor.execute(sql)
    db.commit()
    print('数据更新成功')
except:
    db.rollback()
    print('数据更新失败')


cursor.close()
db.close()



