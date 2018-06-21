
# 主窗口
from tkinter import *

# 创建主窗口
window = Tk()

# 设置标题
window.title('Titanjun')

# 设置窗口大小
window.geometry('400x400')



# 进入消息循环
window.mainloop()


'''
# 除此之外的方法
# 框体大小的可调性, 分别表示x, y方向的可变性
window.resizable(0, 0)
# 退出
window.quit()

# 刷新页面
window.update()
'''