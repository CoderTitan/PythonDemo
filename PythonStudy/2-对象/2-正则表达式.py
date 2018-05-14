# -*- coding: UTF-8 -*-


import re

# 正则表达式
# 1. re.match函数
match = re.match('https', 'https :// www .titanjun .top')
print(match)
print(match.group())
print(match.groups())
print(match.span())

match2 = re.match('www', 'https://www.titanjun.top')
print(match2)
# print(match2.group())

print('-------华丽分割线--------')


# 2. re.search
str = 'https :// www .titanjun .top'
search1 = re.search(r'www', str, re.M | re.I)
print(search1)
print(search1.span())
print(search1.group())
print(search1.groups())

print('-------华丽分割线--------')


# 3. sub替换函数
subStr = '2018-05-03 # 文章的写作日期'
# 删除注释
subStr2 = re.sub('#.*$', '', subStr)
print(subStr2)

# 时间上替换-
# \D: 代表任意非数字
subStr3 = re.sub('\D', '.', subStr2)
print(subStr3)
print(re.sub('\D', '.', subStr2, 2))

print('-------华丽分割线--------')


# 4. compile 函数
pattern = re.compile(r'\d+')  # 用于匹配至少一个数字
print(pattern.match('titan0929'))
print(pattern.match('titan0929', 5, 7)) # 从第5个字符开始匹配
m = pattern.match('0929titan')
print(m.group())
print(m.start())
print(m.end())
print(m.span())
print('-------华丽分割线--------')


# 5. findall
pattern2 = re.compile(r'\d+')  # 用于匹配至少一个数字
fin1 = pattern2.findall('titanjun09-www123titan29')
fin2 = pattern2.findall('titan123jun45www90', 6, 16)
print(fin1)
print(fin2)
print('-------华丽分割线--------')


# 6. split
split1 = re.split('\W+', 'https://www.titanjun.top')
print(split1)
split2 = re.split('\W+', 'https://www.titanjun.top', 1)
print(split2)






















