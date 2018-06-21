
# 主窗口
from tkinter import *

# 创建主窗口
window = Tk()

# 设置标题
window.title('Titanjun')

# 设置窗口大小
window.geometry('400x400')


def selectorAction():
    print(tag.get())

# 一组单选框要绑定同一个变量
tag = IntVar()
radio1 = Radiobutton(window, text = 'one', value = 23, variable = tag, command = selectorAction)
radio1.pack()
radio2 = Radiobutton(window, text = 'two', value = 32, variable = tag, command = selectorAction)
radio2.pack()
radio3 = Radiobutton(window, text = 'ten', value = 10, variable = tag, command = selectorAction)
radio3.pack()



# 进入消息循环
window.mainloop()
