# 主窗口
from tkinter import *
from tkinter import ttk

# 创建主窗口
window = Tk()

# 设置标题
window.title('Titanjun')

# 设置窗口大小
window.geometry('400x400')


# 创建表格
tree = ttk.Treeview(window)
tree.pack()

# 添加一级树枝
treeA1 = tree.insert('', 0, '浙', text='浙江', values=('A1'))
treeA2 = tree.insert('', 1, '鲁', text='山东', values=('A2'))
treeA3 = tree.insert('', 2, '苏', text='江苏', values=('A3'))

# 添加二级树枝
treeA1_1 = tree.insert(treeA1, 0, 'H', text='杭州', values=('A1_1'))
treeA1_2 = tree.insert(treeA1, 1, 'Z', text='舟山', values=('A1_2'))
treeA1_3 = tree.insert(treeA1, 2, 'J', text='嘉兴', values=('A1_3'))

treeA2_1 = tree.insert(treeA2, 0, 'N', text='济南', values=('A2_1'))
treeA2_2 = tree.insert(treeA2, 1, 'L', text='临沂', values=('A2_2'))
treeA2_3 = tree.insert(treeA2, 2, 'Q', text='青岛', values=('A2_3'))
treeA2_4 = tree.insert(treeA2, 3, 'Y', text='烟台', values=('A2_4'))


# 三级树枝
treeA1_1_1 = tree.insert(treeA1_1, 0, 'G', text='江干', values=('A1_1_1'))
treeA1_1_1 = tree.insert(treeA1_1, 1, 'X', text='萧山', values=('A1_1_2'))



# 进入消息循环
window.mainloop()
