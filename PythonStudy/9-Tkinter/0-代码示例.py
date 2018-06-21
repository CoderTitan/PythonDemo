# 主窗口
from tkinter import *

# 创建主窗口
window = Tk()

# 设置标题
window.title('Titanjun')

# 设置窗口大小
window.geometry('400x400')


text = Text(window, bg='yellow', width=30, height=5)
text.pack()





# 进入消息循环
window.mainloop()
