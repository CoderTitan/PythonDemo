
from multiprocessing import Process
import time, os



def sonRun(str):
    print('子进程启动')
    time.sleep(3)
    print('子进程结束')


if __name__ == '__main__':
    print('父进程启动')
    pro = Process(target=sonRun, args=('titan', ))
    pro.start()

    # 父进程结束不能影响子进程, 让父进程等待子进程结束在执行父进程
    pro.join()
    print('父进程结束')






