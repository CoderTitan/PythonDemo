# 主窗口
from tkinter import *

# 创建主窗口
window = Tk()

# 设置标题
window.title('Titanjun')

# 设置窗口大小
window.geometry('400x400')


# 某个鼠标按键在控件上被点击
def buttonAction(event):
    print(event.x, event.y)

button = Button(window, text='这是一个按钮')
button.bind('<Button-4>', buttonAction)
button.pack()

'''
#<Button-1>鼠标左键
#<Button-3>鼠标右键
#<Button-2>鼠标中键
#<Button-4>向上滚动
#<Button-5>向下滚动
#<Double-Button-1>鼠标左键双击
#<Double-Button-3>鼠标右键双击
#<Double-Button-2>鼠标中键双击
#<Triple-Button-1>鼠标左键三击
#<Triple-Button-3>鼠标右键三击
#<Triple-Button-2>鼠标中键三击
'''


# 鼠标在某个按键被按下时的移动事件
label = Label(window, text='https://www.titanjun.top', bg='orange')
label.place(x=100, y=50, height=30)

def labelAction(event):
    print(event.x, event.y)
label.bind('<B1-Motion>', labelAction)

'''
#<B1-Motion>左键移动
#<B3-Motion>右键移动
#<B2-Motion>中键移动
'''


# 按钮点击释放事件
label2 = Label(window, text='博客地址: https://www.titanjun.top', bg='orange')
label2.place(x=100, y=100, height=30)
label2.bind('<ButtonRelease-1>', labelAction)

'''
#<ButtonRelease-1>释放鼠标左键
#<ButtonRelease-3>释放鼠标右键
#<ButtonRelease-2>释放鼠标中键
'''



# 按钮点击释放事件
label3 = Label(window, text='加油: https://www.titanjun.top', bg='yellow')
label3.place(x=100, y=150, height=30)
label3.bind('<Leave>', labelAction)

'''
#<Enter>鼠标光标进入控件时触发
#<Leave>鼠标光标离开控件时触发
'''




# 进入消息循环
window.mainloop()
