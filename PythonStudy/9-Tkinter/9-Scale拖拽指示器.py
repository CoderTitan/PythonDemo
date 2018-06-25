# 主窗口
from tkinter import *

# 创建主窗口
window = Tk()

# 设置标题
window.title('Titanjun')

# 设置窗口大小
window.geometry('400x400')


'''
供用户通过拖拽指示器改变变量的值，可以水平，也可以竖直
tkinter.HORIZONTAL  水平
tkinter.VERTICAL   竖直
length 水平时表示宽度，竖直时表示高度
tickinterval  选择值将会为该值的倍数
'''

scale = Scale(window, from_ = 0, to = 10, orient = HORIZONTAL, length = 200, label='choice:', digits = 2)
scale.pack()

# 设置初始值
# scale.set(34)

# 取值
def showNumber(event):
    print(scale.get())

scale["command"] = showNumber



# 进入消息循环
window.mainloop()
