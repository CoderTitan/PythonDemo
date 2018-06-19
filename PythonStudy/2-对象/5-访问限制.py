
# 访问限制

class Person(object):
    '人类的基类'

    empCount = 0

    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.__age = age

    # 注意: 方法的参数必须以self当第一个参数
    # self代表类的实例(某个对象), 谁调用这个方法self就代表谁
    def displayCount(self):
        print("被调用次数: %d" % Person.empCount)


    def displayPerson(self):
        print("姓名:", self.name, ',', "性别:", self.sex)




# 1.创建第一个对象
person1 = Person("titan", 'man', 20)
person1.displayPerson()
person1.name = 'jun'


# 如果要让内部的属性不被外界访问(设置私有属性), 在属性前加两个下划线
# 在Python中两个下划线修饰的属性, 那么这个属性就是私有属性
# 但是在Python中没有绝对的私有, 可以再冲虚运行的过程中给对象动态的添加属性

person1.__age = 10
print(person1.__age)

person1.a = 200
print(person1.a)

