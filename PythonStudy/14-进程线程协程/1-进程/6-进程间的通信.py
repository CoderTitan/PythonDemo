from multiprocessing import Process, Queue
import time, os


def write(q):
    print('启动写进程%s' % os.getpid())
    for chr in ["A", "B", "C", "D"]:
        q.put(chr)
        time.sleep(1)
    print('结束写子进程%s' % os.getpid())

def read(q):
    print('启动读子进程%s' % os.getpid())
    while True:
        value = q.get(True)
        print('value=' + value)

    print('结束读子进程%s' % os.getpid())


if __name__ == '__main__':
    # 父进程创建队列并传递给子进程
    queue = Queue()
    pw = Process(target=write, args=(queue, ))
    pr = Process(target=read, args=(queue, ))

    pw.start()
    pr.start()

    pw.join()
    # pr进程里是个死循环，无法等待其结束，只能强行结束
    pr.terminate()

    print('父进程结束')


