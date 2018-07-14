# Number数字
# 数字函数
import math

# 返回数字的绝对值，如abs(-12) 返回 12
print(abs(-12))
# 返回数字的上入整数(小数向上取整)，如math.ceil(4.1) 返回 5, math.ceil(4.0) 返回 4
print(math.ceil(4.01))
# 返回e的x次幂, 如math.exp(2) 返回7.38905609893065
print(math.exp(2))
# 返回数字的绝对值，如math.fabs(-10) 返回10.0
print(math.fabs(-10))
# 返回数字的下舍整数(小数向下取整)，如math.floor(4.9)返回 4
print(math.floor(4.999))
print(math.log(8, 2))
print(max(2, 4, 1, 5, 7, 12, 5))
print(math.modf(99.09))
print(round(90.09, 1))
print(math.sqrt(4))


print('----------------')
# 随机数函数
import random

# 从序列的元素中随机挑选一个元素
print(random.choice((1, 3, 5, 2)))
print(random.choice([1, 2, 3, 4]))
print(random.choice("titanjun"))

# 从指定范围内，按指定基数递增的集合中获取一个随机数
print(random.randrange(10, 100, 3))

# 随机生成的一个实数，它在[0,1)范围内
print("random:", random.random())

# 改变随机数生成器的种子, 可生成同一个随机数
random.seed(5)
print(random.random())
random.seed()
print(random.random())

print('--------')

# 随机生成指定范围[a,b]的整数
print(random.randint(1, 6))

# 随机生成指定范围[a,b)的整数
print(random.randrange(2, 8))

# 随机生成指定范围[a,b)的指定步长的数
print(random.randrange(1, 10, 3))

# 随机生成指定序列中的指定个数的元素(返回列表)
print(random.sample('titanjun', 4))


# 将序列的所有元素随机排序
list1 = [1, 2, 3, 4]
random.shuffle(list1)
print(list1)

# 随机生成下一个实数
# 随机生成一个在该范围内的实数
print(random.uniform(2, 5))


# 随机生成6位验证码
print('---随机验证码---')
checkCode = ''
for i in range(6):
    temp = random.randint(0, 9)
    checkCode += str(temp)
print("6位随机验证码:", checkCode)

print('------')


import math
print(math.e)
print(math.pi)
print(math.tau)
print(math.sqrt(13))
