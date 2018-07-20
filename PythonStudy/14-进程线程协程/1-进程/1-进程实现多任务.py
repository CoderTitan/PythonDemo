'''

对于操作系统而言，一个任务就是一个进程

进程是系统中程序执行和资源分配的基本单位。每个进程都有自己的数据段、代码段、和堆栈段


multiprocessing 库
跨平台版本的多进程模块，提供了一个Process类来代表一个进程对象
'''

from multiprocessing import Process
import time, os


# 紫禁城需要执行的代码
def sonRun(str):
    while True:
        # getpid: 获取当前进程的id号
        # getppid: 获取当前进程的父进程的id号
        print('%s--%s--%s' % (str, os.getpid(), os.getppid()))
        time.sleep(1.2)


if __name__ == '__main__':
    print('主(父)进程启动--%s' % (os.getpid()))

    # c创建子进程
    # target: 说明进程执行的函数操作
    pro = Process(target=sonRun, args=('titan', ))
    # 启动进程
    pro.start()

    while True:
        print('beautiful, titan')
        time.sleep(1)