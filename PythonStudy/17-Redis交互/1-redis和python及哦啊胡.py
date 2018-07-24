

import redis

# 链接
red = redis.StrictRedis(host='localhost', port=6379, password='titan')


# 格局数据类型的不同调用的方法也不同
# 写数据
red.set('z1', 'titan')

# 读数据
print(red.get('z1'))


# 缓冲多条命令然后依次执行, 减少服务器-客户端之间的TCP数据包
pipe = red.pipeline()
pipe.set('z2', 'coder')
pipe.set('z3', 'coder1')
pipe.execute()


