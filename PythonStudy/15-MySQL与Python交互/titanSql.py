
# 对数据库的操作进行封装


import pymysql

class TitanSql():
    # 初始化对象
    def __init__(self, host, user, passwd, dbName):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.dbName = dbName

    # 链接数据库
    def connet(self):
        self.db = pymysql.connect(self.host, self.user, self.passwd, self.dbName)
        self.cursor = self.db.cursor()


    # 关闭数据库
    def close(self):
        self.cursor.close()
        self.db.close()


    # 查询符合条件的数据个数
    def getSearchCount(self, sql):
        count = 0
        try:
            self.connet()
            self.cursor.execute(sql)
            count = self.cursor.rowcount
            self.close()
        except:
            print("查询失败")

        return count


    # 查询符合条件的下一条数据
    def getSearchOne(self, sql):
        result = None
        try:
            self.connet()
            self.cursor.execute(sql)
            result = self.cursor.fetchone()
            self.close()
        except:
            print("查询失败")

        return result


    # 查询符合条件的所有的数据
    def getSearchAll(self, sql):
        result = ()
        try:
            self.connet()
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            self.close()
        except:
            print("查询失败")

        return result


    # 插入数据
    def insert(self, sql):
        return self.__edit(sql)


    # 更新数据
    def update(self, sql):
        return self.__edit(sql)


    # 删除数据
    def delete(self, sql):
        return self.__edit(sql)


    # 插入/更新/删除数据相关操作封装
    def __edit(self, sql):
        count = 0
        try:
            self.connet()
            count = self.cursor.execute(sql)
            self.db.commit()
            self.close()
        except:
            self.db.rollback()
            print('数据提交失败')

        return count