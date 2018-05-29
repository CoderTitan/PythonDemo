
# 一个.py文件就是一个模块

'''
def sayGood():
    print('good')


def sayNice():
    print('nice')

def sayBad():
    print('bad')


age = 20
name = 'titan'



print('这是Titan模块')
'''



# 每一个模块中都有一个__name__属性, 当其值等于__main__时, 表明该模块自身在执行, 否则被引入了其他文件
# 当前文件如果为程序的入口文件, 则__name__属性的值为__main__

if __name__ == '__main__':
    print('这是Titan模块--b')
else:
    def sayGood():
        print('good--b')


    def sayNice():
        print('nice--b')


    def sayBad():
        print('bad--b')


    age = 26
    name = 'titan--b'





