
# 读文件
'''过程
1. 打开文件
2. 读取文件内容
3. 关闭文件
'''


# 1. 打开文件
'''
open(file, mode)
参数:
file: 文件路径
mode: 打开方式

'''

'''
# 打开文件
path = r'/Users/quanjunt/Documents/Quanjun/GitHub/PythonDemo/PythonStudy/4-装饰器和文件读写/text.txt'
file = open(path, 'w+')

# 读取文件
str = file.read()
print(str)

print('----------')
# 读取一行
print(file.readline())

# 遍历
for line in file:
    print(line)


# 把文件读到列表中
print(list(file))
print(file.readlines())

# 写入文件
leng = file.write('我是一只小鸭子')
print(leng)

file.writelines(['hello', 'Python'])


# tell/seek
# 打开文件
path = r'/Users/quanjunt/Documents/Quanjun/GitHub/PythonDemo/PythonStudy/4-装饰器和文件读写/text.txt'
file = open(path, 'rb+')

l = file.readline()
print(l)

# pos = file.tell()
# print(pos)

file.seek(5, 0)
print(file.readline())

file.close()

'''

path = r'/Users/quanjunt/Documents/Quanjun/GitHub/PythonDemo/PythonStudy/4-装饰器和文件读写/text.txt'

with open(path, 'rb+') as file:
    str = file.read()
    print(str)
file.close()




