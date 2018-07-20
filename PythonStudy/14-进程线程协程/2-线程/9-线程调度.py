
import threading, time

# 线程条件变量
cond = threading.Condition()

def run1():
    with cond:
        for i in range(0, 10, 2):
            print(threading.current_thread().name, i)
            time.sleep(1)
            cond.wait()
            # 通知其他线程的操作
            cond.notify()


def run2():
    with cond:
        for i in range(1, 10, 2):
            print(threading.current_thread().name, i)
            time.sleep(1)
            # 通知其他线程可以进行操作
            cond.notify()
            # 等待
            cond.wait()


threading.Thread(target=run1).start()
threading.Thread(target=run2).start()




