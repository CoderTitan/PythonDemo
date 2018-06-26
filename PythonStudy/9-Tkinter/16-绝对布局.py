# 主窗口
from tkinter import *

# 创建主窗口
window = Tk()

# 设置标题
window.title('Titanjun')

# 设置窗口大小
window.geometry('400x400')


#绝对布局,窗口的变化对位置没有影响
# 创建四个label
label1 = Label(window, text='11111', bg='red')
label2 = Label(window, text='22222', bg='yellow')
label3 = Label(window, text='33333', bg='blue')
label4 = Label(window, text='44444', bg='orange')


# 绝对布局
label1.place(x=10, y=10, width=200)
label2.place(x=30, y=30)
label3.place(x=60, y=61)
label4.place(x=91, y=91, width=200, height=50)



# 进入消息循环
window.mainloop()
