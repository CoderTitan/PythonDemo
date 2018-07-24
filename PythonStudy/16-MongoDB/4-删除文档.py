

from pymongo import MongoClient

# 链接服务器
conn = MongoClient("localhost", 27017)

# 练级额数据库
db = conn.mydb

# 获取集合
collection = db.student


# 删除文档
try:
    # 删除一条数据
    # res = collection.delete_one({'age': 90})
    # print(res.deleted_count)

    # 删除多条数据
    res1 = collection.delete_many({'age': 90})
    # 输出删除的数据的数量
    print(res1.deleted_count)




    print('删除成功')
except:
    print('删除失败')

# 断开
conn.close()