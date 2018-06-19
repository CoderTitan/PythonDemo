
# 导入父类的类
# from 文件名 import 模块名
from Father import Father
from Mother import Mother

class Son(Father, Mother):
    def __init__(self, money, faceValue):
        Father.__init__(self, money)
        Mother.__init__(self, faceValue)



