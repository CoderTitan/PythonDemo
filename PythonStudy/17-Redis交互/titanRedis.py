
import redis

class TitanRedis():
    # 初始化
    def __init__(self, passed, host='localhost', port=6379):
        self.__redis = redis.StrictRedis(host=host, port=port, password=passed)
        

    # 写入值
    def set(self, key, value):
        self.__redis.set(key, value)


    # 读取值
    def get(self, key):
        if self.__redis.exists(key):
            return self.__redis.get(key)
        else:
            return ''