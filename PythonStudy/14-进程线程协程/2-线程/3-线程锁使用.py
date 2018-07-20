
'''

两个线程同时工作，一个存钱，一个取钱

可能导致数据异常


思路：加锁，

'''




import threading


# 定义全局变量
num = 0

# 创建锁对象
lock = threading.Lock()

# 子线程要执行的操作
def run(n):
    global num
    for i in range(100000):
        # 锁
        # 确保了这段代码只能由一个线程从头到尾的完整执行
        # 阻止了多线程的并发执行，包含锁的某段代码实际上只能以单线程模式执行，所以效率大大滴降低了
        # 由于可以存在多个锁，不同线程持有不同的锁，并试图获取其他的锁，可能造成死锁，导致多个线程挂起。只能靠操作系统强制终止

        '''
        # 添加一把锁
        lock.acquire()

        # try: 如果线程1出现问题, 那么所就永远不会被释放, 所以要加上try, 无论成败与否就一定要释放锁
        try:
            num += n
            num -= n
        finally:
            # 修改完一定要释放锁, 否则会一直存在
            lock.release()
        '''

        # 与上面代码功能相同，with lock可以自动上锁与解锁
        with lock:
            num += n
            num -= n



if __name__ == '__main__':
    # 创建线程
    t1 = threading.Thread(target=run, args=(6, ))
    t2 = threading.Thread(target=run, args=(9, ))

    # 开启线程
    t1.start()
    t2.start()

    # 等待线程结束
    t1.join()
    t2.join()

    print('num = ', num)


