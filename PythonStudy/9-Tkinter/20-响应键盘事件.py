# 主窗口
from tkinter import *

# 创建主窗口
window = Tk()

# 设置标题
window.title('Titanjun')

# 设置窗口大小
window.geometry('400x400')


# 响应所有的按键
label = Label(window, text='https://www.titanjun.top', bg='orange')
# 设置焦点
label.focus_set()
label.place(x=100, y=50, height=30)

def labelAction(event):
    print(event.char, event.keycode)
label.bind('<b>', labelAction)



# 响应所有的按键
label2 = Label(window, text='https://www.titanjun.top', bg='yellow')
# 设置焦点
label2.focus_set()
label2.place(x=100, y=100, height=30)
label2.bind('<KeyRelease-a>', labelAction)



# 进入消息循环
window.mainloop()
