

import pymongo
# 用于ID查询的库
from bson.objectid import ObjectId


# 链接服务器
conn = pymongo.MongoClient("localhost", 27017)

# 练级额数据库
db = conn.mydb

# 获取集合
collection = db.student


# 查询文档
try:
    # 查询集合中的第一条数据
    # print(collection.find_one())
    # print(collection.find())
    # 查询所有文档
    '''
    res0 = collection.find()
    
    for row in res0:
        print(row)
    '''


    # 查询部分文档
    '''
    res1 = collection.find({'age': {'$gt': 20}})
    for row in res1:
        print(row)
    '''


    # 统计查询
    res2 = collection.count_documents({'age': {'$gt': 19}, 'gender': 0})
    print(res2)


    # 正则表达式查询
    # res11 = collection.find({'name': {'$regex': '^c'}})
    # for row in res11:
    #     print(row)


    # 根据ID查询
    # res3 = collection.find({'_id': ObjectId('5b52cdbbd87e53d6306f3585')})
    # print(res3)
    # res12 = collection.find_one({'_id': ObjectId('5b52cdbbd87e53d6306f3585')})
    # print(res12)
    '''
    res3 = collection.find({'_id': ObjectId('5b52cdbbd87e53d6306f3585')})
    print(res3)
    print(type(res3))
    for row in res3:
        print(row)
    '''


    # 根据指定条件查询
    # res10 = collection.find({'age': 19})
    # for row in res10:
    #     print(row)


    # 排序
    # 默认升序
    # res4 = collection.find().sort('age')
    # 降序: DESCENDING, 升序: ASCENDING

    # res4 = collection.find().sort('age', pymongo.DESCENDING)
    # for row in res4:
    #     print(row)

    res4 = collection.find().sort('age', 1)
    for row in res4:
        print(row)




    # 跳过指定记录输出
    # res13 = collection.find({'age': {'$gt': 19}, 'gender': 0}).skip(1)
    # for row in res13:
    #     print(row)


    # 分页查询
    # res5 = collection.find().skip(3).limit(3)
    # for row in res5:
    #     print(row)



    print('查询成功')
except:
    print('查询失败')

# 断开
conn.close()














