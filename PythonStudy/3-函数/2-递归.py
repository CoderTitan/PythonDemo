
'''递归调用
一个函数调用函数本身(凡是循环能做的事情, 递归都能写出来)

方式:
1. 写出临界条件
2. 找这一次和上一次的关系
3. 假设当前函数已经能用, 调用自身上一次的计算结果, 在求本次的计算结果
'''


# 输入一个数(大于1), 求1+2+3+...+n的和
'''常规方式

def sum1(n):
    sum = 0

    for x in range(1, n + 1):
        sum += x

    return sum

print(sum1(4))

# 结果输出: 10
'''

# 递归方式
def sum2(n):
    if n == 1:
        return 1
    else:
        return n + sum2(n - 1)

print(sum2(5))


# 递归遍历目录
# 一般不使用, 对系统消耗较大
import os

def getAllDir(path, space = ""):
    fileList = os.listdir(path)
    space += "  "

    # 处理每一个文件
    for fileName in fileList:
        # 判断是否是目录
        fileAbsPath = os.path.join(path, fileName)
        if os.path.isdir(fileAbsPath):
            print(space + "目录: ", fileName)
            # 是目录的情况下, 再次遍历此目录
            getAllDir(fileAbsPath, space)
        else:
            print(space + "普通文件: ", fileName)



path = r'/Users/quanjunt/Documents/Quanjun/GitHub/PythonDemo/PythonStudy/4-装饰器和文件读写'
getAllDir(path)



# 栈模拟递归遍历目录
# def getAllDirDE(path):












