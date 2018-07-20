

import threading

# 创建一个全局的ThreadLocal对象
# 每个县城都有一个独立的存储空间
# 每个线程对ThreadLocal对象都可以读写, 但是互不影响
local = threading.local()

# 全局变量
num = 0

def run(x, n):
    x = x + n
    x = x - n


def localFunc(n):
    # 每个线程都有local.x, 就是线程的局部变量
    local.x = num
    for i in range(10000):
        run(local.x, n)
    print('%s--%s' % (threading.current_thread().name, local.x))



if __name__ == '__main__':
    t1 = threading.Thread(target=localFunc, args=(6, ))
    t2 = threading.Thread(target=localFunc, args=(9, ))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


    print('num = ', num)












