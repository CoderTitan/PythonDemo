
# 自定义模块

# 引入单个或多个模块
# 格式: import module1[, module2, module3, module4, ....]

import time, random, os


# 引入自定义模块, 不用加.py后缀
# 一个模块只会被引入一次, 防止重复引用
import Titan

Titan.sayBad()
Titan.sayGood()
print(Titan.name)
















