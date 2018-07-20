from multiprocessing import Pool
import time, random, os



# 子进程的操作
def sonRun(num):
    print('子进程-%d-启动--%s' % (num, os.getpid()))
    start = time.time()
    time.sleep(random.choice([1, 2, 3]))
    end = time.time()
    print('子进程-%d-结束--%s--耗时--%.2f' % (num, os.getpid(), end - start))


if __name__ == '__main__':
    print('父进程启动')

    # 创建多个进程
    # 进程池
    # 表示可以同时执行的进程数量
    # Pool默认大小是CPU核心数
    pool = Pool(2)
    for i in range(3):
        # 创建进程放进进程池统一管理
        pool.apply_async(sonRun, args=(i, ))


    # 如果用的是进程池, 在调用join之前必须先调用close,调用close之后就不能再继续添加新的进程了
    pool.close()
    # 进程池对象调用join，会等待进程池中所有的子进程结束完毕再去执行父进程
    pool.join()


    print('父进程结束')






