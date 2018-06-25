# 主窗口
from tkinter import *

# 创建主窗口
window = Tk()

# 设置标题
window.title('Titanjun')

# 设置窗口大小
window.geometry('400x400')

'''
def menuAction1():
    print('menubar')

# 菜单条
menubar = Menu(window)
window.configure(menu=menubar)


# 创建一个菜单选项
menu1 = Menu(menubar, tearoff=False)
# 菜单选项添加内容
for item in ['Python', 'PHP', 'CPP', 'C', 'Java', 'JavaScript', 'VBScript', 'Exit']:
    if item == 'Exit':
        # 添加分割线
        menu1.add_separator()
        menu1.add_command(label=item, command=window.quit)
    else:
        menu1.add_command(label=item, command=menuAction1)

# 想菜单条上添加菜单选项
menubar.add_cascade(label='语言', menu=menu1)


# 菜单2的事件处理
def menuAction2():
    print(menuStr.get())

menuStr = StringVar()

menu2 = Menu(menubar, tearoff=True)
for item in ['red', 'orange', 'blue', 'gray']:
    menu2.add_radiobutton(label=item, variable=menuStr, command=menuAction2)
# 添加到菜单列表
menubar.add_cascade(label='颜色', menu=menu2)

'''



# 鼠标右键菜单
menubar2 = Menu(window)

menu3 = Menu(menubar2, tearoff=False)
for item in ['Python', 'PHP', 'CPP', 'C', 'Java', 'JavaScript', 'VBScript', 'Exit']:
    menu3.add_command(label=item)

menubar2.add_cascade(label='开发语言', menu=menu3)




# 添加/删除菜单
def menuClick():
    print("menu3")

# 添加command项
menu3.insert_command(1, label='command', command=menuClick)

# 添加radiobutton项
menu3.insert_radiobutton(3, label='radiobutton', command=menuClick)

# 添加checkbutton项
menu3.insert_checkbutton(5, label='checkbutton', command=menuClick)

# 添加分割线
menu3.insert_separator(4)
# menu3.insert_separator(0)


# 删除
# 两个参数: 参数1为开始的索引，参数2为结束的索引，如果不指定参数2，只获取第一个索引处的内容
menu3.delete(2, 4)
menu3.delete(0)





# 用于显示菜单
def showMenu(event):
    print('window')
    # 鼠标点击处的坐标
    menubar2.post(event.x_root, event.y_root)

# window绑定鼠标事件
window.bind("<Button-2>", showMenu)




# 进入消息循环
window.mainloop()
