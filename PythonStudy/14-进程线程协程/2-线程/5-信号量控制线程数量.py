


import threading, time

# 控制可同时执行的线程的个数
sem = threading.Semaphore(3)

def threadRun():
    with sem:
        for i in range(5):
            print('%s--%d' % (threading.current_thread().name, i))
            time.sleep(1)



if __name__ == '__main__':
    for i in range(5):
        threading.Thread(target=threadRun).start()



