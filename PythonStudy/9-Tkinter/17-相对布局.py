# 主窗口
from tkinter import *

# 创建主窗口
window = Tk()

# 设置标题
window.title('Titanjun')

# 设置窗口大小
window.geometry('400x400')




# 创建四个label
label1 = Label(window, text='11111', bg='red')
label2 = Label(window, text='22222', bg='yellow')
label3 = Label(window, text='33333', bg='blue')
label4 = Label(window, text='44444', bg='orange')


# 布局
label1.pack(side=LEFT, fill=Y)
label2.pack(side=RIGHT, fill=Y)
label3.pack(side=TOP, fill=X)
label4.pack(side=BOTTOM, fill=X)









# 进入消息循环
window.mainloop()
