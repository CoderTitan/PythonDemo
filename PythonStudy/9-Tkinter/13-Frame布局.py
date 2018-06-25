# 主窗口
from tkinter import *

# 创建主窗口
window = Tk()

# 设置标题
window.title('Titanjun')

# 设置窗口大小
window.geometry('400x400')


'''
框架控件
在屏幕上显示一个矩形区域，多作为容器控件
'''

# 第一层容器
frame = Frame(window)
frame.pack()

# 左边容器
leftFrame = Frame(frame)
Label(leftFrame, text='左上位置', bg='red', height=5, width=10).pack(side=TOP)
Label(leftFrame, text='左下位置', bg='yellow', height=5, width=10).pack(side=TOP)
leftFrame.pack(side=LEFT)

# 右边容器
rightFrame = Frame(frame)
Label(rightFrame, text='右上位置', bg='orange', height=5, width=10).pack(side=TOP)
Label(rightFrame, text='右下位置', bg='blue', height=5, width=10).pack(side=TOP)
rightFrame.pack(side=RIGHT)









# 进入消息循环
window.mainloop()
