from functools import reduce



# python内置函数
# 1. map函数
# 根据提供的函数对指定序列做映射, 并返回映射后的序列

'''
map(function, iterable, ...)

参数介绍:
function -- 函数，有两个参数
iterable -- 一个或多个序列

Python 2.x 返回列表。
Python 3.x 返回迭代器
'''


# 调用外部函数
def square(x):
    return x ** 2

res = map(square, [1, 2, 3, 4])
print(res)
print(list(res))


# 使用匿名函数
res1 = map(lambda x: x * 3, [1, 2, 3, 4])
print(list(res1))


# 使用内置函数
res2 = map(str, [2, 3, 4, 5])
print(list(res2))

# 多个序列
res3 = map(lambda x, y: x * y, [1, 2, 3, 4], [3, 2, 4, 1])
print(list(res3))


print('-------reduce--------')


# 2. reduce
'''
在 Python3 中，reduce() 函数已经被从全局名字空间里移除了，它现在被放置在 fucntools 模块里，如果想要使用它，则需要通过引入 functools 模块来调用 reduce() 函数

reduce() 函数会对参数序列中元素进行累积。
函数将一个数据集合（链表，元组等）中的所有数据进行下列操作：用传给 reduce 中的函数 function（有两个参数）先对集合中的第 1、2 个元素进行操作，得到的结果再与第三个数据用 function 函数运算，最后得到一个结果

参数
function -- 函数，有两个参数
iterable -- 可迭代对象
initializer -- 可选，初始参数

返回值
返回函数计算结果
'''

# 求元素的和
def mySum(x, y):
    return x + y

list1 = [1, 2, 3, 4]
red = reduce(mySum, list1)
print(red)

red2 = reduce(mySum, list1, 2)
print(red2)

# 匿名函数
red3 = reduce(lambda x, y: x * y, list1)
print(red3)

red4 = reduce(lambda x, y: x * y, list1, 3)
print(red4)

red5 = reduce(lambda x, y: x + y, ['1', '2', '3', '4'], '数字: ')
print(red5)

print('--------filter-------')

# 过滤
'''
filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。
该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判，然后返回 True 或 False，最后将返回 True 的元素放到新列表中

filter(function, iterable)
参数
function -- 判断函数。
iterable -- 可迭代对象。

返回值
python2中返回的是过滤后的列表, 而python3中返回到是一个filter类
'''

def isOdd(x):
    if x % 2 == 1:
        return True
    return False

list2 = [1, 2, 3, 4, 5, 6]
fil0 = filter(isOdd, list2)
print(fil0)
print(list(fil0))

# 匿名函数
fil = filter(lambda x: x % 2 == 0, list2)
print(list(fil))

'''输出结果:
<filter object at 0x1039e20f0>
[1, 3, 5]
[2, 4, 6]
'''

print('------sort--------')


# 排序
'''
- 在列表中有一个内置的排序函数`sort()`, 对列表的对象进行排序, 没有返回值
- `sorted()`函数对所有可迭代的对象进行排序操作
- `sort`与`sorted`区别：
  - `sort`是应用在`list`上的方法，`sorted`可以对所有可迭代的对象进行排序操作。
  - `list`的`sort`方法返回的是对已经存在的列表进行操作，而内建函数`sorted`方法返回的是一个新的`list`，而不是在原来的基础上进行的操作
  
sorted(iterable[, cmp[, key[, reverse]]])

'''

# 用sort
list3 = [3, 7, 2, 5, 0, 4]
list3.sort()
print(list3)

aList = ['123', 'Google', 'Runoob', 'Taobao', 'Facebook']
aList.sort(reverse=True) # 降序
print(aList)


def takeSecond(elem):
    return elem[1]

random = [(2, 2), (3, 4), (4, 1), (1, 3)]

# 指定第二个元素排序
random.sort(key=takeSecond)
print(random)

'''输出结果:
[0, 2, 3, 4, 5, 7]
['Taobao', 'Runoob', 'Google', 'Facebook', '123']
[(4, 1), (2, 2), (1, 3), (3, 4)]
'''

print('------sorted--------')

list4 = sorted(list3)
print(list4)

#按绝对值大小排序
list5 = [4,-7,2,6,-3]
#key接受函数来实现自定义排序规则
list6 = sorted(list5, key=abs)
print(list6)

# 将序排列
print(sorted(list5, key=abs, reverse=True))


#函数可以自己写
def myLen(str):
    return len(str)

list7 = ['b333','a1111111','c22','d5554']
list8 = sorted(list7, key=myLen) # 默认升序排序
print(list8)

# 匿名函数
list9 = sorted(list7, key=lambda x: len(x), reverse=True)
print(list9)

'''输出结果:
[0, 2, 3, 4, 5, 7]
[2, -3, 4, 6, -7]
[-7, 6, 4, -3, 2]
['c22', 'b333', 'd5554', 'a1111111']
['a1111111', 'd5554', 'b333', 'c22']
'''

print('-----enumerate--------')

# enumerate
# 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中

seasons = ['Spring', 'Summer', 'Fall', 'Winter']
sea1 = enumerate(seasons)
print(sea1)
print(list(sea1))

# 自定义起始索引
sea2 = list(enumerate(seasons, start=1))
print(sea2)

# 普通的 for 循环
i = 0
for element in seasons:
     print(i, seasons[i])
     i +=1

# for 循环使用 enumerate
for i, ele in enumerate(seasons):
    print(i, ele)


print('------zip--------')

# zip
# zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
#
# 如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。
# zip([iterable, ...])

a = [1, 2, 3]
b = ['a', 'b', 'c']
c = [4, 5, 6, 7]

zip1 = zip(a, b)
print(zip1)
print(list(zip1))

# 两个列表不同元素个数, 元素个数与最短的列表一致
zip2 = zip(a, c)
print(list(zip2))

# `*`号操作符，可以将元组解压为列表
a1, c1 = zip(*zip(a, c))
print(a1)
print(c1)

print('------reverse-----')

# reverse
# 函数用于反向列表中元素
list31 = [1, 2, 3, 4]
list31.reverse()
print(list31)
