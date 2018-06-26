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

# 定义列title(接受一个元组)
tree["columns"] = ('name', 'sex', 'age', 'height', 'weight')

# 设置列宽度
tree.column('name', width=100)
tree.column('sex', width=50)
tree.column('age', width=50)
tree.column('height', width=80)
tree.column('weight', width=80)

# 设置表头(列名)
tree.heading('name', text='姓名')
tree.heading('sex', text='性别')
tree.heading('age', text='年龄')
tree.heading('height', text='身高(CM)')
tree.heading('weight', text='体重(KG)')

# 添加数据
tree.insert('', 0, text='line1', values=('Titan', 'M', 20, 180, 80))
tree.insert('', 1, text='line2', values=('Jun', 'M', 19, 170, 65))
tree.insert('', 2, text='line3', values=('Coder', 'M', 20, 170, 70))
tree.insert('', 3, text='line4', values=('Che', 'W', 18, 165, 45))

# 上面第一个参数为第一层级, 这里目前用不到, 后面树状结构中会用到



# 进入消息循环
window.mainloop()
