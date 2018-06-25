# 主窗口
from tkinter import *

# 创建主窗口
window = Tk()

# 设置标题
window.title('Titanjun')

# 设置窗口大小
window.geometry('400x400')


'''
数值范围控件
'''

# 绑定变量
spinStr = StringVar()

# 事件监听
def updateAction():
    # 在最后拼接上'12'
    # spin1.insert(END, 12)
    print(spinStr.get())

'''属性介绍
from_: 起始值
to: 最大值
increment: 步长
textvariable: 绑定变量
command: 绑定函数, 事件监听
values: 设置后, 每次更新值将使用values指定的值
'''
# spin = Spinbox(window, from_ = 0, to = 100, increment = 10, textvariable = spinStr, command = updateAction)
# spin.pack()

spin1 = Spinbox(window, values=[0, 10, 30, 50, 80, -9], increment = 10, textvariable = spinStr, command = updateAction, bg='red')
spin1.pack()


# 进入消息循环
window.mainloop()
