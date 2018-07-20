'''

在一个进程的内部，要同时干多件事，就需要同时运行多个“子任务”，我们把进程内的这些“子任务”叫做线程


线程通常叫做轻型的进程。线程是共享内存空间的并发执行的多任务，每一个线程都共享一个进程的资源

线程是最小的执行单元，而进程由至少一个线程组成。如何调度进程和线程，完全由操作系统绝对，程序自己不能决定什么时候执行，执行多长时间


模块
1、_thread模块       低级模块 底层模块(c语言)
2、threading模块     高级模块，对_thread进行了封装

'''


import threading, time

def run(num):
    print('子线程%s开始' %  threading.current_thread().name)

    #实现线程功能
    time.sleep(2)
    print('num = ', num)
    time.sleep(2)

    print('子线程%s结束' % threading.current_thread().name)

if __name__ == '__main__':
    # 任何进程默认就会启动一个线程，称为主线程，主线程可以启动新的子线程
    # current_thread()：返回返回当前线程的实例
    # threading.current_thread().name: 打印当前线程的名称
    print('主线程%s启动' % threading.current_thread().name)

    # 创建子线程
    # target: 指定线程要执行的代码, name: 线程的名称
    thread = threading.Thread(target=run, name='sonThread', args=(2, ))
    # 开启线程
    thread.start()

    #等待线程结束
    thread.join()

    print('主 线程%s结束' % threading.current_thread().name)

















