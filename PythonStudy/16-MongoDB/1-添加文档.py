
from pymongo import MongoClient
from pymongo import results

# 链接服务器
conn = MongoClient("localhost", 27017)

# 练级额数据库
db = conn.mydb

# 获取集合
collection = db.student


# 添加文档
try:
    # 添加一条数据
    # one = collection.insert_one({"name": "coder19", "age": 19, "gender": 1, "address": "北京", "isDelete": 0})
    # print(one)
    #
    # # 获取id值
    # print(one.inserted_id)


    # 添加多条数据
    # mylist = [
    #     {'name': '个人博客', 'age': 10, 'address': 'https://www.titanjun.top'},
    #     {'name': 'Github', 'age': 11, 'address': 'https://github.com/CoderTitan'}
    # ]


    # 插入指定 _id 的多个文档
    mylist = [
        {'_id': 1, 'name': '简书', 'age': 12, 'address': 'https://www.jianshu.com/u/5bd5e9ed569e'},
        {'_id': 2, 'name': 'csdn', 'age': 13, 'address': 'https://blog.csdn.net/shmilycoder'},
        {'_id': 3, 'name': '掘金', 'age': 14, 'address': 'https://juejin.im/user/5a7a64ae6fb9a0636323fd06'},
    ]
    many = collection.insert_many(mylist)

    print(many)
    # 输出插入的所有文档对应的 _id 值
    print(many.inserted_ids)

    print('添加成功')
except:
    print('添加失败')

# 断开
conn.close()







