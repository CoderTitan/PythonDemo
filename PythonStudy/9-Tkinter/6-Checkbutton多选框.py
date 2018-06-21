# 主窗口
from tkinter import *

# 创建主窗口
window = Tk()

# 设置标题
window.title('Titanjun')

# 设置窗口大小
window.geometry('400x400')

def update():
    message = ''
    if tag1.get() == True:
        message += 'titan \n'
    if tag2.get() == True:
        message += 'jun \n'
    if tag3.get() == True:
        message += 'coder \n'

    #清楚text中的所有内容
    text.delete(0.0, END)
    text.insert(INSERT, message)

# 要绑定的变量
tag1 = BooleanVar()
check1 = Checkbutton(window, text = 'Titan', variable = tag1, command = update)
check1.pack()

tag2 = BooleanVar()
check2 = Checkbutton(window, text = 'Juned', variable = tag2, command = update)
check2.pack()

tag3 = BooleanVar()
check3 = Checkbutton(window, text = 'Coder', variable = tag3, command = update)
check3.pack()


text = Text(window, bg = 'orange', width = 50, height = 5)
text.pack()


















# 进入消息循环
window.mainloop()
