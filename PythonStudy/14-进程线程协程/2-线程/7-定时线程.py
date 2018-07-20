import threading

def run():
    print('titanjun')


# 延迟线程的执行
thread = threading.Timer(5, run)
thread.start()

# 等待线程执行完才执行后面的
thread.join()

print('父线程结束')