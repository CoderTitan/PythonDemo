
# 面向对象
class Person(object):
    '人类的基类'

    empCount = 0

     def __init__(self, name, sex):
        self.name = name
        self.sex = sex
        Person.empCount += 1

    # 注意: 方法的参数必须以self当第一个参数
    # self代表类的实例(某个对象), 谁调用这个方法self就代表谁
    def displayCount(self):
        print("被调用次数: %d" % Person.empCount)


    def displayPerson(self):
        print("姓名:", self.name, ',', "性别:", self.sex)


# 1.创建第一个对象
person1 = Person("titan", 'man')
person1.displayPerson()

# 2.创建第二个对象
person2 = Person('jun', 'woman')
person2.displayPerson()
person2.displayCount()
print(Person.empCount)


# 3.增加类的属性
person1.age = 19
print(person1.age)

# 4.修改属性值
person1.age = 20
print(person1.age)

# 5.删除属性
del person1.age
# 此处条用age属性会报错
# print(person1.age)

# 6.常用函数
# 6.1.检查是否存在一个属性
print(hasattr(person1, 'age')) #False
print(hasattr(person1, 'name')) #True

# 6.2.访问对象的属性
print(getattr(person1, 'name'))  #titan

# 6.3.设置一个属性(如果属性不存在，会创建一个新属性)
setattr(person2, 'age', 17)
print(person2.age) #17

# 6.4.删除属性
delattr(person2, 'age')

# Python内置类属性
# 1.类的文档字符串
print(Person.__doc__)
# 输出结果: 人类的基类

# 2.类的所有父类构成元素
print(Person.__bases__)
# 输出结果: (<class 'object'>,)

# 3.类名
print(Person.__name__)
# 输出结果: Person

# 4. 类定义所在的模块
print(Person.__module__)
# 输出结果: __main__

# 2.类的属性(字典)
print(Person.__dict__)

'''输出结果
{
'__module__': '__main__', 
'__doc__': '人类的基类', 
'empCount': 2, 
'__init__': <function Person.__init__ at 0x1041a7510>, 
'displayCount': <function Person.displayCount at 0x1041a76a8>, 
'displayPerson': <function Person.displayPerson at 0x1041a7730>, 
'__dict__': <attribute '__dict__' of 'Person' objects>, 
'__weakref__': <attribute '__weakref__' of 'Person' objects>
}
'''


# 私有类
# class Dog:
#     '小狗狗'
#
#     __age = 14
#
#     def __init__(self, name):