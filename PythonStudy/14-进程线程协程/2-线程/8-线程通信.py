
import threading, time

def action():
    # 事件对象
    event = threading.Event()

    def run():
        for i in range(5):
            # 阻塞, 等待事件的触发
            event.wait()
            # 重置
            event.clear()

            print('titanjun--%d' % i)


    thread = threading.Thread(target=run).start()
    return event

eve = action()


# 触发事件
for i in range(5):
    time.sleep(2)
    eve.set()









