'''

# 主窗口
import tkinter

def action1():
    print('按钮1')



# 创建主窗口
window = tkinter.Tk()

# 设置标题
window.title('Titanjun')

# 设置窗口大小
window.geometry('400x400')


# 创建按钮
button1 = tkinter.Button(window,
                         text='按钮1',
                         bg='orange',
                         height=3,
                         width=20,
                         bd=3,
                         relief='sunken',
                         activebackground='orange',
                         activeforeground='white',
                         command=action1
                         )
button1.pack()


button2 = tkinter.Button(window, text='Titanjun', height=3, command=window.quit(), highlightcolor='red')
button2.pack()

'''

from tkinter import *

window = Tk()
window.title('Titanjun')

# 设置窗口大小
window.geometry('400x400')


button1 = Button(window, text='text1', width=30, height=3)
button1.pack()



# 进入消息循环
window.mainloop()



'''
activebackground
当鼠标放上去时，按钮的背景色

2	
activeforeground
当鼠标放上去时，按钮的前景色

3	
bd
按钮边框的大小，默认为 2 个像素

4	
bg
按钮的背景色

5	
command
按钮关联的函数，当按钮被点击时，执行该函数

6	
fg
按钮的前景色（按钮文本的颜色）

7	
font
文本字体

8	
height
按钮的高度

9	
highlightcolor
要高亮的颜色

10	
image
按钮上要显示的图片

11	
justify
显示多行文本的时候,设置不同行之间的对齐方式，可选项包括LEFT, RIGHT, CENTER

12	
padx
按钮在x轴方向上的内边距(padding)，是指按钮的内容与按钮边缘的距离

13	
pady
按钮在y轴方向上的内边距(padding)

14	
relief
边框样式，设置控件3D效果，可选的有：FLAT、SUNKEN、RAISED、GROOVE、RIDGE。默认为 FLAT。

15	
state
设置按钮组件状态,可选的有NORMAL、ACTIVE、 DISABLED。默认 NORMAL。

16	
underline
下划线。默认按钮上的文本都不带下划线。取值就是带下划线的字符串索引，为 0 时，第一个字符带下划线，为 1 时，前两个字符带下划线，以此类推

17	
width
按钮的宽度，如未设置此项，其大小以适应按钮的内容（文本或图片的大小）

18	
wraplength
限制按钮每行显示的字符的数量

19	
text
按钮的文本内容

19	
anchor
锚选项，控制文本的位置，默认为中心
'''