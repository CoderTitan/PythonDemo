

'''
__name__属性:
模块就是一个可执行的.py文件, 一个模块呗另一个程序引用, 我们不想让模块中的某些代码执行, 可以用__name__属性来使程序仅调用模块中的一部分

'''


import Titan

print(dir(Titan))

print(dir())

sum = 30
print(dir())


del sum
print(dir())



















