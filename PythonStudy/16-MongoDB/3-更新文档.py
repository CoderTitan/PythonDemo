
from pymongo import MongoClient

# 链接服务器
conn = MongoClient("localhost", 27017)

# 练级额数据库
db = conn.mydb

# 获取集合
collection = db.student


# 添加文档
try:
    # 修改前
    print('修改前')
    print(collection.find_one({'name': 'coder1'}))
    print(collection.find_one({'name': 'coder19'}))

    # update更新一条数据
    collection.update_one({'name': 'coder1'}, {'$set': {'age': 80}})

    # replace更新数据
    collection.replace_one({'name': 'coder19'}, {'age': 90, 'name': 'coder19'})


    # 修改后
    print('修改后')
    print(collection.find_one({'name': 'coder1'}))
    print(collection.find_one({'name': 'coder19'}))


    # 更新多条数据
    # collection.update_many({'name': 'coder2'}, {'$set': {'age': 90}})


    print('更新成功')
except:
    print('更新失败')

# 断开
conn.close()






# https://www.cnblogs.com/nixingguo/p/7260604.html