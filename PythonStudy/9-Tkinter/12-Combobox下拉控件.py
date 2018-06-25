# 主窗口
from tkinter import *
from tkinter import ttk

# 创建主窗口
window = Tk()

# 设置标题
window.title('Titanjun')

# 设置窗口大小
window.geometry('400x400')



# 绑定变量
cv = StringVar()
combo = ttk.Combobox(window, textvariable=cv)
combo.pack()

# 设置下拉菜单数据(元组数据)
combo['value'] = ('杭州', '湖州', '温州', '嘉兴', '舟山')

# 设置默认值
combo.current(0)

# 绑定事件
def comboboxClick(event):
    print(cv.get())
    print(combo.get())

combo.bind('<<ComboboxSelected>>', comboboxClick)





# 进入消息循环
window.mainloop()
