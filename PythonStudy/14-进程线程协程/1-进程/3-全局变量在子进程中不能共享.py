from multiprocessing import Process
import time

# 定义一个全局变量
num = 100

# 子进程执行的操作
def sonRun():
    print('子进程启动')
    global num
    num += 1
    print(num)
    print('子进程结束')


if __name__ == '__main__':
    print('父进程启动')

    # 创建子进程
    pro = Process(target=sonRun)
    # 启动进程
    pro.start()
    # 等待子进程执行
    pro.join()


    # 在子进程中欧修改全局变量对父进程中的全局变量没有影响
    # 在创建子进程时对全局变量做了一个备份，父进程中的与子进程中的num是完全不同的两个变量
    print('父进程结束--%d' % num)