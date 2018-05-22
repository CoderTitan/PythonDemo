
# 装饰器

'''
def sayNumber(num):
    print('titan is %d' % num)


def outer(func):
    def inner(num):
        if num < 0:
            num = 0
        func(num)
    return inner

sayNumber(-12)


sayNumber = outer(sayNumber)

sayNumber(-13)
'''




# 使用@符号, 将咋混个时期应用到函数

def outer(func):
    def inner(num):
        if num < 0:
            num = 0
        func(num)
    return inner


@outer
def sayNumber(num):
    print('titan is %d' % num)



sayNumber(-14)
