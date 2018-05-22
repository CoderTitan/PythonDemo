
# 通用装饰器

def outer(func):
    def inner(*args, **kwargs):
        print('--------')

        func(*args, **kwargs)

    return inner


@outer
def say(name, age):
    print('my name is %s, I am %d years old' % (name, age))

say('titan', 20)



# 函数的参数: 理论上可以无限个, 但实际上, 最好不要超过6-7个
