

'''
# from...import: 从模块中导入一个指定的部分到当前的命名空间
# 格式: from module import name1[, name2, name3, ....]
同样可以导入多个方法或者变量

# 弊端: 可能重名



from Titan import sayGood, sayBad, age

sayBad()
sayGood()
print(age)

'''


'''
from...import * 语句
# 作用: 把一个模块中所有的内容, 全部倒入当前命名空间, 但是最好不要过多地使用


'''

from Titan import *

sayGood()

print(age)

















