
# 字符串
'''
str = 'Hello Python'


# 1. 输出完整字符串
print("完整字符串--" + str)
# 结果输出:

# 2. 输出第一个字符
print("第一个字符--" + str[0])

# 3. 输出第三到七个字符
print("第3-7个字符--" + str[2:6])

# 4. 输出低2个字符开始的所有字符
print("第2个开始的所有字符--" + str[1:])

# 5. 拼接字符串
# 像上面一样, 字符串用 `+`拼接
print("拼接--" + str)

# 6. 输出3次
# `*` 表示重复操作, 需要重复操作几次, 后面跟上次数即可
print(str * 3)

# 7. 输出最后一个字符
print("最后一个字符--" + str[-1])

# 8. 输出倒数第二个字符
print("倒数第二个字符--" + str[-2])
'''

# 判断字符串中是否包含某字符串
str = 'Hello Python'

if ('llo' in str):
    str += ' True'
else:
    str += ' False'
print(str)

# 判断字符串是否不包含某字符串
if ('py' not in str):
    str += ' not in'
else:
    str += ' in'
print(str)


# 格式化
print('che is %d' % 19)

# format函数
# 不设置指定位置，按默认顺序
str1 = '{} {}'.format('hello', 'python')
print(str1)
# 设置指定位置
str2 = '{0}{1}'.format('Python', '字符串')
print(str2)
# 设置指定位置
str3 = '{1} {0} {1}'.format('hello', 'che')
print(str3)

# 设置参数
print("姓名: {name}, 年龄: {age}".format(name='che', age=18))
# 设置字典参数
dic = {'name': 'jun', 'age': 20}
print("姓名: {name}, 年龄: {age}".format(**dic))
# 设置列表参数
list0 = ['titan', 20]
print("姓名: {0[0]}, 年龄: {0[1]}".format(list0))


print('百分比: %d%%' % 23)
print('{}索引值: {{0}}'.format('jun'))
print('{:#x}'.format(9))
print('{:#X}'.format(9))

str4 = '''hello
che'''
print(str4)


print('--------这是一条完美的分割线-----------')

# 字符串内建函数
# 1.把字符串的第一个字符大写
print('titan'.capitalize())
# 2.返回一个原字符串居中,并使用空格填充至长度 width 的新字符串
print('titan'.center(10, '-'))
# 3.统计字符串里某个字符出现的次数
print('hello world'.count('l', 1, 8))
print('hello world'.count('l'))
# 编码字符串
print('titan'.encode('UTF-8','strict'))
# 是否已某一字符结尾
str5 = 'her is my girl friend haha!!'
print(str5.endswith('!!'))
print(str5.endswith('ha', 0, len(str5) - 2))
# 替换制表符
print('hello\tpython'.expandtabs())
# 检测是否包含某字符串, 返回索引值
print(str5.find('irl'))
print(str5.index('gi'))
# 检测是否包含字母和数字
print('jun0929'.isalnum())
print('titan'.isalpha())
print('234'.isdecimal())
print('23e'.islower())
print('JING'.isupper())

# 通过指定字符连接序列中元素后生成的新字符串
seq1 = ['a', 's', 'd']
print('-'.join( seq1 ))

# 一个原字符串左对齐,并使用空格填充至指定长度的新字符串
str6 = 'python'
print(str6.ljust(10, '9'))

# 字符转换
tuple12 = 'https://www.titanjun.top'.partition('://')
print(tuple12)

# 替换
str7 = 'Python is a good language!'
print(str7.replace('o', 'i', 2))

# 在指定位置检测字符串
print('this'.startswith('th', 1, 4))
print('Python'.swapcase())

# 分割字符串
print(str7.split(' '))
print(str7.split(' ', 3))

# 换行符分割
str8 = 'ab c\n\nde fg\rkl\r\n'
print(str8.splitlines())

str9 = 'ab c\n\nde fg\rkl\r\n'
print(str9.splitlines(True))

