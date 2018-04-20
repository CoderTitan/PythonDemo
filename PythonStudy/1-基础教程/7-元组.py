
# 元组
# 计算元素个数
print(len((1, 2, 3)))
# 合并元组
tuple1 = (1, 2) + (4, 5)
print(tuple1)
# 重复
tuple2 = ('jun',) * 3
print(tuple2)
# 检测是否包含某元素
if (2 in tuple1):
    print('2在该元组内')
else:
    print('不在元组内')
# 遍历元组
for x in tuple1:
    print(x)

# 元组内置函数
# 元组中元素最大值
print(max(tuple1))
# 元组中元素最小值
print(min(tuple1))
# 列表转换为元组
print(tuple(['a', 'd', 'f']))

