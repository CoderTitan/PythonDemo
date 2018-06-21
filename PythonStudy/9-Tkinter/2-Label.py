# 主窗口
import tkinter
from PIL import Image
from PIL import ImageTk

# 创建主窗口
window = tkinter.Tk()

# 设置标题
window.title('Titanjun')

# 设置窗口大小
window.geometry('400x400')


'''Label: 显示文本
#win  父窗体
#text  显示的文本内容
#bg    背景色
#fg    字体颜色
#wraplength  指定text文本中多宽进行换行
#justify  设置换行后的对齐方法
#anchor   位置  n北  e东  s南  w西  center居中  ne   se   sw   nw

'''

label = tkinter.Label(window,
                      text="我是一只小鸭子",
                      bg='#999999',
                      fg='white',
                      font=('黑体', 13),
                      justify='center',
                      height=5,
                      width=30,
                      anchor='n',
                      # wraplength=30
                      underline=3,
                      bd=3,
                      relief='flat'
                      )
label.pack()

# label显示图片
image = Image.open('头像.png')
image = ImageTk.PhotoImage(image)
label1 = tkinter.Label(window, image=image, bg='#aaaaaa')
label1.pack()



# 进入消息循环
window.mainloop()
