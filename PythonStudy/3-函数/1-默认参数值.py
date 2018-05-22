
# 函数
'''
定义函数

格式:
def 函数名(参数列表):
    语句
    return 表达式


def 定义函数关键字
'''


# 1. 默认参数
def sumCount(count = 4):
    sum = 0
    for i in range(count + 1):
        sum += i

    print(sum)

sumCount()

sumCount(5)


# 关键字参数
# 允许函数调用时的参数与函数定义时的参数顺序不一致

def printInfo(name, age):
    print(name, age)

printInfo('jun', 20)
printInfo(age=19, name='titan')





























