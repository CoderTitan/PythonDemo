

'''重写

__str__(): 在调用print打印对象时自动调用, 是给用户用的, 是一个描述对象的方法
__repr__(): 是给机器用的, 在Python解释器里面直接敲对象名再回车后调用的方法

注意: 在没有 str是, 且有repr, str = repr
'''


class Person(object):
    '人类的基类'

    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

    def __str__(self):
        return "这里是str"



per = Person('jun', 's')
print(per)






