

import pymysql

db = pymysql.connect('localhost', 'root', 'jun.0929', 'titansql')

# 创建cursor对象
cursor = db.cursor()


sql = 'insert into userinfo values'

for i in range(10, 20):
    ageStr = "(0, %d)" % i
    addsql = sql + ageStr

    try:
        cursor.execute(addsql)
        # 提交到数据库
        db.commit()
        print('插入数据成功')
    except:
        # 如果提交失败则回滚到上一次的提交
        db.rollback()
        print('插入数据失败')

cursor.close()
db.close()


