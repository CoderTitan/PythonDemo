# 主窗口
from tkinter import *

# 创建主窗口
window = Tk()

# 设置标题
window.title('Titanjun')

# 设置窗口大小
# window.geometry('400x400')

'''
列表框控件，可以包含一个或者多个文本框
作用：在listbox控件的小窗口显示一个字符串

'''

'''
# 创建一个listbox, 添加几个元素
# SINGLE:
# BROWSE:
# MULTIPLE:
# EXTENDED:
lb = Listbox(window, selectmode = EXTENDED)
lb.pack()

for item in ["good", "nice", "handsome", "vg", "vn"]:
    # 按顺序添加
    lb.insert(END, item)
# 在开始位置添加
lb.insert(ACTIVE, 'Titn')
# 在最后添加
lb.insert(END, 'jun')
# 在具体的索引出添加元素
lb.insert(2, 'lululu')
# 把列表当成一个元素添加
lb.insert(ACTIVE, [1, 2, 3])
# 添加元组
lb.insert(ACTIVE, ('che', '09'))

#删除  参数1为开始的索引，参数2为结束的索引，如果不指定参数2，只删除第一个索引处的内容
# lb.delete(1, 2)
# lb.delete(1)

#选中   参数1为开始的索引，参数2为结束的索引，如果不指定参数2，只选中第一个索引处的内容
lb.selection_set(2, 5)
lb.selection_set(0)

# 取消
lb.selection_clear(3, 4)
lb.selection_clear(0)

#获取到列表中的元素的个数
print(lb.size())

#从列表中取值  参数1为开始的索引，参数2为结束的索引，如果不指定参数2，只获取第一个索引处的内容
print(lb.get(1, 3))
print(lb.get(5))

#返回当前的索引项，不是item元素
print(lb.curselection())

# 判断某选项是否被选中
print(lb.selection_includes(3))
print(lb.selection_includes(5))
'''

'''
# 绑定变量
lbv = StringVar()
lb = Listbox(window, selectmode = SINGLE, listvariable = lbv)
lb.pack()

for item in ["good", "nice", "handsome", "jun", "titan"]:
    lb.insert(END, item)


# 打印当前列表中的选项
print(lbv.get())
print(lb.get(1))

# 设置选项(所有重新赋值)
# lbv.set((1, 2, 3))


# 绑定事件
def listboxAction(event):
    print(lb.get(lb.curselection()))

# 1代表鼠标左键
lb.bind('<Double-Button-1>', listboxAction)
'''



# 滚动
lb = Listbox(window, selectmode=EXTENDED)
for item in ["good", "nice", "handsome", "from", "thinter","good1", "nice1", "handsome1", "vg1", "vn1","good3", "nice3", "handsome3", "vg3", "vn3"]:
    lb.insert(END, item)

# 滚动条
sc = Scrollbar(window)
sc.pack(side = RIGHT, fill = Y)
lb.configure(yscrollcommand = sc.set)
lb.pack(side = LEFT, fill = BOTH)
# 额外给属性赋值
sc["command"] = lb.yview








# 进入消息循环
window.mainloop()
