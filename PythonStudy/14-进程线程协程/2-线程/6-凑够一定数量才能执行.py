import threading, time


# 控制需要累计的线程的个数
bar = threading.Barrier(3)

def threadRun():
    print('%s--start' % threading.current_thread().name)
    time.sleep(1)
    bar.wait()
    print('%s--end' % threading.current_thread().name)


if __name__ == '__main__':
    for i in range(5):
        threading.Thread(target=threadRun).start()