# 字典
# 1.内置函数
dic1 = {'name': 'titan', 'age':20}
# 计算字典元素个数，即键的总数
print(len(dic1))
# 字典(Dictionary) str() 函数将值转化为适于人阅读的形式，以可打印的字符串表示
print(str(dic1))
# 返回输入的变量类型，如果变量是字典就返回字典类型
print(type(dic1))


# 内置方法
dic2 = {'name': 'titan', 'age':20}
# 判断键是否存在于字典中, 在True, 不在False
print(dic2.__contains__('name'))

# 以列表返回可遍历的(键, 值) 元组数组
print(dic2.items())

# 删除字典内所有元素
dic2.clear()
print(dic2)


# get() 函数返回指定键的值，如果值不在字典中返回默认值
dic5 = {'name': 'titan', 'age':20}
print(dic5.get('name'))
print(dic5.get('Sex', 'man'))
print(dic5.setdefault('name'))
print(dic5.setdefault('Sex', 'man'))
print(dic5)

# 合并字典
dic6 = {'sex': 'new'}
dic5.update(dic6)
print(dic5)

# 删除
print(dic5.pop('Sex'))
print(dic5)
print(dic5.popitem())
print(dic5)

# fromkeys() 函数用于创建一个新字典，以序列seq中元素做字典的键，value为字典所有键对应的初始值
# dic3 = dict.fromkeys(['name', 'titan'])
# print(dic3)
# dic4 = dict.fromkeys(['name', 'titan'], 20)
# print(dic4)










