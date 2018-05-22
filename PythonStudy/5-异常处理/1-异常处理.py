
# 异常处理


'''
错误处理的语句
try.......except....else(else可有可无)

格式:

try:
    语句t
except 错误码 as e:
    语句1
except 错误码 as e:
    语句2
except 错误码 as e:
    语句3
    ...
except 错误码 as e:
    语句n
else:
    语句e




作用: 用来检测try语句块中的错误, 从而让except语句补货错误信息并处理
'''

'''
try:
    print(7 / 0)
except ZeroDivisionError:
    print('处暑为0')
except NameError:
    print('没有改变量')
except SyntaxError:
    print('')

else:
    print('代码OK')

print('-----')


# 第二种情况
try:
    print(7 / 0)
except (ZeroDivisionError, NameError):
    print('程序异常')

# 第三种情况
try:
    print(7 / 0)
except :
    print('程序异常')
'''



'''
特殊:
1. 错误其实是class类, 所有的错误都是继承自BaseException, 所以再补货的时候, 他捕获了该类型的错误, 还会把子类一网打尽

注意: 还有一些错误是无法跳过的, 比如内存错误


2. 跨越多层调用
多函数的多层级调用
'''


# try--except--finally语句
'''
try:
    语句t
except 错误码 as e:
    语句1
except 错误码 as e:
    语句2
except 错误码 as e:
    语句3
    ...
except 错误码 as e:
    语句n
finally:
    语句e

# 无论语句t是否有错误, finally语句一定执行
'''


# 抛出异常
# raise 语句允许程序员强制抛出一个指定的异常
try:
    raise NameError('TitanJun')
except NameError:
    print('NameError错误')
    raise

# 断言
# def sumNumber(num, div):
#
#     assert (div != 0), 'div不能为0'
#
#     return num / div
#
# print(sumNumber(2, 0))

