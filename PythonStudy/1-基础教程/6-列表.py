
# 列表

# 1. 脚本操作符
list1 = [1, 2, 3]
# 元素个数
print(len(list1))
# 重复
list2 = [2] * 3
print(list2)
# 是否包含某元素
if (3 in list1):
    print('3在列表内')
else:
    print('3不在列表内')
# 遍历列表
for x in list1 :
    print(x)

# 2.列表函数&方法
print(max(list1))
print(list(('q', 1)))
list1.append(2)
print(list1)
print(list1.count(2))
print(list1.index(3))
list1.insert(1, 'jun')
print(list1)
list1.remove(3)
print(list1)
list1.reverse()
print(list1)
# list1.sort()
# print(list1)
# 添加多个值
list3 = [12, 'as', 45]
list4 = (23, 'ed')
list3.extend(list4)
print(list3)

print(list3.pop())
print(list3)
print(list3.pop(2))
print(list3)


