

'''
class Person(object):
    # 类属性, 是可以用类名访问的属性
    ranCount = 10
    title = "titan"

    # 对象属性: 能用对象调用的属性

    def __init__(self, title):

        self.title = title



# 类属性的优先级高于对象属性
# 动态添加的属性是对象属性, 只对当前对象起作用, 对于类创建的其他对象没有作用



# 动态添加方法
from types import MethodType


per = Person("jun")

def say(self):
    print("my name is " + self.title)

per.speak = MethodType(say, per)

per.speak()
'''



# @property
class Person(object):


    def __init__(self, title):
        # 访问限制
        self.__title = title


    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title


person = Person('titan')

# 属性直接对外暴露
# 不安全, 没有数据的过滤
person.title = 'jun'

print(person.title)


# @property: 可以让你对受限制访问的属性使用点语法直接访问




