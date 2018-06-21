


# 多行文本
from tkinter import *

# 创建主窗口
window = Tk()

# 设置标题
window.title('Titanjun')

# 设置窗口大小
window.geometry('400x400')


'''
text = Text(window, bg='yellow', width=40, height=10)
#INSERT索引表示在光标处插入
text.insert(INSERT, 'I Love')
#END索引号表示在最后插入
text.insert(END, ' you')
text.pack()

text.insert(INSERT, '自定义标签的名字')
#第一个参数为自定义标签的名字
#第二个参数为设置的起始位置，第三个参数为结束位置
#第四个参数为另一个位置
text.tag_add('tag1', '1.7', '1.12', '1.14')
#用tag_config函数来设置标签的属性
text.tag_config('tag1', font=17, background='blue', foreground='red')
# text.tag_config('tag1', bg='yellow', fg='red')
#新的tag会覆盖旧的tag
'''

'''
def show():
    print('好了, 你赢了')


# text还可以插入按钮  图片等
b1 = Button(text, text='点我点我', command=show)
# 在text创建组件的命令
text.window_create(INSERT, window=b1)
'''



text = Text(window, bg='yellow', width=100, height=10)
# 添加右侧滚动条
scroll = Scrollbar()
# side放到窗体的那一侧   fill填充
scroll.pack(side=RIGHT, fill=Y)
text.pack(side=RIGHT, fill=Y)
# 两者关联
scroll.config(command=text.yview)
text.config(yscrollcommand=scroll.set)

str = '''致橡树--舒婷
我如果爱你——
绝不像攀援的凌霄花，
借你的高枝炫耀自己；
我如果爱你——
绝不学痴情的鸟儿，
为绿荫重复单调的歌曲；
也不止像泉源，
常年送来清凉的慰藉；
也不止像险峰，
增加你的高度，
衬托你的威仪。
甚至日光，
甚至春雨。
不，
这些都还不够！
我必须是你近旁的一株木棉，
作为树的形象和你站在一起。
根，
紧握在地下；
叶，
相触在云里。
每一阵风过，
我们都互相致意，
但没有人，
听懂我们的言语。
你有你的铜枝铁干，
像刀，
像剑，
也像戟；
我有我红硕的花朵，
像沉重的叹息，
又像英勇的火炬。
我们分担寒潮、
风雷、
霹雳；
我们共享雾霭、
流岚、
虹霓。
仿佛永远分离，
却又终身相依。
这才是伟大的爱情，
坚贞就在这里：
爱——
不仅爱你伟岸的身躯，
也爱你坚持的位置，
足下的土地。
'''

text.insert(INSERT, str)





# 进入消息循环
window.mainloop()
